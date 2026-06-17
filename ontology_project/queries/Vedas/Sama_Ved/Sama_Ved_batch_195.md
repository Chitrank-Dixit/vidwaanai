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

### Verse 1 (Sama Ved 0.3881)
- **Original**: पंच जनों (समाज के पाँचों वर्गों ) का हित चाहने वाले और सब कुछ देखने वाले शुद्ध अग्निदेव जिन्हें ऋत्विजों ने यज्ञ के लिए प्रथम स्थापित किया है, उन समर्थ अग्निदेव की हम स्तुति करते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3882)
- **Original**: 1520. अग्ने पवस्व स्वपा अस्मे धर्च: सुवीर्यम्‌। दधद्रयिं मयि पोषम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3883)
- **Original**: है अग्निदेव ! आप उत्तम कर्म की प्रेरणा देने वाले हैं । आप हमें तेज तथा पराक्रम से युक्त शक्ति प्रदान करें, हमें ऐश्वर्य और पोषक तत्वों से सम्पन्न बनाएँ
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3884)
- **Original**: उत्तराचिंकि चतुर्दशो ध्यायः 14.5 1521.अग्ने पावक रोचिषा मन्द्रया देव जिह्यया। आ देवान्वक्षि यक्षि च
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3885)
- **Original**: हे पवित्रता प्रदान करने वाले अग्निदेव ! देवताओं को प्रसन्न करने वाली ज्वालारूपी जिद्डा द्वारा, देवताओं को आमचिित करके आप उनके निमित्त यज्ञ सम्पन्न करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3886)
- **Original**: 1522.त॑ त्वा घृतस्नवीमहे चित्रभानो स्वर्दृशम्‌। देवाँ आ बीतये वह
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3887)
- **Original**: हे घृत से उत्पन्न होने वाले अद्भुत तेजस्वी अग्निदिव ! सबको देखने वाले आपकी हम प्रार्थना करते हैं । हवि सेवनार्थे देवों को आप यहाँ बुलाएँ
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3888)
- **Original**: 1523.वीतिहोत्र॑ त्वा कवे द्युमन्‍्तं समिधीमहि। अग्ने बृहन्तमध्वरे
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3889)
- **Original**: हे ज्ञानी अम्निदेव ! यज्ञानुरागी, तेजस्वी तथा महान्‌ आपको हम यज्ञ में प्रज्वलित करते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3890)
- **Original**: ड़ति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3891)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3892)
- **Original**: 1524.अवा नो अग्न ऊतिभिर्गायत्रस्य प्रभर्मणि। विश्वासु धीषु वन्द्य
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3893)
- **Original**: हे अग्निदेव ! आप सभी यज्ञों में वन्दनीय हैं। गायत्री छनद वाले सामगान से स्तुति करने पर प्रसन्न हुए आप अपने संरक्षणरूपी साधनों से हमारी रक्षा करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3894)
- **Original**: 1525.आ नो अग्ने रयिं भर सत्रासाहं वरेण्यम्‌। विश्वास पृत्सु दुष्टरम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3895)
- **Original**: हे अग्निदेव ! दरिद्रता को नष्ट करने वाले, शत्रुओं को पराजित करने वाले, वरण करने योग्य, श्रेष्ठ ऐश्वर्य आप हमें प्रदान करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3896)
- **Original**: 1526. आ नो अमने सुचेतुना रयिं विश्वायुपोषसम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3897)
- **Original**: मार्डीक॑ श्रेष्ठ जीवसे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3898)
- **Original**: हे अग्निदेव ! आप उत्तम ज्ञान से युक्त, जीवन भर पोषक सामर्थ्य प्रदान करने वाला, सुखदायक घन हमारे दीर्घ जीवन के लिए हमें प्रदान करें.
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3899)
- **Original**: जि 1527.अग्नि हिन्वन्तु नो धिय: सप्तिमाशुमिवाजिषु । तेन जेष्म धनंधनम्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3900)
- **Original**: हमारी बुद्धियाँ अग्नि (प्रतिभा) को उसी प्रकार प्रेरणा दें, जिस प्रकार युद्ध में शीघ्र चलने वाले घोड़े को प्रेरित किया जाता है । जीवन-संप्राम में हम सभी ऐश्वर्यों के विजेता हों
- **Translation**: 

---

