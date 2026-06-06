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

### Verse 1 (Vishnu Puran 0.8681)
- **Original**: स्त्रीत्वमेवोषभोगहेतु:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8682)
- **Original**: अनृतमेव व्यवहारजयहेतु:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8683)
- **Original**: उन्नताम्बुतैब पृथियीहेतु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8684)
- **Original**: ब्रह्मसूत्रमेब विप्रत्वहेतु:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8685)
- **Original**: रल्रधातुतैव इलाघ्यताहेतु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8686)
- **Original**: लिडुधारणमेवाश्रमहेतु:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8687)
- **Original**: अन्याय एव वृत्तिहेतु:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8688)
- **Original**: दोर्बल्यमेवावृत्तिहेतु:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8689)
- **Original**: अभयप्रगल्भोघ्वारणमेव पाण्टडित्यहेतु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8690)
- **Original**: अना्यतैव साथुत्वहेतु:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8691)
- **Original**: स््रानमेव प्रसाधनद्वेतु:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8692)
- **Original**: दानमेव धम्महितु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8693)
- **Original**: स्वीकरणमेव विवाहहेतु:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8694)
- **Original**: सद्देषधार्ये्र पात्रम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8695)
- **Original**: दूरायतनोदकमेव तीर्थहितु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8696)
- **Original**: कपटवेषधारणमेव महत्त्वहेतु:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8697)
- **Original**: इत्येवमनेकदोषोत्ते तु भूमण्डले सर्ववर्णेश्वेन यो यो बलवान्स स भूपति- भविष्यति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8698)
- **Original**: एवं चातिलुब्धकराजासहाइशैलानामन्तर द्रोणी प्रजास्संश्रयिष्यन्ति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8699)
- **Original**: जीविष्यति अनवरतं चात्र कल्युगे क्षयमाया- त्यखिल एवैष जन:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8700)
- **Original**: ओ्रौते स्मात्ते च॒ धर्मे विध्नवमत्यन्तमुपगते क्षीणप्राये च कलाबशेष- जगत्प्नप्श्नराचरगुरोरादिमध्यान्तरहितस्थ॒ ब्रह्म- मयस्थात्मरूपिणो भगवतो वासुदेवस्थांश- इशम्बलग्रामप्रधानब्राह्मणस्य विष्णुबवशसो गृहेष्रगुणद्धिंसमन्वित: कल्किरूपी जगत्यत्रावतीर्य- सकल्स्‍्लेच्छदस्युदुष्टाचरणचेतसामशेषाणा क्षयं.. करिष्यति चतुर्थ अंडा हे0र तब दिन-दिन धर्म और अर्थका थोड-थोड़ा हास तथा क्षय होनेके कारण संसारका क्षय हो जायगा
- **Translation**: 

---

