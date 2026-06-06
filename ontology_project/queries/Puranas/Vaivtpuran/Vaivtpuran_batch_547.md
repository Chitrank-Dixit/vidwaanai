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

### Verse 1 (Vaivtpuran 36.8042)
- **Original**: सर्वसम्पत्प्रदस्यास्य कवचस्य धर्मार्थकाममोक्षेषु विनियोग: 3» हीं कमलवासिन्ये॑ स्वाहा मे पातु मस्तकम्‌ । 35 श्रीं श्रिय स्वाहेति च कर्णयुग्म॑ सदाउवतु । 3 हों श्री क्लों महालक्ष्म्यै स्वाहा मे पातु नासिकाम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.8043)
- **Original**: 35 श्रीं पद्मयालयायै च स्वाहा दन्‍्त॑ सदाउवतु । 3* श्रीं कृष्णप्रियाय॑े च दन्तरन्ध्रं सदाउवतु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.8044)
- **Original**: 35 श्रीं नाग़यणेशाय॑ मम कण्ठं॑ सदाउवतु । 3» श्रीं केशवकान्ताय मम स्कन्ध॑ सदाउवतु
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.8045)
- **Original**: 3 श्रीं पद्मनिवासिन्ये स्वाहा नाभि सदाउवतु । 3» हीं श्रीं संसारमात्रे मम वक्ष: सदाउवतु
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.8046)
- **Original**: 3+ श्रीं श्री कृष्णकान्तायै स्वाहा पृष्ठ सदाउवतु । 3 हू श्रीं ज्रिये स्वाहा मम हस्तौ सदा5वतु
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.8047)
- **Original**: 3> श्रों मिवासकान्ताये मम पादौ सदाउवतु । 30 हों श्रीं क्लीं श्रियै स्वाहा सर्वाज्र में सदाउयतु
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.8048)
- **Original**: पातूर्ष्यमधो विष्णुप्रियाउवतु । सतर्त सर्वत: पातु विष्णुप्राणधिका मघम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 37.18083)
- **Original**: + श्रीदु्गास्तोत्राणि * 797 44.48 44404. 4
- **Translation**: 

---

### Verse 9 (Vaivtpuran 37.18084)
- **Original**: 40 00400 00008 0 0
- **Translation**: 

---

### Verse 10 (Vaivtpuran 37.18085)
- **Original**: 40440000। ।।।। 4 40/]
- **Translation**: 

---

### Verse 11 (Vaivtpuran 37.18086)
- **Original**: ै [(] %8
- **Translation**: 

---

### Verse 12 (Vaivtpuran 37.18087)
- **Original**: 8#&#&#% #& 3» क्रीं भद्रकाल्य स्वाहा मम वक्ष: सदावतु । 3» क्रीं कालिकायै स्वाहा मम नाभिं सदावतु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 37.18088)
- **Original**: <% ह्रीं कालिकायै स्वाहा मम पृष्ठ सदावतु। रक्तबीजविनाशिन्ये स्वाहा हस्तो सदावतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 37.18089)
- **Original**: 3» हीं क्लीं मुण्डमालिन्यै स्वाहा पादौ सदावतु । 30 हीं चामुण्डायै स्वाहा सर्वाड्रं मे सदाबतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 37.18090)
- **Original**: प्राच्यां पातु महाकाली आग्रेय्यां रक्तदन्तिका । दक्षिणे पातु चामुण्डा नैऋत्यां पातु कालिका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 37.18091)
- **Original**: श्यामा च खारुणे पातु वायव्यां पातु चणिडिका । उत्तरें विकटास्था चर ऐशान्यां साइहासिनी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 37.18092)
- **Original**: ऊर्ध्व पातु लोलजिह्ना मायाद्या पात्वथ: सदा । जले स्थले चान्तरिक्षे पातु विश्वप्रसू: सदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 37.18093)
- **Original**: इति ते कथित वत्स सर्वमनत्रौधविग्रहम्‌ । सर्वेधाँ कवचानां चर सारभूत॑ परात्यपरम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 37.18094)
- **Original**: सप्तद्वीपेश्रों राजा सुचन्द्रोौइस्थ प्रसादतः । कबचस्य॒ प्रसादेन मान्धाता पृथिवीपति:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 37.18095)
- **Original**: प्रचेता लोमशश्जैब यत: सिद्धों बभूब ह । यतो हि योगिनां श्रेष्ठ: सौभारि: पिप्पलायन:
- **Translation**: 

---

