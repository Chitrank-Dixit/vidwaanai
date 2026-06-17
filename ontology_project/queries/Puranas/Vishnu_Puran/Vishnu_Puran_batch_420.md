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

### Verse 1 (Vishnu Puran 0.8381)
- **Original**: 75--77
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8382)
- **Original**: कुरुके पुत्र सुधनु, जद् और परीक्षित्‌ आदि हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8383)
- **Original**: सुधनुका पुत्र सुहोत्र था, सुहोत्रका च्यवन, च्यवनका कृतक और कुतकका पुत्र उपरिचर वसु हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8384)
- **Original**: वसुके बृहद्रथ, प्रत्यग्र, कुशाम्बु, कुचेल और मात्स्य आदि सात पुत्र थे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8385)
- **Original**: इनमेंसे युहदथके कुशाग्र, कुदाग्रके यृषभ, वृषभके पुष्पवान, पुष्पवानके सत्यहित, सत्यहितके सुधन्चा और सुधन्याके जतुका जन्म हुआ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8386)
- **Original**: बृहद्रथके दो खण्डोंमें विभक्त एक पुत्र और हुआ था जो कि जराकेः द्वारा जोड़ दिये जानेपर जरासन्ध कहलाया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8387)
- **Original**: उससे सहदेवका जन्म हुआ तथा सहदेवसे सोमप और सोमपसे श्रुतिश्रवाकी उत्पत्ति हुई
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8388)
- **Original**: इस प्रकार मैंने तुमसे यह मागध भूपात्मेंका वर्णन कर दिया है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8389)
- **Original**: 335 औ तततता इति श्रीविष्णपुराणे चतुर्थेईशे एकोन्विंशोउध्यायः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8390)
- **Original**: नि बीसवाँ अध्याय कुरुके वैद्ञका वर्णन श्रीपराजर उवाच ओऔपराहारजी जोस्ठे--[ कुरुपुत्र ] परीक्षितके परीक्षितो जनमेजयश्रुतसेनोग्रसेन-
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8391)
- **Original**: जनमेजय, श्रुतसेन, उग्सेन और भीमसेन नामक चार पुत्र भीमसेनाशत्वार: पुत्रा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8392)
- **Original**: ज्ोस्तु सुरथो नामात्मजो खभूब
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8393)
- **Original**: तस्यापि विदूरथः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8394)
- **Original**: तस्मात्सावभौमस्सार्वभौमाजयत्सेन- स्तस्मादाराधितस्ततश्चायुतायुरयुतायो रक्रो धनः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8395)
- **Original**: तस्थाद्वेवातिथि:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8396)
- **Original**: . ततश्ष ऋक्षोउन्‍्यो3भवत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8397)
- **Original**: ऋक्षाद्धीमसेनस्ततश्र दिल्लीप:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8398)
- **Original**: दिलीपात्‌ प्रतीप:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8399)
- **Original**: तस्यापि देवापिशान्तनुबाद्लीकसंज्ञासखत्रयः पुत्रा बभूयु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8400)
- **Original**: देवापिाल एवारण्यं विवेश
- **Translation**: 

---

