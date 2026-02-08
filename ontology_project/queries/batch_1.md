# Batch 1: Deities & Avatars (50 Queries)

**Focus**: Major Hindu Deities (Tridev, Tridevi) and the Avatars of Vishnu.
**Output Format**: Strict JSON for Neo4j ingestion.

## JSON Schema Requirement
For all queries, append this instruction:
> **Output Format**: Provide the response **ONLY** as a valid JSON object with the following structure. Do not include markdown code blocks or explanatory text outside the JSON.
>
> ```json
> {
>   "nodes": [
>     {
>       "id": "unique_id (e.g., deity:vishnu)",
>       "label": "Entity Type (e.g., Deity, Avatar, Character)",
>       "properties": {
>         "name_en": "English Name",
>         "name_sa": "Sanskrit Name (Devanagari)",
>         "attributes": ["attr1", "attr2"],
>         "description": "Brief description"
>       }
>     }
>   ],
>   "relationships": [
>     {
>       "source": "source_node_id",
>       "target": "target_node_id",
>       "type": "RELATIONSHIP_TYPE (e.g., IS_AVATAR_OF, CONSORT_OF, PARENT_OF)",
>       "properties": {
>         "source_text": "Scripture reference (e.g., Bhagavata Purana 1.3)"
>       }
>     }
>   ]
> }
> ```

---

## 1. Perplexity Pro (20 Queries)
*Use for fact retrieval and citing specific scriptures.*

### The Trimurti (Creation, Preservation, Destruction)
1.  "List the core attributes, vehicles (vahanas), and weapons of **Lord Vishnu** based on the Puranas."
2.  "List the core attributes, vehicles, and weapons of **Lord Shiva** based on the Puranas."
3.  "List the core attributes, vehicles, and weapons of **Lord Brahma** based on the Puranas."
4.  "Identify the primary consorts of the Trimurti (Saraswati, Lakshmi, Parvati) and their specific domains."

### The Dashavatara (Ten Avatars of Vishnu)
5.  "List the 10 canonical Avatars of Vishnu (Dashavatara) with their Sanskrit names and associated Yuga (Era)."
6.  "Describe **Matsya Avatar**: narrative significance, demon defeated (if any), and associated scripture."
7.  "Describe **Kurma Avatar**: role in Samudra Manthan and key relationships."
8.  "Describe **Varaha Avatar**: narrative of saving Bhudevi and key antagonist."
9.  "Describe **Narasimha Avatar**: narrative of Prahlada and Hiranyakashipu."
10. "Describe **Vamana Avatar**: interaction with Bali and the three steps."
11. "Describe **Parashurama Avatar**: lineage (Rishis) and key conflicts."
12. "Describe **Rama Avatar**: key family members (Dasharatha, Kaushalya) and primary antagonist."
13. "Describe **Krishna Avatar**: birth parents (Vasudeva, Devaki) and foster parents (Nanda, Yashoda)."
14. "Describe **Buddha Avatar** (in Vaishnava context): theological role related to delusion/ahimsa."
15. "Describe **Kalki Avatar**: prophesied role, vehicle, and future arrival details."

### Other Major Deities
16. "List attributes and family relationships for **Ganesha** (parents, brother, vehicle)."
17. "List attributes and family relationships for **Kartikeya/Skanda**."
18. "List attributes and forms of **Durga** (Navadurga names)."
19. "List attributes and role of **Indra** as King of Devas."
20. "List attributes and role of **Agni** (Fire God) as messenger."

---

## 2. Gemini Pro (15 Queries)
*Use for structural modeling and schema extraction.*

### Hierarchy & Classification
21. "Create a taxonomy of **Vedic Deities** (Adityas, Rudras, Vasus) identifying who belongs to which group."
22. "Model the family tree of **Shiva** and **Parvati** including children and prominent Ganas."
23. "Model the lineage of **Rama** (Surya Vamsha) going back 5 generations from Dasharatha."
24. "Model the lineage of **Krishna** (Yadava Vamsha) identifying key ancestors like Yadu."
25. "Classify the **Ashta Dikpalas** (Guardians of Directions) with their respective directions and cities."

### Comparison & Schema
26. "Compare attributes of **Vishnu** vs **Shiva** (e.g., Vertical vs Horizontal tilak, Vaishnava vs Shaiva distinctives)."
27. "Compare the role of **Hanuman** in Ramayana vs Mahabharata (relationships to Rama and Bhima)."
28. "Define the relationship attributes for `IS_AVATAR_OF`. What properties should this edge have? (e.g., partial vs full incarnation)."
29. "Define the relationship attributes for `RISHI_OF`. How to link a Rishi to a Mantra or Sookta?"
30. "Structure the **Sapta Rishis** (Seven Sages) for the current Manvantara."

---

## 3. ChatGPT Plus (15 Queries)
*Use for normalization and synthesis.*

### Normalization
31. "Standardize these names to IAST: 'Ram', 'Laxman', 'Sita', 'Hanuman', 'Ravan', 'Vibhishan', 'Kumbhakarna', 'Indrajit'."
32. "Standardize these names to IAST: 'Yudhishthir', 'Bheem', 'Arjun', 'Nakul', 'Sahadev', 'Drupadi', 'Duryodhan'."
33. "Resolve aliases for **Arjuna**: 'Partha', 'Kaunteya', 'Dhananjaya', 'Gudakesha', 'Savyasachi'. Map them all to `id: character:arjuna`."
34. "Resolve aliases for **Krishna**: 'Madhava', 'Govinda', 'Kesava', 'Vasudeva', 'Janardana'. Map them all to `id: character:krishna`."
35. "Resolve aliases for **Shiva**: 'Mahadeva', 'Shankara', 'Bholenath', 'Rudra', 'Tryambaka'. Map them all to `id: deity:shiva`."

### Synthesis & Consistency
36. "Synthesize the story of **Samudra Manthan**. List all participating Devas, Asuras, and the emerging Gems (Ratnas) as nodes."
37. "Synthesize the **Marriage of Sita**. List participants (kings), the test (Shiva Dhanush), and the outcome."
38. "Synthesize the **Birth of Pandavas**. Link each Pandava to their divine father (Dharma, Vayu, Indra, Ashvins)."
39. "Check consistency: Is **Balarama** considered an avatar of Vishnu or Shesha? Provide the most common Puranic consensus as the relationship."
40. "Check consistency: Who are the parents of **Hanuman**? (Vayu/Shiva/Kesari/Anjana). Create relationships reflecting the dual paternity mythos if applicable."
41. "Check consistency: List the weapons of **Durga** and which Deva gave each weapon."
42. "Synthesize: The **Vehicles (Vahanas)** of all major deities. Create rigid `HAS_VEHICLE` relationships."
43. "Synthesize: The **Abodes (Lokas)** of major deities (Vaikuntha, Kailash, Satyaloka). Create `RESIDES_IN` relationships."
44. "Synthesize: The **Consorts** of the Dikpalas (e.g., Indra-Shachi). Create `CONSORT_OF` relationships."
45. "Synthesize: The **Weapons (Astras)** associated with distinct deities (Sudarshana-Vishnu, Trishula-Shiva, Vajra-Indra)."
