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

### Verse 1 (Sama Ved 0.3301)
- **Original**: 1287. एष इन्द्राय वायवे स्वर्जित्यरि षिच्यते । पवित्रे दक्षसाधन:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3302)
- **Original**: शक्तिवर्द्धक एवं स्वर्गीय सुख को अपने अधिकार में रखने वाला दिव्य सोम, अंतरिक्ष से छनकर इन्द्रदेव (मेघों) और वायुदेव के निमित्त नीचे आता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3303)
- **Original**: उत्तराचिंके दशमो5ध्याय: 10.5 1288. एष नृभ्रिर्वि नीयते दिवो मूर्धा वृषा सुतः । सोमो वनेषु विश्ववित्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3304)
- **Original**: * बलवान, सबकुछ जानने वाला, द्युलोक (आदि) में प्रशंसित दिव्यरस रूप सोम, बत्रत्विजों द्वारा लकड़ी के बने पात्रों में रखकर (यज्ञस्थल की ओर) ले जाया जाता है.
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3305)
- **Original**: 1289. एघ गव्युरचिक्रदत्पवमानो हिरण्ययु: । इन्दुः सत्राजिदस्तृत:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3306)
- **Original**: चुलोक में प्रतिष्ठित, शक्तिवर्द्धक, रसरूप, विश्वज्ञाता यह सोम वनों (वृक्ष-वनस्पतियों के माध्यम से), मनुष्यों द्वारा प्रयुक्त किया जाता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3307)
- **Original**: 1290. एप शुष्म्यसिष्यददन्तरिक्षे वृषा हरि:। पुनान इन्दुरिन्द्रमा
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3308)
- **Original**: यह प्रकाशित, विजयशील, अपराजित शुद्ध सोम, गौओं एवं स्वर्णादि (खनिजों) को समृद्ध करने के लिए शब्द करता हुआ अवतरित होता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3309)
- **Original**: 1291. एप शुष्प्यदाभ्य: सोम: पुनानो अर्धति। देवावीरघशंसहा
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3310)
- **Original**: देवताओं का रक्षक, पापकर्मियों का संहारक, नष्ट न होने वाला, शोधित हुआ, बलयुक्त, सोमरस कलश में पहुँचता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3311)
- **Original**: इति पंचम: खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3312)
- **Original**: षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3313)
- **Original**: 1292. स सुतः पीतये बृषा सोम: पवित्रे अर्पति
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3314)
- **Original**: विषघ्नन्रक्षांसि देवयु:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3315)
- **Original**: दिव्यगुणों से युक्त, इन्द्रादि देवों के लिए तैयार किया हुआ, अभीष्ट प्रदायक सोम, विकारों को नष्ट करता हुआ शोधन यंत्र से टपकता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3316)
- **Original**: 1293. स पवित्रे विचक्षणो हरिरर्षति धर्णसिः। अभि योनि कनिक्रदत्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3317)
- **Original**: सबका संरक्षक, सबका धारक, दुष्टों का संहारक वह हरिताभ सोम, छन्‍ने से पवित्र होकर, शब्द करते हुए कलश में पहुँचता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3318)
- **Original**: 1294. स वाजी रोचनं दिव: पवमानो वि धावति। रक्षोहा वारमव्ययम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3319)
- **Original**: चुलोक में प्रकाशवान्‌, सामर्थ्यबान्‌, दुष्टों का संहारक, शोधित होता हुआ यह दिव्य सोम अविरल प्रवाहित होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3320)
- **Original**: 1295. स त्रितस्याधि सानवि पवमानो अरोचयत्‌। जामिभि: सूर्य सह
- **Translation**: 

---

