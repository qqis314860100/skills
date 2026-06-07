# Prompt Review

Use when the user asks to improve, diagnose, or compress a prompt.

## Required Input

If the original prompt is missing, ask for it.

## Diagnosis Checklist

- Goal: is the desired outcome explicit?
- Scope: is the target repo/file/page/module clear?
- Audience: is it for the user, team, or agent?
- Boundaries: what must not change?
- Inputs: are logs, screenshots, files, data, or URLs provided?
- Workflow: should the agent inspect first, plan first, implement directly, or stop for approval?
- Verification: what proves success?
- Reporting: what should the agent return?
- Weight: is the prompt overbuilt or under-specified?
- Routing: does it need domain skills, browser checks, review, research, or brainstorming?

## Rewrite Output

Default:

```markdown
## Diagnosis

- [high-signal issues]

## Improved Prompt

[ready-to-copy prompt]

## Notes

[why this weight and structure]
```

For broad prompts, provide:

- short version
- standard version
- heavy version
- when to use each

## Compression Rules

When the user wants a shorter prompt:

- keep goal, boundary, and verification
- delete roleplay unless it changes quality
- delete generic instructions the agent already follows
- preserve anti-goals for risky tasks
- preserve stop conditions and human gates
