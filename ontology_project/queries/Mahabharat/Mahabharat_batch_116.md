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

### Verse 1 (Mahabharat 0.1151)
- **Original**: पोमसेटकों हतुमार॒जोसे छेट और बालचीत 267 जितेनिय और पत्ित्नात्पा युधिष्ठिर अपने भाइयोंके सहित
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1151)
- **Original**: पोमसेटकों हतुमार॒जोसे छेट और बालचीत 267 जितेनिय और पत्ित्नात्पा युधिष्ठिर अपने भाइयोंके सहित
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1152)
- **Original**: सत्कार स्वीकार किया । फिर भीमसेन आदि धाइयोंने ड्रोपदी उन महर्षियोंके पास गये। वे सब दिव्य ज्ञानसम्पन्न थे। उन्होंने
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1152)
- **Original**: सत्कार स्वीकार किया । फिर भीमसेन आदि धाइयोंने ड्रोपदी उन महर्षियोंके पास गये। वे सब दिव्य ज्ञानसम्पन्न थे। उन्होंने
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1153)
- **Original**: और वेद-बेदाडमें पारज्त सहस्तों ब्राह्मणोंके सहित उस जब महाराज युधिष्ठिरको अपने आश्रममें आते देखा तो वे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1153)
- **Original**: और वेद-बेदाडमें पारज्त सहस्तों ब्राह्मणोंके सहित उस जब महाराज युधिष्ठिरको अपने आश्रममें आते देखा तो वे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1154)
- **Original**: मनोरप और पवित्र आश्रममें प्रवेश किया। यह साक्षात्‌ अन्न होकर आशीवाँद देते हुए उनका स्वागत करनेके लिये
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1154)
- **Original**: मनोरप और पवित्र आश्रममें प्रवेश किया। यह साक्षात्‌ अन्न होकर आशीवाँद देते हुए उनका स्वागत करनेके लिये
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1155)
- **Original**: इच्रभवन और स्वर्कक समान जान पड़ता था। वहाँके सब चले। उन महर्षियोंका तेज अप्रिके समान था और बे निरन्तर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1155)
- **Original**: इच्रभवन और स्वर्कक समान जान पड़ता था। वहाँके सब चले। उन महर्षियोंका तेज अप्रिके समान था और बे निरन्तर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1156)
- **Original**: स्थानोंका दर्शन कर वे परम पवित्र भागीरथीके तटपर आये। स्वाध्यायमें छगे रहते थे। उन्होंने विधिपूर्वक धर्मराजका
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1156)
- **Original**: स्थानोंका दर्शन कर वे परम पवित्र भागीरथीके तटपर आये। स्वाध्यायमें छगे रहते थे। उन्होंने विधिपूर्वक धर्मराजका
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1157)
- **Original**: वहाँ यह सीतानामसे विख्यात है। उसमें ख्रानादिसे पत्ित्र हो, सल्कार किया तथा पवित्र जल, पुष्प, फल और पूल समर्पण
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1157)
- **Original**: वहाँ यह सीतानामसे विख्यात है। उसमें ख्रानादिसे पत्ित्र हो, सल्कार किया तथा पवित्र जल, पुष्प, फल और पूल समर्पण
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1158)
- **Original**: देवता, ऋषि और पितरोंका तर्पंण एवं जप करके वे बड़े किये। महाराज युथिष्ठिर्ने भी बड़ी विनयसे महर्षियोंका
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1158)
- **Original**: देवता, ऋषि और पितरोंका तर्पंण एवं जप करके वे बड़े किये। महाराज युथिष्ठिर्ने भी बड़ी विनयसे महर्षियोंका
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1159)
- **Original**: आनन्दके साथ अपने आश्रममें रहने लंगे। जा-- औराा भीमसेनकी हनुमानूजीसे भेंट और बातचीत वैहम्पायनजी कहते हैं--जनमेजय ! अर्जुनेसे मिकमेकी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1159)
- **Original**: आनन्दके साथ अपने आश्रममें रहने लंगे। जा-- औराा भीमसेनकी हनुमानूजीसे भेंट और बातचीत वैहम्पायनजी कहते हैं--जनमेजय ! अर्जुनेसे मिकमेकी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1160)
- **Original**: पास आयी और मनमें अत्यन्त प्रसन्न होकर भीमसेनसे कहने 6.
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1160)
- **Original**: पास आयी और मनमें अत्यन्त प्रसन्न होकर भीमसेनसे कहने 6.
- **Translation**: 

---

