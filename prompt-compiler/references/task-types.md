# Task Types

Use this file when the prompt request is broad or ambiguous.

## Classifier

- `tiny-edit`: copy, color, spacing, one-line behavior, small config
- `bugfix`: known failure, regression, error, broken behavior
- `feature`: add or change bounded behavior
- `ui-ux`: visual hierarchy, interaction, layout, product experience
- `legacy-ui-plan`: design a UI/UX plan from old code without implementing
- `refactor`: improve structure while preserving behavior
- `legacy-modernization`: old project, tangled logic, performance and maintainability issues
- `performance`: identify bottlenecks, measure, optimize, verify
- `research`: summarize, compare, choose, or investigate
- `review`: critique prompt/code/design/plan before implementation
- `agent-workflow`: long-running, multi-stage, multi-agent, or reusable command
- `project-instruction`: AGENTS.md, CLAUDE.md, skill, team workflow, durable guardrail

## Risk Signals

Increase prompt weight when the task has:

- unclear expected behavior
- business logic hidden in old code
- API/contract compatibility constraints
- security, payments, auth, data writes, or migrations
- cross-file or cross-team impact
- design judgment or product tradeoffs
- need for screenshots, metrics, tests, or review evidence
- intent to reuse the prompt or workflow later

Decrease prompt weight when:

- scope is one file or one obvious element
- user is vibe coding and expects fast iteration
- behavior is easy to inspect manually
- no durable prompt artifact is needed

## Default Mapping

- tiny-edit -> Level 0 or 1
- ordinary bugfix -> Level 1 or 2
- risky bugfix/performance -> Level 2 or 3
- legacy UI plan -> Level 3
- implementation after approved plan -> Level 2 or 3
- legacy modernization -> Level 3 or 4
- reusable command/AGENTS.md/CLAUDE.md -> Level 4
