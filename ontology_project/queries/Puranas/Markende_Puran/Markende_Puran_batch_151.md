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

### Verse 1 (Markende Puran 0.3001)
- **Original**: हबाच 2 हलोका। 24, एवम्‌ 27 पृक्नमादितः
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3002)
- **Original**: 2439 4 इस्र प्रकार श्रीयार्कण्डेयपुणणमें सावर्णिक पन्‍्वन्तकी कचाके अन्तर्गत देवीमाहान्म्यमें अण्ड-सुण्ड-वध' वायक सातर्ण अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3003)
- **Original**: हज 20590,
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3004)
- **Original**: +रक्तयीज-यथ्थ + 297 550 227222 /7++777### # 666 66533 /2:3:3:% 274 7 7 ##& ह#5क्‍स्‍55:5:::5: 32:00 4744 # 84 3.60202022.00 76 7 # अष्टमोउध्याय: रक्तबीज-वध ध्यान एतस्मिन्नन्तरे भूष जिनाशाय सुरद्विपाम। (“##'अब्णां करुणातक्िताहीं धृतपाशाहुशबाणचाप्हस्ताम्‌।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3005)
- **Original**: भवायामरसिंहानामतिवीर्यबलान्विता:.
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3006)
- **Original**: अणिमादिधिरावृतां पपूर्जरहमित्येव विभावये भवानीप्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3007)
- **Original**: ग्रहोशगुहविष्णूनां तथेद्॒स्थ चर शक्तयरः। मैं अणिमा आदि सिद्धिसयी किरणोंसे आवृत
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3008)
- **Original**: झरीरेभ्यो विनिष्क्रम्य तद्ूपैश्षण्डिकां ययुः
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3009)
- **Original**: भवानीका ध्यान कर्ता हूँ। उनके शरीरका रंग यस्य देवस्वथ यदूपें यथाभूपषणवाहनम्‌। लाल है। नेत्रोंगें कहणा लहरा रही है तथा हाथोंमें
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3010)
- **Original**: तद्धदेव हि तब्छक्तिरसुग़न्‌ योद्धुमाययों
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3011)
- **Original**: पाश, अड्भुश, याण और धनुप शोभा पाते हैं।)
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3012)
- **Original**: हंसयुक्तविधानाग्रे. साक्षसूत्रकमण्डलु:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3013)
- **Original**: ऋषिरयाच # 9 4 +&'अण्डेच निहते दैत्ये मुण्डे च विनिषातिते। अहुलेषु उ सैन्येषु क्षयित्तेष्वसुरेश्वरः
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3014)
- **Original**: त्ततः कोपपराधीनचेताः शुभ: प्रतापतानू। उद्योग सर्वसैन्यानां दैत्यानामादिदेश ह
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3015)
- **Original**: अहा सर्वबलैदैत्या: पडशीतिरुदायुधा:। ऋण्चुनां चतुरशीतिमिंयाँन्तू स्वचलैवृता:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3016)
- **Original**: कोटिवीर्याँणि पद्काशदसुणणां कुलानि वै। शर्त कुलानि धौम्राणां निर्गक्छन्तु ममाज़या
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3017)
- **Original**: 'कालका दौईदा मौर्या: कालकेयास्तथासुरा:। युद्धाय सज्जा निर्यान्तु आज्ञया त्थरिता मम
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3018)
- **Original**: जत्याज्ञाप्यासुरपति: शुम्भो भैरवज्ञासनः। निर्जगाम भरहामसैन्पप्तहसैर्यहुभिर्वृतर:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3019)
- **Original**: आयान्‍्त चण्डिका दृद्दा तत्मैन्यपतिभीषणम्‌। ज्यास्थनै: पूरयामास॒ धरणीगगनान्तरमू्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3020)
- **Original**: तत्त: सिंहो महानादपतीय कृत्तवान्‌ नृप। घण्टास्वनेन तत्नादमम्बिका चोपबुंहयत्‌
- **Translation**: 

---

