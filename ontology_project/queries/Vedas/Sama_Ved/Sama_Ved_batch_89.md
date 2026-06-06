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

### Verse 1 (Sama Ved 0.1761)
- **Original**: के कं के
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1762)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1763)
- **Original**: 680.अभि त्वा शूर नोनुमो5दुग्धा इब धेनव: । ईशानमस्य जगत: स्वर्द्शमीशानमिन्द्र तस्थुष:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1764)
- **Original**: 1 । हे शूरवीर इन्द्रदेव ! विश्व सृजेता, सर्वज्ञ आपके दर्शन के लिए हम उसी तरह लालाबित हैं, जैसे न दृहो हुई गौएँ अपने बछड़े के पास जाने के लिए लालायित रहती हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1765)
- **Original**: 6891.न त्वावाँ अन्यो दिव्यो न पार्थिवो न जातो न जनिष्यते । अश्वायन्तो मघवन्निन्द्र वाजिनो गव्यन्तस्त्वा हवामहे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1766)
- **Original**: है ऐश्वर्यवान्‌ इद्ध ! आपके समान इस पृथ्वीलोक या दिव्यलोक में, न कोई है, न कभी हुआ है और न के ड्ोगा । हे इन्द्रदेव ! अश्य, गौ तथा धन-धान्य की कामना वाले हम आपकी प्रार्थना करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1767)
- **Original**: 682.कया नश्चित्र आ भुवदूती सदावृध: सखा । कया शचिष्ठया वृता
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1768)
- **Original**: निरन्तर प्रगतिशील वीर इन्द्र ! किन-किन तृप्तिकारक पदार्थों कौ भेंट से, किस प्रकार की पूजा पद्धति से प्रसन होकर, आप किन शक्तियों सहित हमारे सहयोगी बनेंगे ?
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1769)
- **Original**: 683.कस्त्वा सत्यो मदानां मंहिष्ठो मत्सदनन्‍्धसः
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1770)
- **Original**: दृढा चिदारुजे वसु
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1771)
- **Original**: 4 5 सत्यनिष्ठों को आनन्द प्रदाद करने वालों में सोम स्वोपरि है; क्योंकि हे इद्धदेव ! यह आपको दुर्थर्ष शत्रुओं के ऐश्वर्य को नष्ट करने की प्रेरणा देता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1772)
- **Original**: 684 .अभी घु णग: सखीनामविता जरितृणाम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1773)
- **Original**: शतं भवास्यूतये
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1774)
- **Original**: स्तुतियों से प्रसन्‍न करने वाले, अपने मित्रों के रक्षक हे इन्द्रदेव ! हमारी हर प्रकार से रक्षा करने के लिए आप उच्चकोटि की तैयारी से प्रस्तुत हों
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1775)
- **Original**: 685.तं वो दस्ममृतीषहं वसोर्मन्दानमन्धस: । अभि वत्सं न स्वसरेषु धेनव इन्द्र गीर्भिनवामहे
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1776)
- **Original**: गौएँ जिस प्रकार गौशाला में अपने बढ़ड़ों के पास जाने के लिए लालायित रहती हैं, उसी प्रकार हे ऋत्विजो ! शत्रुओं से रक्षा करने वाले, तेजस्वी, सोमरस से तृप्त होने वाले इन्द्र की हम स्तुति करते है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1777)
- **Original**: उत्तराथिंके तृतीयो5ध्याय: हब 686.च्युक्षं सुदानुं तविषीभिरावृतं गिरि न पुरुभोजसम्‌ । क्षुमन्तं वाजं शतिनं सहस्तरिणं मक्षू गोमन्तमीमहे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1778)
- **Original**: देवलोक बासी, उत्तम दानदाता, सामर्थ्यवान्‌ इद्धदेव से सब प्रकार के ऐश्वर्य, मैकड़ों गीओ तथा पोषक अन की हम कामत्रा करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1779)
- **Original**: 687.तरोभियों विदद्वसुमिन्द्रं सबाध ऊतये । बृहदगायन्त: सुतसोमे अध्वरे हुवे भरं न कारिणम्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1780)
- **Original**: जैसे अभिभावक को बालक पुकारता है, चैसे हो हम अपने हितकारी इद्धदेव को सहायता के लिये बुलाते हैं । है ऋत्विजो ! अपनी रक्षा के लिए सोमयज्ञ में ऐश्वर्य देने वाले वेंगवान्‌ अश्यों से युक्त इद्धदेव का आराधना करो
- **Translation**: 

---

