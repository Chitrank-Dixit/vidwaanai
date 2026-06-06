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

### Verse 1 (Vishnu Puran 0.4341)
- **Original**: हे रंजन्‌ ! ऐसी बस्तु कौन-सो है 2?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4342)
- **Original**: [तु अपनेहीको देख--] समस्त प्रजाके लिये तू राजा है, पिताके लिये पुत्र है, शत्रुके लिये झन्रु है; पत्रीका पति है और पुत्रका फ्ता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4343)
- **Original**: ऐे एजन्‌ ! बह, मे गैंतुड्े क्या क हर 2
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4344)
- **Original**: ह महीपते ! तू क्या यह सिर है, अथवा प्रीवा है या पेट अथवा पादादिमेंसे कोई है ? तथा ये सिर आदि भी तेरे कया हैं 2?
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4345)
- **Original**: हे पृथिवीश्चवर ! तू इन समस्त अवयवॉसे पृथक है; अतः साबधान होकर बिचार कि 'मैं कौन हैँ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4346)
- **Original**: हे महाराज ! आत्मतन्त्व इस प्रकपर व्यवस्थित है। उसे सबसे पृथक करके ही बताया जा सकता है । तो फिर, मैं उसे 'अहं' शब्दसे कैसे बतला सकता हूँ ?
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4347)
- **Original**: न जीर नि इति श्रीविष्णुपुराणे द्वितीयेंडशे त्रयोदशोध्याय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4348)
- **Original**: न और चोदहयाँ अध्याय जड़भरत और सौबीरनरेश्नका संवाद अ्रीपराशर उवाच निशम्य तस्थेति बच: परमार्थसमन्वितम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4349)
- **Original**: प्रश्रयावनतो भूल्वा तमाह नृपति्द्धिजम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4350)
- **Original**: 9 ण्जोचाच भगवन्यत्त्वया प्रोक्ते परमार्थमयं बच: । श्रुते तस्मिन्भ्रमन्‍्तीव मनसो मम वृत्तव:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4351)
- **Original**: 2 एतद्विबिकविज्ञानं यदशेषेषु_ उन्तुषु । भवता दर्शितं विप्र तत्परं प्रकृतेमहत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4352)
- **Original**: 3 नाहँ वहामि शिविकां शिव्ििका न मयि स्थिता । शारीरमन्यदस्मत्तो येनेये झिलिका धृता
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4353)
- **Original**: । 4 गुणप्रवृत्त्या भूतानां प्रवृत्ति: कर्मचोदिता । प्रवर्तन्ते गुणा होते कि ममेति त्वयोदितम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4354)
- **Original**: 5 एतस्मिन्यरमार्थज्ष मम श्रोत्रपर्थ गते। मनो विह्नलतामेति परमार्थार्थितां गतम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4355)
- **Original**: 686 श्रीपरावारणी बोले--उनके ये परमार्थमय वचन सुनकर राजाने विनयाबतत होकर उन विप्रवरसे कहा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4356)
- **Original**: राजा बोले--भगयन्‌ ! आपने जो परमार्थमय वचन कहे हैं उन्हें सुनकर मेरी मनोवृत्तियाँ भ्रान्त-सी हो गयी हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4357)
- **Original**: हे तिप्र ! आपने सम्पूर्ण जीबॉमें व्याप्त जिस असंग विज्ञानका दिग्दर्शन कराया है कह प्रकृतिसे परे ब्रह्म ही है (इसमें मुझे क्लेई सन्‍्देह तहीं है]
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4358)
- **Original**: परंतु आपने जो कहा कि में दिव्चिकाक्तरे खहन नहीं कर रहा हूँ, शित्रिका मेरे ऊपर नहीं है, जिसने इसे लठा रस्वा है वत्र दरीर मुझसे अत्यन्त पृथक है। जीवॉडी प्रयृत्ति गुणों (सत्त्व, रज; तम) कौ प्रेरणासे होती है और गुण कमौसे प्रेरित होकर प्रवृत्त होते हैं--इसमें मेरा कतृत्व कैसे माना जा सकता है ?
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4359)
- **Original**: हे परसार्थज्ञ ! यह बात मेरे कानॉमें पड़ते ही मेरा मन परमार्थका जिज्ञास होकर घड़ा उतायल्ा हो रहा है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4360)
- **Original**: अआन् 14 ] द्वितीय अंञझ 157 पूर्वमेल महाभाग॑ कपिलर्षिमह द्विज
- **Translation**: 

---

