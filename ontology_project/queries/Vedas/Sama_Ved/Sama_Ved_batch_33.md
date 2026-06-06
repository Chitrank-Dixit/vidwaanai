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

### Verse 1 (Sama Ved 0.641)
- **Original**: 2.श्ड सामवेट- संहिता ऋषि, देवता, छन्‍्द-विवरण अर्ँ्रष-शंयु बा्हस्पत्व 115 । श्रुतकक्ष अथवा सुकक्ष आड्रिरस 116, 150, 151, 155, 158, 170, 173, 188, 213 । हर्यत प्रागाथ 117 । श्रुतकक्ष आद्विसस 118, 119, 140, 145, 197, 199, 215, 232 । देवजाम्य इन्द्रमातर ऋषिका 120, 175 । गोषूक्ति-अश्वसूक्ति काण्वायन 121,122, 211 । मेघातिथि काण्व और प्रियमेध आद्रिसस 123, 124, 157, 225, 227 । सुकक्ष और श्रुतकक्ष 125, 126 । भारद्वाज 127 । श्रुतकक्ष 128 । मध्षच्छन्दा वैश्वामित्र 129, 130, 160,164, 166, 180, 189, 198, 205 । व्रिशोक काण्व 131, 133, 134, 136, 161, 204, 207, 216 । वसिष्ठ मैत्रावरुणि 132, 156 । कम्व घौर 135, 185 । वत्स कार्ण्व 137, 143, 152, 182, 186, 187, 193, 206 । कुसीदी काण्व 138, 162, 167 । मेघातिथि काण्व 139, 146, 171, 217, 222, 223, 229, 230 । श्यावाश्व आत्रेय 141
- **Translation**: 

---

### Verse 2 (Sama Ved 0.642)
- **Original**: प्रगाथ काण्व 142, 194 । इरिम्बिठि काण्व 144, 159, 191 । गोतम राहुगण 147, 179, 218 । भरद्वाज बाहस्पत्य 148, 201-202 । बिन्दु अथवा पूतदक्ष आड्रिरस 149, 174 । शुनःशेप आजीगर्ति 153, 163, 183, 214 । शुनःशेप आजीगर्ति अथवा वामदेव 154
- **Translation**: 

---

### Verse 3 (Sama Ved 0.643)
- **Original**: विश्वामित्र गाथिन 165, 195, 210, 226 । प्रियमेध आड्रिरस 168 । वामदेव गौतम 169, 172, 181, 190, 196, 203, 209, 212, 224
- **Translation**: 

---

### Verse 4 (Sama Ved 0.644)
- **Original**: गोधा ऋषिका 176 । दध्यड्ड्ाथर्वण 177 । प्रस्कण्व काण्व 178, 221 । उलो वातायन 18 4
- **Translation**: 

---

### Verse 5 (Sama Ved 0.645)
- **Original**: सत्यधृति वारुणि 192 । गृत्समद शौनक 200 । सुकक्ष आद्रिरस 208 । ब्रह्मतिथि काण्व 219 । विश्वामित्र गाधिन अथवा जम्रदग्नि 220 । दुर्मित्र (अथवा सुमित्र) कौत्स 228 । विश्वामित्र गाधिन अथवा अभीपाद्‌ उदल 231
- **Translation**: 

---

### Verse 6 (Sama Ved 0.646)
- **Original**: देवता - इन्द्र 115-148, 150-170,172-218, 220, 223-232
- **Translation**: 

---

### Verse 7 (Sama Ved 0.647)
- **Original**: मरुद्गण 149, 221
- **Translation**: 

---

### Verse 8 (Sama Ved 0.648)
- **Original**: सदसस्पति 171 । अश्विनीकुमार और मित्रावरूण 219
- **Translation**: 

---

### Verse 9 (Sama Ved 0.649)
- **Original**: विष्णु 222
- **Translation**: 

---

### Verse 10 (Sama Ved 0.650)
- **Original**: छन्द- गायत्री 115- 232 ।
- **Translation**: 

---

### Verse 11 (Sama Ved 0.651)
- **Original**: इति द्वितीयो5 ध्याय:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.652)
- **Original**: । "9 “ता >>डेन्सनपरकथ नरक 9-7
- **Translation**: 

---

### Verse 13 (Sama Ved 0.653)
- **Original**: अथ तृतीयो5 ध्याय:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.654)
- **Original**: त्रयोदश: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.655)
- **Original**: 233. अभि त्वा शूर नोनुमो5दुग्धा इब धेनवः । ईशानमस्य जगत: स्वर्द्शमीशानमिन्द्र तस्थुष:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.656)
- **Original**: हे शूरवीर इन्द्रदेव ! विश्व सृजेता, सर्वज्ञ, आपके दर्शन के लिए हम उसी तरह लालायित हैं, जैसे न दुही हुई गौएँ अपने बछड़े के पास जाने के लिए लालायित रहती हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.657)
- **Original**: 234. त्वामिद्धि हवामहे सातौ वाजस्य कारव: । त्वां वृत्रेष्विन्द्र सत्पर्ति नरस्त्वां काष्ठास्वर्वत:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.658)
- **Original**: है इन्द्रदेव
- **Translation**: 

---

### Verse 19 (Sama Ved 0.659)
- **Original**: हम साधक आपको अन्न वृद्धि के लिए आवाहित करते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.660)
- **Original**: हे इद्धदेव ! विद्वज्जन संघर्ष के समय मदद के लिए आपको हो पुकारते हैं
- **Translation**: 

---

