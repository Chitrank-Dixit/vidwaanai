# Domain Specification: Indian Scriptures & Vedic Philosophy

## 1. Domain Scope
The ontology models the knowledge contained in Indian scriptures (Vedas, Upanishads, Puranas, Epics - Ramayana & Mahabharata) and the philosophical concepts derived from them.

**Goal**: To create a structured knowledge graph that enables:
- Semantic search (e.g., "Find verses about Dharma in the Gita").
- Reasoning (e.g., "How is Krishna related to the concept of Avatar?").
- Cross-referencing between different scriptures.

## 2. Core Entity Types

### 2.1. Divine & Mythological Beings
- **Deity**: A god or goddess (e.g., *Vishnu*, *Shiva*, *Lakshmi*).
    - Attributes: `name`, `sanskrit_name`, `domain` (e.g., Preservation), `vehicles`, `weapons`, `consort`.
- **Avatar**: An incarnation of a deity (e.g., *Rama*, *Krishna*, *Narasimha*).
    - Attributes: `incarnation_of` (Deity), `purpose`, `era` (Yuga).
- **Character**: A named individual in the scriptures (e.g., *Arjuna*, *Ravana*, *Hanuman*).
    - Attributes: `role` (Protagonist, Antagonist, Sage), `lineage`, `caste` (optional/contextual).

### 2.2. Philosophical Concepts
- **Concept**: Abstract ideas or principles (e.g., *Dharma*, *Karma*, *Moksha*, *Atman*, *Brahman*).
    - Attributes: `definition`, `sanskrit_term`, `related_concepts`.
- **Practice**: Spiritual or ritual practices (e.g., *Yoga*, *Yajna*, *Tapasya*).
    - Attributes: `goal`, `method`, `practitioners`.

### 2.3. Locations & Events
- **Location**: Geographical or mythological places (e.g., *Ayodhya*, *Lanka*, *Vaikuntha*, *Kurukshetra*).
    - Attributes: `type` (City, Forest, Celestial Realm), `significance`.
- **Event**: Major occurrences (e.g., *Kurukshetra War*, *Samudra Manthan*, *Ram's Exile*).
    - Attributes: `participants`, `outcome`, `location`.

### 2.4. Textual Entities
- **Scripture**: The work itself (e.g., *Bhagavad Gita*).
    - Attributes: `author`, `language`, `period`.
- **Verse**: A specific unit of text (e.g., *BG 2.47*).
    - Attributes: `chapter`, `verse_number`, `text`, `translation`.

## 3. Relationships

### 3.1. Entity-to-Entity
- `IS_AVATAR_OF` (Avatar -> Deity)
- `IS_CONSORT_OF` (Deity -> Deity)
- `IS_PARENT_OF` / `IS_CHILD_OF` (Character -> Character)
- `KILLED_BY` / `KILLED` (Character -> Character)
- `MENTOR_OF` / `DISCIPLE_OF` (Character -> Character)
- `LOCATED_IN` (Location -> Location/Realm)
- `HAPPENED_AT` (Event -> Location)
- `PARTICIPATED_IN` (Character -> Event)

### 3.2. Text-to-Entity
- `MENTIONS` (Verse -> Entity/Concept)
    - *Example*: "Verse 2.47 MENTIONS Karma".
- `DEFINES` (Verse -> Concept)
    - *Example*: "Verse 2.20 DEFINES Atman".
- `APPEARS_IN` (Character -> Scripture)

### 3.3. Concept-to-Concept
- `IS_A` (Hierarchical: *Bhakti Yoga* IS_A *Yoga*)
- `RELATED_TO` (Associative: *Karma* RELATED_TO *Rebirth*)
- `LEADS_TO` (Causal: *Dharma* LEADS_TO *Moksha*)

## 4. Use Cases
1.  **Genealogy Tracking**: Tracing lineages (Vamshavali) in Puranas.
2.  **Concept Mapping**: Visualizing how 'Dharma' is interpreted differently in Ramayana vs. Mahabharata.
3.  **Narrative QA**: Answering "Who killed Ravana and using what weapon?"
4.  **Thematic Search**: Finding all verses related to 'Duty' across all ingested texts.
