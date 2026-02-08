# Vidwaan AI Ontology Maintenance Plan

**Version**: 1.0
**Effective Date**: 2026-02-08

## 1. Governance Roles

| Role | Responsibilities | User/Agent |
|------|------------------|------------|
| **Ontology Owner** | Final approval of schema changes, defining domain scope. | User (Chitrank) |
| **Maintainer** | Executing batch queries, running validation scripts, deploying updates. | User / CI Bot |
| **Contributor** | Suggesting new entities, resolving conflicts. | Multi-LLM Agents |

## 2. Update Schedule

### Quarterly Review (Q-Review)
- **Scope**: Review all "Concept" definitions for clarity. Check for new academic/scriptural interpretations.
- **Action**: Run `validate_ontology.py` on the full dataset.

### On-Demand Updates
- Triggered by: New feature requirements (e.g., adding "Ayurveda" domain).
- **Process**:
    1.  Create new Query Batch (Phase 2).
    2.  Execute & Normalize (Phase 3).
    3.  Merge & Deploy (Phase 4 & 5).

## 3. Change Management

### Adding New Entities
1.  Add prompt to `ontology_project/queries/`.
2.  Generate JSON response.
3.  Run `aggregate_responses.py`.

### Modifying Schema
1.  Update `ontology_project/domain_specification.md`.
2.  Update internal `validate_ontology.py` rules if necessary.
3.  Refactor existing graph data using Neo4j Cypher migrations.

## 4. Versioning Strategy
We follow **Semantic Versioning** for the ontology:
- **Major (1.0.0)**: Breaking changes to core class hierarchy (e.g., merging `Deity` and `Avatar`).
- **Minor (1.1.0)**: Adding new sub-domains (e.g., adding `MedicinalPlant` class).
- **Patch (1.0.1)**: Corrections to data or attributes (e.g., fixing spelling of a Sanskrit name).

## 5. Feedback Loop
- **Log Issues**: Use `ontology_project/issues.md` (to be created) to log missing entities or wrong relationships.
- **LLM Feedback**: Use Perplexity to periodically fact-check random samples of the graph.
