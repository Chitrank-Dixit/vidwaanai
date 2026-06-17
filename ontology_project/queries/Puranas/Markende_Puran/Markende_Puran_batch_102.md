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

### Verse 1 (Markende Puran 0.2021)
- **Original**: महाभाग सावर्णि भगवती पहामाथाके अयुप्रहमे मैं सेडन करता हूँ। ले अपने दस हाथोंमें खड्ण,
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2022)
- **Original**: जिस प्रकार मन्बन्तरके स्वामी हुए, चही प्रसद्ञ चक्र, गदा, बाण, धनुप, परिथ, झूल, भुशुण्डि, ' सुनाता हूँ
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2023)
- **Original**: पूर्वकालको बात हैं, स्वारोचिष मस्तक और शद्ब धारण करतों हैं। उनके तोन
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2024)
- **Original**: मन्चत्तरमें सुस्थ नामके एक राजा थे, जो चैत्रबशमें नेज् हैं। के समस्त अज्ञोंगें दिव्य आधू
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2025)
- **Original**: 4णोंसे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2026)
- **Original**: उत्पन्न हुए थे। उनका समस्त भूपण्डलपर अधिकार विभूषित हैं; उनके शरोरक्ती झान्ति नॉलमरणिके
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2027)
- **Original**: ये प्रजाका अपने औरस पुत्रोंकी भाँति समान हैं तधा त्रे दक्ष मुख और दक्ष पैरॉसे
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2028)
- **Original**: ध्रमंगूर्वक पालन करते थे; फिर भी उस समय युक्त हैं।]
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2029)
- **Original**: कौल्ाविध्कंसी' नामके क्षात्रय उनके शत्रु हो 6.3: अह्दीदेतौक्टें तमन्कार है। 2. कोलाबि थी वह किसी विशेष कछुललके धानिस को रांद्ां है। दक्षिणपें 'कौला' नएरों प्रसिद्ध हैं, वह चीन आतमें तण॑धानी थीं। जिन क्षत्रियोँगे उसपर >्पक्रांण करके इरूक। वित्वंत्त किला, ते ' कोलाविध्यंसो' कहत्गये:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2030)
- **Original**: शक * संक्षिप्त मार्कण्डेयपुराण « गये
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2031)
- **Original**: राजा सुरथकी दण्डनीति बड़ों प्रबल
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2032)
- **Original**: प्रत्युबाच्च स ते वैश्य; प्रश्रयाखनतो नृपम्‌
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2033)
- **Original**: थी! उनका शब्रुओंके साथ संग्राम हुआ। यद्यपि
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2034)
- **Original**: ण़जाका बल क्षीण हो चला था; इसलिये ऋोलाविध्व॑ंसी संख्यामें कम थे तो भी राजा सुरथ
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2035)
- **Original**: उनके दुष्ट, बलवान्‌ एवं दुरात्मा मन्त्रियोंने वहाँ चुद्धमें उनसे परास्‍््त हो गये
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2036)
- **Original**: तब ने युद्धभूमिसे
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2037)
- **Original**: उनकी राजधानीमें भी राजकीय सेना और खजानेको अपने उगरकों लौट आये और केवल अपने
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2038)
- **Original**: वहाँसे हथिया लिया
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2039)
- **Original**: सुरथका प्रभुत्व नष्ट हो देशके राजा होकर रहने लगे (सपूची पृथ्वीसे
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2040)
- **Original**: चुका था, इसलिये वे शिकार खेलनेके बहाने अब उनका अधिकार जाता रहा) किंतु यहाँ भी
- **Translation**: 

---

