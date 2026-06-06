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

### Verse 1 (Mahabharat 0.4361)
- **Original**: साथ हो जानेसे ही उसकी इतनी झक्ति बढ़ गयी है। अब तो उसने प्रसन्न चित्तसे उसकी प्रशंसा करते हुए कहा, “कर्ण !
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4361)
- **Original**: साथ हो जानेसे ही उसकी इतनी झक्ति बढ़ गयी है। अब तो उसने प्रसन्न चित्तसे उसकी प्रशंसा करते हुए कहा, “कर्ण !
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4362)
- **Original**: पाष्डबॉंकी सेनामें आपके और कर्णके हिस्सेका ही भाग रह तुन्हारा जैसा विचार है, मैं वैसा ही करूँगा। छकड़े तुम्हारे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4362)
- **Original**: पाष्डबॉंकी सेनामें आपके और कर्णके हिस्सेका ही भाग रह तुन्हारा जैसा विचार है, मैं वैसा ही करूँगा। छकड़े तुम्हारे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4363)
- **Original**: गया है, उसे आप कर्णके साथ मिलकर आज एक साथ नष्ट बाण लेकर चलेंगे तथा हम सब राजास्प्रेग तुम्हारे पीछे-पीछे कर दीजिये। आप कोई ऐसी युक्ति कीजिये, जिससे पाज्चाल अलेंगे।' राजन्‌ ! कर्णसे ऐसा कहकर आपका पुत्र बड़ी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4363)
- **Original**: गया है, उसे आप कर्णके साथ मिलकर आज एक साथ नष्ट बाण लेकर चलेंगे तथा हम सब राजास्प्रेग तुम्हारे पीछे-पीछे कर दीजिये। आप कोई ऐसी युक्ति कीजिये, जिससे पाज्चाल अलेंगे।' राजन्‌ ! कर्णसे ऐसा कहकर आपका पुत्र बड़ी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4364)
- **Original**: और सृक्षयोंके सहित कुन्तीके पुत्र ज्ीघ्र ही नष्ट हो जायें। विनयसे महास्थी शल्यके-पास गया और उससे प्रेमपूर्वक
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4364)
- **Original**: और सृक्षयोंके सहित कुन्तीके पुत्र ज्ीघ्र ही नष्ट हो जायें। विनयसे महास्थी शल्यके-पास गया और उससे प्रेमपूर्वक
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4365)
- **Original**: कर्ण रथ्ियोंमें श्रेष्ठ है और आप सारथियोंमें सर्वोत्तम हैं। कहने रूगा, मद्रेशर ! आप सत्य्रत, महाभाग और
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4365)
- **Original**: कर्ण रथ्ियोंमें श्रेष्ठ है और आप सारथियोंमें सर्वोत्तम हैं। कहने रूगा, मद्रेशर ! आप सत्य्रत, महाभाग और
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4366)
- **Original**: आप दोनोंका-सा संयोग संसारमें नं कधी हुआ है न होगा वक्ताऑमें अप्रगण्य हैं। मैं सिर झुकाकर अत्यन्त विनयके
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4366)
- **Original**: आप दोनोंका-सा संयोग संसारमें नं कधी हुआ है न होगा वक्ताऑमें अप्रगण्य हैं। मैं सिर झुकाकर अत्यन्त विनयके
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4367)
- **Original**: ही। जिस भ्रकार श्रीकृष्ण सब अवस्थाओमें अर्जुनकी रक्षा
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4367)
- **Original**: ही। जिस भ्रकार श्रीकृष्ण सब अवस्थाओमें अर्जुनकी रक्षा
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4368)
- **Original**: सारधि बन जानेपर तो कर्ण इन्द्र और समस्त देवताओंके
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4368)
- **Original**: सारधि बन जानेपर तो कर्ण इन्द्र और समस्त देवताओंके
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4369)
- **Original**: छिये भी अजेय हो जायगा, फिर पाण्डबॉंकी तो बात ही
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4369)
- **Original**: छिये भी अजेय हो जायगा, फिर पाण्डबॉंकी तो बात ही
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4370)
- **Original**: क्या है?”
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4370)
- **Original**: क्या है?”
- **Translation**: 

---

