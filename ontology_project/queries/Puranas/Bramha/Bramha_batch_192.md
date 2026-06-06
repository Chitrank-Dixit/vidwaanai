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

### Verse 1 (Bramha 0.3821)
- **Original**: शूरसेनने भूषण, वस्त्र तथा मधुर वाणीसे बूढ़े विवाहके लिये इस प्रकार कहा--'मेरा पुत्र
- **Translation**: 

---

### Verse 2 (Bramha 0.3822)
- **Original**: मन्त्रीका सत्कार करके उन्हें बहुत बड़ी सेनाके युवराज नागेश्वर सब गुणोंकी खान है। वह
- **Translation**: 

---

### Verse 3 (Bramha 0.3823)
- **Original**: साथ भेजा। वे पूर्वदेशमें जाकर महाराज विजयसे बुद्धिमान, शूर, दुर्जय तथा शत्रुओंको संताप
- **Translation**: 

---

### Verse 4 (Bramha 0.3824)
- **Original**: मिले और नाना प्रकारके वचनों तथा नीतिजनित देनेवाला है। उसका विवाह करना है। मैं बूढ़ा
- **Translation**: 

---

### Verse 5 (Bramha 0.3825)
- **Original**: उपायोंसे राजाको संतुष्ट किया। मन्त्रीने राजकुमारी हुआ। अब पुत्रको राज्यका भार सौंपकर निश्चिन्त
- **Translation**: 

---

### Verse 6 (Bramha 0.3826)
- **Original**: भोगवती और युवराज नागका विवाह तय करा होना चाहता हूँ। आपलोग मेरे हित-साधनमें
- **Translation**: 

---

### Verse 7 (Bramha 0.3827)
- **Original**: दिया। राजा विजयने कन्या देना स्वीकार कर तत्पर हो उसके विवाहके लिय प्रयत्न करें।'
- **Translation**: 

---

### Verse 8 (Bramha 0.3828)
- **Original**: लिया। बूढ़े मन्त्री लौट आये और शूरसेनसे राजाकी बात सुनकर अमात्यगण हाथ जोड़कर
- **Translation**: 

---

### Verse 9 (Bramha 0.3829)
- **Original**: उन्होंने ब्रिवाह निश्चित होनेका सब वृत्तान्त सुना बोले--'महाराज ! आपके पुत्र सब गुणोंमें श्रेष्ठ
- **Translation**: 

---

### Verse 10 (Bramha 0.3830)
- **Original**: दिया। तदनन्तर बहुत समय व्यतीत हो जानेपर हैं और आप भी सर्वत्र विख्यात हैं। फिर आपके
- **Translation**: 

---

### Verse 11 (Bramha 0.3831)
- **Original**: वृद्ध मनत्री अन्य सब सचिवोंको साथ लेकर पुत्रका विवाह करनेके लिये क्या मन्त्रणा करनी है
- **Translation**: 

---

### Verse 12 (Bramha 0.3832)
- **Original**: सहसा राजा विजयके वहाँ पहुँचे और इस प्रकार और किस बातकी चिन्ता।' अमात्योंके यों कहनेपर
- **Translation**: 

---

### Verse 13 (Bramha 0.3833)
- **Original**: बोले--' राजनू्‌! महाराज शूरसेनके राजकुमार नाग नृपश्रेष्ठ शूरसेन कुछ गम्भीर हो गये। वे उन
- **Translation**: 

---

### Verse 14 (Bramha 0.3834)
- **Original**: बड़े हो बुद्धिमान्‌ और गुणोंके समुद्र हैं। वे स्वयं अमात्योंकों यह बताना नहों चाहते थे कि मेरा
- **Translation**: 

---

### Verse 15 (Bramha 0.3835)
- **Original**: यहाँ आना नहीं चाहते। क्षत्रियोंक बिबाह अनेक बेटा सर्प है; तथा ये भी इस बातसे अपरिचित ही
- **Translation**: 

---

### Verse 16 (Bramha 0.3836)
- **Original**: प्रकारसे होते हैं। अत: यह विवाह शस्त्रों द्वारा हो रहे। राजाने फिर कहा-'कौन कन्या गुणोंमें
- **Translation**: 

---

### Verse 17 (Bramha 0.3837)
- **Original**: जाय तो अच्छा है।' सबसे अधिक है तथा कौन राजा ऊँचे कुलमें
- **Translation**: 

---

### Verse 18 (Bramha 0.3838)
- **Original**: वृद्ध मन्त्रीकी बात सुनकर राजा घिजयने उसे उत्पन्न, श्रोमान्‌ और उत्तम गुणोंके आश्रय हैं ?”
- **Translation**: 

---

### Verse 19 (Bramha 0.3839)
- **Original**: सत्य ही माना और भोगवतीका विवाह शस्त्रके राजाका यह कथन सुनकर अमात्योमेंसे एक परम
- **Translation**: 

---

### Verse 20 (Bramha 0.3840)
- **Original**: साथ ही शास्त्र-विधिके अनुसार सम्पन्न हुआ। युद्धिमान्‌ पुरुष, जो महाराजके संकेतको समझनेवाले
- **Translation**: 

---

