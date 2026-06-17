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

### Verse 1 (Bhagwat_Geeta 18.1532)
- **Original**: हे पार्थ! मनुष्य जिस बुद्धिके द्वारा धर्म और अधर्मको तथा कर्तव्य और अकर्तव्यको भी यथार्थ नहीं जानता, वह बुद्धि राजसी है
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 18.1533)
- **Original**: अधर्म॑ धर्ममिति या मन्यते तमसावृता। सर्वार्थान्विपरीतां श्र बुद्द्धिः सा पार्थ तामसी
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 18.1534)
- **Original**: हे अर्जुन ! जो तमोगुणसे घिरी हुई बुद्धि अधर्मको भी “यह धर्म है' ऐसा मान लेती है तथा इसी प्रकार अन्य सम्पूर्ण पदार्थोकों भी विपरीत मान लेती है, वह बुद्धि तामसी है
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 18.1535)
- **Original**: धृत्या यया धारयते मनःप्राणेन्द्रियक्रिया: । योगेनाव्यभिचारिण्या धृतिः सा पार्थ सात्त्विकी
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 18.1536)
- **Original**: हे पार्थ! जिस अव्यभिचारिणी धारणशक्तिसे' मनुष्य ध्यानयोगके द्वारा मन, प्राण और इच्द्रियोंकी क्रियाओंको* धारण करता है, वह धृति सात्त्विकी है
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 18.1537)
- **Original**: 1. भगवद्दिषयके सिवाय अन्य सांसारिक विषयोंको धारण करना ही व्यभिचारदोष है, उस दोषसे जो रहित है, वह “अव्यभिचारिणी धारणा' है। 2. मन, प्राण और इन्द्रियोंको भगवत्प्राप्तिके लिये भजन, ध्यान और
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 18.1538)
- **Original**: * अध्याय 18 * 229 यया तु धर्मकामारर्थान्धृत्या धारयतेउर्जुन। प्रसड़ेन फलाकाडुश्षी क्षति: सा पार्थ राजसी
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 18.1539)
- **Original**: परंतु हे पृथापुत्र अर्जुन! फलकी इच्छावाला मनुष्य जिस धारणशक्तिके द्वारा अत्यन्त आसक्तिसे धर्म, अर्थ और कामोंको धारण करता है, वह धारणशक्ति राजसी है
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 18.1540)
- **Original**: यया स्वप्नं भयं शोकं विषादं मदमेव च। न विमुज्जति दुर्मेधा धृति: सा पार्थ तामसी
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 18.1541)
- **Original**: हे पार्थ! दुष्ट बुद्धिवाला मनुष्य जिस धारणशक्तिके द्वारा निद्रा, भय, चिन्ता और दुःखको तथा उन्मत्तताको भी नहीं छोड़ता अर्थात्‌ धारण किये रहता है--वह धारणशक्ति तामसी है
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 18.1542)
- **Original**: सुखं त्विदानीं त्रिविधं श्रुणु मे भरतर्षभ। अभ्यासाद्रमते यत्र दुःखान्तं च निगच्छति
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 18.1543)
- **Original**: यत्तदग्रे विषमिव परिणामे5मृतोपमम्‌। तत्सुखं सात्त्विकं प्रोक्तमात्मबुर्द्रप्रसादजम्‌
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 18.1544)
- **Original**: हे भरतश्रेष्ठ
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 18.1545)
- **Original**: अब तीन प्रकारके सुखको भी तू मुझसे सुन। जिस सुखमें साधक मनुष्य भजन, ध्यान और सेवादिके अभ्याससे रमण करता है और जिससे दुःखोंके अन्तको प्राप्त हो जाता है--जो ऐसा सुख निष्काम कर्मोमें लगानेका नाम 'उनकी क्रियाओंको धारण करना' है।
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 18.1546)
- **Original**: 230 * श्रीमद्धगवद्रीता * है, वह आरम्भकालमें यद्यपि विषके तुल्य प्रतीत होता है, परन्तु परिणाममें अमृतके तुल्य है; इसलिये वह परमात्मविषयक बुद्धिके प्रसादसे उत्पन्न होनेवाला सुख सात्त्विक कहा गया है
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 18.1547)
- **Original**: विषयेन्द्रियसंयोगाद्यत्तदग्रेडमतोपमम्‌_
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 18.1548)
- **Original**: परिणामे विषमिव तत्सुखं राजसं स्मृतम्‌
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 18.1549)
- **Original**: जो सुख विषय और इन्द्रियोंके संयोगसे होता है, वह पहले--भोगकालमें अमृतके तुल्य प्रतीत होनेपर भी परिणाममें विषके तुल्य* है; इसलिये वह सुख राजस कहा गया है
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 18.1550)
- **Original**: यदग्रे चानुबन्धे च सुखं मोहनमात्मन:। निद्रालस्यप्रमादोत्थं तत्तामसमुदाहतम्‌
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 18.1551)
- **Original**: जो सुख भोगकालमें तथा परिणाममें भी आत्माको मोहित करनेवाला है--वह निद्रा, आलस्य और प्रमादसे उत्पन्न सुख तामस कहा गया है
- **Translation**: 

---

