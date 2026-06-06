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

### Verse 1 (Mahabharat 941.8331)
- **Original**: अन्तर्धान हो गये और पाण्छव वीर दक्षिणाभिमुख होकर नारायण-स्वरूप भगवान्‌ श्रीकृष्णके प्रभावसे ही खाण्डव
- **Translation**: 

---

### Verse 2 (Mahabharat 941.8331)
- **Original**: अन्तर्धान हो गये और पाण्छव वीर दक्षिणाभिमुख होकर नारायण-स्वरूप भगवान्‌ श्रीकृष्णके प्रभावसे ही खाण्डव
- **Translation**: 

---

### Verse 3 (Mahabharat 941.8332)
- **Original**: चल दिये। जाते-जाते वे रूबणसमुद्रके उत्तर तटपर होते बनको जलाया था
- **Translation**: 

---

### Verse 4 (Mahabharat 941.8332)
- **Original**: चल दिये। जाते-जाते वे रूबणसमुद्रके उत्तर तटपर होते बनको जलाया था
- **Translation**: 

---

### Verse 5 (Mahabharat 941.8333)
- **Original**: तुम्हारे भाई अर्जुनको चाहिये कि ये इस
- **Translation**: 

---

### Verse 6 (Mahabharat 941.8333)
- **Original**: तुम्हारे भाई अर्जुनको चाहिये कि ये इस
- **Translation**: 

---

### Verse 7 (Mahabharat 941.8334)
- **Original**: हुए दक्षिण और पश्चिम दिशाकी ओर बढ़ने लगें। उत्तम अख्ा गाण्डीव धनुषकों यहीं छोड़कर वनमें जायें;
- **Translation**: 

---

### Verse 8 (Mahabharat 941.8334)
- **Original**: हुए दक्षिण और पश्चिम दिशाकी ओर बढ़ने लगें। उत्तम अख्ा गाण्डीव धनुषकों यहीं छोड़कर वनमें जायें;
- **Translation**: 

---

### Verse 9 (Mahabharat 941.8335)
- **Original**: तत्पक्षात्‌ केवल पश्चिम दिशाकी ओर मुड़ गये और क्योंकि अब इन्हें इसकी कोई आवश्यकता नहीं है। यह
- **Translation**: 

---

### Verse 10 (Mahabharat 941.8335)
- **Original**: तत्पक्षात्‌ केवल पश्चिम दिशाकी ओर मुड़ गये और क्योंकि अब इन्हें इसकी कोई आवश्यकता नहीं है। यह
- **Translation**: 

---

### Verse 11 (Mahabharat 941.8336)
- **Original**: आगे बढ़कर उन्होंने समुद्रमें डूबी हुई द्वारकापुरीकों गाण्डीव धनुष सब प्रकारके थुषोमें श्रेष्ठ है। इसे पहले मैं
- **Translation**: 

---

### Verse 12 (Mahabharat 941.8336)
- **Original**: आगे बढ़कर उन्होंने समुद्रमें डूबी हुई द्वारकापुरीकों गाण्डीव धनुष सब प्रकारके थुषोमें श्रेष्ठ है। इसे पहले मैं
- **Translation**: 

---

### Verse 13 (Mahabharat 941.8337)
- **Original**: देखा। फिर योग, धर्ममें स्थित पाण्डवॉने वहाँसे घूमकर अर्जुनके लिये ही बरुणसे मागकर ले आया था, अब पुनः । दृख्वोकी परिक्रय! पुरी करनको इच्छासे उनसे दिशाकतो और
- **Translation**: 

---

### Verse 14 (Mahabharat 941.8337)
- **Original**: देखा। फिर योग, धर्ममें स्थित पाण्डवॉने वहाँसे घूमकर अर्जुनके लिये ही बरुणसे मागकर ले आया था, अब पुनः । दृख्वोकी परिक्रय! पुरी करनको इच्छासे उनसे दिशाकतो और
- **Translation**: 

---

### Verse 15 (Mahabharat 941.8338)
- **Original**: इसे बरुणको ही वापस कर देना चाहिये।' यात्रा की । कफऋर्ज्- मार्गमें द्रौपदी तथा सहदेव आदि चार पाण्डबॉंका गिरना वैज्ञग्पायपजी कहते हैं--राजन्‌ ! नियमोंका पालन
- **Translation**: 

---

### Verse 16 (Mahabharat 941.8338)
- **Original**: इसे बरुणको ही वापस कर देना चाहिये।' यात्रा की । कफऋर्ज्- मार्गमें द्रौपदी तथा सहदेव आदि चार पाण्डबॉंका गिरना वैज्ञग्पायपजी कहते हैं--राजन्‌ ! नियमोंका पालन
- **Translation**: 

---

### Verse 17 (Mahabharat 941.8339)
- **Original**: पूछा--“भैया ! राजकुमारी ड्रौपदीने कभी कोई पाप करनेवाले योगयुक्त पाण्डबॉने पक्षिमंसे उत्तर दिझ्ामें आकर
- **Translation**: 

---

### Verse 18 (Mahabharat 941.8339)
- **Original**: पूछा--“भैया ! राजकुमारी ड्रौपदीने कभी कोई पाप करनेवाले योगयुक्त पाण्डबॉने पक्षिमंसे उत्तर दिझ्ामें आकर
- **Translation**: 

---

### Verse 19 (Mahabharat 941.8340)
- **Original**: नहीं किया था; फिर बताड़ये, क्या कारण है कि वह नीखे महागिरि हिमारूयका दर्शन किया। उसको लाँघकर जब वे
- **Translation**: 

---

### Verse 20 (Mahabharat 941.8340)
- **Original**: नहीं किया था; फिर बताड़ये, क्या कारण है कि वह नीखे महागिरि हिमारूयका दर्शन किया। उसको लाँघकर जब वे
- **Translation**: 

---

