---
name: refresh-knowledge-bank
description: Refresh an existing repository knowledge bank based on current repository evidence.
---

# Use case
Use when the repository already has a knowledge bank and repository state may have changed.

# Workflow
1. Follow shared knowledge-bank rules.
2. Read knowledge-bank config.
3. Read all existing knowledge files first.
4. Read the templates for target structure.
5. Discover changed or relevant repository areas.
6. Update files in place.
7. Preserve valid human-authored content.
8. Move resolved uncertainties out of open-questions.md and add new ones.

# Refresh behavior
- Update stale sections.
- Preserve valid sections.
- Do not rewrite unchanged files unnecessarily.