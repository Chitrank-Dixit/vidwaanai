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

### Verse 1 (Vaivtpuran 13.2969)
- **Original**: आसनपर विराज गये। विष्णु-पार्षदोंने श्वेत चँवर और भक्तिपूर्बक मेरे गुण गाते रहना इनका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.2970)
- **Original**: डुलाकर उनकी सेवा कौ। जब उनके मार्गका स्वभाव-सा बन गया है। मैं भी रात-दिन इनके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.2971)
- **Original**: श्रम दूर हो गया, तब भगवान्‌ श्रीहरिने अमृतके कल्याणकी चिन्तामें ही लगा रहता हूँ; क्योंकि
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.2972)
- **Original**: समान अत्यन्त मनोहर एवं मधुर वचन कहा। जो जिस प्रकार मेरी उपासना करते हैं, मैं भी । क्र ++ उसी प्रकार उनकी सेवामें तत्पर रहता हूँ*--यह मेरा नियम है।' । इतनेमें भगवान्‌ शंकर भी वहाँ पहुँच गये।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.2973)
- **Original**: रिया उनके हाथमें त्रिशूल था। वे वृषभपर आखरूद
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.2974)
- **Original**: कै थे और आँखें रक्तकमलके समान लाल थीं। वहाँ पहुँचते ही वे वृषभसे उतर पड़े और भक्तिविनम्र स्ि- लन्ड 2662 ) 3 अं 2 होकर उन्होंने शान्तस्वरूप परात्पर प्रभु लक्ष्मीकान्त 0503. मल व भगवान्‌ नारावणकों श्रद्धापूर्वक प्रणाम किया। भगवान्‌ विष्णु बोले--महादेव ! यहाँ कैसे उस समय भगवान्‌ श्रीहरि रत्रमय सिंहासनपर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.2975)
- **Original**: पधारना हुआ ? अपने क्रोधका कारण बताइये ? विराजमान थे। रत्ननिर्मित अलक्लारोंसे उनका महादेबने कहा--भगवन्‌! राजा वृषध्वज श्रीविग्रह सुशोभित था। किरीट, कुण्डल, चक्र
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.2976)
- **Original**: मेशा परम भक्त है। मैं उसे प्राणोंसे भी बढ़कर और बनमालासे वे अनुपम शोभा पा रहे थे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.2977)
- **Original**: प्रिय मानता हूँ। सूर्यने उसे शाप दे दिया है--यही नूतन मेघके समान उनकी श्याम कान्ति थी।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.2978)
- **Original**: मेरे क्रोधका कारण है। जब मैं अपने कृपापात्र उनका परम सुन्दर विग्रह चार भुजाओंसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.2979)
- **Original**: पत्रके शोकसे प्रभावित होकर सूर्यको मारनेके सुशोभित था और चार भुजावाले अनेक पार्षद
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.2980)
- **Original**: लिये तैयार हुआ, तब वह त्रह्माकी शरणमें चला *ये यथा मां प्रपद्चन्ते तांस्तथैय भजाम्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.2981)
- **Original**: (प्रकृतिखण्ड 13। 29)
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.2982)
- **Original**: गया और इस समय ब्रह्मासहित उसने आपकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.2983)
- **Original**: अपना ग्रास बना लिया है। यही नहीं, किंतु शरण ग्रहण कर ली है। जो व्यक्ति ध्यान अथवा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.2984)
- **Original**: उसका पुत्र रथध्वज भी अब जगतमें नहीं है। वचनसे भी आपके शरणापन्न हो जाते हैं, उनपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.2985)
- **Original**: इस समय रथध्वजके दो पुत्र हैं, उन महाभाग विपत्ति और संकट अपना कुछ भी प्रभाव नहीं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.2986)
- **Original**: पुत्रोंके नाम हैं-धर्मध्वज और कुशध्वज। वे डाल सकते। वे जरा और मृत्युसे सर्वथा रहित
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.2987)
- **Original**: परम चैष्णवपुरुष सूर्यके शापसे श्रीहीन होकर हो जाते हैं। भगवन्‌ ! शरणागतिका फल तो प्रत्यक्ष
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.2988)
- **Original**: जीवन व्यतीत कर रहे हैं-ऐसा कहा जाता है। ही है, फिर मैं क्या कहूँ? आपका स्मरण करते
- **Translation**: 

---

