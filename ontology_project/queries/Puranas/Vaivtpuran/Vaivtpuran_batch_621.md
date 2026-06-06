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

### Verse 1 (Vaivtpuran 55.19236)
- **Original**: त॑ पठित्वा गुरुमुखाद भवन्‍्त्येव बुधा जना: । गुणानां वा स्तवानां ते शतांशं वक्तुमक्षम:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.5333)
- **Original**: जो राधामन्त्रका उपासक होकर प्रतिदिन इस
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.5334)
- **Original**: श्रीनारायण कहते हैं--नारद! इस प्रकार कवचका भक्तिभावसे पाठ करता है, वह विष्णुतुल्य
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.5335)
- **Original**: राधिकाकी कथा कहकर बारंबार माधवका स्मरण तेजस्वी होता तथा राजसूय-यज्ञका फल पाता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.5336)
- **Original**: करके भगवान्‌ शंकरके सम्पूर्ण अज्ोंमें रोमात्न हो है। सम्पूर्ण तीथोंमें स्नान, सब प्रकारका दान,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.5337)
- **Original**: आया। उनके नेत्रोंसे आँ%सुओंकी धारा बहने लगी। सम्पूर्ण ब्रतोंमें उपवास, पृथ्वीकी परिक्रमा, समस्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.5338)
- **Original**: श्रोकृष्णे समान कोई देवता नहीं है, गड्भा-जैसी यज्ञॉंकी दीक्षाका ग्रहण, सदैव सत्यकी रक्षा, दूसरी नदी नहीं है, पुष्ककके समान कोई तीर्थ नित्यप्रति श्रीकृष्णकी सेवा, श्रीकृष्ण-नैवेद्यका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.5339)
- **Original**: नहीं है तथा ब्राह्मणसे बढ़कर कोई वर्ण नहीं है। भरक्षण तथा चारों वेदोँका पाठ करनेपर मनुष्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.5340)
- **Original**: नारद! जैसे परमाणुसे बढ़कर सूक्ष्म, महाविष्णु जिस फलको पाता है, उसे निश्वय ही वह इस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.5341)
- **Original**: (महाविराट)-से बढ़कर महान्‌ तथा आकाशसे कवचके पाठसे पा लेता है। राजद्वारपर, श्मशानभूमिमें,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.5342)
- **Original**: अधिक विस्तृत दूसरी कोई वस्तु नहीं है, उसी सिंहों और व्याप्रोंसे भरे हुए वनमें, दावानलमें,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.5343)
- **Original**: प्रकार वैष्णवसे बढ़कर ज्ञानी तथा भगवान्‌ शंकरसे विशेष संकटके अवसरपर, डाकुओं और चोरोंसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.5344)
- **Original**: बढ़कर कोई योगीन्द्र नहीं है। देवर्षे ! उन्होंने ही भय प्राप्त होनेपर, जेल जानेपर, विपत्तिमें पड़
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.5345)
- **Original**: काम, क्रोध, लोभ और मोहपर विजय पायी है। जानेपर, भयंकर एवं अटूट बन्धनमें बँधनेपर तथा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.5346)
- **Original**: भगवान्‌ शिव सोते, जागते हर समय श्रीकृष्णके रोगोंसे आक्रान्त होनेपर यदि मनुष्य इस कवचको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.5347)
- **Original**: ध्यानमें तत्पर रहते हैं। जैसे कृष्ण हैं, वैसे शिव धारण कर ले तो निश्चय ही वह समस्त दुःखोंसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.5348)
- **Original**: हैं। श्रीकृष्ण और शिवमें कोई भेद नहीं है।* छूट जाता है। दुर्गे! महेश्वरि! यह तुम्हारा ही
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.5349)
- **Original**: वत्स! जैसे वैष्णवोंमें शम्भु तथा देवताओंमें माधव कवच तुमसे कहा है। तुम्हों सर्वरूपा माया हो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.5350)
- **Original**: श्रेष्ठ हैं, उसी प्रकार कबचोंमें यह जगन्मड्जल और छलसे इस विषयमें मुझसे पूछ रही हो।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.5351)
- **Original**: राधाकबच सर्वोत्तम है। 'शि” यह मड्गलवाचक है 3 रां हीं श्री राधिकेति डे5न्तं वह्िजायान्तमेव च । मस्तक केशसंघांश . मन्त्रराआ: सदावतु
- **Translation**: 

---

