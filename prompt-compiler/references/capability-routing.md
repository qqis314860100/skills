# Capability Routing

Use this file when the prompt should call or coordinate other skills/capabilities.

## Principle

Prompt Compiler frames and routes. Domain skills execute or contribute expertise.

Use the smallest sufficient capability set. Route by phase, not by enthusiasm.

## Routing Modes

- `suggest`: recommend a capability to the user
- `invoke`: use an available skill/tool now because the user wants work done
- `embed`: write capability instructions into the prompt for a downstream agent

## Routing Table

| Need | Capability |
|------|------------|
| UI/UX redesign, visual hierarchy, frontend polish | `frontend-design` |
| Creative divergence,方案发散, CPD/superpower | `superpower-brainstorming` / embedded brainstorming workflow |
| Code risk review after implementation | `code-review-expert` or review workflow |
| Browser screenshots, responsive checks, interaction verification | `browser` / `playwright` |
| Latest docs, external facts, product/tech comparison | `research` / web / Context7 for technical docs |
| Parallel agents, background work, reusable commands | `agent-workflow` / coding-agent |
| Repo instructions, AGENTS.md, CLAUDE.md, long-lived agent setup | `ai-project-harness` |

## Phase Order

1. Explore: context reading, current-state summary
2. Brainstorm: CPD/superpower if the task needs creative options
3. Design: domain skill such as `frontend-design`
4. Implement: coding workflow
5. Verify: tests, build, browser screenshots
6. Review: code/design review
7. Persist: AGENTS.md/CLAUDE.md/custom command/skill if needed

## Embedded Capability Section

Use this when generating a downstream prompt:

```markdown
## Capability Plan

Use these capabilities if available:

1. `frontend-design`
   Analyze visual hierarchy, layout density, responsive behavior, states, and product fit.

2. `superpower / CPD`
   During planning only, generate conservative, ambitious, and counter-intuitive options. Compare by business value, cost, risk, compatibility, and verifiability.

3. `browser` / `playwright`
   After frontend implementation, inspect desktop and mobile layouts for overflow, overlap, clipped text, broken interactions, and empty states.

Do not modify code during brainstorming. Do not change business logic unless explicitly approved.
```

## Anti-Patterns

- routing every tiny edit through multiple skills
- invoking brainstorming during direct bug fixes
- using design skills to ignore existing business constraints
- using review as a replacement for tests
- embedding a huge capability plan when a one-line prompt is enough
