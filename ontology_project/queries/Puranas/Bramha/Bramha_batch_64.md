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

### Verse 1 (Bramha 0.1261)
- **Original**: सबके आदिभूत उस परमात्माका पूजन करते हैं और बहुविध; वह परमात्मा सर्यन्र बतलाया जाता है,
- **Translation**: 

---

### Verse 2 (Bramha 0.1262)
- **Original**: बे उन्हें सद्गति प्रदान करते हैं। वे सर्वात्मा, सर्वगत इसलिये बहुविधरूप होनेके कारण वह विश्वरूप । और निर्णुण कहलाते हैं। मैं भगवान्‌ सूर्यको ऐसा माना गया है। एकमात्र वही महान्‌ है और एकमात्र
- **Translation**: 

---

### Verse 3 (Bramha 0.1263)
- **Original**: मानकर अपने ज्ञानके अनुसार उनका पूजन करता हूँ। वही पुरुष कहलाता है; अत: वह एकमात्र सनातन
- **Translation**: 

---

### Verse 4 (Bramha 0.1264)
- **Original**: नारदजी ! यह गोपनीय उपदेश मैंने अपनी भक्तिके परमात्मा ही महापुरुष नाम धारण करता है। वह
- **Translation**: 

---

### Verse 5 (Bramha 0.1265)
- **Original**: कारण आपको बतलाया है। आपने भी इस उत्तम परमात्मा स्वयं ही अपने-आपको सौ, हजार, लाख
- **Translation**: 

---

### Verse 6 (Bramha 0.1266)
- **Original**: रहस्यको भलीभौति समझ लिया। देवता, मुनि और और करोड़ों रूपोंमें प्रकर कर लेता है। जैसे आकाशसे
- **Translation**: 

---

### Verse 7 (Bramha 0.1267)
- **Original**: पुराण--सभी उस परमात्माको वरदायक मानते हैं गिरा हुआ जल भूमिके रसविशेषसे दूसरे स्वादका हो
- **Translation**: 

---

### Verse 8 (Bramha 0.1268)
- **Original**: और इसी भावसे सब लोग भगवान्‌ दिवाकरका जाता है, उसी प्रकार गुणमय रसके सम्पर्कसे बह
- **Translation**: 

---

### Verse 9 (Bramha 0.1269)
- **Original**: पूजन करते हैं। परात्मा अनेक रूप प्रवीत होने लगता है। जैसे एक
- **Translation**: 

---

### Verse 10 (Bramha 0.1270)
- **Original**: ख्रह्माजी कहते हैं--इस प्रकार मित्र देवताने ही वायु समस्त शरीरोंमें पाँच रूपोंमें स्थित है, उसी
- **Translation**: 

---

### Verse 11 (Bramha 0.1271)
- **Original**: पूर्वकालमें नारदजीको यह उपदेश दिया था। भानुके प्रकार आत्माकी भी एकता और अनेकता मानी गयी
- **Translation**: 

---

### Verse 12 (Bramha 0.1272)
- **Original**: उपदेशकों मैंने भी आप लोगोंसे कह सुनाया। जो है। जैसे अप्नि दूसरे स्थानकी विशेषतासे अन्य नाम
- **Translation**: 

---

### Verse 13 (Bramha 0.1273)
- **Original**: सूर्यका भक्त न हो, उसे इसका उपदेश नहीं देना धारण करती है, उसी प्रकार वह परमात्मा ब्रह्म
- **Translation**: 

---

### Verse 14 (Bramha 0.1274)
- **Original**: चाहिये। जो मनुष्य प्रतिदिन इस प्रसंगको सुनाता आंदिके रूपोमें भिन्न-भिन्न नाम धारण करता है। जैसे
- **Translation**: 

---

### Verse 15 (Bramha 0.1275)
- **Original**: और जो सुनता है, वह निःसंदेह भगवान्‌ सूर्यमें प्रवेश एक दौप हजाएं दीपोको प्रकट करता है, बैसे ही वह
- **Translation**: 

---

### Verse 16 (Bramha 0.1276)
- **Original**: करता है। आरम्भसे ही इस कथाकों सुनकर रोगी एक ही परमात्मा हजारों रूपोंको उत्पन्न करता है।
- **Translation**: 

---

### Verse 17 (Bramha 0.1277)
- **Original**: मनुष्य रोगसे मुक्त हो जाता है और जिज्ञासुको उत्तम संसारमें जो चराचर भूत हैं, बे नित्य नहीं हैं; परंतु बह
- **Translation**: 

---

### Verse 18 (Bramha 0.1278)
- **Original**: ज्ञान एवं अभीष्ट गतिकी प्राप्ति होती है। मुनियो! जो परमात्पा अक्षय, अप्रमेय तथा सर्वव्यापी कहा जाता , इसका पाठ करता है, वह जिस-जिस वस्तुकी है। बह ब्रह्म सदसत्स्वरूप है। लोकमें देवकार्य तथा
- **Translation**: 

---

### Verse 19 (Bramha 0.1279)
- **Original**: कामना करता है, उसे निश्चय ही प्राप्त कर लेता है। “स्पेस 98-280 * श्रसत्रपि शररेषु न स लिप्येत कर्मभि: । ममात्तरात्मा तब च ये चान्ये देहसंस्थिता:
- **Translation**: 

---

### Verse 20 (Bramha 0.1280)
- **Original**: सर्वेषां साक्षिभूतोउसी न ग्राह्म: केनचित्‌ क्वचित्‌। सगुणो निगुंणों विश्वो ज्ञानगप्यों हासी स्मृतः
- **Translation**: 

---

