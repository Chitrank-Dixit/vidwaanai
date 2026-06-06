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

### Verse 1 (Vaivtpuran 543.12814)
- **Original**: 5 अ 5 शक 45444 548 8 5 8 ##. जाय।' तब “बहुत अच्छा' कहकर जाते हुए
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12815)
- **Original**: दैत्यकी कया बिसात है?' युद्धक्षेत्रमें गये। उस भगवान्‌ शिवके पीछे वह दैत्यराज दौड़ा। फिर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12816)
- **Original**: समय उन्होंने मेरे दिये हुए त्रिशूल तथा श्रेष्ठ तो मृत्युझ्य शंकर मृत्युके भयसे त्रस्त होकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12817)
- **Original**: कबचको साथ नहीं लिया था। उनका त्रिपुरके भागे। उनका डमरू गिर पड़ा। मनोहर व्याप्रचर्मकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12818)
- **Original**: साथ एक वर्षतक दिन-रात युद्ध होता रहा; किंतु भी यही दशा हुई। वे दिगम्बर होकर दानवके कोई भी किसीपर विजय नहीं पा सका। भयसे दसों दिशाओंमें भागने लगे। वे चाहते तो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12819)
- **Original**: समराड्रणमें दोनों समान सिद्ध हुए। प्रिये! उसे मार डालते; परंतु भक्तबत्सल जो ठहरे। अत:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12820)
- **Original**: पृथ्वीपर युद्ध करके दैत्यराज मायासे बहुत भक्तपर कृपा करके उसे मारते नहीं थे। साधु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12821)
- **Original**: ऊँचाईपर पचास करोड़ योजन ऊपर उठ गया। पुरुष दुष्टके अनुसार बर्ताव कदापि नहीं करते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12822)
- **Original**: साथ ही विश्वनाथ शंकर भी उस दैत्यका बंध हैं। भगवान्‌ शिव उसे समझा भी न सके। उन्होंने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12823)
- **Original**: करनेके लिये तत्काल ऊपरको उठे। वहाँ निराधार कृपापूर्वक उसे अपना स्वरूप ही माना; क्योंकि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12824)
- **Original**: स्थानपर एक मासतक युद्ध चलता रहा। भयानक उनकी सर्वत्र समान दृष्टि थी। शिव उसे अपनी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12825)
- **Original**: संग्राम हुआ। अन्तमें शिवको उठाकर उस दैत्यने मृत्यु मानकर भयभीत हो उठे। उनका अहंकार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12826)
- **Original**: भूतलपर दे मारा। रथसहित रुद्रके धराशायी हो गल गया। भद्दे! मुझे याद करते हुए उन्होंने मेरी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12827)
- **Original**: जानेपर देवर्षिगण भयभीत हो मेरी स्तुति करने ही शरण ली। उस समय मुझे अपने आश्रमपर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12828)
- **Original**: लगे और बार-बार बोले--' श्रीकृष्ण! रक्षा करो, आते देख उन्हें कुछ धैर्य मिला। उनके कण्ठ,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12829)
- **Original**: रक्षा करो।' भयका कारण उपस्थित हुआ जान ओठ और तालु सूख गये थे और वे भयसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12830)
- **Original**: शिवने निर्भयतापूर्वक मेरा ही स्मरण किया। विह्नल हो ' हे हरे! रक्षा करो, रक्षा करो '--इसका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12831)
- **Original**: उन्होंने संकटकालमें मेंरे ही दिये हुए स्तोत्रसे जप कर रहे थे। तब मैंने उस दैत्यकों अपने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12832)
- **Original**: भक्तिपूर्वक मेरा स्तवन किया। उस समय अपनी पास बिठाकर समझाया और सब समाचार पूछा।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12833)
- **Original**: कलाद्वारा शीघ्र ही वृषभरूप धारण करके मैंने पूछनेपर उसने सब बातें क्रमशः बतायीं। उस
- **Translation**: 

---

