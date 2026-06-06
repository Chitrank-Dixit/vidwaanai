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

### Verse 1 (Mahabharat 0.5851)
- **Original**: समय वहाँ सहसा सभी ख्त्रियाँ रो पड़ीं। इसके बाद कुरुराज बाहुबलका भरोसा रखते हैं, उसी प्रकार-कोरवोंको तो
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5851)
- **Original**: समय वहाँ सहसा सभी ख्त्रियाँ रो पड़ीं। इसके बाद कुरुराज बाहुबलका भरोसा रखते हैं, उसी प्रकार-कोरवोंको तो
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5852)
- **Original**: युथ्िष्ठिस्ने भ्रातृप्रेमयश कर्णकी सब खियोंको वहाँ उन्हींके बलका भरोसा था। ओह ! इस रहस्पको छिपाकर तो
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5852)
- **Original**: युथ्िष्ठिस्ने भ्रातृप्रेमयश कर्णकी सब खियोंको वहाँ उन्हींके बलका भरोसा था। ओह ! इस रहस्पको छिपाकर तो
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5853)
- **Original**: बुलवाया और उनको साथ लेकर झाखविधिसे कर्णका आपके हमारा सत्यानाझ ही कर दिया। आज कर्णकी मृत्युसे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5853)
- **Original**: बुलवाया और उनको साथ लेकर झाखविधिसे कर्णका आपके हमारा सत्यानाझ ही कर दिया। आज कर्णकी मृत्युसे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5854)
- **Original**: ्रेतकर्म किया। फिर वे कहने छूगे, “मैं बड़ा पापी हूँ, हम सभी भाइयोंको बड़ा दुःख हो रहा है। अभिमन्यु,
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5854)
- **Original**: ्रेतकर्म किया। फिर वे कहने छूगे, “मैं बड़ा पापी हूँ, हम सभी भाइयोंको बड़ा दुःख हो रहा है। अभिमन्यु,
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5855)
- **Original**: मैंने न जाननेके कारण ही अपने बड़े भाईंका वध करा दिया। ड्रौपदीके पुत्र, पाक्नालबीर और करवोंके मारे जानेसे मुझे
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5855)
- **Original**: मैंने न जाननेके कारण ही अपने बड़े भाईंका वध करा दिया। ड्रौपदीके पुत्र, पाक्नालबीर और करवोंके मारे जानेसे मुझे
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5856)
- **Original**: अतः उनकी पत्नियोंके हृदयमें मेरे प्रति कोई छिया जितना दुःख है, उससे सौगुना कर्णकी मृत्युसे हो रहा है। अब
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5856)
- **Original**: अतः उनकी पत्नियोंके हृदयमें मेरे प्रति कोई छिया जितना दुःख है, उससे सौगुना कर्णकी मृत्युसे हो रहा है। अब
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5857)
- **Original**: हुआ द्वेष हो तो बह दूर हो जाना चाहिये।' ऐसा कहकर तो मुझे कर्णका ही शोक है, उससे मैं ऐसे जल रहा हूँ मानो
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5857)
- **Original**: हुआ द्वेष हो तो बह दूर हो जाना चाहिये।' ऐसा कहकर तो मुझे कर्णका ही शोक है, उससे मैं ऐसे जल रहा हूँ मानो
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5858)
- **Original**: वे विकलत चित्तसे गड्भाजीसे बाहर निकले और अपने सब किसीने आग लगा दी हो । यदि हमें यह बात मालूम होती तो
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5858)
- **Original**: वे विकलत चित्तसे गड्भाजीसे बाहर निकले और अपने सब किसीने आग लगा दी हो । यदि हमें यह बात मालूम होती तो
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5859)
- **Original**: भाइयोंके सहित तटपर आये। जज औ- ख्रीपर्व समाप्त
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5859)
- **Original**: भाइयोंके सहित तटपर आये। जज औ- ख्रीपर्व समाप्त
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5860)
- **Original**: श्रीगणेशाय नमः
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5860)
- **Original**: श्रीगणेशाय नमः
- **Translation**: 

---

