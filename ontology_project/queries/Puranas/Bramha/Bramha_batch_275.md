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

### Verse 1 (Bramha 0.5481)
- **Original**: और इच्छानुसार चलनेवाले विमानसे वैकुण्ठधाममें मारकर विदेहकुमारी सीताको अग्निपरीक्षाद्वारा शुद्ध
- **Translation**: 

---

### Verse 2 (Bramha 0.5482)
- **Original**: जाता है। उस समय दिव्याड्भनाएँ उसकी सेबामें प्रमाणित किया और विभीषणको राज्य दे भगवान्‌
- **Translation**: 

---

### Verse 3 (Bramha 0.5483)
- **Original**: रहतो हैं और गन्धर्व उसके यशका गान करते हैं। वासुदेवकी प्रतिमाको साथ लेकर वे पुष्पक
- **Translation**: 

---

### Verse 4 (Bramha 0.5484)
- **Original**: वह अपने साथ कुलकी इब्कीस पीढ़ियोंका भी विमानपर आरूढ़ हुए और अनायास हो पूर्वजोंद्वारा
- **Translation**: 

---

### Verse 5 (Bramha 0.5485)
- **Original**: उद्धार कर देता है। मुनिवरों! इस प्रकार मैंने पालित अयोध्या नगरीमें जा पहुँचे। भक्तवत्सल
- **Translation**: 

---

### Verse 6 (Bramha 0.5486)
- **Original**: भगवान्‌ अनन्तके सम्बन्धमें कुछ निवेदन किया। श्रीरघुताथजीने. अपने छोटे भाई भरत और
- **Translation**: 

---

### Verse 7 (Bramha 0.5487)
- **Original**: कौन ऐसा मनुष्य है, जो सौ वर्षोर्में भी उनके शत्रुघ्नको भिन्न-भिन्न राज्योंपर अभिषिक्त किया
- **Translation**: 

---

### Verse 8 (Bramha 0.5488)
- **Original**: गुणोंका वर्णन कर सके। और स्वयं सम्राटकी भाँति समस्त धूमण्डलके
- **Translation**: 

---

### Verse 9 (Bramha 0.5489)
- **Original**: इस प्रकार मनुष्योंकों भोग और मोक्ष देनेवाले राज्यपर आसीन हुए। उन्होंने अपने पुरातन स्वरूप
- **Translation**: 

---

### Verse 10 (Bramha 0.5490)
- **Original**: परम दुर्लभ पुरुषोत्तमक्षेत्र तथा अनन्त वासुदेवके श्रीविष्णकी उस प्रतिमाका आराधन करते हुए
- **Translation**: 

---

### Verse 11 (Bramha 0.5491)
- **Original**: माहात्म्यका वर्णन किया गया। पुरुषोत्तमक्षेत्रमें
- **Translation**: 

---

### Verse 12 (Bramha 0.5492)
- **Original**: रधड * संक्षिप्त ब्रह्मपुराण * शड्ख, चक्र, गदा, पद्म और पीताम्बर धारण
- **Translation**: 

---

### Verse 13 (Bramha 0.5493)
- **Original**: पाता है, उसे पुरुषोत्तमक्षेत्रमें एक ही मासमें ग्राप्त करनेवाले कमलनयन भगवान्‌ श्रीकृष्ण विराजमान
- **Translation**: 

---

### Verse 14 (Bramha 0.5494)
- **Original**: कर लेता है। तपस्या, ब्रह्मचर्यपालन तथा आसक्ति- हैं, जिन्होंने कंस और केशीका संहार किया था।
- **Translation**: 

---

### Verse 15 (Bramha 0.5495)
- **Original**: त्यागसे जो फल मिलता है, उसे मनीषी पुरुष जो लोग वहाँ देव-दानव-वन्दित श्रीकृष्ण, बलभद्र
- **Translation**: 

---

### Verse 16 (Bramha 0.5496)
- **Original**: वहाँ सदा ही पाते रहते हैं। सब तीथ्थोंमें ज्लान- और सुभद्राका दर्शन करते हैं, वे धन्य हैं।
- **Translation**: 

---

### Verse 17 (Bramha 0.5497)
- **Original**: दान करनेका जो पुण्य फल बताया गया है, वह भगवान्‌ श्रीकृष्ण तीनों लोकोंके स्वामी तथा
- **Translation**: 

---

### Verse 18 (Bramha 0.5498)
- **Original**: मनीषी पुरुषोंको यहाँ सर्वदा प्राप्त होता है। सम्पूर्ण अभीष्ट वस्तुओंके दाता हैं। जो सदा विधिपूर्वक तीर्थसेबन तथा व्रत और नियमोंके उनका ध्यान करते हैं, वे निश्चय ही मुक्त हो जाते
- **Translation**: 

---

### Verse 19 (Bramha 0.5499)
- **Original**: पालनसे जो फल बताया गया है, उसे वहाँ हैं। जो सदा श्रीकृष्णमें अनुरक रहते हैं, रातकों
- **Translation**: 

---

### Verse 20 (Bramha 0.5500)
- **Original**: इन्द्रियसंयमपूर्वक पवित्रतासे रहनेवाला पुरुष प्रतिदिन सोते समय श्रीकृष्णका चिन्तन करते हैं और फिर
- **Translation**: 

---

