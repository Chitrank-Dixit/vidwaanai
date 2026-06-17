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

### Verse 1 (Rig Ved 0.301)
- **Original**: सूक्त-14 ] [ऋषि - मेधातिथि काण्व । देवता-विश्वेदेवा । छन्द-गायत्री
- **Translation**: 

---

### Verse 2 (Rig Ved 0.302)
- **Original**: ] 135, ऐभिर ने दुवो गिरो विश्वेभि: सोमपीतये । देवेभिर्याहि यक्षि च
- **Translation**: 

---

### Verse 3 (Rig Ved 0.303)
- **Original**: है अभ्विदेव ! आप सम्रस्त देवों के साथ इस यज्ञ में सोम पीने के लिए आएँ एवं हमारी परिचर्या और स्तुतियों को ग्रहण करके यज्ञ कार्य सम्प करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.304)
- **Original**: 136. आ त्वा कण्वा अहृषत गृणन्ति विप्र ते धिय:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.305)
- **Original**: देवेभिरग्न आ गहि
- **Translation**: 

---

### Verse 6 (Rig Ved 0.306)
- **Original**: है मेधावी अग्निदिव ! कण्वऋषि आपको बुला रहे हैं, वे आपके कार्यों की प्रशंसा करते हैं । अत: आप देवों के साथ यहाँ पधारें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.307)
- **Original**: कि 137. इन्द्रवायू बृहस्पर्ति मित्राग्नि पूषणं भगम्‌। आदित्यान्‌ मारुतं गणम्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.308)
- **Original**: यज्ञशाला में हम इन्द्र, वायु, बृहस्पति, मित्र, अग्नि, पृषा, भग, आदित्यगण और मरुद्गण आदि देवों का आवाहन करते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.309)
- **Original**: 138. प्र वो प्रियन्त इन्दवों मत्सरा मादयिष्णव:। द्रप्सा मध्वश्चमूषद:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.310)
- **Original**: कूट-पीसकर तैयार किया हुआ, आउनद और हर्ष बढ़ाने वाला यह मधुर सोमरस अग्निदेव के लिए चमसादि पात्रों में भरा हुआ है
- **Translation**: 

---

### Verse 11 (Rig Ved 0.311)
- **Original**: 139. ईब्तते त्वामवस्यव: कण्वासो वृक्तबर्हिष:। हविष्मन्तो अरड्कृत:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.312)
- **Original**: कण्व जग के वंशज अपनी सुरक्षा को कामना से, कुश-आसन बिछ्लकर ह॒विष्यानन व अलंकारों से युक्त होकर अग्निदेव की स्तुति करते हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.313)
- **Original**: 140. घृतपृष्ठा मनोयुजो ये त्वा वहन्ति वह्यः। आ देवान्त्सोमपीतये
- **Translation**: 

---

### Verse 14 (Rig Ved 0.314)
- **Original**: अतिदीप्तिमान्‌ पृष्ठ भाग वाले, मन के संकल्प मात्र से ही रथ में नियोजित हो जाने वाले अश्वों (से खीचे गये रथ) द्वास आप सोमपान के निमित्त देवों को ले आएँ
- **Translation**: 

---

### Verse 15 (Rig Ved 0.315)
- **Original**: 141. तान्‌ यजत्राँ ऋतावृधो 5ग्ने पल्ीवतस्कृधि। मध्व: सुजिल्न पायय
- **Translation**: 

---

### Verse 16 (Rig Ved 0.316)
- **Original**: है अग्निदिव ! आप यज्ञ की समृद्धि एवं शोभा बढ़ाने बाले पूजनीय इद्धादि देव को सपत्नीक इस यज्ञ में बुलाएँ तथा उन्हें मधुर सोमरस का पान कराएँ
- **Translation**: 

---

### Verse 17 (Rig Ved 0.317)
- **Original**: 142. ये यजत्रा य ईड्यास्ते ते पिबन्तु जिल्वया। मधोरग्ने वषट्कृति
- **Translation**: 

---

### Verse 18 (Rig Ved 0.318)
- **Original**: है अभ्निदेव ! यजन किये जाने योग्य और स्तुति किये जाने योग्य जो देवगण हैं, वे यज्ञ में आपकी जिह्ा से आनन्दपूर्वक मधुर सोमरस का पान करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.319)
- **Original**: 143. आकोीं सूर्यस्य रोचनाद्‌ विश्वान्‌ देवाँ उषर्बुध: । विप्रो होतेह वक्षति
- **Translation**: 

---

### Verse 20 (Rig Ved 0.320)
- **Original**: हे मेधावी होतारूप अग्निदेव ! आप प्रातःकाल में जागने वाले विश्वेदेवों को सूर्य-रश्मियों से युक्त करके हमारे पास लाते हैं
- **Translation**: 

---

