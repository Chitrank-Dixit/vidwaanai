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

### Verse 1 (Bramha 0.7681)
- **Original**: न करे। नग्न होकर कभी स्नान और शयन न परायी स्त्रीकों नंगी अवस्थामें न देखे। अपनी
- **Translation**: 

---

### Verse 2 (Bramha 0.7682)
- **Original**: करे। दोनों हाथोंसे सिर न खुजलाये। बिना कारण बिष्ठापर दृष्टिपात न करे। रजस्वला स्त्रीका दर्शन,
- **Translation**: 

---

### Verse 3 (Bramha 0.7683)
- **Original**: बार-बार सिरके ऊपरसे स्तान न करे। सिरसे स्पर्श तथा उसके साथ भाषण भी वर्जित है। पानीमें
- **Translation**: 

---

### Verse 4 (Bramha 0.7684)
- **Original**: स्नान कर लेनेपर किसी भी अड्भमें तेल न मल-मूत्रका त्याग अथवा मैथुन न करे। बुद्धिमानू
- **Translation**: 

---

### Verse 5 (Bramha 0.7685)
- **Original**: लगाये। सब अनध्यायोंके दिन स्वाध्याय बंद पुरुष मल-मूत्र, केश, राख, खोपड़ी, भूसी, कोयले,
- **Translation**: 

---

### Verse 6 (Bramha 0.7686)
- **Original**: रखे। ब्राह्मण, अग्नि, गौ तथा सूर्यकी ओर मुँह सड़ी-गलोी बस्तुएँ, रस्सी तथा केवल पृथ्वीपर और
- **Translation**: 

---

### Verse 7 (Bramha 0.7687)
- **Original**: करके पेशाब न करे। दिनमें उत्तरकी ओर और मार्गमें कभी न बैठे
- **Translation**: 

---

### Verse 8 (Bramha 0.7688)
- **Original**: गृहस्थ मनुष्य अपने वैभवके
- **Translation**: 

---

### Verse 9 (Bramha 0.7689)
- **Original**: रातमें दक्षिणही ओर मुँह करके मल-मूत्रका अनुसार देवता, पितर, मनुष्य तथा अन्यान्य
- **Translation**: 

---

### Verse 10 (Bramha 0.7690)
- **Original**: त्याग करे। जहाँ ऐसा करनेमें कोई बाधा हो, प्राणियोंका पूजन करके पीछे भोजन करे। भलीभाँति
- **Translation**: 

---

### Verse 11 (Bramha 0.7691)
- **Original**: वहाँ इच्छानुसार करे। गुरुके दुष्कर्मकी चर्चा न आचमन करके हाथ-पैर धोकर पवित्र हो पूर्व या
- **Translation**: 

---

### Verse 12 (Bramha 0.7692)
- **Original**: करे। यदि वे क्रुद्ध हों तो उन्हें विनयपूर्वक प्रसन्न उत्तरकी ओर मुँह करके भोजनके लिये आसनपर
- **Translation**: 

---

### Verse 13 (Bramha 0.7693)
- **Original**: करे। दूसरे लोग भी यदि गुरुकी निन्‍्दा करते हों बैठे और हाथोंको घुटनोंके भीतर करके मौनभावसे
- **Translation**: 

---

### Verse 14 (Bramha 0.7694)
- **Original**: तो उसे न सुने। ब्राह्मण, राजा, दुःखसे आतुर भोजन करें। भोजनके समय मनको अन्यत्र न ले
- **Translation**: 

---

### Verse 15 (Bramha 0.7695)
- **Original**: मनुष्य, विद्यावृद्ध पुरुष, गर्भिणी स्त्री, रोगसे जाय। यदि अन्न किसी प्रकारकी हानि करनेवाला : व्याकुल मनुष्य, गूँगा, अंधा, बहरा, मत्त, उन्मत्त हो तो उस हानिको ही बताये, उसके सिवा अज्नके ' व्यभिचारिणी स्त्री, उपकारी, बालक और पतित--ये और किसी दोषकी चर्चा न करें। भोजनके साथ
- **Translation**: 

---

### Verse 16 (Bramha 0.7696)
- **Original**: यदि सामनेसे आते हों तो स्वयं किनारे हटकर * पूवाँ संध्यां सनक्षत्रां पश्चिमाँ सदिवाकराम्‌। उपासीत यथान्यायं॑ नैनां जद्यादनापदि
- **Translation**: 

---

### Verse 17 (Bramha 0.7697)
- **Original**: असत्प्रलापमनृतं वाक्पारुष्प॑ च वर्जयेत्‌। असच्छास्त्रपसद्भादमसत्सेवां च वै ट्विजा:
- **Translation**: 

---

### Verse 18 (Bramha 0.7698)
- **Original**: 18-19)
- **Translation**: 

---

### Verse 19 (Bramha 0.7699)
- **Original**: 370 * संक्षिप्त ्रह्मपुराण « 0777 “:“7:7 07 बच चिचछिचिमिजज्_्न्स्‍्भमाााेऋ ऑन नल िििििननौनााा ते छ &:&%2::233 33 ऋऋऋऋऋन्-ऋ ॉ इनको जानेके लिये मार्ग देना चाहिये। विद्धान्‌
- **Translation**: 

---

### Verse 20 (Bramha 0.7700)
- **Original**: ऐसा वस्त्र न पहने। जिसमें कीड़े अथबा बाल पुरुष देवालय, चैत्यवृक्ष, चौराहा, विद्यावृद्ध पुरुष
- **Translation**: 

---

