import argparse
import concurrent.futures
import json
import os
import pathlib
import subprocess


def git(*args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
    result = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120, env=env)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def branches(repo):
    try:
        text = git("ls-remote", "--heads", repo["html_url"] + ".git")
        return repo["full_name"], {"branches": [dict(zip(("sha", "ref"), line.split("\t"))) for line in text.splitlines()], "error": None}
    except (RuntimeError, subprocess.TimeoutExpired) as error:
        return repo["full_name"], {"error": str(error)}


def compare(base, ref):
    result = {"ref": ref, "sha": git("rev-parse", ref)}
    try:
        result["merge_base"] = git("merge-base", base, ref)
        result["behind"], result["ahead"] = map(int, git("rev-list", "--left-right", "--count", base + "..." + ref).split())
        result["commits"] = git("log", "--format=%H%x09%an%x09%aI%x09%s", base + ".." + ref).splitlines()
        result["changed_files"] = git("diff", "--name-only", base + "..." + ref).splitlines()
        result["patch_equivalence"] = git("cherry", base, ref).splitlines() if result["ahead"] else []
    except (RuntimeError, subprocess.TimeoutExpired) as error:
        result["error"] = str(error)
    return result


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=pathlib.Path)
    parser.add_argument("--acquire", type=pathlib.Path)
    parser.add_argument("--refs", default="refs/remotes/audit-")
    parser.add_argument("--base", default="upstream/main")
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    if args.acquire:
        inventory = json.loads(args.acquire.read_text(encoding="utf-8"))
        results = {}
        for name, value in inventory.items():
            tips = [branch["sha"] for branch in value.get("branches", [])]
            if not tips:
                results[name] = {"status": "unavailable", "error": value.get("error")}
                continue
            checked = subprocess.run(["git", "cat-file", "--batch-check=%(objecttype)"],
                                     input="\n".join(tips) + "\n", capture_output=True, text=True, check=True)
            if all(line == "commit" for line in checked.stdout.splitlines()):
                results[name] = {"status": "objects_present"}
                continue
            try:
                git("-c", "gc.auto=0", "fetch", "--no-tags", "--no-write-fetch-head",
                    "https://github.com/" + name + ".git",
                    "+refs/heads/*:refs/remotes/ecosystem-" + name.split("/")[0] + "/*")
                results[name] = {"status": "fetched"}
            except (RuntimeError, subprocess.TimeoutExpired) as error:
                results[name] = {"status": "error", "error": str(error)}
            save(args.output, results)
            print(name, results[name]["status"], flush=True)
        save(args.output, results)
    elif args.inventory:
        repos = json.loads(args.inventory.read_text(encoding="utf-8"))["forks"]
        results = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            for name, value in pool.map(branches, repos):
                results[name] = value
                if len(results) % 100 == 0:
                    save(args.output, results)
                    print(len(results), flush=True)
        save(args.output, results)
    else:
        base = git("rev-parse", args.base)
        refs = git("for-each-ref", "--format=%(refname)", "refs/remotes").splitlines()
        results = {"upstream": base, "branches": []}
        for ref in refs:
            if ref.startswith(args.refs):
                results["branches"].append(compare(base, ref))
                save(args.output, results)
                print(ref, flush=True)


if __name__ == "__main__":
    main()
