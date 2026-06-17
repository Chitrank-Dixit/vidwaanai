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

### Verse 1 (Vishnu Puran 0.11961)
- **Original**: श्रीव्यासजी बोले--मुनिका यह वाक्य सुनकर उन अप्सराओने उन्हें फिर प्रसन्न किया, तब मुनिवरने उनसे कहा-- उसके पश्चात्‌ तुम फिर स्वर्गलोकमें चली
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11962)
- **Original**: आ0 38 ] पशक्कम अंझ डरे9 एवं तस्य मुनेश्शापादष्टावक्रस्य चक्रिणम्‌ । भर्तरें प्राप्त ता याता दस्युहस्तं सुराद़्ना:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11963)
- **Original**: 84 सर्व॑ तदुपसंहतम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11964)
- **Original**: 85 भ्रवतां चोपसंहार आसज्नस्तेन पाण्डव । बल तेजस्तथा वीर्य माहात्य॑ चोपसंहतम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11965)
- **Original**: 86 जातस्य नियतो मृत्यु: पतन च तथोज्ते: । विप्रयोगावसानस्तु संयोग: सदझ्ये क्षय:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11966)
- **Original**: 87 विज्ञाय न युधाइशोकं न हर्षमुपयान्ति ये । तेषामेवेतरे चेष्टां शिक्षन्तस्सन्ति तादृशाः चेष्टां शिक्षन्तस्सन्ति :
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11967)
- **Original**: 88 तस्मात्त्वया नस्श्रेष्ट ज्ञात्वैतदभ्रातृभिस्सह । परित्यज्याखिलं तन्ज्न॑ं गन्तव्यं तपसे वनम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11968)
- **Original**: 89 तद्च्छ धर्मराजाय निवेहतद्बो मम। परश्चो भ्रातृभिस्सार्द यथा यासि तथा कुरु
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11969)
- **Original**: 90 इत्युक्तो भ्येत्य पार्थाभ्यां यमाध्यां च सहार्जुन: । दृष्ट चैवानुभूत॑ चर सर्वमार्यातवांस्तथा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11970)
- **Original**: 99 व्यासवा्कर्य च ते सर्वे श्रुत्वार्जुनमुखेरितम्‌। राज्ये परीक्षित॑ कृत्वा ययु: पाण्डुसुता बनम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11971)
- **Original**: 92 इत्येतत्तव मैत्रेय बिस्तरेण मयोदितम्‌। जातस्य यहादोर्वशे वासुदेवस्य चेष्टितम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11972)
- **Original**: 93 स्पा विकिसका लिजाक न नाल तस्य श्रृूणुयात्सदा । कस गच्छति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11973)
- **Original**: 94 जाओगी"
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11974)
- **Original**: इस प्रकार मुनिवर अष्टाबक्रके झापसे ही बे देवाड्नाएँ श्रीकष्णचन्द्रकों पति पाकर भी फिर दस्युओंके हाथमें पड़ी हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11975)
- **Original**: उपसंहार किया है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11976)
- **Original**: तथा तुपस्त्रेगोंका अच्त भी अब निकट ही है; इसलिये उन सर्वेश्वरने तुम्हारे बल, तेज, वीर्य और माहात्प्यका सक्लोच कर दिया है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11977)
- **Original**: 'जो उत्पन्न हा है उसकी मृत्यु निश्चित है, उच्चतका पतन अवश्यम्भावी , सं॑योगक्रा अन्त बियोग ही है तथा सक्षय (एकत्र करने) के अनन्तर क्षय (व्यय) होना सर्वधा निश्चित ही है'---ऐसा जानकर जो बुद्धिमान्‌ पुरुष लाभ या हानिमें हर्ष अथवा शोक नहीं करते उन्हींकी चेष्ठाका अवलछम्बन कर अन्य मनुष्य भी अपना वैसा आचरण बनाते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11978)
- **Original**: इसल्लये हे नसथश्रेष्ठ ) तुम ऐसा जानकर अपने भाइयॉसहित सम्पूर्ण राज्यकों छोड़कर तपस्पाके लिये वनको जाओ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11979)
- **Original**: अब तुम जाओ तथा धर्मराज युश्रिष्ठिरसे मेरी ये सारी बातें कहो और जिस तरह परसों भाइयोंसहित बनको चले जा सको वैसा यत्र करो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11980)
- **Original**: मुनिबर व्यासजीके ऐसा कहनेपर अर्जुनने [ इन्द्रप्रस्थमें ] आकर पृथा-पुत्र (युधिष्ठर और भीमसेन) तथा यम्जों ( हक और सहदेव) से उन्होंने जो कुछ जैसा-जैसा देखा और सुना था सब ज्यॉ-का-त्यों सुना दिया
- **Translation**: 

---

