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

### Verse 1 (Vishnu Puran 0.6501)
- **Original**: 532 अविष्णुपुराण
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6502)
- **Original**: अण्2 इत्पाकर्ण्य समस्तदेबैस्न्द्रिण च्ञ बराढमित्येव समन्वीप्सितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6503)
- **Original**: ततश्व शतक्रतोर्यृषरूप- धारिण: ककुदि स्थितो5तिरोषसमन्थितो भगवत- श्वराचरगुरोरच्युतस्यतेजसाप्यायितो देवासुर- सड्य्रामे समस्तानेवासुराज्निजघान
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6504)
- **Original**: यह सुनकर समस्त देवगण और इन्द्रगे 'बहूत अच्छा'---ऐसा कहकर उनका कथन स्वीकार कर लिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6505)
- **Original**: फिर वुषभ-रूपधारी इन्द्रकी पीठपर चढ़कर चराच्तरगुरु भगवान्‌ अच्युतके तेजसे परिपूर्ण होकर राजा पुरञ्ञयने रोषपूर्वतक सभी दैत्यॉक्व्रे मार यतश्न॒ वृषभककुदि स्थितेन राज्ञा दैतेयबले
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6506)
- **Original**: उस राजाने बैसके ककुद, (कन्चे) पर निषूदितमतश्नासा ककुत्स्थसंज्ञामबाप
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6507)
- **Original**: ककुत्स्थस्याप्यनेना: पुत्रो$भकत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6508)
- **Original**: पृथुरनेनस:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6509)
- **Original**: पृथोर्विष्टराश्व:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6510)
- **Original**: तस्यापि चान्रो युवनाश्च:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6511)
- **Original**: चान्द्रस्य तस्य युवनाश्रस्थ श्ञावस्त: यः पुरी श्ावस्तीं निवेशयामास
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6512)
- **Original**: शावस्तस्थ बृहदश्न: तस्थापि कुकल्याश्र:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6513)
- **Original**: योअसावुदकस्य महर्षेरपकारिणं धुलधुनामानमसुरं वैष्णवेन तेजसाप्यायित: पुत्रसहस्लेरेकिंशद्धिः परिवृतों जधान धु्धुमारसंज्ञामवाप ।। 40
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6514)
- **Original**: तस्य क्ञ तनयास्समस्ता एवं धुन्धुपुखनिःश्रासापिना बिनेशु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6515)
- **Original**: वदृढाश्रचन्वाश्च- श्ष त्रय: केवल शेषिता:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6516)
- **Original**: दृदाश्राद्धर्यश्र:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6517)
- **Original**: तस्माश्च॒निकुम्भ:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6518)
- **Original**: निकुम्मस्यामिताश्च:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6519)
- **Original**: ततअ कुशाश्व:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6520)
- **Original**: तस्माश् प्रसेनजित्‌
- **Translation**: 

---

