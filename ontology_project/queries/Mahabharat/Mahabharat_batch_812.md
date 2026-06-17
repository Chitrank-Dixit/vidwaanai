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

### Verse 1 (Mahabharat 941.8111)
- **Original**: दर संक्षिप्त [ आश्रमेधिकपर्त डालनेका विधान इस प्रकार है--) गोमाताके सामने घास
- **Translation**: 

---

### Verse 2 (Mahabharat 941.8111)
- **Original**: दर संक्षिप्त [ आश्रमेधिकपर्त डालनेका विधान इस प्रकार है--) गोमाताके सामने घास
- **Translation**: 

---

### Verse 3 (Mahabharat 941.8112)
- **Original**: और सबेरे तिलका उबटन लगाकर स्नान करे तथा सदा ही रखकर इस प्रकार कहना चाहिये--'संसारकी समस्त गौएँ!
- **Translation**: 

---

### Verse 4 (Mahabharat 941.8112)
- **Original**: और सबेरे तिलका उबटन लगाकर स्नान करे तथा सदा ही रखकर इस प्रकार कहना चाहिये--'संसारकी समस्त गौएँ!
- **Translation**: 

---

### Verse 5 (Mahabharat 941.8113)
- **Original**: अपने मुँहसे 'तिलन-तिल'का उच्चारण किया करे; क्योंकि तिल मेरी माताएँ और सम्पूर्ण वृषभ मेरे पिता हैं। गोमाताओ ! मैंने
- **Translation**: 

---

### Verse 6 (Mahabharat 941.8113)
- **Original**: अपने मुँहसे 'तिलन-तिल'का उच्चारण किया करे; क्योंकि तिल मेरी माताएँ और सम्पूर्ण वृषभ मेरे पिता हैं। गोमाताओ ! मैंने
- **Translation**: 

---

### Verse 7 (Mahabharat 941.8114)
- **Original**: सब पापोंको नष्ट करनेवाले होते हैं। द्विजातियोंकों तिल तुम्हारी सेवायें यह घासकी मुट्ठी अर्पण की है, इसे स्वीकार
- **Translation**: 

---

### Verse 8 (Mahabharat 941.8114)
- **Original**: सब पापोंको नष्ट करनेवाले होते हैं। द्विजातियोंकों तिल तुम्हारी सेवायें यह घासकी मुट्ठी अर्पण की है, इसे स्वीकार
- **Translation**: 

---

### Verse 9 (Mahabharat 941.8115)
- **Original**: खरीदकर या दानमें लेकर बेचना नहीं चाहिये
- **Translation**: 

---

### Verse 10 (Mahabharat 941.8115)
- **Original**: खरीदकर या दानमें लेकर बेचना नहीं चाहिये
- **Translation**: 

---

### Verse 11 (Mahabharat 941.8116)
- **Original**: जो तिलोंका करो ।' * यह मत्र पढ़कर अथवा गायत्रीका उच्चारण कस्के
- **Translation**: 

---

### Verse 12 (Mahabharat 941.8116)
- **Original**: जो तिलोंका करो ।' * यह मत्र पढ़कर अथवा गायत्रीका उच्चारण कस्के
- **Translation**: 

---

### Verse 13 (Mahabharat 941.8117)
- **Original**: भोजन करने; उबटन रूगाने और-दान देनेके अतिरिक्त और एकाग्रचित्तसे घासको अभिमन्त्रित करके गौको खिला दे;
- **Translation**: 

---

### Verse 14 (Mahabharat 941.8117)
- **Original**: भोजन करने; उबटन रूगाने और-दान देनेके अतिरिक्त और एकाग्रचित्तसे घासको अभिमन्त्रित करके गौको खिला दे;
- **Translation**: 

---

### Verse 15 (Mahabharat 941.8118)
- **Original**: किसी काममें उपयोग करता है, वह कौड़ा होकरंःअपने ऐसा करनेसे जिस पुण्यफलकी प्राप्ति होती है; उसे सुनो । उस
- **Translation**: 

---

### Verse 16 (Mahabharat 941.8118)
- **Original**: किसी काममें उपयोग करता है, वह कौड़ा होकरंःअपने ऐसा करनेसे जिस पुण्यफलकी प्राप्ति होती है; उसे सुनो । उस
- **Translation**: 

---

### Verse 17 (Mahabharat 941.8119)
- **Original**: पितरोंके साथ कुत्तेकी विष्ठामें डूबता है। ग्राह्मणको स्वय॑ तिल पुरुषने जान-बूझकर या अनजानमें जो-जो पाप किये होते हैं,
- **Translation**: 

---

### Verse 18 (Mahabharat 941.8119)
- **Original**: पितरोंके साथ कुत्तेकी विष्ठामें डूबता है। ग्राह्मणको स्वय॑ तिल पुरुषने जान-बूझकर या अनजानमें जो-जो पाप किये होते हैं,
- **Translation**: 

---

### Verse 19 (Mahabharat 941.8120)
- **Original**: पेर्नेकी मझीनमें तिल डालकर तेल नहीं पेरना चाहिये। जो वह सब नष्ट हो जाते हैं तथा उसको कभी बुरे स्वप्न नहीं
- **Translation**: 

---

### Verse 20 (Mahabharat 941.8120)
- **Original**: पेर्नेकी मझीनमें तिल डालकर तेल नहीं पेरना चाहिये। जो वह सब नष्ट हो जाते हैं तथा उसको कभी बुरे स्वप्न नहीं
- **Translation**: 

---

