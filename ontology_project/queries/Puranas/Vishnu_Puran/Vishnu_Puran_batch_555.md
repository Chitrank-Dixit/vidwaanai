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

### Verse 1 (Vishnu Puran 0.11081)
- **Original**: 35 सत्यं तद्यदि गोविन्द नोपचारकृतं मम । तदस्तु पारिजातो5यं मम गेहविभूषणम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11082)
- **Original**: 36 बिभ्रती पारिजातस्यथ केशपक्षेण मझ़्रीम्‌। सपत्रीनामह॑ मध्ये शोभेयमिति कामये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11083)
- **Original**: 37 श्रीपराज्चार उवाच इत्युक्तस्स प्रहस्पैनां पारिजात॑ गरुत्पति । आरोपयामास॒ हरिस्तमूचुर्वनरक्षिण:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11084)
- **Original**: 38 भो हाची देवराजस्य महिषी तत्परिग्रहम्‌। पारिजातं॑ न गोविन्द हर्तुमहसि पादपम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11085)
- **Original**: 39 उत्पन्नो देवराजाय दत्तस्सोषपि ददौ पुनः । महिष्ये सुमहाभाग देव्यै शच्यै कुतृहल्ात्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11086)
- **Original**: 40 हचीविभूषणार्थाय देवैरमृतमन्थने । उत्पादितो5यं न क्षेमी गृहीत्वैन गमिष्यसि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11087)
- **Original**: 41 श्रीविष्णुपुराण [ आू 30 कृपासे तुझे कभी वृद्धावस्था या बिरूपता व्याप्त न होगी । हे अनिन्दिताड्ि ! तेरा नवयौवन सदा स्थिर रहेगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11088)
- **Original**: श्रीपराशरजी खोले--तदनन्तर अदितिको आज्ञासे देवराजने अत्यन्त आदर-सत्कारके साथ श्रीकृष्णचन्द्रका पूजन किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11089)
- **Original**: किन्तु कल्पवृक्षके पुष्पोंसे अलड्जुता इन्द्राणीने सत्यभामाकों मानुषी समझकर थे पुष्प न दिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11090)
- **Original**: हे साधुश्रेष्ठ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11091)
- **Original**: तदनन्तर सत्यभामाके सहित श्रीकृष्णचन्द्रने भी देवताओंके नन्‍दन आदि मनोहर डद्यानोंको देखा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11092)
- **Original**: वहाँपर केशिनिषृदन जगन्नाथ श्रीकृष्णने सुगन्धपूर्ण मझजरी-पुञ्धधारी, नित्याह्भादकारी और ताम्रनर्ण बाल फ्तोंसे सुशोभित, अमृत-मन्थनके समय प्रकट हुआ तथा सुनहरी झालवाल्म पारिजात-वृक्ष देखा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11093)
- **Original**: हे द्विजोत्तम ! उस अत्युत्तम वृक्षराजकों देखकर परम अ्रीतिवश सत्यभामा अति प्रसन्न हुई और श्रीगोकिन्दसे बोली--“हे कृष्ण ! इस वृक्षको द्वारकापुरी क्यों नहीं ले चलते ?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11094)
- **Original**: यदि आपका यह जचन फि 'तुम ही मेरी अत्यन्त प्रिया हो' सत्य है तो मेरे गृहोद्यानमें लगानेके लिये इस वृक्षकों छे चल्तिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11095)
- **Original**: हे कृष्ण ! आपने कई बार मुझसे यह प्रिय वाक्य कहा है कि 'हे सत्ये ! मुझे तू जितनी प्यारी है उतनी न जाम्बवती है और न रुक्मिणी हो'
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11096)
- **Original**: हे गोलिन्द ! यदि आपका यह कथन सत्य है--क्ेबल मुझे जहत्थना ही नहीं है---तो यह पारिजात- वृक्ष मेंरे गृहका भूषण हो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11097)
- **Original**: मेरी ऐसी इच्छा है कि मैं अपने केश-कलापोंमें पास्जात-पुष्प गूँधकर अपनी अन्य सपन्नियॉमें सुशोभित होऊँ'
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11098)
- **Original**: श्रीपराशरजी जोले--सत्यभामाके इस प्रकार कहनेपर श्रीहरिने हँसते हुए उस पारिजात -वृक्षकों गरुडपर रख्य लिया; तब नन्‍्दनवनके रक्षकोने कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11099)
- **Original**: “हे गोविन्द ! देवराज इन्द्रकी पत्नी जो महारानी शची है यह पारिजात-वृक्ष उनकी सम्पत्ति है, आप इसका हरण न कीजिये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11100)
- **Original**: क्षीर-समुद्रसे उत्पन्न होनेके अनन्तर यह देवराजको दिया गया था; फिर हे महाभाग ! देवराजने कुतूहलवज्ञ इसे अपनी महिषी शाचीदेवीको दे दिया है
- **Translation**: 

---

