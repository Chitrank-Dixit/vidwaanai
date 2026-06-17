# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.12921)
- **Original**: 47 पाताल समनुप्राप्तस्ततो वेदशिरा मुनि:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12922)
- **Original**: प्राप्रवानेतदखिलेंं स च॒ प्रमतये ददों
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12923)
- **Original**: 48 दर्त प्रमतिना चैतज्ञातुकर्णाय थीमते । जातुकर्णेन चैवोक्तमन्येषां पुण्यकर्मणाम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12924)
- **Original**: 49 पुलस््यतवरदानेन ममाप्येतत्स्मृति गतम्‌। मयापि तु्य॑ मैत्रेय यथावत्कथितं त्विदम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12925)
- **Original**: 50 त्वमप्येतच्छिनीकाय कलेरन्ते वदिष्यसि
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12926)
- **Original**: 51 इत्येतत्परम॑ गुहां कलिकल्मघनाझनम्‌ । यः श्रृणोति नरो भक्त्या सर्वपापै: प्रमुच्यते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12927)
- **Original**: 52 समस्ततीर्थरत्रानानि. समस्तामरसंस्तुति: । कृता तेन भवेदेतद्य: श्रूणोति दिने दिने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12928)
- **Original**: 53 कपिलादानजनित॑ पुण्यम्रत्यन्तदुर्लभम्‌ भुत्वैतस्थ दहाध्यायानवाप्रोति न संशय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12929)
- **Original**: "4 बस्त्वेतत्सकलं श्रूणोति पुरुष: कृत्वा मनस्यच्युतं चष्ठ अंश 4744 करनेसे और पितृगणको पिण्ड देनेसे अपने पितामहोंको तारता हुआ पुरुष जिस पुण्यका भागी होता है वही पुण्य अक्तिपूर्वक इस पुराणका एक अध्याय सुननेसे प्राप्त हो जाता है ।
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12930)
- **Original**: यह पुराण संसारसे भयभीत हुए पुरुषोंक्त्र अति उत्तम रक्षक, अत्यत्त श्रवणयोग्य तथा पतित्रोंमें परम उत्तम है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12931)
- **Original**: यह मनुष्योंके दुःस्वप्लोंको नष्ट करनेवाल्म, सम्पूर्ण दोषोंको टूर करनेवाल्म्र, माज़लिक वस्तुओमें परम माड्नलिक और सत्तान तथा सम्पत्तिका देनेखाला है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12932)
- **Original**: इस आर्थपुराणको सबसे पहले भगवान्‌ ब्रह्माजीने ऋभुको सुनाया था। ऋभने प्रियवतकों सुनाया और प्रियत्रतने भागुरिसे कहा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12933)
- **Original**: फिर इसे भागुरिने स्तम्भमित्रको, स्तम्भमित्री दधीचिको, द्धीचिने सारस्वटदकों और सारस्वतने भृगुको सुनाया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12934)
- **Original**: तथा भृगुने पुरुकुत्ससे, पुर्कुत्सने नर्मदासे और नर्मदाने घृतराष्ट्र एले पूरणनागसे कहा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12935)
- **Original**: हे ट्विज ! इन दोनोंने यह पुणण नागराज वासुकिकों सुनाया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12936)
- **Original**: जासुकिने वत्सको, बत्सने अश्वतरकों, अश्वतरने कम्बलको और कम्बलने एह्ापुत्रको सुनाया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12937)
- **Original**: इसी समय मुनिजर वेदशिय पावाललोकमें पहुँचे, उन्होंने यह समस्त पुराण प्राप्त किया और फिर प्रमतिकों सुनाया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12938)
- **Original**: प्रमतिने उसे परम बुद्धिमान्‌ जातुकर्णकों दिया तथा जातुकर्णे . अन्यान्य पृण्यज्ञीक महात्माओंको सुनाया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12939)
- **Original**: [ पूर्व-जन्ममें सारस्वतके मुख्ससे सुना हुआ यह पुराण ] पुलस्त्यजीके वरदानसे मुझे भी स्गरण रह गया। सो मैने ज्यॉ-का-स्यों तुम्हें सुना दिया । अब तुम भी कलियुगके अन्तमें इसे शिनीककों सुनाओगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12940)
- **Original**: जो पुरुष इस अति गुह्य और कलि-कल्मष-नाशक पुराणको भक्तिपूर्वक सुनता है यह सब्र पापोंसे मुक्त हो जाता है
- **Translation**: 

---

