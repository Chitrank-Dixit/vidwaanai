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

### Verse 1 (Vishnu Puran 0.12121)
- **Original**: श्रीपराझरजी कोले--हे सहाभाग ! इसी विषयों महामति व्यासदेवने जो कुछ कहा है वह मैं यथावत्‌ बर्णन करता हूँ, सुनो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12122)
- **Original**: एक बार मुनियोंमें [परस्पर] पुण्यके विषयमें यह वार्ताछाप हुआ कि 'किस समयमें थोड़ा-सा पुण्य भी महान्‌ फल देता है और कौन उसका सुखपूर्वक अनुष्ठान कर सकते हैं ?'
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12123)
- **Original**: हे मैत्रेय ! वे समस्त मुनिश्रेष्ठ इस सन्देहका निर्णय करनेके लिये महामुनि व्यासजीके पास यह प्रश्न पूछने गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12124)
- **Original**: हे ट्विज ! कहाँ पहुँचनेपर उन मुनिजनोंने मेरे पुत्र महाभाग व्यासजीकों गद्जाजीमें आधा स्त्रान किये देखा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12125)
- **Original**: ते महर्षिंगण व्यासजीके स्नान कर चुकनेकी प्रतीक्षामें उस महानदीके तटपर वुक्षोंके तले बैठे रहे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12126)
- **Original**: उस समय गक्नजीमें डुबको लगाये मेरे पुत्र व्यासने जलसे उठकर उन मुनिजनॉंके सुनते हुए (कलियुग ही ग्रेष् है, शुद्र ही श्रेष्ठ है' यह कचन कहा । ऐसा कहकर उन्होंने फिर जलमें गोता छगाया और फिर उठकर कहां-- “झुद्ग ! तुप्त ही ओरष्ठ हो, तुम ही धन्य हो"
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12127)
- **Original**: यह कहकर ले महामुनि फिर जलमें मग्र हो गये और फिर खड़े होकर बोकछे--“'स्तियाँ ही साधु हैं, वे हो धन्य हैं, उनसे अधिक धन्य और कौन है ?”
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12128)
- **Original**: ततः स््रात्वा यथान्यायमायान्तं च कृतक्रियम्‌। उपतस्थुर्महाभागं मुनयस्ते सुतें मम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12129)
- **Original**: 9 कृतसंवन्दनांशआाह कृतासनपरिग्रहान्‌ । किमर्थमागता यूयमिति सत्यवतीसुतः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12130)
- **Original**: 10 तमूचु: संशय प्रष्ट भवन्त॑ वयमागता: । अलं तेनास्तु तावन्न: कथ्यतामपरं त्वया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12131)
- **Original**: 11 कलिस्साध्विति यत्रोक्ते शुद्र: साध्विति योषित: । यदाह भगवान्‌ साधु धन्याश्रेति पुनः पुनः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12132)
- **Original**: 12 तत्सव॑ श्रोतुमिच्छामो न चेद्‌ गुहां महामुने । तत्कथ्यतां ततो हत्स्थं पृच्छामस्त्वां प्रयोजनम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12133)
- **Original**: 13 श्रीपयाशर उवाच इत्युक्तो मुनिभिरवव्यास: प्रहस्येदमथात्रवीतू । श्रूयतां भो मुनिश्रेष्ठा यदुक्ते साधु साध्विति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12134)
- **Original**: 14 श्रीग्यास उवाच यत्कृते अरे पागल शोक हायमेन हद । तपसो ब्रह्मचर्यस्य जपादेक्ष फल द्विजा:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12135)
- **Original**: च्राप्नोति पुरुषस्तेन कल्लिस्साध्विति भाषितम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12136)
- **Original**: 16 ध्यायन्कृते यजन्यज़ैख्नेतायां द्वापरेडर्चयन। यदाप्नोति तदाप्ोति कलो संकीरत्य केशवम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12137)
- **Original**: 17 धर्मोत्कर्षमतीवात्र प्राप्नोति पुरुष: कलौ । अल्पायासेन धर्मज्ञास्तेन तुष्टोउस्म्यहं कले:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12138)
- **Original**: 18 ततस्स्वधर्मसम्प्राप्तैर्यष्टटयं.. विधिवद्धनै:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12139)
- **Original**: 19 उन तय जन बन उमककलण कथा वथा भोज्य॑ वृधेज्या च द्विजन्मनाम्‌ । पतनाय ततो भाव्यं संयमिभिस्सदा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12140)
- **Original**: 20 असम्यक्वरणे दोषस्तेषां सर्वेषु वस्तुषु । भोज्यपेयादिकं चैषां नेच्छाप्राप्तिकरं द्विजा:
- **Translation**: 

---

