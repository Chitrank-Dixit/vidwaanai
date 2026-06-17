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

### Verse 1 (Mahabharat 941.8421)
- **Original**: उपाख्यानका पाठ करता है, वह मोक्षरूप परम सिद्धिको प्राप्त उसका सेवन क्‍यों नहीं करते; कामनासे, भयसे, लोभसे
- **Translation**: 

---

### Verse 2 (Mahabharat 941.8421)
- **Original**: उपाख्यानका पाठ करता है, वह मोक्षरूप परम सिद्धिको प्राप्त उसका सेवन क्‍यों नहीं करते; कामनासे, भयसे, लोभसे
- **Translation**: 

---

### Verse 3 (Mahabharat 941.8422)
- **Original**: कर छेता है। इस विषयमें मेरे मनमें तनिक भी संदेह नहीं है। कि
- **Translation**: 

---

### Verse 4 (Mahabharat 941.8422)
- **Original**: कर छेता है। इस विषयमें मेरे मनमें तनिक भी संदेह नहीं है। कि
- **Translation**: 

---

### Verse 5 (Mahabharat 941.8423)
- **Original**: ख़र्गारोह्णपर्व समाप्त
- **Translation**: 

---

### Verse 6 (Mahabharat 941.8423)
- **Original**: ख़र्गारोह्णपर्व समाप्त
- **Translation**: 

---

### Verse 7 (Mahabharat 941.8424)
- **Original**: संक्षिप्त महाभारत समाप्त
- **Translation**: 

---

### Verse 8 (Mahabharat 941.8424)
- **Original**: संक्षिप्त महाभारत समाप्त
- **Translation**: 

---

### Verse 9 (Mahabharat 941.8425)
- **Original**: *+ म्रातापितृसह्लाण पुत्रदारप्तानि च। संसोरेशनुभूतानि यात्ति याद्यक्ति चापे
- **Translation**: 

---

### Verse 10 (Mahabharat 941.8425)
- **Original**: *+ म्रातापितृसह्लाण पुत्रदारप्तानि च। संसोरेशनुभूतानि यात्ति याद्यक्ति चापे
- **Translation**: 

---

### Verse 11 (Mahabharat 941.8426)
- **Original**: + हर्वस्थाससहस्नाणि भयर्थानशतानि च।दिक्से दिवसे मूहमाविशत्ति न पष्डितम्‌
- **Translation**: 

---

### Verse 12 (Mahabharat 941.8426)
- **Original**: + हर्वस्थाससहस्नाणि भयर्थानशतानि च।दिक्से दिवसे मूहमाविशत्ति न पष्डितम्‌
- **Translation**: 

---

### Verse 13 (Mahabharat 941.8427)
- **Original**: $ ऊर्घबाहु्विरम्पेष न च कब्िच्छृणोति मे
- **Translation**: 

---

### Verse 14 (Mahabharat 941.8427)
- **Original**: $ ऊर्घबाहु्विरम्पेष न च कब्िच्छृणोति मे
- **Translation**: 

---

### Verse 15 (Mahabharat 941.8428)
- **Original**: धर्मदर्षश्ष काम्ष से किम न सेव्यते
- **Translation**: 

---

### Verse 16 (Mahabharat 941.8428)
- **Original**: धर्मदर्षश्ष काम्ष से किम न सेव्यते
- **Translation**: 

---

### Verse 17 (Mahabharat 941.8429)
- **Original**: $ न जातु कामान्न भयात्र लेभाडम॑ त्यजेजीवितस्यापि हेतोः। नित्यो धर्म: सुखदुःसे त्वनित्ये जीवो निलयो हेतुसुव तवनित्व:
- **Translation**: 

---

### Verse 18 (Mahabharat 941.8429)
- **Original**: $ न जातु कामान्न भयात्र लेभाडम॑ त्यजेजीवितस्यापि हेतोः। नित्यो धर्म: सुखदुःसे त्वनित्ये जीवो निलयो हेतुसुव तवनित्व:
- **Translation**: 

---

### Verse 19 (Mahabharat 941.8430)
- **Original**: » इम्र भारतसाकितीं प्रात्सत्थाय यः पठेत्‌।स भारतफ़ल प्राप्य पर ब्रह्माधिगच्छति
- **Translation**: 

---

### Verse 20 (Mahabharat 941.8430)
- **Original**: » इम्र भारतसाकितीं प्रात्सत्थाय यः पठेत्‌।स भारतफ़ल प्राप्य पर ब्रह्माधिगच्छति
- **Translation**: 

---

