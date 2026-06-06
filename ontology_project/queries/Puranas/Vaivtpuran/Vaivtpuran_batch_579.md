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

### Verse 1 (Vaivtpuran 45.4441)
- **Original**: आज्ञा ले पुष्करक्षेत्रमें तपस्या करनेके लिये चली मनसापञ्लमीको उन देवीके लिये बलि अर्पण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4442)
- **Original**: गयी। वहाँ जाकर उसने परब्रह्म भगवान्‌ श्रीकृष्णकी करता है, वह अवश्य ही धनवान्‌, पुत्रवान्‌ और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4443)
- **Original**: तीन युगोंतक उपासना की। इसके बाद उसे कीर्तिमान्‌ होता है। महाभाग! पूजाका विधान
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4444)
- **Original**: तपस्यामें सिद्धि प्राप्त हुई। भगवान्‌ श्रीकृष्णने कह चुका। अब धर्मदेवके मुखसे जैसा कुछ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4445)
- **Original**: सामने प्रकट होकर उसे दर्शन दिये। उस समय सुना है, वह उपाख्यान कहता हूँ, सुनो।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4446)
- **Original**: कृपानिधि श्रीकृष्णने उस कृशाड्री बालापर अपनी प्राचीन समयकी बात है। भूमण्डलके सभी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4447)
- **Original**: कृपाकी दृष्टि डाली। उन्होंने उसका दूसरोंसे पूजन मानव नागोंके भयसे आक्रान्त हो गये थे। नाग
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4448)
- **Original**: कराया और स्वयं भी उसकी पूजा की; साथ जिन्हें काट खाते, वे जीवित नहीं बचते थे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4449)
- **Original**: ही बर दिया कि 'देवि! तुम जगत्‌में पूजा प्राप्त यह देख-सुनकर कश्यपजी भी भयभीत हो गये;
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.4450)
- **Original**: करो।' इस प्रकार कल्याणी मनसाको वर प्रदान अत: ब्रह्माजीके अनुरोधसे उन्होंने सर्पभयनिवारक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.4451)
- **Original**: करके भगवान्‌ अन्तर्धान हो गये। मन्त्रोंकी रचना की । ब्रह्माजीके उपदेशसे लेदबीजके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.4452)
- **Original**: इस तरह इस मनसादेवीकी सर्वप्रथम अनुसार मन्त्रोंकी रचना हुईं। साथ ही ब्रह्माजीने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.4453)
- **Original**: भगवान्‌ श्रीकृष्णने पूजा की। तत्पश्चात्‌ शंकर, अपने मनसे उत्पन्न करके इन देवीकों इस मन्त्रकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.4454)
- **Original**: कश्यप, देवता, मुनि, मनु, नाग एवं मानव अधिष्ठात्री देवी बना दिया। तपस्या तथा मनसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.4455)
- **Original**: आदिसे त्रिलोकीमें श्रेष्ठ त्रतका पालन करनेवाली प्रकट होनेके कारण ये देवी 'मनसा' नामसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.4456)
- **Original**: यह देवी सुपूजित हुई। फिर कश्यपजीने जरत्कार विख्यात हुईं। कुमारी अवस्थामें ही ये भगवान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4457)
- **Original**: मुनिके साथ उसका विवाह कर दिया। वे मुनि शंकरके धाममें चली गयीं। कैलासमें पहुँचकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4458)
- **Original**: महान्‌ योगी थे। विवाह करनेके पश्चात्‌ तपस्या इन्होंने भक्तिपूर्वक भगवान्‌ चन्द्रशेखर्की पूजा करनेमें संलग्र हो गये। वे एक दिन पुष्करक्षेत्रमें करके उनकौ स्तुति की। मुनिकुमारी मनसाने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4459)
- **Original**: उस बटवृक्षके नीचे देवी जरत्कारुकी जाँघपर देबताओंके वर्षसे हजार वर्षोतक भगवान्‌ शंकरकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4460)
- **Original**: लेट गये और उन्हें नींद आ गयी। इतनेमें उपासना कौ। तदनन्तर भगवान्‌ आशुतोष इनपर
- **Translation**: 

---

