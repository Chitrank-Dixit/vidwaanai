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

### Verse 1 (Vishnu Puran 0.7121)
- **Original**: अच्यैव ते व्यलीकलज्ञा- यत्यास्तथा शास्तिमहं करोमि
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7122)
- **Original**: यथा च नैवमध्याप्यतिमन्थरवचना भविष्यसीति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7123)
- **Original**: अथ भगवान्‌ पितामह: त॑ कुमार सनश्निवार्य स्वयमपृच्छत्तां ताराम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7124)
- **Original**: कथय यत्से कस्यायमात्मज: सोमस्य वा बृहस्पतेर्वा इत्युक्ता लज्जमानाह सोमस्येति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7125)
- **Original**: ततः प्रस्फुर- कुमारमालिड्रय साधु साधु बत्स प्राज्ञोउसीति बुध इति तस्य च्ञ नाम चक्रे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7126)
- **Original**: 255 देनेमें] बड़ा उद्योग किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7127)
- **Original**: तथा सकल देव-सेनाके सहित इन्द्र बुहस्पतिजीके सहायक हुए
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7128)
- **Original**: इस प्रकार ताराके लिये उनमें तारकामय नामक अत्यन्त घोर युद्ध छिड़ गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7129)
- **Original**: तब स्द्ध आदि देवगण दानवोंके प्रति और दानवगण देवताओंके प्रति नाना प्रकास्के दास्र छोड़ने छगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7130)
- **Original**: इस प्रकार देवासुर-संग्रामसे क्षुब्ध-क्त्ति हो सम्पूर्ण संसारने ब्रह्माजीकी शरण ली
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7131)
- **Original**: तब भगवान्‌ कमलछ-यगोनिने भी शुक्र, रुद्र, दानव और देवगणको युद्धसे निवृत्त कर बृहस्पतिजीको ताय दिकया दी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7132)
- **Original**: उसे गर्भिणी देखकर बृहस्पतिजीने कहा--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7133)
- **Original**: “मेरे क्षेत्र तुझको दूसरेक् पुत्र धारण करना उचित नहीं हैं; इसे दूर कर, अधिक धृष्टता करना ठीक नहों”
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7134)
- **Original**: बृहस्पतिजोके ऐसा कहनेपर उस पतिव्रताने पतिके खचनानुसार वह गर्भ इधीकास्तम्ब (सींकको झाड़ी) में छोड़ दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7135)
- **Original**: उस छोड़े हुए गर्भने अपने तेजसे समस्त देवताओंके तेजकों मल्ठिग कर दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7136)
- **Original**: तदनन्तर उस बालककों सुच्दरताके कारण बृहस्पति और चन्द्रमा दोनोंको उसे लेनेके छिये उत्सुक देख देवताओंने सन्देह हो.जानेके कारण तारासे पूछझ---
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7137)
- **Original**: “ हे सुभगे ! तू हमको सच-सच बता, यह पुत्र वृहस्पतिका है या चन्‍्द्रमाकग्र ?''
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7138)
- **Original**: उनके ऐसा कहनेपर तायणने खज्लावचदा कुछ भी न कहा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7139)
- **Original**: जब बहुत कुछ कहनेपर भो वह देवताओंसे न बोल्मे तो वह बालक उसे ज्ञाप देनेके लिये उच्यृत होकर बोल्ला---
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7140)
- **Original**: “अरी दुष्टा माँ ! तू मेरे पिताका नाम क्‍यों नहीं बतलाती ? तुझ व्यर्थ लज्जावतीकी मैं अभी ऐसी गति करूँगा जिससे तू आजसे हो इस प्रकार अत्यन्त धीरे-धीरे बोलना भूल जायगी”
- **Translation**: 

---

