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

### Verse 1 (Vishnu Puran 0.601)
- **Original**: उनके नाम ये हैं--धान, जौ, उड़द, गेहूँ, छोटे थान्य, प्रिय्युसप्तमा होते अष्टमास्तु कुलत्थका:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.602)
- **Original**: 24 । तिल, काँगनो और कुलूथी--ये आठ तथा ज््यामाक (सर्मा), नीवार, यनतिरू, गवेधु, वेणुयल और मर्करट (मक्का)
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.603)
- **Original**: 21--25)
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.604)
- **Original**: ये चौदह ग्राम्य और कनन्‍य ओषधियाँ यज्ञानुप्ठानकी सामग्री हैं और यज्ञ इनकी उत्पत्तिका प्रधान हेतु है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.605)
- **Original**: अज्ञोके सहित. ये ओषधियाँ प्रजाकों बुद्धिका परम कारण हैं इसलिये इहलोक-परलोकके ज्ञाता पुरुष यज्ञोंका अनुष्ठान किया करते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.606)
- **Original**: हे मुनिश्रेष्ठ ! नित्यप्रति किया जानेवाला यज्ञानुष्ठान मनुष्योंका परम उपकासक और उनके किये हुए पापॉको शान्त करनेवात्पर है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.607)
- **Original**: है महामुने ! जिनके चित्तमें कालकी गतिसे पापकता बीज बढ़ता है उन्हों लोगोंका चित्त यज़्में प्रवत नहीं होता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.608)
- **Original**: उन यज्ञके विरोधियोंने वैदिक मत, वेद और यज्ञादि कर्म--सभीकी निन्‍्दा की है। 30
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.609)
- **Original**: ने प्रवृत्तिमार्गका उच्छेद करनेवाफे ही थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.610)
- **Original**: हे धर्मवानॉमें श्रेष्ठ मैत्रेय ! इस प्रकार कृषि आदि जीविकाक॑ साधनोंके निश्चित हो जानेपर प्रजापति ब्रह्माजीने प्रजाकी रचना कर उनके स्थान और गुणोंके अनुसार
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.611)
- **Original**: मर्यीद' , नर्ण और आश्रमोंके धर्म तथा अपने धर्मका भली अ्कार पालन करनेवाले समस्त वर्णकरि लोक आदिकी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.612)
- **Original**: स्थारना की
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.613)
- **Original**: कर्मनिष्ठ क्राह्मणोंका स्थान पितृलोक हैं, युद्ध-क्षेत्रसे कभी न हटनेवाले क्षत्रियोंक्रा इन्द्रत्लेक है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.614)
- **Original**: तथा अपने धर्मका पालन करनेवाले वैज्योंका वायुलोक और सेवाथर्मपरायण चूद्रोंका गन्धर्वलोक है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.615)
- **Original**: अट्ठासी हजार ऊर्ध्वरिता मुनि हैं; उनका जो स्थान बताया गया है वहीं गुल्कुछवासी खह्मचारियोंका स्थान है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.616)
- **Original**: इसी प्रकार बनबासी वामप्रस्थोंका स्थान सप्तर्पिलेक, गृहस्थॉका पितुत्लेक और संय्यासियोंका ब्रह्मस्प्रेक है तथा आत्मानुभवसे तृप्त योगियोंका स्थान अमरपद (मोक्ष) है 37-38
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.617)
- **Original**: जो निरत्तर एकान्तसेजी और ब्रह्मचिन्तनमें मप्र रहनेबाले योगिजन हैं उनका जो परमस्थान है उसे पष्डितजन ही देख
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.618)
- **Original**: ] प्रथम अंश रेत गत्वा गत्वा निवर्तन्ते अन्द्रसूर्यादयों गरहाः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.619)
- **Original**: अद्याषि न निकर्तन्ते द्वादशाक्षरचिन्तका:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.620)
- **Original**: 40 तापमिस्नमश्धतापिल॑ पहारौरवरौरतौ । असिपन्रवर्न घोरं कालसूत्रमबीचिकम्‌
- **Translation**: 

---

