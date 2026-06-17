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

### Verse 1 (Vaivtpuran 70.18944)
- **Original**: सो5वतीर्णों हि भगवान्‌ भारावतरणाय च । गोपालबालवेषश्ष॒ मायेशों मायया प्रभु:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 70.18945)
- **Original**: सर्यहन्तिच सर्वेशो रक्षिता तस्य कः पुमान्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 70.18946)
- **Original**: स यं रक्षति सर्वात्मा तस्थ हन्ता न को5पि च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 70.18947)
- **Original**: डति औब्रह्मवैवर्ते कंसबान्धवजनकृता श्रीकृप्णस्तुति: सम्पूर्णा। ( श्रीकृष्णजन्मखण्ड 72
- **Translation**: 

---

### Verse 5 (Vaivtpuran 70.18948)
- **Original**: 99--105)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 75.9113)
- **Original**: + श्रीकृष्णजन्मखण्ड * ड15 ऋषऋऋ# ######&# कक ##############$#$$ऊऋऊऊ$%ऊ$%##############ऋऊऋऊ 55% %# मुने! उन त्रिदशेश्वरोंने खड़े-खड़े पुनः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 75.9114)
- **Original**: इस लोकमें भी वह भगवान्‌ विष्णुके समान ही स्तवन किया। वे सब-के-सब वहाँ भगवान्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 75.9115)
- **Original**: विख्यात एवं पूजित होता है; इसमें संशय नहीं श्रीकृष्णके तेजसे व्याप्त हो रहे थे। धर्म, शिव
- **Translation**: 

---

### Verse 9 (Vaivtpuran 75.9116)
- **Original**: है। निश्चय ही उसे वाक्सिद्धि और मन्त्रसिद्धि और ब्रह्माजीके द्वारा किये गये इस स्तवराजकों
- **Translation**: 

---

### Verse 10 (Vaivtpuran 75.9117)
- **Original**: भी सुलभ हो जाती है। वह सम्पूर्ण सौभाग्य जो प्रतिदिन श्रीहरिके पूजाकालमें भक्तिपूर्वक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 75.9118)
- **Original**: और आरोग्य लाभ करता है। उसके यशसे सारा पढ़ता है, वह उनकी अत्यन्त दुर्लभ और दृढ़
- **Translation**: 

---

### Verse 12 (Vaivtpuran 75.9119)
- **Original**: जगत्‌ पूर्ण हो जाता है। वह इस लोकमें पुत्र, भक्ति प्राप्त कर लेता है। देवता, असुर और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 75.9120)
- **Original**: विद्या, कविता, स्थिर लक्ष्मी, साध्वी सुशीला मुनीद्रोंको श्रीहरिका दास्य दुर्लभ है; परंतु इस
- **Translation**: 

---

### Verse 14 (Vaivtpuran 75.9121)
- **Original**: पतित्रता पत्नी, सुस्थिर संतान तथा चिरकालस्थायिनी स्तोत्रका पाठ करनेबाला उसे पा लेता है। साथ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 75.9122)
- **Original**: कीर्ति प्राप्त कर लेता है और अन्‍्तमें उसे ही अणिमा आदि सिद्धियों तथा सालोक्य आदि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 75.9123)
- **Original**: श्रीकृष्णके निकट स्थान प्राप्त होता है। चार प्रकारकी मुक्तियोंकों भी प्राप्त कर लेता है। (अध्याय 5) #+0-+--प्ययेट+ज+म सर स्थित सर्वत्र. निर्लिप्तमात्मरूप॑ परात्यरम्‌ । निरीहमवितक्य॑च तेजोरूप नमाम्यहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 75.9124)
- **Original**: सगुणं निर्गुणं ब्रह्म ज्योतीरूप सनातनम्‌ । साकार॑ च निराकार॑ तेजोरूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 75.9125)
- **Original**: त्वमनिर्वचनीय॑ च व्यक्तमव्यक्तपेककम्‌। स्वेच्छामयं सर्वरूप॑ तेजोरूप॑नमाम्यहम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 75.9126)
- **Original**: गुणत्रयविभागाय रूपत्रयधर॑ परम्‌। कलया ते सुरा: सर्वे कि जानन्ति श्रुते: परम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 75.9127)
- **Original**: सर्वरूप॑ सर्ववीजमबीजकम्‌ । सर्वान्तकमनन्त॑ च तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

