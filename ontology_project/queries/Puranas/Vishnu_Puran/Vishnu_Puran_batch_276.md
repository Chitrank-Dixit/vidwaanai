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

### Verse 1 (Vishnu Puran 0.5501)
- **Original**: इस प्रकार वाणीका संयम करके अनिषिद्ध अप्न भोजन करे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5502)
- **Original**: अन्नकी निन्‍्दा न करे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5503)
- **Original**: प्रथम पाँच प्रास अत्यन्त मौन होकर गअहण करे, उनसे फकप्राणोंकी तुप्ति होती है।। 89
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5504)
- **Original**: भोजनके अनन्तर भली प्रकार आचमन करे और फिर पूर्व या उत्तरकी ओर मुख करके हा्थोंक्रो उनके सूलदेशतक धोकर सिधिपूर्वक आचमन करे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5505)
- **Original**: तदनच्तर, स्वस्थ और श्ञान्त-चित्तसे आसनपर बैठकर अपने इश्देवॉका चिन्तन करे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5506)
- **Original**: [ और इस प्रकार कहे--- ) “[ प्राणएरूप ] फ्वनसे फ्रज्वलित हुआ जठराप्रि आकाइशके द्वारा अवकादञयुक्त अन्नका परिपाक करे और [ फिर अन्नरससे ] मेरे शरीस्के पार्थिव घातुओंको पुष्ट करे जिससे मुझे सुख प्राप्त हो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5507)
- **Original**: यह अप्र मेरे शरीरस्थ पृचिबी, जल, अप्रि और वायुका बल बढ़ानेवाल्म हो और इन चारों तत्वोके रूपमें परिणत हुआ यहे अन्न ही मुझे निरन्तर सुख देनेवाला हो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5508)
- **Original**: यह अन्न मेरे प्राण, अपान, समान, उदान और न्‍्यानकी पुष्टि करे तथा मुझे भी निर्वाध सुखकी प्राप्ति हो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5509)
- **Original**: मेरे ख़ाये हुए सम्पूर्ण अन्नका अगस्ति नामक अग्नि और बडलानल परिपाक करें, मुझे उसके परिणामसे होनेवाल्ा सुख्र प्रदान करें और उससे मेंरे दारीस्को आशेग्यता प्राप्त हो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5510)
- **Original**: 'देह और इन्द्रियादिके अधिष्ठाता एकमात्र भगवान्‌ किव्णु ही प्रधान हैं'-- इस्र सत्पके नलसे मेरा खाया हुआ समस्त अन्न परिपक होकर मुझे आरोग्यता प्रदान करे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5511)
- **Original**: “भोजन करनेवाला, भोज्य अन्न और उसका परिपाक-- ये सब विष्णु ही है'--इस सत्य भावनाके बलसे मेरा स्वाया हुआ यह अन्न पच जाय”
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5512)
- **Original**: ऐसा कहकर अपने उदरपर हाथ फेरे और सावधान होकर अधिक श्रम उत्पन्न न करनेवाले कार्योमिं लग जाय
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5513)
- **Original**: 198 >> अचअकिष्णुपुराण ख 9ख9 आछआछ पफसछक्‍छछ_ओः रै1 98 सच्छास््रादिविनोदेन सन्मार्गादबिरोधिना । दिने नयेत्ततस्सन्ध्यामुपतिष्ठेत्समाहित:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5514)
- **Original**: 99 दिनान्तसशख्यां सूर्येण पूर्वापृक्षै्युतां बुध: । उपतिष्ठेद्यथान्याय्यं सम्यगाचम्य पार्थिव
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5515)
- **Original**: 900 सर्वकालमुपस्थान सन्ध्ययो: पार्थिवेष्यते । अन्यत्र सूतकाशौचविशभ्रमातुरभीतितः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5516)
- **Original**: 101 सूर्येणाभ्युदितों यश्च त्यक्त: सूर्येण वा स्वपन्‌। अन्यत्रातुरभावात्तु प्रायश्चित्ती भवेन्नर:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5517)
- **Original**: 1902 तस्मादनुदिते सूर्य समुत्याय महीपते। उपत्िष्ठेत्नरस्सन्ध्यामस्वपंश्च॒दिनान्तजाम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5518)
- **Original**: 103 उपतिष्ठन्ति वै सन्थ्यां ये नपूर्वां न पश्चिमाम्‌ । ख्जन्ति ते दुरात्यानस्तामिस्र नरक॑ नृप
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5519)
- **Original**: 104 पुनः पाकमुपादाय सायमप्यवनीपते । वैश्वदेवनिपित्त तै पल्यमन्त्रे बलिं हरेत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5520)
- **Original**: 105 तत्रापि श्रपचादिभ्यस्तथैवान्नविसर्जनम्‌
- **Translation**: 

---

