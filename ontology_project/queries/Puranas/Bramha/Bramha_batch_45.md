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

### Verse 1 (Bramha 0.881)
- **Original**: पर्बतॉंके नाम सुनो। कुमुद, उन्नत, वलाहक, द्रोण, व्याधियाँ भी नहीं सतातीं। वहाँ हर समय सुख
- **Translation**: 

---

### Verse 2 (Bramha 0.882)
- **Original**: कड्कू, महिष तथा पर्वतश्रेष्ठ ककुद्यानू-ये सात मिलता है। प्लक्षद्वीपके वर्षों सात ही ऐसी
- **Translation**: 

---

### Verse 3 (Bramha 0.883)
- **Original**: पर्वत हैं। इनमें द्रोणपर्वतपर कितनी ही महौषश्रियाँ नदियाँ हैं, जो समुद्रमें जा मिलती हैं। अनुतप्ता,
- **Translation**: 

---

### Verse 4 (Bramha 0.884)
- **Original**: हैं। नदियोंके नाम इस प्रकार हैं-- श्रोणी, तोया, शिखा, विप्राशा, त्रिदिवा, क्रमु, अमृता तथा
- **Translation**: 

---

### Verse 5 (Bramha 0.885)
- **Original**: वितृष्णा, चन्द्रा, शुक्रा, बिमोचनी तथा निवृत्ति। सुकृता-ये सात वहाँकौ नदियाँ हैं। इस प्रकार
- **Translation**: 

---

### Verse 6 (Bramha 0.886)
- **Original**: वहाँ श्वेत आदि सात वर्ष हैं, जिनमें चारों वर्णोंके प्लक्षद्वीपके प्रधान-प्रधान पर्वतों और नदियोंका
- **Translation**: 

---

### Verse 7 (Bramha 0.887)
- **Original**: लोग निबास करते हैं। शाल्मलद्वीपमें कपिल, वर्णन किया गया। छोटी-छोटी नदियाँ और छोटे-
- **Translation**: 

---

### Verse 8 (Bramha 0.888)
- **Original**: अरुण, पीत तथा कृष्ण वर्णके लोग होते हैं, जो छोटे पहाड़ तो वहाँ हजारों हैं। उन वर्षोंमें युगोंकी
- **Translation**: 

---

### Verse 9 (Bramha 0.889)
- **Original**: क्रमश: ब्राह्मण, क्षत्रिय, बैश्य और शूद्र माने जाते व्यवस्था नहीं है। वहाँ सदा ही त्रेतायुगके समान
- **Translation**: 

---

### Verse 10 (Bramha 0.890)
- **Original**: हैं। ये सब लोग यज्ञपरायण हो सबके आत्मा, समय रहता है। प्लक्षद्वीपसे लेकर शाकद्वीपतकके
- **Translation**: 

---

### Verse 11 (Bramha 0.891)
- **Original**: अविनाशी एवं यज्ञमें स्थित भगवान्‌ विष्णुकी लोग पाँच हजार वर्षोंतक नीरोग जीवन व्यतीत
- **Translation**: 

---

### Verse 12 (Bramha 0.892)
- **Original**: बायुरूपमें आराधना करते हैं। इस अत्यन्त मनोहर करते हैं। उन द्वापोंमें वर्णाश्रम-विभागपूर्वक चार
- **Translation**: 

---

### Verse 13 (Bramha 0.893)
- **Original**: ट्वीपमें देवताओंका सांनिध्य बना रहता है। वहाँ प्रकारका धर्म है तथा वहाँ चार ही वर्ण हैं,
- **Translation**: 

---

### Verse 14 (Bramha 0.894)
- **Original**: शाल्मलि नामका महान वृक्ष है, जो उस द्वीपके जिनके नाम इस प्रकार हैं--आर्यक, कुरु, विविश्व
- **Translation**: 

---

### Verse 15 (Bramha 0.895)
- **Original**: नामकरणका कारण बना है। यह द्वीप अपने तथा भावी। ये क्रमश: ब्राह्मण, क्षत्रिय, वैश्य तथा
- **Translation**: 

---

### Verse 16 (Bramha 0.896)
- **Original**: समान विस्तारवाले सुराके समुद्रसे घिरा हुआ है शूद्रकी कोटिके हैं। उस द्वीपके मध्यभागमें प्लक्ष
- **Translation**: 

---

### Verse 17 (Bramha 0.897)
- **Original**: और वह सुराका समुद्र शाल्मलट्टीपसे दुगुने (पाकड़) नामका बहुत विशाल वृक्ष है, जो! विस्तारवाले कुशद्वीपद्वारा सब ओरसे आवृत है। जम्बूद्वीपमें स्थित जम्बू (जामुन) वृक्षके ही बराबर
- **Translation**: 

---

### Verse 18 (Bramha 0.898)
- **Original**: कुशद्ठीपमें ज्योतिष्मान्‌ राजा हैं; अब उनके पुत्रोंके है। उसीके नामपर उस द्वीपका प्लक्षद्वीप नाम
- **Translation**: 

---

### Verse 19 (Bramha 0.899)
- **Original**: नाम बतलाये जाते हैं, सुनो-उद्धिद, वेणुमान्‌, रखा गया है। प्लक्षद्वीपमें आर्यक आदि वर्णोंके
- **Translation**: 

---

### Verse 20 (Bramha 0.900)
- **Original**: सुरथ, रन्धन, धृति, प्रभाकर और कपिल। इन्हींके लोग जगत्लष्टा सर्वेश्वर भगवान्‌ श्रीहरिका चन््रमाके
- **Translation**: 

---

