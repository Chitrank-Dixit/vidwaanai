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

### Verse 1 (Mahabharat 0.5221)
- **Original**: यपराजका आधिपत्य हो गया है। आज कर्ण और अर्जुनमें जैसा युद्ध हुआ है, बैसा पहले कभी नहीं हुआ था। कर्णने
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5221)
- **Original**: यपराजका आधिपत्य हो गया है। आज कर्ण और अर्जुनमें जैसा युद्ध हुआ है, बैसा पहले कभी नहीं हुआ था। कर्णने
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5222)
- **Original**: 3 चढ़ाई कस्के श्रीकृष्ण, अर्जुन तथा अन्य झब्ुओंको प्राय: है. %% काबूमें कर लिया था; किंतु कुछ फल नहीं हुआ। निक्षय
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5222)
- **Original**: 3 चढ़ाई कस्के श्रीकृष्ण, अर्जुन तथा अन्य झब्ुओंको प्राय: है. %% काबूमें कर लिया था; किंतु कुछ फल नहीं हुआ। निक्षय
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5223)
- **Original**: 0 ही दैव पाण्डवोंके अधीन होकर काम कर रहा है। वह उनकी तो रक्षा करता है और हमारा नाश । यही कारण है कि तु्हारे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5223)
- **Original**: 0 ही दैव पाण्डवोंके अधीन होकर काम कर रहा है। वह उनकी तो रक्षा करता है और हमारा नाश । यही कारण है कि तु्हारे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5224)
- **Original**: हैं अथंकी सिद्धिके लिये प्रयत्न करनेवाले सभी वीर जत्रुओंके. हावसे बलपूर्वक मारे गये। तुम्हारी सेनाके प्रमुख योद्धा इञ्,
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5224)
- **Original**: हैं अथंकी सिद्धिके लिये प्रयत्न करनेवाले सभी वीर जत्रुओंके. हावसे बलपूर्वक मारे गये। तुम्हारी सेनाके प्रमुख योद्धा इञ्,
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5225)
- **Original**: 4 थम और कुबेरके समान प्रभावझाली थे। उममें पराक्रम, ... मद्रराजकी ये बातें. सुनकर और - मन-ही-मन ज्ञौर्य; बल, तेज तथा और भी बहुत-से उत्तम गुण मौजूद थे।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5225)
- **Original**: 4 थम और कुबेरके समान प्रभावझाली थे। उममें पराक्रम, ... मद्रराजकी ये बातें. सुनकर और - मन-ही-मन ज्ञौर्य; बल, तेज तथा और भी बहुत-से उत्तम गुण मौजूद थे।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5226)
- **Original**: अपने अन्यायोंका भी -स्मरण करके दुर्योधन थे एक प्रकारसे अवध्य थे; तो भी उन्हें पाष्डकयोद्धाओंने
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5226)
- **Original**: अपने अन्यायोंका भी -स्मरण करके दुर्योधन थे एक प्रकारसे अवध्य थे; तो भी उन्हें पाष्डकयोद्धाओंने
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5227)
- **Original**: उदास हो गया। उसकी बुद्धि कुछ भी काम रणमें मार डाला। अतः भारत ! सुम झोच न करो
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5227)
- **Original**: उदास हो गया। उसकी बुद्धि कुछ भी काम रणमें मार डाला। अतः भारत ! सुम झोच न करो
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5228)
- **Original**: यह सब ॒ देती थी। दुःखसे अत्यन्त पीड़ित होकर वह बारंबार प्रारब्यका खेल है। सबको सदा ही सिद्धि नहीं मिलती, ऐसा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5228)
- **Original**: यह सब ॒ देती थी। दुःखसे अत्यन्त पीड़ित होकर वह बारंबार प्रारब्यका खेल है। सबको सदा ही सिद्धि नहीं मिलती, ऐसा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5229)
- **Original**: उसासे भरने लूगा। अ भीम और अर्जुन आदिके भयसे दुर्योधनके रोकनेपर भी कोरब-सेनाकां भागना तथा दोनों ओरकी सेनाओंका शिविरमें जाना स्ञय कहते हैं--सहाराज । उस समय कौरवब-सैनिक
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5229)
- **Original**: उसासे भरने लूगा। अ भीम और अर्जुन आदिके भयसे दुर्योधनके रोकनेपर भी कोरब-सेनाकां भागना तथा दोनों ओरकी सेनाओंका शिविरमें जाना स्ञय कहते हैं--सहाराज । उस समय कौरवब-सैनिक
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5230)
- **Original**: दुर्योधनकी यह झुस्वीरोंके योग्य बात सुनकर सारबिने भ्रीमसेनके भयसे व्याकुल होकर भाग रहे थे। उनकी यह
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5230)
- **Original**: दुर्योधनकी यह झुस्वीरोंके योग्य बात सुनकर सारबिने भ्रीमसेनके भयसे व्याकुल होकर भाग रहे थे। उनकी यह
- **Translation**: 

---

