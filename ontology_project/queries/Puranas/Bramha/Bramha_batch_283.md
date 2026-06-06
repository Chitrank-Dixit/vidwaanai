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

### Verse 1 (Bramha 0.5641)
- **Original**: हैं। यह सम्पूर्ण संसार आपसे ही अ्भुरित होता अड्भ भी आप हो हैं। आप अविनाशी, वेदोंके भी
- **Translation**: 

---

### Verse 2 (Bramha 0.5642)
- **Original**: है, अत: आप परम महान्‌ और सबसे उत्तम हैं। वेद (ज्ञेय तत्व), धाता, विधाता और समाहित
- **Translation**: 

---

### Verse 3 (Bramha 0.5643)
- **Original**: देव! आप सबसे ज्वेष्ट हैं, पुरुष हैं और आप ही रहनेवाले हैं। आप जलराशि समुद्र हैं। आप ही
- **Translation**: 

---

### Verse 4 (Bramha 0.5644)
- **Original**: दस प्राणवायुओंके रूपमें स्थित हैं। आप विश्वरूप उसके मूल हैं। आप ही धाठा और आप ही बसु हैं। आप
- **Translation**: 

---

### Verse 5 (Bramha 0.5645)
- **Original**: होकर चार भागोंमें स्थित हैं। अमृतस्वरूप होकर सैद्, आप घृलत्मा और आप इन्द्रियातीत हैं। आप
- **Translation**: 

---

### Verse 6 (Bramha 0.5646)
- **Original**: नौ भागोंके साथ झ्युलोकमें रहते हैं और नौ सबसे आगे चलनेवाले और गाँवके नेता हैं। आप . भागोंसहित सनातन पौरुषेय रूप धारण करके ही गरुड़् और आप ही आदिमान्‌ हैं। आप ही
- **Translation**: 

---

### Verse 7 (Bramha 0.5647)
- **Original**: अन्तरिक्षमें निवास करते हैं। आपके दो भाग संग्रह (लघु) और आप ही परम महान्‌ हैं। अपने
- **Translation**: 

---

### Verse 8 (Bramha 0.5648)
- **Original**: पृथ्वीमें स्थित हैं और चार भाग भी यहाँ हैं। मनको वशमें रखनेवाले और अपनी महिमासे
- **Translation**: 

---

### Verse 9 (Bramha 0.5649)
- **Original**: आपसे यज्ञोंकी उत्पत्ति होती है, जो जगतूमें वृष्टि कभी च्युत न होनेवाले भी आप ही हैं। आप
- **Translation**: 

---

### Verse 10 (Bramha 0.5650)
- **Original**: करनेवाले हैं। आपसे ही विराट्की उत्पत्ति हुई, यम और नियम हैं। आप प्रांशु (उन्नत शरीरवाले)
- **Translation**: 

---

### Verse 11 (Bramha 0.5651)
- **Original**: जो सम्पूर्ण ज़गत्‌के हृदयमें अन्तर्यामी पुरुषरूपसे और चतुर्भुज हैं। अन्न, अन्तरात्मा और परमात्मा
- **Translation**: 

---

### Verse 12 (Bramha 0.5652)
- **Original**: विराजमान हैं। वह विराट्‌ पुरुष अपने तेज, यश भी आप हो कहलाते हैं। आप गुरु और गुरुतम , और ऐश्वर्यक कारण सम्पूर्ण भूतोंसे विशिष्ट है। हैं, बाम और दक्षिण हैं। आप ही पीपल एवं
- **Translation**: 

---

### Verse 13 (Bramha 0.5653)
- **Original**: आपसे ही देवताओंका आहारभूत हवनीय घृत
- **Translation**: 

---

### Verse 14 (Bramha 0.5654)
- **Original**: 272 + संक्षिप्त ग्रह्मपुराण + उत्पन्न हुआ। ग्राम्य और जंगली ओषधियाँ तथा
- **Translation**: 

---

### Verse 15 (Bramha 0.5655)
- **Original**: करनेवाले हैं, आपको नमस्कार है। प्रभो। आप पशु एवं मृग आदि भी आपसे हो प्रकट हुए हैं।
- **Translation**: 

---

### Verse 16 (Bramha 0.5656)
- **Original**: पृथ्वीको ऊपर उठानेके लिये विशाल कच्छपका देवदेव! आप ध्येय और ध्यानसे परे हैं। आपने
- **Translation**: 

---

### Verse 17 (Bramha 0.5657)
- **Original**: शरीर धारण करनेवाले हैं, आपने अपनी पीठपर ही ओषधियोंको उत्पन्न किया है। आप ही सात
- **Translation**: 

---

### Verse 18 (Bramha 0.5658)
- **Original**: मन्दराचलकों धारण किया था। महाकूर्मस्वरूप मुखोंवाले देदीप्यमान विग्रहसे युक्त काल हैं। यह
- **Translation**: 

---

### Verse 19 (Bramha 0.5659)
- **Original**: आप भगवान्‌को नमस्कार है। पृथ्वीका उद्धार स्थावर और जड्गम तथा चर और अचर सम्पूर्ण
- **Translation**: 

---

### Verse 20 (Bramha 0.5660)
- **Original**: करनेवाले महावराहकों नमस्कार है। भगवन्‌। जगत्‌ आपसे ही प्रकट हुआ है और आपमें ही
- **Translation**: 

---

