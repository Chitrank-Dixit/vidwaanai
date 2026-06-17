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

### Verse 1 (Mahabharat 0.2261)
- **Original**: असलियतका ज्ञान रखनेवाला, सब कार्योकि करनेका ढंग होनेके कारण उन्हें पहलान न सके, इसीसे उनके विपरीत हो
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2261)
- **Original**: असलियतका ज्ञान रखनेवाला, सब कार्योकि करनेका ढंग होनेके कारण उन्हें पहलान न सके, इसीसे उनके विपरीत हो
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2262)
- **Original**: जाननेवाला तथा मनुष्योंमें सबसे बढ़कर उपायका जानकार शये और उल्हें राज्यका भाग देनेमें आपकी सम्पति नहीं हुईं।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2262)
- **Original**: जाननेवाला तथा मनुष्योंमें सबसे बढ़कर उपायका जानकार शये और उल्हें राज्यका भाग देनेमें आपकी सम्पति नहीं हुईं।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2263)
- **Original**: है, वह मनुष्य पण्डित कहलाता हैं। जिसकी वाणी कहीं चुधिप्ठिरमें करताका अभाव; दया, धर्म, सत्य तथा पराक्रम
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2263)
- **Original**: है, वह मनुष्य पण्डित कहलाता हैं। जिसकी वाणी कहीं चुधिप्ठिरमें करताका अभाव; दया, धर्म, सत्य तथा पराक्रम
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2264)
- **Original**: रुकती नहीं, जो विचित्र डंगसे बातचीत करता हैं; तकंमें है; ये आपमें पूज्यबुद्धि रखते हैं। इन्हीं सदगुणोंके कारण थे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2264)
- **Original**: रुकती नहीं, जो विचित्र डंगसे बातचीत करता हैं; तकंमें है; ये आपमें पूज्यबुद्धि रखते हैं। इन्हीं सदगुणोंके कारण थे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2265)
- **Original**: निपुण और प्रतिभाशाली है तथा जो ग्रन्धके तात्पयंकों झीधर सोच-विचारकर चुपचाप बहुत-से केश सह रहे हैं। आप
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2265)
- **Original**: निपुण और प्रतिभाशाली है तथा जो ग्रन्धके तात्पयंकों झीधर सोच-विचारकर चुपचाप बहुत-से केश सह रहे हैं। आप
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2266)
- **Original**: बता सकता है, यह पण्डित कहलाता है। जिसकी विद्या वुर्घोधन, शकुनि, कर्ण तथा दुःशासन-जैसे अयोग्य
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2266)
- **Original**: बता सकता है, यह पण्डित कहलाता है। जिसकी विद्या वुर्घोधन, शकुनि, कर्ण तथा दुःशासन-जैसे अयोग्य
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2267)
- **Original**: बुद्धिका अनुसरण करती है और बुद्धि विद्याका, तथा जो व्यक्तियोंपर राज्यका भार रखकर कैसे ऐश्वर्यवृद्धि चाहते हैं?
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2267)
- **Original**: बुद्धिका अनुसरण करती है और बुद्धि विद्याका, तथा जो व्यक्तियोंपर राज्यका भार रखकर कैसे ऐश्वर्यवृद्धि चाहते हैं?
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2268)
- **Original**: झि्ट पुरुवोकी मर्यादाका उल्लंघन नहीं करता, वही 'पण्डित' अपने वास्तविक स्वरूपका ज्ञान, उद्योग, दुःख सहनेकी दाक्ति
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2268)
- **Original**: झि्ट पुरुवोकी मर्यादाका उल्लंघन नहीं करता, वही 'पण्डित' अपने वास्तविक स्वरूपका ज्ञान, उद्योग, दुःख सहनेकी दाक्ति
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2269)
- **Original**: की पदवी पा सकता है। बिना पढ़े हीं गर्व करनेवाले, दरिद और शथर्ममें स्थिरता--ये गुण जिस मनुष्यको पुसुषार्थसे च्युत
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2269)
- **Original**: की पदवी पा सकता है। बिना पढ़े हीं गर्व करनेवाले, दरिद और शथर्ममें स्थिरता--ये गुण जिस मनुष्यको पुसुषार्थसे च्युत
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2270)
- **Original**: होकर भी बड़े-बड़े मनसूबे बाँधनेवाले और बिना काम किये नहीं करते, वही पण्डित कहलाता है। जो अच्छे कमोंका
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2270)
- **Original**: होकर भी बड़े-बड़े मनसूबे बाँधनेवाले और बिना काम किये नहीं करते, वही पण्डित कहलाता है। जो अच्छे कमोंका
- **Translation**: 

---

