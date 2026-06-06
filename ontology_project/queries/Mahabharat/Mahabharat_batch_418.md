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

### Verse 1 (Mahabharat 0.4171)
- **Original**: . भीमसेनने भी धनुष उठाया और बाणोंकी वर्षासे झत्रुके डालनेसे ही तुप्करी विजय होगी और मेरे हृदयका काँटा भी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4171)
- **Original**: . भीमसेनने भी धनुष उठाया और बाणोंकी वर्षासे झत्रुके डालनेसे ही तुप्करी विजय होगी और मेरे हृदयका काँटा भी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4172)
- **Original**: हाथीकों बहुत पीड़ित किया; इससे यह भाग. चला, निकल जायगा। इसलिये तुम इच्छानुसार अपनी सेनाकी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4172)
- **Original**: हाथीकों बहुत पीड़ित किया; इससे यह भाग. चला, निकल जायगा। इसलिये तुम इच्छानुसार अपनी सेनाकी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4173)
- **Original**: व्यूहर्वना करो ।' । भाईकौ बात सुनकर अ्जुनने झन्रुओंके मुकाबलेमें
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4173)
- **Original**: व्यूहर्वना करो ।' । भाईकौ बात सुनकर अ्जुनने झन्रुओंके मुकाबलेमें
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4174)
- **Original**: अपनी सेनाका >अर्थचन्भाकार व्यूह बनाया। उसके वाम
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4174)
- **Original**: अपनी सेनाका >अर्थचन्भाकार व्यूह बनाया। उसके वाम
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4175)
- **Original**: भागयें भीमसेन, दाहिने भागयें धृष्टयुप्र तथा मध्यमें राजा. युथ्चिष्ठिर और अर्जुन खड़े हुए। नकुछ और सहदेव--ये दोनों युथिष्ठिर्के पीछे थे। पदश्नालदेशीय युधामत्यु और उत्तमौजा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4175)
- **Original**: भागयें भीमसेन, दाहिने भागयें धृष्टयुप्र तथा मध्यमें राजा. युथ्चिष्ठिर और अर्जुन खड़े हुए। नकुछ और सहदेव--ये दोनों युथिष्ठिर्के पीछे थे। पदश्नालदेशीय युधामत्यु और उत्तमौजा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4176)
- **Original**: अर्जुनके पहियोंकी रक्षा करने लगे।-जझेष कीरोमेंसे जिन्हें
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4176)
- **Original**: अर्जुनके पहियोंकी रक्षा करने लगे।-जझेष कीरोमेंसे जिन्हें
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4177)
- **Original**: व्यूहमें जहाँ स्थान मिला; वे वहीं खूब उत्साहके साथ डट
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4177)
- **Original**: व्यूहमें जहाँ स्थान मिला; वे वहीं खूब उत्साहके साथ डट
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4178)
- **Original**: गये। इस प्रकार कौरथ तथा पाण्डवोने व्यूह बनाकर फिर
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4178)
- **Original**: गये। इस प्रकार कौरथ तथा पाण्डवोने व्यूह बनाकर फिर
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4179)
- **Original**: युद्धमें मर छूगाया। दोनों दलोंमें ऊैली आवाज करनेवाले
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4179)
- **Original**: युद्धमें मर छूगाया। दोनों दलोंमें ऊैली आवाज करनेवाले
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4180)
- **Original**: है बाजे बज उठे । विजयाभिल्‍्मषी शूरवीरोंका सिंहनाद सुनायी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4180)
- **Original**: है बाजे बज उठे । विजयाभिल्‍्मषी शूरवीरोंका सिंहनाद सुनायी
- **Translation**: 

---

