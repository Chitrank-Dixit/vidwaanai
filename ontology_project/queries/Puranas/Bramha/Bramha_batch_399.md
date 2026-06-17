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

### Verse 1 (Bramha 0.7961)
- **Original**: एवं स्वागतपूर्ण वचन बोलते हैं, वे मनुष्य किसीकी हिंसा नहीं करते तथा किसीके प्रति
- **Translation**: 

---

### Verse 2 (Bramha 0.7962)
- **Original**: स्वर्गलोकमें जानेके अधिकरी हैं। जो कठोर, आसक्त नहीं होते, वे कर्म-बन्धनमें नहीं पड़ते।
- **Translation**: 

---

### Verse 3 (Bramha 0.7963)
- **Original**: कड़बी तथा निष्ठुर ब्रात मुँहसे नहीं निकालते, जो प्राण-संहारसे दूर रहनेवाले, सुशील, दयालु,
- **Translation**: 

---

### Verse 4 (Bramha 0.7964)
- **Original**: चुगली नहीं खाते, साधुतासे रहते हैं, कठोर प्रिय और अप्रियको समान समझनेवाले तथा
- **Translation**: 

---

### Verse 5 (Bramha 0.7965)
- **Original**: भाषण और परद्रोह त्याग देते हैं तथा सम्पूर्ण जितेन्द्रिय हैं, वे भी कर्मोंसे नहीं बंधते। जो सब
- **Translation**: 

---

### Verse 6 (Bramha 0.7966)
- **Original**: भूतोंके प्रति सम एवं जितेन्द्रिय होते हैं, वे मनुष्य प्राणियोंपर दया रखते, सब जीवॉके लिये विश्वासपात्र
- **Translation**: 

---

### Verse 7 (Bramha 0.7967)
- **Original**: स्वर्गलोकमें जाते हैं। जो श्ठोंसे बात नहीं करते बने रहते और हिंसापूर्ण बर्तावका त्याग कर देते
- **Translation**: 

---

### Verse 8 (Bramha 0.7968)
- **Original**: विरुद्ध कर्मोंकों त्याग देते, कोमल बचन बोलते, हैं, वे मनुष्य स्वर्गलोकमें जानेवाले हैं। जो पराये
- **Translation**: 

---

### Verse 9 (Bramha 0.7969)
- **Original**: क्रोध न करके मनोहर वाणी मुँहसे निकालते और थनके प्रति कभी ममता नहों रखते और परायी
- **Translation**: 

---

### Verse 10 (Bramha 0.7970)
- **Original**: कुपित होनेपर भी शान्ति धारण करते हैं, वे मानव स्त्रियोंसे सदा दूर रहते हैं तथा जो धर्मत; प्राप्त
- **Translation**: 

---

### Verse 11 (Bramha 0.7971)
- **Original**: स्वर्गगामी होते हैं। देवि! यह वाणीद्वारा पाला अर्थका ही उपभोग करनेवाले हैं, वे मनुष्य
- **Translation**: 

---

### Verse 12 (Bramha 0.7972)
- **Original**: ज़ानेवाला धर्म है। शुभ तथा सत्य गुणोंवाले स्वर्गगामी होते हैं। जो परस्त्रियोंके प्रति सदा
- **Translation**: 

---

### Verse 13 (Bramha 0.7973)
- **Original**: विद्वान्‌ मनुष्योंकों सदा इसका सेवन करना चाहिये। माता, बहिन और पुत्रीका-सा बर्ताव करते हैं, वे
- **Translation**: 

---

### Verse 14 (Bramha 0.7974)
- **Original**: कल्याणि! मानसिक धर्मसे युक्त मनुष्य सदा मानव स्वर्गलोकमें जाते हैं। जो केवल अपनी ही
- **Translation**: 

---

### Verse 15 (Bramha 0.7975)
- **Original**: स्वर्गमें जाते हैं। मैं उनका वर्णन करता हूँ, सुनो। स्त्रीके प्रति अनुराग रखते, ऋतुंकाल आनेपर ही
- **Translation**: 

---

### Verse 16 (Bramha 0.7976)
- **Original**: निर्जन वनमें रखे हुए पराये धनपर जब दृष्टि पड़े, पत्नीके साथ समागम करते तथा विषय-सुखोंके
- **Translation**: 

---

### Verse 17 (Bramha 0.7977)
- **Original**: उस समय जो मनसे भी उसे लेना नहीं चाहते, वे उपभोगमें कभी आसक्त नहीं होते, वे ही मनुष्य
- **Translation**: 

---

### Verse 18 (Bramha 0.7978)
- **Original**: स्वर्गगामी होते हैं। इसी प्रकार जो परायी स्प्रियोंको स्थर्गलोकके यात्री होते हैं। जो अपने सदाचारके
- **Translation**: 

---

### Verse 19 (Bramha 0.7979)
- **Original**: एकान्तमें पाकर मनके द्वारा भी कामबश उन्हें नहीं कारण पण्यी स्त्रियोंकी ओरसे सदा आँखें बंद / ग्रहण करते, जो शत्रु और मित्रको सदा एक-चित्तसे किये रहते हैं, इन्द्रियोंकों अपने अधीन रखते और
- **Translation**: 

---

### Verse 20 (Bramha 0.7980)
- **Original**: अपनाते, शास्त्रोंका अध्ययन करते, पवित्र एवं शीलकी सदा रक्षा करते हैं, ब्रे मानव स्वर्गगामी
- **Translation**: 

---

