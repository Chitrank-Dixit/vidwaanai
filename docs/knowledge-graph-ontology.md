# Vedic Knowledge Graph Ontology

## Overview
This document defines the schema and ontology used in the VidwaanAI Knowledge Graph. The ontology is implemented in `src/graph/schema.py` and enforced via Neo4j constraints.

## Entity Types
Nodes in the graph are labeled with one of the following types:

| Type | Description | Examples |
|------|-------------|----------|
| **Deity** | Divine beings or gods | Agni, Indra, Shiva, Vishnu |
| **Concept** | Philosophical or metaphysical ideas | Dharma, Karma, Atman, Moksha |
| **Character** | Individuals from scriptures | Arjuna, Rama, Sita |
| **Location** | Physical or mythological places | Ayodhya, Kurukshetra, Vaikuntha |
| **Event** | Significant occurrences | Mahabharata War, Ashvamedha Yajna |
| **Text** | Scriptures or specific texts | Rig Veda, Bhagavad Gita |
| **Teaching** | Specific doctrines or instructions | Four Noble Truths, Upadesha |
| **Practice** | Spiritual or ritual practices | Yoga, Yajna, Tapas |
| **Emotion** | Emotional states or sentiments | Bhakti (Devotion), Kopa (Anger) |
| **Quality** | Attributes or Gunas | Sattva, Rajas, Tamas |
| **TimePeriod**| Chronological eras | Yuga (Kali Yuga, Satya Yuga) |

## Relationship Types
Edges in the graph represent relationships between entities:

### Hierarchical & Compositional
- **IS_A**: Inheritance (e.g., *Shiva IS_A Deity*)
- **PART_OF**: Composition (e.g., *Ayodhya PART_OF Kosala*)

### Causal & Functional
- **CAUSES**: Action leads to result (e.g., *Karma CAUSES Rebirth*)
- **LEADS_TO**: Practice leads to goal (e.g., *Yoga LEADS_TO Moksha*)
- **MANIFESTS_AS**: Avatar manifestation (e.g., *Vishnu MANIFESTS_AS Rama*)

### Social & Familial
- **PARENT_OF** / **CHILD_OF**: Genealogy
- **SPOUSE_OF**: Marital relation
- **SIBLING_OF**: Sibling relation
- **ENEMY_OF** / **ALLY_OF**: Antagonistic or supportive relations

### Spiritual & Educational
- **TEACHER_OF** / **STUDENT_OF**: Guru-Shishya tradition (e.g., *Krishna TEACHER_OF Arjuna*)
- **DEVOTEE_OF**: Bhakti relation (e.g., *Hanuman DEVOTEE_OF Rama*)
- **EXEMPLIFIES**: Character embodies concept (e.g., *Rama EXEMPLIFIES Dharma*)

### Contextual
- **MENTIONED_IN**: Entity appears in a text
- **LOCATED_AT**: Spatial association
- **HAPPENED_AT**: Event location
- **OCCURRED_DURING**: Temporal association
- **OPPOSES**: Conceptual duality (e.g., *Dharma OPPOSES Adharma*)

## Data Properties
All nodes (Entities) share a common structure:
- `id`: Unique identifier (formatted as `Type:Name`, e.g., `Deity:Agni`)
- `name`: Display name
- `description`: Optional text description (extracted from source)
- `source_verse_id`: Reference to the Veda/Gita verse where this entity was extracted

## Implementation Details
- **Code**: defined in `src/graph/schema.py` using Python Enums.
- **Constraints**: Enforced in Neo4j (ID uniqueness) via `src/graph/setup_graph.py`.
- **Extraction**: `src/graph/entity_extractor.py` uses LLM to map text to these types.
