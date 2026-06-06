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

### Verse 1 (Mahabharat 0.4301)
- **Original**: अहारसे अद्वराजको पीड़ित करके फिर सौ जाणोंसे उसके और पाझ्नाल योद्धा तेज किये हुए अख-झख् लेकर गर्जना
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4301)
- **Original**: अहारसे अद्वराजको पीड़ित करके फिर सौ जाणोंसे उसके और पाझ्नाल योद्धा तेज किये हुए अख-झख् लेकर गर्जना
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4302)
- **Original**: हंधीको भी घायल किया। तब आडराजने नकुलपर एक सौ करते हुए वहाँ आ पहुँचे और उतर हाथियोंपर बाणोंकी बौछार करने छगे। नकुछ, सहदेव, ड्रोपदीके पुत्र, प्रभवद्रक, सात्यकि, झिखण्डी तथा चेकितान--ये सभी वीर चारों ओरसे याणोंकी झड़ी छगाने छगे। आठ तोमरोंका प्रहार किया, किंतु उसने प्रत्येक तोमरके
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4302)
- **Original**: हंधीको भी घायल किया। तब आडराजने नकुलपर एक सौ करते हुए वहाँ आ पहुँचे और उतर हाथियोंपर बाणोंकी बौछार करने छगे। नकुछ, सहदेव, ड्रोपदीके पुत्र, प्रभवद्रक, सात्यकि, झिखण्डी तथा चेकितान--ये सभी वीर चारों ओरसे याणोंकी झड़ी छगाने छगे। आठ तोमरोंका प्रहार किया, किंतु उसने प्रत्येक तोमरके
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4303)
- **Original**: वीन-सीन टुकड़े कर डाले और एक अर्धचन्द्राकार बाण मारकर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4303)
- **Original**: वीन-सीन टुकड़े कर डाले और एक अर्धचन्द्राकार बाण मारकर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4304)
- **Original**: उसके मस्तकको भी काट लिया। फिर तो बह म्लेक्फराज
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4304)
- **Original**: उसके मस्तकको भी काट लिया। फिर तो बह म्लेक्फराज
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4305)
- **Original**: हाथीके साथ ही भूमिपर गिर पड़ा।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4305)
- **Original**: हाथीके साथ ही भूमिपर गिर पड़ा।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4306)
- **Original**: उनके साथ ही मेकल, उत्कल, कलिड्र, निषथ तथा तात्रलिप
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4306)
- **Original**: उनके साथ ही मेकल, उत्कल, कलिड्र, निषथ तथा तात्रलिप
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4307)
- **Original**: आदि देझोंके योद्धा भी नकुछकों मार डालनेकी इच्छासे उसपर
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4307)
- **Original**: आदि देझोंके योद्धा भी नकुछकों मार डालनेकी इच्छासे उसपर
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4308)
- **Original**: थाणों और तोमरोंकी वर्षा करने लगे। उन सबके अखोंकी
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4308)
- **Original**: थाणों और तोमरोंकी वर्षा करने लगे। उन सबके अखोंकी
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4309)
- **Original**: बौछारसे नकुछकों ढक गया देख पाष्डव, पाञ्ाल और सोमक
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4309)
- **Original**: बौछारसे नकुछकों ढक गया देख पाष्डव, पाञ्ाल और सोमक
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4310)
- **Original**: क्षत्रिय बड़े क्रोधमें भरकर वहाँ आ पहुँचे । फिर तो पाष्डवपक्षके रथी बीरोंका उन हाथियोंके साथ घोर युद्ध होने लगा। उन्होंने
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4310)
- **Original**: क्षत्रिय बड़े क्रोधमें भरकर वहाँ आ पहुँचे । फिर तो पाष्डवपक्षके रथी बीरोंका उन हाथियोंके साथ घोर युद्ध होने लगा। उन्होंने
- **Translation**: 

---

