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

### Verse 1 (Bramha 0.7341)
- **Original**: कमोंके निरन्तर साक्षौ रहते हैं। इनके साथ धर्म जाता है, अत: धर्म ही सच्चा सहायक है। इसलिये
- **Translation**: 

---

### Verse 2 (Bramha 0.7342)
- **Original**: जीवका अनुसरण करता है। जब शरीरसे प्राण मनुष्योंको सदा धर्मका सेवन करना चाहिये।
- **Translation**: 

---

### Verse 3 (Bramha 0.7343)
- **Original**: निकल जाता है, तब त्वचा, हड्डी, मांस, वीर्य और धर्मयुक्त प्राणी उत्तम स्वर्गगतिको प्राप्त होता है,
- **Translation**: 

---

### Verse 4 (Bramha 0.7344)
- **Original**: रक्त भी उस शरीरको छोड़ देते हैं। उस समय जीव इसी प्रकार अधर्मयुक्त मानव नरकमें पड़ता है;
- **Translation**: 

---

### Verse 5 (Bramha 0.7345)
- **Original**: धर्मसे युक्त होनेपर ही इस लोक और परलोकमें अत; विद्वान्‌ पुरुष पापसे प्राप्त होनेवाले धनमें
- **Translation**: 

---

### Verse 6 (Bramha 0.7346)
- **Original**: सुख एवं अभ्युदयको प्राप्त होता है। अनुराग न रखे। एकमात्र धर्म ही मनुष्योंका
- **Translation**: 

---

### Verse 7 (Bramha 0.7347)
- **Original**: मुनियोने पूछा--भगवन्‌! आपने यह भलीभौंति * एक: प्रसूबते थिप्रा एक एव हि नश्यति । एकस्तरति दुर्गाणि गच्छस्पेकस्तु दुर्तिम्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.7348)
- **Original**: असहाय: पिता माता तथा प्राता सुतो गुरु:। ज्ञातिसम्बन्धिवर्गक्ष मित्रवर्गस्तवैव च
- **Translation**: 

---

### Verse 9 (Bramha 0.7349)
- **Original**: मृत शरीरम॒त्सृज्य काहलोप्टसम॑ जना:ः। मुहूर्तमिव रोदित्वा ततो यान्ति पराइ्सुखाः
- **Translation**: 

---

### Verse 10 (Bramha 0.7350)
- **Original**: तैस्तच्छरीरमुत्सुष्ट. धर्म एकोउनुगच्छति। तस्माद्धम: सहायक्ष सेवितव्य: सदा नृभि:
- **Translation**: 

---

### Verse 11 (Bramha 0.7351)
- **Original**: प्राणी धर्मसमायुक्तों गच्छेत्स्वर्गगतिं पराम्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.7352)
- **Original**: तथैवाथर्मसंयुछो. नरक॑ चोपपच्ते
- **Translation**: 

---

### Verse 13 (Bramha 0.7353)
- **Original**: तस्मात्पापागतैरथैंनानुरण्येत घण्डित:। धर्म एकों मनुष्याणां सहाय: परिकीर्तित:
- **Translation**: 

---

### Verse 14 (Bramha 0.7354)
- **Original**: लोभान्मोहादनुक्रोशाद्धयाद्वाथ यहुल्लुतः। तर: करोत्यकार्याणि परार्थे लोभमोहितः
- **Translation**: 

---

### Verse 15 (Bramha 0.7355)
- **Original**: धर्मक्षार्थक्1ष कामश्व॒त्रितय॑ जीवत: फलम्‌ । एतत्त्रयमवाप्तव्यमधर्मपरिवर्जितम्‌
- **Translation**: 

---

### Verse 16 (Bramha 0.7356)
- **Original**: (217। 4-11)
- **Translation**: 

---

### Verse 17 (Bramha 0.7357)
- **Original**: » धर्मकी महिमा एवं अधर्मकी गतिका निरूपण तथा अन्नदानका माहात्म्य * 357 समझा दिया कि धर्म किस प्रकार जीवका अनुसरण
- **Translation**: 

---

### Verse 18 (Bramha 0.7358)
- **Original**: एकको कन्या देनेकी प्रतिज्ञा करके फिर दूसरेको करता हैं। अब हम यह जानना चाहते हैं कि
- **Translation**: 

---

### Verse 19 (Bramha 0.7359)
- **Original**: देना चाहता है, वह भी मरनेपर कौड़ेकी योनिमें (शरीरके कारणभूत] बोर्यकी उत्पत्ति कैसे होती है।
- **Translation**: 

---

### Verse 20 (Bramha 0.7360)
- **Original**: जन्म पाता है। उस योनिमें बह तेरह वर्षोतक व्यासजीने कहा-द्विजवरों! शरीरमें स्थित ' जीवित रहता है। फिर अधर्मका क्षय होनेपर यह जो पृथ्वी, वायु, आकाश, जल, तेज और मनके
- **Translation**: 

---

