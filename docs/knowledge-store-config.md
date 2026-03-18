knowledge_bank:
  output_dir: ".github/knowledge"

  required_files:
    - knowledge-index.md
    - repo-overview.md
    - architecture-map.md
    - coding-conventions.md
    - test-strategy.md
    - workflow-runbook.md
    - glossary.md
    - open-questions.md

  discovery:
    config_files:
      - package.json
      - tsconfig.json
      - next.config.js
      - next.config.ts
      - vite.config.ts
      - vitest.config.ts
      - jest.config.js
      - jest.config.ts
      - .eslintrc
      - .eslintrc.js
      - .eslintrc.cjs
      - eslint.config.js
      - prettier.config.js
      - Dockerfile
      - docker-compose.yml
      - Makefile

    config_dirs:
      - .github/workflows

    source_dirs:
      - src
      - app
      - pages
      - components
      - features
      - domain
      - services
      - lib
      - hooks
      - store

    test_dirs:
      - test
      - tests
      - __tests__
      - src

    docs_dirs:
      - docs
      - .github

  generation:
    include_metadata_block: true
    preserve_existing_human_content: true
    distinguish_observed_inferred_recommended_unknown: true
    prefer_repo_local_evidence: true
    log_conflicts_in_open_questions: true

  confidence_levels:
    - low
    - medium
    - high