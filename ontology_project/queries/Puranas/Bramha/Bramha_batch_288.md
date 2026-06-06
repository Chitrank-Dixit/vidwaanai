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

### Verse 1 (Bramha 0.5741)
- **Original**: (केसरका मध्यभाग) था। वह कमल ही पितामह और वर्ण आदि काल्पनिक भाव नहीं हैं। वे सदा
- **Translation**: 

---

### Verse 2 (Bramha 0.5742)
- **Original**: ब्रह्मजीका सुन्दर गृह था। उसमें चार मुखोंवाले शुद्ध, सुप्रतिष्तित और एकरूप हैं। जब-जब धर्मकी
- **Translation**: 

---

### Verse 3 (Bramha 0.5743)
- **Original**: देवाधिदेव ब्रह्माजी प्रकट हुए। उस समय भगवान्‌ हानि और अधर्मका उत्थान होता है, तब-तब वे
- **Translation**: 

---

### Verse 4 (Bramha 0.5744)
- **Original**: विष्णुके कानोंकी मैलसे दो महाबली और महापसाक्रमी अपने-आपको संसारमें प्रकट करते हैं। पूर्वकालमें
- **Translation**: 

---

### Verse 5 (Bramha 0.5745)
- **Original**: दानव उत्पन्न हुए, जो ब्रह्माजीको मार डालनेके लिये उन्हीं प्रजापालक भगवानने वाराहरूप धारण करके
- **Translation**: 

---

### Verse 6 (Bramha 0.5746)
- **Original**: उद्यत हो गये। उनका नाम मधु और कैटभ था। धूथुनसे जलको हटाया और रसातलमें डूबी हुई
- **Translation**: 

---

### Verse 7 (Bramha 0.5747)
- **Original**: भगवानने समुद्ररूपी शयनगृहसे उठकर उन दोनों पृथ्वीको अपनी एक दाढ़से कमलके फूलकी भाँति
- **Translation**: 

---

### Verse 8 (Bramha 0.5748)
- **Original**: दुर्धर्ष दैत्यॉका वध किया। ये तथा और भी ऊपर उठा लिया। उन्होंने हो नृसिंहरूप धारण
- **Translation**: 

---

### Verse 9 (Bramha 0.5749)
- **Original**: भगवान्‌की असंख्य लीलाएँ हैं, जिनकी मैं गणना करके हिरण्यकशिपुका वध किया और विप्रचित्ति
- **Translation**: 

---

### Verse 10 (Bramha 0.5750)
- **Original**: नहीं कर सकता।इस समय अजन्मा भगवान्‌के जिस आदि अन्य दानवोंको भी मार गिराया। फिर जामन
- **Translation**: 

---

### Verse 11 (Bramha 0.5751)
- **Original**: अबतारका प्रसज्भ चल रहा है, वह मधुरामें हुआ था। अबतार लेकर मायांसे बलिको बाँधा और दैत्योंको
- **Translation**: 

---

### Verse 12 (Bramha 0.5752)
- **Original**: इस प्रकार भगवान्‌को जो सात्त्विक मूर्ति है, वही जीतकर तीनों लोकोंको अपने तीन पगोंसे ही नाप
- **Translation**: 

---

### Verse 13 (Bramha 0.5753)
- **Original**: अबतार धारण करती है। वह प्रद्युम्न नामसे विख्यात लिया। वे ही भृगु-वंशमें परमप्रतापी जमदग्रिकुमार
- **Translation**: 

---

### Verse 14 (Bramha 0.5754)
- **Original**: है और सदा रक्षाकार्यमें संलग्र रहती है। वह भगवान्‌ परशुरामके रूपमें उत्पन्न हुए, जिन्होंने पिताके
- **Translation**: 

---

### Verse 15 (Bramha 0.5755)
- **Original**: वासुदेवकी इच्छाके अनुसार देवता, मनुष्य और बधका बदला लेनेके लिये क्षत्रियोंका संहार कर
- **Translation**: 

---

### Verse 16 (Bramha 0.5756)
- **Original**: तिर्यक्‌ योनिमें अवतीर्ण होती है और उसीके डाला। उन्हीं भगवानने अत्रिकुमार प्रतापी दत्ताश्रेयक
- **Translation**: 

---

### Verse 17 (Bramha 0.5757)
- **Original**: अनुकूल स्वभाव बना लेती है। भक्त पुरुषोंद्वारा रूपमें अवतीर्ण हो महात्मा अलर्कको अष्टाड्रयोगका
- **Translation**: 

---

### Verse 18 (Bramha 0.5758)
- **Original**: पूजित होनेपर वह उनकी मनोवाञिछत कामनाओंको उपदेश दिया। ज़ेतामें दशरथनन्दन श्रीरामके रूपमें
- **Translation**: 

---

### Verse 19 (Bramha 0.5759)
- **Original**: भी पूर्ण करती है। इस तरह मैंने यहाँ भगवानके प्रकट होकर उन्होंने ही त्रिभुवनकों भय देनेवाले
- **Translation**: 

---

### Verse 20 (Bramha 0.5760)
- **Original**: अवतारका रहस्य बतलाया है। भगवान्‌ विष्णु यद्यपि रावणका युद्धमें संहार किया। कृतकृत्य हैं, उन्हें कुछ करना अथवा पाना नहीं प्रलयकालमें जब सारी सृष्टि एकार्णवर्में निमग्र
- **Translation**: 

---

