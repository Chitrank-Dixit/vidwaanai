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

### Verse 1 (Vaivtpuran 12.846)
- **Original**: मेरे पुत्र व्याधिगण किसी प्राणीका स्पर्श करते पापियोंके भी शासक हैं। उनके पैर स्थूल थे।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.847)
- **Original**: हैं। अतः इसमें मेरा तथा मेरे पुत्रोंका कोई दोष शरीरकी कान्ति श्याम थी। धर्मनिष्ठ सूर्यनन्दन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.848)
- **Original**: नहों है। अब तुम मेरा निश्चित विचार सुनो। यम परकब्रह्मस्वरूप सनातन भगवान्‌ श्रीकृष्णका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.849)
- **Original**: भद्ठे! धर्मसभामें बैठनेवाले जो धर्मज्ञ महात्मा मन्त्र जप रहे थे। उन सबको देख महासाध्वी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.850)
- **Original**: काल हैं, उनसे इस विषयमें पूछो। फिर जो उचित मालावतीके मुख और नेत्र प्रसन्नतासे खिल उठे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.851)
- **Original**: हो वह अवश्य करना।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.852)
- **Original**: मालावतीने कहा--हे काल! आप कर्मोंके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.853)
- **Original**: जिनकी आज्ञाका पालन करते हैं। सती मालाबति! साक्षी हैं, कर्मस्वरूप हैं तथा नारायणके सनातन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.854)
- **Original**: जिनकी आज्ञासे वृक्ष समयपर फूल और फल अंश हैं। भगवन्‌। आप परमेश्वरको नमस्कार है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.855)
- **Original**: धारण करते और देते हैं, जिनके आदेशसे पृथ्वी प्रभो! मैं जीवित हूँ। फिर मेरे प्रियतमको आप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.856)
- **Original**: जलका तथा समस्त चराचर प्राणियोंका आधार क्यों हर ले जाते हैं ? कृपानिधे! आप सर्वज्ञ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.857)
- **Original**: बनी हुई है, क्षमाशील वसुधा जिनके भयसे हैं। अत: सबके दुःखको भी जानते हैं।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.858)
- **Original**: कभी-कभी सहसा कम्पित हो उठती है, ', कालपुरुष बोले--पतिकब्रते! मैं अथवा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.859)
- **Original**: जिनकी मायासे माया भी सदा मोहित रहती यमराज किस गिनतीमें हैं। मृत्युकन्या और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.860)
- **Original**: है, सबको जन्म देनेवाली प्रकृति जिनके भयसे व्याधियोंकी क्‍या बिसात है। हम सब लोग सदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.861)
- **Original**: भीत रहती है, वस्तुओंकी सत्ताकों बतानेवाले ईश्वरकी आज्ञाका पालन करनेके लिये भ्रमण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.862)
- **Original**: वेद भी जिनका अन्त नहीं जानते, समस्त पुराण करते हैं। जिन्होंने प्रकृतिकी सृष्टि की है; ब्रह्मा, जिनकी ही स्तुतिका पाठ करते हैं, जिन विष्णु और शिव आदि देवताओंको प्रकट किया
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.863)
- **Original**: तेजोमय सर्वव्यापी भगवानूकी सोलहवीं कलास्वरूप है; मुनीन्द्र, मनु और मानव आदि समस्त जन्तु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.864)
- **Original**: ब्रह्मा, विष्णु और महाविराट्‌ पुरुष उन्हींके जिनसे उत्पन्न हुए हैं, योगिजन जिनके चरणारविन्दका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.865)
- **Original**: नामका जप करते हैं, वे ही सबके ईश्वर, चिन्तन करते हैं, बुद्धिमान्‌ मनुष्य जिन परमात्माके
- **Translation**: 

---

