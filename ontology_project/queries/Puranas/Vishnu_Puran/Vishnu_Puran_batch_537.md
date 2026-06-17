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

### Verse 1 (Vishnu Puran 0.10721)
- **Original**: 8 ततो गोपांश्व गोपीश्व यथा पूर्वममित्रजित्‌ । तथैवाध्यवदत्पेम्णा. बहुमानपुरस्सरम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10722)
- **Original**: 9 स्‌ वैश्षित्सम्परिष्तक्त: कांश्िध परिषस्वजे। हास्य॑ चक्रे सम॑ कैश्िद्ञेपैगोपीजनैस्तथा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10723)
- **Original**: 10 प्रियाण्यनेकान्यवदन्‌ गोपास्तत्र हलायुधम्‌ । गोष्यश्न प्रेमकरुपिताः प्रोचुस्सेर्यमथापरा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10724)
- **Original**: 19 गोष्यः पप्रच्छरपरा नागरीजनवल्लभ:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10725)
- **Original**: कच्चिदास्ते सुखं कृष्णश्चलप्रेमलवात्मक:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10726)
- **Original**: 12 अस्मशेष्टामपहसन्न॒ कशित्पुरयोषिताम्‌ । सौभाग्यमानमधिकं करोति क्षणसौहदः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10727)
- **Original**: 13 श्रीपराज्रजी बोले--परंम बुद्धिमानू राजा अनादिनिधन भगवान्‌ हरि बोले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10728)
- **Original**: श्रीभगवानने कहा--हे नरेश्वर! तुय अपने अभिमत दिन्य स्त्रेकॉक्मो जाओ; मेरी कृपासे तुम्हें अन्यारत परम ऐश्वर्य प्राप्त होगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10729)
- **Original**: कहाँ अत्यन्त दिव्य भोगॉंकों भोगकर तुम्त अन्तमें एक महान्‌ कुलमें जन्म स्थेगे, उस समय तुम्हें अपने पूर्वजन्पका स्मरण रहेगा और छिर मेरी कृपासे तुम मोक्षपद प्राप्त करोगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10730)
- **Original**: ओऔपराशरजी बोले--भगवानक इस प्रकार कहनेपर राजा मुचुकुन्दने जगदीक्षर श्रोअच्चतकों प्रणाम किया और गुफासे निकलकर देखा कि लोग यहत छोटे- ब्छेटे हो गये हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10731)
- **Original**: उस समय कॉलियुगकों वर्तमान समझकर राजा तपस्या करनेके लिये श्रीनर नारायणके स्थान गन्धमादनपर्वतपर चले गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10732)
- **Original**: इस प्रकार कश्णचन्द्रने ठपायपूर्वक शत्रुकों माट्कर फिर मधुरामें आ उसकी हाथी, घोड़े और रथादिसे सुझोभित सेनाको अपने बज्ीभूत किया और उसे द्वारकामें व्वकर यजा उम्रसेनकों अर्पण कर दिया। तबसे यदुवंश शत्रुओंके दमनसे निःशैक हो गया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10733)
- **Original**: है मैत्रेय ! इस सम्पूर्ण विग्रहके झान्त हो जानेपर अलटेबजी अपने बान्धवोंके दर्शनकी उत्कण्ठासे नन्‍्दजीके गोकुलको गये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10734)
- **Original**: नहाँ फ्ट्ुंचकर झत्रुजित्‌ बलभद्रजीने गोप और गोपियोंका पहल्ीकी भाँति अति आदर और प्रेमके साथ अभिवादन किया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10735)
- **Original**: किसीने उनका आलिक्वन किया और किसीको उन्होंने गले लूगाया तथा किन्हीं गोप और गोपियोंके साथ उन्होंने हास- परिहास किया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10736)
- **Original**: गोपोंने बल्समजीसे अनेकों प्रिय बचन कहे तथा गोपियोंमेंसे कोई प्रणयकुपित होकर बोलीं और किनन्‍्हींने उपाल्म्भयुक्त बातें की
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10737)
- **Original**: किन्‍्हीं अन्य गोपियोंने पूआ-- चञ्नल एव अल्प प्रेम करना ही जिनका स्वभाव है, वे नगर-नारियोंके प्राणाधार कृष्ण तो आनन्दमें हैं न ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10738)
- **Original**: वे क्षणिक ख्रेहबाले नन्दनन्दन हमारी चेष्टाओऑका उपहास करते हुए क्‍या नगरकी महिलाओंके सौभाग्यका मान नहीं बढ़ाया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10739)
- **Original**: 378 श्रीविष्णुपुराण [ आ* 27 कचित्स्मरति नः कृष्णो गीतानुगमने कलम्‌। अप्यसौ मातर॑ द्र्ल॑ं सकृदप्यागमिष्यति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10740)
- **Original**: 14 अथवा कि तदालापै: क्रियन्तामपरा: कथा: । यस्पास्माभिविना तेन विनास्माक॑ भविष्यति
- **Translation**: 

---

