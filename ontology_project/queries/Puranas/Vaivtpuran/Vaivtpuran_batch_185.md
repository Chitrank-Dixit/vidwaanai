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

### Verse 1 (Vaivtpuran 13.3069)
- **Original**: प्रसड़ कहता हूँ, सुनों। (अध्याय 14) +#50/700- नव न्‍ज2त परत भगवती तुलसीके प्रादुर्भावका प्रसड़ भगवान्‌ नारायण कहते हैं--नारद!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3070)
- **Original**: उसकी शोभा बढ़ाता रहा। नारद! कार्तिककौ धर्मध्वजकी पत्नीका नाम माधवी था। वह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3071)
- **Original**: पूर्णिमाके दिन उसके गर्भसे एक कन्या प्रकट राजाके साथ गन्धमादन पर्वतपर सुन्दर उपबनमें हुई। उस समय शुभ दिन, शुभ योग, शुभ आनन्द करती थी। यों दीर्घकाल बीत गया,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3072)
- **Original**: क्षण, शुभ लग्र और शुभ ग्रहका संयोग था। किंतु उन्हें इसका ज्ञान न रहा कि कब दिन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3073)
- **Original**: ऐसे योगसे सम्पन्न शुक्रवारके दिन देवी माधवीने बीता, कब रात। तदनन्तर राजा धर्मध्वजके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3074)
- **Original**: लक्ष्मीके अंशसे प्रादुर्भूर उस कन्याकों जन्म हृदयमें ज्ञानका प्रादुर्भावभ हुआ और उन्होंने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3075)
- **Original**: दिया। कनन्‍्याका मुख ऐसा मनोहर था मानो हास-विलाससे विलग होना चाहा; परंतु माधवी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3076)
- **Original**: शरदऋतुकी पूर्णिमाका चन्द्रमा हो। नेत्र शरत्कालीन अभी तृप्त नहीं हो सकी थी, फिर भी उसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3077)
- **Original**: प्रफुल्ल कमलके समान सुन्दर थे। अधर पके गर्भ रह गया। उसका गर्भ प्रतिदिन बढ़ता और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3078)
- **Original**: हुए बिम्बाफलकी तुलना कर रहे थे। मनकों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3079)
- **Original**: मुग्ध करनेबाली उस कन्याके हाथ और पैरके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3080)
- **Original**: और जलपर रही; फिर हजारों बर्षोतक वह केबल तलवे लाल थे। उसकी नाभि गहरी थी।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3081)
- **Original**: पत्ते चचाकर रही और हजारों वर्षोतक केवल शौतकालमें सुख देनेके लिये उसके सम्पूर्ण
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3082)
- **Original**: वायुके आधारपर उसने प्राणॉंकों टिकाकर रखा। अड्भू गरम रहते थे और उष्णकालमें वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3083)
- **Original**: इससे उसका शरीर अत्यन्त क्षीण हो गया था। शीतलाड़्री बनी रहती थी। वह सदा सोलह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3084)
- **Original**: तदनन्तर वह सहस्रों वर्षोतक बिलकुल निराहार वर्षकी किशोरी जान पड़ती थीं। उसके सुन्दर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3085)
- **Original**: रही। निर्लक्ष्य होकर एक पैरपर खड़ी हो वह केश ऐसे थे मानो वटवृक्षको घेरकर शोभा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3086)
- **Original**: तपस्या करती रही। उसे देखकर ब्रह्मा उत्तम पानेवाले बरोह हों। उसको कान्ति पीले
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3087)
- **Original**: वर देनेके विचारसे बदरिकाश्रममें पधारे। हंसपर चम्पककी तुलना कर रही थी। बह असंख्य
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3088)
- **Original**: बैठे हुए चतुर्मुख ब्रह्माको देखकर तुलसीने प्रणाम सुन्दरियोंमें एक थीं। स्त्री और पुरुष उसे
- **Translation**: 

---

