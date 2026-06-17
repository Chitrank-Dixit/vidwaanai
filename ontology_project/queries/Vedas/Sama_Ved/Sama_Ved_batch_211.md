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

### Verse 1 (Sama Ved 0.4201)
- **Original**: हे दर्शन करने योग्य सर्वज्ञ इन्द्रदेव
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4202)
- **Original**: ! आप हरांर लिए पर्याप्त घन लाकर दें । शत्रुओं के पास से भी जीत कर लाये धन को हमारे संरक्षण के निमित प्रयोग करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4203)
- **Original**: 1645. तव त्यदिन्द्रियं बृहत्तव दक्षमुत क्रतुम्‌। बच्र॑ शिशाति धिषणा वरेण्यम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4204)
- **Original**: हे इन्द्रदेव ! आण्की तीक्ष्ण बुद्धि, आपके शौर्य, सामर्थ्य, कुशलता, पराक्रम और श्रेष्ठ वज़ को तेजस्वी बनाती है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4205)
- **Original**: उत्तराचिके सप्तदशोडध्याय- 17.5 1646. तव द्यौरित्ध पौस्यं पृथिवी वर्धति श्रवः । त्वामापः पर्वतासश्न हिन्विरे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4206)
- **Original**: हे इन्द्रदेव ! अन्तरिक्ष से आपकी शक्ति-सामर्थ्य का और प्रथ्वी से आपके यशस्वी स्वरूप का विस्तार होता है । जलप्रवाह और पर्वत आपके पास आपको अपना अधिपति मानकर पहुँचते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4207)
- **Original**: 1647. त्वां विष्णुर्बृहन्क्षयो मित्रों गृणाति वरुण: । त्वां शद्धों मदत्यनु मारुतम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4208)
- **Original**: हे इद्धदेव ! महान्‌ आश्रयदाता मानकर के विष्णु, मित्र और वरुणादि देवता आपका स्तुतिगान कंरते हैं । मरुदगणों के बल से आप हर्षित होते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4209)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4210)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4211)
- **Original**: 1648. नमस्ते अग्न ओजसे गृणन्ति देव कृष्टय: । अमैरमित्रमर्टय
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4212)
- **Original**: है अग्निदेव ! बल के निमित्त साधक आपको नमन कर के स्तुतिगान करते हैं । अपने पराक्रम से आप शत्रुओं का संहार करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4213)
- **Original**: 1649. कुवित्सु नो गविष्टये5ग्ने संवेषिषो रयिम्‌ । उरुकृदुरु णस्कृधि
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4214)
- **Original**: है अग्निदेव ! गौओं की इच्छा करने वाले आप हमारे लिए प्रचुर धन प्रदान करें । महानता के पोषक आप से हम महानता की कामना करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4215)
- **Original**: 1650. मा नो अग्ने महाधने परा वर्ग्भारभृद्यथा । संवर्ग सं रयि जय
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4216)
- **Original**: है अग्निदेव ! युद्ध में आप हम से विपरीत न हों, जिस प्रकार भारवाहक भार को उठा लाता है , उसी प्रकार शत्रु से जीती हुई, संग्रहित सम्पदा को लाकर हमें प्रदान करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4217)
- **Original**: 1651. समस्य मन्यवे विशो विश्वा नमन्त कृष्टय: । समुद्रायेव सिन्धव:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4218)
- **Original**: सभी प्रजाजन इन्देव के क्रोध के समक्ष वैसे ही झुकते हैं, जैसे समुद्र कौ ओर नदियाँ स्वयं झुकती चली जाती हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4219)
- **Original**: 1652. वि चिद्बृत्रस्य दोधत: शिरो बिभेद वृष्णिना । वच्रेण शतपर्वणा
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4220)
- **Original**: संसार को भयभीत करने वाले (कम्पित करने वाले) वृत्रासुर के शीश को शक्तिसम्पन्न इन्द्रदेव ने अपने तीक्ष्ण प्रहार वाले वज़ से अलग कर दिया (काट डाला)
- **Translation**: 

---

