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

### Verse 1 (Mahabharat 0.4741)
- **Original**: 46 संक्षिप्त महाभारत [ कर्णपर्व इसके लिये प्रयत्न करना चाहिये। इन माद़ीके पुत्रों अथवा
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4741)
- **Original**: 46 संक्षिप्त महाभारत [ कर्णपर्व इसके लिये प्रयत्न करना चाहिये। इन माद़ीके पुत्रों अथवा
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4742)
- **Original**: हाँककर भीमसेनकी सेनामें जा पहुँचे । राजा युथ्मिष्ठिरको मारनेसे क्‍या त्मभः होगा ? दुर्योधनका
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4742)
- **Original**: हाँककर भीमसेनकी सेनामें जा पहुँचे । राजा युथ्मिष्ठिरको मारनेसे क्‍या त्मभः होगा ? दुर्योधनका
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4743)
- **Original**: ज्राण संकटमें पड़ा है, उसे चलकर बचाओ ।' । कर्णने झल्यकी यह बात सुनी और देखा कि दुर्योधन
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4743)
- **Original**: ज्राण संकटमें पड़ा है, उसे चलकर बचाओ ।' । कर्णने झल्यकी यह बात सुनी और देखा कि दुर्योधन
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4744)
- **Original**: (. 9. रच कृत साहा वाह है छोडका आपके पुरकतो बाय. 99 555 नकुछ और सहदेवके साथ अपने घायल झरीरसे छाबनीपर कर 8 तह
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4744)
- **Original**: (. 9. रच कृत साहा वाह है छोडका आपके पुरकतो बाय. 99 555 नकुछ और सहदेवके साथ अपने घायल झरीरसे छाबनीपर कर 8 तह
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4745)
- **Original**: 0 2 3 हे 57743 ] लंच का ढ00 4 +« क्र खः अर्जुनद्वारा अश्वत्थामाकी पराजय, कर्णद्वारा भार्गवाख्रका प्रयोग, श्रीकृष्ण और अर्जुनका युधिष्ठिस्‍से मिलनेके लिये छावनीपर जाना तथा युधिष्टिरका उनसे कर्णके मारे जानेका समाचार पूछना सक्य कहते हैं--महाराज ! इसी समय अश्वत्थामा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4745)
- **Original**: 0 2 3 हे 57743 ] लंच का ढ00 4 +« क्र खः अर्जुनद्वारा अश्वत्थामाकी पराजय, कर्णद्वारा भार्गवाख्रका प्रयोग, श्रीकृष्ण और अर्जुनका युधिष्ठिस्‍से मिलनेके लिये छावनीपर जाना तथा युधिष्टिरका उनसे कर्णके मारे जानेका समाचार पूछना सक्य कहते हैं--महाराज ! इसी समय अश्वत्थामा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4746)
- **Original**: परियका प्रहार किया। किंतु अर्जुनने उसे हैंसते-हँसते रख्वियोंकी बहुत बड़ी सेना साथ लेकर, जहाँ अर्जुन खड़ें थे,
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4746)
- **Original**: परियका प्रहार किया। किंतु अर्जुनने उसे हैंसते-हँसते रख्वियोंकी बहुत बड़ी सेना साथ लेकर, जहाँ अर्जुन खड़ें थे,
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4747)
- **Original**: काट डाला। अब अश्वत्यापाका क्रोध और बढ़ गया। उसने वहाँ ही सहसा आ थभ्रमका। उसे आते देख अर्जुनने
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4747)
- **Original**: काट डाला। अब अश्वत्यापाका क्रोध और बढ़ गया। उसने वहाँ ही सहसा आ थभ्रमका। उसे आते देख अर्जुनने
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4748)
- **Original**: ऐन्द्राख्का प्रयोग किया, परंतु अर्जुनने महेन्द्रखसे उसे झान्त एकबआरगी उसका बढ़ाव रोक दिया। अश्वस्थामा झल्ला
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4748)
- **Original**: ऐन्द्राख्का प्रयोग किया, परंतु अर्जुनने महेन्द्रखसे उसे झान्त एकबआरगी उसका बढ़ाव रोक दिया। अश्वस्थामा झल्ला
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4749)
- **Original**: कर दिया। साथ ही अश्वत्थामाकों भी अपने बाणोंसे ढक उठा; बह बाणोंकी मारसे श्रीकृष्ण और अ्जुनको
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4749)
- **Original**: कर दिया। साथ ही अश्वत्थामाकों भी अपने बाणोंसे ढक उठा; बह बाणोंकी मारसे श्रीकृष्ण और अ्जुनको
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4750)
- **Original**: दिया। ड्रोणकुमार्ने अपने सायकॉंसे उन बराणोंकों काट आकादित करने लूगा। यह देख अर्जुनने हैँसते-हैसते
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4750)
- **Original**: दिया। ड्रोणकुमार्ने अपने सायकॉंसे उन बराणोंकों काट आकादित करने लूगा। यह देख अर्जुनने हैँसते-हैसते
- **Translation**: 

---

