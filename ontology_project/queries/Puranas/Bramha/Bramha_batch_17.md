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

### Verse 1 (Bramha 0.321)
- **Original**: दिया। पारदोंके सारे केश उड़ा दिये। चितामें जलनेसे रोक दिया। उन्हींके आश्रममें बह , धर्मविजयी राजा सगरने इस पृथ्वीकों जीतकर अश्वमेध-यज्ञकी दीक्षा ली और अश्वको देशमें बिचरनेके लिये छोड़ा। वह अश्व जब पूर्व-दक्षिण ःु
- **Translation**: 

---

### Verse 2 (Bramha 0.322)
- **Original**: समुद्रके तटपर विचर रहा था, डस समय किसीने
- **Translation**: 

---

### Verse 3 (Bramha 0.323)
- **Original**: ।उसको चुरा लिया और पृथ्वीके भीतर छिपा है
- **Translation**: 

---

### Verse 4 (Bramha 0.324)
- **Original**: दिया। राजाने अपने पुजॉसे उस प्रदेशको खुदवाया। ; 2 0
- **Translation**: 

---

### Verse 5 (Bramha 0.325)
- **Original**: सह सागरकी खुदाई होते समय उन्होंने वहाँ [1 7 8:12 कै)
- **Translation**: 

---

### Verse 6 (Bramha 0.326)
- **Original**: आदिपुरुष भगवान्‌ विष्णुको जो हरि, कृष्ण और
- **Translation**: 

---

### Verse 7 (Bramha 0.327)
- **Original**: । प्रजापति नामसे भी प्रसिद्ध हैं, महर्षि कपिलके रूपमें शयन करते देखा। जागनेपर उनके नेत्रोंके गर्भ जहरके साथ ही प्रकट हुआ। वही महाराज
- **Translation**: 

---

### Verse 8 (Bramha 0.328)
- **Original**: का सगर हुए। और्वने बालकके जातकर्म आदि
- **Translation**: 

---

### Verse 9 (Bramha 0.329)
- **Original**: संस्कार किये, खेद-शास्त्र पढ़ाये तथा आग्नेय- अस्त्र भी प्रदान किया, जो देवताओंके लिये भी दुःसह है। उसीसे सगरने हैहयबंशी क्षत्रियोंका विनाश किया और लोकमें बड़ी भारों कीर्ति पायी। तदनन्तर उन्होंने शक, यबन, काम्बोज, पारद तथा पहुचगणोंका सर्वनाश करनेके लिये उद्योग किया। वीरबर महात्मा सगरकी मार
- **Translation**: 

---

### Verse 10 (Bramha 0.330)
- **Original**: 18 ' + संक्षिप्त ब्रह्मपुराण * तेजसे वे सभी जलकर भस्म हो गये। केवल चार
- **Translation**: 

---

### Verse 11 (Bramha 0.331)
- **Original**: की। उसके भीतर तिलके बराबर साठ हजार गर्भ ही बचे, जिनके नाम है--बर्षिकेतु, सुकेतु, धर्मरथ
- **Translation**: 

---

### Verse 12 (Bramha 0.332)
- **Original**: थे। वे समयानुसार सुखपूर्वक बढ़ने लगे। राजाने और पञ्ननद। ये ही राजाके वंश चलानेवाले हुए।
- **Translation**: 

---

### Verse 13 (Bramha 0.333)
- **Original**: उन सब गर्भोंकों घीसे भरे हुए घड़ोंमें रखवा दिया कपिलरूपधारी भगवान्‌ नारायणने उन्हें वरदान
- **Translation**: 

---

### Verse 14 (Bramha 0.334)
- **Original**: और उनका पोषण करनेके लिये प्रत्येकके पीछे दिया कि “राजा इक्ष्वाकुका बंश अक्षय होगा और
- **Translation**: 

---

### Verse 15 (Bramha 0.335)
- **Original**: एक-एक धाय नियुक्त कर दी। तत्पक्षात्‌ क्रमशः इसकी कीर्ति कभी मिट नहीं सकती।' भगवानने
- **Translation**: 

---

### Verse 16 (Bramha 0.336)
- **Original**: दस महीनोंमें सगरकी प्रसन्नता बढ़ानेवाले वे सभी समुद्रको सगरका पुत्र बना दिया और अन्तमें उन्हें
- **Translation**: 

---

### Verse 17 (Bramha 0.337)
- **Original**: कुमार उठ खड़े हुए। पञ्नजन ही राजा बनाये अक्षय स्वर्गवासके लिये भी आशीर्वाद दिया। उस
- **Translation**: 

---

### Verse 18 (Bramha 0.338)
- **Original**: गये। पद्नजनके पुत्र अंशुमान्‌ हुए, जो बड़े समय समुद्रने अर्ध्य लेकर महाराज सगरका वन्दन
- **Translation**: 

---

### Verse 19 (Bramha 0.339)
- **Original**: पराक्रमी थे। उनके पुत्र दिलीप हुए, जो खट्वाड़ुके किया। सगरका पुत्र होनेके कारण ही समुद्रका
- **Translation**: 

---

### Verse 20 (Bramha 0.340)
- **Original**: नामसे भी प्रसिद्ध हैं, जिन्होंने स्वर्गसे यहाँ आकर नाम सागर हुआ। उन्होंने अश्वमेध-यज्ञके उस
- **Translation**: 

---

