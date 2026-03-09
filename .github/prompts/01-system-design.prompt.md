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