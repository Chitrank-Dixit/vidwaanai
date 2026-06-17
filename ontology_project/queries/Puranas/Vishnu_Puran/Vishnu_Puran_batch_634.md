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

### Verse 1 (Vishnu Puran 0.12661)
- **Original**: 7 अीपराजर उवाच अ्हृष्टस्साध्विति प्राह तत: केशिध्वजो नृप: । स्वाण्डिक्यजनकं प्रीत्या श्रूयतां वचर्न मम
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12662)
- **Original**: 8 अहं ह्वाविद्यया मृत्युं तर्तुकामः: करोमि वै । राज्य यागांश्व विविधान्भोगै: पुण्यक्षर्य तथा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12663)
- **Original**: 9 तदिदं ते मनो दिष्टधा विवेकैश्वर्यतां गतम्‌। तच्छुयतामविद्यायास्स्वरूप॑. कुलनन्दन
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12664)
- **Original**: 10 अनात्मन्यात्मबुद्धियया चास्वे स्वमिति या मति: । संसारतरुसम्भूतिबीजमेतदद्विधा स्थितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12665)
- **Original**: 11 पश्चभूतात्मके देहे देही मोहतमोबृतः । अहं मपैतदित्युच्: कुरुते कुमतिर्मतिम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12666)
- **Original**: 12 आकाशवायवग्रिजलपृथिवीभ्य: पृथक्‌ स्थिते । आत्मन्यात्ममर्य भाव॑ क: करोति कलेवरे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12667)
- **Original**: 13 कलेवरोपभोग्यं हि गृहक्षेत्रादिक च कः । अदेहे ह्ात्मनि प्राज्ञो ममेदमिति मन्यते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12668)
- **Original**: 14 इत्थ॑ च॒पुत्रपौत्रेषु तहेहोत्यादितेषु कः । करोति पण्डितस्स्वाम्यमनात्मनि कलेवरे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12669)
- **Original**: 15 सर्व देहोपभोगाय कुरुते कर्म मानवः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12670)
- **Original**: देहश्वान्यो यदा पुंसस्तदा बन्धाय तत्परम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12671)
- **Original**: 16 मृण्मयं हि यथा गेहं लिप्यते वै मृदम्भसा । पार्थिवोउर्य तथा देहो मृदम्ब्नालेपनस्थितः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12672)
- **Original**: 17 भी ] मुझे कोई दोष न होगा। [ किन्तु राज्याधिकार होनेपर यथावत्‌ प्रजापालन न करनेसे दोषका भागी होना पड़ता है ] क्योंकि यद्यपि यह (स्वकर्म) अविद्या हो है तथापि नियमविरुद्ध व्याग करनेपर यह बन्धनका कारण होती है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12673)
- **Original**: यह राज्यकी चाह मुझे तो जन्मात्तरके [ कर्मोंद्वारा प्राप्त ] सुखभोगके ल्तिये होती है; और वही मन्त्री आदि अन्य जनॉको राग एवं ल्म्रेभ आदि दोषोंसे उत्पन्न होती है केवल धर्मानुरोधसे नहीं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12674)
- **Original**: “उत्तम क्षत्रियोंका [ राज्यादिकी ] याचना करना धर्म नहीं है' यह महात्माओंका मत है। इसील्क्यि मैने अधिद्या (पालनादि कर्म) के अन्तर्गत तुम्हारा राज्य नहीं माँगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12675)
- **Original**: जो त्ओेग अहंकाररूपी मदिराका पान करके उच्मत्त हो रहे हैं तथा जिनका चित्त मपताग्रस्त हो रहा है वे मूढ़जन ही राज्यकी अभिलाषा करते हैं; मेरे-जैसे ल्लेग राज्यकी इच्छा नहीं करते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12676)
- **Original**: श्रीपराहरजी खोलले--तब राजा केशिध्वजने प्रसन्न होकर खाण्डिक्य जनकको साधुवाद दिया और प्रीतिपूर्वक कहा, मेरा खचन सुनो--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12677)
- **Original**: मैं अविद्याद्वाय मृत्युको पार करनेकी इच्छासे ही राज्य तथा विविध यज्ञोंका अनुष्ठान करता हूँ और नाना भोगोंद्वारा अपने पुण्योंका क्षय कर रहा हूँ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12678)
- **Original**: हे कुलनन्दन ! बड़े सौभाग्यकी बात है कि तुम्हारा मन विवेकसम्पन्न हुआ है अतः तुम अविद्याका स्वरूप सुनो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12679)
- **Original**: संसार-वुक्षकी बीजभूता यह अविद्या दो प्रकारकी है--अनात्मामें आत्मबुद्धि और जो अपना नहीं है उसे अपना मानना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12680)
- **Original**: यह कुमति जीव मोहरूपी अन्धकारसे आबुत होकर इस पश्चभूतात्मक देहमें 'मैं' और 'मेरापन' का भाव करता है
- **Translation**: 

---

