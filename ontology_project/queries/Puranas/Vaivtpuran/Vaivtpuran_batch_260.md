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

### Verse 1 (Vaivtpuran 13.11342)
- **Original**: पैरोंमें रत्नमय मझीर शोभा दे रहे थे। दो रत्ननिर्मित मन लगानेवाले श्रीहरि संध्याकों बलराम और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11343)
- **Original**: कुण्डलोंकी प्रभासे उनके गण्डस्थल अत्यन्त ग्वालबालोंके साथ घर गये। इस प्रकार एक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11344)
- **Original**: उद्दीप्त हो रहे थे। श्यामसुन्दरका श्रीविग्रह करोड़ों वर्षतक भगवानने ऐसा ही किया। वे प्रतिदिन गौओं,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11345)
- **Original**: कन्दर्पोंकी लावण्यलीलाका धाम था। वे मनको ग्वालबालों तथा बलरामजीके साथ यमुनातटपर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11346)
- **Original**: मोहे लेते थे। उनके श्रीअड्भ चन्दन, अगुरु, अभय देहि गोविन्द यहिसंहर्ण कुरु
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11347)
- **Original**: वयं त्वां शरणं यामो रक्ष नः शरणागतानू
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11348)
- **Original**: इत्येवमुक्त्वा ते सर्वे तस्थुर्ध्यात्वा पदाम्बुजम्‌ । दूरीकृतक्ष॒ दाबाग्रि: श्रीकृष्णापृतदृष्टित:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11349)
- **Original**: दूरीभूतेउज॒ दावाग्रीौ.. विपत्तौं. प्राणसंकटे । स्तोत्रमेतत्‌ू पठित्वा च मुच्यते नात्र संशय:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11350)
- **Original**: शब्रुसैन्य॑ क्षयं याति सर्वत्र विजयी भबेत्‌ । इहलोके हरेर्भक्तिमनते दास्यं॑ लभेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11351)
- **Original**: (19। 173-181)
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11352)
- **Original**: * श्रीकृष्णजन्मखण्ड + 505 क्कककऋक़ऋऋ#ऋ ऋऋ कक ऋकऋ कक 4 #####ऋ## 44868 5 ### 55% ####### 8 # # कस्तूरी और कुछ्ूूमसे चर्चित थे। वे पारिजातपुष्पोंकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11353)
- **Original**: वही पीछे और अगल-बगलमें भी दृष्टिगोचर हुई। मालाओंसे विभूषित थे। उनकी अड्गकान्ति नूतन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11354)
- **Original**: मुने! वहाँ वृन्दावनमें सब कुछ श्रीकृष्णके ही जलधरकी श्याम शोभाको लज्जित कर रही थी।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11355)
- **Original**: तुल्य देख जगदगुरु ब्रह्मा उसी रूपका ध्यान करते शरीरमें नूतन यौवनका अछ्डुर प्रस्फुटित हो रहा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11356)
- **Original**: हुए वहाँ बैठ गये। गौएँ, बछड़े, बालक, लता, था। मस्तकपर मोरपंखका मुकुट और उसमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11357)
- **Original**: गुल्म और वीरुध आदि सारा वृन्दावन ब्रह्माजीको मालतीकी मालाओंका संयोग बड़ा मनोहर जान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11358)
- **Original**: श्यामसुन्दरके ही रूपमें दिखायी दिया। यह परम पड़ता था। अपने अड्जोंकी सौन्दर्यमयी दीप्तिसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11359)
- **Original**: आश्चर्य देखकर ब्रह्माजीने फिर ध्यान लगाया। वे आभूषणोंको भी भूषित कर रहे थे। शरत्कालकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11360)
- **Original**: अब उन्हें सारी त्रिलोकी श्रीकृष्णके सिवा और पूर्णिमाके चन्द्रमाकी प्रभाकों लूट लेनेवाले मुखकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11361)
- **Original**: कुछ भी नहीं दिखायी दी। कहाँ गये वृक्ष ? कहाँ कान्तिसे वे परम सुन्दर प्रतीत होते थे। ओठ
- **Translation**: 

---

