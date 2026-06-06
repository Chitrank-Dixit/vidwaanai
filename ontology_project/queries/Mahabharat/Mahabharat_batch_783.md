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

### Verse 1 (Mahabharat 941.7821)
- **Original**: किये रहो।' अन्तर्यामीकी प्रधानता और ब्रह्मरूपी बनेका वर्णन बह्णने कहा--प्रिये ! जगतका ञ्ञासक एक हीं है, सुनकर संब लोग अपनी-अपनी दिशा दूसरा नहीं। जो हृदयके भीतर विराजमान है, उस
- **Translation**: 

---

### Verse 2 (Mahabharat 941.7821)
- **Original**: किये रहो।' अन्तर्यामीकी प्रधानता और ब्रह्मरूपी बनेका वर्णन बह्णने कहा--प्रिये ! जगतका ञ्ञासक एक हीं है, सुनकर संब लोग अपनी-अपनी दिशा दूसरा नहीं। जो हृदयके भीतर विराजमान है, उस
- **Translation**: 

---

### Verse 3 (Mahabharat 941.7822)
- **Original**: (अपने-अपने स्थान) को चल दियें। फिर उन्होंने उस परमात्माकों ही मैं सबका झासक बतत्ता रहा हूँ। जैसे पानी
- **Translation**: 

---

### Verse 4 (Mahabharat 941.7822)
- **Original**: (अपने-अपने स्थान) को चल दियें। फिर उन्होंने उस परमात्माकों ही मैं सबका झासक बतत्ता रहा हूँ। जैसे पानी
- **Translation**: 

---

### Verse 5 (Mahabharat 941.7823)
- **Original**: उपदेशके अर्थपर जब विचार किया तो सबसे पहले सपोंकि डालू स्थानसे नीचेकी ओर प्रवाहित होता है, वैसे हीं उस
- **Translation**: 

---

### Verse 6 (Mahabharat 941.7823)
- **Original**: उपदेशके अर्थपर जब विचार किया तो सबसे पहले सपोंकि डालू स्थानसे नीचेकी ओर प्रवाहित होता है, वैसे हीं उस
- **Translation**: 

---

### Verse 7 (Mahabharat 941.7824)
- **Original**: पनमें दूसरोंको डँसनेका घाव पैदा हुंआ, असुरोमें परमात्माकी प्रेरणासे मैं जिस तरहके कार्यमें नियुक्त होता हूँ,
- **Translation**: 

---

### Verse 8 (Mahabharat 941.7824)
- **Original**: पनमें दूसरोंको डँसनेका घाव पैदा हुंआ, असुरोमें परमात्माकी प्रेरणासे मैं जिस तरहके कार्यमें नियुक्त होता हूँ,
- **Translation**: 

---

### Verse 9 (Mahabharat 941.7825)
- **Original**: स्वोधाविक दम्भका आविधांव हुआ तथा देवताओंने दानकों उसीका पालन करता रहता हूँ। एक हीं गुरु है दूसरा नहीं।
- **Translation**: 

---

### Verse 10 (Mahabharat 941.7825)
- **Original**: स्वोधाविक दम्भका आविधांव हुआ तथा देवताओंने दानकों उसीका पालन करता रहता हूँ। एक हीं गुरु है दूसरा नहीं।
- **Translation**: 

---

### Verse 11 (Mahabharat 941.7826)
- **Original**: और महर्षियोंने दमकों हीं अपनानेका निश्चय किया। इस जो हुदयमें स्थित है, उस परमात्माकों हो मैं गुरु बतल्ा रहा
- **Translation**: 

---

### Verse 12 (Mahabharat 941.7826)
- **Original**: और महर्षियोंने दमकों हीं अपनानेका निश्चय किया। इस जो हुदयमें स्थित है, उस परमात्माकों हो मैं गुरु बतल्ा रहा
- **Translation**: 

---

### Verse 13 (Mahabharat 941.7827)
- **Original**: प्रकार सर्प, देवता, ऋषि और दानव--ये सब एक हीं हूँ। एक ही बन्धु है, उससे भिन्न दूसरा कोई जन्धु नहीं है।
- **Translation**: 

---

### Verse 14 (Mahabharat 941.7827)
- **Original**: प्रकार सर्प, देवता, ऋषि और दानव--ये सब एक हीं हूँ। एक ही बन्धु है, उससे भिन्न दूसरा कोई जन्धु नहीं है।
- **Translation**: 

---

### Verse 15 (Mahabharat 941.7828)
- **Original**: उपदेशक गुरुके पास गये थे और एक हीं शब्दके उपदेझसे जो इृदयमें स्थित है, उस परपात्माकों ही मैं बच्चु कहता हूँ।
- **Translation**: 

---

### Verse 16 (Mahabharat 941.7828)
- **Original**: उपदेशक गुरुके पास गये थे और एक हीं शब्दके उपदेझसे जो इृदयमें स्थित है, उस परपात्माकों ही मैं बच्चु कहता हूँ।
- **Translation**: 

---

### Verse 17 (Mahabharat 941.7829)
- **Original**: उनकी बुद्धिका संस्कार हुआ तो भी उनके मनमें भिन्न-भिन्न उसीके उपदेशसे आन्यवगण बन्धुमान्‌ होते हैं और सप्तर्षि
- **Translation**: 

---

### Verse 18 (Mahabharat 941.7829)
- **Original**: उनकी बुद्धिका संस्कार हुआ तो भी उनके मनमें भिन्न-भिन्न उसीके उपदेशसे आन्यवगण बन्धुमान्‌ होते हैं और सप्तर्षि
- **Translation**: 

---

### Verse 19 (Mahabharat 941.7830)
- **Original**: प्रकास्के भाव उत्पन्न हो गये। श्रोता गुरुके कहे हुए स्थेंग आकाशपें प्रकाशित होते हैं। एक हीं ओता हैं दूसरा
- **Translation**: 

---

### Verse 20 (Mahabharat 941.7830)
- **Original**: प्रकास्के भाव उत्पन्न हो गये। श्रोता गुरुके कहे हुए स्थेंग आकाशपें प्रकाशित होते हैं। एक हीं ओता हैं दूसरा
- **Translation**: 

---

