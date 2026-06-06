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

### Verse 1 (Vishnu Puran 0.8601)
- **Original**: इनके अनन्तर पृथिबीगें दस शुज्ज्बंशीय राजागण होंगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8602)
- **Original**: उनमें पहला पुष्यमित्र नामक सेनापति अपने स्वामीको मारकर स्वय॑ राज्य करेगा, उसका पुत्र अग्रिमित्र छोगा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8603)
- **Original**: अम्रिमित्रय्त्र पूत्र सुज्येश्य, सुज्येछ्का वसुमित्र, वसुमित्रका उदक, उर्दकका पुलिल्दक, पुल्निदिकका प्लोषघसु, स्रोषलसुका वज़मित्र। वज्रमित्रका
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8604)
- **Original**: आश्रषठ ] भागवतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8605)
- **Original**: तस्मादेबभूतिः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8606)
- **Original**: इत्येते शुद्भा ह्ादशोत्तरें वर्षशरत पृथ्ित्री भोक्ष्यन्ति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8607)
- **Original**: । तत: कण्यानेषा भूर्यास्थत्ति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8608)
- **Original**: देवभूति तु शुड्टराजानं व्यसनिनं तस्वैवामात्य: काण्वो वसुदेवनामा ते निहत्य स्वयमवर्नी भोक्ष्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8609)
- **Original**: ततस्यथ पुत्रो भूमित्रस्तस्यापि नारायण:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8610)
- **Original**: नारायणात्पजस्सुश्ञर्मा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8611)
- **Original**: एते काण्वायनाश्रत्वारः पद्च- चलत्वारिशद्ठर्षाणि भूपतयो भविष्यन्ति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8612)
- **Original**: सुशर्माणं तु काण्वं तदभृत्यो बलिपुच्छकनामा हत्वान्ग्रजातीयो वसुधां भोक्ष्यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8613)
- **Original**: ततञर कृष्णनामा तदभ्राता पृथिवीपतिर्भविष्यति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8614)
- **Original**: तस्थापि पुत्र: शान्तकर्णिस्तस्थापि पूर्णोत्सड्रस्तत्पुत्रशशातकर्णिस्तस्माचलम्बोदर- स्तस्माश्ल पिलकस्ततो.. मेघस्वातिस्तत: पदुमान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8615)
- **Original**: . ततश्रारिष्टकर्मा ततो हालाहलछ;
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8616)
- **Original**: हालाहलात्पललकस्तत: पुलिन्दसेनस्ततः . सुन्दरस्ततइशातकर्णिस्तत- हिद्ववस्वातिस्ततक्ष गोपतिपुत्रस्तत्पुत्रोइलिमान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8617)
- **Original**: तस्यथापि शान्तकर्णिस्तत: शिवश्रित- स्ततश्ल॒ शिवस्कन्थस्तस्मादपि. यज्ञश्रीस्ततो द्वियज्ञस्तस्माशन्द्रभी:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8618)
- **Original**: तस्मात्युलोमाचि:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8619)
- **Original**: एतमेते त्रिशाशत्वार्यब्दशतानि घट- पश्चाशदधिकानि पृथिवीं भोश्ष्यन्ति आम्रभृत्या:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8620)
- **Original**: सप्नाभीरप्रभूतयो दूद्मा गर्दभिलाश् भूभुजो भविष्यन्ति
- **Translation**: 

---

