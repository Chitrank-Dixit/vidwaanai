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

### Verse 1 (Padam Puran 7.1321)
- **Original**: भाति सर्यत्र यो भूत्वा धूतानों धूतिवर्थन:।
- **Translation**: 

---

### Verse 2 (Padam Puran 7.1322)
- **Original**: समधायाय सद्धम॑ नमामि प्रणव परम्‌
- **Translation**: 

---

### Verse 3 (Padam Puran 7.1323)
- **Original**: खिचार॑ वेदरूपे ते यज़ाड़्ये यज्ञवल्लभम्‌। योति सर्वस्थ स्मेकस्थ ऑकार. प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 4 (Padam Puran 7.1324)
- **Original**: तारक सर्वल्पेकाना नौरूपेण विराजितम्‌
- **Translation**: 

---

### Verse 5 (Padam Puran 7.1325)
- **Original**: संसारा्णवमपग्रानौ सम्ताम्ि प्रणव हरिम्‌ ।। वसते सर्वभूतेषु एकरूपेण तैकधा
- **Translation**: 

---

### Verse 6 (Padam Puran 7.1326)
- **Original**: धामकैवल्थरूपेण.. नमामि. वरद॑ सुख्म्‌
- **Translation**: 

---

### Verse 7 (Padam Puran 7.1327)
- **Original**: सूक्ष्म सूक्ष्मतरे. झुरद्ध निर्गुणं॑_गुणनायकम
- **Translation**: 

---

### Verse 8 (Padam Puran 7.1328)
- **Original**: वर्मिति प्राकृतैर्भावलेंदाख्येत॑.. नमाम्यहम्‌
- **Translation**: 

---

### Verse 9 (Padam Puran 7.1329)
- **Original**: देवदैत्पवियोगैश्व यर्जिते तुष्टिधिस्तथा । येटैश.. योगिभिश्येंय. तमोड़तरे.. नमास्यहस्‌
- **Translation**: 

---

### Verse 10 (Padam Puran 7.1330)
- **Original**: व्यापक. विश्वयेतार विज्ञान परम॑ पदम्‌। दिये दशिखगुणे. शात्ते खच्दे. प्रणबमीश्ररम्‌
- **Translation**: 

---

### Verse 11 (Padam Puran 7.1331)
- **Original**: यस्य मायां प्रबिष्टास्तु अह्याद्याध सुरासुरा-।न किन्दन्ति पर शुद्ध मोक्षद्वाई नमाम्यहम्‌
- **Translation**: 

---

### Verse 12 (Padam Puran 7.1332)
- **Original**: आननन्‍दकत्दाय च केबलाय शुद्धाय हँसाय परायराय
- **Translation**: 

---

### Verse 13 (Padam Puran 7.1333)
- **Original**: नघो5स्तु तस्के गुणनायकाय ओयासुदेखाय महाप्रभाय
- **Translation**: 

---

### Verse 14 (Padam Puran 7.1334)
- **Original**: श्रीणाझजन्पेत विराजमान रविप्रभेणापि सुद्डनेन
- **Translation**: 

---

### Verse 15 (Padam Puran 7.1335)
- **Original**: गदार्यकेसापि विशोभमान विष्णु सदैव शरण प्रपे
- **Translation**: 

---

### Verse 16 (Padam Puran 7.1336)
- **Original**: ये वेद कोई सुगुणे शुण्यमामाथारभूते सचराचरस्प
- **Translation**: 

---

### Verse 17 (Padam Puran 7.1337)
- **Original**: य॑ सूर्यवैधानरतुल्यतेजस ते जासुदेव द्ञारण प्रफे
- **Translation**: 

---

### Verse 18 (Padam Puran 7.1338)
- **Original**: तसोघकुसोे स्वकौर्विकाज्च॑कर्मेति नित्ये यतिधर्महेतुम्‌
- **Translation**: 

---

### Verse 19 (Padam Puran 7.1339)
- **Original**: उच्योतमान॑ रवितेजसोध्ये॑ते वासुदेव॑ शरण प्रपद्चे
- **Translation**: 

---

### Verse 20 (Padam Puran 7.1340)
- **Original**: सुधानिधात॑ विमलाशुरूपमानदमानेन. विराजमानम्‌
- **Translation**: 

---

