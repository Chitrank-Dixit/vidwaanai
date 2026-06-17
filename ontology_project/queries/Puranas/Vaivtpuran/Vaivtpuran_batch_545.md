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

### Verse 1 (Vaivtpuran 36.8002)
- **Original**: ब्रह्माको लक्ष्मीका जो परम शुभकारक कवच मन्त्र सनत्कुमारने दिया था। उन्होंने ही गोपनीय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.8003)
- **Original**: प्रदान किया था, ठसे सुनों। उस कवचको पाकर स्तोत्र, उसका चरित, पूजाकी विधि और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.8004)
- **Original**: ब्रह्माने कमलपर बैठे-बैठे जगत्‌की सृष्टि की और सामवेदोक मनोहर ध्यान भी बतलाया था। महालक्ष्मीकी कृपासे बे लक्ष्मीवान्‌ हो गये। फिर दुर्गा कवच, गुदा स्तोन्र और दशाक्षर-मन्त्र
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.8005)
- **Original**: पद्मालयासे वरदान प्राप्त करके ब्रह्मा लोकोंके पूर्वकालमें दुर्वासाने पुष्कराक्ष-पुत्रको प्रदान किया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.8006)
- **Original**: अधी श्वर हो गये। उन्हीं ब्रह्माने पद्मकल्पमें अपने था। इसके पश्चात्‌ देवीके उस परम अद्भुत सम्पूर्ण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.8007)
- **Original**: प्रिय पुत्र बुद्धिमान्‌ सनत्कुमारकों यह परम अद्भुत चरितको सुनोगे, जिसे उन्होंने महायुद्धके आरम्भमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.8008)
- **Original**: कवच दिया था। नारद! सनत्कुमारने वह कबच प्रार्था। करनेपर बतलाया था। अब मैँ तुम्हें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.8009)
- **Original**: पुष्कराक्षकों प्रदान किया था, जिसके पढ़ने एवं महालक्ष्मीका मन्त्र बतलाता हूँ; उसे श्रवण करो।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.8010)
- **Original**: धारण करनेसे ब्रह्मा समस्त सिद्धोंके स्वामी, * 37 श्रीं कमलवासिन्य स्वाहा' यही वह परम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.8011)
- **Original**: महान्‌ परमैश्वर्यसे सम्पन्न और सम्पूर्ण सम्पदाओंसे अद्भुत मन्त्र है। मुने! सनत्कुमारने बुद्धिमान्‌ युक्त हो गये। पुष्कराक्षको जो पूजाविधि और सामवेदोक्त ध्यान सम्पूर्ण सम्पत्तियोंके प्रदाता इस कवचके बतलाया था, उसे सुनो। सहस्नदलकमल जिनका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.8012)
- **Original**: प्रजापति ऋषि हैं, बृहती छन्द है, स्वयं पद्मालया आसन है, जो भगवान्‌ पद्मनाभकी सती-साध्वी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.8013)
- **Original**: देवी हैं और धर्म-अर्थ-काम-मोक्षमें इसका प्रियतमा हैं, कमल जिनका घर है, जिनका मुख
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.8014)
- **Original**: विनियोग किया जाता है। यह परम अद्भुत कबच कमलके सदृश और नेत्र कमलपत्रकी-सी आभावाले
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.8015)
- **Original**: महापुरुषेकि पुण्यका कारण है।' 3» ह्लीं कमलवासिन्य हैं, कमलका फूल जिन्हें अधिक प्रिय है, जो [स्वाहा' मेरे मस्तककी रक्षा करे। “श्रीं' मेरे कमल-पुष्पकी शय्यापर शयन करती हैं, जिनके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.8016)
- **Original**: कपालकी और 'श्रीं श्रियै नम: ' नेत्रोंकी रक्षा करे। हाथमें कमल शोभा पाता है, जो कमल-पुष्पोंकी [3 श्रीं श्रियै स्वाहा' सदा दोनों कानोंकी रक्षा मालासे विभूषित हैं, कमलॉंके आभूषण जिनकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.8017)
- **Original**: करे। '30 हुं श्रीं क्लीं महालक्ष्म्यै स्वाहा' मेरी शोभा बढ़ाते हैं, जो स्वयं कमलॉकी शोभाकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.8018)
- **Original**: नासिकाकी रक्षा करे।' 3» श्रीं पद्मालयायै स्वाहा '
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.8019)
- **Original**: 378 + संक्षिस ब्रह्मैवर्तपुराण * कक कक कक; कक कक ###############&########
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.8020)
- **Original**: #ऋ# 5 $%%$ कक क सदा दाँतोंकी रक्षा करें। '3& श्रीं कृष्णप्रियायै
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.8021)
- **Original**: नामक परम अद्भुत कबचका वर्णन कर दिया। स्वाहा' सदा दाँतोंके छिद्रोंको रक्षा करे। '37
- **Translation**: 

---

