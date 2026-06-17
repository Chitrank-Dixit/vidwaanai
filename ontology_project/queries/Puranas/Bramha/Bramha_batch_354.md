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

### Verse 1 (Bramha 0.7061)
- **Original**: तथा पापियोंके लिये अत्यन्त दुर्गम होता है।
- **Translation**: 

---

### Verse 2 (Bramha 0.7062)
- **Original**: » यमलोकके मार्ग और चारों द्वारोंका वर्णन * इड3 यपदूत पाशोंमें बाँधकर उसे खींचते और मुद्॒रोंसे
- **Translation**: 

---

### Verse 3 (Bramha 0.7063)
- **Original**: बारंधार चीखता-चिह्लाता है; तो भी दूषित कर्मवाले पीटते हुए उस विज्ञाल पथपर ले जाते हैं। यमदूतंकि , उस पापीको वे तोखे शूलों, मुद्ररों, खड़ग और अनेक रूप होते हैं। वे देखनेमें बड़े डरावने और
- **Translation**: 

---

### Verse 4 (Bramha 0.7064)
- **Original**: शक्तिके प्रहारों और वज्रमय भयंकर डंडॉसे समस्त प्राणियोंको भय पहुँचानेवाले होते हैं।
- **Translation**: 

---

### Verse 5 (Bramha 0.7065)
- **Original**: घायल करके जोर-जोरसे डाँटते हैं। कभी-कभी उनके मुख विकराल, नासिका टेढ़ी, आँखे तीन,
- **Translation**: 

---

### Verse 6 (Bramha 0.7066)
- **Original**: तो एक-एक पापीको अनेक यमदूत चारों ओरसे हि
- **Translation**: 

---

### Verse 7 (Bramha 0.7067)
- **Original**: घेरकर पीटते हैं। बेचारा जीव दुःखसे पीड़ित हो 2
- **Translation**: 

---

### Verse 8 (Bramha 0.7068)
- **Original**: मूरच्छित होकर इधर-उधर गिर पड़ता है; तथापि ये दूत उसे घसीटकर ले जाते हैं। कहीं भयभीत
- **Translation**: 

---

### Verse 9 (Bramha 0.7069)
- **Original**: होते, कहाँ त्रास पाते, कहाँ लड़खड़ाते और कहाँ दुःखसे करुण क्रन्दन करते हुए जोबॉकों उस
- **Translation**: 

---

### Verse 10 (Bramha 0.7070)
- **Original**: मार्गसे जाना पड़ता हैं। यमदूतोंकी फटकार
- **Translation**: 

---

### Verse 11 (Bramha 0.7071)
- **Original**: पड़नेसे थे उद्विग्र हो उठते हैं और भयसे विह्ल हो काँपते हुए शरोरसे दौड़ने लगते हैं। मार्गपर
- **Translation**: 

---

### Verse 12 (Bramha 0.7072)
- **Original**: कहीं कॉटे बिछे होते हैं और कुछ दूरतक तपी
- **Translation**: 

---

### Verse 13 (Bramha 0.7073)
- **Original**: हुई बालू मिलतो है। जिन भनुष्योंने दान नहों किया है, वे उस मार्गपर जलते हुए पैरोंसे चलते हैं। जीवहिंसक मनुष्यके सब ओर मरे हुए बकरोंकी लाशें पड़ी किक जिल्यका
- **Translation**: 

---

### Verse 14 (Bramha 0.7074)
- **Original**: होती हैं, जिनकी जली और फटी हुई चमड़ीसे मेदे 6: की.
- **Translation**: 

---

### Verse 15 (Bramha 0.7075)
- **Original**: और रक्तकी दुर्गन्ध आती रहती है। वे बेदनासे ठोड़ी, कपोल और मुख फैले हुए तथा ओठ लंबे ' पीड़ित हो जोर-जोरसे चीखते-चिह्लते हुए यममार्गकी होते हैं। वे अपने हाथोंमें विकराल एवं भयंकर
- **Translation**: 

---

### Verse 16 (Bramha 0.7076)
- **Original**: यात्रा करते हैं। शक्ति, भिन्दिपाल, खड्‌ग, तोमर, आयुध लिये रहते हैं। उन आयुधोंसे आगकी
- **Translation**: 

---

### Verse 17 (Bramha 0.7077)
- **Original**: बाण और तीखी नोकवाले शूलोंसे उनका अब्ज- लपटें निकलती रहती हैं। पाश, साँकल और
- **Translation**: 

---

### Verse 18 (Bramha 0.7078)
- **Original**: अड्ज बिदीर्ण कर दिया जाता है। कुत्ते, बाघ, भेड़िये डंडेसे भय पहुँचानेवाले, महाबली, महाभयंकर
- **Translation**: 

---

### Verse 19 (Bramha 0.7079)
- **Original**: और कौए उनके शरोरका मांस नोच-नोचकर खाते यमकिंकर यमराजको आज्ञासे प्राणियोंकी आयु , रहते हैं। मांस खानेवाले लोग उस मार्गपर चलते समाप्त होनेपर उन्हें लेनेके लिये आते हैं। जीव
- **Translation**: 

---

### Verse 20 (Bramha 0.7080)
- **Original**: समय आरेसे चीरे जाते हैं, सुअर अपनी दाढ़ोंसे यातना भोगनेके लिये अपने कर्मके अनुसार जो
- **Translation**: 

---

