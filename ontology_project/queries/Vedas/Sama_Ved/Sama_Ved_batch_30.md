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

### Verse 1 (Sama Ved 0.581)
- **Original**: 210. धानावन्तं करम्भिणमपूपवन्तमुक्थिनम्‌। इन्द्र प्रार्जुषस्व न:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.582)
- **Original**: हे इन्द्रदेव दही और सत्तू से मिश्रित पकाये हुए पुओं की हृवि को मन्त्रोच्चार के साथ हम समर्पित करते हैं, आप प्रात: इसे स्वीकार करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.583)
- **Original**: 2191. अपां फेनेन नमुचे: शिर इन्द्रोदवर्तयः । विश्वा यदजय स्पृथ:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.584)
- **Original**: सभी स्पर्धा करने वालों को पराजित करने के बाद इन्द्रदेव ने नमुचि (रोग) के सिर को जल के झाग (समुद्रफेन ओपषधि) से तोड़ा
- **Translation**: 

---

### Verse 5 (Sama Ved 0.585)
- **Original**: [इस ऋचा में एक सन्दर्थ से रोग निवारक तथा दूसरे सन्दर्भ से चित्तवृत्तियों को जीतने के सूत्र हैं ।] 212. इमे त इन्द्र सोमा: सुतासो ये च सोत्वा: । तेषां मत्स्व प्रभूवसो
- **Translation**: 

---

### Verse 6 (Sama Ved 0.586)
- **Original**: हे महान्‌ ऐश्वर्यशाली इन्द्रदेव ! यह सोमरस आपके लिये शोधित करके रस्वा गया है । आप इस शुद्ध किये हुए सोमरस का पान करके आनन्दित हों
- **Translation**: 

---

### Verse 7 (Sama Ved 0.587)
- **Original**: 213. तुभ्यं सुतासः सोमा: स्तो्ण बर्हिर्विभावसो । स्तोतृभ्य इन्द्र मृडय
- **Translation**: 

---

### Verse 8 (Sama Ved 0.588)
- **Original**: हे ऐश्वर्यवान्‌ इन्रटेव ! आपके लिए यह शोधित सोमरस आसन पर स्थापित है । हे इन्द्रदेव ! इस पवित्र कुश-आसन पर पधार कर आप सोमरस का पान करें तथा साधकों को प्रसन्‍न करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.589)
- **Original**: इति दशमः खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.590)
- **Original**: के के के
- **Translation**: 

---

### Verse 11 (Sama Ved 0.591)
- **Original**: एकादश: खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.592)
- **Original**: 214. आ व इन्द्र कृवि यथा वाजयन्तः शतक्रतुम्‌ । मंहिष्ठं सिद्ध इन्दुभि:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.593)
- **Original**: जिस प्रकार अन की इच्छा वाले खेत में पानी सींचते हैं, उसी तरह हम बल की कामना वाले साधक उन महान इद्धदेव को सोमरस से सोचते हैं.
- **Translation**: 

---

### Verse 14 (Sama Ved 0.594)
- **Original**: 215. अतद्चिदिन्द्र न उपा याहि शतवाजया
- **Translation**: 

---

### Verse 15 (Sama Ved 0.595)
- **Original**: इषा सहत्लवाजया
- **Translation**: 

---

### Verse 16 (Sama Ved 0.596)
- **Original**: हे इन्द्रदेव ! सैकड़ों प्रकार के बल से परिपूर्ण, हज़ारों तरह के पोषक-तत्त्वों एवं रसों सहित, आप अन्तरिक्ष से हमारे यज्ञ में आएँ
- **Translation**: 

---

### Verse 17 (Sama Ved 0.597)
- **Original**: 216. आ बुन्दं वृत्रहा ददे जातः पृच्छाद्विमातरम्‌ । क उग्रा: के ह श्रृण्विरे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.598)
- **Original**: जन्म लेते हो बाण हाथ में लेकर वृत्र को मारने वाले इद्धदेव ने अपनी माता से पूछा, कि अन्य महान्‌ वीर कौन-कौन से प्रसिद्ध हैं ?
- **Translation**: 

---

### Verse 19 (Sama Ved 0.599)
- **Original**: 297, बृबदुक्थं हवामहे सृप्रकरस्नमूतये । साध: कृण्वन्तमवसे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.600)
- **Original**: प्रजा की रक्षा के लिए अपने हाथों को फैलाये, साधनों सहित तत्पर इन्द्रदेव का आवाहन, हम अपने संरक्षण के लिए करते हैं
- **Translation**: 

---

