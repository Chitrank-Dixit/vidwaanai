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

### Verse 1 (Vishnu Puran 0.8961)
- **Original**: नारदजीसे यह समाचार पाकर केंसने कुपित होकर वसुदेल और देखकीको कारागहमें बन्द कर दिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8962)
- **Original**: है ड्वेज ! शसुदेखणी भी, जैसा कि उन्होंने पहरेट कह दिया था, अपने प्रत्येक पुत्रको केसक्वे सौंपते रहे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8963)
- **Original**: ऐसा सुना जाता है कि पहले छः गर्भ हिरण्यकशिपूफे पुत्र थें। भगवान्‌ विष्णुकी प्रेरणासे योगनिदा उन्‍हें क्रमशः गर्भनें स्थित करती रही *
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8964)
- **Original**: जिस अविद्या-रूपिणीसे सम्पूर्ण जगत्‌ मोहित हो रहा है, वह योगनिद्रा भगवान्‌ विष्णुकी महामाया है उससे भगवान्‌ श्रोहरिने कहा--
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8965)
- **Original**: ओरीभगवान्‌ बोछे--हे निद्रे ! जा, मेरे आज्ञासे तू पातालूमें स्थित छः गर्भाँंको एक-एक करके देवकोकी कुक्षिमें स्थापित कर दे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8966)
- **Original**: कंसद्वारा उन सबक्रे मारे जानेपर शेष नामक मेरा आँडा अपने अंशांशसे देलकीके ___ $ थे ब्लालक पूर्वजन्ममे हिरण्यकशिपुफे भाई कालनेमिके पुत्र थे; इसीसे इन्हें उसका पुत्र ऊहा गया कालनेमिके पुत्र थे; इसीसे इन्हें उसका पुत्र ऊहा गया है। ड्न णाक्षसकुमारोंने हिरण्यकदिपुका अनादर कर भगवान्‌की भक्ति की थी; अतः उसते कुपित होकर इन्हें शाप दिया कि तुमणोग अपने पिताके हाथसे ही मारे जाओगे । यह प्रसंग हरिवेदामें आया है ।
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8967)
- **Original**: आ 1] पञ्चम अंश 3143 गोकुले वसुदेवस्य भार्यान्‍्या रोहिणी स्थिता । तस्थास्स सम्भूतिसमं देवि नेयस्त्वयोदरम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8968)
- **Original**: 74 सप्तमों भोजराजस्यथ भयाद्रोघोपरोधत: । देवक्या: पतितो गर्भ इति लोको बदिष्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8969)
- **Original**: 75 गर्भसड्डूर्षणात्सो5थ लोके सड्डूर्षणेति वे । संज्ञामवाप्स्यते बीरइश्वेताद्रेशिखरोपम:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8970)
- **Original**: 76 ततो5ह सम्भविष्यामि देवकीजठरे शुभे । गर्भे त्वया यश्योदाया गन्तव्यमविलम्बितम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8971)
- **Original**: 77 ज्रावृदकाले चर नभपि कृष्णाष्टम्थामह निशि । उत्पत्य्थामि नवम्यां तु प्रसूर्ति त्वमवाप्स्यसि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8972)
- **Original**: 78 यशोदाशायने मां तु देबक्यास्त्वामनिन्दिते । मच्छक्तिप्रेरितमतिर्वसुदेशो.. नविष्यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8973)
- **Original**: 79 कंसश्च त्वामुपादाय देवि शैलशिल्ातले। प्रक्षेप््यत्यन्तरिक्षे चर संस्थान त्वमवाप्स्यसि
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8974)
- **Original**: 80 ततस्त्वां शतदुकछक्र: प्रणम्य मम गौरवात्‌ । प्रणिपातानतशिरा भगिनीत्वे ग्रहीष्यति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8975)
- **Original**: 89 ते च शुप्भनिशुष्भादीन्‍हत्वा दैत्यास्सहखश: । स्थानैरनेके: पृथिवीमशेषां मण्डयिष्यसि
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8976)
- **Original**: 82 लज्जा पुष्टिरुषा या तु काचिदन्या त्वमेव सा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8977)
- **Original**: 83 ये त्वामार्येति दुर्गेति वेदगर्भाम्बिकेति च। भ्रद्रेति भद्रकालीति क्षेमदा भाग्यदेति च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8978)
- **Original**: 84 प्रातक्षैबापरा्ने च स्तोष्यन्त्यानप्रमूर्त्तय: । तेषां हि प्रार्थित॑ सर्व मत्प्रसादाद्धविष्यति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8979)
- **Original**: 85 सुरामांसोपहारैश्व भक्ष्यभोज्यैश्न पूजिता । नृणामशेषकामांस्त्व॑ प्रसन्ना सम्प्रदास्यसि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8980)
- **Original**: 86 ते सर्वे सर्वदा भट्ढे मठ्नसादादसंशयम्‌। असन्दिग्धा भविष्यन्ति गच्छ देवि यथोदितम्‌
- **Translation**: 

---

