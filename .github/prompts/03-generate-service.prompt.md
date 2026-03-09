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