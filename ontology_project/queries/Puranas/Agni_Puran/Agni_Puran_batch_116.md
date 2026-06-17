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

### Verse 1 (Agni Puran 0.2301)
- **Original**: दण्डकारण्य भी उत्तम तोर्थ हैं। कालंजर, मुझवट, भी क्यों न हों, सर्वत्र स्वर्गलोककी प्राप्ति करानेवाली
- **Translation**: 

---

### Verse 2 (Agni Puran 0.2302)
- **Original**: शूर्पारक, मन्दाकिनी, चित्रकूट और श्रृड्अवेरपुर हैं। राजगृह पवित्र तीर्थ है। शालग्राम तीर्थ
- **Translation**: 

---

### Verse 3 (Agni Puran 0.2303)
- **Original**: श्रेष्ठ तीर्थ हैं। अवन्ती भी उत्तम तीर्थ है। अयोध्या प्रापोंका नाश करनेवाला है। वटेश, बामन तथा
- **Translation**: 

---

### Verse 4 (Agni Puran 0.2304)
- **Original**: सब पापोंका नाश करनेवाली है। नैमिषारण्य परम कालिका-संगम तीर्थ भी उत्तम हैं
- **Translation**: 

---

### Verse 5 (Agni Puran 0.2305)
- **Original**: 18--20
- **Translation**: 

---

### Verse 6 (Agni Puran 0.2306)
- **Original**: पवित्र तीर्थ है। वह भोग और मोक्ष प्रदान लौहित्य-तोर्थ, करतोया नदी, शोणभद्र तथा
- **Translation**: 

---

### Verse 7 (Agni Puran 0.2307)
- **Original**: करनेबाला है
- **Translation**: 

---

### Verse 8 (Agni Puran 0.2308)
- **Original**: 21--24
- **Translation**: 

---

### Verse 9 (Agni Puran 0.2309)
- **Original**: 8 इस ग्रकार आदि आग्लेव महापुराणमें 'तीर्थमाहात्म्य-वर्णत” नामक एक सा नाँवाँ अध्याय पूदा हुआ
- **Translation**: 

---

### Verse 10 (Agni Puran 0.2310)
- **Original**: 109 # एक सौ दसवाँ अध्याय गड़्ाजीकी महिमा अग्निदेव कहते हैं-- अब गद्जाका माहात्म्यम
- **Translation**: 

---

### Verse 11 (Agni Puran 0.2311)
- **Original**: गज्जादेवी सब पापोंकों दूर करनेवाली तथा बतलाता हूँ। गड्भाका सदा सेवन करना चाहिये।
- **Translation**: 

---

### Verse 12 (Agni Puran 0.2312)
- **Original**: स्वर्गलोक देनेवाली हैं। गड्भाके जलमें जबतक खह भोग और मोक्ष प्रदान करनेवाली हैं। जिनके
- **Translation**: 

---

### Verse 13 (Agni Puran 0.2313)
- **Original**: हड्डी पड़ी रहती है, तबतक वह जीव स्वर्गमें जीचसे गड्भा बहती हैं, वे सभी देश श्रेष्ठ तथा
- **Translation**: 

---

### Verse 14 (Agni Puran 0.2314)
- **Original**: निवास करता है। अंधे आदि भी गड्जाजीका पावन हैं। उत्तम गतिकी खोज करनेवाले प्राणियोंक
- **Translation**: 

---

### Verse 15 (Agni Puran 0.2315)
- **Original**: सेवन करके देवताओंके समान हो जाते हैं। लिये गड्ढा ही सर्वोत्तम गति है। गड्जाका सेवन
- **Translation**: 

---

### Verse 16 (Agni Puran 0.2316)
- **Original**: गड्जा-तीर्थसे निकली हुई मिट्टी धारण करनेवाला करनेपर वह माता और पिता-दोनोंके कुलोंका
- **Translation**: 

---

### Verse 17 (Agni Puran 0.2317)
- **Original**: मनुष्य सूर्यके समान पापोंका नाशक होता है। जो उद्धार करती है। एक हजार चान्द्रायण-व्रतकी
- **Translation**: 

---

### Verse 18 (Agni Puran 0.2318)
- **Original**: मानव गज्जाका दर्शन, स्पर्श, जलपान अथवा अपेक्षा गड्भजाजीके जलका पीना उत्तम है। एक
- **Translation**: 

---

### Verse 19 (Agni Puran 0.2319)
- **Original**: “गड्जा' इस नामका कीर्तन करता है, वह अपनी मास गड्जाजीका सेवन करनेवाला मनुष्य सब
- **Translation**: 

---

### Verse 20 (Agni Puran 0.2320)
- **Original**: सैकड़ों-हजारों पीढ़ियोंके पुरुषोंकों पवित्र कर यज्ञोंका फल पाता है
- **Translation**: 

---

