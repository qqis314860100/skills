---
name: atom-team-workflow
description: Personal and small-team software delivery workflow for new projects, legacy refactors, frontend/backend 1+1 teams, AI-assisted development, modernization, performance work, UI redesigns, and feature upgrades. Use when asked to design or apply a lightweight development process, refactor an old project safely, start a new project with practical guardrails, define validation/commit rules, reduce process overhead, or coordinate a tiny team without heavyweight enterprise ceremony.
---

# Atom Team Workflow

Use this skill to guide personal or small-team software work. It fits solo projects, "one frontend + one backend" teams, and AI-assisted coding where the goal is to move fast without losing rollback, compatibility, or product correctness.

Core standard:

```text
日常轻、边界硬、高风险重、上下文省、自动化单独管。
```

## First Decision

Classify the work before suggesting rules or editing process files:

- **New project**: create the smallest useful harness before building too much.
- **Legacy refactor**: protect existing behavior first; new technology comes after baseline and rollback.
- **Feature work**: keep one user capability or one technical topic per change.
- **Performance/UI modernization**: measure or screenshot before changing; compare after.
- **Release/AFK automation**: raise guardrails; require clean worktree, bounded tasks, and stop-on-failure.

If the user wants implementation, update the repository's actual guide files or scripts instead of only explaining a process.

## Universal Rules

Use these as the default for personal and small teams:

- **Single-topic change**: one commit or PR expresses one feature, fix, refactor, migration, or workflow update. Cross-layer changes are fine only when they serve the same topic.
- **One detailed rule source**: keep entry files short; put detailed workflow rules in one canonical document.
- **Hard architecture boundaries**: UI, API/business logic, data/retrieval/infrastructure responsibilities must not blur.
- **Two validation tiers**:
  - Normal: smallest relevant check, targeted test, local smoke, typecheck, or build.
  - High-risk: real user/service flow, migration safety, permissions, deletion, auth, payment/order/core business path, streaming/async, release, or automation loop.
- **Context budget**: use `rg` before reading files, inspect small ranges, summarize logs, and avoid loading build output, databases, PDFs, or long console logs unless needed.
- **Chinese-readable team docs when the team works in Chinese**: keep filenames used by tools if needed, but make the content readable for the humans.

## New Project Workflow

For a new project, avoid over-building the process before the product exists.

1. Define the product goal, core users, and first vertical slice.
2. Create a short entry file for agents and developers: what this is, where to start, hard boundaries, common commands.
3. Define the architecture boundary only as far as the current design needs.
4. Add minimal scripts: install, dev, lint/typecheck, build/test, verify if useful.
5. Build one end-to-end slice before adding more framework, plugin, hook, or subagent machinery.
6. Add heavier checks only after the same problem appears repeatedly or before release.

Good default: `light harness -> vertical slice -> targeted checks -> iterate`.

## Legacy Refactor Workflow

For an old company project, the first job is not to introduce new technology. The first job is to avoid breaking current business.

1. Identify core flows that must not break: login, permissions, key forms, list/detail, create/edit/delete, payment/order/approval/export/upload, scheduled jobs, or company-specific critical paths.
2. Record a baseline before changing code:
   - screenshots or screen recordings for key pages
   - API inputs/outputs for key endpoints
   - performance numbers for slow pages or queries
   - known bugs and intentional current behavior
3. Pick a pilot module that is representative but not the riskiest.
4. Separate work types:
   - refactor: preserve behavior
   - technology upgrade: change platform or dependencies
   - performance: improve measured bottlenecks
   - UI redesign: change experience and layout
   - feature change: change business capability
5. Preserve compatibility first. For backend, avoid breaking API contracts and migrations without rollback or backup. For frontend, use routes, feature flags, or side-by-side replacement when possible.
6. Move module by module. After the pilot proves the pattern, repeat with the same checklist.

Rule of thumb:

```text
先保真，再变快，再变新，再变好看。
```

## Frontend/Backend 1+1 Collaboration

For one frontend developer and one backend developer:

- Start each slice with a contract: endpoint shape, auth/permission behavior, error shape, loading/empty/error UI, and rollback expectation.
- Backend should provide stable contracts or mocks early; frontend should expose UI states without waiting for perfect backend data.
- Do not hide missing backend capability with fake frontend completion.
- Keep integration checks small but real on critical paths.
- When frontend and backend change together for one capability, a single topic is acceptable; unrelated cleanup should be separate.

## Validation Guide

Use the cheapest check that proves the actual risk.

Normal examples:

- docs/process change: syntax or link scan, maybe no runtime check
- small UI state change: component/page smoke or targeted browser check
- ordinary API field: targeted request or unit/integration test
- utility refactor: focused test or direct function assertion

High-risk examples:

- auth, permissions, payments, orders, deletion, data migration
- upload/import/export, async jobs, queues, streaming, retries
- core pages or core business paths
- cross-service contracts
- release, deployment, feature flags, AFK/agent automation

For high-risk work, collect evidence but keep it concise: command names, short result, screenshot path if useful, and the specific path tested.

## Commit And PR Shape

Prefer this structure:

```text
Goal: what user/business/technical outcome this change delivers
Change: what changed, grouped by area
Validation: smallest checks run, with high-risk flow evidence if applicable
Risk: compatibility, rollback, migration, or known remaining risk
```

Commit message guidance:

- Use conventional commits if the repo does.
- Prefer local team language for descriptions.
- Keep one topic per commit.
- Do not add AI footer text unless the repo explicitly requires it.

## When To Add More Process

Add guardrails only when they pay for themselves:

- repeated mistakes -> add a checklist or deterministic check
- risky command or data operation -> add a hook, script, or human approval gate
- release or migration -> add rollback and verification steps
- team handoff confusion -> add a short canonical doc
- long-running AI automation -> add queue, clean-worktree rule, stop-on-failure, and context budget

Avoid adding process for one-off preferences, speculative future scale, or problems that have not appeared yet.

## Expected Output

When asked to design or update a workflow, produce or implement:

- the current mode: new project, refactor, feature, performance, UI, release, or AFK
- the minimal rules that protect this mode
- the high-risk list specific to the project
- the smallest validation standard
- the commit/PR shape
- any repo files or scripts that should change

Keep the answer practical. If editing a repo, make the smallest useful change and verify it with lightweight checks.
