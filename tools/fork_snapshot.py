import argparse
import json
import pathlib
import subprocess

from fork_branch_audit import git, save


def patch_ids(revisions):
    command = ["git", "log", "--no-merges", "--pretty=format:%H", "-p", *revisions]
    with subprocess.Popen(command, stdout=subprocess.PIPE) as producer:
        result = subprocess.run(["git", "patch-id", "--stable"], stdin=producer.stdout,
                                capture_output=True, text=True, check=True)
        producer.stdout.close()
        if producer.wait() != 0:
            raise RuntimeError("Patch production failed")
    return {commit: patch for patch, commit in (line.split() for line in result.stdout.splitlines())}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("branches", type=pathlib.Path)
    parser.add_argument("--base", default="upstream/main")
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    branches = json.loads(args.branches.read_text(encoding="utf-8"))
    base = git("rev-parse", args.base)
    upstream = set(patch_ids([base]).values())
    community = patch_ids(["--all", "^" + base])
    result = {"upstream": base, "method": "merge-base, ancestry counts, stable patch-id, file diffs; not semantic validation",
              "tips": {}, "repositories": branches}
    tips = sorted({branch["sha"] for repo in branches.values() for branch in repo.get("branches", [])})
    for tip in tips:
        row = {"sha": tip}
        try:
            row["merge_base"] = git("merge-base", base, tip)
            row["behind"], row["ahead"] = map(int, git("rev-list", "--left-right", "--count", base + "..." + tip).split())
            row["last_commit"] = git("show", "-s", "--format=%aI%x09%cI%x09%an%x09%s", tip)
            row["unique_commits"] = git("rev-list", "--no-merges", base + ".." + tip).splitlines()
            row["patch_equivalent_upstream"] = [commit for commit in row["unique_commits"] if community.get(commit) in upstream]
            row["changed_files"] = git("diff", "--name-only", row["merge_base"], tip).splitlines()
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            row["error"] = str(error)
        result["tips"][tip] = row
        if len(result["tips"]) % 100 == 0:
            save(args.output, result)
            print(len(result["tips"]), flush=True)
    result["complete"] = all("error" not in row for row in result["tips"].values())
    result["patch_ids"] = community
    save(args.output, result)


if __name__ == "__main__":
    main()
