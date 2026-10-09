import argparse
import datetime
import hashlib
import json
import pathlib
import platform
import subprocess
import time


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def relink(relinker, source, output, expected, timeout):
    result = {"stage": "NOT_TESTED", "input": str(source), "expected_sha256": expected,
              "runtime_tested": False, "checks": dict.fromkeys(
                  ("rendering", "controller", "keyboard", "audio", "filesystem", "shutdown", "leaks", "frame_time"), "NOT_TESTED")}
    if not source.is_file():
        result["blocker"] = "Input file unavailable"
        return result
    result["input_sha256"] = sha256(source)
    if result["input_sha256"] != expected:
        result["blocker"] = "Input checksum mismatch; conversion refused"
        return result
    if output.exists() or output.with_suffix(".registry.json").exists():
        raise ValueError("Output must be fresh to exclude stale conversion evidence")
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [str(relinker), "--windows", "--windows-diagnostics", "--registry", str(source), str(output)]
    result["command"] = command
    start = time.monotonic()
    try:
        process = subprocess.run(command, capture_output=True, timeout=timeout)
        result.update(returncode=process.returncode,
                      stdout=process.stdout.decode("utf-8", errors="replace"),
                      stderr=process.stderr.decode("utf-8", errors="replace"))
        registry = output.with_suffix(".registry.json")
        if process.returncode == 0 and output.is_file() and registry.is_file():
            result.update(stage="RELINKED", output_sha256=sha256(output), registry_sha256=sha256(registry),
                          blocker="Guest execution requires an isolated test environment; relinking does not verify functionality")
        else:
            result.update(stage="RELINK_FAILED", blocker="Relinker failed or did not produce both executable and registry")
    except subprocess.TimeoutExpired:
        result.update(stage="RELINK_FAILED", blocker="Relinker timeout", timed_out=True)
    except OSError as error:
        result["blocker"] = str(error)
    result["elapsed_seconds"] = time.monotonic() - start
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=pathlib.Path)
    parser.add_argument("--root", type=pathlib.Path, required=True)
    parser.add_argument("--relinker", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("timeout must be positive")
    args.output.mkdir(parents=True, exist_ok=True)
    repo = pathlib.Path(__file__).resolve().parents[1]
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=repo))
    report = {"schema_version": 1, "observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "source_commit": revision, "source_dirty": dirty, "host": platform.platform(),
              "relinker_sha256": sha256(args.relinker), "applications": []}
    for target in json.loads(args.manifest.read_text(encoding="utf-8"))["applications"]:
        result = relink(args.relinker.resolve(), (args.root / target["input"]).resolve(),
                        (args.output / target["id"] / "app.exe").resolve(), target["input_sha256"], args.timeout)
        report["applications"].append({**target, **result})
        (args.output / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(target["id"], result["stage"], flush=True)
    return 0 if all(app["stage"] == "RELINKED" for app in report["applications"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
