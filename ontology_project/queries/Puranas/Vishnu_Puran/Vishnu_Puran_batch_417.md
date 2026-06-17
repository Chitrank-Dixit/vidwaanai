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

### Verse 1 (Vishnu Puran 0.8321)
- **Original**: 45---47
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8322)
- **Original**: अ* 19 ] द्विजमीढस्थ तु यवीनरसंज्ञ: पुत्र:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8323)
- **Original**: सन्नतिमान्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8324)
- **Original**: सन्नतिमत: कृत: पुत्रो3भूत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8325)
- **Original**: ये हिरण्यनाभो योगमध्यापयामास
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8326)
- **Original**: अश्चतुर्विशति प्राच्यसामगानां संहिताश्वकार
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8327)
- **Original**: कृताछोग्रायुथः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8328)
- **Original**: येन प्राचुयेंण नीपक्षय: कृत:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8329)
- **Original**: उम्रायुधाक््षेम्थ: .. ्षेम्यात्सुधीरस्तस्मादिपुझ्रय स्तस्माच बहुरथ इत्येते पौरवा:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8330)
- **Original**: पुत्रोउईप्रबत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8331)
- **Original**: . तस्पादपि.. झान्तिः गान्तेस्सुशान्तिस्सुआन्ते: पुरक्षयस्तस्माथ ऋऋक्षः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8332)
- **Original**: ततश्व हर्यश्रवः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8333)
- **Original**: तस्मान्पुद्ल- सृञ्नयबृहदिषुयवीनरकाम्पिल्यसंज्ञा: पश्चानामेव तेषां विषयाणां रक्षणायालमेते मत्पुत्रा इति पित्राभिह्निता: पाञ्ञाला:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8334)
- **Original**: मुद़लाच्न पौ क़ल्या: क्षत्रोपेता द्विजातयो बचूवु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8335)
- **Original**: मुद्रलादबृहदश्च:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8336)
- **Original**: बृहदशाहिवोदासोडहल्‍्या च मिथुनमभूत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8337)
- **Original**: शरद्तश्राहल्यायां शतानन्दो3भवत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8338)
- **Original**: शतानन्दात्सत्यधृतिर्धनुबेंदान्तगो जज्ञे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8339)
- **Original**: सत्यधृतेर्वराष्सरसमुर्वज्ञी दृषठा रेतस्कन्न झरस्तम्बे पपात
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8340)
- **Original**: तत्च द्विधागतमपत्यद्वयय कुमार: कन्या चाभवत्‌
- **Translation**: 

---

