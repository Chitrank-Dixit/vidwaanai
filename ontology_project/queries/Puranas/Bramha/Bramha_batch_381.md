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

### Verse 1 (Bramha 0.7601)
- **Original**: पुराना आँवला, खीर, नारियल, फालसा, नारंगी, एवं च। नम: स्वाहाये स्वधाये नित्यमेव नमो
- **Translation**: 

---

### Verse 2 (Bramha 0.7602)
- **Original**: खजूर, अंगूर, नीलकैथ, परवल, चिरांजी, बेर, भसमः।' * इस मन्त्रका श्राद्धके आरम्भ और अन्तमें
- **Translation**: 

---

### Verse 3 (Bramha 0.7603)
- **Original**: जंगली बेर, इन्द्रजाौ और भतुआ-इन फलोंको तीन बार जप करे। पिण्डदान करते समय भी
- **Translation**: 

---

### Verse 4 (Bramha 0.7604)
- **Original**: श्राद्धमें यलपूर्वक लेना चाहिये। गुड़, शक्कर, एकाग्रचित्त होकर इसका जप करना चाहिये।
- **Translation**: 

---

### Verse 5 (Bramha 0.7605)
- **Original**: खाँड़, गायका दूध, दहो, घी, तिलका तेल, सेंधा इससे पितर शीघ्र ही आ जाते हैं और राक्षस भाग
- **Translation**: 

---

### Verse 6 (Bramha 0.7606)
- **Original**: तथा समुद्र और झीलसे उत्पन्न होनेवाला नमक, खड़े होते हैं तथा तीनों लोकोंके पितर तृप्त होते
- **Translation**: 

---

### Verse 7 (Bramha 0.7607)
- **Original**: पवित्र सुगन्‍्ध, चन्दन, अरगजा तथा केसर भी हैं। यह मन्त्र पितरोंको तारनेवाला है। श्राद्धमें
- **Translation**: 

---

### Verse 8 (Bramha 0.7608)
- **Original**: पितरोंको निवेदन करे। सामयिक शाक, चौलाई, रेशम, सन अथवा कपासका नया सूत देना चाहिये।
- **Translation**: 

---

### Verse 9 (Bramha 0.7609)
- **Original**: बथुआ, मूली तथा जंगली साग श्राद्धमें देनेयोग्य ऊन अथवा पाटका सूत्र वर्जित है। विद्वान्‌ पुरुष
- **Translation**: 

---

### Verse 10 (Bramha 0.7610)
- **Original**: है। चम्पा, चमेली, बेला, लोध, अशोक, तुलसी, जिसमें कोर न हो, ऐसा वस्त्र फटा न होनेपर भी
- **Translation**: 

---

### Verse 11 (Bramha 0.7611)
- **Original**: तिलक, शतपत्नरा, सुगन्धित शेफालिका, कुब्जक, श्राद्धमें न दे; क्योंकि उससे पितरोंकों तृप्ति नहों
- **Translation**: 

---

### Verse 12 (Bramha 0.7612)
- **Original**: तगर, बनकेवड़ा और जूही आदि पुष्प श्राद्धमें होती और दाताके लिये भी अन्यायका फल प्राप्त
- **Translation**: 

---

### Verse 13 (Bramha 0.7613)
- **Original**: अर्पण करने योग्य हैं। कमल, कुमुद, पद्म, होता है। पिता आदिमेंसे जो जीवित हो, उसको
- **Translation**: 

---

### Verse 14 (Bramha 0.7614)
- **Original**: पुण्डरीक, इन्दीवर, कोकनद और कह्ार भी पिण्ड नहीं देना चाहिये, अपितु उसे विधिपूर्वक
- **Translation**: 

---

### Verse 15 (Bramha 0.7615)
- **Original**: पितरोंको निवेदन करे। गूगल, चन्दन, श्रीवास उत्तम अन्न भोजन कराना चाहिये। भोगकी इच्छा
- **Translation**: 

---

### Verse 16 (Bramha 0.7616)
- **Original**: (बेल), अगर तथा ऋषिगुग्गुल-ये पितरोंके रखनेवाला पुरुष श्राद्धके पश्चात्‌ पिण्डको अम्निमें
- **Translation**: 

---

### Verse 17 (Bramha 0.7617)
- **Original**: योग्य धूप हैं। चना और मसूर श्राद्धमें वर्जित हैं। डाल दे और जिसे पुत्रको अभिलाषा हो, वह
- **Translation**: 

---

### Verse 18 (Bramha 0.7618)
- **Original**: स्त्री, ऊँटनी और भेड़के दूध, दहो और घीका मध्यम अर्थात्‌ पितामहके पिण्डको मन्त्रोच्चारणपूर्वक
- **Translation**: 

---

### Verse 19 (Bramha 0.7619)
- **Original**: परित्याग करे। ताड़, वरुमा, काँकोल, बहुपत्रा अपनी पतलीके हाथमें दे दे और पली उसे खा ले।
- **Translation**: 

---

### Verse 20 (Bramha 0.7620)
- **Original**: (शिवलिंगी), अर्जुनी-फल, नीबू, रक्तबिल्व और जो उत्तम कान्तिकी इच्छा रखनेवाला हो, वह
- **Translation**: 

---

