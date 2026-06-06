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

### Verse 1 (Sama Ved 0.3281)
- **Original**: ) सोम शोधन -- रस परिपाक]
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3282)
- **Original**: इति तृतीयः खण्ड:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3283)
- **Original**: के के के
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3284)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3285)
- **Original**: 1280. एष बाजी हितो नृभ्रिर्विश्वविन्मनसस्पतिः । अव्यं वार॑ वि धावति
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3286)
- **Original**: सर्वज्ञाता, मन का अधिपति, हितकारी एवं बलशाली दिव्य सोम, यज्ञकर्तताओं द्वारा शुद्ध होकर यज्ञ कलश में प्रतिष्ठित होता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3287)
- **Original**: 1281. एष पवित्रे अक्षरत्सोमो देवेभ्य: सुतः । विश्वा धामान्याविशन्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3288)
- **Original**: देवों के निमित्त निष्पन हुआ यह सोम, शुद्ध होकर देवों के शरोरों में संव्याप्त हो जाता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3289)
- **Original**: 1282. एप देव: शुभायते5धि योनावमर्त्य: । वृत्रहा देववीतम:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3290)
- **Original**: देवताओं को अतिप्रिय, देवत्व को बढ़ाने वाला, अविनाशी, शत्रुसंहारक सोम, यज्ञ कलश में अत्यधिक शोभायमान होता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3291)
- **Original**: ह 1283. एप वृषा कनिक्रदद्दशभिर्जामिभिर्यत: । अभि द्रोणानि धावति
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3292)
- **Original**: दसों अँगुलियों द्वारा निचोड़ा गया, बलवर्द्धक यह सोमरस शब्दनाद करता हुआ, वेगपूर्वक कलश में पहुँचता है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3293)
- **Original**: 1284. एष सूर्यमरोचयत्पवमानों अधि द्यवि । पवित्रे मत्सरो मद:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3294)
- **Original**: पवित्र करने बाले द्युलोक में यह आनन्दित करने बाला शुद्ध सोम सूर्यदेव को प्रकाशित करता है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3295)
- **Original**: 1285. एप सूर्येण हासते संवसानो विवस्वता । पतिर्वाचों अदाभ्य:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3296)
- **Original**: किसी के बन्धन में न रहने वाला, स्तुत्य यह सोम तेजस्वी सूर्यदेव द्वारा जलादि'पंचतत्तवों में मिलाये जाने के लिए छोड़ा जाता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3297)
- **Original**: इति चतुर्थ:खण्डः
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3298)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3299)
- **Original**: 1286. एब कविरभिष्ट्तः पवित्रे अधि तोशते । पुनानो घ्नन्नप द्विष:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3300)
- **Original**: कवियों-ज्ञानियों के द्वारा स्तुत्य, शोधित, विकार नाशक यह सोमरस तृप्ति प्रदान करने वाला है
- **Translation**: 

---

