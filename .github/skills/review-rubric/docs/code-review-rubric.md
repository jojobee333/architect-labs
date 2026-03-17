# Code Review Rubric (100-Point System + Critical Fail Layer)

## 0. Critical Fail Conditions (Auto-Reject)

If any of the following are present, the PR is not mergeable regardless of score:

- Security vulnerability
- Auth or permission bypass
- Injection risk
- Sensitive data exposure
- Data corruption risk
- Unsafe migration
- Broken core functionality
- Missing tests for high-risk logic
- Silent failure of critical paths
- Swallowed critical errors that block diagnosis
- Severe regression risk in core workflows

---

## 1. Correctness & Functional Behavior — 20 pts

### 18–20
- All requirements implemented correctly
- Edge cases handled
- No obvious regressions

### 14–17
- Core behavior correct
- Minor edge cases missing

### 10–13
- Works in common cases
- Edge cases unclear or partially broken

### 1–9
- Major logic flaws or high regression risk

### 0
- Broken or fails core requirement

---

## 2. Readability & Maintainability — 15 pts

### 14–15
- Clear naming
- Focused functions/classes
- Low cognitive load

### 11–13
- Mostly readable
- Small maintainability issues

### 8–10
- Noticeable complexity
- Mixed responsibilities
- Awkward structure

### 1–7
- Hard to follow
- Tangled logic
- Brittle organization

### 0
- Unmaintainable

---

## 3. Architecture & Design Quality — 15 pts

### 14–15
- Strong boundaries
- Good abstraction choices
- Logic placed correctly
- Extensible without excess complexity

### 11–13
- Mostly sound design
- Minor layering or abstraction issues

### 8–10
- Works but structure is brittle or inconsistent

### 1–7
- Poor separation of concerns
- Leaky abstractions
- Misplaced logic

### 0
- Fundamentally unsound design

---

## 4. Test Quality & Coverage — 15 pts

### 14–15
- Happy path, edge cases, and failure modes covered
- Regression tests included where needed

### 11–13
- Happy path covered
- Some edge cases covered
- Limited failure-mode testing

### 8–10
- Mostly happy path only
- Meaningful gaps remain

### 1–7
- Minimal, weak, or brittle tests
- Risky logic under-tested

### 0
- No meaningful tests

---

## 5. Error Handling & Resilience — 10 pts

### 9–10
- Failure modes handled clearly
- Errors propagated or reported usefully
- No silent failures

### 7–8
- Most important errors handled
- Minor gaps

### 5–6
- Basic guards present
- Important failure paths not handled well

### 1–4
- Weak error handling
- Runtime failure likely

### 0
- No meaningful error handling

---

## 6. Performance & Efficiency — 10 pts

### 9–10
- No obvious waste
- Appropriate algorithms and data access patterns
- Avoids repeated or unnecessary work

### 7–8
- Acceptable with minor inefficiencies

### 5–6
- Noticeable inefficiencies
- Acceptable only at small scale

### 1–4
- Poor patterns such as repeated heavy work, N+1 access, excessive rendering, or wasteful loops

### 0
- Severe performance issue

---

## 7. Security & Data Safety — 5 pts

### 5
- Input handling, auth, secrets, and data protection are sound

### 4
- Minor low-risk concern

### 2–3
- Meaningful weakness exists

### 1
- Serious security concern

### 0
- Critical vulnerability

---

## 8. Consistency with Standards — 5 pts

### 5
- Matches project conventions and patterns

### 4
- Minor inconsistencies

### 2–3
- Several deviations

### 1
- Significant mismatch

### 0
- Ignores standards

---

## 9. Documentation & Developer Experience — 5 pts

### 5
- Docs/comments/config guidance updated where needed
- Complex logic explained well

### 4
- Minor gaps

### 2–3
- Some missing docs or unclear usage impact

### 1
- Major documentation gaps

### 0
- No documentation where clearly needed

---

## 10. Observability & Debuggability — 5 pts

### 5
- Logs, errors, metrics, or tracing are sufficient to diagnose behavior

### 4
- Mostly traceable
- Small visibility gaps

### 2–3
- Limited diagnostic support

### 1
- Poor visibility

### 0
- Opaque or silent behavior

---

## Decision Model

- If any Critical Fail Condition exists → REJECT
- Else if score is 85–100 → APPROVE
- Else if score is 70–84 → REQUEST CHANGES
- Else → REJECT

### High-Risk Areas
Apply stricter standards if the change touches:
- Auth
- Payments
- Migrations
- Concurrency
- Persistence logic

For high-risk changes:
- Testing should generally be at least 12/15
- Correctness must be strong
- No category should show severe weakness without explanation