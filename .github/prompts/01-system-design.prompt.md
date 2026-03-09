---
name: 01-system-design
description: Generate a production-grade system architecture from requirements and constraints.
---

Design a production-grade software system.

System Name
${input:system_name:System name}

Requirements
${input:requirements:List functional and non-functional requirements}

Constraints
${input:constraints:List constraints such as team size, timeline, cloud platform, scale expectations}

Process

1. Identify assumptions and missing information.
2. Propose 2–3 viable architecture options.
3. Compare the options using the following criteria:
   - complexity
   - scalability
   - operational burden
   - development velocity
4. Recommend the best option and explain the reasoning.

Provide the following outputs:

- Assumptions
- Architecture options with tradeoffs
- Recommended architecture
- Module or service decomposition
- API or event contracts
- Data model
- Deployment topology
- Observability strategy
- Testing strategy
- Top 5 technical risks