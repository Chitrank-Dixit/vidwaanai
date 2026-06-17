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

### Verse 1 (Vaivtpuran 32.7597)
- **Original**: श्रेष्ठ पुरुष दृष्टिगोचर हो रहे थे। वे भक्तोंपर भद्रकालीको प्रणाम करके पुष्करतीर्थमें गये और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.7598)
- **Original**: अनुग्रह करनेवाले थे तथा उनका मुख मन्द वहाँ मन्त्र सिद्ध करने लगे। उन्होंने एक महीनेतक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.7599)
- **Original**: मुस्कानसे खिल रहा था। परशुरामने उन ईश्वरको अन्न-जलका परित्याग कर दिया और भक्तिपूर्वक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.7600)
- **Original**: दण्डकी भाँति लेटकर सिरसे प्रणाम किया और श्रीकृष्णके चरणकमलका ध्यान करते हुए वायुको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.7601)
- **Original**: वर माँगा--' भगवन्‌! मैं इक्कीस बार पृथ्वीको अवरुद्ध कर दिया। फिर आँखें खोलकर देखा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.7602)
- **Original**: भूपालोंसे रहित कर दूँ, आपके चरणकमलोंमें तो उनको आकाश एक अद्भुत तेजसे व्याप्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.7603)
- **Original**: मेरी अनपायिनी सुदृढ़ भक्ति हो और मैं निरन्तर दिखायी पड़ा। उस तेजसे दसों दिशाएँ उद्दौत
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.7604)
- **Original**: आपके पादारविन्दका दास बना रहूँ--यह बर हो रही थीं और सूर्यका तेज प्रतिहत हो गया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.7605)
- **Original**: मुझे प्रदान कीजिये।' तब श्रीकृष्ण उन्हें वह वर था। उस तेजोमण्डलके मध्य उन्हें एक रत्ननिर्मित
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.7606)
- **Original**: देकर वहीं अन्तर्धान हो गये और परशुराम उन क़तूनां राजसूयो यो गायत्री छन्दसां च यः। गन्धर्वाणां चित्ररथस्त॑ गरिष्ठं नमाम्यहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.7607)
- **Original**: क्षीरस्वरूपो गब्यानां पवित्राणां च. पावकः। पुण्यदानां च य: स्तोत्र त॑ नमामि शुभप्रदम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.7608)
- **Original**: तृणानां कुशरूपो यो व्याधिरूपश॒ बैरिणाम्‌। गुणानां शान्तरूपो यक्षित्रकूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.7609)
- **Original**: तेजोरूपो ज्ञानकूप: सर्वरूपध्ध यो महान्‌। सर्वानिर्वचनीय च त॑ नमामि स्वयं विभुम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.7610)
- **Original**: सर्वाधारेषु यो बवायुर्यधात्मा नित्यरूपिणाम्‌ू । आकाशो व्यापकानां यो व्यापक॑ त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.7611)
- **Original**: वेदानिर्वचनीय॑ यन्न स्तोतुं पण्डितः क्षम: । यदनिर्ववनीय॑ च को वा तत्स्तोतुमीश्चर:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.7612)
- **Original**: वेदा न शक्ता य॑ स्तोतुं जडीभूता सरस्वती । तं च वाइमनसो: पार॑ को विद्वान्‌ स्तोतुमीश्चर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7613)
- **Original**: शुद्धतेज:स्वरूप॑ च भक्तानुग्रहविग्रहम्‌ । अतीवकमनीय॑ च. श्यामरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7614)
- **Original**: द्विभुज॑ मुरलीवक्म॑ किशोर॑ सस्मित॑ मुदा । शश्वद्‌ गोपाक्ननाभिश्च वीक्ष्यमाणं नमाम्यहम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7615)
- **Original**: राधया दत्तताम्बूलं भुक्तवत्त॑ मनोहरम्‌ । रम्रसिंहासनस्थ॑ च तमीशं .प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7616)
- **Original**: रत्रभूषणभूषाद्य सेवित॑ श्वेतचामरै: । पार्षदप्रवरैगोंपकुमारैस्त नमाम्यहम्‌
- **Translation**: 

---

