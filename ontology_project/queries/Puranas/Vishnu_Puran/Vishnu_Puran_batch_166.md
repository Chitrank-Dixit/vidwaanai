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

### Verse 1 (Vishnu Puran 0.3301)
- **Original**: और हे महामुने ! यह सद्ठेका समुद्र भी शाकद्रीपसे घिरा हुआ है, जो विस्तारमें ऋश्ञद्टीपसे क्रौऋद्दीपस्य विस्ताराद्‌ ट्विगुणेन महामुने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3302)
- **Original**: शाकद्वीपेश्वरस्थापि भव्यस्थ सुमहात्मनः । सप्तैव तनयास्तेषां ददौ वर्षाणि सप्त सः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3303)
- **Original**: 59 जआाकट्ठीपके राजा महात्मा भव्यके भी सात ही पुत्र थे। उनको भी उन्होंने पृथकु-पृथक्‌ सात वर्ष
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3304)
- **Original**: 118 श्रीविष्णुपुराण [ अन्ड जलदक्ष कुमारश्च, सुकुमारो मरीचक:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3305)
- **Original**: कुसुमोदश्च मौदाकि: सप्तमश्न महाहुम:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3306)
- **Original**: 60 तर्संज्ञान्येव तत्रापि सप्त वर्षाण्यनुक्रमात्‌। तत्रापि पर्वताः . सप्त वर्षविच्छेदकारिण:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3307)
- **Original**: 61 पूर्वस्तत्रोदयगिरिजलाधारस्तथापर: तथा रैवतक:ः धद्यामस्तथैवास्तगिरिद्विज
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3308)
- **Original**: आम्बिकेयस्तथा रम्यः केसरी पर्वतोत्तम:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3309)
- **Original**: 62 शाकस्तत्र महावृक्ष: सिद्धगन्धर्यसेवित: । यत्रत्यवातसंस्पर्शादाह्मदोी जायते परः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3310)
- **Original**: 63 तञ्न॒पुण्या जनपदाश्चातुर्वर्ण्यसमन्यिता: । नद्यश्नात्र॒ महापुण्या: सर्वपापभयापहा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3311)
- **Original**: 64 सुकुमारी कुमारी च नलिनी धेनुका च या । इक्षुश्न वेणुका चैब गभस्ती सप्तमी तथा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3312)
- **Original**: 65 अन्याश्ञ॒शतहशतस्तत्र श्षुद्रनद्यो महामुने। महीथरास्तथा सन्ति शतशो5थ सहस्रशः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3313)
- **Original**: 66 ता: पिबन्ति मुदा युक्ता जलदादिषु ये स्थिता: । वर्षेषु ते जनपदा: स्वगदिभ्येत्य मेदिनीम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3314)
- **Original**: 67 धर्महानिर्न तेष्वस्ति न सड्भूर्य: परस्परम्‌। मर्यादाव्युत्कमो नाषि तेषु देशेषु सप्तसु
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3315)
- **Original**: 68 वड्ाश्न मागधाओैब मानसा मन्दगास्तथा । बड्ढा ब्राह्मणभूयिष्ठा मागधाः क्षत्रियास्तथा । वैश्यास्तु मानसास्तेषां शुद्वास्तेषां तु मनदगा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3316)
- **Original**: 69 शाकद्दीपे तु तैर्विष्णुः सूर्यरूपधरों सुने । यथोक्तिरिज्यते सम्यककर्ममिर्नियतात्मभि:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3317)
- **Original**: 70 शाकद्दीपस्तु मैत्रेय क्षीरोदेन समावृतः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3318)
- **Original**: शाकद्दीपप्रमाणेन. वलयेनेव वेष्टित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3319)
- **Original**: 79 क्षीराब्धि: सर्वतो ब्रह्मन्पुष्कराख्येन वेष्टित: । द्वीपेन झ्ञाकड्जीपात्तु द्विगुणेन समन्ततः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3320)
- **Original**: 72 पुष्करे सबनस्यापि महावीरो5भवत्सुत: । धातकिश्व॒ तयोस्तत्र द्वे वर्षे नामचिह्ठिते । महावीर॑ तथैवान्यद्धातकीखण्डसंज्ञितम्‌
- **Translation**: 

---

