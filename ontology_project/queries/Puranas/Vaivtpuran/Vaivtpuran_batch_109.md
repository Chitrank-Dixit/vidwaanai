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

### Verse 1 (Vaivtpuran 7.18493)
- **Original**: दिकक्‍पालानां महेन्द्रश्तम त॑ नमामि परें बरम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.18494)
- **Original**: अक्षराणामकारों यस्तं प्रधानं नमाप्यहम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.18495)
- **Original**: इन्द्रियाणां मनो यो हि सर्वश्रेष्ठ नमाम्यहम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.18496)
- **Original**: तेजसां ब्रह्मतेजश्ष॒वरेण्यं॑ त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.18497)
- **Original**: काल: कलयतां यो हि तं॑ नमामि विलक्षणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.18498)
- **Original**: मित्रेषु जन्मदाता अस्त॑ सार॑ प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.18499)
- **Original**: पतिब्रता च पलीनां नमस्ये त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.18500)
- **Original**: शालग्रामश्च यन्त्राणां त॑ विशिष्ट नमाम्यहम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.18501)
- **Original**: धर्माणां सत्यरूपों यो विशिष्ट त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.18502)
- **Original**: शब्दरूपश्च॒गगने त॑ प्रणम्यं नमाम्यहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.18503)
- **Original**: गन्धर्वाणां चित्ररथस्त॑ गरिष्ठं नमास्यहम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.18504)
- **Original**: पुण्यदानां च यथः स्तोत्र त॑ नमामि शुभधप्रदम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.18574)
- **Original**: » भ्रीकृष्णास्तोत्राणि + <915 कक कक डक ऋ%ऋ क्ऋ््छ %ऋक्् ऋकऋऋ ऋ ऋऋ%ऋ $%%%%ऊ$%ऋ$%ऊऋऊऋ%$%%$%$%ऊ%%%%$%%ऊऋक% सुभगो5दुर्भगो याग्मी दुराराध्यो दुरत्यय:। वेदहेतुश वेदाक्ष वेदाड़ों वेदविद्‌ विभु:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.18575)
- **Original**: इत्येयमुक्या देवाश्च॒ प्रणेमुश्च॒ मुहुर्मुहुः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.18576)
- **Original**: हर्षाशुलोचना: सर्वे बवृषु: कुसुमानि च
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.18577)
- **Original**: द्विचत्वारिंशन्नामानि प्रातरुत्थाय यः पठेत्‌। दृढां भक्ति हरेदास्यं लभते वाडिछितं फलम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.18578)
- **Original**: इति श्रीब्रह्मबैवर्ते देव: कृत यर्भस्थपरमेश्वरस्य श्रीकृष्णस्य स्तवन॑ सम्पूर्णय्‌। है ( श्रीकृष्णजन्मखण्ड 7।53--59) 4840-00 ियएए2 2000 आविर्भावकाले श्रीकृष्णस्वरूपम्‌ तत्रैेव भगवान्‌ कृष्णों दिव्यरूपं विधाय च । ह॒त्पशकोषाद्‌ देवक्या हरिराविर्गभभूबव ह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.18579)
- **Original**: अतीवकमनीय॑ ज्॒ शरीर॑ सुमनोहरम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.18580)
- **Original**: द्विभुज॑ मुसलीहरस्त॑ स्फुरन्मकरकुण्डलम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.18581)
- **Original**: ईषद्धास्यप्रसन्नास्यं भक्तानुग्रहकातरम्‌ । मणिरलेन्द्रसागाणां. भूषणैश्च विभूषितम्‌
- **Translation**: 

---

