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

### Verse 1 (Bramha 0.2281)
- **Original**: भगवान्‌ विष्णु वहाँसे अन्तर्धान हो गये। राजाके तुम्हें साक्षात्कार कराऊँगा। उस परमानन्दमय पदको
- **Translation**: 

---

### Verse 2 (Bramha 0.2282)
- **Original**: हर्षकी सोमा न रहो। उनका शरीर रोमाझित हो पाकर तुम परम पद-मोक्षको प्राप्त हो जाओगे!
- **Translation**: 

---

### Verse 3 (Bramha 0.2283)
- **Original**: गया। उन्होंने भगवान्‌के दर्शनसे अपनेको कृतकृत्य राजेन्द्र! इस पृथ्वीपर जबतक बादल पानी बरसाते
- **Translation**: 

---

### Verse 4 (Bramha 0.2284)
- **Original**: माना। तत्पक्षात्‌ श्रीकृष्ण, बलराम और वरदायिनी रहेंगे, जबतक आकाश, चन्द्रमा, सूर्य और तारे
- **Translation**: 

---

### Verse 5 (Bramha 0.2285)
- **Original**: सुभद्राकों मणिकाश्चननजटित विमानाकार रघथोंमें दीखते रहेंगे, जबतक सात समुद्र वथा पेरु आदि
- **Translation**: 

---

### Verse 6 (Bramha 0.2286)
- **Original**: बिठाकर वे बुद्धिमान्‌ नरेश अमात्य और मन्त्रियोंसहित पर्वत मौजूद रहेंगे तथा जबतक द्युलोकमें देवताओंकी
- **Translation**: 

---

### Verse 7 (Bramha 0.2287)
- **Original**: मड़्लपाठ तथा बाजे-गाजेके साथ ले आये और सत्ता बनी रहेगी, तबतक इस भूतलपर सर्वत्र
- **Translation**: 

---

### Verse 8 (Bramha 0.2288)
- **Original**: उन्हें परम मनोहर पवित्र स्थानमें पधराया। फिर तुम्हारी अक्षय कीर्ति छायो रहेगी । तुम्हारे यज्ञाड़से (शुभ तिथि, शुभ समय, शुभ नक्षत्र और शुभ प्रकट होनेवाला तालाब इन्द्रधुम्नसरोवरके नामसे
- **Translation**: 

---

### Verse 9 (Bramha 0.2289)
- **Original**: मुहूर्तमें ब्राह्मणोंके द्वारा उनकी प्रतिष्ठा करायी। प्रसिद्ध तीर्थ होगा, जिसमें एक बार स्नान करके
- **Translation**: 

---

### Verse 10 (Bramha 0.2290)
- **Original**: उत्तम प्रास्रादमें वेदोक्त विधिपूर्वक प्रतिष्ठा करके भी मनुष्य इन्द्रलोक प्राप्त कर सकते हैं। जो इस
- **Translation**: 

---

### Verse 11 (Bramha 0.2291)
- **Original**: उन सब विग्रहोंको स्थापित किया; फिर भाँति- सरोवरके सुन्दर तटपर पिण्डदान करेगा, वह अपनी
- **Translation**: 

---

### Verse 12 (Bramha 0.2292)
- **Original**: झि:जा: कहना का इक्कीस पीढ़ियोंका उद्धार करके इन्द्रलोकको जायगा
- **Translation**: 

---

### Verse 13 (Bramha 0.2293)
- **Original**: ... और वहाँ ब्रिमानपर बैठकर अप्सराओंसे पूजित हो
- **Translation**: 

---

### Verse 14 (Bramha 0.2294)
- **Original**: 977“ गन्धर्वोंके गीत सुनता हुआ चौदह इद्रोंकी आयुपर्यन्त
- **Translation**: 

---

### Verse 15 (Bramha 0.2295)
- **Original**: निवास करेगा। सरोवरके दक्षिण भागमें नैर्ऊृत्य
- **Translation**: 

---

### Verse 16 (Bramha 0.2296)
- **Original**: ! कोणकी ओर जो बरगदका वृक्ष खड़ा है, उसके समीप केवड़ेके वनसे आच्छादित एक मण्डप है, जो नाना प्रकारके वृक्षोंसे व्याप्त है। आषाढ़के शुक्ल पक्षकी पश्षमीको महानक्षत्रमें हमारी इन प्रतिमाओंको ले आकर लोग सात दिनॉतक मण्डपमें स्थापित रखेंगे। उस समय बड़ा उत्सव होगा। सोनेके दण्ड लगे हुए चँवर तथा रत्नभूषित व्यजनोंद्वारा
- **Translation**: 

---

### Verse 17 (Bramha 0.2297)
- **Original**: सब लोग हमें हथा करेंगे। इस प्रकार मड्भलपाठपूर्वक ' हमारी स्थापना होगी। ब्रह्मचारी, संन्यासी, स्नातक, '
- **Translation**: 

---

### Verse 18 (Bramha 0.2298)
- **Original**: + मार्कण्डेय मुनिको प्रलयकालमें बालमुकुन्दका दर्शन और यरदान प्राप्त होता * भाँतिके सुगन्धित पुष्पोंसे विधिवत्‌ पूजा करके
- **Translation**: 

---

### Verse 19 (Bramha 0.2299)
- **Original**: होता है। अतः मुनिबरो! स्वगलोककी इच्छा इच्छा सुबर्ण, मणि, मोती और नाना प्रकारके सुन्दर वस्त्र
- **Translation**: 

---

### Verse 20 (Bramha 0.2300)
- **Original**: रखनेवाले ब्राह्मण आदिको चाहिये कि वे ज्येष्ठ अर्पण किये। विविध प्रकारके दिव्य रत्र, आसन,
- **Translation**: 

---

