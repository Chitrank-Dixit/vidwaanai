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

### Verse 1 (Mahabharat 0.4601)
- **Original**: युधिष्ठिरपर धावा किया। उस समय झिखण्डी, सात्यकि तथा भलीधधाँति पीड़ित किया। तब कर्णने भी उममेंसे प्रत्येककों
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4601)
- **Original**: युधिष्ठिरपर धावा किया। उस समय झिखण्डी, सात्यकि तथा भलीधधाँति पीड़ित किया। तब कर्णने भी उममेंसे प्रत्येककों
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4602)
- **Original**: पाण्डब लोग राजाको सब ओरसे घेरकर उनकी रक्षा करने दस-दस बाणोंसे बाँध डाला। उनके घोड़े, सारथि और रथ
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4602)
- **Original**: पाण्डब लोग राजाको सब ओरसे घेरकर उनकी रक्षा करने दस-दस बाणोंसे बाँध डाला। उनके घोड़े, सारथि और रथ
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4603)
- **Original**: लगे। इसी प्रकार आपके पक्षवाले झुरवीर योद्धा भी डटकर जब कर्णके बाणोंसे आच्छादित हो गये तो उन्होंने विवज्ञ
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4603)
- **Original**: लगे। इसी प्रकार आपके पक्षवाले झुरवीर योद्धा भी डटकर जब कर्णके बाणोंसे आच्छादित हो गये तो उन्होंने विवज्ञ
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4604)
- **Original**: कर्णकी रक्षा करने छगे। उस समय युधिष्ठिर आदि पाण्डव होकर कर्णको आगे बढ़नेके लिये मार्ग दे दिया। अपने
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4604)
- **Original**: कर्णकी रक्षा करने छगे। उस समय युधिष्ठिर आदि पाण्डव होकर कर्णको आगे बढ़नेके लिये मार्ग दे दिया। अपने
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4605)
- **Original**: और कर्ण आदि हमलोग निर्भय होकर युद्धमें लग गये। जा आग कर्ण और युधिष्टिरका संग्राम, कर्णकी मूर्च्छा, कर्णद्वारा युथिष्ठिरका पराभव तथा भीमके द्वारा कर्णका परास्त होना सज़य कहते हैं--महाराज ! कर्णने उस सेनाको चीरकर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4605)
- **Original**: और कर्ण आदि हमलोग निर्भय होकर युद्धमें लग गये। जा आग कर्ण और युधिष्टिरका संग्राम, कर्णकी मूर्च्छा, कर्णद्वारा युथिष्ठिरका पराभव तथा भीमके द्वारा कर्णका परास्त होना सज़य कहते हैं--महाराज ! कर्णने उस सेनाको चीरकर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4606)
- **Original**: गिरा। मानो प्राण निकल गये हों, ऐसा निश्ेष्ट और अखेत धर्मराजपर धावा किया। उस समय झप्नुओंने उसपर नाना
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4606)
- **Original**: गिरा। मानो प्राण निकल गये हों, ऐसा निश्ेष्ट और अखेत धर्मराजपर धावा किया। उस समय झप्नुओंने उसपर नाना
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4607)
- **Original**: होकर कर्ण झल्यके सामने ही गिर पड़ा। राजा युधिप्ठिस्ते प्रकास्के हजारों अख्र-झख््र चलाये, किंतु उसने उन सबके
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4607)
- **Original**: होकर कर्ण झल्यके सामने ही गिर पड़ा। राजा युधिप्ठिस्ते प्रकास्के हजारों अख्र-झख््र चलाये, किंतु उसने उन सबके
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4608)
- **Original**: अर्जुनका हित करनेकी इच्छासे कर्णपर पुनः प्रहार नहीं दुकड़े-टुकड़े कर डाले । इतना ही नहीं, अपने भयंकर बाणोंसे
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4608)
- **Original**: अर्जुनका हित करनेकी इच्छासे कर्णपर पुनः प्रहार नहीं दुकड़े-टुकड़े कर डाले । इतना ही नहीं, अपने भयंकर बाणोंसे
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4609)
- **Original**: किया। कर्णको उस अबवस्थामें देखकर कौरवसेनामें उसने शन्नुओंको घायल भी कर डाला। उनके मस्तकों,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4609)
- **Original**: किया। कर्णको उस अबवस्थामें देखकर कौरवसेनामें उसने शन्नुओंको घायल भी कर डाला। उनके मस्तकों,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4610)
- **Original**: हाहाकार मच गया। धुजाओं तथा जंघाओंको काट गिराया
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4610)
- **Original**: हाहाकार मच गया। धुजाओं तथा जंघाओंको काट गिराया
- **Translation**: 

---

