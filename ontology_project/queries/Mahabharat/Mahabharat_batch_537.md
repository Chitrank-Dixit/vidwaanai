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

### Verse 1 (Mahabharat 0.5361)
- **Original**: सबको युद्धभूमिमें यथास्थान खड़ा किया। फिर कृपाचार्य,
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5361)
- **Original**: सबको युद्धभूमिमें यथास्थान खड़ा किया। फिर कृपाचार्य,
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5362)
- **Original**: कृतवर्मा, अश्वस्थामा, झाल्य, झकुनि तथा अन्य राजाओंने
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5362)
- **Original**: कृतवर्मा, अश्वस्थामा, झाल्य, झकुनि तथा अन्य राजाओंने
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5363)
- **Original**: मिलकर यह झपथ ली कि “हममेंसे कोई भी अकेला होकर पाण्डबोंसे न छड़े, जो अकेर्त्ा ही उनसे लड़ेगा अथवा जो किसी लड़ते हुए योड्धाको अकेला छोड़ देगा, उसे पाँच
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5363)
- **Original**: मिलकर यह झपथ ली कि “हममेंसे कोई भी अकेला होकर पाण्डबोंसे न छड़े, जो अकेर्त्ा ही उनसे लड़ेगा अथवा जो किसी लड़ते हुए योड्धाको अकेला छोड़ देगा, उसे पाँच
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5364)
- **Original**: महापातक और पाँच उपपातक लगेंगे। इसलिये सब एक-
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5364)
- **Original**: महापातक और पाँच उपपातक लगेंगे। इसलिये सब एक-
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5365)
- **Original**: दूसरेकी रक्षा करते हुए साथ रहकर युद्ध करें। । इस प्रकार शपथ लेकर समस्त पहारथ्ियोंने मग्रराजको 5 - आगे किया और बड़ी झीप्रताके साथ झत्रुओंपर चढ़ाई कर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5365)
- **Original**: दूसरेकी रक्षा करते हुए साथ रहकर युद्ध करें। । इस प्रकार शपथ लेकर समस्त पहारथ्ियोंने मग्रराजको 5 - आगे किया और बड़ी झीप्रताके साथ झत्रुओंपर चढ़ाई कर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5366)
- **Original**: इच्छासे कोरवोंपर चढ़ आये। उनकी सेना क्षुब्ध हुए समुद्रकी
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5366)
- **Original**: इच्छासे कोरवोंपर चढ़ आये। उनकी सेना क्षुब्ध हुए समुद्रकी
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5367)
- **Original**: 98 संक्षिप्त महाभारत [ झल्यपर्व भाँति गर्जना कर रही थी। पाण्डबॉका सिंहनाद सुनकर
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5367)
- **Original**: 98 संक्षिप्त महाभारत [ झल्यपर्व भाँति गर्जना कर रही थी। पाण्डबॉका सिंहनाद सुनकर
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5368)
- **Original**: धर्मराजको आगे करके झल्यपर धावा कर दिया। आपके पुत्रोंके मनमें भय समा गया। तब मद्धराज झल्यने
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5368)
- **Original**: धर्मराजको आगे करके झल्यपर धावा कर दिया। आपके पुत्रोंके मनमें भय समा गया। तब मद्धराज झल्यने
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5369)
- **Original**: माद्दीकुमार नकुछ और सहदेव भी आपकी सेनापर टूट पड़े। उन्हें धीरज बैंधाया और सर्वतोभद्र नामक व्यूह बनाकर
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5369)
- **Original**: माद्दीकुमार नकुछ और सहदेव भी आपकी सेनापर टूट पड़े। उन्हें धीरज बैंधाया और सर्वतोभद्र नामक व्यूह बनाकर
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5370)
- **Original**: फिर पाण्डवॉने कौस्व-सेनाको अपने बाणोंसे बहुत घायल पाण्डवॉंके ऊपर धावा किया। उस समय वे सिन्धुदेशके
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5370)
- **Original**: फिर पाण्डवॉने कौस्व-सेनाको अपने बाणोंसे बहुत घायल पाण्डवॉंके ऊपर धावा किया। उस समय वे सिन्धुदेशके
- **Translation**: 

---

