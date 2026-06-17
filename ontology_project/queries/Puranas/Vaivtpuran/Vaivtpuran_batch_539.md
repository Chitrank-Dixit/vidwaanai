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

### Verse 1 (Vaivtpuran 35.7882)
- **Original**: बारंबार प्रणाम है। दुर्गतिनाशिनीकों मेरा अभिवादन निषधराज, मगधाधिपति एवं कान्यकुब्ज, सौराष्ट्र, है। मायारूपा आपको मैं बारंबार सिर झुकाता राढीय, बारेन्‍्द्र, सौम्य बंगीय, महाराष्ट्र, गुर्जरजातीय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7883)
- **Original**: हूँ। जगद्धात्रीको नमस्कार-नमस्कार। जगत्कत्रीको और कलिंग आदिके सैकड़ों-सैकड़ों राजा बारह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7884)
- **Original**: पुन:-पुनः प्रणाम। जगज्जननीकों मेरा नमस्कार अक्षौहिणी सेनाके साथ आये; परंतु परशुरामजीने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 35.7885)
- **Original**: प्राप्त हो। कारणरूपा आपको बारंबार अभिवादन सबको रणभूमिमें सुला दिया। यह देखकर एक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 35.7886)
- **Original**: है। सृष्टिका संहार करनेवाली जगन्माता! प्रसन्न लाख नरपतियोंके साथ बारह अक्षौहिणी सेना
- **Translation**: 

---

### Verse 6 (Vaivtpuran 35.7887)
- **Original**: होइये। मैं आपके चरणोंकी शरण ग्रहण करता लेकर राजा सुचन्द्र रणस्थलमें आये। सुचन्रके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 35.7888)
- **Original**: हूँ, मेरी प्रतिज्ञा सफल कीजिये। मेंरे प्रति आपके साथ भयानक युद्ध हुआ, पर वे परास्त न हो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 35.7889)
- **Original**: विमुख हो जानेपर कौन मेरी रक्षा कर सकता सके। तब परशुरामने देखा कि मुण्डमाला धारण
- **Translation**: 

---

### Verse 9 (Vaivtpuran 35.7890)
- **Original**: है? भक्तवत्सले! शुभ! आप मुझ भक्तपर कृपा किये हुए विकटानना भयंकरी जगज्जननी भद्रकाली
- **Translation**: 

---

### Verse 10 (Vaivtpuran 35.7891)
- **Original**: कीजिये। सुमुखि! पहले शिवलोकमें आपलोगोंने उनकी रक्षा कर रही हैं। यह देखकर परशुरामने मुझे जो वरदान दिया था, उस वरको आपको शस्त्रास्त्रका त्याग करके महामायाकी स्तुति
- **Translation**: 

---

### Verse 11 (Vaivtpuran 35.7892)
- **Original**: सफल करना चाहिये। मां रुद्रो नैऋत्यां स्थाणुरेव च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 35.7893)
- **Original**: पातु आरम्भ कौ। परशुरामद्वारा किये गये इस स्तवनको सुनकर _ /्जरख 7 ल रर टंटपएखए/पफ पफै:ख:7ण7"ोएएफ 3 हों श्रीं क्लीं ऐँ स्द्राय स्वाहा नार्भि सदाउवतु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 35.7894)
- **Original**: 3# हों ऐं. श्री इंश्वराय स्वाहा पृष्ठ॑सदाउबतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7895)
- **Original**: & हीं क्लीं मृत्युकयाय स्वाहा भ्रृश्व सदाउवतु। 3 हाँ श्रीं क्लौं ईशानाय स्वाहा पाश्व॑ सदाउवतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7896)
- **Original**: 35% हीं ईश्वराय स्वाहा उदर॑ पातु मे सदा। 30 श्रीं क्लीं मृत्युअयाय स्वाहा बादू सदाउञतु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7897)
- **Original**: 3 हाँ श्रीं क्लीं ईश्वराय स्वाहा पातु करों मम्र
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7898)
- **Original**: 3* महेश्वराय रुद्राय नितम्बं॑ पातु में सदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7899)
- **Original**: 3 हीं श्रों भूतनाथाय स्वाहा पादौ । % सर्वेश्वराय सर्वाय स्वाहा सर्व सदाउवतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7900)
- **Original**: कबचं काण्वशाखोक्तमतिगोप्यं सुदुर्लभम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7901)
- **Original**: अश्वमेधसहस्ताणि राजसूयशतानि च । सर्वाणि कवचस्यास्थ कलां नाहन्ति षोडशीम्‌
- **Translation**: 

---

