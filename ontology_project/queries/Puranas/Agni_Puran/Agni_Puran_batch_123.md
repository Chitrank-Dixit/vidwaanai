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

### Verse 1 (Agni Puran 0.2441)
- **Original**: तदनन्तर शेष अन्नकों ब्राह्मणोंकी आज्ञा लेकर उद्देश्यसे आहुति दे'। हवनसे शेष बचे हुए
- **Translation**: 

---

### Verse 2 (Agni Puran 0.2442)
- **Original**: एकमें मिला दे और पिण्ड बनानेके लिये पात्रसे अन्नमेंसे क्रमशः देवताओं और पितरोंके पात्रोंमें
- **Translation**: 

---

### Verse 3 (Agni Puran 0.2443)
- **Original**: बाहर निकाले और पितरोंके उच्छिष्ट अन्नके पास परोसे और पात्रको हाथसे ढक दे। उस समय
- **Translation**: 

---

### Verse 4 (Agni Puran 0.2444)
- **Original**: ही अवनेजन करके कुशोंपर संकल्पपूर्वक तीन 1, यदि दूसरेकी भूमिमें श्राद्ध करते हों ठो थोड़ा अन्न और जल कुशापर अपसब्यभावसे रखकर कहें--' इदमन्नमेतद्धूस्वामिपितृध्यों नमः
- **Translation**: 

---

### Verse 5 (Agni Puran 0.2445)
- **Original**: " 2. देवताओं, फितरों, महायोगियों, स्वधा और स्वाहाकों मेरा स्बंदा नमस्कार है, नमस्कार है। 3. यह मन्त्र तौन ऋचाओंमें है। पूरा मन्त्र इस प्रकार हैं -- 3» मधु याता ऋतायते मधु क्षरात्ति सित्थव: । माध्वीर्ण: सन्त्वोषधी:
- **Translation**: 

---

### Verse 6 (Agni Puran 0.2446)
- **Original**: 3> मधु नक्तमुतोव्सो मधुमत्‌ पार्थिव रज:। मधु झौरस्तु नः पिता
- **Translation**: 

---

### Verse 7 (Agni Puran 0.2447)
- **Original**: 3# मधुमान्नों यनस्पतिर्सधु्मां5स्तु सूर्य:। माध्वीर्गावों भवन्तु न!
- **Translation**: 

---

### Verse 8 (Agni Puran 0.2448)
- **Original**: (यजु0 13। 27--29) <> मधु मधु मधु आ 4, उक्त ऋकाके अतिरिक्त भी “उदौरतामबर0' (यजु0 19। 46) इत्यादि पफितृमत्रॉका ' 3» कृणुष्व पाज:0” (बजु0 13।9) इत्यादि सक्षोघ्न-मन्जोंका, 'सहल्लशोषां:0' (यजु0 31) इत्यादि पुरुषसूक्तका तथा '3> आशु: शिक्ञान:0' (यत्रु0 17
- **Translation**: 

---

### Verse 9 (Agni Puran 0.2449)
- **Original**: 33) इत्यादि मन्जॉंका एवं शतरुद्रियकां पाठ भी किया जाता है। +नमस्तुध्यं बिरूपाक्ष नमस्ते3नेकचक्षुपे। नमः पिनाकहस्ताय वज़हस्ताय पै तम:
- **Translation**: 

---

### Verse 10 (Agni Puran 0.2450)
- **Original**: " इस श्लोकको भी पढुना चाहिये।
- **Translation**: 

---

### Verse 11 (Agni Puran 0.2451)
- **Original**: पिण्डदान करे।' दूसरोंका मत है कि ब्राह्मण जब
- **Translation**: 

---

### Verse 12 (Agni Puran 0.2452)
- **Original**: शुभागमन होता रहे। हमारे पास माँगनेवाले भोजनके पश्चात्‌ हाथ-मुँह धोकर आचमन कर
- **Translation**: 

---

### Verse 13 (Agni Puran 0.2453)
- **Original**: आवें, किंतु हम किसीसे न माँगें।' फिर स्वधा- लें, तब पिण्डदान देना चाहिये। आचमनके पश्चात्‌
- **Translation**: 

---

### Verse 14 (Agni Puran 0.2454)
- **Original**: ब्राचनके लिये पिण्डोॉंपर पवित्रकसहित कुश जल, फूल और अक्षत दे
- **Translation**: 

---

### Verse 15 (Agni Puran 0.2455)
- **Original**: 22--253
- **Translation**: 

---

### Verse 16 (Agni Puran 0.2456)
- **Original**: बिछाबवे और ब्राह्मणोंसे पूछे--'मैं स्वधा-वाचन फिर अक्षय्योदक देकर मनुष्य आशीर्वादकी
- **Translation**: 

---

### Verse 17 (Agni Puran 0.2457)
- **Original**: कराऊँगा।' ब्राह्मण आज्ञा दें-'स्वधा-वाचन प्रार्थना करे'। ' 50 अघोरा: पितर: सन्‍्तु।' (मेरे
- **Translation**: 

---

### Verse 18 (Agni Puran 0.2458)
- **Original**: कराओ।' तब श्राद्धकर्ता पुरुष इस प्रकार कहे-- पितर सौम्य हों।) ऐसा कहकर जल गिरावे, फिर
- **Translation**: 

---

### Verse 19 (Agni Puran 0.2459)
- **Original**: . “ब्राह्मणो! आपलोग मेरे पिता, पितामह और प्रार्था करे--'हमारा गोत्र सदा ही बढ़ता रहे,
- **Translation**: 

---

### Verse 20 (Agni Puran 0.2460)
- **Original**: प्रपतामहके लिये स्वधा-वाचन करें।' ब्राह्मण हमारे दाता भी निरन्तर अभ्युदयशील हों, बेदोंकी
- **Translation**: 

---

