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

### Verse 1 (Bhagwat_Geeta 17.1417)
- **Original**: यातयामं॑ गतरसं पूति पर्युषितं च यत्‌। उच्छिष्टमपि चामेध्यं भोजनं तामसप्रियम्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 17.1418)
- **Original**: जो भोजन अधपका, रसरहित, दुर्गन्धयुक्त, बासी और उच्छिष्ट है तथा जो अपवित्र भी है, वह भोजन तामस पुरुषको प्रिय होता है
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 17.1419)
- **Original**: अफलाकाद्िशक्षभिर्यज्ञो विधिदृष्टो य इज्यते। यष्ट॒व्यमेवेति मनः समाधाय स सात्त्विक:
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 17.1420)
- **Original**: जो शास्त्रविधिसे नियत, यज्ञ करना ही कर्तव्य है--इस प्रकार मनको समाधान करके, फल न चाहने- वाले पुरुषोंद्वारा किया जाता है, वह सात्तिक है
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 17.1421)
- **Original**: अभिसन्धाय तु फलं दम्भार्थमपि चैव यत्‌। इज्यते भरतश्रेष्ठ तं यज्ञं विद्ध्धि राजसम्‌
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 17.1422)
- **Original**: परन्तु हे अर्जुन! केवल दम्भाचरणके लिये अथवा फलको भी दृष्टिमें रखकर जो यज्ञ किया
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 17.1423)
- **Original**: 212 * श्रीमद्धगवद्रीता * जाता है, उस यज्ञको तू राजस जान
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 17.1424)
- **Original**: विधिहीनमसूष्ठान्न॑ मन्त्रहीनमदक्षिणम्‌। श्रद्धाविरहितं यज्ञ॑ तामसं परिचक्षते
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 17.1425)
- **Original**: शास्त्रविधिसे हीन, अनदानसे रहित, बिना मन्तरेंके, बिना दक्षिणाके और बिना श्रद्धाके किये जानेवाले यज्ञको तामस यज्ञ कहते हैं
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 17.1426)
- **Original**: देवद्विजगुरुप्राज्ञपूजनं शौचमार्जवम्‌ । ब्रह्मचर्यमहिंसा च शारीर तप उच्यते
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 17.1427)
- **Original**: देवता, ब्राह्मण, गुरुः और ज्ञानीजनोंका पूजन, पवित्रता, सरलता, ब्रह्मचर्य और अहिंसा--यह शरीर-सम्बन्धी तप कहा जाता है
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 17.1428)
- **Original**: अनुद्वेगकरं वाक्यं सत्यं प्रियहितं च यत्‌। स्वाध्यायाभ्यसनं चैव वाड्म्मयं तप उच्यते
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 17.1429)
- **Original**: जो उद्धेग न करनेवाला, प्रिय और हितकारक एवं यथार्थ भाषण है! तथा जो वेद-शास्त्रोंके पठनका एवं परमेश्वरके नाम-जपका अभ्यास है-- वही वाणी-सम्बन्धी तप कहा जाता है
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 17.1430)
- **Original**: 1. यहाँ 'गुरु' शब्दसे माता, पिता, आचार्य और वृद्ध एवं अपनेसे जो किसी प्रकार भी बड़े हों, उन सबको समझना चाहिये। 2. मन और इन्द्रियोंद्रार जैसा अनुभव किया हो, ठीक वैसा ही कहनेका नाम “यथार्थ भाषण' है।
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 17.1431)
- **Original**: * अध्याय 17* 213 मनःप्रसादः सौम्यत्वं॑ मौनमात्मविनिग्रहः । भावसंशुद्द्विरित्येतत्तपो_ मानसमुच्यते
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 17.1432)
- **Original**: मनकी प्रसन्नता, शान्तभाव, भगवच्चिन्तन करनेका स्वभाव, मनका निग्रह और अन्त:करणके भावोंकी भलीभाँति पवित्रता--इस प्रकार यह मनसम्बन्धी तप कहा जाता है
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 17.1433)
- **Original**: श्रद्धयपा परया तप्तं तपस्तत्त्रिविधं नरैः। अफलाकाड्स्षिभिरयुक्ति: सात्त्विके परिचक्षते
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 17.1434)
- **Original**: फलको न चाहनेवाले योगी पुरुषोंद्वारा परम श्रद्धासे किये हुए उस पूर्वोक्त तीन प्रकारके तपको सात्त्विक कहते हैं
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 17.1435)
- **Original**: सत्कारमानपूजार्थ तपो दम्भेन चैव यत्‌। क्रियते तदिह प्रोक्ते राजसं चलमश्चुवम्‌
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 17.1436)
- **Original**: जो तप सत्कार, मान और पूजाके लिये तथा अन्य किसी स्वार्थके लिये भी स्वभावसे या पाखण्डसे किया जाता है, वह अनिश्चित* एवं क्षणिक फलवाला तप यहाँ राजस कहा गया है
- **Translation**: 

---

