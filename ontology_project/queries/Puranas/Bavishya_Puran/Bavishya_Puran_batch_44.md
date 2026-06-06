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

### Verse 1 (Bavishya Puran 0.861)
- **Original**: दैल्यपत्यों महाभागा दैत्यातों कन्यका; झरुभा:कुमाशा ये च दैत्यानो शान्ति कुर्वश्तु ते सदा
- **Translation**: 

---

### Verse 2 (Bavishya Puran 0.862)
- **Original**: आरक्तेन.. शर्परैण रक्तात्तायतस्फेचना: । महाभागा: कृताटोपा: शज्झाद्याः कृतलक्षणा:
- **Translation**: 

---

### Verse 3 (Bavishya Puran 0.863)
- **Original**: आनत्तो नागगणजेद्र आदित्याराधने. रत-
- **Translation**: 

---

### Verse 4 (Bavishya Puran 0.864)
- **Original**: महाप्रापविषं हत्वा शान्तिझासु करोतु ते
- **Translation**: 

---

### Verse 5 (Bavishya Puran 0.865)
- **Original**: अतिपीतीन.. देहेन. विस्फुरद्धोगसन्पदा
- **Translation**: 

---

### Verse 6 (Bavishya Puran 0.866)
- **Original**: तेजसा. चातिदीसय. कृतस्वस्तिकल्प्रज्छन:
- **Translation**: 

---

### Verse 7 (Bavishya Puran 0.867)
- **Original**: नागरट्‌ तक्षक: श्रीमान्‌ ताशक्ेट्या समा्वितः ।करोतु ते महाझान्ति. सर्वदोषसिपापहास्‌
- **Translation**: 

---

### Verse 8 (Bavishya Puran 0.868)
- **Original**: अतिकृष्शेन. वर्जेन.. स्फुरिताधिकपाततक । कप्टरेस्तरात्रयोपेतो घोषद॑श्टायुधोद्यत:
- **Translation**: 

---

### Verse 9 (Bavishya Puran 0.869)
- **Original**: कर्कोटको.. महानागो.. विषदर्पबल्प्र्वित: । विषज्ञस्माप्रिसंताप॑ हत्था शान्ति करोंतु ते
- **Translation**: 

---

### Verse 10 (Bavishya Puran 0.870)
- **Original**: पद्चर्ज: पद्चकाक्ति:. फुल्लपदायतेक्षण: । ख्यात: पद्मो
- **Translation**: 

---

### Verse 11 (Bavishya Puran 0.871)
- **Original**: महानागो नित्य भास्करपूजक:
- **Translation**: 

---

### Verse 12 (Bavishya Puran 0.872)
- **Original**: स॒ते जात्ति शुभ शीघ्रमचले सप्प्रबच्छतु। क्यामेतर देहभारेण.. औपत्कमलल्मेचन:
- **Translation**: 

---

### Verse 13 (Bavishya Puran 0.873)
- **Original**: विषदर्पबलोन्मत्तो. औवायों. रेखयान्यित-
- **Translation**: 

---

### Verse 14 (Bavishya Puran 0.874)
- **Original**: ऋछलुपालत्रिया. दीज्.. सूर्यपादाब्जपूजक:
- **Translation**: 

---

### Verse 15 (Bavishya Puran 0.875)
- **Original**: महानिप॑ गरबेट्ट हत्वा ज्न्ति करोंतु ते। अशिगौरेण देहेन ्द्रार्धकृतभेखर:
- **Translation**: 

---

### Verse 16 (Bavishya Puran 0.876)
- **Original**: दीपभागे कृताटोपशुधलश्षणरक्षितः
- **Translation**: 

---

### Verse 17 (Bavishya Puran 0.877)
- **Original**: कुलिकोों नाथ नागेन्ड्रो नित्व॑सूर्यपरायण-
- **Translation**: 

---

### Verse 18 (Bavishya Puran 0.878)
- **Original**: अपहस्यथ विष घोरे अन्तरिक्षी च थे ताणा ये नागा: स्वर्गसंस्थिता:
- **Translation**: 

---

### Verse 19 (Bavishya Puran 0.879)
- **Original**: गिरिकन्टस्दरॉंषु ये पाताले ये ख्यिता नागाः सर्वे बत्र समाहिताः
- **Translation**: 

---

### Verse 20 (Bavishya Puran 0.880)
- **Original**: सूर्यणादार्थनासक्ता जाफियो ताथकत्याक तथा नागकुमारफा:
- **Translation**: 

---

