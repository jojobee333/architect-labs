# Shared rules for all knowledge-bank workflows

## Execution requirement
You must follow the discovery order strictly.

Do not:
- skip steps
- reorder steps
- generate outputs before completing discovery

## Discovery order
1. Inspect repository structure
2. Inspect configuration
3. Inspect representative source files
4. Inspect representative test files
5. Inspect existing docs
6. Inspect existing knowledge bank files if present

## Truth handling
Distinguish:
- Observed → directly supported by code/config/docs
- Inferred → derived from strong evidence
- Recommended → suggested improvement (explicitly labeled)
- Unknown → not determinable from repository

## Evidence rules
- Prefer repository-local evidence over general knowledge
- Do not invent architecture intent
- Do not infer patterns from a single file unless clearly representative
- If evidence is partial, label as Inferred or Unknown
- If no evidence exists, explicitly state that

## Conflict handling
- Record conflicting patterns
- Do not silently normalize them

## Duplication handling
- Do not repeat the same information across files
- Place information in the most appropriate file
- Reference instead of duplicating when necessary

## Scope guidance
- Focus on representative patterns, not exhaustive enumeration
- Prioritize high-impact modules and flows
- Avoid documenting trivial or obvious code

## Drift awareness
- If existing knowledge conflicts with repository evidence, record the conflict
- Do not silently overwrite conflicting information
- Prefer updating or annotating over deleting when uncertain

## Completion checks
Before finishing, verify:

- all required files are present
- each file has a distinct purpose
- required sections are present
- uncertainty is explicitly logged
- conflicting patterns are recorded
- content is grounded in repository evidence
- no significant duplication exists across files
- no major repository area is unaccounted for
- outputs are usable without re-reading the repository