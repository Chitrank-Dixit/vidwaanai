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

### Verse 1 (Bramha 0.1881)
- **Original**: उस नगरमें अनेकों वन, उपवन, पतित्र एवं तुम जितेन्द्रिय एवं विशुद्धचित्त होकर सुनो। मैं
- **Translation**: 

---

### Verse 2 (Bramha 0.1882)
- **Original**: मनोरम उद्यान, भाँति-भाँतिके पुष्पोंसे सुशोभित सत्ययुगके राजा इन्द्रहुम्बका चरित्र बतलाता हूँ।
- **Translation**: 

---

### Verse 3 (Bramha 0.1883)
- **Original**: दिव्य देवमन्दिर, शाल, ताल, तमाल, बकुल, इस पृथ्वीपर मालवामें अवन्ती (उज्जैन) नामकी
- **Translation**: 

---

### Verse 4 (Bramha 0.1884)
- **Original**: नागकेसर, पीपल, कनेर, चन्दन, अगर, चम्पा नगरी बिख्यात है। वही राजा इन्द्रप्रकी राजधानी
- **Translation**: 

---

### Verse 5 (Bramha 0.1885)
- **Original**: तथा अन्यान्य मनोहर वृक्ष, लता-गुल्म आदि थी। अवन्ती इस पृथ्वीके मुकुटके समान थी।
- **Translation**: 

---

### Verse 6 (Bramha 0.1886)
- **Original**: शोभा पाते थे। अनेकों जलाशय उस महापुरीको वहाँ हष्ट-पुष्ट मनुष्य भरे थे। उसकी चहारदीवारी
- **Translation**: 

---

### Verse 7 (Bramha 0.1887)
- **Original**: शोभा बढ़ा रहे थे। अबन्तीपुरोमें त्रिनेत्रधारी और दरवाजे दृढ़ बने हुए थे। दरवाजोंपर मजबूत
- **Translation**: 

---

### Verse 8 (Bramha 0.1888)
- **Original**: त्रिपुरशत्रु भगवान्‌ शिव महाकाल नामसे प्रसिद्ध किंवाड़ और सुदृढ़ यन्त्र लगे थे। नगरके चारों [होकर रहते हैं। वे समस्त कामनाओंके पूर्ण ओर अनेकों खाइयाँ बनी हुई थीं। नगरमें बहुत-
- **Translation**: 

---

### Verse 9 (Bramha 0.1889)
- **Original**: करनेवाले हैं। वहाँ एक शिवकुण्ड है, जो सब से व्यापारी बसते थे। नाना प्रकारके बर्तनोंकी
- **Translation**: 

---

### Verse 10 (Bramha 0.1890)
- **Original**: पापोंका नाश करनेवाला हैं। उसमें विधिपूर्वक अच्छी बिक्री होती थी। रथ चलने लायक सड़कें
- **Translation**: 

---

### Verse 11 (Bramha 0.1891)
- **Original**: स्नान करके देवताओं, ऋषियों और पितरोंका और बाजार सुन्दर थे। चौराहोंसे चारों ओर जानेके
- **Translation**: 

---

### Verse 12 (Bramha 0.1892)
- **Original**: तर्पण करें। फिर शिवालयमें जाकर भगवान्‌ लिये मार्गोंका अच्छी प्रकार विभाग हुआ था।
- **Translation**: 

---

### Verse 13 (Bramha 0.1893)
- **Original**: शिवकी तीन बार प्रदक्षिणा करे। तत्पश्चात्‌ स्नान, अनेकों घर और गोपुर बने हुए थे। बहुत-सी
- **Translation**: 

---

### Verse 14 (Bramha 0.1894)
- **Original**: पुष्प, गन्‍्ध, धूप और दीप आदिके द्वारा भक्तिपूर्वक गलियाँ उस नगरको शोभा बढ़ाती थीं। राजहंसोंके
- **Translation**: 

---

### Verse 15 (Bramha 0.1895)
- **Original**: महाकालका विधिवत्‌ पूजन करे। ऐसा करनेवाला समान श्वेत और मनोहर महल लाखोंकी संख्यामें
- **Translation**: 

---

### Verse 16 (Bramha 0.1896)
- **Original**: मनुष्य एक हजार अश्वमेध-यज्ञोंका फल पाता है। बने हुए थे, जो उस पुरीकी श्रीबृद्धि कर रहे थे।
- **Translation**: 

---

### Verse 17 (Bramha 0.1897)
- **Original**: वह सब पापोंसे मुक्त हो समस्त कामनाओंको पूर्ण अनेकों यज्ञसम्बन्धी उत्सवोंके कारण उस नगरमें
- **Translation**: 

---

### Verse 18 (Bramha 0.1898)
- **Original**: करनेवाले विमानोंद्वारा भगवान्‌ शिवके परम धाममें आनन्द छाया रहता था। गाने और बजानेको ध्वनि
- **Translation**: 

---

### Verse 19 (Bramha 0.1899)
- **Original**: जाता है। है गूँजती रहती थी। भाँति-भाँतिकी ध्वजा और पताकाओंसे वह पुरी सुशोभित थी। हाथी, घोड़े, रथ और पैदलोंको सेना सब ओर व्याप्त थी। अनेक प्रकारके सैनिक वहाँ भरें थे। अनेकों जनपदोंके लोग वहाँ बसे हुए थे। ब्राह्मण, क्षत्रिय,
- **Translation**: 

---

### Verse 20 (Bramha 0.1900)
- **Original**: वैश्य, शूद्र तथा दिद्वान्‌ पुरुषोंसे वह नगरी
- **Translation**: 

---

