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

### Verse 1 (Bramha 0.801)
- **Original**: ऊँचाई चौरासी हजार योजन है। वह पृथ्वीके हैं। जितने समुद्र, द्वीप, वर्ष, पर्वत, बन, नदियाँ
- **Translation**: 

---

### Verse 2 (Bramha 0.802)
- **Original**: भीतर सोलह हजार योजनतक चला गया है तथा तथा पवित्र देवताओंके स्थान हैं, समस्त भूतलका
- **Translation**: 

---

### Verse 3 (Bramha 0.803)
- **Original**: उसके शिखरकी चौड़ाई बत्तीस हजार योजन है। मान जितना बड़ा है, जिसके आधारपर यह टिका
- **Translation**: 

---

### Verse 4 (Bramha 0.804)
- **Original**: उसके मूलका विस्तार सोलह हजार योजन है। हुआ है तथा जो इसका उपादान कारण है, वह
- **Translation**: 

---

### Verse 5 (Bramha 0.805)
- **Original**: वह पर्बत पृथ्वीरूपी कमलकी कर्णिकाके रूपमें सब यथार्थरूपसे बतलाइये। स्थित है। उसके दक्षिणमें हिमवान्‌, हेमकूट और लोमहर्षणजी ओोले--मुनिवरों! सुनो, मैं इस
- **Translation**: 

---

### Verse 6 (Bramha 0.806)
- **Original**: निषध पर्वत हैं तथा उत्तरमें नील, श्वेत और भूमण्डलका वृत्तान्त संक्षेपमें सुनाता हूँ। जम्बू,
- **Translation**: 

---

### Verse 7 (Bramha 0.807)
- **Original**: श्रृद्धवान्‌ गिरि हैं। मध्यके दो पर्वत (निषध और प्लक्ष, शाल्मल, कुश, क्रौक्ध, शाक तथा पुष्कर-ये
- **Translation**: 

---

### Verse 8 (Bramha 0.808)
- **Original**: नील) एक-एक लाख योजन लंबे हैं। शेष पर्व॑त सात ट्वीप हैं, जो क्रमश:--लवण, इक्षुरस, सुरा, । क्रमश: दस-दस हजार योजन छोटे होते गये हैं। घृत, दधि, दुग्ध तथा जलरूप सात समुद्रोंसे घिरे , उन सबकी ऊँचाई और चौड़ाई दो-दो हजार
- **Translation**: 

---

### Verse 9 (Bramha 0.809)
- **Original**: 0 * संक्षिप्त ब्रह्मपुराण * ।$ केसराचलके रूपमें स्थित है। बन आक अं बज आग
- **Translation**: 

---

### Verse 10 (Bramha 0.810)
- **Original**: आदि 4-3 केसर-पर्वत हैं। शिखिवास, है। इसी प्रकार उत्तर दक्षिणभागके चाह रम्यकवर्ष, उससे दक्षिण हिरण्मयवर्ष तथा उससे
- **Translation**: 

---

### Verse 11 (Bramha 0.811)
- **Original**: पे का, शन्यपारण हि 4 48-84 574“ 240 8
- **Translation**: 

---

### Verse 12 (Bramha 0.812)
- **Original**: हंस, नाग तथा कालझर आदि अन्य पर्वत 373. 0%%0#+ 4 2 नौ
- **Translation**: 

---

### Verse 13 (Bramha 0.813)
- **Original**: उत्तरभागके केसराचल हैं। मेरुगिरिके ऊपर ब्यारथीन वास ता है आप
- **Translation**: 

---

### Verse 14 (Bramha 0.814)
- **Original**: चौदह हजार योजनके विस्तारवाली एक विशाल पाक यह को पर सी आह व
- **Translation**: 

---

### Verse 15 (Bramha 0.815)
- **Original**: पुरी है, जो ब्रह्माजीकी सभा कहलाती है। उसमें तथा उत्तर आओ 3 अं 'चों सब ओर आठों दिशाओं और विदिशाओमें इन्द्र जा ऋी कि का और
- **Translation**: 

---

### Verse 16 (Bramha 0.816)
- **Original**: आदि लोकपालोंके विख्यात नगर हैं। पट ये जब पद के थे व्यय, सौ
- **Translation**: 

---

### Verse 17 (Bramha 0.817)
- **Original**: भगवान्‌ विष्णुके चरणोंसे निकलकर चनद्रमण्डलको पपा िकनह है। के का 5
- **Translation**: 

---

### Verse 18 (Bramha 0.818)
- **Original**: आप्लाबित करलेवाली गज्ा ब्रह्मपुरीके चारों ओर हा 00 आज 0 है ये चूक ही पिरती हैं। वहाँ गिरकर वे चार भागोंमें बट जाती जे नेक का छ । हैं। उस समय उनके क्रमश:--सीता, अलकनन्दा, का लक जनक पद है। और भद्ठा नाम होते हैं। पूर्व ओर सीता एक उसके फल विशाल गजराजके बराबर होते हैं।
- **Translation**: 

---

### Verse 19 (Bramha 0.819)
- **Original**: चर पबापर जल हु नी भाव वे गन्धमादनपर्वतपर सब ओर गिरकर फूट जाते
- **Translation**: 

---

### Verse 20 (Bramha 0.820)
- **Original**: - न. सु सु्थाथ ही आय कान चल बीत दो
- **Translation**: 

---

