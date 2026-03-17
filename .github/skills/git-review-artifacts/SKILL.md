---
name: git-review-artifacts
description: Resolve repo from config, fetch branch, and collect git artifacts needed for code review.
---

# Purpose

Use this skill when a review agent needs to gather branch diffs and supporting git artifacts before performing a code review.

This skill resolves a repo name using `config/repo-map.yaml`, checks out or fetches the requested branch, determines the review base, and collects review artifacts.

# Inputs

- `repo_name`: logical repo name from `config/repo-map.yaml`
- `branch_name`: target branch to review
- `base_branch` (optional): override base branch; otherwise use repo default from config

# Required Outputs

Generate or collect the following:

- repo path
- resolved remote
- resolved base branch
- merge base SHA
- target branch SHA
- changed file list
- name-status diff
- unified diff
- commit list between base and target
- optional stats summary

# Procedure

## Step 1: Resolve Repo
Read `config/repo-map.yaml` and find:
- local_path
- default_base_branch
- remote

If repo is missing, fail clearly.

## Step 2: Prepare Repo
In the resolved local path:
- verify it is a git repo
- fetch from remote
- fetch target branch
- fetch base branch

## Step 3: Determine Base
Use:
- explicit `base_branch` input if provided
- otherwise `default_base_branch` from config

Then compute:
- merge base between `remote/base_branch` and `remote/branch_name`

## Step 4: Collect Artifacts
Collect:
- `git status --short`
- `git rev-parse` for base and target
- `git diff --name-only`
- `git diff --name-status`
- `git diff --stat`
- full unified diff
- `git log --oneline` between merge base and target

## Step 5: Return Review Context
Return a concise summary containing:
- repo path
- review range
- changed files
- commit count
- artifact file locations if saved

# Suggested Commands

```bash
git fetch origin
git fetch origin <branch_name>
git fetch origin <base_branch>
git merge-base origin/<base_branch> origin/<branch_name>
git diff --name-only <merge_base>..origin/<branch_name>
git diff --name-status <merge_base>..origin/<branch_name>
git diff --stat <merge_base>..origin/<branch_name>
git diff <merge_base>..origin/<branch_name>
git log --oneline <merge_base>..origin/<branch_name>