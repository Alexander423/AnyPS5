import argparse
import datetime
import json
import os
import pathlib
import urllib.error
import urllib.request


def fetch(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "AnyPS5-fork-audit"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=45) as response:
        return json.load(response), response.headers.get("Link", "")


def next_page(link):
    for part in link.split(","):
        if 'rel="next"' in part:
            url = part.split(";")[0].strip().strip("<>")
            if not url.startswith("https://api.github.com/"):
                raise ValueError("Unexpected pagination host")
            return url
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=pathlib.Path, required=True)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    result = {"observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "complete": False,
              "scope": "GitHub upstream forks endpoint; branch and patch review tracked separately", "forks": [], "errors": []}
    url = "https://api.github.com/repos/boykopovar/AnyPS5/forks?per_page=100&sort=oldest"
    seen = set()
    if args.resume and args.output.exists():
        result = json.loads(args.output.read_text(encoding="utf-8"))
        if result["complete"]:
            return 0
        url = result.get("resume_url") or url
        if not url.startswith("https://api.github.com/"):
            raise ValueError("Unexpected resume host")
        seen = {repo["id"] for repo in result["forks"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        while url:
            data, link = fetch(url)
            for repo in data:
                if repo["id"] not in seen:
                    seen.add(repo["id"])
                    result["forks"].append({key: repo.get(key) for key in
                        ("id", "full_name", "html_url", "default_branch", "pushed_at", "archived", "disabled", "forks_count", "license")})
            url = next_page(link)
            result["resume_url"] = url
            args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            print(f"Collected {len(seen)} forks", flush=True)
        result["complete"] = True
    except (urllib.error.URLError, ValueError) as error:
        headers = getattr(error, "headers", {})
        result["resume_url"] = url
        result["errors"].append({"url": url, "error": str(error), "status": getattr(error, "code", None),
                                 "rate_limit_reset": headers.get("X-RateLimit-Reset"), "retry_after": headers.get("Retry-After")})
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
