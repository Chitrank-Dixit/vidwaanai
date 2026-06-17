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

### Verse 1 (Vaivtpuran 6.9271)
- **Original**: उतरकर वे नारायणदेव गोप-गोपियोंसे भरी हुई और वक्ष:स्थलपर बनमाला शोभा दे रही थी।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9272)
- **Original**: उस रमणीय सभामें जा पहुँचे। उन्हें देखते ही उनके श्रीअड्र चन्दन, अगुरु, कस्तूरी तथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9273)
- **Original**: ब्रह्म आदि देवता, गोप और गोपी सब-के- केसरके अद्गभरागसे अलंकृत थे। चार भुजाएँ और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9274)
- **Original**: सब सानन्‍्द उठकर खड़े हो गये। सबके हाथ मुस्कराता हुआ मनोहर मुख देखने ही योग्य थे।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9275)
- **Original**: जुड़े हुए थे। देवर्षिगण सामवेदोक्त स्तोत्रद्वारा भक्तोंपर अनुग्रह करनेके लिये वे आकुल दिखायी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9276)
- **Original**: उनकी स्तुति करने लगे। उनकी स्तुति समाप्त देते थे। श्रेष्ठ मणिरत्रोंके सारातिसार तत्त्वसे बने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9277)
- **Original**: होनेपर नारायणदेव आगे जाकर श्रीकृष्णविग्रहमें हुए आभूषण उनके अड्ोंकी शोभा बढ़ा रहे थे।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9278)
- **Original**: बिलीन हो गये। यह परम आश्चर्यकी बात देखकर उनके बामभागमें सुरम्य शरीरवाली शुक्लवर्णा, [सबको बड़ा विस्मय हुआ। मनोहरा, ज्ञानरूपा एवं विद्याकी अधिष्ठात्री देवी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9279)
- **Original**: इसी समय वहाँ एक दूसरा सुवर्णमय रथ सरस्वती दिखायी दीं, जिनके हाथोंमें वेणु, वीणा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9280)
- **Original**: आ पहुँचा। उससे जगत्‌का पालन करनेवाले और पुस्तकें थीं। वे भी भक्तोंपर अनुग्रह करनेके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9281)
- **Original**: त्रिलोकीनाथ विष्णु स्वयं उतरकर उस सभामें लिये कातर जान पड़ती थीं। उन महानारायणके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9282)
- **Original**: आये। उनके चार भुजाएँ थीं। वनमालासे दाहिने भागमें शरत्कालके चन्द्रमाकी-सी प्रभा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9283)
- **Original**: विभूषित पीताम्बरधारी सम्पूर्ण अलंकारोंकी शोभासे तथा तपाये हुए सुबर्णकी भाँति कान्तिसे प्रकाशमान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9284)
- **Original**: सम्पन्न तथा करोड़ों सूर्योंके समान प्रकाशमान परम मनोहरा और रमणीया देवी लक्ष्मी दृष्टिगोचर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9285)
- **Original**: श्रीमान्‌ विष्णु बड़े मनोहर दिखायी देते थे। वे हुईं, जिनके मुखारविन्दपर मन्द मुस्कान खेल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9286)
- **Original**: मन्द-मन्द मुस्करा रहे थे। मुने! उन्हें देखते ही रही थी। उनके सुन्दर कपोल उत्तम रत्नमय
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9287)
- **Original**: सब लोग उठकर खड़े हो गये। सबने प्रणाम कुण्डलोंसे जगमगा रहे थे। बहुमूल्य रत्र,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9288)
- **Original**: करके उनका स्तवन किया। तत्पश्चात्‌ वे भी वहीं महामूल्यवान्‌ वस्त्र उनके श्रीअज्ञोंकी शोभा बढ़ाते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9289)
- **Original**: श्रोराधिकावल्लभ श्रीकृष्णके शरीरमें लीन हो थे। अमूल्य र्नोंद्वारा निर्मित बाजूबंद और कंगन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9290)
- **Original**: गये। यह दूसरा महान्‌ आश्चर्य देखकर उन उनकी भुजाओंकी श्रीवृद्धि कर रहे थे। श्रेष्ठ रह्लोंक
- **Translation**: 

---

