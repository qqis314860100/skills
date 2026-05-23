---
name: ai-project-harness
description: "Design, audit, or improve an AI-friendly software project harness: repository-as-record documentation, AGENTS.md/CLAUDE.md navigation, executable constraints, CI/lint backpressure, agent-readable architecture, review loops, entropy control, and spec-first workflows. Use when Codex is asked to set up an AI development project, make a repo easier for coding agents to work in, create project instructions for agents, convert team conventions into checks, review an agentic development workflow, or apply Harness Engineering practices to a codebase."
---

# AI Project Harness

Use this skill to turn a long-lived software repo into a reliable working environment for coding agents. Treat the harness as everything around the model: repo structure, instructions, tools, checks, workflow state, feedback loops, and human gates.

Use it when the project will be visited repeatedly by Codex, Claude Code, or other agents. If the task is a one-off edit or disposable prototype, keep the harness minimal and avoid heavy process.

Core stance: humans steer, agents execute. Do not try to script every agent step. Encode intent, boundaries, and verification so the agent can choose a path and the system can reject bad outcomes.

## Workflow

1. Read the project entry points first: `README*`, `AGENTS.md`, `CLAUDE.md`, package/build files, CI config, test config, and existing docs.
2. Identify the project mode: solo project, team repo, legacy migration, greenfield scaffold, agent-orchestrated workflow, or spec-as-product project.
3. Map current harness components into guides and sensors.
4. Find missing context, unenforced conventions, unclear gates, and entropy sources.
5. Implement the smallest useful harness improvement, then run the project checks that prove it works.
6. If behavior correctness cannot be mechanically verified, create a human review gate with high-quality evidence instead of pretending it is solved.

## Long-Lived Project Standard

Use this skill to standardize projects that need durable AI collaboration. A strong target should have:

- a short root entry file that tells agents where to start
- a documented architecture or dependency map
- deterministic checks in CI or local scripts
- a clear human gate for product behavior
- an explicit place for decisions, plans, and drift handling

If any of those are missing, prioritize them before polishing prompts or adding more agent automation.

Calibrate the amount of harness to the repo:

- `light`: add a root guide, the core checks, and one clear architecture note.
- `workable`: tighten boundaries, add repo-specific sensors, and make failure messages actionable.
- `strong`: add drift checks, review packets, and periodic cleanup.
- `overfit`: simplify the harness; remove process that no longer pays for itself.

## Evaluation Toolkit

For long-lived projects, keep at least one repeatable harness check:

- a repo readiness audit
- a command that checks the root guide, architecture map, CI, tests, and lint
- a way to summarize what is present, what is missing, and what should be added next

Use [scripts/audit_harness.py](scripts/audit_harness.py) as the default smoke test for harness readiness. Run it against a repo root after changes to instructions, CI, or architecture.

## Distribution

Keep this skill as the source of truth in the repo. When you update it, sync it to both local runtime directories with [scripts/sync_skill.sh](scripts/sync_skill.sh) instead of editing installed copies by hand.

## Harness Map

Build or audit these layers in order.

### 1. Repository As Record

Put decisions where agents can read them. Knowledge that lives only in chat, meetings, tickets, or memory does not exist to the agent.

Prefer these durable artifacts:

- `AGENTS.md` or `CLAUDE.md` as the short navigation entry point.
- `docs/ARCHITECTURE.md` for module boundaries and dependency direction.
- `docs/decisions/` or ADRs for irreversible or non-obvious choices.
- `docs/plans/active/` and `docs/plans/completed/` for long-running work.
- `docs/generated/` for schemas, API snapshots, route maps, or other machine-generated context.
- Issue tracker state for in-flight work when the agent can read it.

Keep the root agent file as a map, not a manual. Aim for 60-100 lines: what this repo is, where to look next, hard rules, common commands, and verification gates.

### 2. Guides Before Work

Guides increase first-pass success. Use them for stable direction, not micromanagement.

- Use concise project instructions for repo layout, naming, architecture, testing, and forbidden patterns.
- Prefer boring, well-documented, widely used technology when the choice is otherwise neutral.
- Make architecture explicit: layers, dependency direction, allowed cross-cutting entry points, ownership boundaries.
- For spec-first work, write `SPEC.md` for the problem and constraints, and `WORKFLOW.md` for state transitions and required evidence. Do not over-specify implementation unless it is truly required.
- For generated code, provide examples of the desired local style, because agents will imitate nearby patterns.

### 3. Sensors After Work

Sensors let agents self-correct. Convert every repeated review comment into a check, script, or test when possible.

- Use typecheck, lint, tests, format, build, security scans, and architecture tests as deterministic sensors.
- Add custom lint rules or scripts for repo-specific invariants.
- Make failure messages actionable. Include what failed, why it matters, and where to fix it.
- Use AI review only for semantic risks that deterministic checks cannot cover.
- Keep expensive reasoning sensors conditional: run them for risky changes, repeated failures, design ambiguity, security-sensitive work, or release gates.

Good sensor error shape:

```text
Error: UI imports from service layer directly.
Fix: Route cross-layer access through <domain>/runtime/provider.ts.
See: docs/ARCHITECTURE.md#layering
```

### 4. Backpressure Over Prescription

Constrain outcomes more than implementation paths.

- Prefer "all public routes need auth coverage" over "edit these five files in this order."
- Prefer "no module may import backward across the layer graph" over "always use pattern X."
- Block only rules that protect correctness, safety, reliability, or long-term maintainability.
- Warn or document preferences when many valid implementations exist.
- Keep local autonomy inside enforced boundaries.

### 5. Entropy Control

Agents reproduce the patterns they see, including bad ones. Make cleanup continuous.

- Track golden rules: shared utilities over duplicate helpers, typed boundaries over YOLO probing, predictable local abstractions over opaque wrappers for critical paths.
- Schedule or periodically run drift checks: duplicate helpers, oversized files, stale docs, inconsistent errors, untested critical paths, architectural leakage.
- When the same mistake appears twice, update instructions; when it appears three times, add a mechanical check.
- Treat refactoring as part of generation throughput, not a later luxury.

### 6. Throughput And Merge Flow

Optimize for fast correction only after backpressure exists.

- Keep agent changes small enough to review and revert.
- Allow quick iteration on flaky or low-risk failures, but do not bypass deterministic correctness gates.
- For high-throughput teams, make PR/ticket review packets summarize goal, files changed, checks run, screenshots/logs, known risks, and remaining human decisions.
- For solo projects, prefer quality and comprehension over raw PR velocity. The missing reviewer is the main risk.

### 7. Validation Loop

For long-lived repos, do not stop at one pass.

1. Audit the current harness.
2. Apply the smallest useful improvement.
3. Re-run the relevant checks or workflow.
4. Compare what the agent can now infer without extra explanation.
5. Repeat until the repo’s rules are stable enough that a fresh agent can onboard safely.

### 8. Behavior Gate

Behavior correctness is the weak point of most harnesses. Tests and AI review often prove structure, not user intent.

When behavior cannot be fully automated:

- Preserve the user goal and acceptance criteria in a file or ticket.
- Ask the agent to produce evidence: test output, screenshots, traces, logs, before/after examples, and a risk note.
- Require human confirmation for product behavior, UX judgment, business policy, security acceptance, or irreversible operations.
- Make the human decision explicit in the workflow state.

## Output Templates

When auditing a repo, produce:

```markdown
## Harness Summary
- Current maturity: light / workable / strong / overfit
- Main risk: ...
- Best next improvement: ...

## Guides
- Present: ...
- Missing: ...

## Sensors
- Present: ...
- Missing: ...

## Recommended Changes
1. ...
2. ...
3. ...

## Verification
- Run: ...
- Human gate needed for: ...
```

When adding a root agent file, use:

```markdown
# Project Agent Guide

## What This Is
One paragraph describing the product and stack.

## Start Here
- Read ...
- Then read ...

## Hard Rules
- ...

## Common Commands
- Install: ...
- Test: ...
- Lint: ...
- Build: ...

## Before Finishing
- Run ...
- Update ...
```

## Anti-Patterns

- Do not create giant instruction files that duplicate the whole repo.
- Do not rely on prose for rules that can be checked mechanically.
- Do not hide crucial context in private chat or unlinked documents.
- Do not optimize for agent autonomy before adding backpressure.
- Do not treat passing tests as proof that product behavior is correct.
- Do not add heavy orchestration to a solo or small project before simple guides and sensors exist.
- Do not install a generic harness without surfacing its assumptions about language, workflow, branch strategy, commits, and review culture.
