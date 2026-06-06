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

### Verse 1 (Vaivtpuran 119.19070)
- **Original**: ध्यान॑ च किण्णोर्वेदोक्त शाश्वतं सर्वदुर्लभम्‌ । मूलेल सर्व॑ देय॑ च नैवेद्यादिकमुत्तमम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 119.19071)
- **Original**: अतीवगुप्त कबचं पितुर्वक्त्रान्यया श्रुतम्‌ । पित्रे दत्त पुरा विप्र गड्डायां शूलिना श्वरुवम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 119.19072)
- **Original**: शूलिने ब्रह्मणे दत्त गोलोके रासमण्डले । धर्माय गोपीकान्तेन. कृपया परमाद्भुतम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 119.19073)
- **Original**: ब्रह्मोवाच राधाकान्त महाभाग कवच यत्‌ प्रकाशितम्‌ । ब्रह्माण्डणावन॑ नाम कृपया कथय प्रभो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 119.19074)
- **Original**: मां महेश च धर्म च भक्त च भक्तवत्सल । त्वत्प्रसादेन पुत्रेभ्यों दास्याभि भक्तिसंयुत:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 119.19075)
- **Original**: श्रीकृष्ण उवाच श्रृणु वक्ष्यामि बरहोश धर्मेंदे कवर्च परम्‌। अहं दास्यामि युक्‍्मभ्य॑ गोपनीय सुदुर्लभम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 119.19076)
- **Original**: यस्मै कसम न दातव्यं॑ प्राणतुल्य ममैव हि। यत्तेजो मम देहेडस्ति तत्तेज: कवचेडपि चा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 119.19077)
- **Original**: कुरु सृष्टिपिदं थ्रृत्वा धाता त्रिजगतां भव। संहर्ता भव हे शबम्भो मम तुल्यो भवे भव
- **Translation**: 

---

### Verse 9 (Vaivtpuran 119.19078)
- **Original**: है धर्म त्वमिर्द धृत्वा भव साक्षी च कर्मणाम्‌ । तपसां फलदाता च॑ यूयं भवत मद्वरात्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 119.19079)
- **Original**: ख्रह्माण्डपावनस्थास्थ कवचस्य हरि: स्वयम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 119.19080)
- **Original**: ऋषिश्छन्द्ष॒ गायत्री देवो5ह॑ जगदीश्वर:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 119.19081)
- **Original**: धर्मार्थकाममोक्षेपु. विनियोग: प्रकीर्तित: । त्रिलक्षबारपठनात्‌ू सिद्धिदं कवच विधे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 119.19082)
- **Original**: यो भवेत्‌ सिद्धकबचो मम तुल्यो भवेत्तु सः। तेजसा सिन्द्रायोगेन ज्ञानेन विक्रमेण च
- **Translation**: 

---

### Verse 14 (Vaivtpuran 119.19083)
- **Original**: प्रणवों मे शिरः: पातु नमो रासेश्रराय च। भाल॑ पायात्रेत्रयुग्म॑ नमो राधेश्वराय च
- **Translation**: 

---

### Verse 15 (Vaivtpuran 119.19084)
- **Original**: कृष्ण: पायाच्छोत्रयुग्मं हे हरे प्राणमेत्र च्
- **Translation**: 

---

### Verse 16 (Vaivtpuran 119.19085)
- **Original**: जिढ़्िकां वह्िजाबा तु कृष्णाबेति चर सर्वतः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 119.19086)
- **Original**: भ्रीकृष्णाय स्वाहेति च कण्ठं पातु षडक्षरः । ह्रीं कृष्णाय नमो वक्त्रं क्लीं पूर्वश्च भुजद्धयम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 119.19087)
- **Original**: नमो गोपाड्नेशाय स्कन्थावष्टाक्षरोउवतु । दन्तपंक्तिमोष्युग्म॑ नमो. गोपीश्वराय च
- **Translation**: 

---

### Verse 19 (Vaivtpuran 119.19088)
- **Original**: 30 नमो भगवते रासमण्डलेशाय स्वाहा । स्वयं वशक्षःस्थलं पातु मन्त्रोड्य॑ घोडशाक्षर:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 119.19089)
- **Original**: ऐं कृष्णाय स्वाहेति च कर्णयुग्मं सदावतु । 340 विष्णवे स्वाहेति च कपोल॑ सर्वतो5यतु
- **Translation**: 

---

