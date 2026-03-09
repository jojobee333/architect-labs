---
name: 02-implementation-plan
description: Convert a chosen architecture into a concrete development plan and repository structure.
---

Using the architecture defined in this repository, create an implementation plan.

Include the following sections.

Milestones

Break development into logical milestones that deliver incremental value.

Repository Structure

Define the directory layout and module boundaries.

Example:

src/
domain/
application/
infrastructure/
interfaces/

Backlog

Provide a prioritized backlog in implementation order.

Each item should include:

- feature description
- dependencies
- test coverage expectations

CI/CD Plan

Define:

- build pipeline
- test stages
- deployment workflow
- rollback strategy

Architecture Decisions

List ADRs that should be created during implementation.


## Teaching Mode Requirements
When presenting any architecture, design option, or recommendation:

1. Define all important terms in plain English before using them deeply.
2. Explain the request/data flow step by step.
3. Describe each major component and its role.
4. State why this option exists and what problem it solves.
5. Include pros, cons, risks, and operational complexity.
6. Explain when this option is a good fit and when it is not.
7. Include a small example scenario showing how the system behaves.
8. Include a short analogy for a junior engineer.
9. Avoid unexplained jargon.
10. Prefer clarity and learning value over brevity.

For every option, use this exact output structure:

### Option <Name>
- Summary
- What problem it solves
- Core components
- Request flow
- Data flow
- Strengths
- Weaknesses
- Operational overhead
- Failure modes
- Best fit
- Poor fit
- Simple analogy
- Recommendation notes

## Term Glossary
Define all key terms used in the response in plain English.



