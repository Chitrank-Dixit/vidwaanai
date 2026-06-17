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

### Verse 1 (Mahabharat 0.1461)
- **Original**: छ्स्पिः पूछा तो ब्राह्मणोंने उसे उसका स्थान बता दिया । वहाँ जाकर >अंडा3240
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1461)
- **Original**: छ्स्पिः पूछा तो ब्राह्मणोंने उसे उसका स्थान बता दिया । वहाँ जाकर >अंडा3240
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1462)
- **Original**: हे देखा कि धर्मव्याध कमाईखादेमे बेठकर मास बेच रहा है। हु नई ब्राह्मण एकान्तमें जाकर बैठ गया। व्याधको यह मालूम हो
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1462)
- **Original**: हे देखा कि धर्मव्याध कमाईखादेमे बेठकर मास बेच रहा है। हु नई ब्राह्मण एकान्तमें जाकर बैठ गया। व्याधको यह मालूम हो
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1463)
- **Original**: ब्राह्मणने प्रसन्न होकर कहा, 'ठीक है, ऐसा ही करो। जया कि कोई ब्राह्मण मुझसे मिलनेके लिये आये हैं, अतः
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1463)
- **Original**: ब्राह्मणने प्रसन्न होकर कहा, 'ठीक है, ऐसा ही करो। जया कि कोई ब्राह्मण मुझसे मिलनेके लिये आये हैं, अतः
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1464)
- **Original**: फिर आगे-आगे ब्राह्मण चला और पीछे-पीछे व्याथ । घरपर वह ज्ीघ्र ब्राह्मणके समीप आया और बोल्मा--'भगवन्‌ !
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1464)
- **Original**: फिर आगे-आगे ब्राह्मण चला और पीछे-पीछे व्याथ । घरपर वह ज्ीघ्र ब्राह्मणके समीप आया और बोल्मा--'भगवन्‌ !
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1465)
- **Original**: पहुँचकर धर्मव्याथने ब्राह्मणदेवताके पैर धोकर बैठनेको आपके चरणोमें प्रणाम है। मैं आपका स्वागत करता हूँ। मैं
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1465)
- **Original**: पहुँचकर धर्मव्याथने ब्राह्मणदेवताके पैर धोकर बैठनेको आपके चरणोमें प्रणाम है। मैं आपका स्वागत करता हूँ। मैं
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1466)
- **Original**: आसन दिया। उसपर बैठकर उसने व्याधसे कहा, हे तात ! ही बह व्याध है, जिसे ढैढ़ते हुए आपने यहाँतक आनेका कष्ट
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1466)
- **Original**: आसन दिया। उसपर बैठकर उसने व्याधसे कहा, हे तात ! ही बह व्याध है, जिसे ढैढ़ते हुए आपने यहाँतक आनेका कष्ट
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1467)
- **Original**: यह मांस बेचनेका काम तुम्हारे योग्य नहीं है। मुझे तो तुम्हारे किया-है। आपका भला हो
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1467)
- **Original**: यह मांस बेचनेका काम तुम्हारे योग्य नहीं है। मुझे तो तुम्हारे किया-है। आपका भला हो
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1468)
- **Original**: आज़ा दीजिये; मैं क्‍या सेवा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1468)
- **Original**: आज़ा दीजिये; मैं क्‍या सेवा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1469)
- **Original**: इस घोर कर्मसे बड़ा ब्रेक हो रहा है। कहूँ ? यह तो मैं जानता हैँ कि आप कैसे यहाँ पधारे हैं।उस
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1469)
- **Original**: इस घोर कर्मसे बड़ा ब्रेक हो रहा है। कहूँ ? यह तो मैं जानता हैँ कि आप कैसे यहाँ पधारे हैं।उस
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1470)
- **Original**: व्याथ बोत्मा--विप्रवर ! मैंने यह काम अपनी इच्छासे नहीं प्रतिब्रता स्लीने ही आपको मिथिलामें भेजा है।' डठाया है। यह धंधा मेरे कुलूमें दादों-परदादोंके समयसे चला व्याथकी बात सुनकर ब्राह्मण बड़े विस्मयमें पड़ा और
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1470)
- **Original**: व्याथ बोत्मा--विप्रवर ! मैंने यह काम अपनी इच्छासे नहीं प्रतिब्रता स्लीने ही आपको मिथिलामें भेजा है।' डठाया है। यह धंधा मेरे कुलूमें दादों-परदादोंके समयसे चला व्याथकी बात सुनकर ब्राह्मण बड़े विस्मयमें पड़ा और
- **Translation**: 

---

