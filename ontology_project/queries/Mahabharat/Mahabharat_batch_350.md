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

### Verse 1 (Mahabharat 0.3491)
- **Original**: ! 4 54)!
- **Translation**: 

---

### Verse 2 (Mahabharat 0.3491)
- **Original**: ! 4 54)!
- **Translation**: 

---

### Verse 3 (Mahabharat 0.3492)
- **Original**: ] 5 तो दे दिया, किंतु पीछे उसे पूर्ण नहीं किया ।' दु्षोधिनके ऐसा कहनेपर आचार्य श्रेणने 1 कुछ खित्र होकर कहा, राजन! तु ऐसा
- **Translation**: 

---

### Verse 4 (Mahabharat 0.3492)
- **Original**: ] 5 तो दे दिया, किंतु पीछे उसे पूर्ण नहीं किया ।' दु्षोधिनके ऐसा कहनेपर आचार्य श्रेणने 1 कुछ खित्र होकर कहा, राजन! तु ऐसा
- **Translation**: 

---

### Verse 5 (Mahabharat 0.3493)
- **Original**: . जे! नहीं समझना चाहिये । मैं तो सदा तुम्हारा प्रिय 28 करनेकी ही चेष्टा करता हूँ। किंतु क्या करूँ ? 5 04-77. अर्जुन जिसकी रक्षा करते हों, उसे देवता, गये। उस समय अर्जुनका झन्ुओंके साथ- ऐसा घोर युद्ध हुआ, जैसा पहले न तो कभी देखा गया और न सुना ही गया था। महाराज ! इधर, आचार्य ड्रोणने चक्रव्यूहका निर्माण असुरं गन्धर्व, सर्प, राक्षस तंथा सम्पूर्ण स्थेक भी नहीं जीत
- **Translation**: 

---

### Verse 6 (Mahabharat 0.3493)
- **Original**: . जे! नहीं समझना चाहिये । मैं तो सदा तुम्हारा प्रिय 28 करनेकी ही चेष्टा करता हूँ। किंतु क्या करूँ ? 5 04-77. अर्जुन जिसकी रक्षा करते हों, उसे देवता, गये। उस समय अर्जुनका झन्ुओंके साथ- ऐसा घोर युद्ध हुआ, जैसा पहले न तो कभी देखा गया और न सुना ही गया था। महाराज ! इधर, आचार्य ड्रोणने चक्रव्यूहका निर्माण असुरं गन्धर्व, सर्प, राक्षस तंथा सम्पूर्ण स्थेक भी नहीं जीत
- **Translation**: 

---

### Verse 7 (Mahabharat 0.3494)
- **Original**: रोमाक्षकारी तुमुल युद्ध छिड़ गया। सकते। जहाँ विश्वविधाता भगवान्‌ श्रीकृष्ण और अर्जुन हैं,
- **Translation**: 

---

### Verse 8 (Mahabharat 0.3494)
- **Original**: रोमाक्षकारी तुमुल युद्ध छिड़ गया। सकते। जहाँ विश्वविधाता भगवान्‌ श्रीकृष्ण और अर्जुन हैं,
- **Translation**: 

---

### Verse 9 (Mahabharat 0.3495)
- **Original**: . ब्रेणाचार्यद्वारा सुरक्षित उस दुर्दव्य व्यूहपर भीमसेनकों वहाँ झंकरके सिवा और किसका बल काम दे सकता है ?
- **Translation**: 

---

### Verse 10 (Mahabharat 0.3495)
- **Original**: . ब्रेणाचार्यद्वारा सुरक्षित उस दुर्दव्य व्यूहपर भीमसेनकों वहाँ झंकरके सिवा और किसका बल काम दे सकता है ?
- **Translation**: 

---

### Verse 11 (Mahabharat 0.3496)
- **Original**: आगे करके पाण्डबॉने आक्रमण/ किया।7 सात्य॑कि; तात ! इस समय तुमसे सत्य कहता हूँ, यह कभी अन्यथा
- **Translation**: 

---

### Verse 12 (Mahabharat 0.3496)
- **Original**: आगे करके पाण्डबॉने आक्रमण/ किया।7 सात्य॑कि; तात ! इस समय तुमसे सत्य कहता हूँ, यह कभी अन्यथा
- **Translation**: 

---

### Verse 13 (Mahabharat 0.3497)
- **Original**: चेकितान, नहीं हो सकता--आज पाण्डवपक्षके किसी एक ओएष्ठ
- **Translation**: 

---

### Verse 14 (Mahabharat 0.3497)
- **Original**: चेकितान, नहीं हो सकता--आज पाण्डवपक्षके किसी एक ओएष्ठ
- **Translation**: 

---

### Verse 15 (Mahabharat 0.3498)
- **Original**: बृहत्क्षत्र, महारथीका नाझ करूँगा। आज वह व्यूह बनाऊँया, जिसे
- **Translation**: 

---

### Verse 16 (Mahabharat 0.3498)
- **Original**: बृहत्क्षत्र, महारथीका नाझ करूँगा। आज वह व्यूह बनाऊँया, जिसे
- **Translation**: 

---

### Verse 17 (Mahabharat 0.3499)
- **Original**: युधामन्यु, देवता भी नहीं तोड़ सकते
- **Translation**: 

---

### Verse 18 (Mahabharat 0.3499)
- **Original**: युधामन्यु, देवता भी नहीं तोड़ सकते
- **Translation**: 

---

### Verse 19 (Mahabharat 0.3500)
- **Original**: लेकिन अर्जुनकों तुम झिसी भी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.3500)
- **Original**: लेकिन अर्जुनकों तुम झिसी भी
- **Translation**: 

---

