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

### Verse 1 (Vaivtpuran 17.1114)
- **Original**: खो बैठते हैं, उन परमात्माका स्तबन दूसरा कौन सर्वाधार, परात्पर एवं महान्‌ विराटू-रूप धारण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.1115)
- **Original**: विद्वान्‌ कर सकता है? मैं शोकातुर अबला उन करते हैं, जिनके रोम-रोममें अनन्त ब्रह्माण्डोंका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.1116)
- **Original**: निरीह परात्पर परमेश्वरकी स्तुति क्या कर समुदाय शोभा पाता है। कभी अपनी ही
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.1117)
- **Original**: सकती हूँ।* *मालावत्युवाच वन्दे त॑ परमात्मानं॑ सर्वकारणकारणम्‌ । विना येन शवाः: सर्वे प्राणिनों जगतीतले
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.1118)
- **Original**: निर्लिपं साक्षिकंपं च सर्वेषां सर्वकर्मसु । विध्यमानं न दुष्ट च सर्व: सर्वत्र सर्वदा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.1119)
- **Original**: येन सृष्ठ च प्रकृति: सर्वाधारा परात्परा । ब्रह्मविष्णुशियादीनां प्रसूर्या त्रिगुणात्मिका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.1120)
- **Original**: जगल्सष्टा स्वयं ब्रह्मा नियतो यस्य सेवया । पाता विष्णुश्ष जगतां संहर्त्ता शंकर: स्वयम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.1121)
- **Original**: ध्यायन्ते य॑ सुरा: सर्वे मुनयो मनवस्तथा। सिद्धाश्ष योगिन: सनन्‍्तः सन्ततं प्रकृते: परम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.1122)
- **Original**: साकार॑ च निराकारं परं स्वेच्छामयं विभुम्‌। वरं॑ करेण्यं वरदं॑ वराहँ वरकारणम्‌। तपःफल॑ तपोबीज॑ तपसां च फ़लप्रदम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.1123)
- **Original**: स्वय॑ तपःस्वरूप॑च सर्वरूप॑च सर्वत:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.1124)
- **Original**: सर्वाधार॑ सर्वबीज॑ कर्म तत्कर्मणां फलम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.1125)
- **Original**: तेषा च फलदातारें. तद्ठटीजक्षयकारणम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.1126)
- **Original**: स्वयं तेज:स्वकृपं च भक्तानुग्रहविग्रहम्‌ । सेवाध्यानं न घटते भक्तानां विग्रह॑ विना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.1127)
- **Original**: तत्तेजो मण्डलाकारं. सूर्यकोटिसमप्रभपू । अतीव कमनीय॑ च रूप॑ तत्र मनोहरमसू
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.1128)
- **Original**: नवीननीरदश्यामं शरत्पक्कूजलोचनम्‌ । शरत्पार्बणचन्द्रास्यमीषद्धास्यसमन्वितम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.1129)
- **Original**: कोटिकन्दर्पलावण्य॑ लीलाधाम मनोहरम्‌ । चन्दनोक्षितसर्वाड्र रत्रभूषणभूषितम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.1130)
- **Original**: ट्विभुजं मुरलीहस्त॑ पीतकौरोयवाससम्‌ । किशोरवयस॑ शान्त॑ राधाकान्तमनन्तकमू
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.1131)
- **Original**: गोपाडुनापरिवत कुजचिन्निर्जने बने । कुत्रचिद्रासमध्यस्थ॑ राधया. परिसेवितम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.1132)
- **Original**: कुजचिद गोपवेशं च चवेष्टितं गोपबालकैः। शतश्रृज्भाचलोत्कू्ट _ रम्ये . वृन्दावने. बने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.1133)
- **Original**: निकरं॑ कामधेनूनां रक्षत्त॑ शिशुरूपिणम्‌ू । गोलोके. विरजातीरे पारिजातवने.. बने
- **Translation**: 

---

