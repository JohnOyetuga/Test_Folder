---
description: "Use when preparing, drafting, or making Git commits in this workspace. Draft a commit message and get explicit approval before committing."
---
# Commit Message Workflow

- When changes are ready to commit, review the exact staged diff and draft a concise commit message that accurately describes it.
- Present the proposed message to the user before committing. Do not run `git commit` until the user explicitly approves that message.
- If the staged changes do not form a clear, cohesive commit, explain the issue and ask how the user wants to proceed rather than guessing.
- Do not stage, unstage, or amend changes unless the user asks.
