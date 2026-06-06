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

### Verse 1 (Vaivtpuran 0.41)
- **Original**: । 12--14)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.42)
- **Original**: * ग्रह्मखण्ड + 3 5555 55555 % 55% 5 % 4 444 4 4 15 47 8 4 64 6 89% # 6488 44688 666 48 88 8
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.43)
- **Original**: 868 8# 84644 68686 6 86 5 888 88858 मतका निरूपण किया गया है? कीजिये। जहाँ गणेशजीके चरित्र, जन्म और बत्स! जिस पुराणमें प्रकृतिके स्वरूपका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.44)
- **Original**: कर्मका तथा उनके गृढ़ कवच, स्तोत्र और निरूपण हुआ हो, गुणोंका लक्षण वर्णित हो तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.45)
- **Original**: मन्त्रोंका बर्णन हो, जो उपाख्यान अत्यन्त अद्भुत “महत्‌' आदि तत्त्वोंका निर्णय किया गया हो;
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.46)
- **Original**: और अपूर्व हो तथा कभी सुननेमें न आया हो, जिसमें गोलोक, वैकुण्ठ, शिवलोक तथा अन्यान्य
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.47)
- **Original**: वह सब मन-ही-मन याद करके इस समय आप स्वर्गादि लोकोंका वर्णन हो तथा अंशों और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.48)
- **Original**: उसका वर्णन करें। परमात्मा श्रीकृष्ण सर्वत्र कलाओंका निरूपण हो, उस पुराणंकों श्रवण
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.49)
- **Original**: परिपूर्ण हैं तथापि इस जगत्‌में पुण्य-द्षेत्र कराइये। सूतनन्दन ! प्राकृत पदार्थ क्या हैं? प्रकृति
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.50)
- **Original**: भारतवर्षमें जन्म (अवतार) लेकर उन्होंने नाना क्या है तथा प्रकृतिसे परे जो आत्मा या परमात्मा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.51)
- **Original**: प्रकारके लीला-बिहार किये। मुने! जिस पुराणमें है, उसका स्वरूप क्‍या है? जिन देवताओं और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.52)
- **Original**: उनके इस अवतार तथा लीला-विहारका वर्णन देवाड़नाओंका भूतलपर गूृढ़रूपसे जन्म या
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.53)
- **Original**: हो, उसकी कथा कहिये। उन्होंने किस पुण्यात्माके अबतरण हुआ है, उनका भी परिचय दीजिये।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.54)
- **Original**: पुण्यमय गृहमें अवतार ग्रहण किया था? किस समुद्रों, पर्वतों और सरिताओंके प्रादुर्भावकी भी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.55)
- **Original**: धन्या, मान्या, पुण्यवती सती नारीने डनको कथा कहिये। प्रकृतिके अंश कौन हैं? उसकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.56)
- **Original**: पुत्ररूपसे उत्पन्न किया था? उसके घरमें प्रकट कलाएँ और उन कलाओंकी भी कलाएँ क्‍या
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.57)
- **Original**: होकर वे भगवान्‌ फिर कहाँ और किस कारणसे हैं? उन सबके शुभ चरित्र, ध्यान, पूजन और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.58)
- **Original**: चले गये? वहाँ जाकर उन्होंने क्या किया और स्तोत्र आदिका बर्णन कीजिये। जिस पुराणमें दुर्गा,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.59)
- **Original**: बहाँसे फिर अपने स्थानपर कैसे आये? किसकी सरस्वती, लक्ष्मी और सावित्रीका वर्णन हो,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.60)
- **Original**: प्रार्थनासे उन्होंने पृथ्वीका भार उतारा? तथा श्रीराधिकाका अत्यन्त अपूर्व और अमृतोपम
- **Translation**: 

---

