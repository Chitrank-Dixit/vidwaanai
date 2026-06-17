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

### Verse 1 (Vaivtpuran 543.12434)
- **Original**: चद्वरीक आपके चरणकमलोंमें सदा रमता रहे। सम्पूर्ण अड्न चन्दनसे चर्चित थे। नेत्र शरद्‌ ऋतुके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12435)
- **Original**: जैसे मधुप कमलमें स्थित हो उसके मकरन्दका प्रफुल्ल कमलॉकों लज्जित कर रहे थे। मुख शरद्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12436)
- **Original**: पान करता है; उसी प्रकार मेरा मनरूपी भ्रमर ऋतुकी पूर्णिमाके चन्द्रमाकी भाँति मनोहर था,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12437)
- **Original**: भी आपके चरणारविन्दोंमें स्थित हो भक्तिरसका मस्तकपर श्रेष्ठ रत्रमय मुकुट अपनी उज्वल आभा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12438)
- **Original**: निरन्तर आस्वादन करता रहे। आप जन्म-जन्ममें बिखेर रहा था। दाँत पके हुए अनारके दाने-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12439)
- **Original**: मेरे प्राणनाथ हों और अपने चरणकमलोंकी परम जैसे स्वच्छ दिखायी देते थे। आकृति बड़ी [दुर्लभ भक्ति मुझे दें। मेरा चित्त सोते-जागते, मनोहर थी। उन्होंने विनोदके लिये एक हाथमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12440)
- **Original**: दिन-रात आपके स्वरूप तथा गुणोंके चिन्तनमें मुरली और दूसरे हाथमें लीलाकमल ले रखा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12441)
- **Original**: सतत निमग्र रहे। यही मेरी मनोवाञ्छा है। था। वे करोड़ों कन्द्पॉँकी लावण्य-लीलाके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12442)
- **Original**: गोपियाँ बोलीं--प्राणबन्धो! आप जन्म- मनोहर धाम थे। उन गुणातीत परमेश्वरकी ब्रह्मा,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12443)
- **Original**: जन्ममें हमारे प्राणनाथ हों और श्रीराधाकी ही शेषनाग और शिव आदि निरन्तर स्तुति करते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12444)
- **Original**: भाँति हम सबको भी सदा अपने साथ रखें। हैं। वे ब्रह्मस्वरूप तथा ब्राह्मणहितैषी हैं। श्रुतियोंने।. गोपियोंका यह बचन सुनकर प्रसन्नमुखवाले उनके ब्रह्मरूपका निरूपण किया है। वे अव्यक्त श्रीमान्‌ यशोदानन्दनने कहा--“तथास्तु' (ऐसा और व्यक्त हैं। अविनाशी एवं सनातन ज्योति:-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12445)
- **Original**: ही हो)। तत्पश्चात्‌ उन जगदीश्वरने श्रीराधिकाको स्वरूप हैं। मड्गलकारी, मज्जलके आधार, मम्जलमय
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12446)
- **Original**: प्रेमपूर्वक्क सहलदलोंसे युक्त क्रीडाकमल तथा तथा मड्गलदाता हैं। मालतीकी मनोहर माला दी। साथ ही अन्य श्यामसुन्दरके उस अद्भुत रूपकों देखकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12447)
- **Original**: गोपियोंकों भी उन गोपीव्भने हँसकर प्रसादस्वरूप राधाने बेगपूर्वक आगे बढ़कर उन्हें प्रणाम किया पुष्प तथा मालाएँ भेंट कौं। तदनन्तर वे बड़े उन्हें अच्छी तरह देखकर प्रेमके वशीभूत हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12448)
- **Original**: प्रेमसे बोले। वे सुध-बुध खो बैठीं। प्रियतमके मुखारविन्दकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12449)
- **Original**: . श्रीकृष्णने कहा--ब्रजदेवियो! तीन मास बाँकी चितवनसे देखते-देखते उनके अधरोपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12450)
- **Original**: व्यतीत होनेपर वृन्दावनके सुरम्य रासमण्डलमें मुस्कराहट दौड़ गयी और उन्होंने लज्जावश
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12451)
- **Original**: तुम सब लोग मेरे साथ रासक्रीड़ा करोगी। जैसा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12452)
- **Original**: 546 + संक्षिप्त ग्रह्मवैवर्तपुराण * £#444444 444 44444 4 44446 44444 484 444 44444 444 4444 44484 8 # 84% 5444 84 ## 44 4 5 4 ऊ 8 5 % मैं हूँ, वैसी ही तुम हो। हममें तुममें भेद नहीं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12453)
- **Original**: बैठ गये। फिर सारी गोपियाँ भी बारंबार उन्हें है। मैं तुम्हारे प्राण हूँ और तुम भी मेरे लिये
- **Translation**: 

---

