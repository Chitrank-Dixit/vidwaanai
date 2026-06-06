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

### Verse 1 (Vaivtpuran 23.1602)
- **Original**: है। इसके बाद दिद्वान्‌ पुरुष दोनों भुजाओंके वे तुम्हारे ऊपर लीलाविहार करते हैं)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1603)
- **Original**: मृत्तिकामयी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1604)
- **Original**: मूलभागमें, ललाटमें, कण्ठदेशमें और वक्ष:- देवि! मैंने जो भी दुष्कर्म किया है, मेरा वह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1605)
- **Original**: स्‍्थलमें तिलक लगाये। यदि ललाटमें तिलक न सारा पाप तुम हर लो।' हो तो स्त्रान, दान, तप, होम, देवयज्ञ तथा उद्धतासि बराहेण कृष्णेन शतबाहुना।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1606)
- **Original**: पितृयज्ञ-सब कुछ निष्फल हो जाता है। ब्राह्मण आरुद्या मम गात्राणि सर्व पाप॑ं प्रमोचय
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1607)
- **Original**: स््रानके पश्चात्‌ तिलक करके संध्या और तर्पण पुण्य॑ देहि महाभागे स्त्रानानुज्ञां कुरुष्ष माम्‌।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1608)
- **Original**: करे। फिर भक्तिभावसे देवताओंको नमस्कार “सैकड़ों भुजाओंसे सुशोभित वराहरूपधारी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1609)
- **Original**: करके प्रसन्नतापूर्वक अपने घरको जाय। वहाँ श्रीकृष्णने एकार्णबके जलसे तुम्हें ऊपर उठाया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1610)
- **Original**: यत्रपूर्वक पैर धोकर धुले हुए दो वस्त्र धारण [631_] सं0 ब्र0 बै0 प्राण 4
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1611)
- **Original**: 76 + संक्षिप्त ब्रह्मवैयर्तपुराण +
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1612)
- **Original**: ###&###### # #### 88866 # # # ## ### #4# ## # % ### # # # 4 # 8 58% 6 % 4 4 # ## ## # % # # # कक # 4 हक ऊ 55 ऊ कक के करे। तत्पश्चात्‌ बुद्धिमान्‌ पुरुष मन्दिरमें जाय। यह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1613)
- **Original**: अनुसार उसका वर्णन करता हूँ। कोई-कोई साक्षात्‌ श्रीहरिका ही कथन है। जो स्नान करके नैष्णव पुरुष श्रीहरिको प्रतिदिन भक्तिभावसे सोलह पैर धोये बिना ही मन्दिरमें घुस जाता है, उसका सुन्दर तथा पवित्र उपचार अर्पित करते हैं। कोई स्नान, जप और होम आदि सब नष्ट हो जाता बारह द्रव्योंका उपचार और कोई पाँच वस्तुओंका है। जो गृहस्थ पुरुष पानीसे भींगे या तेलसे तर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1614)
- **Original**: उपचार चढ़ाते हैं। जिनकी जैसी शक्ति हो, उसके वस्त्र पहनकर घरमें प्रवेश करता है, उसके ऊपर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1615)
- **Original**: अनुसार पूजन करें। पूजाकी जड़ है--भगवान्‌के लक्ष्मी रुष्ट हो जाती हैं और उसे अत्यन्त भयंकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1616)
- **Original**: प्रति भक्ति। आसन, वस्त्र, पाद्य, अर्ध्य, आचमनीय, शाप देकर उसके घरसे निकल जाती हैं। यदि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1617)
- **Original**: पुष्प, चन्दन, धूप, दीप, उत्तम नैवेद्य, गन्ध, ब्राह्मण पिण्डलियोंसे ऊपरतक पैरोंकों धोता है
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1618)
- **Original**: माल्य, ललित एवं विलक्षण शय्या, जल, अन्न तो वह जबतक गड्जाजीका दर्शन न कर ले,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1619)
- **Original**: और ताम्बूल--ये सामान्यतः अर्पित करने योग्य तबतक चाण्डाल बना रहता है। सोलह उपचार हैं। गन्ध, अन्न, शय्या और अह्मन्‌! पवित्र साधक आसनपर बैठकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1620)
- **Original**: ताम्बूल--इनको छोड़कर शेष द्रव्य बारह उपचार आचमन करे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1621)
- **Original**: फिर संयमपूर्वक रहकर भक्तिभावसे
- **Translation**: 

---

