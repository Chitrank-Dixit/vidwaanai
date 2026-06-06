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

### Verse 1 (Vaivtpuran 0.401)
- **Original**: सर्वदाके लिये पतिके साथ पूर्णतः: अभिन्नता प्राप्त “शिव” शब्द कल्याणका बाचक है और “कल्याण'
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.402)
- **Original**: कर लोगी। सुरेश्वरि! प्रतिवर्ष प्रशस्त समयमें शब्द मुक्तिका। शिवके उच्चारणसे मोक्ष या
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.403)
- **Original**: समस्त लोकोंमें तुम्हारी शरत्कालिक पूजा होगी। कल्याणकी प्राप्ति होती है, इसीलिये महादेवजीको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.404)
- **Original**: गाँवों और नगरोंमें तुम ग्रामदेवताके रूपमें पूजित शिव कहा गया है*। धन और भाई-बन्धुओंका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.405)
- **Original**: होओगी तथा विभिन्न स्थानोंमें तुम्हारे पृथक्‌- वियोग होनेपर जो शोक-सागरमें डूब गया हो,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.406)
- **Original**: पृथक्‌ मनोहर नाम होंगे। मेरी आज्ञासे शिवरचित बह मनुष्य शिव शब्दका उच्चारण करके सर्वथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.407)
- **Original**: नाना प्रकारके तन्‍्त्रोंद्वारा तुम्हारी पूजा की जायगी। कल्याणका भागी होता है। 'शि' पापनाशक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.408)
- **Original**: मैं तुम्हारे लिये स्तोत्र और कवचका विधान अर्थमें है और 'ब' मोक्षदायक अर्थमें। महादेवजी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.409)
- **Original**: करूँगा। तुम्हारे सेवक ही महान्‌ और सिद्ध होंगे मनुष्योंके पापहन्ता और मोक्षदाता हैं। इसलिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.410)
- **Original**: तथा धर्म, अर्थ, काम एवं मोक्षरूप फलके भागी उन्हें शिव कहा गया है। जिसकी वाणीमें शिव-यह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.411)
- **Original**: होंगे। मातः ! पुण्यक्षेत्र भारतवर्षमें जो तुम्हारी *महादेव महादेव महादेवेति वादिन:। पश्चाद्यामि महात्रस्तो नामश्रवणलोभत:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.412)
- **Original**: शिवेति मन्त्रमुच्चार्यप्राणांस्त्थजति यो. नर:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.413)
- **Original**: कोटिजन्मार्जितातू मुक्ति प्रयाति सः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.414)
- **Original**: शिव कल्याणवचन॑ कल्याणं मुक्तिवाचिकम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.415)
- **Original**: यतस्तत्‌ प्रभवेत्तेन स शिव: परिकोर्तित:। (ब्रह्मखंण्ड 6
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.416)
- **Original**: 48-51)
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.417)
- **Original**: सेबा-पूजा करेंगे, उनके यश, कीर्ति, धर्म और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.418)
- **Original**: शिवको भी स्तोत्र और कवच दिया। ब्रह्मन्‌! ऐश्वर्यकी वृद्धि होगी। फिर धर्मको भी वही मन्त्र और वही सिद्धि एवं प्रकृतिसे ऐसा कहकर भगवानने उसे कामबीज
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.419)
- **Original**: ज्ञान देकर कामदेव, अग्नि और वायुको भी मन्त्र (क्लीं)-सहित एकादशाक्षर-मन्त्रका उपदेश दिया,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.420)
- **Original**: आदिका उपदेश दिया। इसी प्रकार कुबेर आदिको जो परम उत्तम मन्त्रराज कहा गया है। फिर
- **Translation**: 

---

