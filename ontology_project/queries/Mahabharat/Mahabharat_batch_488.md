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

### Verse 1 (Mahabharat 0.4871)
- **Original**: देबताओंसहित सम्पूर्ण खराखर जगतका नाश कर सकते वारुक रथ जोतकर ले आया, तो उन्होंने धर्मराजसे आज्ञा
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4871)
- **Original**: देबताओंसहित सम्पूर्ण खराखर जगतका नाश कर सकते वारुक रथ जोतकर ले आया, तो उन्होंने धर्मराजसे आज्ञा
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4872)
- **Original**: हों ? इस धूमण्डलपर तुम्हारे समान योद्धा है ही नहीं। ली. और ब्राह्मणों्रारा स्वस्तिवाचम कराकर वे अपने
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4872)
- **Original**: हों ? इस धूमण्डलपर तुम्हारे समान योद्धा है ही नहीं। ली. और ब्राह्मणों्रारा स्वस्तिवाचम कराकर वे अपने
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4873)
- **Original**: व्रह्माजीने प्रजाकी सृष्टि करनेके पश्चात्‌ इस महान्‌ गाण्डीज मडुलूमय रथपर विराजमान हुए। उस समय थधर्मराज
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4873)
- **Original**: व्रह्माजीने प्रजाकी सृष्टि करनेके पश्चात्‌ इस महान्‌ गाण्डीज मडुलूमय रथपर विराजमान हुए। उस समय थधर्मराज
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4874)
- **Original**: धनुषकी भी रचना की थी, जिससे तुम युद्ध करते हो, युथ्चिष्ठिस्ते अर्जुनको आझ्लीर्बाद दिये। तत्पश्चात्‌ अजुन । इसलिये तुम्हारी बराबरी करनेवाल्मा कोई नहीं है। तो भी कर्णके रथकी ओर चल दिये। कुछ दूर जानेपर उनके मनमें
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4874)
- **Original**: धनुषकी भी रचना की थी, जिससे तुम युद्ध करते हो, युथ्चिष्ठिस्ते अर्जुनको आझ्लीर्बाद दिये। तत्पश्चात्‌ अजुन । इसलिये तुम्हारी बराबरी करनेवाल्मा कोई नहीं है। तो भी कर्णके रथकी ओर चल दिये। कुछ दूर जानेपर उनके मनमें
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4875)
- **Original**: तुम्हारे हितके लिये एक बात बता देना आवश्यक है; तुम बड़ी खिन्ता हुईं। ये सोचने छगे--“मैंने कर्णको मारनेकी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4875)
- **Original**: तुम्हारे हितके लिये एक बात बता देना आवश्यक है; तुम बड़ी खिन्ता हुईं। ये सोचने छगे--“मैंने कर्णको मारनेकी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4876)
- **Original**: कर्णको अपनेसे छोटा समझकर उसकी अवहेलना न प्रतिज्ञा तो की है, किन्तु यह किस तरह पूर्ण होगी ?'
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4876)
- **Original**: कर्णको अपनेसे छोटा समझकर उसकी अवहेलना न प्रतिज्ञा तो की है, किन्तु यह किस तरह पूर्ण होगी ?'
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4877)
- **Original**: करना। मैं तो महारथी कर्णको तुम्हारे समान या तुमसे भी अर्जुनको चिन्तित देख भगवान्‌ मथुसूदनने कहा--
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4877)
- **Original**: करना। मैं तो महारथी कर्णको तुम्हारे समान या तुमसे भी अर्जुनको चिन्तित देख भगवान्‌ मथुसूदनने कहा--
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4878)
- **Original**: बढ़कर समझता हूँ। इसलिये पूरा प्रयास करके तुम्हें उसका ! तुमने अपने धनुषसे जिन-जिन
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4878)
- **Original**: बढ़कर समझता हूँ। इसलिये पूरा प्रयास करके तुम्हें उसका ! तुमने अपने धनुषसे जिन-जिन
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4879)
- **Original**: वध करना चाहिये। वह अप्निके समान तेजस्वी और वायुके पायी है, उन्हें जीतनेबाला इस संसारमें
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4879)
- **Original**: वध करना चाहिये। वह अप्निके समान तेजस्वी और वायुके पायी है, उन्हें जीतनेबाला इस संसारमें
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4880)
- **Original**: समान बेगवान्‌ है, क्रोध होनेपर काछके समान हो जाता है। कोई मतुष्य नहीं है। जो. तुन्हारेजैसे
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4880)
- **Original**: समान बेगवान्‌ है, क्रोध होनेपर काछके समान हो जाता है। कोई मतुष्य नहीं है। जो. तुन्हारेजैसे
- **Translation**: 

---

