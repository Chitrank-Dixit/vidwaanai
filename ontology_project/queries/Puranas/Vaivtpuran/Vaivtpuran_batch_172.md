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

### Verse 1 (Vaivtpuran 12.6534)
- **Original**: प्रजापति ऋषि हैं, बृहती छन्‍्द है और स्वयं मिलता है, वह उसे श्रीगणेशकी कृपासे प्राप्त हो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6535)
- **Original**: लम्बोदर गणेश देवता हैं। धर्म, अर्थ, काम और जाता है-यह ध्रुव सत्य है। मोक्षमें इसका विनियोग कहा गया है। मुने! यह नारदजीने कहा--प्रभो! गणेशके स्तोत्र
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6536)
- **Original**: सम्पूर्ण कवचोंका सारभूत है।' 30 ग॑ हुं श्रीगणेशाय तथा उनके मनोहर पूजनको तो मैंने सुन लिया,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6537)
- **Original**: स्वाहा' यह मेरे मस्तककी रक्षा करे। बत्तीस
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6538)
- **Original**: केरड + संक्षिम ब्रह्मवैवर्तपुराण « 5&&# ##% ## # % # # 5 # % # 5 # क 4 इक 5 ऋ कक 5 अ 55% 5 5 % $ 5 5 5 # % 44 4 4 4 44 8858 # 888 ###& 948 8 8 8 5 8 55 # अक्षरोंवाला मन्त्र सदा मेरे ललाटको बचाबे। ' 34
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6539)
- **Original**: शयन और जागरणकालमें योगियोंके गुरु मेरा हीं क्लीं श्री गम्‌' यह निरन्तर मेरे नेत्रोंकी रक्षा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6540)
- **Original**: पालन करें। बत्स ! इस प्रकार जो सम्पूर्ण मनत्रसमूहोंका करे। विप्लेश भूतलपर सदा मेरे तालुकी रक्षा करें।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6541)
- **Original**: विग्रहस्वरूप है, उस परम अद्भुत संसारमोहन ' 3» हीं श्रीं क्लीं' यह निरन्तर मेरी नासिकाकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6542)
- **Original**: नामक कवचका तुमसे वर्णन कर दिया। सूर्यनन्दन! रक्षा करे तथा “3 गाँ गं शूर्पकर्णाय स्वाहा ' यह
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6543)
- **Original**: इसे प्राचीनकालमें गोलोकके वृन्दाबनमें रासमण्डलके मेरे ओठको सुरक्षित रखे। षोडशाक्षर-मन्त्र मेरे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6544)
- **Original**: अवसरपर श्रीकृष्णने मुझ विनीतको दिया था। दाँत, तालु और जीभको बचावे। '3» लं॑ श्रीं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6545)
- **Original**: वही मैंने तुम्हें प्रदान किया है। तुम इसे जिस- लम्बोदराय स्वाहा” सदा गण्डस्थलकी रक्षा करे।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6546)
- **Original**: किसीको मत दे डालना। यह परम श्रेष्ठ, सर्वपूज्य ' 3» क्लीं ह्वीं विध्ननाशाय स्वाहा' सदा कानोंकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6547)
- **Original**: और सम्पूर्ण संकटोंसे उबारनेबाला है। जो मनुष्य रक्षा करे। '3» श्रीं ग॑ गजाननाय स्वाहा' सदा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6548)
- **Original**: विधिपूर्वक गुरुकी अभ्यर्चना करके इस कवचको कंधोंकी रक्षा करे। '3& हीं विनायकाय स्वाहा'
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6549)
- **Original**: गलेमें अथवा दक्षिण भुजापर धारण करता है, वह सदा पृष्ठभागकी रक्षा करे।' 3» क्लीं हीं' कंकालकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6550)
- **Original**: निस्संदेह विष्णु ही है। ग्रहेन्द्र! हजारों अश्वमेध और 'गं' वक्ष:स्थलकी रक्षा करे। विप्ननिहन्ता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6551)
- **Original**: और सैकड़ों वाजपेय-यज्ञ इस कवचकी सोलहवीं हाथ, पैर तथा सर्वाज्गको सुरक्षित रखे। पूर्वदिशामें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6552)
- **Original**: कलाकी समानता नहीं कर सकते। जो मनुष्य इस लम्बोदर और अग्रिकोणमें विप्ननायक रक्षा करें।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6553)
- **Original**: कवचको जाने बिना शंकर-सुवन गणेशकी भक्ति दक्षिणमें विश्लेश और नैऋत्यकोणमें गजानन रक्षा
- **Translation**: 

---

