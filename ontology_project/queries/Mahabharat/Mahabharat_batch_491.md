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

### Verse 1 (Mahabharat 0.4901)
- **Original**: कर्ण रणभूमिमें निर्भय-सा विचरता-है। उस प्रज्वलित आप मेरे स्वामी एवं संरक्षक हैं तो मेरी विजय निश्चित है।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4901)
- **Original**: कर्ण रणभूमिमें निर्भय-सा विचरता-है। उस प्रज्वलित आप मेरे स्वामी एवं संरक्षक हैं तो मेरी विजय निश्चित है।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4902)
- **Original**: भार्गवाख्ककी ओर भी मेरी दृष्टि है, जिसे कर्णने प्रकट किया संसारके' भूत और धविष्यका निर्माण आपके हाथमें है,
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4902)
- **Original**: भार्गवाख्ककी ओर भी मेरी दृष्टि है, जिसे कर्णने प्रकट किया संसारके' भूत और धविष्यका निर्माण आपके हाथमें है,
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4903)
- **Original**: है। निक्षय ही, यह बह संग्राम है, जहाँ कर्ण मेरे हाथसे मारा जिसपर आप प्रसन्न हैं, उसकी विजयमें क्‍या संदेह है?
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4903)
- **Original**: है। निक्षय ही, यह बह संग्राम है, जहाँ कर्ण मेरे हाथसे मारा जिसपर आप प्रसन्न हैं, उसकी विजयमें क्‍या संदेह है?
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4904)
- **Original**: जायगा और जबतक यह पृथ्वी कायम रहेगी, तबतक समस्त कृष्णा !; कर्णकी तो बात ही क्‍या है? आपकी सहायता
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4904)
- **Original**: जायगा और जबतक यह पृथ्वी कायम रहेगी, तबतक समस्त कृष्णा !; कर्णकी तो बात ही क्‍या है? आपकी सहायता
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4905)
- **Original**: प्राणी इस बातकी चर्चा करेंगे। आज मेरे गाण्डीब धनुष्से
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4905)
- **Original**: प्राणी इस बातकी चर्चा करेंगे। आज मेरे गाण्डीब धनुष्से
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4906)
- **Original**: संक्षिप्त महाभारत [ कर्णपर्त
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4906)
- **Original**: संक्षिप्त महाभारत [ कर्णपर्त
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4907)
- **Original**: कर्णके मस्तककों धड़से अलग कर देना। +
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4907)
- **Original**: कर्णके मस्तककों धड़से अलग कर देना। +
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4908)
- **Original**: घृठराह्ने पूछ--सद्भय ! मेरे पुत्रों तथा पाण्डब-सुक्षयोमें
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4908)
- **Original**: घृठराह्ने पूछ--सद्भय ! मेरे पुत्रों तथा पाण्डब-सुक्षयोमें
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4909)
- **Original**: पहलेसे हो महाभयंकर संग्राम छिड़ा हुआ था । फिर जब अर्जुन
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4909)
- **Original**: पहलेसे हो महाभयंकर संग्राम छिड़ा हुआ था । फिर जब अर्जुन
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4910)
- **Original**: यहाँ आ पहुँचे तो युद्धकां स्वरूप कैसा हो गया ?
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4910)
- **Original**: यहाँ आ पहुँचे तो युद्धकां स्वरूप कैसा हो गया ?
- **Translation**: 

---

