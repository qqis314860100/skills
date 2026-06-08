---
name: prompt-compiler
description: Use when the user wants to write, improve, diagnose, compress, structure, or turn an idea into an effective prompt for Codex, Claude Code, coding agents, design agents, research agents, or reusable AGENTS.md/CLAUDE.md/custom-command workflows. Trigger on requests like "帮我写提示词", "这个任务怎么 prompt", "优化这个 prompt", "为什么 agent 跑偏", "沉淀成 workflow", "把需求转成 agent 能执行的提示词", or when the user explicitly asks to use prompt-compiler. Do not trigger for ordinary coding/design/debugging tasks unless the user asks for a prompt rather than implementation.
---

# Prompt Compiler

Turn vague intent into the smallest effective agent prompt. This skill is a compiler and router, not a universal gate for all work.

Core stance: use structure only when it buys clarity. Tiny edits should remain tiny; complex, ambiguous, risky, or reusable work deserves stronger framing.

## Trigger Boundary

Use this skill when the user asks to:

- write, improve, review, compress, or debug a prompt
- convert a fuzzy task into an agent-executable prompt
- design a reusable workflow for Codex, Claude Code, AGENTS.md, CLAUDE.md, or slash/custom commands
- decide what prompt weight or skill routing a complex task needs
- add brainstorming, CPD/superpower, frontend-design, review, browser verification, or other capability routing to a prompt

Do not use this skill just because the underlying task is coding, design, or bug fixing. If the user says "fix this bug" or "update this UI", do the task directly unless they ask for a prompt.

## Task Brief Confirmation

For complex, ambiguous, high-risk, multi-skill, or user-authorized routing work, output a concise `Task Brief` before execution. This is a lightweight confirmation gate, not a full plan.

Do not use a Task Brief for tiny edits, ordinary bug fixes, or clear direct implementation requests.

A Task Brief should confirm:

- understood goal
- recommended process
- capability routing and confidence
- explicit non-goals
- next step after confirmation

If the user confirms, proceed with the chosen skill or workflow. If the user rejects the route, revise the brief.

## Core Workflow

1. Identify the user's real request:
   - prompt creation
   - prompt review/debugging
   - prompt compression
   - agent workflow design
   - skill/capability routing
   - reusable project instruction
2. Classify the task type and risk. See [task-types.md](references/task-types.md) when classification is non-obvious.
3. Choose prompt weight. See [prompt-weights.md](references/prompt-weights.md).
4. Add only the necessary sections:
   - context
   - goal
   - inputs/variables
   - constraints and anti-goals
   - workflow
   - verification contract
   - report format
   - capability routing
5. If routing is complex or uncertain, produce a Task Brief first.
6. If domain expertise is needed, route to the smallest useful capability set. See [capability-routing.md](references/capability-routing.md).
7. Output ready-to-copy prompt text. Include short/standard/heavy variants only when useful.

## Missing Information

Ask for missing information only when a reasonable assumption would be risky. Otherwise, state the assumption and continue.

Always ask for the original prompt when the user asks to optimize "this prompt" but has not provided it.

Common missing inputs:

- goal: what result should change?
- scope: which page, module, repo, files, product area?
- boundary: what must not change?
- verification: how should success be checked?
- audience: who will use the output?
- target agent/tool: Codex, Claude Code, browser agent, research agent, team member?

## Prompt Weights

- `Level 0`: one-line vibe-coding nudge
- `Level 1`: goal + boundary
- `Level 2`: context + goal + constraints + verification
- `Level 3`: full workflow prompt with report format
- `Level 4`: reusable AGENTS.md/CLAUDE.md/custom-command or multi-agent workflow

Prefer the lightest prompt that gives enough control.

## Capability Routing

Prompt Compiler owns framing and routing. Domain skills own expertise and execution.

Use three routing modes:

- `suggest`: tell the user which skill/capability should be used
- `invoke`: actually use the available skill in the current turn when the user wants the work done
- `embed`: write capability instructions into the generated prompt for a downstream agent

Default to the smallest capability set. Do not route tiny edits. Do not let brainstorming override business constraints, tests, or existing logic.

If Superpowers is available, do not duplicate its full development workflow. Prompt Compiler should clarify the task and route to Superpowers phases when useful; Superpowers owns brainstorming, planning, TDD, subagent development, review, verification, and branch finishing.

## Output Patterns

For prompt creation, usually output:

```markdown
## Recommended Prompt

[ready-to-copy prompt]

## When To Use

[brief note]
```

For complex routing confirmation, output:

```markdown
## Task Brief

I understand the goal as:
- [goal]

Recommended process:
- [process]

Capability routing:
- `[skill]`: [suggest/invoke/embed + confidence + reason]

Non-goals:
- [what not to do]

After confirmation:
- [next step]
```

For prompt review, output:

```markdown
## Diagnosis

- [issue]

## Improved Prompt

[ready-to-copy prompt]

## Why This Is Better

[brief note]
```

For complex tasks, output variants:

```markdown
## Short Version

[vibe-coding prompt]

## Standard Version

[normal agent prompt]

## Heavy Version

[full workflow prompt]
```

## References

Load only what the current request needs:

- [task-types.md](references/task-types.md): classify task shape and risk
- [prompt-weights.md](references/prompt-weights.md): choose prompt weight
- [capability-routing.md](references/capability-routing.md): route to frontend-design, review, browser, research, brainstorming, multi-agent
- [prompt-review.md](references/prompt-review.md): diagnose and rewrite prompts
- [coding.md](references/coding.md): bugfix, refactor, legacy modernization, performance prompts
- [ui-ux.md](references/ui-ux.md): UI/UX, legacy UI redesign, frontend verification prompts
- [agent-workflow.md](references/agent-workflow.md): long-running workflows, delegation, reusable commands
