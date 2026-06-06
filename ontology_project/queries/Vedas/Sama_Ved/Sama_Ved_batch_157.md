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

### Verse 1 (Sama Ved 0.3121)
- **Original**: हे परम आनन्ददायों सोमदेव ! इन्द्रदेव को तृप्ति प्रदान करने के लिए, आप शोधन यंत्र में से निर्मलधारा के रूप में निकलें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3122)
- **Original**: 2209. स पवस्व मदिन्तम गोभिरञ्ञानो अक्तुभि: । एन्रस्य जठरं विश
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3123)
- **Original**: है आनन्दप्रदायक सोमदेव ! गाय के पुष्टिकारक दुग्धादि के मिश्रण में छणमकर आप इन्द्रदेव के उदर में प्रवेश करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3124)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3125)
- **Original**: के के के
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3126)
- **Original**: पञ्ञम: खण्ड;
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3127)
- **Original**: 1210. अया वीती परि स््रव यस्त इन्दो मदेष्वा । अवाहन्नवतीर्नव
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3128)
- **Original**: हे सोमदेव ! इन्द्रदेव के सेवन के लिए आप शुद्ध हों । आपका दिव्य रस जीवन संग्राम में बाधाओं को नष्ट करने में समर्थ है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3129)
- **Original**: 12191. पुर: सद्य इत्थाधिये दिवोदासाय शंबरम्‌ । अध त्यं तुर्वशं यदुम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3130)
- **Original**: सोमरस पीकर इन्द्रदेव ने यज्ञ करने वाले दिवोदास (दिव्य गुणों के लिए समर्पित व्यक्ति) के लिए शम्बरासुर (अकल्याण करने वाले) को, तुर्वश (क्रोध) को और यदु (नियंत्रण विहीन) को मारा
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3131)
- **Original**: उत्तराच्कि नवमो5ध्याय: 9.5 1212. परि णो अश्वमश्वविदगोमदिन्दो हिरण्यवत्‌ । क्षरा सहस्निणीरिष:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3132)
- **Original**: है सोमदेव ! आप हमें गौ, अश्व, सुवर्ण आदि ऐश्वर्य और अभीष्ट पोषक अन प्रदान करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3133)
- **Original**: 1213. अपध्नन्पथते मृधो5प सोमो अराव्ण: । गच्छन्निद्धस्थ निष्कृतम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3134)
- **Original**: यह सोमरस विकारों का नाश कर, अनुदारों को हटाकर, इन्द्रदेव के स्थान तक पहुँचने के लिए पवित्र होता है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3135)
- **Original**: 1214. महो नो राय आ भर पवमान जही मृथः । रास्वेन्दों वीरवद्यशः
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3136)
- **Original**: हे पवित्रकर्मा सोमदेव ! आप हमें बहुत साधन, पुत्रादि तथा यश प्रोप्त कराएँ और शत्रुओं का हनन करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3137)
- **Original**: 1215. न त्वा शतं च न छ्ुुतो राधो दित्सन्तमा मिनन्‌ । यत्पुनानो मखस्यसे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3138)
- **Original**: है पवित्र सोमदेव ! यज्ञ करने वाले को जब आप ऐश्वर्य देने कौ इच्छा करते हैं, तो आपको सँकड़ों शत्रु भी रोक नहीं सकते
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3139)
- **Original**: 1216. अया पवस्व धारया यया सूर्यमरोचय: । हिन्वानो मानुषीर॒प:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3140)
- **Original**: हे सोमदेव ! मनुष्यों के लिए हितकारी, जल की वर्षा करने बाले, आप सूर्यदेव को प्रकाशित करने वाली क्षमता से स्वयं भी पवित्र हों
- **Translation**: 

---

