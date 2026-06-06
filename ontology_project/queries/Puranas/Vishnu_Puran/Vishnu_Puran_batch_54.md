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

### Verse 1 (Vishnu Puran 0.1061)
- **Original**: -हे सर्वपावनि मातेश्वरि ! हमारे कोश (खजाना) , गोष्ठ (पन्चु-शाला) , गृह, भोगसामग्री, दरीर और स्त्री आदिको आप कभी न त्यागें अर्थात्‌ इनमें भरपूर रहें
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1062)
- **Original**: अयथि विष्णुवक्ष:स्थल निवासिनि! हमारे पूत्र, सूहद, पश्चु और भूषण आदिको आप कभी न छोड़ें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1063)
- **Original**: है अमले ! जिन मनुष्योंको तुम छोड़ देती हो उन्हें सत्व (मानसिक बऊ), सत्य, शौच और शील आदि गुण भी जीघ हो त्याग देते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1064)
- **Original**: और तुम्हारी कृषा दृष्टि होनेपर तो गुणहीन पुरुष भी शीघ्र ही शीऊ आदि सम्पूर्ण गुण और कुलीनता तथा ऐश्वर्य आदिसे सम्पन्न हो जाते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1065)
- **Original**: है देवि ! जिसपर तुम्हारी कृप्रादृष्टि है यही प्रशंसनीय है, वही गुणी है, वही धन्यभाग्य है, वही कुलीन और बूद्धिमान्‌ है तथा वही शूरवीर और पराक्रमो है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1066)
- **Original**: हे विष्णुप्रिये ! हे जगज्जननि ! तुम जिससे विमुख हो उसके तो शोौल आदि सभी गुण तुरन्त अखगुणरूप हो जाते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1067)
- **Original**: हे देवि ! तुम्हारे गुणोंका वर्णन करनेमें तो श्रीज्रह्माजीकी रसना भी समर्थ नहीं है। [फिर मैं क्या कर सकता हूँ ?] अतः हे कमलनयने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1068)
- **Original**: अब मुझपर प्रसन्न हो और मुझे कभी न छोड़ो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1069)
- **Original**: श्रीपराशरजी बोले--हे ट्विज ! इस प्रकार सम्यक्‌ स्तुति किये जानेपर सर्वभूतस्थिता श्रीलक्ष्मीजी सब देवताओंके सुनते हुए इद्से इस प्रकार बोलीं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1070)
- **Original**: श्रीविष्णुपुराण [ आ0 9 श्रीरवाच परितुष्टास्मि देबेश स्तोत्रेणानेन ते हरे । बर॑ वृणीघ्र यस्त्विष्टो वरदाह॑ तवागता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1071)
- **Original**: 135 इत्र उवाच बरदा यदि मे देवि बराहों यदि वाष्यहम्‌ । त्रैलोक्य न त्वया त्याज्यमेष मेउस्तु बरः परः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1072)
- **Original**: 936 स्तोत्रेण यस्तथैतेन त्वां स्तोष्यत्यब्धिसम्भवे । स त्वया न परित्याज्यो द्वितीयो5स्तु वरो मम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1073)
- **Original**: 137 श्रौदवाच त्रैलोक्यं त्रिद्शश्रेष्ठ न सन्तयक्ष्यामि खास । द्तो बरो मया यस्ते स्तोत्नाराधनतुष्टया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1074)
- **Original**: 138 यश्व साय॑ तथा प्रात: स्तोत्रेणानेन मानव: । माँ स्तोष्यति न तस्याहं भविष्यामि पराइसुखी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1075)
- **Original**: 139 आपवशर उवाच एवं ददो वरं देवी देवराजाय वै पुरा। मैत्रेय श्रीर्महाभागा स्तोत्राराधनतोषिता
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1076)
- **Original**: 140 भृगो: ख्यात्यां समुयत्ना श्रीः पूर्वपुदधे: पुन: । देवदानवयत्रेन अ्रसूताउपृतमन्धने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1077)
- **Original**: 141 एवं यदा जगत्स्वामी देवदेयो जनार्दन: । अवतार करोत्येषा तदा श्रीस्तत्सहायिनी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1078)
- **Original**: 142 पुनश्न पद्मादुत्यन्ना आदित्यो5भूद्यदा हरिः । यदा तु भार्गवो रामस्तदाभूद्धरणी त्वियम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1079)
- **Original**: 143 राघवत्वे$भवत्सीता रुक्मिणी कृष्णजन्मनि । अन्येषु चावतारेषु विष्णोरेषानपायिनी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1080)
- **Original**: 144 देवत्वे देवदेहेयं॑ मनुष्यत्वे च मानुषी। विष्णोर्देहानुरूपां जै करोत्येषात्मनस्तनुम्‌
- **Translation**: 

---

