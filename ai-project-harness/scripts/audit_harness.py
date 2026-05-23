#!/usr/bin/env python3
"""Smoke test a repo for long-lived AI project harness readiness.

Checks for the main ingredients of a durable harness:
- a root agent guide
- an architecture or boundary document
- CI/workflow automation
- deterministic tests/lint/config signals
- decision or plan records

The goal is not to prove quality, only to show whether the repo has the
minimum structure that lets agents work repeatedly without drifting.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    details: str
    weight: int


def any_exists(root: Path, candidates: list[str]) -> str | None:
    for rel in candidates:
        if (root / rel).exists():
            return rel
    return None


def any_glob(root: Path, patterns: list[str]) -> str | None:
    for pattern in patterns:
        if any(root.glob(pattern)):
            return pattern
    return None


def check_root_guide(root: Path) -> Check:
    hit = any_exists(root, ["AGENTS.md", "CLAUDE.md", "README.md"])
    return Check("root guide", hit is not None, hit or "missing", 2)


def check_architecture(root: Path) -> Check:
    hit = any_exists(root, [
        "docs/ARCHITECTURE.md",
        "ARCHITECTURE.md",
        "docs/architecture.md",
    ])
    return Check("architecture map", hit is not None, hit or "missing", 2)


def check_ci(root: Path) -> Check:
    hit = any_glob(root, [".github/workflows/*.yml", ".github/workflows/*.yaml"])
    return Check("ci workflows", hit is not None, hit or "missing", 2)


def check_tests(root: Path) -> Check:
    hit = any_exists(root, [
        "tests",
        "test",
        "__tests__",
        "pytest.ini",
        "tox.ini",
        "package.json",
        "pyproject.toml",
        "vitest.config.ts",
        "vitest.config.js",
        "jest.config.js",
        "jest.config.ts",
    ])
    return Check("test signal", hit is not None, hit or "missing", 1)


def check_lint(root: Path) -> Check:
    hit = any_exists(root, [
        ".eslintrc",
        ".eslintrc.js",
        ".eslintrc.cjs",
        "eslint.config.js",
        "eslint.config.mjs",
        "eslint.config.ts",
        "ruff.toml",
        "pyproject.toml",
        "mypy.ini",
    ])
    return Check("lint signal", hit is not None, hit or "missing", 1)


def check_records(root: Path) -> Check:
    hit = any_exists(root, [
        "docs/decisions",
        "docs/plans",
        "docs/generated",
        "feedback",
        "references",
    ])
    return Check("decision/plan records", hit is not None, hit or "missing", 1)


def check_scripts(root: Path) -> Check:
    hit = any_exists(root, ["scripts"])
    return Check("maintenance scripts", hit is not None, hit or "missing", 1)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    if not root.exists():
        print(f"error: path does not exist: {root}", file=sys.stderr)
        return 2

    checks = [
        check_root_guide(root),
        check_architecture(root),
        check_ci(root),
        check_tests(root),
        check_lint(root),
        check_records(root),
        check_scripts(root),
    ]
    total = sum(c.weight for c in checks)
    score = sum(c.weight for c in checks if c.passed)

    print(f"Repo: {root}")
    print(f"Score: {score}/{total}")
    print()
    for c in checks:
        mark = "PASS" if c.passed else "FAIL"
        print(f"- {mark:<4} {c.name:<24} {c.details}")

    print()
    if score == total:
        print("Assessment: strong harness baseline")
    elif score >= total * 0.7:
        print("Assessment: workable harness baseline")
    elif score >= total * 0.4:
        print("Assessment: light harness baseline")
    else:
        print("Assessment: harness needs setup")

    missing = [c.name for c in checks if not c.passed]
    if missing:
        print("Next: add " + ", ".join(missing))
    else:
        print("Next: keep the harness small and maintain the checks")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
