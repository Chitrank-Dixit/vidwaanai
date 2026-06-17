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

### Verse 1 (Mahabharat 0.4521)
- **Original**: और मित्र हो। इन तीन कारणोंसे ही अबतक जीवित बच्चे उसके स्वामी ब्राह्मणने कहा, चूँकि तुमने इस निरफराध
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4521)
- **Original**: और मित्र हो। इन तीन कारणोंसे ही अबतक जीवित बच्चे उसके स्वामी ब्राह्मणने कहा, चूँकि तुमने इस निरफराध
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4522)
- **Original**: हुए हो। इस समय मेरे सामने राजा दुर्योधनका बड़ा भारी होमघेंनुके बश्लेको मारा है, इसलिये संग्राममें लड़ते-लड़ते
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4522)
- **Original**: हुए हो। इस समय मेरे सामने राजा दुर्योधनका बड़ा भारी होमघेंनुके बश्लेको मारा है, इसलिये संग्राममें लड़ते-लड़ते
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4523)
- **Original**: काम है और उसकी जिम्मेवारी भी मेरे ही ऊपर है। मैं तुम्हारे तुष्हारें र्थकां पहिया गडढ़ेमें फैंस जायगा और तुम बड़ी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4523)
- **Original**: काम है और उसकी जिम्मेवारी भी मेरे ही ऊपर है। मैं तुम्हारे तुष्हारें र्थकां पहिया गडढ़ेमें फैंस जायगा और तुम बड़ी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4524)
- **Original**: कठोर वचनोंकों क्षमा करनेकी प्रतिज्ञा कर चुका हूँ। ऑआपत्तिमें फैस जाओगे। ब्राह्मणके उस प्रबल झापसे मुझे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4524)
- **Original**: कठोर वचनोंकों क्षमा करनेकी प्रतिज्ञा कर चुका हूँ। ऑआपत्तिमें फैस जाओगे। ब्राह्मणके उस प्रबल झापसे मुझे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4525)
- **Original**: झत्रुओपर विजय तो तुम-जैसे हजारों झल्योंकी सहायताके अआर्ज भी भय बना हुआ है। उस ब्राह्मणकों मैंने हजार गौएँ ' बिना भी मैं पा सकता हूँ। किंतु मित्रसे द्रोह्ट करना बड़ा पाप और छः सौ बैल देने चाहे, परंतु मैं उसे प्रसन्न न कर सका।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4525)
- **Original**: झत्रुओपर विजय तो तुम-जैसे हजारों झल्योंकी सहायताके अआर्ज भी भय बना हुआ है। उस ब्राह्मणकों मैंने हजार गौएँ ' बिना भी मैं पा सकता हूँ। किंतु मित्रसे द्रोह्ट करना बड़ा पाप और छः सौ बैल देने चाहे, परंतु मैं उसे प्रसन्न न कर सका।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4526)
- **Original**: हैं, इसीसे तुम अबतक बचे हुए हो।' मैं बड़े सत्कारपूर्वक्क उस ब्राह्मणको अपना भरा-पूणर
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4526)
- **Original**: हैं, इसीसे तुम अबतक बचे हुए हो।' मैं बड़े सत्कारपूर्वक्क उस ब्राह्मणको अपना भरा-पूणर
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4527)
- **Original**: . शल्यने कहा--कर्ण ! तुम अपने शत्रुओंके विषयमें जो
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4527)
- **Original**: . शल्यने कहा--कर्ण ! तुम अपने शत्रुओंके विषयमें जो
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4528)
- **Original**: 28 संक्षिप्त महाभारत [ कर्णपर्व कुछ कह रहे हो वह सब तो तुम्हारा बकवाद ही है। मैं
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4528)
- **Original**: 28 संक्षिप्त महाभारत [ कर्णपर्व कुछ कह रहे हो वह सब तो तुम्हारा बकवाद ही है। मैं
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4529)
- **Original**: तथा सोजीर देश प्रायः निन्दित और अपविज्र माने गये: हैं। सहस्नों कणोंकी सहायताके बिना भी युद्धमें झन्नुओंको जीत
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4529)
- **Original**: तथा सोजीर देश प्रायः निन्दित और अपविज्र माने गये: हैं। सहस्नों कणोंकी सहायताके बिना भी युद्धमें झन्नुओंको जीत
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4530)
- **Original**: पाप्लाल देशके लोग बेदोंका स्वाध्यायः करते हैं, कुरू देझके सकता हैँ। निवासी धर्मका आश्रय छेते है। मत्य देशके लोग सत्यवादी मद्ग॒राजके इस प्रकार कहनेपर कर्ण उनसे दूने कटुवाक्य
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4530)
- **Original**: पाप्लाल देशके लोग बेदोंका स्वाध्यायः करते हैं, कुरू देझके सकता हैँ। निवासी धर्मका आश्रय छेते है। मत्य देशके लोग सत्यवादी मद्ग॒राजके इस प्रकार कहनेपर कर्ण उनसे दूने कटुवाक्य
- **Translation**: 

---

