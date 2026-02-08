# Phase 3: Response Normalization & Conflict Resolution

**Goal**: Standardize data formats and resolve discrepancies in the aggregated output.

## 1. Normalization (ChatGPT / Gemini)

### Template: Entity ID Standardization
> **Prompt**:
> "I have a list of entities from different LLM responses. Normalize their IDs and Names to follow this convention:
> - **ID**: snake_case, prefixed with type (e.g., `deity:shiva`, `character:arjuna`).
> - **Name**: PascalCase, standard IAST transliteration if applicable.
>
> **Input List**:
> [INSERT_JSON_LIST_OF_NODES]
>
> **Output**: Clean JSON list with corrected IDs and Names."

### Template: Relationship Normalization
> **Prompt**:
> "Standardize the relationship types in this list to UPPER_SNAKE_CASE.
> Ensure consistent usage (e.g., convert `father_of` to `IS_PARENT_OF`, `avatar` to `IS_AVATAR_OF`).
>
> **Input List**:
> [INSERT_JSON_LIST_OF_RELATIONSHIPS]
>
> **Output**: Clean JSON list."

---

## 2. Conflict Resolution (Gemini Pro)

### Template: Attribute Merge
> **Prompt**:
> "I have two conflicting entries for the entity `[ENTITY_ID]`.
>
> **Entry A**:
> ```json
> [ENTRY_A_JSON]
> ```
>
> **Entry B**:
> ```json
> [ENTRY_B_JSON]
> ```
>
> **Task**: Merge these into a single comprehensive JSON object.
> - If values contradict, favor the Puranic/Scriptural source.
> - Combine list attributes (e.g., names, weapons) without duplicates."

### Template: Ontology Alignment
> **Prompt**:
> "Source A categorizes `Ashvatthama` as a `Character`. Source B categorizes him as `Immortal` (Chiranjivi) and `Partial Avatar`.
>
> **Task**: creating a unified node definition that captures all valid categories/types.
> Suggest the best primary `type` and add others as attributes or secondary labels."
