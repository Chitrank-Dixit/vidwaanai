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

### Verse 1 (Bramha 0.7641)
- **Original**: 368 + संक्षिप्त ब्रह्मपुराण *« व्यासजी बोले--पिताको तो पिण्ड दे,
- **Translation**: 

---

### Verse 2 (Bramha 0.7642)
- **Original**: यृद्धिको प्राप्त होता है-इसमें तनिक भी संदेह पितामहको प्रत्यक्ष भोजन कराये और प्रपितामहको
- **Translation**: 

---

### Verse 3 (Bramha 0.7643)
- **Original**: नहीं है। जो श्राद्धके समय इस पितृमेधबिषयक भी पिण्ड दे दे। यही शास्त्रोंका निर्णय है। मरे
- **Translation**: 

---

### Verse 4 (Bramha 0.7644)
- **Original**: अध्यायका पाठ करता है, उसके दिये हुए अन्नको हुएको पिण्ड देने और जीवितको भोजन करानेका
- **Translation**: 

---

### Verse 5 (Bramha 0.7645)
- **Original**: पितरलोग तीन युगोंतक खाते रहते हैं। इस प्रकार विधान है। उस अबवस्थामें सपिण्डीकरण और
- **Translation**: 

---

### Verse 6 (Bramha 0.7646)
- **Original**: मैंने यहाँ श्राद्ध-कल्पका वर्णन किया। यह पापोंका पार्वणश्राद्ध नहीं हो सकता।* नाश और पुण्योंकी वृद्धि करनेवाला है। श्राद्धके जो मनुष्य श्राद्ध-सम्बन्धी विधिका पालन
- **Translation**: 

---

### Verse 7 (Bramha 0.7647)
- **Original**: अवसरपर मनुष्यको संयतचित्त होकर इसका करता है, वह आयु, धन और पुत्रोंके साथ ही
- **Translation**: 

---

### Verse 8 (Bramha 0.7648)
- **Original**: श्रवण और पाठ करना चाहिये। “#>“-नप2490/-,- गृहस्थोचित सदाचार तथा कर्तव्याकर्तव्यका वर्णन व्यासजी कहते हैं--त्राह्मणो ! इस प्रकार गृहस्थ
- **Translation**: 

---

### Verse 9 (Bramha 0.7649)
- **Original**: आचाररूप धर्मका सदा पालन करना चाहिये। पुरुष हज्य, कव्य और अन्नसे देवता, पितर तथा
- **Translation**: 

---

### Verse 10 (Bramha 0.7650)
- **Original**: सदाचार बुरे लक्षणोंका नाश करता है। ब्राह्मणों! अतिधियोंका पूजन करे। सम्पूर्ण भूत, भरण-
- **Translation**: 

---

### Verse 11 (Bramha 0.7651)
- **Original**: अब मैं सदाचारका स्वरूप बतलाता हूँ, एकाग्रचित्त पोषणके योग्य कुद्म्बीजन, पशु, पक्षी, चींटियाँ, होकर उसका पालन करना चाहिये। गृहस्थको संन्यासी, भिक्षुक, पथिक तथा सदाचारी ब्राह्मण
- **Translation**: 

---

### Verse 12 (Bramha 0.7652)
- **Original**: धर्म, अर्थ और काम-तीनोंके साधनका यत्न आदि जो भी उपस्थित हों, गृहस्थ पुरुष अपने
- **Translation**: 

---

### Verse 13 (Bramha 0.7653)
- **Original**: करना चाहिये। उनके सिद्ध होनेपर उसे इस लोक घरमें सबको संतुष्ट करे। जो नित्य और नैमित्तिक
- **Translation**: 

---

### Verse 14 (Bramha 0.7654)
- **Original**: और परलोकमें सिद्धि प्राप्त होती है। मनको वशमें क्रियाओंका उल्लल्नन करता है, बह पापभोजी है।
- **Translation**: 

---

### Verse 15 (Bramha 0.7655)
- **Original**: करके अपनी आयका एक चौथाई भाग पारलौकिक मुनि बोले--महर्षे! आपने पुरुषोंके नित्य,
- **Translation**: 

---

### Verse 16 (Bramha 0.7656)
- **Original**: कल्याणके लिये संगृहीत करें। आधे भागसे नैमित्तिक और काम्य-त्रिविध कर्मोका वर्णन
- **Translation**: 

---

### Verse 17 (Bramha 0.7657)
- **Original**: नित्य-नैमित्तिक कार्योंका निर्वाह करते हुए अपना किया; अब हम सदाचारका वर्णन सुनना चाहते
- **Translation**: 

---

### Verse 18 (Bramha 0.7658)
- **Original**: भरण-पोषण करे तथा एक चौथाई भाग अपने हैं, जिसका अनुष्ठान करके मनुष्य इस लोक और
- **Translation**: 

---

### Verse 19 (Bramha 0.7659)
- **Original**: लिये मूल पूँजीके रूपमें रखकर उसे बढ़ाये। परलोकमें भी सुखका भागी हो। ब्राह्मणो! ऐसा करनेसे धन सफल होता है। इसी व्यासजीने कहा--ब्राह्मणो! गृहस्थ पुरुषकों
- **Translation**: 

---

### Verse 20 (Bramha 0.7660)
- **Original**: प्रकार पापकी निवृत्ति तथा पारलौकिक उन्नतिके सदा ही सदाचारकी रक्षा करनी चाहिये। आचारहीन
- **Translation**: 

---

