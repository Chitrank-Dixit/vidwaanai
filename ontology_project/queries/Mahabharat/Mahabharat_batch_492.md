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

### Verse 1 (Mahabharat 0.4911)
- **Original**: ... सज़यने कहा--राजन्‌ ! उस समय अर्जुन घोड़े औरे सारथिसहित रथों, सवारसहित हाथियों और घोड़ों। पैदलों एवं संम्पूर्ण शाुओंकों अपने बाण-समूहोंकी मारसे मृत्दुके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4911)
- **Original**: ... सज़यने कहा--राजन्‌ ! उस समय अर्जुन घोड़े औरे सारथिसहित रथों, सवारसहित हाथियों और घोड़ों। पैदलों एवं संम्पूर्ण शाुओंकों अपने बाण-समूहोंकी मारसे मृत्दुके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4912)
- **Original**: अधीन करने रूगे। उनके पहुँचनेके पहले कृपाचार्य और छूटे हुए बाण कर्णको मौतके घाट उत्ारेंगे। कृष्ण ! मैं आपसे सद्ची बात बता रहा हूँ, आज कर्णके मारे जानेसे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4912)
- **Original**: अधीन करने रूगे। उनके पहुँचनेके पहले कृपाचार्य और छूटे हुए बाण कर्णको मौतके घाट उत्ारेंगे। कृष्ण ! मैं आपसे सद्ची बात बता रहा हूँ, आज कर्णके मारे जानेसे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4913)
- **Original**: दुर्घोधन अपने राज्य और जीवन--दोनोंसे निराश हो जायगा। मेरे बाणोंसे कर्णके दुकड़े-टुकड़े हुए देख आज
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4913)
- **Original**: दुर्घोधन अपने राज्य और जीवन--दोनोंसे निराश हो जायगा। मेरे बाणोंसे कर्णके दुकड़े-टुकड़े हुए देख आज
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4914)
- **Original**: राजा दुर्योधन आपके उन वचनोंकों स्मरण करे, जिन्हें आपने
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4914)
- **Original**: राजा दुर्योधन आपके उन वचनोंकों स्मरण करे, जिन्हें आपने
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4915)
- **Original**: उसकी भल्ताईके लिये कहा था। कौरवोंकी सभामें पाण्डवॉंकी निन्‍्दा करते हुए कर्णने द्रोपदीसे जो कठोर बातें. कहीं थी, उनके लिये आज उसे खूब पञश्चाताप होगा। आज
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4915)
- **Original**: उसकी भल्ताईके लिये कहा था। कौरवोंकी सभामें पाण्डवॉंकी निन्‍्दा करते हुए कर्णने द्रोपदीसे जो कठोर बातें. कहीं थी, उनके लिये आज उसे खूब पञश्चाताप होगा। आज
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4916)
- **Original**: कर्णके मारे जानेपर घृतराष्ट्रके सभी पुत्र राजा दुर्योधनके . साथ इस तरह भयभीत होकर भागेंगे, जैसे सिंहसे डरे हुए
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4916)
- **Original**: कर्णके मारे जानेपर घृतराष्ट्रके सभी पुत्र राजा दुर्योधनके . साथ इस तरह भयभीत होकर भागेंगे, जैसे सिंहसे डरे हुए
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4917)
- **Original**: मृग भागते हैं। कर्णके पुत्र और मित्रोंको भी आज जीवित
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4917)
- **Original**: मृग भागते हैं। कर्णके पुत्र और मित्रोंको भी आज जीवित
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4918)
- **Original**: नहीं रहनें दूँगा। सृतपुत्रकी मौत देखकर राजा दुर्योधन अब
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4918)
- **Original**: नहीं रहनें दूँगा। सृतपुत्रकी मौत देखकर राजा दुर्योधन अब
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4919)
- **Original**: अपने लिये चिन्ता करें। आज राजा थृतराष्रको उनके
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4919)
- **Original**: अपने लिये चिन्ता करें। आज राजा थृतराष्रको उनके
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4920)
- **Original**: पुत्र-पौत्र, मन्त्री तथा सेवकॉसहित्‌ राज्यकी ओरसे निराश
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4920)
- **Original**: पुत्र-पौत्र, मन्त्री तथा सेवकॉसहित्‌ राज्यकी ओरसे निराश
- **Translation**: 

---

