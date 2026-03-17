---
name: repo-config
description: Generate, validate, and maintain the supported repository config used by code review workflows.
---

# Purpose

Use this skill to create or update the canonical repository mapping file:

- `config/supported-repos.yaml`

This config is the source of truth for supported repositories that review agents and git artifact skills must use.

# When to Use

Use this skill when:
- the config file does not exist
- a new repository must be added
- a repository path or default branch changes
- the code reviewer needs to resolve a repo name to a local path
- validating that a requested repo is supported

# Required Config Shape

```yaml
version: 1

defaults:
  remote: origin
  default_base_branch: main
  artifact_root: artifacts/reviews

repos:
  repo-name:
    local_path: C:/dev/repo-name
    default_base_branch: main
    remote: origin
    language_hint: python