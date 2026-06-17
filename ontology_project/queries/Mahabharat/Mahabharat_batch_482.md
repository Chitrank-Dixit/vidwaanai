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

### Verse 1 (Mahabharat 0.4811)
- **Original**: किया और 'तथास्तु' कहकर -धनुषको नवाते हुए थे है
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4811)
- **Original**: किया और 'तथास्तु' कहकर -धनुषको नवाते हुए थे है
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4812)
- **Original**: युधिप्ठिसे बोले--'राजन्‌ ! अब मेरे गुणोंको सुनिये-- >
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4812)
- **Original**: युधिप्ठिसे बोले--'राजन्‌ ! अब मेरे गुणोंको सुनिये-- >
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4813)
- **Original**: पिनाकधारी भगवान्‌ झंकरको छोड़कर दूसरा कोई भी मेरे “9, द लि 0 नल्लअडननओ
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4813)
- **Original**: पिनाकधारी भगवान्‌ झंकरको छोड़कर दूसरा कोई भी मेरे “9, द लि 0 नल्लअडननओ
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4814)
- **Original**: समान धनुर्थर नहीं है; मेरी जीरताका उन्होंने भी अनुमोदन घर किनबक-. ध्ब्बड हज
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4814)
- **Original**: समान धनुर्थर नहीं है; मेरी जीरताका उन्होंने भी अनुमोदन घर किनबक-. ध्ब्बड हज
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4815)
- **Original**: नष्ट कर डाछँगा। मेरे चरणोंमें रथ और ध्वजाके चिह्न हैं। तर लक हि - शुट्न-जसा वर यह युद्ध पहुंच जाय तो उसे काई भी वही +- नर 8 कक 45 रजत सकता। कहर, दक्ष एव और पक्िय-हुर क्घ
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4815)
- **Original**: नष्ट कर डाछँगा। मेरे चरणोंमें रथ और ध्वजाके चिह्न हैं। तर लक हि - शुट्न-जसा वर यह युद्ध पहुंच जाय तो उसे काई भी वही +- नर 8 कक 45 रजत सकता। कहर, दक्ष एव और पक्िय-हुर क्घ
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4816)
- **Original**: विज्ञाओंके राजाओंका मैंने संहार किया है।' 'कृष्ण ! अब भागकर एक कोस दूर आ बैठा है, तू क्‍या उल्लाहना
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4816)
- **Original**: विज्ञाओंके राजाओंका मैंने संहार किया है।' 'कृष्ण ! अब भागकर एक कोस दूर आ बैठा है, तू क्‍या उल्लाहना
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4817)
- **Original**: हम दोनों विजवज्ञाली रथपर बैठकर सूतपुत्र कर्णका वध देगा ? हाँ, भीमसेनको मेरी निन्‍्दा करनेका अधिकार है;
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4817)
- **Original**: हम दोनों विजवज्ञाली रथपर बैठकर सूतपुत्र कर्णका वध देगा ? हाँ, भीमसेनको मेरी निन्‍्दा करनेका अधिकार है;
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4818)
- **Original**: करनेके लिये झीप्र हीं चल दें। आज राजा युपिष्ठिर प्रसन्न क्योंकि वे समस्त संसारके प्रमुल वीरोंके साथ लड़ रहे
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4818)
- **Original**: करनेके लिये झीप्र हीं चल दें। आज राजा युपिष्ठिर प्रसन्न क्योंकि वे समस्त संसारके प्रमुल वीरोंके साथ लड़ रहे
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4819)
- **Original**: हों, मैं कर्णको अपने बाणोंसे नष्ट कर डालूँगा।' यों कहकर हैं। शन्रुओंको पीड़ा पहुँचा रहे हैं। असंख्य शुरवीरों,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4819)
- **Original**: हों, मैं कर्णको अपने बाणोंसे नष्ट कर डालूँगा।' यों कहकर हैं। शन्रुओंको पीड़ा पहुँचा रहे हैं। असंख्य शुरवीरों,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4820)
- **Original**: अर्जुन पुनः युधिष्ठिसे बोले--'आज या तो कर्णकी माता अनेकों राजाओं, रथ्ियों, घुड़सवारों तथां हजारों हाथियोंको
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4820)
- **Original**: अर्जुन पुनः युधिष्ठिसे बोले--'आज या तो कर्णकी माता अनेकों राजाओं, रथ्ियों, घुड़सवारों तथां हजारों हाथियोंको
- **Translation**: 

---

