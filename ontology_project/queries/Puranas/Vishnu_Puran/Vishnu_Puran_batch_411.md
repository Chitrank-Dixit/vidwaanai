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

### Verse 1 (Vishnu Puran 0.8201)
- **Original**: तस्माश्व महामना:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8202)
- **Original**: महाशाल, महाशाल्म्के सहामना और महासनाके उच्चीनर तस्मादुशीनरतितिक्षु द्वौ पुत्रावुत्यन्नौ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8203)
- **Original**: उश्ीनरस्थापि शिक्षिनुगनरकृमिबर्माख्या: पञ्च पुत्रा बभूवु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8204)
- **Original**: पृषदर्भसुवीरकेकयमद्रका- अ्वत्वारश्शियिपुत्रा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8205)
- **Original**: तितिक्षोरपि रुदाद्रथः पुत्रोईभूत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8206)
- **Original**: तस्थापि हेमो हेमस्यापि सुतपा: सुतपसश्च बलि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8207)
- **Original**: यस्य क्षेत्रे दीर्घतमसाडु-बड्रकलिड्सुहापोण्ड्राख्यं वालेय॑ क्षत्रमजन्बत
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8208)
- **Original**: तन्नामसन्ततिसंज्ञाश्ष पद्चव्रिषया बभूवुः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8209)
- **Original**: अड्भादनपानस्ततो दिविरथस्तस्माद्धम॑रथ:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8210)
- **Original**: ततश्नित्ररथो रोमपादसंज्ञ:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8211)
- **Original**: यस्‍स्यथ दशरथो मित्र जन्ने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8212)
- **Original**: यस्याजपुत्रो दशरथइशान्तां नाम कन्यामनपत्यस्थ दुहितृत्वे युयोज
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8213)
- **Original**: रोमपादाघतुरड्भस्तस्मात्यूथुलाक्ष:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8214)
- **Original**: ततश्चम्पों यश्चग्पां निवेशवामास
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8215)
- **Original**: चम्पस्थ हर्यझी नामात्मजो5भूत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8216)
- **Original**: हर्यड्डाम्द्द्वर्थो भद्गरथादबृहद्रथो बृहद्रथादबृहत्कर्मा बृहत्कर्पणश्व बृहद्धानुस्तस्माच्च बृहन्मना बृहन्मनसो जयद्रथः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8217)
- **Original**: जयद्रथो ब्रह्मक्षत्रान्तरालसम्भूत्यां पल्यां विजय नाम पुत्रमजीजनत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8218)
- **Original**: विजयश्च धृ्ति पुत्रमबाप
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8219)
- **Original**: तस्थापि धृतब्रत: पुत्रो5भूत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8220)
- **Original**: धृतब्रतात्सत्यकर्मा
- **Translation**: 

---

