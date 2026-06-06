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

### Verse 1 (Vaivtpuran 28.7258)
- **Original**: पच्चौकारीसे युक्त उत्तम मणियोंके कलशोंसे विस्तारवाला गोलोक है। उससे ऊपर दूसरा लोक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.7259)
- **Original**: उज्ज्वल दीखनेवाले अमूल्य मणियोंद्वारा निर्मित नहीं है। वही सर्वोपरि कहा जाता है। मनके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.7260)
- **Original**: सौ करोड़ भवनोंसे युक्त था। समान वेगशाली योगीन््र परशुरामने उस शिवलोककों उसके रमणीय मध्यभागमें उन्हें शंकरजीका देखा। वह महान्‌ अद्भुत लोक उपमान और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.7261)
- **Original**: भवन दीख पड़ा। उस परम मनोहर भवनके चारों उपमेयसे रहित अर्थात्‌ अनुपम, श्रेष्ठ योगीद्धों,, ओर बहुमूल्य मणियोंकी चहारदीवारीका निर्माण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.7262)
- **Original**: + गणपतिखण्ड « 359 40400 4000 00004 /482/ 2 // 2 22]/ ान्‍अ ऑऑ्ाऑपऑपआऑपऑआआअ प हुआ था। वह इतना ऊँचा था कि आकाशका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.7263)
- **Original**: नाना प्रकारकी चित्रकारीसे चित्रित होनेके कारण स्पर्श कर रहा था। उसका रंग दूध और जलके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.7264)
- **Original**: अत्यन्त सुन्दर थे तथा उनपर द्वारपाल नियुक्त थे। समान उज्ज्वल था। उसमें सोलह दरवाजे थे तथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.7265)
- **Original**: उन्हें देखकर परशुरामकों महान्‌ आश्चर्य हुआ। वह सैकड़ों ऐसे मन्दिरोंसे सुशोभित था, जो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.7266)
- **Original**: आगे बढ़नेपर उन्हें शंकरजीकी सभा दिखायी अमूल्य रत्रोंद्वारा निर्मित तथा रत्रोंकी सीढ़ियोंसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.7267)
- **Original**: पड़ी, जो बहुत-से सिद्धगणोंसे व्याप्त, महर्षियोंद्वारा विभूषित थे। उनमें हीरे जड़े हुए रत्नोंके खंभे और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.7268)
- **Original**: सेवित तथा पारिजात-पुष्पोंके गन्धसे युक्त वायुद्वारा किवाड़ लगे थे। वे मणियोंकी जालियोंसे सुशोभित,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.7269)
- **Original**: सुवांसित थी। उस सभामें उन्होंने देवेश्वर शंकरके उत्तम रत्नोंके कलशोंसे प्रकाशित, नाना प्रकारके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.7270)
- **Original**: दर्शन किये। वे रत्नाभरणोंसे सुसज्जित हो सत्रसिंहासनपर विचित्र चित्रोंसे चित्रित अतएव परम मनोहर थे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.7271)
- **Original**: विराजमान थे। उनके ललाटपर चन्द्रमा सुशोभित वहाँ उस भवनके आगे परशुरामने सिंहद्वारका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.7272)
- **Original**: हो रहा था। वे बाघाम्बर पहने तथा त्रिशूल और दर्शन किया, जिसमें बहुमूल्य रत्रोंके बने हुए
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.7273)
- **Original**: पट्टिश धारण किये हुए थे। उनका शरीर विभूतिसे किवाड़ लगे थे। उसका भीतरी भाग पद्मराग एवं
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.7274)
- **Original**: सुशोभित था। वे सर्पका यज्ञोपवीत पहने थे तथा महामरकत मणियोंद्वारा रचित बेदियोंसे सदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.7275)
- **Original**: महान्‌ कल्याणस्वरूप, कल्याण करनेवाले, कल्याणके बाहर-भीतर सुशोभित रहता था। नाना प्रकारके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.7276)
- **Original**: कारण, कल्याणके आश्रयस्थान, आत्मामें रमण चित्रोंसे चित्रित होनेके कारण वह अत्यन्त
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.7277)
- **Original**: करनेवाले, पूर्णजाम और करोड़ों सूर्योंके समान सुहावना लग रहा था। उसके द्वारपर दो भयंकर
- **Translation**: 

---

