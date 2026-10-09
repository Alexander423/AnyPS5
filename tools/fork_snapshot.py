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
    metadata = {}
    for line in git("log", "--all", "--format=%H%x09%an%x09%aI%x09%s", "^" + base).splitlines():
        sha, author, date, subject = line.split("\t", 3)
        metadata[sha] = {"author": author, "author_date": date, "subject": subject}
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
            row["subsystems"] = sorted({"/".join(path.split("/")[:4 if path.startswith("core/libs/prx/") else 2]) for path in row["changed_files"]})
            row["license_files_changed"] = [path for path in row["changed_files"] if "license" in path.lower() or "copying" in path.lower()]
            row["test_files_changed"] = [path for path in row["changed_files"] if "test" in path.lower()]
            row["runtime_validation"] = "NOT_TESTED"
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            row["error"] = str(error)
        result["tips"][tip] = row
        if len(result["tips"]) % 100 == 0:
            save(args.output, result)
            print(len(result["tips"]), flush=True)
    result["complete"] = all("error" not in row for row in result["tips"].values())
    result["patch_ids"] = community
    result["commit_metadata"] = metadata
    save(args.output, result)


if __name__ == "__main__":
    main()
