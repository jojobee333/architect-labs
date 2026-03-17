---
name: review-rubric
description: Shared rubric reference for code review scoring and decision rules.
---

# Purpose

This skill provides the canonical scoring model for code review.

# Source of Truth

Use:
- `docs/code-review-rubric.md`

# Instructions

When scoring a code change:
- apply critical fail conditions first
- then score all categories
- then apply the decision model
- complete scoring even if critical fails exist, for diagnostic value

Do not invent alternate scoring systems unless explicitly requested.