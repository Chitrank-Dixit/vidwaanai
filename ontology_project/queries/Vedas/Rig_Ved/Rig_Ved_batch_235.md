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

### Verse 1 (Rig Ved 0.4681)
- **Original**: ] 2072 श्रेष्ठ यविष्ठ भारताग्ने द्युमन्‍्तमा भर। बसो पुरुस्पृहं रयिम्‌
- **Translation**: 

---

### Verse 2 (Rig Ved 0.4682)
- **Original**: है अतीव बलशाली अग्निदेव ! आप सभी के पालक तथा सुख प्रदान करने वाले आश्रयदाता हैं, अत: महान्‌ तेजस्वी तथा बहुतों द्वारा चाहा गया ऐश्वर्य हमें भरपूर मात्रा में प्रदान करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.4683)
- **Original**: 2073. मा नो अरातिरीशत देवस्य मर्त्यस्य च। पर्षि तस्या उत द्विष:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.4684)
- **Original**: है अग्निदेव ! देवताओं तथा मनुष्यों के दुश्मन हमारे ऊपर स्वापित्व स्थापित न करें । अपितु आप उन शत्रुओं से हमें बचायें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.4685)
- **Original**: 2074. विश्वा उत त्वया वय॑ धारा उदन्याइव। अति गाहेमहि द्विष:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.4686)
- **Original**: है अग्निदेव ! जिस तरह जल की धारायें बड़ी चट्टानों को पार कर जाती हैं, उसी तरह आपका संरक्षण पाकर द्वेष करने वाले सम्पूर्ण शत्रुओं को हम पार कर जायें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.4687)
- **Original**: 2075. शुचि: पावक बन्द्यो5ग्ने बृहद्धि रोचसे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.4688)
- **Original**: त्यं घृतेभिराहुतः
- **Translation**: 

---

### Verse 9 (Rig Ved 0.4689)
- **Original**: हे पवित्रता प्रदान करने वाले अग्निदेव ! आप पवित्र तथा वन्दना के योग्य हैं। आप घृत की आहुतियों से अत्यन्त प्रकाशित होते हैं
- **Translation**: 

---

### Verse 10 (Rig Ved 0.4690)
- **Original**: पं0 2 सू0 9 श्1 2076. त्वं नो असि भारताग्ने वशाभिरुक्षप्रि:। अष्टापदीभिराहुत:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.4691)
- **Original**: हे मनुष्यों के हितकारी अग्निदेव ! आप हमारी सुन्दर गौओं, बैलों तथा गर्भिणी गौओं द्वारा पूजित हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.4692)
- **Original**: 2077 द्रवन्नः सर्पिरासुति: प्रत्नो होता वरेण्य:। सहसस्पुत्रो अद्धुत:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.4693)
- **Original**: इन आननिदेव का भोजन समिधा रूपी अन्न है, जिनमें घृत का सिंचन किया जाता है, जो सनातन तथा होता रूप में वरण के योग्य है । बल से उत्पन्न ऐसे अग्निदेव अद्भुत गुणों के कारण रमणीय हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.4694)
- **Original**: [ सूक्त - 8 ] [ऋषि- गृत्समद (आइ्रिरस शौनहोत्र पक्षाद्‌ ) भार्गव शौनक । देवता- अग्नि । छन्द - गायत्री 6 अनुष्टप्‌
- **Translation**: 

---

### Verse 15 (Rig Ved 0.4695)
- **Original**: ] 2078. वाजयजन्निव नू रथान्योगाँ अग्नेरुप स्तुहि। यशस्तमस्य मीछहुष:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.4696)
- **Original**: हे मनुष्य ! जिस प्रकार धन -धान्य की कामनावाले रथों को उत्तम रीति से तैयार करते हैं, उसी प्रकार अत्यन्त यशस्वी, सबके लिए सुखकारी अग्निदेव की स्तृतियों के द्वारा उतका पूजन करो
- **Translation**: 

---

### Verse 17 (Rig Ved 0.4697)
- **Original**: 2079. यः सुनीथो ददाशुषे5जुर्यो जरयन्नरिम्‌। चारुप्रतीक आहुत:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.4698)
- **Original**: जो अम्निदेव श्रेष्ठ नेतृत्व प्रदान कर उत्तम पथ पर ले जाते हैं, जो अविनाशी तथा श्रेष्ठ उपक्रम वाले हैं, ऐसे शत्रुनाशक, दानशील अग्निदेव का हम आबाहन करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.4699)
- **Original**: 2080, य उ श्रिया दमेष्वा दोषोषसि प्रशस्यते । यस्य ब्रत॑ न मीयते
- **Translation**: 

---

### Verse 20 (Rig Ved 0.4700)
- **Original**: जो अग्निदेव घरों में अपनी कान्ति से युक्त होकर प्रतिष्ठित होते हैं, जो अग्निदिव दिन और रात प्रशंसा के योग्य हैं तथा जिनका व्रत कभी खण्डित नहीं होता; वे अग्निदेव पूज्य तथा प्रशंसनीय हैं
- **Translation**: 

---

