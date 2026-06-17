# Multi-LLM Query Templates

## 1. Perplexity Pro (Fact Retrieval & Verification)

**Goal**: Extract raw facts, lists of entities, and verify relationships with citations.

### Template A: Entity Extraction
> Prompt:
> "Acting as an expert Indologist, list all [ENTITY_TYPE] mentioned in [SCRIPTURE_NAME].
> For each, provide:
> 1. Name (English & Sanskrit if available)
> 2. Key attributes (e.g., Parentage, Weapons, Vehicle)
> 3. Evaluation of their role (e.g., Major/Minor, Protagonist/Antagonist)
> Source from reliable academic or scriptural translations."

### Template B: Relationship Verification
> Prompt:
> "Verify the relationship between [ENTITY_A] and [ENTITY_B] in Hindu mythology.
> Does [ENTITY_A] [RELATIONSHIP] [ENTITY_B]?
> Cite specific verses or chapters from [SCRIPTURE_NAME] if possible."

---

## 2. Gemini Pro (Schema Extraction & Modeling)

**Goal**: Convert unstructured text or lists into structured JSON/Graph schemas.

### Template C: JSON Extraction
> Prompt:
> "You are a Knowledge Graph Engineer. Convert the following text about [TOPIC] into a strict JSON format matching this schema:
> ```json
> {
>   "entities": [{"id": "str", "type": "str", "name": "str", "attributes": {}}],
>   "relationships": [{"source": "id", "target": "id", "type": "str"}]
> }
> ```
> Text:
> [INSERT_TEXT_HERE]"

### Template D: Ontology Extension
> Prompt:
> "Based on the concept of [CONCEPT_NAME] (e.g., Dharma), suggest 5 sub-concepts and 5 related concepts that should be added to the ontology.
> Format as a hierarchy."

---

## 3. ChatGPT Plus (Normalization & Synthesis)

**Goal**: Clean up data, standardize names, and merge conflicting information.

### Template E: Name Normalization
> Prompt:
> "Standardize the following list of names to IAST (International Alphabet of Sanskrit Transliteration) if possible, or common English usage.
> Resolve aliases (e.g., 'Partha' -> 'Arjuna').
> List:
> [INSERT_LIST_HERE]"

### Template F: Conflict Resolution
> Prompt:
> "Source A says [CLAIM_A]. Source B says [CLAIM_B].
> Synthesize a single description that acknowledges the variation or identifies the most canonical version according to [SCRIPTURE_NAME]."

---

## 4. Unified Gemini Pro (Fact Retrieval, Schema Extraction, Normalization & Synthesis)

**Goal**: Execute a complete Indological fact extraction, name normalization, and graph modeling workflow in a single step using Gemini.

### Unified Template:
> "You are an expert Indologist and a Knowledge Graph Engineer. Perform fact retrieval, name normalization, and relationship modeling for the following query.
> 
> Query: [INSERT_QUERY_HERE]
> 
> Output the response ONLY as a valid JSON object matching the schema below. Do not include markdown code blocks or explanatory text outside the JSON.
> 
> JSON Schema:
> {
>   "nodes": [
>     {
>       "id": "Standardized_Name (e.g. Krishna, Arjuna, Vashishtha, Lanka)",
>       "label": "Entity Type (Deity/Concept/Character/Place/Event/Text)",
>       "properties": {
>         "name_en": "Common English Name",
>         "description": "Brief description including key attributes and scriptural context"
>       }
>     }
>   ],
>   "relationships": [
>     {
>       "source": "source_node_id",
>       "target": "target_node_id",
>       "type": "RELATIONSHIP_TYPE (MENTIONS/IS_AVATAR_OF/RELATED_TO/LOCATED_AT/PARTICIPATED_IN)",
>       "properties": {
>         "context": "Brief explanation of how they are related in the scripture"
>       }
>     }
>   ]
> }"

