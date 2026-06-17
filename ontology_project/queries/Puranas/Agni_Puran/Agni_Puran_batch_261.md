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

### Verse 1 (Agni Puran 0.5201)
- **Original**: (बावली)-का निर्माण करावे और उसमें नदीके आवास-स्थानके आसपास उद्यानका निर्माण करे
- **Translation**: 

---

### Verse 2 (Agni Puran 0.5202)
- **Original**: प्रवाहका प्रवेश करावे। जलाशयारम्भके लिये अथवा सब ओरका भाग पुष्पित तिलोंसे सुशोभित
- **Translation**: 

---

### Verse 3 (Agni Puran 0.5203)
- **Original**: हस्त, मघा, अनुराधा, पुष्य, ज्येष्ठा, शतभिषा,
- **Translation**: 

---

### Verse 4 (Agni Puran 0.5204)
- **Original**: 570 + अग्निपुराण * उत्तराषाढ़ा, उत्तरा-भाद्रपदा और उत्तरा-फाल्गुनी
- **Translation**: 

---

### Verse 5 (Agni Puran 0.5205)
- **Original**: फिर विडज़, घृत और पड्ड-मिश्रित शीतल नक्षत्र उपयुक्त हैं
- **Translation**: 

---

### Verse 6 (Agni Puran 0.5206)
- **Original**: जलसे उनको सींचे। वृक्षोंके फलोंका नाश वरुण, विष्णु और इन्द्रका पूजन करके इस
- **Translation**: 

---

### Verse 7 (Agni Puran 0.5207)
- **Original**: होनेपर कुलथी, उड़द, मूँग, जौ, तिल और घृतसे कर्मको आरम्भ करे। नीम, अशोक, पुन्नाग
- **Translation**: 

---

### Verse 8 (Agni Puran 0.5208)
- **Original**: मिश्रित शीतल जलके द्वारा यदि सेचन किया (नागकेसर), शिरीष, प्रियक्रु, अशोक', कदली
- **Translation**: 

---

### Verse 9 (Agni Puran 0.5209)
- **Original**: जाय तो वृक्षोंमें सदा फलों एवं पुष्पोंकी वृद्धि (केला), जम्बयू (जामुन), वकुल (मौलसिरी)
- **Translation**: 

---

### Verse 10 (Agni Puran 0.5210)
- **Original**: होती है। भेड़ और बकरीकी विष्ठाका चूर्ण, और अनार वृक्षॉंका आरोपण करके ग्रीष्म-ऋतुमें
- **Translation**: 

---

### Verse 11 (Agni Puran 0.5211)
- **Original**: जौका चूर्ण, तिल और जल-इनको एकत्र करके प्रातःकाल और सायंकाल, शीत-ऋतुमें दिनके
- **Translation**: 

---

### Verse 12 (Agni Puran 0.5212)
- **Original**: सात दिनतक एक स्थानपर रखे। उसके बाद समय एवं वर्षा-ऋतुमें रात्रिके समय भूमिके सूख
- **Translation**: 

---

### Verse 13 (Agni Puran 0.5213)
- **Original**: इससे सींचना सभी वृक्षोंके फल और पुष्पोंको जानेपर वृक्षोंको सींचे। वृक्षोंके मध्यमें बीस
- **Translation**: 

---

### Verse 14 (Agni Puran 0.5214)
- **Original**: बढ़ानेवाला है
- **Translation**: 

---

### Verse 15 (Agni Puran 0.5215)
- **Original**: 10--12
- **Translation**: 

---

### Verse 16 (Agni Puran 0.5216)
- **Original**: हाथका अन्तर “उत्तम', सोलह हाथका अन्तर
- **Translation**: 

---

### Verse 17 (Agni Puran 0.5217)
- **Original**: [ मछलीके जल (जिसमें मछली रहती हों)-से “मध्यम” और बारह हाथका अन्तर 'अधम' कहा
- **Translation**: 

---

### Verse 18 (Agni Puran 0.5218)
- **Original**: सींचनेपर वृक्षोंकी वृद्धि होती है। विडंगचाबलके गया है। बारह हाथ अन्तरवाले वृक्षोंकों स्थानान्तरित
- **Translation**: 

---

### Verse 19 (Agni Puran 0.5219)
- **Original**: साथ यह जल वृक्षोंका दोहद (अभिलषित- कर देना चाहिये। घने वृक्ष फलहीन होते हैं।
- **Translation**: 

---

### Verse 20 (Agni Puran 0.5220)
- **Original**: पदार्थ) है। इसका सेचन साधारणतया सभी वृक्ष- पहले उन्हें काट-छाँटकर शुद्ध करे
- **Translation**: 

---

