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

### Verse 1 (Rig Ved 0.7781)
- **Original**: हे इद्धदेव ! आपने अपनी इन्द्रियों का जो बल तथा पराक्रम प्रदर्शित किया है, उसे कोई भी विनष्ट नहीं कर सकता
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7782)
- **Original**: 3391. वामंवाम त आदुरे देवो ददात्वर्यमा । वाम॑ पूषा वाम॑ भगो बाम॑ देव: करूछती
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7783)
- **Original**: रिपुओं का संहार करने वाले हे इन्द्रदेव ! 'अर्यमा' देवता आपको वह मनोहर ऐश्वर्य प्रदान करें । दन्तहीन “पूषा' तथा “भग' देबता आपको वह रमणीय ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7784)
- **Original**: [ सूक्त -31 ] ( ऋषि - वामदेव गौतम । देवता - इन्द्र । छन्द - गायत्री, 3 पादनिचृत्‌ गायत्री ।
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7785)
- **Original**: 3392. कया नश्वित्र आ भुवदूती सदावृध: सखा
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7786)
- **Original**: कया शचिष्ठया बृता
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7787)
- **Original**: निरन्तर प्रगतिशील हे इद्धदेव ! आप किन-किन तृप्तिकारक पदार्थों के भेंट करने से, किस तरह को पूजा विधि से प्रसन्न होंगे ? आप किन दिव्य शक्तियों सहित हमारे सहयोगी बनेंगे ?
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7788)
- **Original**: 3393. कस्त्वा सत्यो मदानां मंहिष्ठो मत्सदन्‍्धसः
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7789)
- **Original**: दृव्हहा चिदारुजे बसु
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7790)
- **Original**: सत्यनिष्ठों को आनन्द प्रदान करने वालों में सोम सर्वोपरि है; क्योंकि हे इद्धदेव ! यह आपको दुर्धर्ष शत्रुओं के ऐश्वर्य को नष्ट करने की प्रेरणा देता है
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7791)
- **Original**: 3394. अभी षु ण: सखीनामविता जरितृणाम्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7792)
- **Original**: शत भवास्यूतिभि:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7793)
- **Original**: स्तुतियों से प्रसन्न करने वाले अपने मित्रों के रक्षक हे इन्द्रदेव ! हमारी हर प्रकार से रक्षा करने के लिये आप उच्चकोटि की तैयारी से प्रस्तुत हों
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7794)
- **Original**: 3395. अभी न आ ववृत्स्व चक्र न वृत्तमर्वत: । नियुद्धिश्चर्षणीनाम्‌ 4
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7795)
- **Original**: हे इन्द्रदेव ! हम याजकगण आपका अनुगमन करते हैं । आप हम याजकों की प्रार्थनाओं से हर्षित होकर, हमारे सम्मुख गोल पहिए के समान पधारें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7796)
- **Original**: [वृत्ताकार चक्र सतत प्रगतिशीलता का प्रतीक है
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7797)
- **Original**: इन्द्र का अनुगयन करते हुए हप सतत प्रगनिश्ञील रहें, यह भाव है। ]
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7798)
- **Original**: 52 ऋग्वेद संहिता भाग - 2 3396, प्रवता हि क्रतूनामा हा पदेव गच्छसि । अभक्षि सूर्ये सचा
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7799)
- **Original**: हे इन्धदेव ! आप यज्ञ मण्डप में अपने स्थान को ज्ञात करके पधारते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7800)
- **Original**: सूर्यदेव के साथ हम आपकी उपासना करते हैं
- **Translation**: 

---

