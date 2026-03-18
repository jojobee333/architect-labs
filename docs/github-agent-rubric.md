# GitHub Agent Rubric (100 points)

---

## 1. Role Clarity and Scope Control — 10

Measures clarity, boundaries, and responsibility limits.

Good:
- clear purpose
- defined use cases
- explicit exclusions

Failure modes:
- mixed responsibilities
- unclear scope expansion

---

## 2. Requirement Handling and Assumption Discipline — 10

Measures handling of unknowns and avoidance of hallucination.

Good:
- assumptions explicitly listed
- unknowns acknowledged
- conservative defaults

Failure modes:
- inventing requirements
- ignoring missing inputs

---

## 3. Architectural Judgment and Tradeoff Analysis — 12

Measures decision-making quality.

Good:
- 2–3 viable options
- context-aware tradeoffs
- simplicity bias

Failure modes:
- defaulting to patterns blindly
- no comparison of options

---

## 4. System Design Quality — 10

Measures structural coherence.

Good:
- clear boundaries
- defined interfaces
- clean data flow

Failure modes:
- tight coupling
- unclear module responsibilities

---

## 5. Implementation Readiness — 10

Measures actionability.

Good:
- file structure
- sequencing
- entry points defined

Failure modes:
- conceptual output only
- missing steps

---

## 6. Code Generation Quality — 10

Measures maintainability and alignment.

Good:
- cohesive functions
- clear layering
- low coupling

Failure modes:
- oversized files
- unclear abstractions

---

## 7. Testing Strategy and Test Quality — 10

Measures validation depth.

Good:
- core logic tested
- edge cases included
- risk-based coverage

Failure modes:
- trivial tests
- missing failure scenarios

---

## 8. Operational Excellence — 10

Measures production readiness.

Good:
- logging
- metrics
- health checks
- rollout/rollback

Failure modes:
- no observability
- no failure handling

---

## 9. Security and Safety by Default — 10

Measures secure design.

Good:
- input validation
- least privilege
- secret handling

Failure modes:
- unsafe defaults
- missing auth considerations

---

## 10. Tooling and Workflow Integration — 6

Measures fit within GitHub workflows.

Good:
- respects repo structure
- incremental edits
- CI awareness

Failure modes:
- ignores repo context
- breaks workflows

---

## 11. Documentation and Knowledge Transfer — 6

Measures artifact quality.

Good:
- README updates
- ADRs
- setup clarity

Failure modes:
- no documentation
- unclear outputs

---

## 12. Output Control, Token Efficiency, and Reliability — 8

Measures signal quality.

Good:
- phased output
- minimal viable slice
- consistent structure

Failure modes:
- verbose dumps
- unstable output

---

## Enforcement Rules

Agents must:
- state assumptions explicitly
- produce a minimal viable slice first
- use repo context before edits
- include failure cases in tests
- provide file/module-level plans

---

## Critical Fail Conditions

If any ≤ 4:
- Requirement Handling
- Implementation Readiness
- Security

→ Not production-ready