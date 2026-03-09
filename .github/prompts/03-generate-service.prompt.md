---
name: 03-generate-service
description: Implement a service or module while respecting the existing architecture boundaries.
---

Implement a system component.

Component Name
${input:service_name:Service or module name}

Requirements
${input:requirements:Describe responsibilities and behaviors}

Implementation rules

- Respect the architecture boundaries defined in this repository.
- Keep domain logic separate from framework or transport concerns.
- Avoid hidden coupling between modules.
- Keep files focused and cohesive.

Generate the following:

1. Code implementation
2. Unit tests
3. Integration tests if applicable
4. README documentation for the component
5. Updates to any relevant ADRs


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