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

### Verse 1 (Bramha 0.1801)
- **Original**: विन्न नहीं डालते, जिसके यहाँ भगवान्‌ शिवंकी क्रतका पालन करनेवाले दक्ष! मैं तुम्हारे इस
- **Translation**: 

---

### Verse 2 (Bramha 0.1802)
- **Original**: स्तुति होती है। दक्षद्वारा किये हुए इस स्तोत्रका स्तोत्रसे बहुत प्रसन्न हूँ। अधिक कहनेसे कया
- **Translation**: 

---

### Verse 3 (Bramha 0.1803)
- **Original**: पाठ करनेवाला मनुष्य सब पापोंसे मुक्त हो जाता लाभ, तुम्हें मेरा सामीष्य प्राप्त होगा।' यों कहकर
- **Translation**: 

---

### Verse 4 (Bramha 0.1804)
- **Original**: है और मरनेके बाद देवताओंद्वारा पूजित होता है। देवेश्वर महादेवजी अपनी पत्नी और पार्षदोंके साथ
- **Translation**: 

---

### Verse 5 (Bramha 0.1805)
- **Original**: इस परम गोपनीय स्तोत्रका श्रवण करके पापयोनिवाले अमित तेजस्वी दक्षकी दृष्टिसे ओझल हो गये। जो
- **Translation**: 

---

### Verse 6 (Bramha 0.1806)
- **Original**: मनुष्य तथा वैश्य, स्त्री एवं शूद्र भी रुद्रलोक प्रात मनुष्य दक्षद्वारा किये हुए इस स्तोत्नका श्रवण या
- **Translation**: 

---

### Verse 7 (Bramha 0.1807)
- **Original**: करते हैं। जो द्विज प्रत्येक पर्वमें ब्राह्मणोंकों सदा कीर्तन करता है, उसका तनिक भी अमड्जुल नहीं
- **Translation**: 

---

### Verse 8 (Bramha 0.1808)
- **Original**: इस स्तोत्रका श्रवण कराता है, वह निःसंदेह होता। उसे दीर्घ आयुकी प्राप्ति होती है। जैसे
- **Translation**: 

---

### Verse 9 (Bramha 0.1809)
- **Original**: भगवान्‌ शिवके लोकमें जाता है। >>“>न्फय॑स-+>> एकामप्रकक्षेत्र तथा पुरुषोत्तमक्षेत्रकी महिमा लोगहर्षणजी कहते हैं--' महर्षियो ! ब्रह्मजीकी
- **Translation**: 

---

### Verse 10 (Bramha 0.1810)
- **Original**: आया। उन्होंने कहा--'ब्रह्मन्‌! अब आप कही हुईं पवित्र कथा सुनकर उन महर्षियोंको
- **Translation**: 

---

### Verse 11 (Bramha 0.1811)
- **Original**: एकाप्रकक्षेत्रका वर्णन कीजिये।' बड़ी प्रसन्नता हुई। उनके शरीरमें रोमाझ हो. ब्रह्माजी बोले--मुनिवरो! वह क्षेत्र सब पापोंको चतुष्पधेषु रथ्यासु चत्वोपु. सभासु च। हस्त्यश्वरथशालासु जीर्णोेघ्चानालयेपु. च
- **Translation**: 

---

### Verse 12 (Bramha 0.1812)
- **Original**: ये तु पछसु भूतेषु दिशासु विदिशासु च।
- **Translation**: 

---

### Verse 13 (Bramha 0.1813)
- **Original**: इन्दार्कवोर्मध्यगता ये च॑ चन्द्रार्करश्मिषु
- **Translation**: 

---

### Verse 14 (Bramha 0.1814)
- **Original**: रसावलगता ये चये चल तस्मात्परं गता:। नमस्तेभ्यो नमस्तेभ्यो नमस्तेभ्यस्तु सर्वशञः
- **Translation**: 

---

### Verse 15 (Bramha 0.1815)
- **Original**: * सर्वस्त्व॑ सर्वगों देवः सर्वभूतपतिर्भव:। सर्वधभूतान्तरात्मा थे तेन त्वं न निमन्त्रित:
- **Translation**: 

---

### Verse 16 (Bramha 0.1816)
- **Original**: त्वमेव चेज्यसे देव यज्ञैर्विविधदक्षिणै: । त्वमेब कर्ता सर्वस्थ तेन त्वं न निमन्त्रित:
- **Translation**: 

---

### Verse 17 (Bramha 0.1817)
- **Original**: अथवा मायया देब मोहितः सुक्ष्ममा तब। तस्मात्तु कारणाद्वापि त्वं मया ते निमन्त्रित:
- **Translation**: 

---

### Verse 18 (Bramha 0.1818)
- **Original**: प्रसीद॒ मम देवेश त्वमेव शरण मम । त्व॑ गतिस्त्व॑ प्रतिहा च न चान्योउस्तीति मे मति:
- **Translation**: 

---

### Verse 19 (Bramha 0.1819)
- **Original**: [1141] सं0 ख्र0 चु0.-..4 (40। 2--100)
- **Translation**: 

---

### Verse 20 (Bramha 0.1820)
- **Original**: 90 * संक्षिप्त श्रह्मपुराण « हरनेवाला, पवित्र एवं परम दुर्लभ है। मैं उसका। भाँति-भाँतिके वृक्ष, नाना प्रकारके सुन्दर पुष्प संक्षेपसे वर्णन करूँगा, सुनो। एकाम्रक नामसे
- **Translation**: 

---

