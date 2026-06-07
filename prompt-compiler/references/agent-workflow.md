# Agent Workflow Prompts

Use for reusable commands, long-running workflows, multi-agent delegation, and project instructions.

## Reusable Command Shape

```markdown
## Purpose
[One or two direct sentences]

## Inputs / Arguments
- [argument]: [meaning]

## Preconditions
- [what must exist before running]

## Workflow
1. [inspect]
2. [plan]
3. [act]
4. [verify]
5. [report]

## Stop Conditions
- Stop and ask when [missing input/risky change/unclear business rule].

## Verification
- [tests/build/screenshots/review]

## Report
- [fields]
```

## Multi-Agent Delegation

Use only when parallelism helps.

```markdown
Please split this task into parallel agents.

For each sub-agent, define:
- mission
- input context
- scope boundary
- files or areas to inspect
- output format
- risks to watch

The primary agent must merge results, identify conflicts, list gaps, and recommend next steps. Do not let sub-agents modify code unless explicitly authorized.
```

## Human Gates

Add human approval before:

- changing business rules or API contracts
- large refactors or migrations
- introducing major dependencies
- destructive operations
- accepting UX/product tradeoffs that cannot be mechanically tested
- writing durable project rules into AGENTS.md, CLAUDE.md, or skills

## Persisting To Project Instructions

When converting a workflow into AGENTS.md or CLAUDE.md:

- keep the root instruction short
- include trigger boundaries
- link to detailed docs when needed
- encode constraints and verification, not personal chat history
- avoid rules that would make tiny tasks heavy
