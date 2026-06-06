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

### Verse 1 (Mahabharat 0.7441)
- **Original**: ब्राह्मणोंकी पूजामें प्रमाद नहीं करती थी। किसीकी चुगली
- **Translation**: 

---

### Verse 2 (Mahabharat 0.7441)
- **Original**: ब्राह्मणोंकी पूजामें प्रमाद नहीं करती थी। किसीकी चुगली
- **Translation**: 

---

### Verse 3 (Mahabharat 0.7442)
- **Original**: अद्भराग आदिके द्वारा शूज्ार नहीं करती थी। जब थे सुखसेः नहीं खाती थी। चुगल्लीकी आदत मुझे बिलकुल पसंद न
- **Translation**: 

---

### Verse 4 (Mahabharat 0.7442)
- **Original**: अद्भराग आदिके द्वारा शूज्ार नहीं करती थी। जब थे सुखसेः नहीं खाती थी। चुगल्लीकी आदत मुझे बिलकुल पसंद न
- **Translation**: 

---

### Verse 5 (Mahabharat 0.7443)
- **Original**: सोये रहते उस समय आवश्यक कार्य आ जानेपर भी मैं उन्हें थी। मैं घरका दस्वाजा छोड़कर अन्यत्र नहीं खड़ी होती और
- **Translation**: 

---

### Verse 6 (Mahabharat 0.7443)
- **Original**: सोये रहते उस समय आवश्यक कार्य आ जानेपर भी मैं उन्हें थी। मैं घरका दस्वाजा छोड़कर अन्यत्र नहीं खड़ी होती और
- **Translation**: 

---

### Verse 7 (Mahabharat 0.7444)
- **Original**: नहीं जगाती थ्री और ऐसा करके मेरे मनको विशेष संतोष देश्तक किसीसे बात नहीं कस्ती थी। मैंने कभी छियकर या
- **Translation**: 

---

### Verse 8 (Mahabharat 0.7444)
- **Original**: नहीं जगाती थ्री और ऐसा करके मेरे मनको विशेष संतोष देश्तक किसीसे बात नहीं कस्ती थी। मैंने कभी छियकर या
- **Translation**: 

---

### Verse 9 (Mahabharat 0.7445)
- **Original**: होता था। परिवारके पालन-पोषणके कार्यके छिये भी मैं सामने किसीसे अइल्लील परिहास नहीं किया तथा मेरे द्वारा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.7445)
- **Original**: होता था। परिवारके पालन-पोषणके कार्यके छिये भी मैं सामने किसीसे अइल्लील परिहास नहीं किया तथा मेरे द्वारा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.7446)
- **Original**: उ्हें कभी तंग नहीं कस्ती थी। घरकी गुप्त बातोंको सदा किसीका अहित भी नहीं हुआ है। यदि मेरे स्वामी किसी
- **Translation**: 

---

### Verse 12 (Mahabharat 0.7446)
- **Original**: उ्हें कभी तंग नहीं कस्ती थी। घरकी गुप्त बातोंको सदा किसीका अहित भी नहीं हुआ है। यदि मेरे स्वामी किसी
- **Translation**: 

---

### Verse 13 (Mahabharat 0.7447)
- **Original**: छिपाये रहती और घर-द्वास्को सदा झाड़-बुहारकर साफ कामसे बाहर जाकर फिर घरको लौटते हैं तो मैं उठकर उन्हें
- **Translation**: 

---

### Verse 14 (Mahabharat 0.7447)
- **Original**: छिपाये रहती और घर-द्वास्को सदा झाड़-बुहारकर साफ कामसे बाहर जाकर फिर घरको लौटते हैं तो मैं उठकर उन्हें
- **Translation**: 

---

### Verse 15 (Mahabharat 0.7448)
- **Original**: रखती थी। जो स्त्री सदा सावधान रहकर इस धर्म-मार्गका बैठनेके लिये आसन देती और एकापग्रलित्तते उनकी पूजा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.7448)
- **Original**: रखती थी। जो स्त्री सदा सावधान रहकर इस धर्म-मार्गका बैठनेके लिये आसन देती और एकापग्रलित्तते उनकी पूजा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.7449)
- **Original**: पालन करती है; वह खतरियोंमें अरूयतीके समान आदरणीय करती थी। जो अन्न मेरे स्वामी नहीं खाना चाहते, जिस
- **Translation**: 

---

### Verse 18 (Mahabharat 0.7449)
- **Original**: पालन करती है; वह खतरियोंमें अरूयतीके समान आदरणीय करती थी। जो अन्न मेरे स्वामी नहीं खाना चाहते, जिस
- **Translation**: 

---

### Verse 19 (Mahabharat 0.7450)
- **Original**: होती है और स्वर्गलोकमें भी उसकी विशेष प्रतिष्ठा होती है" भक्ष्य, भोज्य या लेहा (चटनी) आदिको वे नहीं पसंद भीष्पजी: कहते हैं--युथिप्ठिर ! इस अकार जहः करते, उन सबको मैं भी त्याग देती थी। सारे कुदुप्बके लिये
- **Translation**: 

---

### Verse 20 (Mahabharat 0.7450)
- **Original**: होती है और स्वर्गलोकमें भी उसकी विशेष प्रतिष्ठा होती है" भक्ष्य, भोज्य या लेहा (चटनी) आदिको वे नहीं पसंद भीष्पजी: कहते हैं--युथिप्ठिर ! इस अकार जहः करते, उन सबको मैं भी त्याग देती थी। सारे कुदुप्बके लिये
- **Translation**: 

---

