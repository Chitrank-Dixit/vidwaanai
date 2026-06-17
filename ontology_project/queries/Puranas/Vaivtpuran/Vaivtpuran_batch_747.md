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

### Verse 1 (Vaivtpuran 543.13254)
- **Original**: कहा--'विप्रवर! आपका परिचय क्‍या है?' तब शंकरको अपना अभिप्राय बताया। उनकी बात
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13255)
- **Original**: उन द्विजराजने गिरिराजको आदरपूर्वक सब कुछ सुनकर भगवान्‌ शंकर हँसे और उन्हें आश्वासन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13256)
- **Original**: बताया। दे स्वयं शैलराजके पास गये; फिर तो सब देवता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13257)
- **Original**: ब्राह्मण बोले--गिरिराज ! मैं घटक -वृत्तिका शीघ्र ही अपने घर लौटकर आनन्दका अनुभव
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13258)
- **Original**: आन्रय लेकर भूमण्डलमें घूमता रहता हूँ। मेरी करने लगे। क्‍यों न हो, इष्टसिद्धि आनन्द
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13259)
- **Original**: मनके समान तीत्र गति है। गुरुदेवके वरदानसे मैं देनेवाली और अभीष्ट वस्तुकी असिद्धि सदा सर्वत्र पहुँचनेमें समर्थ एवं सर्वज्ञ हूँ। मुझे ज्ञात दुःख बढ़ानेवाली होती है। हुआ है कि तुम अपनी इस लक्ष्मी-सरीखी दिव्य उधर शैलराज अपनी सभामें बन्धुवर्गसे घिरे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13260)
- **Original**: कन्याको शंकरके हाथमें देना चाहते हो, जिसके हुए प्रसन्नतापूर्वक बैठे थे। उनके साथ पार्वती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13261)
- **Original**: शील और कुलका कुछ भी पता नहीं है। शंकर भी थी। इसी बीच स्वयं भगवान्‌ शिव ब्राह्मणका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13262)
- **Original**: निराश्रय हैं-उनका कहीं भी ठौर-ठिकाना नहीं रूप धारण करके सहसा वहाँ आ पहुँचे। उनके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13263)
- **Original**: है। वे असड्र-सदा अकेले रहनेवाले हैं। उनके मुख और नेत्रोंसे प्रसन्नता प्रकट हो रही थी।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13264)
- **Original**: न रूप है, न गुण।वे श्मशानमें बिचरनेवाले, सम्पूर्ण ब्राह्मणके हाथमें दण्ड और छत्र था। उनका वस्त्र
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13265)
- **Original**: भूतोंके अधिपति तथा योगी हैं। शरीरपर वस्त्रतक लंबा था। उन्होंने ललाटमें उत्तम तिलक लगा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13266)
- **Original**: नहीं है। सदा दिगम्बर--नंग-धड़ंग रहते हैं । उनके रखा था। उनके एक हाथमें स्फटिकमणिकी माला
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13267)
- **Original**: शरीरमें सर्पॉका वास है। अड्भरागके स्थानमें थी और उन्होंने गलेमें भगवान्‌ शालग्रामको धारण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13268)
- **Original**: राख--भभूत ही उनके अंगोंकों विभूषित करती कर रखा था। उन्हें देखते ही हिमवान्‌ अपने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13269)
- **Original**: है। उनका स्वरूप ही व्यालग्राही (दुष्टों अथवा सेवकगणोंसहित उठकर खड़े हो गये। उन्होंने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13270)
- **Original**: सर्पोंको ग्रहण करनेवाला) है। बे कालका व्यापादन भूमिपर दण्डकी भाँति पड़कर भक्तिभावसे उस
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13271)
- **Original**: (नाश या अपव्यय) करनेवाले हैं। अज्ञात॑मृत्यु, ज्ञ अपूर्व अतिथिको प्रणाम किया। पार्वतीने भी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13272)
- **Original**: अथवा अज्ञ, अनाथ और अबन्धु* हैं। भव विप्ररूपधारी प्राणेश्वरको भक्तिपूर्वक मस्तक झुकाया।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13273)
- **Original**: (संसारकी उत्पत्तिक कारण) अथवा अभव फिर ब्राह्मणने सबको प्रसन्नतापूर्वक आशीर्वाद
- **Translation**: 

---

