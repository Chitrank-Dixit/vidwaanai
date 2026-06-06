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

### Verse 1 (Bramha 0.2461)
- **Original**: ऋषियोंका विधिपूर्वक तर्पण करे। फिर तिल
- **Translation**: 

---

### Verse 2 (Bramha 0.2462)
- **Original**: “अव्यक्तस्वरूप महाप्रलयकारी एवं महान्‌ और जल लेकर पितरोंकी भी तृप्ति करे। उसके
- **Translation**: 

---

### Verse 3 (Bramha 0.2463)
- **Original**: रससे युक्त आप वरवृक्षको नमस्कार है। हे वट! बाद आचमन करके शिव-मन्दिरमें जाय। उसके
- **Translation**: 

---

### Verse 4 (Bramha 0.2464)
- **Original**: आप प्रत्येक कल्पमें अमर हैं। आपपर भगवान्‌ भीतर ग्रवेश करके तीन बार देवताकी परिक्रमा
- **Translation**: 

---

### Verse 5 (Bramha 0.2465)
- **Original**: श्रीहरिका निवास है। न्यग्रोध! मेरे पाप हर करे। तदनन्तर 'मार्कण्डेयेश्वराय नपः ' इस मूलमख्रसे
- **Translation**: 

---

### Verse 6 (Bramha 0.2466)
- **Original**: लीजिये। कल्पवृक्ष! आपको नमस्कार है।' अथवा अधघोर'मन्त्रसे शंकरजीकी पूजा करके
- **Translation**: 

---

### Verse 7 (Bramha 0.2467)
- **Original**: इसके बाद भक्तिपूर्वक परिक्रमा करके उस उन्हें प्रणाम करे और निमप्नाद्धित मन्त्र पढ़कर। कल्पान्तस्थायी वटको नमस्कार करे। ऐसा करनेवाला 1- 3&अघोरेभ्योड थ घोरेभ्यो घोरघोरतरेध्य: सर्वेभ्य: सर्वशर्वेभ्यों नमस्ते अस्तु रुद्ररूपेभ्य:।
- **Translation**: 

---

### Verse 8 (Bramha 0.2468)
- **Original**: * सार्कण्डेयेश्वर शिव, वटवृक्ष श्रीकृष्ण, बलभद्र एवं सुभग्गाके दर्शन-पूजनका माहात्य «119 मनुष्य केंचुलसे छूटे हुए सर्पको भाँति सहसा
- **Translation**: 

---

### Verse 9 (Bramha 0.2469)
- **Original**: एरुष एकाग्रचित्त हो द्वादशाक्षर-मन्त्र ( 3» पापोसे मुक्त हो जाता है। उस वृक्षकी छायामें पहुँच
- **Translation**: 

---

### Verse 10 (Bramha 0.2470)
- **Original**: नमो भगवतते वासुदेवाय )-से भगवान्‌ श्रीकृष्णकी जानेपर मनुष्य ब्रह्महत्यासे भी मुक्त हो जाता है,
- **Translation**: 

---

### Verse 11 (Bramha 0.2471)
- **Original**: पूजा करे। जो द्वादशाक्षर-मन्त्रके द्वारा भक्तिपूर्वक फिर अन्य पापोंकी तो बात ही क्‍या है। भगवान्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.2472)
- **Original**: सदा भगवान्‌ पुरुषोत्तमकी पूजा करते हैं, बे श्रीकृष्णके अज्भसे प्रकट हुए ब्रह्मतेजोमय वरवृक्षरूपी
- **Translation**: 

---

### Verse 13 (Bramha 0.2473)
- **Original**: मोक्षको प्राप्त होते हैं। देवता, योगी तथा सोमपान विष्णुको प्रणाम करके मानव राजसूय और अश्वमेध-
- **Translation**: 

---

### Verse 14 (Bramha 0.2474)
- **Original**: करनेबाले याज्ञिक भी जिस गतिकों नहीं पाते, यज्ञसे भी अधिक फल पाता है और अपने कुलका
- **Translation**: 

---

### Verse 15 (Bramha 0.2475)
- **Original**: उसीको द्वादशाक्षर-मन्त्रका जप करनेवाले पुरुष उद्धार करके विष्णुलोकमें जाता है। भगवान्‌ श्रीकृष्णके
- **Translation**: 

---

### Verse 16 (Bramha 0.2476)
- **Original**: प्राप्त कर लेते हैं। अत: उसी मन्त्रसे भक्तिपूर्वक सामने खड़े हुए गरुड़को जो नमस्कार करता है,
- **Translation**: 

---

### Verse 17 (Bramha 0.2477)
- **Original**: गन्ध-पुष्प आदि सामग्रियोंद्वारा जगद्गुरु श्रीकृष्णकी वह सब पापोंसे मुक्त हो श्रीविष्णुके बैकुण्ठधाममें
- **Translation**: 

---

### Verse 18 (Bramha 0.2478)
- **Original**: पूजा करके उन्हें प्रणाम करे। फिर इस प्रकार जाता है। बटवृक्ष और गरुड़का दर्शन करनेके
- **Translation**: 

---

### Verse 19 (Bramha 0.2479)
- **Original**: प्रार्थना करे--' जगन्नाथ श्रीकृष्ण आपकी जय हो। पश्चात्‌ जो पुस्षोत्म श्रीकृष्ण, बलभद्र और सुभद्रादेबीका
- **Translation**: 

---

### Verse 20 (Bramha 0.2480)
- **Original**: सब पापोंका नाश करनेवाले प्रभो! आपकी जय दर्शन करता है, वह परम गतिको प्राप्त होता है।
- **Translation**: 

---

