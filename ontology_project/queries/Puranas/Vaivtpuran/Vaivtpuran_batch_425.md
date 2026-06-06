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

### Verse 1 (Vaivtpuran 23.1462)
- **Original**: इसके बाद आपकी प्रसन्नताके लिये मैं दार-संग्रह किसका पुत्र या बन्धु है? कर्ममयी तरज्जोंके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1463)
- **Original**: करूँगा; क्योंकि मनकी इच्छा पूर्ण हो जानेपर ही उठनेसे इन सबका संयोग हो जाता है और उन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1464)
- **Original**: मनुष्यको कोई काम करनेमें सुख मिलता है। तरड्रोंक शान्त होनेपर ये एक-दूसरेसे बिछुड़ नारदकी यह बात सुनकर ज्ञानवेत्ताओंमें श्रेष्ठ जाते हैं। जो सत्कर्म करवाता है, वही मित्र है,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1465)
- **Original**: कमलजन्मा ब्रह्माजी बड़े प्रसन्न हुए और अपने वही पिता और गुरु है। जो दुर्बुद्धि उत्पन्न करता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1466)
- **Original**: पुत्रसे फिर इस प्रकार बोले।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1467)
- **Original**: ब्रह्माजीनेी कहा--वत्स! भगवान्‌ शंकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1468)
- **Original**: कथा-बार्ता सुनो और शीघ्र ही मेरे घर लौट तुम्हारे पूर्वजन्मके गुरु हैं और हमारे भी पुरातन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1469)
- **Original**: आओ। शौनक! ऐसा कहकर तीनों लोकोंका गुरु हैं। अत: तुम उन्हीं ज्ञानियोंके गुरु कल्याणदाता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1470)
- **Original**: धारण-पोषण करनेवाले ब्रह्माजी चुप हो गये और शान्तस्वरूप शिवके पास जाओ। वहीं उन पुरातन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1471)
- **Original**: नारदमुनि पिताको भक्तिभावसे प्रणाम करके गुरुसे भगवन्मन्त्रका ज्ञान प्राप्त ककके नारायणकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1472)
- **Original**: शिवलोककों चले गये। (अध्याय 24) #3“>-- लिए थेधन्‍-2>-+>+ नारदजीको भगवान्‌ शिवका दर्शन, शिवद्वारा नारदजीका सत्कार तथा उनकी मनोवाउछापूर्तिके लिये आश्वासन सौति कहते हैं--शौनक ! तदनन्तर विप्रवर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1473)
- **Original**: सुन्दर फूलोंसे भरे हुए मन्दार आदि देववृक्षोंसे नारद क्षणभरमें बड़ी प्रसन्नताके साथ शिवके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1474)
- **Original**: वह सदा आवेष्टित है। सुन्दर कामधेनुएँ उस मनोहर धाममें जा पहुँचे। भगवान्‌ शिवका वह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1475)
- **Original**: धामकी उसी तरह शोभा बढ़ाती हैं, जैसे सैकड़ों अभीष्ट लोक धरुवसे एक लाख योजन ऊपर था।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1476)
- **Original**: बलाकाएँ आकाशकी। उस लोकको देखकर नारद त्रिशूलधारी शिवने दिव्य रज्नोंद्वारा उसका निर्माण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1477)
- **Original**: मुनि मन-ही-मन बड़े विस्मित हुए और सोचने किया है। आधारशून्य आकाशमें योगबलसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1478)
- **Original**: लगे--'जहाँ ज्ञानियों तथा योगियोंके गुरु निवास शम्भुद्वारा धारण किया गया वह विचित्र लोक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1479)
- **Original**: करते हैं, वहाँ ऐसी विचित्रताका होना क्‍या भाँति- भाँतिके दिव्य भवनोंसे सुशोभित है तथा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1480)
- **Original**: आश्चर्य है? यह सृष्टिलोक त्रिलोकौसे अत्यन्त दिन-रात तेजसे उद्धासित होता रहता है। पवित्र
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1481)
- **Original**: विलक्षण है और भय, मृत्यु, रोग, पीड़ा तथा अन्तःकरणदबाले श्रेष्ठ साधक तथा मुनीन्द्रशिरोमणि
- **Translation**: 

---

