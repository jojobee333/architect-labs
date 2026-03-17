from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
import sys
import yaml


def run(cmd: list[str], cwd: Path) -> str:
    result = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def load_repo_map(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--base", required=False)
    parser.add_argument("--config", default="config/repo-map.yaml")
    parser.add_argument("--out", default="artifacts/reviews")
    args = parser.parse_args()

    cfg = load_repo_map(Path(args.config))
    repo_cfg = cfg.get("repos", {}).get(args.repo)

    if not repo_cfg:
        print(f"ERROR: repo '{args.repo}' not found in {args.config}", file=sys.stderr)
        return 1

    repo_path = Path(repo_cfg["local_path"])
    remote = repo_cfg.get("remote", "origin")
    base_branch = args.base or repo_cfg.get("default_base_branch", "main")

    if not repo_path.exists():
        print(f"ERROR: repo path does not exist: {repo_path}", file=sys.stderr)
        return 1

    out_dir = Path(args.out) / args.repo / args.branch.replace("/", "__")
    out_dir.mkdir(parents=True, exist_ok=True)

    run(["git", "fetch", remote], cwd=repo_path)
    run(["git", "fetch", remote, args.branch], cwd=repo_path)
    run(["git", "fetch", remote, base_branch], cwd=repo_path)

    merge_base = run(
        ["git", "merge-base", f"{remote}/{base_branch}", f"{remote}/{args.branch}"],
        cwd=repo_path,
    )

    head_sha = run(["git", "rev-parse", f"{remote}/{args.branch}"], cwd=repo_path)
    base_sha = run(["git", "rev-parse", f"{remote}/{base_branch}"], cwd=repo_path)

    commands = {
        "status.txt": ["git", "status", "--short"],
        "changed_files.txt": ["git", "diff", "--name-only", f"{merge_base}..{remote}/{args.branch}"],
        "name_status.txt": ["git", "diff", "--name-status", f"{merge_base}..{remote}/{args.branch}"],
        "diff_stat.txt": ["git", "diff", "--stat", f"{merge_base}..{remote}/{args.branch}"],
        "commits.txt": ["git", "log", "--oneline", f"{merge_base}..{remote}/{args.branch}"],
        "full.diff": ["git", "diff", f"{merge_base}..{remote}/{args.branch}"],
    }

    for filename, cmd in commands.items():
        content = run(cmd, cwd=repo_path)
        (out_dir / filename).write_text(content + "\n", encoding="utf-8")

    summary = f"""repo_path: {repo_path}
remote: {remote}
base_branch: {base_branch}
target_branch: {args.branch}
merge_base: {merge_base}
base_sha: {base_sha}
head_sha: {head_sha}
artifact_dir: {out_dir}
"""
    (out_dir / "summary.txt").write_text(summary, encoding="utf-8")

    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())