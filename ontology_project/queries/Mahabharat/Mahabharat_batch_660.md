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

### Verse 1 (Mahabharat 0.6591)
- **Original**: पढ़ाता-लिखाता और समस्त स्कोक-स्ययहारोंका ज्ञान कराता इतिहास है, जो आइ्लिरसकुलमें उत्पन्न हुए चिरकारीके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.6591)
- **Original**: पढ़ाता-लिखाता और समस्त स्कोक-स्ययहारोंका ज्ञान कराता इतिहास है, जो आइ्लिरसकुलमें उत्पन्न हुए चिरकारीके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.6592)
- **Original**: है। पिता ही धर्म है, पिता ही स्वर्ग है और पिता ही सबसे बड़ा वृत्ान्तसे सम्बन्ध रखता है। कहते हैं, महर्षि गौतमके एक
- **Translation**: 

---

### Verse 4 (Mahabharat 0.6592)
- **Original**: है। पिता ही धर्म है, पिता ही स्वर्ग है और पिता ही सबसे बड़ा वृत्ान्तसे सम्बन्ध रखता है। कहते हैं, महर्षि गौतमके एक
- **Translation**: 

---

### Verse 5 (Mahabharat 0.6593)
- **Original**: तप है। पिताके प्रसन्न होनेपर सम्पूर्ण देवता प्रसन्न हो जाते हैं। खिरकारी नामवाल्ा पुत्र था, जो बड़ा बुद्धिमान्‌ था। वह
- **Translation**: 

---

### Verse 6 (Mahabharat 0.6593)
- **Original**: तप है। पिताके प्रसन्न होनेपर सम्पूर्ण देवता प्रसन्न हो जाते हैं। खिरकारी नामवाल्ा पुत्र था, जो बड़ा बुद्धिमान्‌ था। वह
- **Translation**: 

---

### Verse 7 (Mahabharat 0.6594)
- **Original**: पिता जो कुछ भी कहता है, वह पुत्रके लिये आशौर्वांद है। यदि चिरकाल्तक जागता और सोता था। किसी कार्यपर बहुत
- **Translation**: 

---

### Verse 8 (Mahabharat 0.6594)
- **Original**: पिता जो कुछ भी कहता है, वह पुत्रके लिये आशौर्वांद है। यदि चिरकाल्तक जागता और सोता था। किसी कार्यपर बहुत
- **Translation**: 

---

### Verse 9 (Mahabharat 0.6595)
- **Original**: पिता प्रसन्न होकर पुत्र॒का अभिनन्‍्दन करे तो वह समस्त पापोंसे देस्तक विचार करता था और चिरविलूम्बके बाद ही काम पूरा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.6595)
- **Original**: पिता प्रसन्न होकर पुत्र॒का अभिनन्‍्दन करे तो वह समस्त पापोंसे देस्तक विचार करता था और चिरविलूम्बके बाद ही काम पूरा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.6596)
- **Original**: मुक्त हो जाता है। वृक्ष अपने फूछ और फल्होंको छोड़ देते हैं; करता था, इसलिये सब ल्छोग उसे चिरकारी कहने लगे । जो
- **Translation**: 

---

### Verse 12 (Mahabharat 0.6596)
- **Original**: मुक्त हो जाता है। वृक्ष अपने फूछ और फल्होंको छोड़ देते हैं; करता था, इसलिये सब ल्छोग उसे चिरकारी कहने लगे । जो
- **Translation**: 

---

### Verse 13 (Mahabharat 0.6597)
- **Original**: किंतु पिता बड़े-से-बड़े संकटमें भी स्नेहके कारण पुत्रको नहीं दूस्तककी बात नहीं सोच सकते, ऐसे मन्दबुद्धि मनुष्य उसे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.6597)
- **Original**: किंतु पिता बड़े-से-बड़े संकटमें भी स्नेहके कारण पुत्रको नहीं दूस्तककी बात नहीं सोच सकते, ऐसे मन्दबुद्धि मनुष्य उसे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.6598)
- **Original**: छोड़ता। अतः पुत्रके लिये पिताका स्थान बहुत ऊँचा है। अस्तु, आहृसी और नासमझ कहते थे। एक दिन गौतमने अपनी
- **Translation**: 

---

### Verse 16 (Mahabharat 0.6598)
- **Original**: छोड़ता। अतः पुत्रके लिये पिताका स्थान बहुत ऊँचा है। अस्तु, आहृसी और नासमझ कहते थे। एक दिन गौतमने अपनी
- **Translation**: 

---

### Verse 17 (Mahabharat 0.6599)
- **Original**: पिताके गौरवपर तो मैंने विचार कर लिया, अब माताके खीका व्यभिचार देखकर बड़ा कोप किया और अपने दूसरे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.6599)
- **Original**: पिताके गौरवपर तो मैंने विचार कर लिया, अब माताके खीका व्यभिचार देखकर बड़ा कोप किया और अपने दूसरे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.6600)
- **Original**: विषयमें सोचता हूँ। पुत्रोंको आज्ञा देकर चिरकारीसे कहा-- “बेटा ! तू अपनी इस जैसे अरणी अप्रिकी उत्पत्तिका कारण है, उसी प्रकार पापिनी माताको मार डाल ।' बिना बिचारे ही यह आज्ञा देकर
- **Translation**: 

---

### Verse 20 (Mahabharat 0.6600)
- **Original**: विषयमें सोचता हूँ। पुत्रोंको आज्ञा देकर चिरकारीसे कहा-- “बेटा ! तू अपनी इस जैसे अरणी अप्रिकी उत्पत्तिका कारण है, उसी प्रकार पापिनी माताको मार डाल ।' बिना बिचारे ही यह आज्ञा देकर
- **Translation**: 

---

