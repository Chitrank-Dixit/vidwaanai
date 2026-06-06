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

### Verse 1 (Mahabharat 0.4001)
- **Original**: अर्जुनको उससे नहीं मारा, इसमें मैं दैवको ही प्रधान कारण तो तुम श्रीकृष्णको ही मार डाल्प्रे; क्योंकि थे ही पाण्डबोंके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4001)
- **Original**: अर्जुनको उससे नहीं मारा, इसमें मैं दैवको ही प्रधान कारण तो तुम श्रीकृष्णको ही मार डाल्प्रे; क्योंकि थे ही पाण्डबोंके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4002)
- **Original**: आती थी। अब वह घटोत्कचपर पड़नेसे व्यर्थ हो गयी--थह लिये मृत्युकप है--यह सोच-सोचकर मुझे रातमें नींद नहीं समझता हूँ। युथ्िष्ठिरका विषाद और भगवान्‌ कृष्ण तथा व्यासजीके द्वारा उसका निवारण घृतराएने पूछ--सञ़्य ! अब आगेकी बात बताओ ।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4002)
- **Original**: आती थी। अब वह घटोत्कचपर पड़नेसे व्यर्थ हो गयी--थह लिये मृत्युकप है--यह सोच-सोचकर मुझे रातमें नींद नहीं समझता हूँ। युथ्िष्ठिरका विषाद और भगवान्‌ कृष्ण तथा व्यासजीके द्वारा उसका निवारण घृतराएने पूछ--सञ़्य ! अब आगेकी बात बताओ ।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4003)
- **Original**: आँसू बहने छगे। उच्छ्लास चलने छगा। उस समय कर्णका घटोत्कचके मारे जानेपर कौरव-पाण्डवॉमें किस प्रकार युद्ध
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4003)
- **Original**: आँसू बहने छगे। उच्छ्लास चलने छगा। उस समय कर्णका घटोत्कचके मारे जानेपर कौरव-पाण्डवॉमें किस प्रकार युद्ध
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4004)
- **Original**: पराक्रम देखकर वे अत्यन्त अभीर हो गये। हुआ? उनको इस अवस्थामें देख भगवान्‌ श्रीकृष्णने कहा-- सजबने कहा--महाराज ! कर्णके द्वारा उस राक्षसके मारे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4004)
- **Original**: पराक्रम देखकर वे अत्यन्त अभीर हो गये। हुआ? उनको इस अवस्थामें देख भगवान्‌ श्रीकृष्णने कहा-- सजबने कहा--महाराज ! कर्णके द्वारा उस राक्षसके मारे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4005)
- **Original**: 'कुत्तीनन्दन ! आप खेद न कीजिये, आपके लिये-यह जानेपर आपके सैनिक बड़े प्रसन्न हुए। वे ऊँचे स्वरसे गर्जना
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4005)
- **Original**: 'कुत्तीनन्दन ! आप खेद न कीजिये, आपके लिये-यह जानेपर आपके सैनिक बड़े प्रसन्न हुए। वे ऊँचे स्वरसे गर्जना
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4006)
- **Original**: व्याकुलता झोभा नहीं देती । यह तो अज्ञानी मनुष्योंका काम करने लगे और बड़े वेगसे इधर-उधर दौड़ने छगे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4006)
- **Original**: व्याकुलता झोभा नहीं देती । यह तो अज्ञानी मनुष्योंका काम करने लगे और बड़े वेगसे इधर-उधर दौड़ने छगे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4007)
- **Original**: उधर उस
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4007)
- **Original**: उधर उस
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4008)
- **Original**: है। उठिये और युद्ध कीजिये । इस महासंप्रापका गुरुतर भार घोर अन्धकारमयी सजनीयें पाण्डवसेनाका संहार हो रहा था,
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4008)
- **Original**: है। उठिये और युद्ध कीजिये । इस महासंप्रापका गुरुतर भार घोर अन्धकारमयी सजनीयें पाण्डवसेनाका संहार हो रहा था,
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4009)
- **Original**: सैभालिये। आप ही घबरा जायँगे, तब तो विजय पिलनेपें इससे राजा युध्िष्ठिकता मन बहुत छोटा हो गया। जे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4009)
- **Original**: सैभालिये। आप ही घबरा जायँगे, तब तो विजय पिलनेपें इससे राजा युध्िष्ठिकता मन बहुत छोटा हो गया। जे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4010)
- **Original**: संदेह ही रहेगा।' श्रीकृष्णकी जात सुनकर युथिष्टिरने आँखें भीमसेनसे बोले--'महाबाहो ! धृतराष््रकी सेनाक्रो रोको; मैं
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4010)
- **Original**: संदेह ही रहेगा।' श्रीकृष्णकी जात सुनकर युथिष्टिरने आँखें भीमसेनसे बोले--'महाबाहो ! धृतराष््रकी सेनाक्रो रोको; मैं
- **Translation**: 

---

