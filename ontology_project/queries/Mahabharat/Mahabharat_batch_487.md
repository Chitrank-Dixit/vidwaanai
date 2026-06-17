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

### Verse 1 (Mahabharat 0.4861)
- **Original**: कुष्हारे छिये मैं जो कुछ चाहता हूँ, वह सब तुम्हें मिले। अब
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4861)
- **Original**: कुष्हारे छिये मैं जो कुछ चाहता हूँ, वह सब तुम्हें मिले। अब
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4862)
- **Original**: है जाओ और झौघ्र ही कर्णका नाझ करो।'
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4862)
- **Original**: है जाओ और झौघ्र ही कर्णका नाझ करो।'
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4863)
- **Original**: इस प्रकार धर्मराजको प्रसन्न करनेके अन्तर अर्जुनने
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4863)
- **Original**: इस प्रकार धर्मराजको प्रसन्न करनेके अन्तर अर्जुनने
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4864)
- **Original**: श्रीकृष्णसे कहा--“गोबिन्द ! अब मेरा रथ तैयार हो।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4864)
- **Original**: श्रीकृष्णसे कहा--“गोबिन्द ! अब मेरा रथ तैयार हो।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4865)
- **Original**: उसमें उत्तम घोड़े जोते जायँ और सब प्रकास्के अख-शख्त्र सजाकर रख दिये जायें फिर सूतपुत्रका वध करनेके लिये
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4865)
- **Original**: उसमें उत्तम घोड़े जोते जायँ और सब प्रकास्के अख-शख्त्र सजाकर रख दिये जायें फिर सूतपुत्रका वध करनेके लिये
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4866)
- **Original**: हें सकता था ? तुम्हारे पास दिव्याख्र हैं, तुममें फुर्ती है, आप ज्ञीत्र ही यात्रा करें।' अर्जुके ऐसा कहनेपर
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4866)
- **Original**: हें सकता था ? तुम्हारे पास दिव्याख्र हैं, तुममें फुर्ती है, आप ज्ञीत्र ही यात्रा करें।' अर्जुके ऐसा कहनेपर
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4867)
- **Original**: औलू है, युद्धक समय तुम्हें घबराहट नहीं होती, तुन्हे श्रीकृष्णने दारूकसे कहा--'तुम पार्थक कथनानुसार सारी
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4867)
- **Original**: औलू है, युद्धक समय तुम्हें घबराहट नहीं होती, तुन्हे श्रीकृष्णने दारूकसे कहा--'तुम पार्थक कथनानुसार सारी
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4868)
- **Original**: अँख्॒-शस्रोंका पूर्ण ज्ञान है। लक्ष्यको बेधने और तैयारी करो।' भगवानकी आज्ञा पाते ही दारूकने रथको
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4868)
- **Original**: अँख्॒-शस्रोंका पूर्ण ज्ञान है। लक्ष्यको बेधने और तैयारी करो।' भगवानकी आज्ञा पाते ही दारूकने रथको
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4869)
- **Original**: “रानेकी कला मालूम है। निश्ञाना मास्ते समय तुम्हारा सब सामरप्रियोंसे सुसज्जित करके उसमें घोड़े जोत दिये और
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4869)
- **Original**: “रानेकी कला मालूम है। निश्ञाना मास्ते समय तुम्हारा सब सामरप्रियोंसे सुसज्जित करके उसमें घोड़े जोत दिये और
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4870)
- **Original**: चित्त एकाग्र रहता है। तुम चाहो तो गय्यवों और उसे अर्जुंनके पास त्थकर खड़ा कर दिया। अजुँनने देखा,
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4870)
- **Original**: चित्त एकाग्र रहता है। तुम चाहो तो गय्यवों और उसे अर्जुंनके पास त्थकर खड़ा कर दिया। अजुँनने देखा,
- **Translation**: 

---

