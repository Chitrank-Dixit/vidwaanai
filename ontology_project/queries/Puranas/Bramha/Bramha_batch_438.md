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

### Verse 1 (Bramha 0.8741)
- **Original**: ही गुणस्वरूप कहलाता है। गुण तो गुणवानमें ही .. यसिप्तजी बोले--राजन्‌! तुम्हारा कहना ठीक
- **Translation**: 

---

### Verse 2 (Bramha 0.8742)
- **Original**: रहते हैं, निर्गुण आत्मामें गुण कैसे रह सकते हैं। है, तुमने वेद और शास्त्रोंका दृष्टान्त देकर अपना
- **Translation**: 

---

### Verse 3 (Bramha 0.8743)
- **Original**: अतः गुणोंके स्वरूपको जाननेवाले विद्वान्‌ पुरुष प्रश्न उपस्थित किया है तथापि अभी ग्रन्थका
- **Translation**: 

---

### Verse 4 (Bramha 0.8744)
- **Original**: ऐसा मानते हैं कि जब जीवात्मा इन प्राकृत गुणोंमें यथार्थ तत्त्व तुम्होरें समझमें नहों आया है। जो
- **Translation**: 

---

### Verse 5 (Bramha 0.8745)
- **Original**: अपनेपनका अभिमान करता है, उस समय वह बेद और शास्त्रोंके ग्रन्थोंको रट लेता है किंतु
- **Translation**: 

---

### Verse 6 (Bramha 0.8746)
- **Original**: गुणवान्‌-सा ही होकर भिन्न-भिन्न गुणोंको देखता उसके तत्वको नहीं समझता, उसका वह रटना
- **Translation**: 

---

### Verse 7 (Bramha 0.8747)
- **Original**: है। किंतु जब उस अभिमानको छोड़ देता है, उस व्यर्थ है। जो याद किये हुए ग्रन्थका अर्थ नहीं
- **Translation**: 

---

### Verse 8 (Bramha 0.8748)
- **Original**: समय देहादिमें आत्मबुद्धिका परित्याग करके जानता, यह तो केवल उसका बोझ ढोता है।
- **Translation**: 

---

### Verse 9 (Bramha 0.8749)
- **Original**: अपने विशुद्ध परमात्मस्वरूपका साक्षात्कार करता उसके तत्त्वका यथार्थ बोध होनेसे ही वह उसके
- **Translation**: 

---

### Verse 10 (Bramha 0.8750)
- **Original**: है। उस परमात्माको बुद्धि आदिसे परे सांख्य- अर्थको ग्रहण कर सकता है। जिसको बुद्धि स्थूल
- **Translation**: 

---

### Verse 11 (Bramha 0.8751)
- **Original**: योगस्वरूप बताया गया है। वह सत्वादि गुणोंसे और मन्द है, अतएब जो ग्रन्थके तत््वको ठीक-
- **Translation**: 

---

### Verse 12 (Bramha 0.8752)
- **Original**: रहित, अव्यक्त, ईश्रर (नियामक), निर्षुण, नित्य ठीक जाननेके लिये उत्सुक नहीं है, बह उस
- **Translation**: 

---

### Verse 13 (Bramha 0.8753)
- **Original**: तथा प्रकृति और उसके गुणोंका अधिष्ठाता पच्चीसवाँ ग्रन्थक्रे विषयका निर्णय कैसे कर सकता है। जो
- **Translation**: 

---

### Verse 14 (Bramha 0.8754)
- **Original**: तत्त्व है। यह सांख्य और योगमें कुशल एवं परम मनुष्य ग्रन्थके तत््वको जाने बिना हो लोभ अथवा
- **Translation**: 

---

### Verse 15 (Bramha 0.8755)
- **Original**: तत््वकी खोज करनेवाले विद्वानॉँका कथन है। इस दम्भवश , उसपर विवाद करता है, वह पापी
- **Translation**: 

---

### Verse 16 (Bramha 0.8756)
- **Original**: प्रकार परस्पर सम्बन्ध रखनेवाले क्षर-अक्षर ( प्रकृति- नरकमें पड़ता है। इसलिये महाराज! सांख्य और
- **Translation**: 

---

### Verse 17 (Bramha 0.8757)
- **Original**: पुरुष)-का स्वरूप बताया गया। सदा एक रूपमें योगके ज्ञाता महात्या पुरुषोंके मतमें मोक्षका जैसा , रहनेवाला परमात्मा अक्षर है और नाना रूपोमें स्वरूप देखा जाता है, उसे मैं यधार्थरूपसे
- **Translation**: 

---

### Verse 18 (Bramha 0.8758)
- **Original**: प्रतीत होनेवाला प्राकृत जगत्‌ क्षर कहलाता है। बतलाता हूँ; सुनो। योगो जिस तत्त्वका साक्षात्कार
- **Translation**: 

---

### Verse 19 (Bramha 0.8759)
- **Original**: सारांश यह कि एकत्व ही अक्षर है और
- **Translation**: 

---

### Verse 20 (Bramha 0.8760)
- **Original**: > क्षर-अक्षर तथा योग और सांख्यका वर्णन 419 24909 विलनिनननलललि्क मम्मे मन भससरशपश मय स यम मरना फजम मरना रन स सम "मम. सम शी तर डी घर नानात्वको ही क्षर कहते हैं। जब जीवात्मा
- **Translation**: 

---

