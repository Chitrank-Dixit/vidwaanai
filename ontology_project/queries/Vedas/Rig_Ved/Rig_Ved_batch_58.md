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

### Verse 1 (Rig Ved 0.1141)
- **Original**: [ऐसी सम्पदा, जो प्रकाशित को जा सके और जो जीवन को प्रकाशित करें, कलंकित न करें। ऐसी सम्पदा की ही "कामना की जानी चाहिए।] [सूक्त - 43 ] [ऋषि- कण्व घौर । देवता- रुद्र- 3 रुद्र, पित्रावरण, 7-9 सोम । छन्द- गायत्री,9 अनुष्टप्‌ ।] 509, कबद्राय प्रचेतसे मीलहुष्टमाय तव्यसे । बोचेम शन्‍्तम हृदे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.1142)
- **Original**: विशिष्ट ज्ञान से सम्पन्न, सुखी एवं बलशालो रुद्रदेव के निमित्त किन सुखप्रद स्त्रेत्रों का पाठ करें ?
- **Translation**: 

---

### Verse 3 (Rig Ved 0.1143)
- **Original**: 510, यथा नो अदिति: करत्पश्वे नृभ्यो यथा गये । यथा तोकाय रुद्रियम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.1144)
- **Original**: अदिति हमारे लिये और हमारे पशुओं, सम्बन्धियों, गौओं और सन्तानों के लिये आरोग्य -वर्धक ओषधियों का उपाय (अन्वेषण-व्यवस्था) करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.1145)
- **Original**: में0 है सु0 4डंड 69 511. यथा नो मित्रो बरुणो यथा रुद्रश्चिकितति। यथा विश्वे सजोषस:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.1146)
- **Original**: मित्र, वरुण और रुद्रदेव जिस प्रकार हमारे हितार्थ प्रयत्त करते हैं, उसी प्रकार अन्य समस्त देवगर्ण भी हमारा कल्याण करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.1147)
- **Original**: 512. गाथपतिं मेधपतिं रुद्रं जलाषभेषजम्‌। तच्छ॑यो: सुम्नमीमहे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.1148)
- **Original**: हम सुखद जल एवं ओषधियों से युक्त, स्तुतियों के स्वामी तथा यज्ञ के स्वामी, रुद्रदेव से आरोग्य सुख की कामना करते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.1149)
- **Original**: स्तुत्प क्चार, अष्टकर्ष एवं रस से पुष्ट ओषधियों के संयोग से आगेग्य सुख प्राण हो सकता है।] 513. यः शुक्र इब सूर्यो हिरण्यमिव रोचते। श्रेष्ठो देवानां बसु:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.1150)
- **Original**: ' सूर्य सदृश सामर्थ्यवान्‌ और स्वर्ण सदृश दीप्तिमान्‌ रुद्रदेव सभी देवों में श्रेष्ठ और ऐश्वर्यवान्‌ हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.1151)
- **Original**: 514, शं॑ न: करत्यवते सुगं मेषाय मेष्ये । नृभ्यो नारिभ्यों गवे
- **Translation**: 

---

### Verse 12 (Rig Ved 0.1152)
- **Original**: हमारे अश्यों, मेढ़ों, भेड़ों, पुरुषों, नारियों और गौओं के लिये वे रुद्रदेव सब प्रकार से मंगलकारी हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.1153)
- **Original**: 515. अस्मे सोम श्रियमधि नि थेहि शतस्य नृणाम्‌। महि श्रवस्तुविनृम्णम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.1154)
- **Original**: है सोमदेव ! हम मनुष्यों को सैकड़ों प्रकार का ऐश्वर्य, तेजयुक्त अन्न, बल और महान्‌ यश प्रदान करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.1155)
- **Original**: 516. मा न: सोम परिबाधो मारातयो जुहुरन्त । आ न इन्दो वाजे भज
- **Translation**: 

---

### Verse 16 (Rig Ved 0.1156)
- **Original**: सोमयाग में बाधा देने वाले शत्रु हमें प्रताड़ित न करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.1157)
- **Original**: कृपण और दुष्टों से हम पीड़ित न हों । हे सोमदेख ! आप हमारे बल में वृद्धि करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.1158)
- **Original**: 517, यास्ते प्रजा अमृतस्य परस्मिन्धामन्नृतस्य । मूर्धा नाभा सोम वेन आभूषन्ती: सोम वेद:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.1159)
- **Original**: है सोमदेव ! यज्ञ के श्रेष्ठ स्थान में प्रतिष्ठित आप अमृत से युक्त हैं । यजन कार्य में सर्वोच्च स्थान पर विभूषित प्रजा को आप जानें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.1160)
- **Original**: सिक्त - 44 ] (ऋषि प्रस्कण्व काण्व । देवता-अग्नि,1-2 अग्नि, अश्विनीकुपार, उषा । छन्द-बार्हत प्रगाथ (विषमा बृहती, समासतो बृहती)
- **Translation**: 

---

