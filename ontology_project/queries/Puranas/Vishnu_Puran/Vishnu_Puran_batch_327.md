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

### Verse 1 (Vishnu Puran 0.6521)
- **Original**: प्रसेनेजितो युवनाश्रो$भवत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6522)
- **Original**: तस्य चापुत्रस्यातिनिर्वेदान्पुनीनामाश्रममण्डले निवसतो दयालुभिरमुनिभिरपत्योत्पादनायेष्टि: कृता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6523)
- **Original**: तस्‍स्यां च भध्यरात्रौ निवृत्तायां मन्त्नपूतजलपूर्ण कलश वेदिमध्ये निवेश्य ते मुनय: सुषुपु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6524)
- **Original**: सुप्तेषु तेषु अतील तृदपरीतस्स भूपालस्तमाश्रम॑ विवेश
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6525)
- **Original**: सुप्तांश्व
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6526)
- **Original**: तन्च कलझ- मपरिमेयमाहात्प्यमन्ज््पूते पपौ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6527)
- **Original**: ग्रबुद्धाश्व बैठकर दैत्यसेनाका बध किया था, अतः उसका नाम ककुत्स्थ पड़ा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6528)
- **Original**: ककुत्स्थके अनेना नामक पुत्र हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6529)
- **Original**: अनेनाके पृथु, पृथुके विष्टराश्व, उनके चान्द्र युवनाश्च तथा उस चादर युवनाश्रके ज्ञावस्त नामक पुत्र हुआ जिसने शावस्तो पुरी बसायी थी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6530)
- **Original**: 34--37
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6531)
- **Original**: शावस्तके बृहदश्न तथा नृहदभ्रके कुतरलयाश्रका जन्म हुआ, जिसने वैष्णवत्तेजसे पूर्णता लाभ कर अपने इक्कीस सहस्र पुत्रोंके साथ मिलकर महर्षि उटकके अफ्कारी धुन्धु नामक दैत्यक्ये मारा था; अतः उनका नाम घुस्धुमार हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6532)
- **Original**: 38--40
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6533)
- **Original**: उनके सभी पूत्र धुन्धुके मुखसे निकफे हुए नि:श्रासाप्रिसे जऊूकर मर गये।
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6534)
- **Original**: उनमेंसे केबल दृढ्ाश्व, अन्द्राध और कपिलाश्व--ये तीन ही बचे थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6535)
- **Original**: दृढ्मश्वसे हर्यश्च, हर्यश्वले निकुम्भ, निकुम्भसे अमिताभ, अमिताधसे कृन्नाध्च, कृशाश्वसे प्रसेनजित्‌ और प्रसेनजित्से युवनाश्वका जन्म हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6536)
- **Original**: 43--48
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6537)
- **Original**: युवनाश्व निःसन्तान होनेके कारण खिन्न चित्तसे मुनीश्चरोंके आश्रमोंमें रहा करता था; उसके दु:खसे द्रवोभूत होकर दयालु मुनिजनोने उसके पुत्र उत्पन्न होनेके लिये यज्ञानुप्टान किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6538)
- **Original**: आधी रातके समय उस यज्ञके समाप्त होनेपर मुनिजन मन्लपूत जलका कलइज्ञ वेदीमें रखकर सो गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6539)
- **Original**: उनके सो जानेपर अत्यन्त पिपासाकुल होकर राजाने उस स्थानमें प्रवेश किया । और सोये होनेके कारण डन ऋषियोंकों उन्होंने नहीं जगाया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6540)
- **Original**: तथा उस अपरिमित माहात्म्यशालौ कलडाके मननपूत जलको पी लिया
- **Translation**: 

---

