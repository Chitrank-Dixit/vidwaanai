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

### Verse 1 (Mahabharat 0.2881)
- **Original**: उनका वह झब्द बड़ा भयंकर हुआ। इसके अन्तर सफेद घोड़ोंसे युक्त उत्तम रथमें बैठे हुए श्रीकृष्ण महाराज और अर्जुनने भी अलोकिक झड्लू बजाये। श्रीकृष्ण पहाराजने
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2881)
- **Original**: उनका वह झब्द बड़ा भयंकर हुआ। इसके अन्तर सफेद घोड़ोंसे युक्त उत्तम रथमें बैठे हुए श्रीकृष्ण महाराज और अर्जुनने भी अलोकिक झड्लू बजाये। श्रीकृष्ण पहाराजने
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2882)
- **Original**: 890 संक्षिप्त महाभारत [ भीष्पपर्व पाकझ्रजन्य नामक, अर्जुनने देवदत्त नामक और भयानक
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2882)
- **Original**: 890 संक्षिप्त महाभारत [ भीष्पपर्व पाकझ्रजन्य नामक, अर्जुनने देवदत्त नामक और भयानक
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2883)
- **Original**: हुए इन कौस्वोंकों देख ।' इसके बाद पृथापुत्र अर्जुनने उन दोनों कर्मवाले भौमसेनने पौण्डू नामक महाशद्धू बजाया । कुल्तीपुत्र
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2883)
- **Original**: हुए इन कौस्वोंकों देख ।' इसके बाद पृथापुत्र अर्जुनने उन दोनों कर्मवाले भौमसेनने पौण्डू नामक महाशद्धू बजाया । कुल्तीपुत्र
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2884)
- **Original**: ही. सेनाओँमें स्थित ताऊ-चाचोंको, दादों-परदादोंकों, सहदेवने सुघोष और मणिपुष्पक नामक जद्धू बजाये। श्रेष्ठ
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2884)
- **Original**: ही. सेनाओँमें स्थित ताऊ-चाचोंको, दादों-परदादोंकों, सहदेवने सुघोष और मणिपुष्पक नामक जद्धू बजाये। श्रेष्ठ
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2885)
- **Original**: मित्रोंको, ससुरोंको और सुहृदोंको भी देखा। उन उपस्थित घनुषवाले काशिराज और महारथी झिखण्डी एवं धृष्टसुप्न
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2885)
- **Original**: मित्रोंको, ससुरोंको और सुहृदोंको भी देखा। उन उपस्थित घनुषवाले काशिराज और महारथी झिखण्डी एवं धृष्टसुप्न
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2886)
- **Original**: सम्पूर्ण बचुओंको देखकर बे कुन्तीपुत्र अजुन अत्यन्त तथा राजा बिराट और अजेय सात्यकि, राजा हुपद एवं
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2886)
- **Original**: सम्पूर्ण बचुओंको देखकर बे कुन्तीपुत्र अजुन अत्यन्त तथा राजा बिराट और अजेय सात्यकि, राजा हुपद एवं
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2887)
- **Original**: करुणासे युक्त होकर “झोक करते हुए यह- वचन ड्रौपदीके पाँचों पुत्र और बड़ी: भुजाबाले सुभद्गापुत्र
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2887)
- **Original**: करुणासे युक्त होकर “झोक करते हुए यह- वचन ड्रौपदीके पाँचों पुत्र और बड़ी: भुजाबाले सुभद्गापुत्र
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2888)
- **Original**: 24--27
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2888)
- **Original**: 24--27
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2889)
- **Original**: । अभिमन्यु-इन सभीने, राजन्‌! अलग-अलग झज्ब
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2889)
- **Original**: । अभिमन्यु-इन सभीने, राजन्‌! अलग-अलग झज्ब
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2890)
- **Original**: अर्जुन बोले--कृष्ण ! युद्धकषेत्रमें डटे हुए युद्ध अभिलाषी बजाये। उस भयानक झब्दने आकाझ और पृथ्वीको भी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2890)
- **Original**: अर्जुन बोले--कृष्ण ! युद्धकषेत्रमें डटे हुए युद्ध अभिलाषी बजाये। उस भयानक झब्दने आकाझ और पृथ्वीको भी
- **Translation**: 

---

