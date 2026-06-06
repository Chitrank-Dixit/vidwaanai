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

### Verse 1 (Vaivtpuran 16.3314)
- **Original**: द्वारपालसे अनुमति लेकर बह भीतर गया। वहाँ सैकड़ों सुन्दर सड़कें और मणिमय विचित्र वेदियाँ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3315)
- **Original**: जाकर देखा, परम मनोहर शह्डुचूड़ राजाओंके थीं। व्यापारकुशल पुरुषोंके द्वारा बनवाये हुए
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3316)
- **Original**: मध्यमें सुबर्णके सिंहासनपर बैठा था। उसके भवन और ऊँचे-ऊँचे महल चारों ओर सुशोभित
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3317)
- **Original**: मस्तकपर सोनेका सुन्दर छत्र तना था, जिसे एक थे, जिनमें नाना प्रकारकी बहुमूल्य बस्तुएँ भरी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3318)
- **Original**: भृत्यने ले रखा था। उस छत्रमें मणियाँ जड़ी गयी थीं। सिन्दूरके समान लाल मणियोंद्वारा बने हुए
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3319)
- **Original**: थीं। वह विचित्र छत्र रत्नरमय दण्डसे सुशोभित असंख्य, विचित्र, दिव्य एवं सुन्दर आश्रम उस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3320)
- **Original**: था। रज्ननिर्मित कृत्रिम पुष्प उसकी शोभाकों और नगरकी शोभा बढ़ाते थे। भी प्रशस्त कर रहे थे। सफेद एवं चमकीले चँवर मुने! इस प्रकारके सुन्दर नगरमें जाकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3321)
- **Original**: हाथमें लेकर अनेक पार्षद शह्लुचूड़की सेवामें पुष्पदन्तने शल्बुचूड़का भवन देखा। वह नगरके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3322)
- **Original**: संलग्न थे। उत्तम वेष एवं रत्रमय भूषणोंसे बिलकुल मध्यभागमें था। नगरकी आकृति वलयके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3323)
- **Original**: ब्रिभूषित होनेके कारण बह बड़ा सुन्दर जान समान गोल थी। वह ऐसा जान पड़ता था, मानों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3324)
- **Original**: पड़ता था। मुने! उसके गलेमें माला थी। शरीरपर पूर्ण चन्द्रमण्डल हो। प्रज्वलित अग्रिकी लपटोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3325)
- **Original**: चन्दनका अनुलेपन था। वह दो महीन उत्तम वस्त्र समान चार परिखाएँ उसे सुरक्षित किये हुए थीं। पहिने हुए था। वह दानव उस समय सुन्दर शत्रुओंके लिये उस भवनमें प्रवेश करना अत्यन्त
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3326)
- **Original**: बेषवाले असंख्य प्रसिद्ध दानबोंसे घिरा था और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3327)
- **Original**: 152 * संक्षिप्त ब्रह्मबैबतंपुराण « अंक क कक अंक ऋऊ कक अंक कक कक अक् कक ऊक कक कक कक % कक ऋ कक ऋक ऋ ऋ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3328)
- **Original**: कऋ कक 5 # % # % % % ऋकऋ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3329)
- **Original**: 5 % क कक कक कक ऋ कक ऋऊ # % असंख्य दूसरे दानव हाथोंमें अस्त्र लिये इधर-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3330)
- **Original**: वायु, वरुण, बुध, मज़ल, धर्म, शनि, ईशान और उधर घूम रहे थे। ऐसे बैभव-सम्पन्न शद्बुचूड़को
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3331)
- **Original**: प्रतापी कामदेव आदि भी आ गये। देखकर पुष्पदन्त आश्चर्यमें पड़ गया। तदनन्तर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3332)
- **Original**: साथ ही, उद्रदंष्टा, उग्रचण्डा, कोटरा, कैटभी उसने शंकरके कथनानुसार युद्धविषयक संदेश
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3333)
- **Original**: तथा स्वयं सौ भुजावाली भयंकर भगवती भद्रकाली सुनाना आरम्भ किया। देवी भी वहाँ आ गयीं। वे देवी अतिशय श्रेष्ठ पुष्पदन्तने कहा--राजेन्द्र ! प्रभो! मैं भगवान्‌
- **Translation**: 

---

