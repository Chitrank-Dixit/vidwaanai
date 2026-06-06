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

### Verse 1 (Vishnu Puran 0.8241)
- **Original**: अ* 19 ] चतुर्थ अंझ उन्नीसवाँ अध्याय पुरुखंदा श्रीपदाशर उवाच पुरोर्जनमेजयस्तस्यापि प्रचिन्वान्‌ प्रचिन्वतः प्रवीर: प्रवीराश्मनस्पुर्मनस्ो: सुझुस्सुद्योर्यहुगतस्तस्यापि संयातिस्संयात्तेरह॑याति- स्ततो रौद्राश्च:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8242)
- **Original**: ऋतेषुकक्षेषुस्थण्डिलेषुकृतेषुजलेषुधरमेंषु- धृतेषुस्थलेघुसब्नतेषुबनेषुनामानो रोद्राश्वस्य दश पुत्रा बभूवु:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8243)
- **Original**: ऋतेषोरन्तिनार: पुत्रो$भूत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8244)
- **Original**: सुप्ततिमप्रतिर्थं धुब॑ चाप्यन्तिनार: पुनत्नानवाप
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8245)
- **Original**: अप्रतिरथस्प कण्व: पुन्नो5भूत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8246)
- **Original**: तस्थाषि मेथातिथि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8247)
- **Original**: यतः काण्वायना द्विजा बभूवुः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8248)
- **Original**: अप्रतिरथ- स्थापरः पुत्रो5भूदैलीनः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8249)
- **Original**: ऐलीनस्य दुष्यन्ता- दाश्चत्वार: पुत्रा बभूवु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8250)
- **Original**: दुष्यन्ताशक्रवर्ती भरतो5भूत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8251)
- **Original**: यन्नामहेतुर्देवेड्लोको गीयते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8252)
- **Original**: माता भस्त्रा पितु: पुत्रो येन जात: स एब सः । भरस्व पुत्र दुष्यन्त मावमंस्थाइशकुन्तलाम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8253)
- **Original**: 12 रेतोधा: पुत्रों नयति नरदेव यमक्षयात्‌। त्व॑ चास्य धाता गर्भस्य सत्यमाह शकुन्तला
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8254)
- **Original**: 13 भरतस्य पत्नीज़्ये नव पुत्रा बभूवु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8255)
- **Original**: नैते ममानुरूपा इत्यभिहितास्तन्थातर: परित्याग- भ्रयात्तत्पुत्राज्ञधु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8256)
- **Original**: ततो5स्थ॒ वितथे पुत्रजन्मनि पुत्रार्थिनो मरुत्सोमयाजिनो दीर्घतमस: पाष्णर्यपास्तादबृहस्पतिवीर्यादुत्तथ्यपल्यां ममतायां समुत्पन्नो भरद्वाजाख्य: पुत्रो मरुद्धिर्दत्त:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8257)
- **Original**: श्रीपराशरजी बोले--पुरुफा पुत्र जनमेजय था। जनमेजयका प्रचिन्वान्‌, प्रचिन्वानका प्रवीर, प्रबीरका मनस्थु, मनस्थुका अभयद, अभयदका सुद्ु, सुद्युका बहुगत, बहुगतका संयाति, संयातिका अहंयाति तथा अहँयातिका पुत्र रौद्राश्च था
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8258)
- **Original**: रीद्राश्वके ऋतेषु, कक्षेषु, स्थप्डिलेखु, कृतेषु, जलेगु, शर्मेंषु, घृतेषु, स्थलेषु, सन्नतेषु और बनेषु नामक दस पुत्र थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8259)
- **Original**: ऋतेषुका पुत्र अन्तिनार हुआ तथा अत्तिनारके सुमति, अप्रतिरथ और धुव नामक तीन पुत्रोने जन्म लिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8260)
- **Original**: इनमेंसे अप्रतिरथका पूत्र कण्ब और कण्वका मेधातिथि हुआ जिसको सन्तान काण्जायन बाह्ण हुए
- **Translation**: 

---

