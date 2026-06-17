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

### Verse 1 (Vaivtpuran 4.9067)
- **Original**: साकार एवं निराकार हैं; उन तेजोरूप परमात्माको शोभा हो रही थी। ब्रह्मन्‌! वहाँ उनको एक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.9068)
- **Original**: मैं नमस्कार करता हूँ। प्रभो! आप अनिर्वचनीय, अत्यन्त अद्भुत और आश्चर्यमय तेज:पुञ्ज दिखायी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.9069)
- **Original**: व्यक्त, अव्यक्त, अद्वितीय, स्वेच्छामय तथा दिया, जो करोड़ों सूर्योंके समान प्रकाशमान था।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.9070)
- **Original**: सर्वरूप हैं। आप तेजःस्वरूप परमेश्वरको मैं वह दिव्य ज्योतिसे जाज्वल्यमान हो रहा था।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.9071)
- **Original**: नमस्कार करता हूँ। तीनों गुणोंका विभाग करनेके ऊपर चारों ओर सात ताड़की दूरीमें उसका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.9072)
- **Original**: लिये आप तीन रूप धारण करते हैं; परंतु हैं प्रकाश फैला हुआ था। सबके तेजको छीन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.9073)
- **Original**: तीनों गुणोंसे अतीत। समस्त देवता आपकी लेनेवाला बह प्रकाशपुझ सम्पूर्ण आश्रमको व्याप्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.9074)
- **Original**: कलासे प्रकट हुए हैं। आप श्रुतियोंकी पहुँचसे करके देदीप्यमान था। वह सर्वत्र व्यापक, सबका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.9075)
- **Original**: भी परे हैं; फिर आपको देवता कैसे जान सकते बीज तथा सबके नेत्रोंको अवरुद्ध कर देनेवाला हैं? आप सबके आधार, सर्वस्वरूप, सबके था। उस तेज:स्वरूपको देखकर वे देवता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.9076)
- **Original**: आदिकारण, स्वयं कारणरहित, सबका संहार ध्यानमग्र हो गये तथा भक्तिभावसे मस्तक एवं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.9077)
- **Original**: करनेवाले त्तथा अन्तरहित हैं। आप तेज:स्वरूप कंधे झुकाकर बड़ी श्रद्धाके साथ उसको प्रणाम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.9078)
- **Original**: परमात्माको नमस्कार है। जो सगुण रूप है, वही करने लगे। उस समय परमानन्दकी प्राप्तिसे उनके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.9079)
- **Original**: लक्ष्य होता है और विद्वान्‌ पुरुष उसीका वर्णन नेत्रोंमें आँसू भर आये थे और सारे अड्ज पुलकित
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.9080)
- **Original**: कर सकते हैं। परंतु आपका रूप अलक्ष्य है; हो गये थे। वे ऐसे जान पड़ते थे मानों उनके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.9081)
- **Original**: अत: मैं उसका वर्णन कैसे कर सकता हूँ ? आप अभीष्ट मनोरथ पूर्ण हो गये हों। उन तेजःस्वरूप
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.9082)
- **Original**: तेजोरूप परमात्माकों मेरा प्रणाम है। आप परमेश्वको नमस्कार करके वे तीनों देवेश्वर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.9083)
- **Original**: निशराकार होकर भी दिव्य आकार धारण करते उठकर खड़े हो गये और उन्‍्हींका ध्यान करते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.9084)
- **Original**: हैं। इन्द्रियातीत होकर भी इन्द्रिययुक्त होते हैं। हुए उस तेजके सामने गये। ध्यान करते-करते आप सबके साक्षी हैं; परंतु आपका साक्षी कोई जगत्स्रष्टा ब्रह्मके दोनों हाथ जुड़ गये। नारद!
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.9085)
- **Original**: नहीं है। आप तेजोमय परमेश्वरकों मेरा नमस्कार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.9086)
- **Original**: ड्श्ड + संक्षिप्त ब्रह्मवैवर्तपुराण * 58885 88%8%# 44 8# 84488 98888 48/48/6484 88 4444 6/ 488 86864 44444 4 86684 8% 44 448 44 4 88888 8 है। आपके पैर नहीं हैं तो भी आप चलनेकी
- **Translation**: 

---

