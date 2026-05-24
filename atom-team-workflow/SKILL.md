---
name: atom-team-workflow
description: Lightweight but enterprise-aware delivery workflow for solo or small software teams, especially frontend/backend 1+1 teams using AI assistance. Use when asked to shape a practical workflow for a new product, legacy refactor, modernization, performance/UI upgrade, feature slice, validation rules, commit/PR discipline, rollout safety, or small-team coordination without heavyweight enterprise ceremony.
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

## When Not To Use

Do not use this skill as the main tool when the task is mainly:

- repo harness or agent instruction system design; use a harness-oriented skill
- multi-session milestone decomposition; use a blueprint-oriented skill
- pure coding standards, language style, or implementation details; use a narrower technical skill
- large-organization governance, compliance program design, or PMO process design

If another skill owns the narrower job, use this skill only for the small-team delivery lens.

## Progressive Disclosure

Only surface the section that matches the current mode.

- For a quick recommendation, give the mode, 3-5 protective rules, and the validation tier.
- For a repo change, name the files/scripts to update and the smallest useful check.
- For a full workflow, expand only the relevant mode sections.
- Do not restate all universal rules unless they materially change the answer.

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
- **Reuse first**: update existing guide files, scripts, templates, screenshots, recordings, or baseline artifacts instead of creating parallel process files.

## AI-Assisted Work Guardrails

When AI agents participate in enterprise work:

- Give agents bounded tasks with explicit touched areas, forbidden areas, acceptance criteria, and validation evidence.
- Require human or owner review for contract changes, permission changes, data migrations, deletion, security-sensitive code, and legacy behavior removal.
- Check AI-generated changes against architecture boundaries, external contracts, secrets/config handling, and existing tests before merging.
- Do not accept broad rewrites, speculative cleanup, or dependency upgrades unless they match the declared work mode and rollback plan.

## New Project Workflow

For a new project, avoid over-building the process before the product exists.

1. Define product goal, target users, non-goals, acceptance criteria, and first vertical slice.
2. Model the domain lightly: glossary, core entities, state transitions, business boundaries, roles, and permission matrix.
3. Record architecture decisions only where they matter: module boundaries, API/version strategy, storage, cache, async jobs, auth, and deployment shape.
4. Design data and API together: schema, indexes, migration/rollback, request/response shape, errors, pagination, idempotency, and versioning.
5. Define UI experience before implementation: page list, primary flows, empty/loading/error/permission states, responsive needs, and design-system choices.
6. Add minimal scripts: install, dev, lint/typecheck, build/test, verify if useful.
7. Build one end-to-end slice before adding more framework, plugin, hook, or subagent machinery.
8. Add heavier checks only after repeated failures or before release.

Good default: `light harness -> vertical slice -> targeted checks -> iterate`.

## Enterprise New Project Gates

For enterprise-grade new products, add these gates without turning daily work into a ceremony:

- **Requirements gate**: every milestone has goal, non-goals, users, acceptance criteria, and rollout owner.
- **NFR baseline**: define minimum security, audit, observability, backup/restore, performance budget, availability, accessibility, and cost expectations.
- **Permission gate**: define roles, resources, actions, data scope, and audit trail before implementing protected features.
- **Data gate**: define migration, rollback, seed data, retention, privacy, and indexing strategy before persistent data changes.
- **API gate**: define contract, error shape, compatibility, idempotency, pagination, and versioning before frontend/backend split work.
- **Operations gate**: define logs, metrics, alerts, release checklist, rollback path, and post-release observation window before production launch.
- **Environment and delivery gate**: define dev/staging/production parity, configuration ownership, secret management, CI required checks, deployment artifact traceability, and rollback trigger before the first production release.

## Legacy Refactor Workflow

For an old company project, the first job is not to introduce new technology. The first job is to avoid breaking current business.

1. Inventory the touched area before implementation: routes/pages, APIs, data tables, permissions, jobs, third-party integrations, known bugs, and business-critical flows.
2. Identify core flows that must not break: login, permissions, key forms, list/detail, create/edit/delete, payment/order/approval/export/upload, scheduled jobs, or company-specific critical paths.
3. Record a baseline before changing code:
   - screenshots or screen recordings for key pages
   - API inputs/outputs for key endpoints
   - performance numbers for slow pages or queries
   - known bugs and intentional current behavior
4. Pick a pilot module that is representative but not the riskiest.
5. Separate work types:
   - refactor: preserve behavior
   - technology upgrade: change platform or dependencies
   - performance: improve measured bottlenecks
   - UI redesign: change experience and layout
   - feature change: change business capability
6. Preserve compatibility first. For backend, avoid breaking API contracts and migrations without rollback or backup. For frontend, use routes, feature flags, adapters, or side-by-side replacement when possible.
7. Move module by module. After the pilot proves the pattern, repeat with the same checklist.

Rule of thumb:

```text
先保真，再变快，再变新，再变好看。
```

## Enterprise Legacy Refactor Rules

Use these as hard gates for enterprise legacy refactors:

- Do not start implementation before the touched area has a baseline inventory.
- Split modernization into tracks: behavior-preserving refactor, dependency/framework upgrade, performance work, UI redesign, and feature change. Do not combine tracks in one PR unless explicitly justified.
- Label each touched module with business risk, data risk, compatibility risk, rollout risk, and rollback method.
- Preserve external contracts by default: URLs, API shapes, error codes, auth behavior, export/import formats, database semantics, and existing visible behavior.
- For high-risk replacements, require one of: feature flag, side-by-side route/module, adapter layer, shadow mode, or documented rollback.
- Capture performance baselines before changing performance-sensitive code; compare after using the same measurement method.
- Capture UI screenshots for key states before redesign: default, loading, empty, error, permission denied, and data-heavy state.
- For legacy usage decisions, runtime evidence outranks static search. Before removing or changing externally visible behavior, check logs, traffic, database usage, scheduled jobs, downstream callers, owner confirmation, or production-like telemetry where available.
- AI agents must not delete legacy logic only because it appears unused. First prove usage with search, runtime evidence, owner confirmation, or tests.
- Large rewrites are forbidden by default. Prefer strangler replacement, module-by-module migration, adapters, and compatibility layers.
- A pilot is proven only when baseline behavior is preserved, validation passes, rollback is documented, and the pattern can handle at least one harder module.

## Frontend/Backend 1+1 Collaboration

For one frontend developer and one backend developer:

- Start each slice with a contract: endpoint shape, auth/permission behavior, error shape, loading/empty/error UI, and rollback expectation.
- Backend should provide stable contracts or mocks early; frontend should expose UI states without waiting for perfect backend data.
- Do not hide missing backend capability with fake frontend completion.
- Keep integration checks small but real on critical paths.
- When frontend and backend change together for one capability, a single topic is acceptable; unrelated cleanup should be separate.
- For each slice, confirm requirement, contract, data shape, permission behavior, UI states, validation method, migration needs, and rollback owner.

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

## Release And Evolution

For release, migration, or high-risk refactor:

- Release in small batches when possible.
- Define monitoring, smoke checks, rollback steps, owner, and observation window.
- For data migrations, require dry-run or rehearsal on production-like data when feasible, backup/restore verification, idempotency or rerun behavior, rollback limits, and post-migration data validation queries.
- Keep a post-release checklist: core flow works, errors are normal, metrics are within budget, support/ops signals are quiet.
- If a release changes data or contracts, document backup/restore or compatibility strategy before deployment.

## Commit And PR Shape

Prefer this structure:

```text
Goal: what user/business/technical outcome this change delivers
Change: what changed, grouped by area
Validation: smallest checks run, with high-risk flow evidence if applicable
Risk: compatibility, rollback, migration, or known remaining risk
```

Shortest example:

```text
Goal: speed up customer search without changing visible behavior
Change: added indexed query path behind existing API contract
Validation: search smoke, slow-query comparison, existing permission test
Risk: rollback by disabling new query path
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

1. Mode: new project / legacy refactor / feature / performance / UI / release / AFK.
2. Minimal rules: 3-5 rules that protect this mode.
3. High-risk items: concrete risks for this project.
4. Baseline: behavior, screenshot, API, data, performance, or NFR evidence needed before work.
5. Validation: smallest check that proves the change.
6. Commit/PR shape: one-topic summary format.
7. Repo changes: files, scripts, templates, or docs that should change.
8. Residual risk: anything still not fully verified.

Keep the answer practical. If editing a repo, make the smallest useful change and verify it with lightweight checks.
