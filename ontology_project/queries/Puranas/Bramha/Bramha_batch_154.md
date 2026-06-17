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

### Verse 1 (Bramha 0.3061)
- **Original**: प्रणाम किया और कैलासपर्वतकी यात्रा की। वहाँ सगर चिन्ता करने लगे कि 'हमारे सब पुत्र
- **Translation**: 

---

### Verse 2 (Bramha 0.3062)
- **Original**: पहुँचकर पवित्र हो बालक भगीरथने तपस्याका ब्राह्मणके शापसे रसातलमें नष्ट हो गये। एक
- **Translation**: 

---

### Verse 3 (Bramha 0.3063)
- **Original**: निश्चय किया और भगवान्‌ शंकरकों सम्बोधित बचा था, वंह भी वनमें चला गया। इस समय
- **Translation**: 

---

### Verse 4 (Bramha 0.3064)
- **Original**: करके इस प्रकार कहा-“प्रभो! मैं बालक हूँ, मेरी क्‍या गति होगी?! मेरी बुद्धि भी बालककों ही है और आप भी असमज्ञाके एक पुत्र था, जो अंशुमान्‌ नामसे
- **Translation**: 

---

### Verse 5 (Bramha 0.3065)
- **Original**: अपने मस्तकपर बाल चन्द्रमाको धारण करते हैं। विख्यात हुआ। यद्यपि अंशुमान्‌ अभी बालक था
- **Translation**: 

---

### Verse 6 (Bramha 0.3066)
- **Original**: मैं कुछ भी नहीं जानता। आप मेरे इस अनजानपनसे तो भी राजाने उसे बुलाकर अपना कार्य बतलाया।
- **Translation**: 

---

### Verse 7 (Bramha 0.3067)
- **Original**: ही प्रसन्न होइये। अमरेश्वर! जो लोग बाणीसे अंशुमानने भगवान्‌ कपिलको आराधना को और
- **Translation**: 

---

### Verse 8 (Bramha 0.3068)
- **Original**: मनसे और क्रियासे कभी मेरा उपकार करते हैं घोड़ा ले आकर राजा सगरको दे दिया। इससे बह
- **Translation**: 

---

### Verse 9 (Bramha 0.3069)
- **Original**: तथा हितसाधनमें संलग्न रहते हैं, उनका कल्याण यज्ञ पूर्ण हुआ। अंशुमानके तेजस्वी पुत्रका नाम
- **Translation**: 

---

### Verse 10 (Bramha 0.3070)
- **Original**: करनेके लिये मैं उमासहित आपको प्रणाम करता दिलीप था। दिलीपके पुत्र परम बुद्धिमान्‌ भगीरथ
- **Translation**: 

---

### Verse 11 (Bramha 0.3071)
- **Original**: हूँ। आप देवता आदिके लिये भी पूज्य हैं। जिन हुए। भगीरथने जब अपने समस्त पितामहोंकी
- **Translation**: 

---

### Verse 12 (Bramha 0.3072)
- **Original**: पूर्वजोंने मुझे अपने सगोत्र और* समानधमकि दुर्गतिका हाल सुना, तब उन्हें बड़ा दुःख हुआ।
- **Translation**: 

---

### Verse 13 (Bramha 0.3073)
- **Original**: रूपमें उत्पन्न किया और पाल-पोसकर बड़ा उन्होंने नृपश्रेष्ठ सगरसे विनयपूर्वक पूछा--' महाराज!
- **Translation**: 

---

### Verse 14 (Bramha 0.3074)
- **Original**: बनाया, भगवान्‌ शिव उनका अभीष्ट मनोरथ पूर्ण उन सबका उद्धार कैसे होगा? राजाने उत्तर
- **Translation**: 

---

### Verse 15 (Bramha 0.3075)
- **Original**: करें। मैं बालचद्रका मुकुट धारण करनेवाले दिया--'बेटा! यह तो भगवान्‌ कपिल ही जानते
- **Translation**: 

---

### Verse 16 (Bramha 0.3076)
- **Original**: भगवान्‌ शंकरको नित्य प्रणाम करता हूँ।' हैं।' यह सुनकर बालक भगीरथ रसातलमें गये
- **Translation**: 

---

### Verse 17 (Bramha 0.3077)
- **Original**: . भगीरथके यों कहते ही भगवान्‌ शिव उनके और कपिलको नमस्कार करके अपना सब
- **Translation**: 

---

### Verse 18 (Bramha 0.3078)
- **Original**: सामने प्रकट हो गये और बोले--'महामते ! तुम मनोरथ उन्हें कह सुनाया। कपिल मुनि बहुत
- **Translation**: 

---

### Verse 19 (Bramha 0.3079)
- **Original**: निर्भय होकर कोई वर माँगो। जो वस्तु देवताओंके देरतक ध्यान करके बोले--' राजन्‌ ! तुम तपस्याद्वारा
- **Translation**: 

---

### Verse 20 (Bramha 0.3080)
- **Original**: लिये भी सुलभ नहीं है, बह भी मैं तुम्हें निश्चय भगवान्‌ शंकरकी आराधना करों और, उनकी
- **Translation**: 

---

