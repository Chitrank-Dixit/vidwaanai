# Batch 3: Locations & Events (50 Queries)

**Focus**: Sacred Geography, Cosmology, and Mythological History (Itihasa).
**Output Format**: Strict JSON for Neo4j ingestion.

## JSON Schema Requirement
For all queries, append this instruction:
> **Output Format**: Provide the response **ONLY** as a valid JSON object.
> ```json
> {
>   "nodes": [
>     {
>       "id": "location:unique_id",
>       "label": "Location (or Event)",
>       "properties": {
>         "name_en": "...",
>         "type": "City/Mountain/River/War/Era",
>         "significance": "..."
>       }
>     }
>   ],
>   "relationships": [...]
> }
> ```

---

## 1. Perplexity Pro (20 Queries)
*Fact retrieval for places and events.*

### Sacred Geography (Bhu-loka)
1.  "List the **Sapta Puri** (Seven Holy Cities) (Ayodhya, Mathura, Maya, Kashi, Kanchi, Avantika, Dvaravati)."
2.  "List the **Char Dham** (Himalayan) pilgrimage sites (Yamunotri, Gangotri, Kedarnath, Badrinath)."
3.  "List the **12 Jyotirlingas** and their locations."
4.  "List the **51 Shakti Peethas** (major ones) and their locations."
5.  "Describe **Mount Kailash**: location and significance as Shiva's abode."
6.  "Describe **Varanasi** (Kashi): significance for Moksha and Shiva."
7.  "Describe **Prayagraj**: significance of Triveni Sangam."
8.  "List the **Sapta Sindhu** (Seven Sacred Rivers) mentioned in Vedas."

### Cosmology (Other Lokas)
9.  "List the **14 Lokas** (7 Upper, 7 Lower) in Hindu Cosmology."
10. "Describe **Vaikuntha**: the abode of Vishnu."
11. "Describe **Svarga**: the abode of Indra (Heaven) and its residents."
12. "Describe **Patala**: the netherworld and its residents (Nagas)."
13. "Describe **Naraka** (Hell) and its role in Karma."
14. "Describe **Mount Meru**: the cosmic mountain at the center of the universe."

### Events
15. "Describe the **Kurukshetra War**: participants, duration (18 days), and outcome."
16. "Describe the **Samudra Manthan** (Churning of Ocean): purpose and list of emerging items."
17. "Describe **Ram's Exile** (Vanavasa): duration (14 years) and key locations visited (Chitrakoot, Panchavati)."
18. "Describe **Sita Swayamvara**: location (Mithila) and the test."
19. "Describe **Lanka Dahan** (Burning of Lanka) by Hanuman."
20. "Describe **Daksha Yajna** and the self-immolation of Sati."

---

## 2. Gemini Pro (15 Queries)
*Modeling timelines and geography.*

### Timeline Modeling
21. "Model the **Chatur Yugas** (Satya, Treta, Dvapara, Kali) with their durations and characteristics."
22. "Create a timeline of the **Ramayana** events (Birth -> Exile -> War -> Pattabhisheka)."
23. "Create a timeline of the **Mahabharata** events (Game of Dice -> Exile -> War -> Parikshit's birth)."
24. "Model the **Manvantara** cycles. Who is the current Manu?"
25. "Model the life cycle of **Brahma** (Kalpa, Day/Night of Brahma)."

### Spatial Modeling
26. "Map the route of **Rama's Exile** from Ayodhya to Lanka. List nodes as 'Location' and edges as 'NEXT_STOP'."
27. "Map the **Pandavas' Exile**. Key locations visited."
28. "Model the geography of the **Universe** (Brahmanda). How do Lokas stack vertically?"
29. "Network of **Holy Rivers**: Link Ganga, Yamuna, Saraswati to their origins and confluences."
30. "Classify **Forests** (Aranyas) mentioned in epics (Dandakaranya, Naimisharanya, Khandavaprastha)."

---

## 3. ChatGPT Plus (15 Queries)
*Normalization and Synthesis.*

### Normalization
31. "Standardize Location names: 'Kashi'/'Banaras'/'Varanasi', 'Prayag'/'Allahabad', 'Avantika'/'Ujjain'."
32. "Standardize River names: 'Ganges'/'Ganga', 'Indus'/'Sindhu'."
33. "Resolve aliases for **Lanka**: Is it Sri Lanka? Standardize as `location:lanka`."
34. "Standardize Event names: 'Mahabharat War', 'Kurukshetra War'. Map to `event:kurukshetra_war`."
35. "Standardize Loka names: 'Heaven'/'Svarga', 'Hell'/'Naraka'."

### Synthesis
36. "Synthesize: The **Curse of Gandhari**. Who was cursed (Krishna) and what was the result?"
37. "Synthesize: The **Game of Dice** (Dyuta). Participants and the critical turning point (Draupadi Vastraharan)."
38. "Synthesize: The **Gita Upadesha**. Location (Kurukshetra), timing (Start of war), participants (Krishna, Arjuna)."
39. "Check consistency: Location of **Dvaraka**. Is it submerged? Note this in attributes."
40. "Synthesize: **River Saraswati**. Mythological status vs physical river debates. Model as 'River' with 'status: invisible/dried'."
41. "Synthesize: The **Ashvamedha Yajna** performed by Yudhishthira. Purpose and significance."
42. "Synthesize: The **Birth of Ganges**. Descent from heaven (Shiva's locks) to earth (Bhagiratha's penance)."
43. "Synthesize: The **Burning of Khandava Forest**. Arjuna and Krishna's role."
44. "Synthesize: The **Putrakameshti Yajna** of Dasharatha. Outcome (Birth of 4 sons)."
45. "Synthesize: The **Great Departure** (Mahaprasthan) of the Pandavas. Climb to Himalayas."
