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

### Verse 1 (Vishnu Puran 0.11101)
- **Original**: समुद्र-मन्थनके समय शचोकों विभूषित करनेके लिये ही देबताओंने इसे उत्पन्न किया था; इसे लेकर आप कुझलपूर्वक नहीं जा सकेंगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11102)
- **Original**: आ* 30 ] देवराजो मुखप्रेक्षी यस्यास्तस्या: परिग्रहम्‌। मौ्यात्रार्थयसे क्षेमी गृहीत्वैनं हि को ब्रजेत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11103)
- **Original**: 42 अवश्यमस्य देकेन्रो निष्कृति कृष्ण यास्यति । वज्रोद्यतकर॑झक्रमनुयास्यन्ति चामरा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11104)
- **Original**: 43 तदलं.. सकलेवेंबैर्विप्ेण. तवाच्युत । विपाककटु यत्कर्म तन्न शंसन्ति पण्डिता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11105)
- **Original**: 44 श्रीपराझ्र उवाच इत्युक्ते तैरवाचैतान्‌ सत्यभामातिकोपिनी । का झाची पारिजातस्य को वा हशक्रस्मुराधिप:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11106)
- **Original**: 45 सामान्यस्सर्वलोकस्थ॒ यद्येषो5मृतमन्थने । समुत्यन्नस्तरु: कस्मादेकों गृह्माति वासबः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11107)
- **Original**: 46 यथा सुरा यथैवेन्दुर्यथा श्रीर्वनरक्षिण: । सामान्यस्सर्वलोकस्य पारिजातस्तथा द्वुम:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11108)
- **Original**: 47 झाची । तत्कथ्यतामल क्षान्त्या सत्या हारयति द्रुमम्‌ ।। 48 कथ्यतां च द्वुतं गत्वा पोल्कोम्या बचने मम । सत्यभामा बदत्येतदिति गर्वोद्धताक्षरम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11109)
- **Original**: 49 यदि त्वे दयिता भर्तुर्यीदि वश्यः पतिस्तव । मर््धर्तुर्रतो वृक्ष तत्कारय निवारणम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11110)
- **Original**: 50 जानामि ते पति शक्रं जानामि त्रिदशेश्वरम्‌ । पारिजातं॑ तथाप्येन॑ मानुषी हारयामि ते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11111)
- **Original**: 51 ऑीपराशर उताच इत्युक्ता रक्षिणों गत्वा शच्या: प्रोचुर्यथोदितम्‌। श्रुत्वा चोत्साहयामास शी शक्रं सुराधिपम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11112)
- **Original**: 52 ततस्समस्तदेवानां सैन्येः परिवृतों हरिम्‌। प्रययौ पारिजातार्थमिन्द्रो योद्धु द्विजोत्तम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11113)
- **Original**: 53 ततः.. परिघनिशख्रिंशगदाशूलबरायुधा: । बभूवुस्त्रिदशास्सज्ञा: शक्रे वज़करे स्थिते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11114)
- **Original**: 54 त्तों निरीक्ष्य गोविन्दो नागराजोपरि स्थितम्‌ । शक्रं देवपरीवारं युद्धाय समुपस्थितम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11115)
- **Original**: 55 ब्रकार शबद्भुनि्धोर्ष दिशइशब्देन पूरयन्‌। मुप्रोच्च झरसझ्जातान्सहस्नायुतशह्शितान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11116)
- **Original**: 56 पञ्चम अंजाम 391 देवराज भी जिसका मुँह देखते रहते हैं उस शाचीकी सम्पत्ति इस पारिजातकी इच्छा आप मृढताहीसे करते हैं; इसे लेकर भल्त कौन सकुशल जा सकता है ?
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11117)
- **Original**: हे कृष्ण ! देवराज इन्द्र इस वृक्षका बदला चुकानेके लिये अवच्ष्य ही व लेकर उचद्यत होंगे और फिर देवगण भी अवश्य ही उनका अनुगमन करेँगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11118)
- **Original**: अतः हे अच्युत ! समस्त देवताओंके साथ रार बढ़ानेसे आपका कोई लाभ नहीं; क्योंकि जिस कर्मका परिणाप कटु होता है, पष्डितजन उसे अच्छा नहीं कहते ''
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11119)
- **Original**: श्रीपराश्रजी बोले--उद्यान-रक्षकोके इस प्रकार कहनेपर सत्यभामाने अत्यन्त क़ुद्ध होकर कहा--'“'“दाबी अथवा देबराज इन्द्र ही इस पारिजातके कौन होते हैं 2
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11120)
- **Original**: यदि यह अमृत-मन्थनके समय उत्पन्न हुआ है, तो सबकी समान सम्पत्ति है। अकेला इन्द्र ही इसे ले सकता है ?
- **Translation**: 

---

