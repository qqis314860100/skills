# UI/UX Prompt Patterns

Use for frontend UI, dashboard, admin, SaaS, legacy UI planning, and implementation prompts.

## Legacy UI Plan From Code

Use when the user wants a design plan before implementation.

```markdown
Please design a UI/UX modernization plan based on the current legacy code. Do not modify code yet.

## Context
This is an existing business system with historical UX, API calls, permissions, state handling, and hidden business logic. First infer the current product flow from the code.

## Goal
Produce an implementable, phased UI/UX plan that preserves existing business logic and API contracts while improving clarity, professionalism, task efficiency, states, and responsive behavior.

## Analyze
1. Current user goals and core tasks.
2. Page/module structure and data sources.
3. Existing interaction flow and state handling.
4. Business rules, permissions, and API contracts that must not change.
5. UI/UX problems: information hierarchy, navigation, forms, filters, tables, details, loading, empty, error, disabled states, responsive behavior.

## Superpower / CPD Brainstorming
Before recommending a final direction, generate:
1. Conservative option: low-risk improvements.
2. Ambitious option: stronger information architecture and interaction changes.
3. Counter-intuitive option: a different structure or workflow, with risks and prerequisites.

Score options by business value, UX lift, implementation cost, legacy compatibility, risk, and phased delivery.

## Output
- Current business and UX understanding
- Main UI/UX problems
- Three options and scores
- Recommended plan
- Page structure and key component design
- State and error handling design
- Phased implementation plan
- Risks and business questions
```

## UI Implementation From Existing Code

```markdown
Please modernize this existing UI while preserving business behavior.

First read the page, components, hooks, API usage, state handling, and styles. Summarize current UX and data flow before editing.

## Constraints
- Do not change API contracts or business rules.
- Do not add unrelated features.
- Reuse existing stack and components where practical.
- Avoid landing-page aesthetics for operational tools.
- Keep layout responsive and accessible.

## Focus
- information hierarchy
- scanability
- task flow
- status and error states
- layout density
- responsive behavior
- visual consistency

## Verification
Run relevant checks. If browser tooling is available, inspect desktop and mobile for overflow, overlap, clipped text, broken interactions, and empty/loading/error states.
```

## Frontend Anti-Goals

- do not redesign from imagination before reading code
- do not bury critical business states in decoration
- do not make dashboards look like marketing pages
- do not add heavy UI libraries without approval
- do not sacrifice table/form usability for visual novelty
- do not ignore empty, loading, error, disabled, and permission states
