# Coding Prompt Patterns

Use for bugfix, refactor, legacy modernization, and performance prompts.

## Bugfix

```markdown
Please fix this bug.

## Symptom
[what happens]

## Expected
[what should happen]

## Reproduction
1. [step]
2. [step]

## Constraints
- Find the root cause before editing.
- Make the smallest behavior-preserving fix.
- Do not refactor unrelated code.

## Verification
- Run relevant tests/build.
- Report root cause, changed files, checks run, and residual risk.
```

## Refactor

```markdown
Please refactor [module] to improve [maintainability/performance/readability] while preserving external behavior.

Before editing, identify current responsibilities, callers, tests, and risks. Work in small steps. Avoid broad formatting churn, public API changes, or unrelated cleanup. If behavior is not covered by tests, add minimal characterization tests or provide a manual verification checklist first.
```

## Legacy Modernization

```markdown
This is an old project with tangled code and performance problems. Do not rewrite it from scratch.

Phase 1: diagnose and protect behavior.
1. Read project entry points, core flows, data/API boundaries, and build/test setup.
2. Summarize architecture, business-critical paths, and likely performance bottlenecks.
3. Identify high-risk areas where behavior must be preserved.
4. If tests are thin, propose or add minimal characterization tests.

Phase 2: implement one low-risk, high-value improvement.
- Keep behavior and API contracts unchanged.
- Avoid large new dependencies and broad rewrites.
- Verify with existing checks and focused manual evidence.

Report current understanding, prioritized plan, actual change, verification, and next step.
```

## Performance

```markdown
Please investigate and improve performance for [area].

First establish a baseline or plausible bottleneck from code/runtime evidence. Do not guess-and-rewrite. Look for repeated renders, unnecessary requests, synchronous blocking work, unbounded loops, large lists, bundle size, cache misses, and expensive derived state. Implement the smallest measurable improvement and report before/after evidence or the limits of verification.
```
