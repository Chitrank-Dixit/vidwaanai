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

### Verse 1 (Sama Ved 0.3181)
- **Original**: 1234. त॑ हि स्वराज॑ वृषभं तमोजसा धिषणे निष्टतक्षतु: । उतोपमानां प्रथमो निषीदर्सि सोमकाम हि ते मन:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3182)
- **Original**: आकाश और पृथ्वी, समर्थ और तेजस्वी इन्द्रदेव को अपनी क्षमता से प्रकट करते हैं। है इन्रदेव ! आप उपमानों में सर्वश्रेष्ठ हैं। आप सोमपान को इच्छा से यज्ञवेदी पर विराजमान होते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3183)
- **Original**: इति सप्तम: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3184)
- **Original**: के के के
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3185)
- **Original**: 9.8 सामवद-संहिता
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3186)
- **Original**: अष्टम; खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3187)
- **Original**: 1235. पवस्व देव आयुषगिद्द्रं गच्छतु ते मदः । बायुमा रोह धर्मणा
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3188)
- **Original**: हे तेजस्वी सोमदेव ! शुद्ध होकर आपका आनन्दवर्द्धक रस इन्द्रदेव को मिले और शक्तियुक्त होकर वायु- देव को प्राप्त हो
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3189)
- **Original**: 1236. पवमान नि तोशसे रयिं सोम श्रवाय्यम्‌ । इन्दो समुद्रमा विश
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3190)
- **Original**: है पवित्र सोमदेव ! आप सराहनीय ऐश्वर्य के लिये दुष्टों को दण्डित करते हैं । हम यज्ञ कलश में आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3191)
- **Original**: 1237. अपघ्नन्पवसे मृथ: क्रतुवित्सोम मत्सर: । नुदस्वादेवयुं जनम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3192)
- **Original**: हे यज्ञकर्म के विशेषज्ञ, आनन्ददायक सोम ! आप शुद्ध होकर अपने दिव्य प्रभाव से नास्तिकों एवं अहित करने वालों को दूर हटाएँ.
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3193)
- **Original**: 1238.अभी नो वाजसातमं रयिमर्ष शतस्पृहम्‌ । इन्दो सहस्रभर्णसं तुविद्युम्मं विभासहम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3194)
- **Original**: हे तेजस्वी सोमदेव ! आप हमें ऐसा श्रेष्ठ ऐश्वर्य प्रदान करें, जो सैकड़ों द्वारा सराहनीय, सहस्रों का पालन- पोषण करने में समर्थ, तेजस्वी और यशवर्द्धक हो
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3195)
- **Original**: 1239. वयं ते अस्य राधसो वसोर्वसो पुरुस्पृहः । नि नेदिष्ठतमा डृष: स्थाम सुम्मे ते अश्विगो
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3196)
- **Original**: हे उत्तम आश्रय देने वाले सोमदेव ! सबके द्वारा सराहनीय, सबको पोषण देने वाले आपकी विभूतियों का हम सानिश्य चाहते हैं । हे सूर्य रश्मियों के साथ रहने वाले सोमदेव ! आपके द्वारा प्रदत्त अन्नादि (पोषक पदार्थों) के उपयोग से हम सुखी हों
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3197)
- **Original**: 1240. परि स्य स्वानों अक्षरदिन्दुरव्ये मदच्युतः । धारा य ऊध्वों अध्वरे भ्राजा न याति गव्ययु:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3198)
- **Original**: सूर्य रश्मियों की कामना करने वाला, स्वाभाविक तेज से युक्त यह श्रेष्ठ सोम, घाररूप में यज्ञार्थ पहुँचता है । याजकों को आनन्दित करने के लिए प्राकृतिक ढंग से परिष्कृत होता है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3199)
- **Original**: 1241. पवस्व सोम महान्त्समुद्र: पिता देवानां विश्वाभि धाम
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3200)
- **Original**: है सोमदेव ! आप अद्वितीय रसयुक्त, सबका पालन करने वाले हैं। आप देवों के सभी स्थानों को अपने दिव्यरस से परिपूर्ण कर दे
- **Translation**: 

---

