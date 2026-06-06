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

### Verse 1 (Agni Puran 0.661)
- **Original**: (अग्विषु0 38। 36-41)
- **Translation**: 

---

### Verse 2 (Agni Puran 0.662)
- **Original**: मुक्त हो जाता है। प्रतिदिन यज्ञोंद्वारा भगवान्‌की
- **Translation**: 

---

### Verse 3 (Agni Puran 0.663)
- **Original**: हजार वर्षोत्क उस मन्दिर्के बनवानेवालेकी आराधना करनेवालेको जो महान्‌ फल मिलता है,
- **Translation**: 

---

### Verse 4 (Agni Puran 0.664)
- **Original**: स्वर्गलोकमें स्थिति होती है। भगवान्‌की प्रतिमा उसी फलको, जो विष्णुका मन्दिर बनवाता है,
- **Translation**: 

---

### Verse 5 (Agni Puran 0.665)
- **Original**: बनानेवाला विष्णुलोकको प्राप्त होता है, उसकी वह भी प्राप्त करता है। जो भगवान्‌ अच्युतका
- **Translation**: 

---

### Verse 6 (Agni Puran 0.666)
- **Original**: स्थापना करनेवाला भगवानमें लीन हो जाता है मन्दिर बनवाता है, वह अपनी बीती हुई सौ
- **Translation**: 

---

### Verse 7 (Agni Puran 0.667)
- **Original**: और देवालय बनवाकर उसमें प्रतिमाकी स्थापना पीढ़ीके पितरोंकों तथा होनेवाले सौ पीढ़ीके
- **Translation**: 

---

### Verse 8 (Agni Puran 0.668)
- **Original**: करनेवाला सदा भगवान्‌के लोकमें निवास पाता वंशजोंको भगवान्‌ विष्णुके लोकको पहुँचा देता
- **Translation**: 

---

### Verse 9 (Agni Puran 0.669)
- **Original**: 42--50
- **Translation**: 

---

### Verse 10 (Agni Puran 0.670)
- **Original**: है। भगवान्‌ विष्णु सप्ततोकमय हैं। उनका मन्दिर। अग्निदेव बोले-- यमराजके इस प्रकार आज्ञा जो बनवाता है, वह अपने कुलको तारता है, उन्हें
- **Translation**: 

---

### Verse 11 (Agni Puran 0.671)
- **Original**: देनेपर यमके दूत भगवान्‌ विष्णुकी स्थापना आदि अक्षय लोकोंकी प्राप्ति कराता है और स्वयं भी
- **Translation**: 

---

### Verse 12 (Agni Puran 0.672)
- **Original**: करनेवालॉकों यमलोकमें नहीं ले जाते। देवताओंकी अक्षय लोकोंको प्राप्त होता है। मन्दिरमें ईंटके
- **Translation**: 

---

### Verse 13 (Agni Puran 0.673)
- **Original**: प्रतिष्ठा आदिकी विधिका भगवान्‌ हयग्रीवने समूहका जोड़ जितने वर्षोतक रहता है, उतने ही
- **Translation**: 

---

### Verse 14 (Agni Puran 0.674)
- **Original**: ब्रह्माजीसे वर्णन किया था
- **Translation**: 

---

### Verse 15 (Agni Puran 0.675)
- **Original**: इस प्रकार आदि आग्रेय महापुराणमें 'देवालय-तिर्माण माहात्प्यादिका वर्णन अड़तीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 16 (Agni Puran 0.676)
- **Original**: उन्तालीसवाँ अध्याय विष्णु आदि देवताओंकी स्थापनाके लिये भूपरिग्रहका विधान भगवान्‌ हयग्रीव कहते हैं--- ब्रह्मन्‌! अब मैं
- **Translation**: 

---

### Verse 17 (Agni Puran 0.677)
- **Original**: वसिष्ठोक्त ज्ञानसागरतन्त्र, स्वायम्भुवतन्त्र, कापिलतन्त्र, विष्णु आदि देवताओंकी प्रतिष्ठाके विषयमें कहूँगा,
- **Translation**: 

---

### Verse 18 (Agni Puran 0.678)
- **Original**: ताक्ष्य (गारुड )-तन्त्र, नारायणीयतन्त्र, आत्रेयतन्त्र, ध्यान देकर सुनिये। इस विषयमें मेरे द्वारा वर्णित
- **Translation**: 

---

### Verse 19 (Agni Puran 0.679)
- **Original**: नारसिंहतन्त्र, आनन्दतन्त्र, आरुणतन्त्र, बौधायनतन्त्र, पद्चरात्रों एवं सप्तरात्रॉंका ऋषियोंने मानवलोकमें
- **Translation**: 

---

### Verse 20 (Agni Puran 0.680)
- **Original**: अष्टाज्भतन्त्र और विश्वतन्त्र। 1--5
- **Translation**: 

---

