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

### Verse 1 (Agni Puran 0.5641)
- **Original**: होती है
- **Translation**: 

---

### Verse 2 (Agni Puran 0.5642)
- **Original**: इस प्रकार आदि आग्रेय महाएराणमें “अष्ाक्षर-पूजा-विधि वर्णन” नामक तीन सौँं तीतवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 3 (Agni Puran 0.5643)
- **Original**: 303# #3ल+अशफशटॉए >> तीन सौ चारवाँ अध्याय पञ्चाक्षर-दीक्षा-विधान; पूजाके मन्त्र अग्निदेव कहते हैं-- मेष (न) सर्गि विष--
- **Translation**: 

---

### Verse 4 (Agni Puran 0.5644)
- **Original**: तत्पश्चात्‌ मूलमन्त्र, इष्ट-मूर्तिसम्बन्धी मन्त्र तथा विसर्ग युक्त मकार (मः ) बसे पहलेका अक्षर
- **Translation**: 

---

### Verse 5 (Agni Puran 0.5645)
- **Original**: अज्भसम्बन्धी मत्त्रोंद्रारा अक्षत छींटते हुए श और उसके साथ अक्षि--इकार (शि)
- **Translation**: 

---

### Verse 6 (Agni Puran 0.5646)
- **Original**: भूतापसारणपूर्वक रक्षात्मक क्रिया सम्पादित करे। दी्घोदक (वा) मर्त्‌ (य )--यह पश्ञाक्षर मन्त्र
- **Translation**: 

---

### Verse 7 (Agni Puran 0.5647)
- **Original**: फिर दूधमें चर पकाकर उसके तीन भाग करे। (नमः शिवाय' ) शिवस्वरूप तथा शिवप्रदाता
- **Translation**: 

---

### Verse 8 (Agni Puran 0.5648)
- **Original**: उनमेंसे एक भाग तो इष्टदेवताको निवेदित कर दे, है। इसके आदिमें 37 लगा देनेपर यह षडक्षर
- **Translation**: 

---

### Verse 9 (Agni Puran 0.5649)
- **Original**: दूसरे भागकी आहुति दे और तीसरा शिष्यसहित मन्त्र हो जाता है। इसका अर्चन (भजन) करके
- **Translation**: 

---

### Verse 10 (Agni Puran 0.5650)
- **Original**: स्वयं ग्रहण करे। फिर आचमन एवं सकलीकरण मनुष्य देवत्व आदि उत्तम फलोंको प्राप्त कर
- **Translation**: 

---

### Verse 11 (Agni Puran 0.5651)
- **Original**: करके आचार्य शिष्यको हृदय-मन्त्रसे अभिमन्त्रित लेता है
- **Translation**: 

---

### Verse 12 (Agni Puran 0.5652)
- **Original**: एक दन्तधावन दे, जो दूधवाले वृक्ष आदिका ज्ञानस्वरूप परब्रह्म ही परम बुद्धिरूप है। वही
- **Translation**: 

---

### Verse 13 (Agni Puran 0.5653)
- **Original**: काष्ठ हो। उससे दाँतोंका शोधन करके, उसे सबके हृदयमें शिवरूपसे विराजमान है। वह
- **Translation**: 

---

### Verse 14 (Agni Puran 0.5654)
- **Original**: चीरकर उसके द्वारा जीभ साफ करनेके बाद शक्तिभूत सर्वेश्वर ही ब्रह्मा आदि मूर्तियोंके भेदसे
- **Translation**: 

---

### Verse 15 (Agni Puran 0.5655)
- **Original**: धोकर पृथ्वीपर फेक दे
- **Translation**: 

---

### Verse 16 (Agni Puran 0.5656)
- **Original**: भिन्‍न-सा प्रतीत होता है। मन्त्रके अक्षर पाँच हैं,।, यदि पूर्वदिशासे फेंकनेपर वह दन्तकाष्ठ उत्तर भूतगण भी पाँच हैं तथा उनके मन्त्र और विषय
- **Translation**: 

---

### Verse 17 (Agni Puran 0.5657)
- **Original**: या पश्चिम दिशाकी ओर जाकर गिरे तो शुभ भी पाँच हैं। प्राण आदि वायु पाँच हैं। ज्ञानेन्द्रियाँ। होता है, अन्यथा अशुभ होता है। पुनः अपने और कर्मेन्द्रियाँ भी पाँच-पाँच हैं। ये सब-की-
- **Translation**: 

---

### Verse 18 (Agni Puran 0.5658)
- **Original**: सम्मुख आते हुए शिष्यको शिखाबन्धके' द्वारा सब वस्तुएँ पञ्माक्षर-ब्रह्मरूप हैं। इसी प्रकार यह
- **Translation**: 

---

### Verse 19 (Agni Puran 0.5659)
- **Original**: रक्षित करके ज्ञानी गुरु वेदीपर उसके साथ सब कुछ अश्टक्षर मन्त्ररूप भी है
- **Translation**: 

---

### Verse 20 (Agni Puran 0.5660)
- **Original**: कुशके बिस्तरपर सो जाय। शिष्य सोते समय दीक्षा-स्थानका मनत्रोच्चारणपूर्वक पश्चगव्यसे
- **Translation**: 

---

