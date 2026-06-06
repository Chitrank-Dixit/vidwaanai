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

### Verse 1 (Vaivtpuran 3.345)
- **Original**: आठ भैरव माने गये हैं। हुई। फिर भगवान्‌के गुह्मदेशसे भूत, प्रेत, पिशाच, श्रीकृष्णके बायें नेत्रसे एक भयंकर पुरुष कृष्माण्ड, ब्रह्मक्षस और विकृत अड्भवाले वेताल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.346)
- **Original**: प्रकट हुआ, जो त्रिशूल, पट्टिश, व्याप्नचर्ममय प्रकट हुए। मुने! तदनन्तर श्रीकृष्णके मुखसे कुछ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.347)
- **Original**: वस्त्र और गदा धारण किये हुए था। वह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.18298)
- **Original**: #भ्रीकृष्णस्तोत्राणि * <ण्5 शिवकृतं अश्रीकृष्णस्तोत्रम्‌ महादेव उबाच जयस्वरूपं॑ जयदं॑ जयेशं जयकारणम्‌ । प्रवरं जयदानां च॒ बन्दे तमपराजितम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.18299)
- **Original**: विश्व॑ विश्वेश्वेशं च्॒ विश्वेश॑ विश्वकारणम्‌ । विश्वाधारं च विश्वस्त॑ विश्वकारणकारणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.18300)
- **Original**: विश्वरक्षाकारणं च विश्वप्नं विश्वजं॑ परम्‌ । फलबीज फलाथार फल चर तत्फलप्रदम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.18301)
- **Original**: तेजःस्वरूपं तेजोद॑ सर्वतेजस्विनां वरम्‌ । इत्येवमुक्त्वा त॑ नत्वा रल्नसिंहासने बरे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.18302)
- **Original**: नारायणं च सम्भाष्य स उवास तदाज्ञया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.18303)
- **Original**: डइति शम्भुकृतं स्तोत्र यो जनः संयतः पठेत्‌ । सर्वसिद्धिर्भवेत्तत्य विजयश्चन॒ पदे. पदे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.18304)
- **Original**: संतत वर्धते मित्र॑ धनमैश्वर्यमेव च । शज्रुसैन्यं क्षयं याति दुःखानि दुरितानि च
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.18305)
- **Original**: डति औब्रह्मवैवर्ते शिवकृतं श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। (ब्रह्मखण्ड 3। 24-29) बह्मकृतं श्रीकृष्णस्तोत्रम्‌ ब्रह्मोवाच कृष्ण बन्दे गुणातीत॑ गोविन्दपेकमक्षरम्‌ । अव्यक्तमत्ययं व्यक्त गोपवेषविधायिनम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.18306)
- **Original**: किशोरवयसं॑ शान्त॑ गोपीकान्त॑ मनोहरम्‌ । नवीननीरदश्याम॑ कोटिकन्दर्पसुन्दरम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.18307)
- **Original**: बृन्दावनवनाभ्यर्णे रासमण्डलसंस्थितम्‌ । रासेश्व_ रासवासं रासोघह्यससमुत्सुकम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.18308)
- **Original**: इत्येवमुक्ला त॑ नत्वा रल़सिंहासने वरे । नारायणेशौं सम्भाष्य स॒ उवास तदाज्ञया
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.18309)
- **Original**: इति ब्रह्मकृतं स्तोत्र प्रातरुत्थाय यः पठेत्‌ । पापानि तस्य नश्यन्ति दुःस्वप्न: सुस्वप्नों भवेत्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.18310)
- **Original**: भ्क्तिर्भवति गोविन्दे. पुत्रपौत्रविवर्धिनी । अकीर्ति: क्षयमाप्रोति सत्कीर्तिवर्धती चिरम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.18311)
- **Original**: इति अ्रीत्रह्मवैवर्ते ब्रह्मकृतं श्रीकृष्णस्तोत्र सम्पूर्णम्‌। (ब्रह्मखण्ड 3। 35-40) धर्मकृतं श्रीकृष्णस्तोत्रम्‌ धर्म उवाच कृष्णं॑ विष्णुं बासुदेव॑ परमात्मानमीश्वरम्‌ । गोविन्द परमानन्दमेकमक्षरमच्युतम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.18312)
- **Original**: गोपेश्वर॑े च गोपीशं गोप॑ गोरक्षक॑ विभुम्‌ । गवामीशं च गोष्स्थ॑ गोबत्सपुच्छधारिणम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.18313)
- **Original**: शोगोषगोपीमध्यस्थं प्रधान पुरुषोत्तमम्‌ । बन्दे नवधनश्याम॑ रासवासं॑ मनोहरम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.18314)
- **Original**: इत्युच्या्य समुत्तिष्ठनू] रत्नसिंहासने बरे । ब्रह्मविष्णुपहेशांस्तानू सम्भाष्य स उवास ह
- **Translation**: 

---

