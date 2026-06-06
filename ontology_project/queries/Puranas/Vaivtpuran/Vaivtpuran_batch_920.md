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

### Verse 1 (Vaivtpuran 543.16714)
- **Original**: यरं॑ च कण्टके यास॑ वर॑च विषभक्षणम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16715)
- **Original**: हरिभकछिविहोनानां. न सकल नाशकारणम्‌ । स्वयं नष्टों भ्र्िहीनों बुद्धिभेदें करोति च
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16716)
- **Original**: - + आरीकृष्णजन्यमखण्ड * 735 कद कु श् अड कऋ ऋक अ ऋड ऋ कक ऊभ्ऊ क #क कक कक का कऊ कबरक फक अर क कक कु क कक इक क बरक अक ऋ शक कक कब क अक क शक कद कक ऊ 5 अं रा. है इसी कारण विद्वान लोग उसे 'राम'
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16717)
- **Original**: अन्यान्य योगग्रन्थोंमें अन्त नहीं मिलता; इसी कहते हैं। रमाका रमणस्थान होनेके कारण राम-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16718)
- **Original**: कारण विद्वान्‌ लोग उसका नाम 'अनन्त' बतलाते तत्त्ववेत्ता 'राम' बतलाते हैं।'रा' लक्ष्मीवाची और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16719)
- **Original**: हैं। 'मुकु' अध्ययमान, निर्माण और मोक्षबाचक “म' ईश्वरबाचक है; इसलिये मनीषीगण लक्ष्मीपतिको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16720)
- **Original**: है; उसे जो देवता देता है, उसी कारण बह 'राम' कहते हैं। सहस्रों दिव्य नामोंके स्मरणसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16721)
- **Original**: “मुकुन्द' कहा जाता है।'मुकु' वेदसम्मत भक्तिस्सपूर्ण जो फल प्राप्त होता है, वह फल निश्चय ही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16722)
- **Original**: प्रेमयुक्त वचनको कहते हैं; उसे जो भक्तोंको देता “राम' शब्दके उच्चारणमात्रसे मिल जाता है*।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16723)
- **Original**: है वह “मुकुन्द' कहलाता है। चूँकि वे मधु विद्वानोंका कथन है कि “नार' शब्दका अर्थ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16724)
- **Original**: दैत्यका हनन करनेवाले हैं, इसलिये उनका एक सारूप्य-मुक्ति है; उसका जो देवता 'अयन' है,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16725)
- **Original**: नाम 'मधुसूदन' है। यों संतलोग बेदमें विभिन्न उसे 'नारायण' कहते हैं। किये हुए पापको “नार'
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16726)
- **Original**: अर्थका प्रतिपादन करते हैं। 'मधु' नपुंसकलिड्र और गमनकों “अयन' कहते हैं। उन पापोंका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16727)
- **Original**: तथा किये हुए शुभाशुभ कर्म और माध्वीक जिससे गमन होता है, वही ये “नारायण” कहे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16728)
- **Original**: (महुएकी शराब)-का वाचक है; अत: उसके जाते हैं। एक बार भी 'नारायण' शब्दके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16729)
- **Original**: तथा भक्तोंके कर्मोके सूदन करनेवालेको 'मधुसूदन' उच्चारणसे मनुष्य तीन सौ कल्पोंतक गड़ा आदि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16730)
- **Original**: कहते हैं। जो कर्म परिणाममें अशुभ और समस्त तीर्थोंमें स्‍्नानके फलका भागी होता है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16731)
- **Original**: भ्रान्तोंके लिये मधुर है उसे 'मधु' कहते हैं, उसका “नार' को पुण्य मोक्ष और “अयन' को अभीष्ट
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16732)
- **Original**: जो 'सूदन' करता है; वही “मधुसूदन' है। ज्ञान कहते हैं। उन दोनोंका ज्ञान जिससे हो, “कृषि' उत्कृष्टटाची, “ण' सद्भधक्तिवाचक वे ही ये प्रभु “नारायण' हैं। और “अ' दातृवाचक है; इसीसे विद्वानूलोग उन्हें जिसका चारों वेदों, पुराणों, शास्त्रों तथा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16733)
- **Original**: “कृष्ण' कहते हैं। परमानन्दके अर्थमें 'कृषि' और अड्'डुरो भक्तिवृक्षतष्य भक्तसब्रेन. वर्धते । पर हरिकथालापपीयूषासेचनेन च
- **Translation**: 

---

