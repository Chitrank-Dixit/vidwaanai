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

### Verse 1 (Sama Ved 0.1461)
- **Original**: इति नवम: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1462)
- **Original**: रूकेके
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1463)
- **Original**: 5.14 सामवेद-संहिता
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1464)
- **Original**: दशम: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1465)
- **Original**: 566. इन्द्रमच्छ सुता इमे वृषणं यन्तु हरयः । श्रुष्टे जातास इन्दव: स्वर्विद:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1466)
- **Original**: तुरन्त तैयार हुआ, आत्पिक ज्ञान की वृद्धि करने वाला, यह हरिताभ सोमरस पराक्रमी इद्धदेव को शीघ्र प्राप्त हो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1467)
- **Original**: 567. प्र धन्वा सोम जागृविरिन्द्रायेन्दो परि स्व । ब्युमन्तं शुष्ममा भर स्वर्विदम्‌। ।2
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1468)
- **Original**: है सोम ! स्फूर्ति से सम्पन होकर आप, इन्द्रदेव के निमित्त कलश में प्रवाहित हों । हमें तेजोवर्द्धक एवं ज्ञानवर्द्धक शक्ति से परिपूरित कर दें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1469)
- **Original**: 568, सखाय आ नि घीदत पुनानाय प्र गायत। शिशु न यज्ञै: परि भूषत श्रिये
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1470)
- **Original**: हे भित्रो ! (त्र्प्रत्वजो) आप आकर बैठें । सोम को शोधित करते समय स्तुति करो । जिस प्रकार शिशु को आभूषणों से सजाते हैं, उसी प्रकार यज्ञ से- यज्ञीय साधनों से इस सोमरस को विभूषित करो
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1471)
- **Original**: 569. त॑ व: सखायो मदाय पुनानमभि गायत । शिशुं न हव्यै: स्वदयन्त गूर्तिभि:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1472)
- **Original**: 4 आनन्ददायी, सोमरस का अभिषवण करते समय हे मित्रो ! इसकी प्रार्थना करो । शिशु को जिस प्रकार से अलंकृत करते हैं, उसी प्रकार यज्ञों और स्तुतियों से आप इसे ग्राह्य बनाओ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1473)
- **Original**: 4 । । 570. प्राणा शिशुर्महीनां हिन्वन्नतस्य दीधितिम्‌ । विश्वा परि प्रिया भुवदघ द्विता
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1474)
- **Original**: यह सोम, यज्ञ का प्राण तथा महान्‌ जल का पुत्र है । यह यज्ञ को प्रकाशित करने वाले, अपने रस को प्रेरित करता है । यह सभी हविष्यान्नों (आहुतियों) में व्याप्त होता हुआ, चुलोक तथा पृथ्वीलोक में व्याप्त रहता है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1475)
- **Original**: 571. पवस्व देववीतय इन्दो धाराभिरोजसा । आ कलशं मथुमान्सोम न: सद;
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1476)
- **Original**: हे सोम ! देवगणों के सेवनार्थ, वेगपूर्वक धाराओंसहित आप कलश में प्रवाहित हों! आनन्ददायक हे सोम ! आप हमारे इस कलश में आकर स्थित हों
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1477)
- **Original**: 572.सोम: पुनान ऊर्मिणाव्यं वारं वि धावति ।अग्रे वाच: पवमान: कनिक्रदत्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1478)
- **Original**: पवित्र होने याला, स्तुति के पश्चात्‌ ध्वनि करता हुआ, शोधित होने वाला यह सोम, प्रवाह के साथ बालों की छलनी से छनता चला जाता है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1479)
- **Original**: 573. प्र पुनानाय वेथसे सोमाय बच उच्यते । भूर्ति न भरा मतिभिर्जुजोषते
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1480)
- **Original**: शुद्ध होने वाले कर्म प्रेरक सोम के निमित्त (हे स्तोतागण) स्तुति करो । प्रार्थना से प्रसन होकर जिस प्रकार दास को धन प्रदान किया जाता हैं, उसी प्रकार ( स्तुति से सोम को प्रसन्‍न करने के लिए) विशेष स्तुति करो
- **Translation**: 

---

