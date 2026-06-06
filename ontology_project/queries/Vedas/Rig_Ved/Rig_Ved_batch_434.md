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

### Verse 1 (Rig Ved 0.8661)
- **Original**: [ सूक्त - 14 ] [ ऋषि - सुतम्भर आत्रिय
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8662)
- **Original**: देवता - अग्नि। छन्द - गायत्री
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8663)
- **Original**: ] 3759, अग्नि स्तोमेन बोधय समिधानो अपर्त्यम्‌ । हव्या देवेषु नो दधत्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8664)
- **Original**: है मनुष्यो ! इन अविनाशों अग्निदेव को उत्तम स्तोत्रों से प्रवृद्ध करें । भली प्रकार प्रज्वलित होने पर वे हमारे हव्य पदार्थों को देवों तक पहुंचाएँ
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8665)
- **Original**: 3760. तमध्वरेष्वीछते देव॑ मर्ता अमर्त्यम्‌। यजिष्ठं मानुषे जने
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8666)
- **Original**: साधकगण यज्ञों में दिव्य गुण-सम्पन्न, अमर और मनुष्यों के मध्य में परम पुजनीय उन अग्निदेव को उत्तम स्तुतियाँ करते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8667)
- **Original**: 3761. त॑ हि शश्वन्त ईव्ते ख्रुचा देव॑ घृतश्चुता । अर्ग्नि ह॒व्याय वोछहवे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8668)
- **Original**: अनेकों स्तोतागण यज्ञ में खुकू के साथ घृत- धारा यहाते हुए देवों के लिए हवियाँ वहन करने के उद्देश्य से दिव्य गुण-सम्पन्न अभिदेव का स्तवन करते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8669)
- **Original**: 3762. अग्निर्जातो अरोचत घ्नन्दस्यूज्ज्योतिषा तम:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8670)
- **Original**: अविन्दद्गा अप: स्व:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8671)
- **Original**: अरणि-मंथन से उत्पन्न अग्निदेव अपने तेज से अन्धकार और राक्षसों को बिनष्ट करते हुए प्रकाशित होते है। इन अग्निदेव से ही किरण, जल और सूर्यदेव प्रकट होते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8672)
- **Original**: 3763. अग्निमीन्ठेन्यं कविं घृतपृष्ठं सपर्यत
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8673)
- **Original**: वेतु मे शुणवद्धवम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8674)
- **Original**: हे मनुष्यों ! आप स्तुति किये जाने योग्य और ज्ञानी अग्निदेव का पूजन करें । वे घृत की आहुतियों से प्रदीप्त ज्वालाओं वाले हैं । वे अग्निदेव हमारे आवाहन को सुनें और जानें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8675)
- **Original**: 3764. अग्नि घृतेन वावृथु: स्तोमेभिर्विश्वचचर्षणिम्‌ । स्वाधीभिर्वचस्युभि:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8676)
- **Original**: ऋषत्विग्गण स्तोत्रों के साथ घृत की आहूतियों द्वारा, स्तुति की कामना वाले ध्यानगम्य देवों के साथ सर्वद्रष्ट अभ्निदेव को प्रवृद्ध करते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8677)
- **Original**: [ सूक्त - 15 ] [ ऋषि - धरुण आड्रिरस । देवता - अग्नि । छन्द - त्रिष्ठ॒प्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8678)
- **Original**: ] 3765. प्र वेधसे कबये वेद्याय गिरं भरे यशसे पूर्व्याय। घृतप्रसत्तो असुरः सुशेवों रायो धर्ता धरुणो वस्वो अग्नि:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8679)
- **Original**: ये अग्निदेव हविरूप घृत से प्रसन्न होते हैं। ये अतिशय बलशाली, अत्यन्त सुखकारी, धनों के अधीश्वर हव्यवाहक, गृहप्रदाता, विधाता, क्रान्तदर्शी, यशस्वी, श्रेष्ठ, जानने योग्य और मेधावी हैं । ऐसे अग्निदेव के लिए हम स्तुतियों की रचना करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8680)
- **Original**: 3766, ऋतेन ऋ जं धरुणं धारयन्त यज्ञस्थ शाके परमे व्योमन्‌। दिवो धर्मन्थरुणे सेदुषों नृज्जातैरजाताँ अभि ये ननक्षु:
- **Translation**: 

---

