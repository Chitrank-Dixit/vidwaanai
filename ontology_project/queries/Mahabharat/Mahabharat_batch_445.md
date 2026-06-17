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

### Verse 1 (Mahabharat 0.4441)
- **Original**: . मद्रराजके इस प्रकार: कटुभाषण कसनेपर कौरब- अर्जुनको बच्चाना चाहेगा तो मैं उसे भी.नष्ट कर डालूँगा
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4441)
- **Original**: . मद्रराजके इस प्रकार: कटुभाषण कसनेपर कौरब- अर्जुनको बच्चाना चाहेगा तो मैं उसे भी.नष्ट कर डालूँगा
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4442)
- **Original**: सेनरापति कर्ण अत्यन्त क्रोधमें भर गया और उनसे कहने अथवा भीष्मके समान स्वयं ही वमल्ोक चल्मा जाऊँगा।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4442)
- **Original**: सेनरापति कर्ण अत्यन्त क्रोधमें भर गया और उनसे कहने अथवा भीष्मके समान स्वयं ही वमल्ोक चल्मा जाऊँगा।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4443)
- **Original**: छूगा, “रहने दो, रहने दो, इस प्रकार क्‍यों बड़बड़ातें हों, अधिक क्या कहूँ, यदि उसकी रक्षाके लिये यम, वरुण,
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4443)
- **Original**: छूगा, “रहने दो, रहने दो, इस प्रकार क्‍यों बड़बड़ातें हों, अधिक क्या कहूँ, यदि उसकी रक्षाके लिये यम, वरुण,
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4444)
- **Original**: तो मेरा और अर्जुनका युद्ध -होनेहीबाला है। यदि वह कुबेर और इञ्र भी अपने अनुयायियोंसहित एक साथ
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4444)
- **Original**: तो मेरा और अर्जुनका युद्ध -होनेहीबाला है। यदि वह कुबेर और इञ्र भी अपने अनुयायियोंसहित एक साथ
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4445)
- **Original**: संग्राममें मुझे परास्त कर दे तो तुम्हारी ही बात सच माली मिलकर युद्धभूमिमें आयेंगे तो मैं उसे उन सबके सहित
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4445)
- **Original**: संग्राममें मुझे परास्त कर दे तो तुम्हारी ही बात सच माली मिलकर युद्धभूमिमें आयेंगे तो मैं उसे उन सबके सहित
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4446)
- **Original**: जायेगी।' इसपर मेद्ररोजनें ऐसा ही हो” इतना कहकर और परास्त कर दूँगा।' कोई उत्तर नहीं दिया। तब कर्णने युद्धके लिये उत्सुक होकर का चख जक हुए के है आओ मल उनसे कहा 'झल्य ! रथ बढ़ाओ।' उन्हें सुनकर मद्रराज हैसे और उसका तिरस्कार करके
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4446)
- **Original**: जायेगी।' इसपर मेद्ररोजनें ऐसा ही हो” इतना कहकर और परास्त कर दूँगा।' कोई उत्तर नहीं दिया। तब कर्णने युद्धके लिये उत्सुक होकर का चख जक हुए के है आओ मल उनसे कहा 'झल्य ! रथ बढ़ाओ।' उन्हें सुनकर मद्रराज हैसे और उसका तिरस्कार करके
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4447)
- **Original**: . युद्धके लिये कूच करके कर्णने अपनी सेनाको बीचहीमें रोककर कहने लगे, 'कर्ण ! बस, अब चुप रहो।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4447)
- **Original**: . युद्धके लिये कूच करके कर्णने अपनी सेनाको बीचहीमें रोककर कहने लगे, 'कर्ण ! बस, अब चुप रहो।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4448)
- **Original**: उत्साहित करनेके लिये पाण्डबोंके एक-एक वीस्से मिलनेपर तुम जोशमें आकर बहुत बढ़ी-चढ़ी बातें कह गये हो। भला,
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4448)
- **Original**: उत्साहित करनेके लिये पाण्डबोंके एक-एक वीस्से मिलनेपर तुम जोशमें आकर बहुत बढ़ी-चढ़ी बातें कह गये हो। भला,
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4449)
- **Original**: कहा, 'आज तुममेंसे जो कोई मुझे: श्रेतवाहन अ्जुनसे कहाँ नस्त्रेष्ठ अर्जुन और कहाँ नराधम तुम
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4449)
- **Original**: कहा, 'आज तुममेंसे जो कोई मुझे: श्रेतवाहन अ्जुनसे कहाँ नस्त्रेष्ठ अर्जुन और कहाँ नराधम तुम
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4450)
- **Original**: यह तो बताओ,
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4450)
- **Original**: यह तो बताओ,
- **Translation**: 

---

