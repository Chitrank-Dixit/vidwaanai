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

### Verse 1 (Agni Puran 0.4641)
- **Original**: पाया था और तभीसे यह हमारे उपयोगमें है', हो गया; उस दशामें वही अभियुक्त धनराशिसे
- **Translation**: 

---

### Verse 2 (Agni Puran 0.4642)
- **Original**: वही यहाँ पूर्ववादी है; जिसने पहले अभियोग दूना धन राजाकों आर्पित करे
- **Translation**: 

---

### Verse 3 (Agni Puran 0.4643)
- **Original**: दाखिल किया है, यह नहीं। यदि कोई यह कहे हत्या या डकैती-चोरी, वाक्पारुष्य (गाली-
- **Translation**: 

---

### Verse 4 (Agni Puran 0.4644)
- **Original**: कि 'ठीक है कि यह सम्पत्ति इसे दानमें मिली गलौज), दण्डपारुष्य (निर्दयतापूर्वक की हुई। थी और इसने इसका उपयोग भी किया है, मारपीट), दूध देनेवाली गायके अपहरण, अभिशाप
- **Translation**: 

---

### Verse 5 (Agni Puran 0.4645)
- **Original**: तथापि इसके यहाँसे अमुकने वह क्षेत्र-सम्पत्ति (पातकका अभियोग), अत्यय (प्राणघात) एवं
- **Translation**: 

---

### Verse 6 (Agni Puran 0.4646)
- **Original**: खरीद ली और उसने पुनः इसे मुझको दे दिया' धनातिपात तथा स्त्रियोंके चरित्न-सम्बन्धी विबाद
- **Translation**: 

---

### Verse 7 (Agni Puran 0.4647)
- **Original**: तब पूर्वपक्ष असाध्य होनेके कारण दुर्बल पड़ जाता प्राप्त होनेपर तत्काल अपराधीसे उत्तर माँगे,
- **Translation**: 

---

### Verse 8 (Agni Puran 0.4648)
- **Original**: है। ऐसा होनेपर उत्तरवादीके साक्षी ही प्रष्टव्य हैं; बिलम्ब न करे। अन्य प्रकारके विवादोंमें उत्तरदानका
- **Translation**: 

---

### Verse 9 (Agni Puran 0.4649)
- **Original**: उन्‍्हींकी गवाही ली जानी चाहिये
- **Translation**: 

---

### Verse 10 (Agni Puran 0.4650)
- **Original**: समय वादी, प्रतिवादी, सभासद्‌ तथा प्राइविवाककी
- **Translation**: 

---

### Verse 11 (Agni Puran 0.4651)
- **Original**: यदि विवाद किसी शर्तके साथ किया गया इच्छाके अनुसार रखा जा सकता है
- **Translation**: 

---

### Verse 12 (Agni Puran 0.4652)
- **Original**: हो, अर्थात्‌ यदि किसीने कहा हो कि “यदि में (दुश्ेंकी पहचान इस प्रकार करे--) अपना पक्ष सिद्ध न कर सकूँ तो पाँच सौ पण विषयमें बयान या गवाही देते समय जो अधिक दण्ड दूँगा, तब यदि वह पराजित हो जाय जगहसे दूसरी जगह जाता-आता है, स्थिर नहीं
- **Translation**: 

---

### Verse 13 (Agni Puran 0.4653)
- **Original**: तो उसके पूर्वकृत पणरूपी दण्डका धन राजाको रह पाता, दोनों गलफर चाटता है, जिसके भाल-
- **Translation**: 

---

### Verse 14 (Agni Puran 0.4654)
- **Original**: दिलवावे। परंतु जो अर्थी धनी है, उसे राजा विवादका देशमें पसीना हुआ करता है, चेहरेका रंग फीौका
- **Translation**: 

---

### Verse 15 (Agni Puran 0.4655)
- **Original**: आस्पदभूत धन हो दिलवाबे”
- **Translation**: 

---

### Verse 16 (Agni Puran 0.4656)
- **Original**: पड़ जाता है, गला सूखनेसे वाणी अटकने लगती
- **Translation**: 

---

### Verse 17 (Agni Puran 0.4657)
- **Original**: राजा छल छोड़कर वास्तविकताका आश्रय ले है, जो बहुत तथा पूर्वापर-विरुद्ध बातें कहा करता
- **Translation**: 

---

### Verse 18 (Agni Puran 0.4658)
- **Original**: व्यवहारोंका अन्तिम निर्णय करें। यथार्थ वस्तु है, जो दूसरेकी बातका ठीक-ठौक उत्तर नहीं दे
- **Translation**: 

---

### Verse 19 (Agni Puran 0.4659)
- **Original**: भी यदि लेखबद्ध न हुई हो तो व्यवहारमें वह पाता और किसीसे दृष्टि नहीं मिला पाता है, जो
- **Translation**: 

---

### Verse 20 (Agni Puran 0.4660)
- **Original**: पराजयका कारण बनती है। सुवर्ण, रजत और ओठ टेढ़े-मेढ़े किया करता है, इस प्रकार जो
- **Translation**: 

---

