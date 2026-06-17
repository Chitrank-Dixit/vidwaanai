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

### Verse 1 (Vaivtpuran 3.285)
- **Original**: होता है। चौदह मनुओंके व्यतीत हो जानेपर कल्प हैं; जो क्रमशः प्रकट होते हैं। जैसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.286)
- **Original**: ब्रह्माजीका एक दिन होता है। ऐसे तीन सौ साठ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.287)
- **Original**: दिनोंके बीतनेपर ब्रह्माजीका एक वर्ष पूरा होता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.288)
- **Original**: मध्यभागमें मण्डलाकार रासमण्डल अत्यन्त मनोहर है। इस तरहके एक सौ आठ वर्षोंकी विधाताकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.289)
- **Original**: दिखायी देता था। वह सुविस्तृत, सुन्दर समतल आयु बतायी गयी है। यह परमात्मा श्रीकृष्णफता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.290)
- **Original**: और चिकना था। चन्दन, कस्तूरी, अगर और एक निमेषकाल है। कालवेत्ता दिद्वानोंने ब्रह्माजीकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.291)
- **Original**: कुड्डूससे उसको सजाया गया था। उसपर दही, आयुके बराबर कल्पका मान निश्चित किया है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.292)
- **Original**: लाबा, सफेद धान और दूर्वादल बिखेरे गये थे। छोटे-छोटे कल्प बहुत-से हैं, जो संवर्त आदिके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.293)
- **Original**: रेशमी सूतमें गुँथे हुए नूतन चन्दन-पल्लबोंकी नामसे विख्यात हैं। महर्षि मार्कण्डेय सात
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.294)
- **Original**: बन्दनवारों और केलेके खंभोंद्वारा वह चारों ओरसे कल्पोंतक जीनेवाले बताये गये हैं; परंतु बह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.295)
- **Original**: घिरा हुआ था। करोड़ों मण्डप, जिनका निर्माण कल्प ब्रह्माजीके एक दिनके बराबर ही बतावा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.296)
- **Original**: उत्तम रत्नोंके सारभागसे हुआ था, उस भूमिकी गया है। तात्पर्य यह कि मार्कण्डेय मुनिकी आयु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.297)
- **Original**: शोभा बढ़ाते थे। उनके भीतर रज्लमय प्रदीप जल ब्रह्माजीके सात दिनमें ही पूरी हो जाती है, ऐसा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.298)
- **Original**: रहे थे। वे पुष्प और सुगन्धकी धूपसे वासित थे। निश्चय किया गया है। ब्राह्म, वाराह और पाद्य-ये
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.299)
- **Original**: उनके भीतर अत्यन्त ललित प्रसाधन-सामग्री तीन महाकल्प कहे गये हैं। इनमें जिस प्रकार
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.300)
- **Original**: 2. 7 सृष्टि होती है, वह बताता हूँ, सुनिये। ब्राह्मकल्पमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.301)
- **Original**: मधु-कैटभके मेदसे मेदिनोकी सृष्टि करके सष्टाने भगवान्‌ श्रीकृष्णकी आज्ञा ले सृष्टि-रचना की. थी। फिर वाराहकल्पमें जब पृथ्वी एकार्णवके जलमें डूब गयी थी, बाराहरूपधारी भगवान्‌ विष्णुके द्वारा अत्यन्त प्रयत्नपूर्वकक रसातलसे उसका उद्धार करवाया और सृष्टि-रचना को; तत्पथ्चात्‌ पा्मकल्पमें सृष्टिकर्ता ब्रह्माने विष्णुके नाभिकमलपर सृष्टिका निर्माण किया। ब्रह्मलोकपर्यन्त जो त्रिलोकी है, उसीकी रचना की, ऊपरके जो नित्य तीन लोक हैं, उनकी नहीं। सृष्टि- निरूपणके प्रसंगमें मैंने यह काल-गणना बतायी है और किद्निन्मात्र सृष्टिका निरूपण किया है। - . - अब फिर आप क्‍या सुनना चाहते हैं? [रखी हुई थी। वहाँ जाकर जगदीश्वर श्रीकृष्ण शौनकजीने पूछा--सूतनन्दन! अब यह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.302)
- **Original**: सबके साथ उन मण्डपोंमें ठहरे। मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.303)
- **Original**: उस बताइये कि गोलोकमें सर्वव्यापी महान्‌ परमात्मा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.304)
- **Original**: रासमण्डलका दर्शन करके वे सब लोग आश्चर्वसे गोलोकनाथने इन नारायण आदिकी सृष्टि करके
- **Translation**: 

---

