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

### Verse 1 (Vishnu Puran 0.11941)
- **Original**: तदिच्छाम: पति प्राप्तुं विप्रेद्ध पुरुषोत्तमम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11942)
- **Original**: 78 श्रीव्यास उवाच एवं भविष्यतीत्युक्त्वा ह्यात्ततार जलान्पुनि: । तमुत्तीणँ च॒ददृशुर्विरूपं वक़मष्टघा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11943)
- **Original**: 79 ते दुष्ठा गृहमानानां यासां हासः स्फुटो$भवत्‌ । ताइशशाप मुनि: कोपमवाप्य कुरुनन्दन
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11944)
- **Original**: 80 यस्माद्विकृतरूपं मां मत्वा हासावमानना
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11945)
- **Original**: भवतीभि: कृता तस्मादेत श्ञापं ददामि व:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11946)
- **Original**: 81 मत्मसादेन भर्तारें लब्ध्वा तु पुरुषोत्तमम्‌। मच्छापोपहतास्सर्वा दस्युहस्त॑ गमिष्यथ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11947)
- **Original**: 82 औव्यास उवाच इत्युदीरितमाकर्ण्य मुनिस्ताभिः प्रसादित: । पुनस्सुरेचद्रल्लोके वै प्राह भूयों गमिष्यथ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11948)
- **Original**: 83 श्रीविष्णुपुराण [ आ* 38 हे पार्थ ! यह सब सर्वात्मा भगवानकी लील्थ्रका ही कौतुक है कि तुझ अकेलेने कौरबॉको नष्ट कर दिया और फिर स्वयं अहीरोंसे पराजित हो गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11949)
- **Original**: हे अर्जुन ! तू जो उन दस्युआँद्वारा हरण की गयी स््रियोंके लिये शोक करता है सो मैं तुझे उसका यथावत्‌ रहस्य बतत्मता हूँ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11950)
- **Original**: एक बार पूर्वकालमें विप्रवर अष्टाबक्रजी सनातन ब्रह्मकी स्तुति करते हुए अनेकों वर्षतक जलमें रहे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11951)
- **Original**: उसी समय दैत्यॉपर विजय श्राप्त करनेसे देवताओनि सुमेरु पर्वतपर एक महान्‌ उत्सव किया । उसमें सब्मिलित होनेके लिये जाती हुई रम्मा और तिलोत्तमा आदि सैकड़ॉ-हजारों देवाड़नाओंने मार्गमें उन मुतिवस्को देखकर उनकी अत्यन्त स्तुति और प्रशंसा की
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11952)
- **Original**: वे देवाड़नाएँ, उन जटाधारी मुनिवरकों कण्ठपर्यन्त जल्में डूबे देखकर विनयपूर्वक स्तुति करती हुई प्रणाम करने लगीं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11953)
- **Original**: हे कौरवश्रेष्ठ ! जिस प्रकार वे द्विजश्रे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11954)
- **Original**: अष्टावक्रजी प्रसन्न हों उसी प्रकार वे अप्सराएँ उनकी स्तुति करने लगीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11955)
- **Original**: अष्टावक्रजी बोले--है महाभागाओ ! मैं तुमसे प्रसन्न हूँ, तुम्हारी जो इच्छ्छा हो मुझसे वही वर माँग लो; मैं अति दुर्लभ होनेपर भी तुम्हारी इच्छा पूर्ण करूँगा । 76
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11956)
- **Original**: तब रम्मा और तिल्लोत्तमा आदि जबैदिकी (वेदप्रसिद्ध) अप्सराओंने उनसे कहा--“हे ट्विज ! आपके प्रसन्न हो जानेपर हमें क्‍या नहीं मिल गया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11957)
- **Original**: तथा अन्य अप्सराओने कहा-- “यदि भगवान्‌ हमपर प्रसन्न हैं तो हे विप्रेन्द्र ! हम साक्षात्‌ पुरुषोत्तमभगवान्‌को पतिरूपसे प्राप्त करना चाहती हैं"
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11958)
- **Original**: श्रीव्यासजी बोल्ले--तब “ऐसा ही होगा'--यह कहकर मुनिवर अष्टावक्र जलसे बाहर आये । उनके बाहर आते समय अप्सराओने आठ स्थानोंमें टेढ़े उनके कुरूप देहको देखा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11959)
- **Original**: उसे देखकर जिन अप्सराओंकी हैंसी छिपानेपर भी प्रकट हो गयी, हे कुरुनन्दन ! उन्हें मुनिवरने क्रुद होकर यह शाप दिया--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11960)
- **Original**: “मुझे कुरूप देखकर तुपने हँसते हुए मेश अपमान किया है, इसलिये मैं तुम्हें यह शाप देता हूँ कि मेरी कृपासे अ्री5#षोत्तमको पतिरूपसे पाकर भी तुम मेरे ज्ञापके बशीभूत होकर लुटेरोंके हाथोंमें पड़ोगी''
- **Translation**: 

---

