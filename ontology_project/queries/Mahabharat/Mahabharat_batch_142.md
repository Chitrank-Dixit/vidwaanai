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

### Verse 1 (Mahabharat 0.1411)
- **Original**: उददेशयसे यहाँ पयारें हैं, वह निष्फरू-नहीं होगा। मेरा फुन सागर। उसकी लंबाई-चौड़ाई अनेकों योजन है। वहाँ एक
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1411)
- **Original**: उददेशयसे यहाँ पयारें हैं, वह निष्फरू-नहीं होगा। मेरा फुन सागर। उसकी लंबाई-चौड़ाई अनेकों योजन है। वहाँ एक
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1412)
- **Original**: कुबल्पाश्व इस भूमण्डलमें अद्वितीय वीर है, यह बड़ा वैर्य बड़ा बलवान्‌ दानव रहता है, उसका नाम है--शुल्युं। वह
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1412)
- **Original**: कुबल्पाश्व इस भूमण्डलमें अद्वितीय वीर है, यह बड़ा वैर्य बड़ा बलवान्‌ दानव रहता है, उसका नाम है--शुल्युं। वह
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1413)
- **Original**: रखनेवाल्ल और फुर्तीका है। आपका अभीष्ट कार्य वह मधुकैटभका पुत्र है। पृथ्वीके भीतर छिपकर रहा करता है।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1413)
- **Original**: रखनेवाल्ल और फुर्तीका है। आपका अभीष्ट कार्य वह मधुकैटभका पुत्र है। पृथ्वीके भीतर छिपकर रहा करता है।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1414)
- **Original**: अब॒श्य पूर्ण करेगा। इसके बलखार पुत्र भी अख-शख्र लेकर बालूके भीतर छिषकर रहनेवाल्म बह महाकरूर दैत्य वर्षभरमें
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1414)
- **Original**: अब॒श्य पूर्ण करेगा। इसके बलखार पुत्र भी अख-शख्र लेकर बालूके भीतर छिषकर रहनेवाल्म बह महाकरूर दैत्य वर्षभरमें
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1415)
- **Original**: इस युद्धमें इसका साथ देंगे। आप मुझे छोड़ दीजिये; क्योंकि एक बार साँस लेता है। जब वह साँस छोड़ता है; उस समय
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1415)
- **Original**: इस युद्धमें इसका साथ देंगे। आप मुझे छोड़ दीजिये; क्योंकि एक बार साँस लेता है। जब वह साँस छोड़ता है; उस समय
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1416)
- **Original**: अब मैंने शस्मोंकों त्याग दिया है, मैं युद्धसे निवृत्त हो गया हैँ। पर्वत और वनोंके सहित यह पृथ्वी डोलने लगती है। उसके
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1416)
- **Original**: अब मैंने शस्मोंकों त्याग दिया है, मैं युद्धसे निवृत्त हो गया हैँ। पर्वत और वनोंके सहित यह पृथ्वी डोलने लगती है। उसके
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1417)
- **Original**: उत्तडुने कहा--'बहुत अच्छा ।' फिर राजर्षि बृहदश्चने उत्तदू श्वासकी आँधीसे रेतका इतना ऊँचा ब्ंडर उठता है; जिससे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1417)
- **Original**: उत्तडुने कहा--'बहुत अच्छा ।' फिर राजर्षि बृहदश्चने उत्तदू श्वासकी आँधीसे रेतका इतना ऊँचा ब्ंडर उठता है; जिससे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1418)
- **Original**: मुनिकी आज्ञा पाकर उनके अभीष्ट कार्यको पूर्ण करनेके सूर्य भी ढक जाता है, सात दिनोतक भूचाल होता रहता है।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1418)
- **Original**: मुनिकी आज्ञा पाकर उनके अभीष्ट कार्यको पूर्ण करनेके सूर्य भी ढक जाता है, सात दिनोतक भूचाल होता रहता है।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1419)
- **Original**: लिये अपने पुत्र कुबलाश्वको आदेश दिया और स्वयं तपोयनमें अप्रिकी लूपटें, चिनगारियाँ और धूएँ उठते रहते हैं।
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1419)
- **Original**: लिये अपने पुत्र कुबलाश्वको आदेश दिया और स्वयं तपोयनमें अप्रिकी लूपटें, चिनगारियाँ और धूएँ उठते रहते हैं।
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1420)
- **Original**: चले गये। दि की ट्रक 1 बी <5(: [7
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1420)
- **Original**: चले गये। दि की ट्रक 1 बी <5(: [7
- **Translation**: 

---

