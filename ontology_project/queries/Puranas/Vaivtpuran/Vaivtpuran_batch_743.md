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

### Verse 1 (Vaivtpuran 543.13174)
- **Original**: निरीह परमात्मस्वरूपमें स्थित हो गया। इस प्रकार था, वह भी भिक्षुकके सामने प्रस्तुत दिखायी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13175)
- **Original**: स्वेच्छामय नाना रूप धारण करनेवाले परमेश्वरका दिया। दूसरे ही क्षणमें वह भिक्षुक द्विभुज-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13176)
- **Original**: दर्शनकर शैलराजके नेत्रोंमें आनन्दके आँसू छलक रूपमें दृष्टिगोचर हुआ। अब उसके हाथमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13177)
- **Original**: आये। उनका अड्भ-अज्ज पुलकित हो गया। विनोदकी साधनभूता मुरली थी। गोपवेष,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13178)
- **Original**: उन्होंने साशड्र दण्डवत्‌-प्रणाम किया और किशोर-अवस्था, श्यामसुन्दर वर्ण, मुस्कराता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13179)
- **Original**: भक्तिभावसे परिक्रमा करके बारंबार मस्तक हुआ मुख, मस्तकपर मोरपंखका मुकुट, श्रीअड्जोमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13180)
- **Original**: झुकाया। फिर हर्षसे उछलकर हिमवानने जब रत्रमय आभूषण, चन्दनके अद्भराग तथा गलेमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13181)
- **Original**: पुनः देखा तो वही भिक्षुक सामने था। बास्तवमें वनमाला-मानो साक्षात्‌ श्रीकृष्ण दर्शन दे रहे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13182)
- **Original**: वह भिक्षुक ही है--ऐसा उन्हें दिखायी दिया। हों। फिर क्षणभरमें वह उज्ज्वल-कान्ति चन्द्रशेखर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13183)
- **Original**: भगवान्‌ विष्णुकी मायासे शैलराज उसके नाना शिवके रूपमें दिखायी दिया। उसके हाथोंमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13184)
- **Original**: रूप-धारण-सम्बन्धी सब बातोंको भूल गये। त्रिशूल और पट्टिश शोभा पा रहे थे। बस्त्रकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13185)
- **Original**: भिक्षुक उनसे भीख माँगने लगा। उसके पास जगह सुन्दर बाघम्बर था। सम्पूर्ण अड्जोमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13186)
- **Original**: भिक्षाका पात्र था। उसने रक्त वस्त्र धारण किया विभूति लगी थी। धवल वर्ण था। गलेमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13187)
- **Original**: था। हाथोंमें श्रक्न॒ और विचित्र डमरूके बाजे अस्थियोंकी माला थी, जो आभूषणका काम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13188)
- **Original**: थे। वह भिक्षामें केवल दुर्गाको ग्रहण करनेके देती थी। कंधेपर सर्पमय यज्ञोपवीत तथा सिरपर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13189)
- **Original**: लिये उत्सुक था, दूसरी किसी बस्तुकों नहीं, तपाये हुए सुवर्णकी-सी कान्तिवाली जटा थी।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13190)
- **Original**: परंतु विष्णु-मायासे मोहित हुए शैलराजने उसकी हाथोंमें शरृज्ष और डमरू थे। सुप्रशस्त एवं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13191)
- **Original**: याचना स्वीकार नहीं कौ। भिक्षुने भी और कुछ मनोहर रूप चित्तकों आकृष्ट कर लेता था।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13192)
- **Original**: नहीं लिया। वह वहीं अन्तर्धान हो गया। प्रिये! भगवान्‌ शिव श्वेत कमलोंके बीजकी मालासे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13193)
- **Original**: उस समय मेना और गिरिराजको ज्ञान हुआ। वे हरिनामका जप करते थे। उनके प्रसन्न मुखपर
- **Translation**: 

---

