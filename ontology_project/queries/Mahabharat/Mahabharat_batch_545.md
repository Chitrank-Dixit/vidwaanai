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

### Verse 1 (Mahabharat 0.5441)
- **Original**: पाण्डव-योद्धा भी सिंहनाद करते हुए दुर्योधन आदि कौरवॉपर चढ़ आये। उस समंय आपके पुत्रने एक प्रास
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5441)
- **Original**: पाण्डव-योद्धा भी सिंहनाद करते हुए दुर्योधन आदि कौरवॉपर चढ़ आये। उस समंय आपके पुत्रने एक प्रास
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5442)
- **Original**: मारकर चेकितानकी छाती चीर डाली, वह खूनसे नहा उठा
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5442)
- **Original**: मारकर चेकितानकी छाती चीर डाली, वह खूनसे नहा उठा
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5443)
- **Original**: और प्राणहीन होकर रथकी बैठकमें गिर पड़ा।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5443)
- **Original**: और प्राणहीन होकर रथकी बैठकमें गिर पड़ा।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5444)
- **Original**: है0रे संक्षिप्त महाभारत । [ अल्यपर्य
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5444)
- **Original**: है0रे संक्षिप्त महाभारत । [ अल्यपर्य
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5445)
- **Original**: थे, उप्त समय उनके ऊपर युधिष्ठिस्ते अनेकों तीक्षण बाणोंका आपकी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5445)
- **Original**: थे, उप्त समय उनके ऊपर युधिष्ठिस्ते अनेकों तीक्षण बाणोंका आपकी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5446)
- **Original**: भीम, नकुछ और सहदेब--इसमेंसे हर एकको. पौँच-पौँच करने लगे तथा कृषाचार्य, कृतवर्मा और झकुनि--ये
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5446)
- **Original**: भीम, नकुछ और सहदेब--इसमेंसे हर एकको. पौँच-पौँच करने लगे तथा कृषाचार्य, कृतवर्मा और झकुनि--ये
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5447)
- **Original**: बाणोंसे घायछ कर दिया। फिर युधिष्ठिस्की छातीपर मद्॒राजको आगे करके धर्मराज युधिष्विस्से युद्ध करने छगे।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5447)
- **Original**: बाणोंसे घायछ कर दिया। फिर युधिष्ठिस्की छातीपर मद्॒राजको आगे करके धर्मराज युधिष्विस्से युद्ध करने छगे।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5448)
- **Original**: बाणोंका जाल-सा फैलाकर उन्हें खूब पीड़ित किया। क्+ औ-- राजा शल्यका पराक्रम, अर्जुन-अश्वत्थामाका युद्ध तथा राजा सुरथका वध सज़य कहते हैं--महाराज ! मद्रराज शल्य जब
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5448)
- **Original**: बाणोंका जाल-सा फैलाकर उन्हें खूब पीड़ित किया। क्+ औ-- राजा शल्यका पराक्रम, अर्जुन-अश्वत्थामाका युद्ध तथा राजा सुरथका वध सज़य कहते हैं--महाराज ! मद्रराज शल्य जब
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5449)
- **Original**: दिया। तदनन्तर, भीमसेनने सत्तर, सात्यकिने नौ तथा युधिप्ठिस्को पीड़ा देने लगे, उस समय सात्यकि, भीमसेन,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5449)
- **Original**: दिया। तदनन्तर, भीमसेनने सत्तर, सात्यकिने नौ तथा युधिप्ठिस्को पीड़ा देने लगे, उस समय सात्यकि, भीमसेन,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5450)
- **Original**: धर्मराजने साठ बाण मारे। फिर झल्यने भी प्रत्येकको नकुछ और सहदेवने आकर शल्यको घेर लिया और उउ्हें
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5450)
- **Original**: धर्मराजने साठ बाण मारे। फिर झल्यने भी प्रत्येकको नकुछ और सहदेवने आकर शल्यको घेर लिया और उउ्हें
- **Translation**: 

---

