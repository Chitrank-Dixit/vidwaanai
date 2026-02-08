# Vedic Ontology Specification

**Version**: 1.0
**Project**: Vidwaan AI - Multi-LLM Ontology
**Date**: 2026-02-08

## 1. Overview
This ontology models the domain of Indian Scriptures, including Deities, Avatars, Characters, Concepts, and their inter-relationships.

## 2. Class Hierarchy
- **Thing**
    - **Entity**
        - **Deity** (e.g., Vishnu, Shiva)
            - **Avatar** (e.g., Rama, Krishna)
        - **Character** (e.g., Arjuna, Ravana)
        - **Location** (e.g., Ayodhya)
        - **Event** (e.g., Kurukshetra War)
    - **Concept** (e.g., Dharma, Karma)
    - **Scripture** (e.g., Ramayana)
        - **Verse**

## 3. Object Properties (Relationships)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `IS_AVATAR_OF` | `Avatar` | `Deity` | Represents an incarnation relationship. |
| `CONSORT_OF` | `Deity` | `Deity` | Represents spousal relationship. |
| `IS_PARENT_OF` | `Entity` | `Entity` | Biological or divine parentage. |
| `KILLED_BY` | `Entity` | `Entity` | Antagonistic termination. |
| `MENTIONS` | `Verse` | `Entity` | Textual reference. |

## 4. Usage Examples (SPARQL)

### Query: Find all Avatars of Vishnu
```sparql
PREFIX : <http://vidwaan.ai/ontology/>
SELECT ?avatar ?name
WHERE {
    ?avatar :IS_AVATAR_OF :deity_vishnu .
    ?avatar rdfs:label ?name .
}
```

### Query: Find Deities who are Consorts
```sparql
PREFIX : <http://vidwaan.ai/ontology/>
SELECT ?deity1 ?deity2
WHERE {
    ?deity1 :CONSORT_OF ?deity2 .
}
```
