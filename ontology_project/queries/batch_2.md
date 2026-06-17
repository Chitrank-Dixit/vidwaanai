# Batch 2: Concepts & Philosophy (50 Queries)

**Focus**: Abstract concepts, philosophical terms, and spiritual practices.
**Output Format**: Strict JSON for Neo4j ingestion.

## JSON Schema Requirement
For all queries, append this instruction:
> **Output Format**: Provide the response **ONLY** as a valid JSON object with the following structure.
> ```json
> {
>   "nodes": [
>     {
>       "id": "concept:unique_id",
>       "label": "Concept",
>       "properties": {
>         "name_en": "English Name",
>         "name_sa": "Sanskrit Name",
>         "definition": "...",
>         "category": "..."
>       }
>     }
>   ],
>   "relationships": [...]
> }
> ```

---

## 1. Perplexity Pro (20 Queries)
*Fact retrieval for definitions.*

### Core Purusharthas (Goals of Life)
1.  "Define **Dharma** in the context of the Mahabharata. List its types (Sva-dharma, Sanatana-dharma)."
2.  "Define **Artha** (Wealth/Purpose) and its legitimate pursuit guidelines in the Shastras."
3.  "Define **Kama** (Desire) and its boundaries according to Dharma texts."
4.  "Define **Moksha** (Liberation) and list its synonyms (Mukti, Nirvana, Kaivalya)."

### Yoga & Sadhanas
5.  "List the **Ashtanga Yoga** limbs (Yama, Niyama, Asana, etc.) with brief definitions."
6.  "Define **Karma Yoga** as explained in Bhagavad Gita Chapter 3."
7.  "Define **Bhakti Yoga** and the nine forms of devotion (Navavidha Bhakti)."
8.  "Define **Jnana Yoga** and the four qualifications (Sadhana Chatushtaya)."
9.  "Define **Raja Yoga** and its focus on meditation (Dhyana)."

### Metaphysics
10. "Define **Brahman** (Ultimate Reality) vs **Atman** (Self) in Advaita Vedanta."
11. "Define **Maya** (Illusion) and its two powers (Avarana, Vikshepa)."
12. "Define **Prakriti** and **Purusha** in Samkhya philosophy."
13. "Define the three **Gunas** (Sattva, Rajas, Tamas) and their characteristics."
14. "Define **Karma** (Law of Cause and Effect) and its three types (Sanchita, Prarabdha, Agami)."
15. "Define **Samsara** (Cycle of Birth/Death) and its cause."

### Rituals & Practices
16. "Define **Yajna** (Sacrifice) and its distinction from **Puja** (Worship)."
17. "Define **Tapas** (Austerity) and examples of famous tapasvis."
18. "Define **Dana** (Charity) and its importance in Kali Yuga."
19. "Define **Dhyana** (Meditation) and different objects of meditation."
20. "Define **Samadhi** (Absorption) and its stages (Savikalpa, Nirvikalpa)."

---

## 2. Gemini Pro (15 Queries)
*Structural modeling and classification.*

### Classification
21. "Create a hierarchy for **Yoga** paths. Is Hatha Yoga a subset of Raja Yoga? Structure it."
22. "Classify the **Vedas** (Rig, Sama, Yajur, Atharva) and their sub-sections (Samhita, Brahmana, Aranyaka, Upanishad)."
23. "Model the structure of the **Prasthana Trayi** (Three Sources: Upanishads, Brahma Sutras, Gita)."
24. "Classify the **Puranas** into Sattvic, Rajasic, and Tamasic categories."
25. "Model the five **Koshas** (Sheaths of the Self) from Taittiriya Upanishad."

### Process Modeling
26. "Model the process of **Creation (Srishti)** according to the Puranas (Brahma's role)."
27. "Model the process of **Dissolution (Pralaya)** and its types (Naimittika, Prakrita)."
28. "Structure the **Warnas** (Social Classes) and their traditional duties (Varna-dharma)."
29. "Structure the **Ashramas** (Stages of Life) and their associated goals."
30. "Model the **Chakras** (Energy Centers) and their associated elements/deities."

---

## 3. ChatGPT Plus (15 Queries)
*Normalization and Synthesis.*

### Normalization
31. "Standardize Sanskrit terms to IAST: 'Dharma', 'Karma', 'Moksha', 'Gnana', 'Vedas', 'Puranas'."
32. "Standardize Yoga terms: 'Pranayam', 'Asana', 'Samadhi', 'Dhyan', 'Pratyahara'."
33. "Resolve aliases for **Soul**: 'Atma', 'Jiva', 'Jivatma', 'Purusha'. Map to `concept:atman` or distinct concepts if necessary."
34. "Resolve aliases for **God**: 'Ishvara', 'Bhagavan', 'Paramatma', 'Deva'. Clarify distinctions or map to `concept:ishvara`."
35. "Standardize names of the **Mahavidyas** (Kali, Tara, Sodashi, etc.)."

### Synthesis
36. "Synthesize the concept of **Avatarhood**. What conditions require an Avatar? (Gita 4.7-8)."
37. "Synthesize: The relationship between **Karma** and **Reincarnation (Punaranjanma)**. Link nodes."
38. "Synthesize: The debate between **Dualism (Dvaita)** and **Non-Dualism (Advaita)** regarding the soul's relation to God."
39. "Check consistency: Is **Ahimsa** (Non-violence) a Yama or Niyama? Verify source (Patanjali)."
40. "Synthesize: The concept of **Guru** (Teacher). Link to 'Disciple' and 'Knowledge'."
41. "Synthesize: The 4 **Mahavakyas** (Great Sayings) of the Upanishads. Link each to its Veda."
42. "Synthesize: The **Triple Gunas** effects on food (Sattvic, Rajasic, Tamasic food)."
43. "Synthesize: The role of **Agni** in a Yajna (Mouth of Gods relationship)."
44. "Synthesize: The paths to **Moksha**. Link Jnana, Bhakti, Karma, and Raja yoga as paths."
45. "Synthesize: The definition of **Bhakti**. Is it an emotion or a discipline? Create attributes."
