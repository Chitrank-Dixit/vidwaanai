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

### Verse 1 (Agni Puran 0.6581)
- **Original**: ही कर्म होते हैं। नाट्य-नृत्य आदिमें पादकर्मके अज्जलि, कपोत, कर्कट, स्वस्तिक, कटक, वर्धमान,
- **Translation**: 

---

### Verse 2 (Agni Puran 0.6582)
- **Original**: अनेक भेद होते हैं
- **Translation**: 

---

### Verse 3 (Agni Puran 0.6583)
- **Original**: 19--21
- **Translation**: 

---

### Verse 4 (Agni Puran 0.6584)
- **Original**: इस प्रकार आदि आरनेय महाएुराणमें “नृत्य आदियमें उप्रयोगी विभिन्न अज्ञॉंकी क्रियाओंका वरिरूपण' नामक तीन सौँ इकतालीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 5 (Agni Puran 0.6585)
- **Original**: 349 # तीन सौ बयालीसवां अध्याय अभिनय और अलंकारोंका निरूपण अग्निदेव कहते हैं-- वसिष्ठ
- **Translation**: 

---

### Verse 6 (Agni Puran 0.6586)
- **Original**: (काव्य! अथवा
- **Translation**: 

---

### Verse 7 (Agni Puran 0.6587)
- **Original**: है। उसके बिना सबकी स्वतन्त्रता व्यर्थ ही है। “नाटक़' आदियें वर्णित विषयोंको जो अभिमुख
- **Translation**: 

---

### Verse 8 (Agni Puran 0.6588)
- **Original**: 'सम्भोग' और “विप्रलम्भ'के भेदसे श्वृज्रार दो कर देता--सामने ला देता, अर्थात्‌ मूर्तरूपसे
- **Translation**: 

---

### Verse 9 (Agni Puran 0.6589)
- **Original**: प्रकारका माना जाता है। उनके भी '“प्रच्छन्न' एवं प्रत्यक्ष दिखा देता है, पात्रोंके उस कार्यकलापको
- **Translation**: 

---

### Verse 10 (Agni Puran 0.6590)
- **Original**: 'प्रकाश'-दो भेद होते हैं। विप्रलम्भ श्रृज्ञारके विद्वान्‌ पुरुष "अभिनय ' मानते या कहते हैं। वह
- **Translation**: 

---

### Verse 11 (Agni Puran 0.6591)
- **Original**: चार भेद माने जाते हैं--पूर्वानुराग, मान, प्रवास चार प्रकारसे सम्भव होता है। उन चारों अभिनयोंके
- **Translation**: 

---

### Verse 12 (Agni Puran 0.6592)
- **Original**: एवं करुणात्मक
- **Translation**: 

---

### Verse 13 (Agni Puran 0.6593)
- **Original**: नाम इस प्रकार हैं--सात्त्विक, वाचिक, आज्लिक
- **Translation**: 

---

### Verse 14 (Agni Puran 0.6594)
- **Original**: इन पूर्वानुरागादिसे 'सम्भोग' थ्रृज्ञारकी उत्पत्ति और आहार्य। स्तम्भ, स्वेद आदि “सात्त्विक
- **Translation**: 

---

### Verse 15 (Agni Puran 0.6595)
- **Original**: होती है। वह भी चार भागोंमें विभाजित होता है अभिनय ' हैं; वाणीसे जिसका आरम्भ होता है,
- **Translation**: 

---

### Verse 16 (Agni Puran 0.6596)
- **Original**: एवं पूर्वका अतिक्रमण नहीं करता। यह स्त्री और वह 'बाचिक अभिनय” है; शरीरसे आरम्भ किये
- **Translation**: 

---

### Verse 17 (Agni Puran 0.6597)
- **Original**: पुरुषका आश्रय लेकर स्थित होता है। उस जानेवाले अभिनयको “आज्लिक' कहते हैं तथा
- **Translation**: 

---

### Verse 18 (Agni Puran 0.6598)
- **Original**: श्रृज्जाररी साधिका अथवा अभिव्यञ्जिका 'रति' जिसका आरम्भ बुद्धिसे किया जाता है, वह
- **Translation**: 

---

### Verse 19 (Agni Puran 0.6599)
- **Original**: मानी गयी है। उसमें वैवर्ण्य और प्रलयके सिवा *आहार्य अभिनय” कहा गया है
- **Translation**: 

---

### Verse 20 (Agni Puran 0.6600)
- **Original**: अन्य सभी सात्त्विक' भावोंका उदय होता है। रसादिका आधान अभिमानकी सत्तासे होता
- **Translation**: 

---

