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

### Verse 1 (Vishnu Puran 0.9581)
- **Original**: 8 पूर्व त्यक्तैस्सरोउम्भोभिईसा योगं पुनर्ययु: । क्रेशै: कुयोगिनो$शोपैरन्तरायहता इव
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9582)
- **Original**: 9 + अत्तराय नी हैं-- अीपराशरजी बोले--इस प्रकार उन राम और कृष्णके व्रजमें बिहार करते-करते वर्षाकाल जीत गया और प्रफुल्लित कमल्मेंसे युक्त शरद्‌-ऋतु आ गयी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9583)
- **Original**: जैसे गृहस्थ पुरुष पुत्र और क्षेत्र आदियें लूगी हुई ममतासे सन्ताप पाते हैं उसी प्रकार मललियाँ गड़्ढोंकि जलमें अत्यन्त ताप पाने लगीं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9584)
- **Original**: संसारकी असारताकों जानकर जिस प्रकार योगिजन श्ञान्त हो जाते हैं उसी प्रकार मयूरगण मदहोन होकर मौन हो गये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9585)
- **Original**: विज्ञानिगण [ सब प्रकारको ममता छोड़कर ] जैसे घरका स्याग कर देते हैं वैसे ही निर्मल श्वेत मेघोनि अपना जलरूप सर्वस्व छोड़कर आक्प्रद्ममण्डलका परित्याग कर दिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9586)
- **Original**: पदार्थोमें ममता करनेसे जैसे देहधारियोंके हृदय सारहीन हो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9587)
- **Original**: जाते है वैसे हो शरत्कालीन सूर्यके तापसे सरोबर सूख गये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9588)
- **Original**: निर्मल्चित्त पुरुषोकि मन जिस प्रकार ज्ञानद्वारा समता प्राप्त कर छेते हैं उसी प्रकार शरत्कालीन जल्म्रेंको [ स्वच्छताके कारण ] कुमुदोंसे योग्य सम्बन्ध प्राप्त हो गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9589)
- **Original**: जिस प्रकार साधु-कुछूसें चरम-देह-घारी योगी सुशोभित होता है उसो प्रकार तास्का-मण्डलक-मष्डित निर्मल आकाशरमें दूर्णचन्द्र विराजमान हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9590)
- **Original**: जिस प्रकार क्षेत्र और पुत्र आदिमें बढ़ी हुई मंमताकों विवेकोजन शानेः-उानेः त्याग देते हैं वैसे ही जत्ल॒दायोंका जल धीरे-धीरे अपने तटको छोड़ने लगा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9591)
- **Original**: जिस प्रकार अच्तरायों" (चिप्रों) से चिचलित हुए कुयोगियोका “व्याधिस्वानसंशेयप्रमादालस्थासिरतिभ्रान्तिदरनालव्यभुपिकत्वानवस्थितत्वानि चित्तविक्षेपास्ते5त्तराया: । (यो द0 6 । 30)
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9592)
- **Original**: 336 निभृतो5भवदत्वर्थ समुद्र: स्तिमितोदकः । क्रमावाप्तमहायोगो निश्चलात्मा यथा यतिः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9593)
- **Original**: 10 सर्वात्रातिप्रसन्नानि सल्लिनि तथाभवन्‌। ज्ञाते सर्वगते विष्णो मनांसीव सुमेधसाम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9594)
- **Original**: 11 बथूव निर्मल व्योम शरदा ध्वस्ततोयदम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9595)
- **Original**: योगाभिदमस्धक्लेशौध॑ योगिनामिव मानसम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9596)
- **Original**: 12 सुर्याशुजनित ताप॑ निन्‍ये तारापति: शमम्‌ । अहंमानोद्धवं दुःखं विवेकः सुमहानिय
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9597)
- **Original**: 13 नभसो5बदं भुव: पड्ूं कालुष्यं चाम्भसरशरत्‌ इन्द्रियाणीन्द्रियार्थेभ्य: प्रत्याहार इवाहरत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9598)
- **Original**: 54 प्राणायाम इवाम्भोभिस्सरसां कृतपूरकैः । अभ्यस्यतेउनुदिवर्स रेचकाकुभभकादिभिः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9599)
- **Original**: 15 विमछाम्बरनक्षत्रे काले चाभ्यागते व्रजे। दददेन््रमहारम्भायोद्यतांस्तानत्रजौकस:.
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9600)
- **Original**: 16 कृष्णस्तानुत्सुकान्दूद्टा गोपानुत्सवलालसान्‌
- **Translation**: 

---

