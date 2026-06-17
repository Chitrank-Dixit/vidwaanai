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

### Verse 1 (Vishnu Puran 0.7361)
- **Original**: सन्नतेः सुनीथस्तस्यापि सुकेतुस्तस्माद्च श्र्मकेतुर्जज़े
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7362)
- **Original**: ततश्च सत्यकेतुस्तस्माद्वि- श्च सुकुमारस्तस्यापि धृष्टकेतुस्ततश्ष॒बीतिहोमत्रस्तस्माद्धा्ों भार्गस्य भार्गभूमिस्ततश्नातुर्वण्ण्यप्रवृत्तिरित्मेते काइय भूभृतः कथिताः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7363)
- **Original**: खर्जेस्तु श्रूयताम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7364)
- **Original**: ओीधिष्णुपुराण [ ऋ 9 धन्कनन्तरिका पुत्र केतुमानू, केतुमानूका भीमरथ, भीमरथका दिजोदास तथा दिवोदासका पुत्र प्रतर्दन हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7365)
- **Original**: उसने मद्रश्नेण्यवैशका नाश करके समस्त चातुऑपर खिजय प्राप्त की थी, इसलिये उसका नाम “झत्ुजित' हुआ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7366)
- **Original**: दिवोदासने अपने इस पुत्र (प्रतर्दन) से अत्यत्त प्रेमबश “वत्स, तत्स' कहा था, इसल्यि इसका नाम 'वत्स' हुआ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7367)
- **Original**: अत्यन्त सत्यपरायण होनेके कारण इसका नाम 'ऋतध्वज' हुआ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7368)
- **Original**: तदनत्तर इसने कुखछय नामक अपूर्व अश्व प्राप्त किया । इसलिये यह इस पृथिवोतलपर 'कुवल्याश्र' नामसे विख्यात हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7369)
- **Original**: इस कत्सके अलर्क नामक पुत्र हुआ जिसके विषयमें यह इल्म्रेके आजतक गाया जाता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7370)
- **Original**: 'पूर्वकालमें अलर्कके अतिरिक्त और किसीने भी झछठ सहस्र वर्षतक युवावस्यामें रहकर पृथिवीका भोग नहीं किया'
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7371)
- **Original**: उस अलर्कके भी सन्नति नामक पुत्र हुआ; सन्नतिके सुनीथ, सुनोधके सुकेतु, सुकेतुके घर्मकेतु, धर्मकेतुके सत्यकेतु, सत्यकेतुके विभु, विभुके सुविभु, सुविभुक्े सुकुमार, सुकुमारके घरष्टकेतु, धृष्टकेतुके लीतिहोत वीतिहोत्रके भार्ग और भार्गके भार्गभुमि नामक पुत्र हुआ भार्गभूमिसे चातुर्वर्ण्यका प्रचार हुआ। इस प्रकार :
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7372)
- **Original**: काह्यवैदके राजाओंका वर्णन हो चुका अब रजिकी सन्तानका विवरण सुनो
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7373)
- **Original**: 18--21
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7374)
- **Original**: अपा++++50 दि. 27070»ः«_>»»« इति श्रीविष्णुपुराणे चतुर्थेंडशे अष्टमोध्ध्यायः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7375)
- **Original**: व्क्च्न औ पकत+े नवाँ अध्याय महाराज रजि और उनके पुत्रॉका चरित्र ओपराशर उठाच श्रीपराशरजी बोले--राजिके अतुल्तित बल- रजेस्तु पक्न पुत्रशतान्यतुलअलछपराक्रमसारा-
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7376)
- **Original**: पराक्रमशाली पाँच सौ पुत्र थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7377)
- **Original**: एक बार देवासुर- ण्यासन्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7378)
- **Original**: देवासुरसंप्रामारम्भे ले परस्पर-
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7379)
- **Original**: संग्रामके आरम्भमें एक-दूसरेको मारनेकी इच्छावाले देवता वधेप्सवो देवाश्चासुराश् ब्रह्माणमुपेत्य पप्रच्छु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7380)
- **Original**: और दैत्योनि क्रह्माजीके पास जाकर पूछा--““भगवन्‌ !
- **Translation**: 

---

