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

### Verse 1 (Vishnu Puran 0.161)
- **Original**: तन्मात्राओंमें विज्ञेप भाव नहों है इसलिये उनकी अनिज्ञेष संज्ञा है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.162)
- **Original**: जे अखिशेष नन्मात्राएँ झान्त, घोर अथवा मृदढ नहीं हैं [अर्थात्‌ उनका सुख-दुःख या मोहरूपसे अनुभन नहीं हो सकता] इस प्रकार तामस अइंकारसे यह भूत- तन्पात्ररूप सर्ग हुआ है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.163)
- **Original**: दस इन्द्रियाँ तैजस अर्थात्‌ राजस अईंकारसे और उनके अधिष्ठाता देन्रता जैकास्क्रि आर्थात्‌ सात्तिक
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.164)
- **Original**: आ02 ] त्वक्‌ चक्षु्नांसिका जिद्ना श्रोत्रमत्रच पश्षमम्‌ । झब्दादीनामबाप्त्य्थ बुद्धियुक्तानि वे द्विज
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.165)
- **Original**: 48 पायूषस्थो करौ पादो वाक्‌ च मैत्रेय पश्चमी । बिसर्गशिल्पगत्युक्ति कर्म तेषां च कध्यते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.166)
- **Original**: 49 आकाशतवायुतेजांसि सलिलं पृथिवी तथा । ग़ब्दादिभिर्गुणब्रहास्संयुक्तान्युत्तरोत्तः..
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.167)
- **Original**: 50 शान्ता घोराश्न मूढाश्र विशेषास्तेन ते स्मृता:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.168)
- **Original**: 51 नानावीर्चा: पृथग्भूत्तास्ततस्ते संहततिं विना । नाशक़ुब्आअजा: ल्ड्डमसमागम्य कृत्सश:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.169)
- **Original**: 52 समेत्यान्योन्यरससययोर्ग परस्परसमाश्रया: । एकसड्भातलक्ष्याश्न॒ सम्प्राप्यैक्यमशेषत:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.170)
- **Original**: 53 पुरुषाथिष्ठितत्वाच्च॒ ग्रधानानुग्रहेण चन। मह॒दाद्या विशेषान्ता हाण्डमुत्पाद्यन्ति ते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.171)
- **Original**: 54 तत्क्रोेण बिवृद्धं सआलखुदखुदबत्समम्‌। भूतेभ्यो5ण्ड मद्ठाबुद्धे, महृत्तदुदकेशयम्‌। प्राकृते ब्रह्मरूपस्य विष्णो: स्थानमनुत्तमम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.172)
- **Original**: 55 तत्राव्यक्तस्वरूपोउसो व्यक्तरूपो जगत्पति: । विष्णुर्त्रह्मस्वरूपेण स्वयमेब व्यवस्थित:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.173)
- **Original**: 56 मेरूरूल्त्रमभूत्तस्य जरायुश्च॒ महीधरा: । गर्भोदक समुद्राक्ष तस्वासन्सुमहात्मनः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.174)
- **Original**: 57 सादिद्ीपसमुद्राभआ्॒ सज्योतिल्ॉकिसंग्रह: । तस्मिन्नण्डे+भवद्धिप्र. सदेवासुरपानुष:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.175)
- **Original**: 58 वारिवहन्यनिलाकादौस्ततो भूतादिना अहिः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.176)
- **Original**: बृते दह्गुणैरण्ड भूतादिर्महता तथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.177)
- **Original**: 59 अव्यक्तेनावृतो ब्रह्मोस्तै: सबैं: सहितो महान्‌ । एपिराबरणैरण्ड सप्तप्रि: प्राकृतैर्वृतम्‌। नारिकेलफलस्पान्तर्बीज॑ बाह्यदलैरिव
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.178)
- **Original**: 60 जुषन्‌ रजो गुणं तत्न स्वयं विश्वेश्वरो हरि: । ब्रह्मा भूत्वास्य जगतो विसृष्टो सम्प्रवर्त्तते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.179)
- **Original**: 669 अ्थम अंग 0] अज्तेकारसे उत्पन्न हुए कहे जाते हैं। इस प्रकार इन्द्रियोंके अधिष्ठाता दस देवता और ग्यारह॒वाँ मन बेकारिक (सात्तिक) हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.180)
- **Original**: हे द्विज
- **Translation**: 

---

