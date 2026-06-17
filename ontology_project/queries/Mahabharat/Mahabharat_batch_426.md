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

### Verse 1 (Mahabharat 0.4251)
- **Original**: ही करता हूँ--यह कहकर अजुंनने शेष संझ्प्तकोंका संहार काठटते छगे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4251)
- **Original**: ही करता हूँ--यह कहकर अजुंनने शेष संझ्प्तकोंका संहार काठटते छगे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4252)
- **Original**: कुछ भाग गये और बहुत-से गिरकर मर गये।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4252)
- **Original**: कुछ भाग गये और बहुत-से गिरकर मर गये।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4253)
- **Original**: आरकभ्भ किया । अर्जुन इतनी झौपतासे बाण हाथमें लेते, संघान अ्रुओंके घोड़े, सारथि, ध्वजा, धनुष, बाण, हाथ, हाथके
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4253)
- **Original**: आरकभ्भ किया । अर्जुन इतनी झौपतासे बाण हाथमें लेते, संघान अ्रुओंके घोड़े, सारथि, ध्वजा, धनुष, बाण, हाथ, हाथके
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4254)
- **Original**: हें सब बातोंको देख नहीं पाते थे। अर्जुनका हस्तलाघव देख हथियार; धघुजाएँ और मस्तक काट गिराये। इसी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4254)
- **Original**: हें सब बातोंको देख नहीं पाते थे। अर्जुनका हस्तलाघव देख हथियार; धघुजाएँ और मस्तक काट गिराये। इसी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4255)
- **Original**: सं भगवान्‌ श्रीकृष्ण भी आश्षर्यमें पड़ गये। उन्होंने अर्जुनसे रे,
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4255)
- **Original**: सं भगवान्‌ श्रीकृष्ण भी आश्षर्यमें पड़ गये। उन्होंने अर्जुनसे रे,
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4256)
- **Original**: क्रहा--'पार्थ ! इस पृथ्वीपर दुर्योधनके कारण राजाओंका यह
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4256)
- **Original**: क्रहा--'पार्थ ! इस पृथ्वीपर दुर्योधनके कारण राजाओंका यह
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4257)
- **Original**: महाभयंकर संहार हो रहा है। आज तुमने जो पराक्रम किया है
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4257)
- **Original**: महाभयंकर संहार हो रहा है। आज तुमने जो पराक्रम किया है
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4258)
- **Original**: बैसा स्वर्गमें केवल इच्ले हीं किया था।' इस प्रकार बातें करते
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4258)
- **Original**: बैसा स्वर्गमें केवल इच्ले हीं किया था।' इस प्रकार बातें करते
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4259)
- **Original**: हुए श्रीकृष्ण और अर्जुन चले जा रहे थे, इतनेहीमें उन्हें दुर्योधनकी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4259)
- **Original**: हुए श्रीकृष्ण और अर्जुन चले जा रहे थे, इतनेहीमें उन्हें दुर्योधनकी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4260)
- **Original**: सेनाके पास झ्ध, दुन्दुधि, भेरी और पणव आदि बाजोंकी 7 उल्ड
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4260)
- **Original**: सेनाके पास झ्ध, दुन्दुधि, भेरी और पणव आदि बाजोंकी 7 उल्ड
- **Translation**: 

---

