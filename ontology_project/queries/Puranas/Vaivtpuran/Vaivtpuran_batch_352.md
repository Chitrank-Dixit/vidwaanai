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

### Verse 1 (Vaivtpuran 16.3534)
- **Original**: समस्त रुद्रगण दानवगणोंके साथ लड़ने लगे। व्याप्त हुई वह शक्ति प्रलयाग्रिकी शिखाके समान
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3535)
- **Original**: वह महान्‌ युद्ध प्रलयकालके समान भयंकर जान जान पड़ती थी। दानवराजने उसे क्रोधपूर्वक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3536)
- **Original**: पड़ता था। उस समय भगवान्‌ शंकर काली और कार्तिकेयके ऊपर बड़े बेगसे दे मारा। वह शक्ति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3537)
- **Original**: पुत्रके साथ बटबृक्षके नीचे ठहरे हुए थे। मुने! उनके शरीरपर प्रज्वलित अग्रिकी राशिके समान
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3538)
- **Original**: शेष समस्त सैन्यसमुदाय निरन्तर युद्धमें तत्पर थे। गिरी। महाबली कार्तिकेय उस शक्तिसे आहत हो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3539)
- **Original**: शल्बुचूड़ रत्रमय आभूषणोंसे विभूषित हो करोड़ों मूच्छित हो गये। तब काली उन्हें गोदमें उठाकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3540)
- **Original**: दानवोंके साथ रमणीय रत्रमय सिंहासनपर विराजमान भ्रगवान्‌ शिवके पास ले गयी। था। उस युद्धमें भगवान्‌ शंकरके समस्त योद्धा शिवने लीलापूर्वक ज्ञान-बलसे उन्हें जीवित
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3541)
- **Original**: पराजित हो गये। समस्त देवता क्षत-विक्षत हो कर दिया। साथ ही असीम बल प्रदान किया।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3542)
- **Original**: भयके मारे भाग चले। प्रतापी बीर कार्तिकिय तत्काल उठकर खड़े हो यह देख भगवान्‌ स्कन्‍्दकों बड़ा क्रोध गये। उसी क्षण भगवान्‌ शंकरने अपनी सेना तथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3543)
- **Original**: हुआ। उन्होंने देवताओऑंको अभय दान दिया और देवताओंको युद्धके लिये प्रेरित किया। सेनासहित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3544)
- **Original**: अपने तेजसे आत्मीय गणोंका बल बढ़ाया। वे दानवराजोंके साथ देवताओंका युद्ध पुनः प्रारम्भ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3545)
- **Original**: स्वयं भी दानवगणोंके साथ युद्ध करने लगे। हुआ। स्वयं देवराज इन्द्र वृषप्रकि साथ युद्ध
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3546)
- **Original**: उन्होंने समराद्भरणमें दानवॉकी सौ अक्षौहिणी करने लगे। सूर्यदेवने विप्रचित्तिक साथ युद्ध छेड़
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3547)
- **Original**: सेनाका संहार कर डाला। कमललोचना कालीने दिया। चन्द्रमा दप्भके साथ भिड़ गये और बड़ा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3548)
- **Original**: कुपित हो खप्पर गिराना आरम्भ किया। वे भारी युद्ध करने लगे। कालने कालेश्वरके साथ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3549)
- **Original**: दानबोंके सौ-सौ खप्पर खून एक साथ पी जाती और अग्रिदेवने गोकर्णके साथ जूझना आरम्भ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3550)
- **Original**: थीं। लाखों हाथी और घोड़ोंकों एक ही हाथसे किया। कालकेयसे कुबेर और मयासुरसे विश्वकर्मा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3551)
- **Original**: समेटकर लौलापूर्वक लील जाती थीं। मुने! लड़ने लगे। मृत्युदेवता भयंकर नामक दानवसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3552)
- **Original**: समरभूमिमें सहस्नों कबन्ध (बिना सिरके धड़) और यम संहारके साथ भिड़ गये। कलविड्जू
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3553)
- **Original**: नृत्य करने लगे। स्कन्दके बाण-समूहोंसे क्षत- और वरुणमें, चञ्लल और वायुमें, बुध और
- **Translation**: 

---

