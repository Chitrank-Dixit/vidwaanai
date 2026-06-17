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

### Verse 1 (Vaivtpuran 543.15634)
- **Original**: जन्मतक मेढक होता है। जो झूठे ही अपनेको इसके लिये यत्रपूर्वक मेरे नामोंका संकीर्तन करना
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15635)
- **Original**: बिद्ठानू कहकर गाँवकी पुरोहिती करता है; वह चाहिये। जो देव-मूर्तियोंकी चोरी करता है, वह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15636)
- **Original**: सात जन्मोंतक नेवला, एक जन्ममें कोढ़ी और सात जन्मॉतक अंधा, दरिद्र, रोगग्रस्त, बहरा और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15637)
- **Original**: तीन जन्मोंतक गिरगिट होता है। फिर एक जन्ममें कुबड़ा होता है। जो नराधम ब्राह्मण और देव- बार होनेके बाद वृक्षकी चींटी होता है। तत्पश्चात्‌ प्रतिमाकों देखकर उन्हें नमस्कार नहीं करता; वह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15638)
- **Original**: क्रमश: शूद्र, वैश्य, क्षत्रिय और ब्राह्मण होता जबतक जीता है तबतक अपवित्र यवन होता है। चारों वर्णोंमें कन्या बेचनेवाला मानव तामिलल है। जो ब्राह्मणमफो आया हुआ देखकर उठकर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15639)
- **Original**: नरकमें जाता है और वहाँ तबतक निवास करता स्वागत नहीं करता; वह निश्चितरूपसे महापापी है, जबतक सूर्य-चन्द्रमाकी स्थिति रहती है। होता है। जो शिवका द्वेषी तथा देव-प्रतिमापर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15640)
- **Original**: इसके बाद वह मांस बेचनेवाला व्याध होता है। चढ़े हुए द्रव्यसे जीविका-निर्वाह करनेवाला है,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15641)
- **Original**: तत्पश्चात्‌ पूर्वजन्ममें जो जैसा होता है, उसीके वह सात जन्मतक मुर्गा होता है। जो अज्ञानी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15642)
- **Original**: अनुसार उसे व्याधि आ घेरती है। मेरे नामको पितरों और देवताओंके वेदोक्त पूजनका विनाश
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15643)
- **Original**: बेचनेवाले ब्राह्मणकौ मुक्ति नहीं होती-यह ध्रुव करता है, बह पापी रौरब नरकमें जाता है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15644)
- **Original**: है। मृत्युलोकमें जिसके स्मरणमें मेरा नाम वहाँ एक हजार वर्षतक यातना भोगनेके पश्चात्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15645)
- **Original**: आता ही नहीं; बह अज्ञानी एक जन्ममें गौकी तीन जन्मोंतक तीर्थकाक होता है। फिर तीन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15646)
- **Original**: योनिमें उत्पन्न होता है। इसके बाद बकरा, फिर जन्मोंतक किसी तीर्थमें सियारकी योनिमें उत्पन्न
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15647)
- **Original**: मेढ़ा और सात जन्मोंतक भैंसा होता है। जो होकर मुर्देकी लाश खाता है। ब्रजेश्वर! वही
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15648)
- **Original**: मानव महान्‌ षड्यन्त्री, कुटिल और धर्महीन होता पापी तीन जन्मोंतक तीर्थोमें शवकी रक्षा तथा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15649)
- **Original**: है; वह एक जन्ममें तेली होकर फिर कुम्हार कर्मानुसार मुर्दोकी कफनखसोटी करता है। जो होता हैं। जो झूठा कलंक लगानेवाला और मूर्ख नित्य दम्भपूर्वक देवताकी पूजा करके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15650)
- **Original**: देवता एवं ब्राह्मणका निन्दक होता है, वह एक भक्तिपूर्वक गुरुका पूजन नहीं करता और न उन्हें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15651)
- **Original**: जन्ममें सोनार होकर सात जन्मोंतक धोबी होता अन्न प्रदान करता है; वह पापी देवताके शापसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15652)
- **Original**: है। जो ब्राह्मण, क्षत्रिय, वैश्य, शूद्र कुत्सित दुःखी, देवल (देवप्रतिमापर चढ़े हुए द्रव्यसे । आचरणवाले तथा पविज्नतासे रहित होते हैं, उन्हें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15653)
- **Original**: » श्रीकृष्णजन्मखण्ड * 683 45% % $ ऋ # $ 8 $ $ $ $ $ % # क क $ $ 5 % $ # $ कक 5 4 ऋ कक 44 ऋ 5 ऋ 5 % 5 कक 5 # % $ ऋ कक कर 54 6 कक 5 अ5 85 % # 8 8 दस हजार वर्षोंतक म्लेच्छयोनिमें जन्म लेना
- **Translation**: 

---

