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

### Verse 1 (Mahabharat 0.5981)
- **Original**: अनेकों पुण्यकर्म किये और फिर देह त्यागकर उन चाहिये। जो राजा प्रजाकी रक्षा नहीं करता; विनयहीन है,
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5981)
- **Original**: अनेकों पुण्यकर्म किये और फिर देह त्यागकर उन चाहिये। जो राजा प्रजाकी रक्षा नहीं करता; विनयहीन है,
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5982)
- **Original**: पुण्यलोकोंको प्राप्त किया जो बड़े-बड़े मेधावी, विद्वान: माजी है, मान्य पुरुषोंका सत्कार नहीं करता और गुणोंमें भी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5982)
- **Original**: पुण्यलोकोंको प्राप्त किया जो बड़े-बड़े मेधावी, विद्वान: माजी है, मान्य पुरुषोंका सत्कार नहीं करता और गुणोंमें भी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5983)
- **Original**: माननीय और प्रयागादि तीर्थस्थानोंमें झरीर छोड़नेवाल्लेंको दोषदृष्टि करता है, वह पापी हो जाता-है और ल्प्रेकमें उसे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5983)
- **Original**: माननीय और प्रयागादि तीर्थस्थानोंमें झरीर छोड़नेवाल्लेंको दोषदृष्टि करता है, वह पापी हो जाता-है और ल्प्रेकमें उसे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5984)
- **Original**: मिलते हैं।' गज गे व्यासजीका युधिष्ठिस्‍से काछकी महिमा कहना तथा युधिष्टिरका अर्जुनके प्रति पुनः अपना शोक प्रकट करना वैज्ञस्पायनजी कहते: हैं--राजन्‌ ! व्यासजीकी बात
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5984)
- **Original**: मिलते हैं।' गज गे व्यासजीका युधिष्ठिस्‍से काछकी महिमा कहना तथा युधिष्टिरका अर्जुनके प्रति पुनः अपना शोक प्रकट करना वैज्ञस्पायनजी कहते: हैं--राजन्‌ ! व्यासजीकी बात
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5985)
- **Original**: लेना मनुष्यके सशकी बात नहीं है। कभी-कभी तो मूर्ख सुनकर राजा युधिष्ठिरते कहा; “भगयन्‌ ! इस पृथ्वीके राज्य
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5985)
- **Original**: लेना मनुष्यके सशकी बात नहीं है। कभी-कभी तो मूर्ख सुनकर राजा युधिष्ठिरते कहा; “भगयन्‌ ! इस पृथ्वीके राज्य
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5986)
- **Original**: मनुष्यको भी उत्तम वस्तुकी प्राप्ति हो जाती है। बास्तवसें और तरह-तरहके भोगोंसे मेरे मनको प्रसन्नता नहीं है; मुझे तो
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5986)
- **Original**: मनुष्यको भी उत्तम वस्तुकी प्राप्ति हो जाती है। बास्तवसें और तरह-तरहके भोगोंसे मेरे मनको प्रसन्नता नहीं है; मुझे तो
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5987)
- **Original**: कार्यकी सिद्धिमें कालहीकी प्रधानता है। झिल्प, मन्त्र और यह झोक खाये जा रहा है। जिनके पति और पुत्र नष्ट हो गये
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5987)
- **Original**: कार्यकी सिद्धिमें कालहीकी प्रधानता है। झिल्प, मन्त्र और यह झोक खाये जा रहा है। जिनके पति और पुत्र नष्ट हो गये
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5988)
- **Original**: ओषधियाँ भी दुर्भाग्यके समय फल नहीं देतीं। समयकी हैं, ऐसी इन अबलाओंका बिलाप सुनकर मुझे तनिक भी चैन
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5988)
- **Original**: ओषधियाँ भी दुर्भाग्यके समय फल नहीं देतीं। समयकी हैं, ऐसी इन अबलाओंका बिलाप सुनकर मुझे तनिक भी चैन
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5989)
- **Original**: अनुकूलता होनेपर जब सौभाग्यका उदय होता है तो बे ही नहीं है।'
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5989)
- **Original**: अनुकूलता होनेपर जब सौभाग्यका उदय होता है तो बे ही नहीं है।'
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5990)
- **Original**: सफलता और वृद्धिकी निमित्त बन जाती हैं। समय आनेपर णजा युध्रिप्ठिकके इस प्रकार कहनेपर वेद-पारड्गडत
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5990)
- **Original**: सफलता और वृद्धिकी निमित्त बन जाती हैं। समय आनेपर णजा युध्रिप्ठिकके इस प्रकार कहनेपर वेद-पारड्गडत
- **Translation**: 

---

