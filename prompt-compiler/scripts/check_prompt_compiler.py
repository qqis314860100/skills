#!/usr/bin/env python3
"""Contract checks for the prompt-compiler skill.

This intentionally does not call an LLM. It verifies the skill package's
deterministic contract: metadata, reference availability, routing examples,
and boundary language that prevents the skill from intercepting tiny edits.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"
CASES = ROOT / "tests" / "e2e_cases.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def check_structure() -> None:
    text = read_text(SKILL)
    frontmatter = parse_frontmatter(text)
    if frontmatter.get("name") != "prompt-compiler":
        fail("frontmatter name must be prompt-compiler")

    description = frontmatter.get("description", "")
    for phrase in [
        "write, improve, diagnose",
        "Do not trigger for ordinary coding/design/debugging tasks",
    ]:
        if phrase not in description:
            fail(f"description missing trigger phrase: {phrase}")

    required_refs = [
        "task-types.md",
        "prompt-weights.md",
        "capability-routing.md",
        "prompt-review.md",
        "coding.md",
        "ui-ux.md",
        "agent-workflow.md",
    ]
    for ref in required_refs:
        if f"references/{ref}" not in text:
            fail(f"SKILL.md does not link references/{ref}")
        if not (REFERENCES / ref).exists():
            fail(f"missing reference: references/{ref}")

    for boundary in [
        "Do not use this skill just because the underlying task is coding",
        "Always ask for the original prompt",
        "Task Brief",
        "Default to the smallest capability set",
        "Do not route tiny edits",
        "do not duplicate its full development workflow",
        "`suggest`",
        "`invoke`",
        "`embed`",
    ]:
        if boundary not in text:
            fail(f"missing boundary rule: {boundary}")


def check_cases() -> None:
    cases = json.loads(read_text(CASES))
    if not isinstance(cases, list) or not cases:
        fail("tests/e2e_cases.json must contain a non-empty list")

    known_refs = {path.name for path in REFERENCES.glob("*.md")}
    seen_names: set[str] = set()
    trigger_count = 0
    skip_count = 0

    for index, case in enumerate(cases, 1):
        name = case.get("name")
        if not name:
            fail(f"case #{index} missing name")
        if name in seen_names:
            fail(f"duplicate case name: {name}")
        seen_names.add(name)

        if not case.get("input"):
            fail(f"case {name} missing input")
        if not isinstance(case.get("should_trigger"), bool):
            fail(f"case {name} should_trigger must be boolean")

        refs = case.get("expected_refs")
        if not isinstance(refs, list):
            fail(f"case {name} expected_refs must be a list")
        for ref in refs:
            if ref not in known_refs:
                fail(f"case {name} references unknown file: {ref}")

        should_trigger = case["should_trigger"]
        if should_trigger:
            trigger_count += 1
            if not refs:
                fail(f"triggering case {name} must include expected refs")
            weight = case.get("expected_weight")
            if weight not in {"Level 0", "Level 1", "Level 2", "Level 3", "Level 4"}:
                fail(f"triggering case {name} has invalid expected_weight: {weight}")
            if case.get("expect_task_brief") and weight not in {"Level 3", "Level 4"}:
                fail(f"case {name} expects a Task Brief but is too light: {weight}")
        else:
            skip_count += 1
            if refs:
                fail(f"skip case {name} should not include expected refs")
            if case.get("expected_weight") is not None:
                fail(f"skip case {name} expected_weight must be null")

    if trigger_count < 4:
        fail("case suite needs at least four trigger examples")
    if skip_count < 2:
        fail("case suite needs at least two skip examples")


def main() -> None:
    check_structure()
    check_cases()
    print("prompt-compiler contract checks passed")


if __name__ == "__main__":
    main()
