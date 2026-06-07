# Prompt Weights

Use the lightest prompt that provides enough control.

## Level 0: One-Line Nudge

Use for tiny vibe-coding edits.

Pattern:

```markdown
[Change request]. Keep the scope small and do not touch unrelated logic.
```

Example:

```markdown
Make the filter bar more compact. Keep existing behavior and data flow unchanged.
```

## Level 1: Goal + Boundary

Use for bounded changes.

Pattern:

```markdown
Please [goal]. Scope: [files/area]. Constraints: [do not change]. Verify by [simple check].
```

## Level 2: Context + Constraints + Verification

Use for normal coding/design work.

Pattern:

```markdown
## Context
[What exists / what is wrong]

## Goal
[Expected result]

## Constraints
- [do not change]
- [reuse existing patterns]

## Verification
- [tests/build/screenshots/manual checks]

## Report
Summarize root cause or design rationale, files changed, checks run, and residual risks.
```

## Level 3: Full Workflow Prompt

Use for complex, ambiguous, risky, or multi-file work.

Pattern:

```markdown
## Context
[Business/product/code context]

## Goal
[Outcome]

## Inputs / Variables
- [known files, URLs, logs, screenshots, constraints]

## Constraints / Anti-Goals
- [must not change]
- [avoid]

## Workflow
1. Read relevant code/docs first.
2. Summarize current behavior.
3. Identify risks and options.
4. Implement or produce the requested plan.
5. Verify.
6. Report.

## Verification Contract
- [mechanical checks]
- [human review evidence]

## Report
- Understanding
- Changes/plan
- Verification
- Risks
- Questions
```

## Level 4: Reusable Workflow

Use when the result should become AGENTS.md, CLAUDE.md, a slash command, custom command, skill, or multi-agent workflow.

Add:

- trigger boundary
- inputs/arguments
- stop conditions
- capability routing
- human review gates
- update/maintenance rules
- examples of short and heavy usage
