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

### Verse 1 (Vaivtpuran 18.1379)
- **Original**: विद्यमान है। ब्रह्माजीसे उत्पन्न जो बालक अत्यन्त क्माँमें दक्ष होनेके कारण 'दक्ष' कहलाया। वेदोंमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1380)
- **Original**: तेजस्वी हुआ, उसका नाम “भृगु' हुआ। जो कर्दम शब्द छायाके अर्थमें विद्यमान है। जो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1381)
- **Original**: बालक होनेपर भी तत्काल अत्यन्त तेजके कारण बालक ब्रह्माजीके कर्दम अर्थात्‌ छायासे प्रकट
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1382)
- **Original**: अरुण वर्णका हो गया और उच्च कोटिकी हुआ, उसका नाम 'कर्दम' रखा-गया4 इसी तरह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1383)
- **Original**: तपस्थाके कारण तेजसे प्रज्वलित होने लगा, वह मरीचि शब्द वेदोंमें तेजोभेदके अर्थमें आता है।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1384)
- **Original**: 'अरुण' नामसे विख्यात हुआ। जिस योगीके अत: जो बालक तत्काल अत्यन्त तेजस्वी रूपमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1385)
- **Original**: योगबलसे हंस उसके अधीन रहते थे, वह परम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1386)
- **Original**: [66 ] अऋऋ आफ ऊऋऊ ऊकफ्ऊऋऊ# कक य #ऋऋऋकऋ%ऋ#क्ऋफऋ़ कफ कफ ऋआऋ आऊऋ #ऋआ #आ कफ आऋआऋऋऋऋआआऋ आअआआआऋआ भआऋआऊऊऋ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1387)
- **Original**: + ख्रह्मस्त्रण्ड + 67 ।।।[।/8।0
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1388)
- **Original**: है है है ह है है
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1389)
- **Original**: 6 86 3463 6 36514) 3।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1390)
- **Original**: योगीनद्र बालक “हंसो' नामसे बिख्यात हुआ।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1391)
- **Original**: तत्काल प्रकर हुआ जो बालक वशीभूत और शिष्य होकर विधाताका अत्यन्त प्रीतिपात्र हुआ, उसका नाम 'वसिष्ठ' रखा गया। जिस बालकका तपमें सदा प्रयज्ञ देखा गया तथा जो सम्पूर्ण कर्मोंमें संयत रहा, वह अपने उसी गुणके कारण
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1392)
- **Original**: “यति' कहलाया। वेदोंमें 'पुल' शब्द तपस्याके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1393)
- **Original**: अर्थमें आता है और “ह' स्फुट-अर्थमें। जिस बालकमें स्फुटरूपसे तपस्याका समूह लक्षित हुआ, बह उसी लक्षणसे 'पुलह' कहलाया। (पुलका अर्थ है--तप:-समूह और 'स्त्य' शब्द अस्ति-' है” के अर्थमें आया है) जिसके पूर्वजन्मोंक तपःसमूह विद्यमान हैं; इसी कारण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1394)
- **Original**: जो तपः-संघस्वरूप है; वह इसी व्युत्पत्तिके द्वारा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1395)
- **Original**: *पुलस्त्य' के नामसे विख्यात हुआ। “त्रि' शब्द त्रिगुणमयी प्रकृतिके अर्थमें आता है और 'अ' बिष्णुके अर्थमें। जिसकी उन दोनोंके प्रति समान भक्ति है, उस बालककों “अत्रि" कहा गया। जिसके मस्तकपर तपस्याके तेजसे प्रकट हुई अग्रिशिखास्वरूपिणी पाँच जटाएँ थीं, उसका नाम
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1396)
- **Original**: 'पशञ्चशिख' हुआ। जिसने दूसरे जन्ममें आन्तरिक अन्धकारसे रहित प्रदेशमें तप किया था, उस शिशुका नाम “अपान्तरतमा' हुआ। जो स्वयं तपस्या करता और दूसरोंको भी उसकी प्राप्ति करा सकता था तथा जो तपस्याका भार बहन करनेमें पूर्ण समर्थ था, वह अपनी इसी योग्यताके कारण “वोदु' कहलाया। मुने! जो बालक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1397)
- **Original**: तपस्याके तेजसे सदा दीप्तिमानू रहता था तथा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1398)
- **Original**: तपस्यामें जिसके चित्तकी स्वाभाविक रुचि थी, वह 'रुचि' नामसे प्रसिद्ध हुआ। जो ब्रह्माजीके क्रोधके समय ग्यारहकी संख्यामें प्रकट हुए और रोने लगे, वे रोदनके हो कारण 'रुद्र' कहलाये। सौति फिर बोले--जिनमें सत्त्वगुणकी
- **Translation**: 

---

