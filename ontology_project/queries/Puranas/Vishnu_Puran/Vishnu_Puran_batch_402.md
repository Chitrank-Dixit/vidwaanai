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

### Verse 1 (Vishnu Puran 0.8021)
- **Original**: तस्याश्व सपल्नी माद्री नामाभूत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8022)
- **Original**: तस्यां च नासत्यदस्नाभ्यां नकुछसहदेबो पाण्डो: पुत्रो जनितो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8023)
- **Original**: श्रुतदेवां तु वृद्धर्मा नाम कारूश उपयेमे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8024)
- **Original**: तस्‍्याँ चर दन्तवक़रो नाम महासुरो जज्ञे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8025)
- **Original**: श्रुतकीर्तिमपि केकयराज उपयेमे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8026)
- **Original**: तस्यां च सन्तर्दनादय: कैकेया: पञ्ञ पुत्रा बभूतरु:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8027)
- **Original**: राजाधिदेव्यामावन्त्यौ विन्दानु- किन्दो जज्ञाते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8028)
- **Original**: श्रुतश्रवसमपि चेदिराजो दमघोषनामोपयेमे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8029)
- **Original**: तस्याँ च शिशुपाल- मुत्पादयामास
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8030)
- **Original**: सवा दैत्यानामादिपुरुषो हिरण्यकशिपुरभवत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8031)
- **Original**: श्रीविष्णुपुराण [ अब शेड भजमानका पुत्र विदूरथ हुआ; विदूरथके शुर, शुरके जामी, शामीके प्रतिक्षत्र, प्रतिक्षन्रके स्वयेभोज, स्वयंभोजके हृदिक तथा हृदिकके कृतवर्मा, झतधन्वा, देवाह और देवगर्भ आदि पुत्र हुए। देवगर्भके पुत्र श्रसेन थे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8032)
- **Original**: 22--27
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8033)
- **Original**: चुरसेनकी मारिषा मामकी पत्नी थी। उससे उन्होंने वसुदेख आदि दस पुत्र उत्पन्न किये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8034)
- **Original**: बसुदेवके जन्म लेते ही देवताओंने अपनों अन्याहत दृष्टिसे यह देखकर कि इनके घरमें भगवान्‌ अंशावतार लेंगे, आनक और दुन्दुधि आदि बाजे बजाये *
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8035)
- **Original**: इसीलिये इनका नाम आनकदुन्दुभि भी हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8036)
- **Original**: इनके देवभाग, देबत्रना, अष्टक, कऊुचक्र, वत्सधारक, सृञ्ञय, स्याम, शक और गण्डूष नासक नौ भाई थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8037)
- **Original**: तथा इन वसुदेव आदि दस भाइसॉकी पृथा, श्रुतदेवा, श्रुतकीर्ति, श्रुतश्रवा और राजाधिदेयी ये पाँच बहिनें थों
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8038)
- **Original**: शुरसेनके कुन्ति नामक एक मित्र थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8039)
- **Original**: से निःसन्तान थे, अतः शूरसेनने दत्तक-विधिसे उन्हें अपनी पृथा नामकी कन्या दे दी थी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8040)
- **Original**: उसका राजा पाण्डुके साथ विवाह हुआ
- **Translation**: 

---

