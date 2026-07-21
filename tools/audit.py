"""Compatibility wrapper for the audit CLI.

This wrapper keeps backward compatibility for direct Python execution while the
primary audit implementation lives in the uv workspace app.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    """Execute the uv-managed audit-runner package.

    Returns:
        The exit code from the uv subprocess.
    """
    import subprocess

    repo_root = Path(__file__).resolve().parents[1]
    cmd = [
        "uv",
        "run",
        "--directory",
        str(repo_root / "tools"),
        "--package",
        "audit-runner",
        "audit-runner",
    ]
    return subprocess.run(cmd, cwd=repo_root, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
