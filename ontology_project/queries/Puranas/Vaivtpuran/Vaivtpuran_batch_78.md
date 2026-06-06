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

### Verse 1 (Vaivtpuran 6.9371)
- **Original**: पल्लवका आधार है तना या डाली तथा उसका भी अवश्य दो। जैसे शरीर छायाके साथ और प्राण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9372)
- **Original**: आधार स्वयं वृक्ष है। वृक्षका आधार अंकुर है, शरीरके साथ रहते हैं, उसी प्रकार हम दोनोंका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9373)
- **Original**: जो बीजकी शक्तिसे सम्पन्न होता है। उस जन्म एवं जीवन एक-दूसरेके साथ बीते। विभो!
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9374)
- **Original**: अंकुरका आधार बीज है, बीजका आधार पृथ्वी यह श्रेष्ठ वर मुझे दे दो। भगवन्‌! भूतलपर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9375)
- **Original**: है, पृथ्वीके आधार शेषनाग हैं। शेषके आधार पहुँचकर भी कहीं हम दोनोंका पलभरके लिये
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9376)
- **Original**: कच्छप हैं, कच्छपषका आधार वायु है और भी वियोग न हो। यह वर मुझे दो। हरे! मेरे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9377)
- **Original**: वायुका आधार मैं हूँ। मेरी आधारस्वरूपा तुम हो; प्राणोंसे ही तुम्हारा शरीर निर्मित हुआ है-मेरे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9378)
- **Original**: क्योंकि मैं सदा तुममें ही स्थित रहता हूँ। तुम प्राण तुम्हारे श्रीअज्ोंस विलग नहीं हैं। मेरी इस
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9379)
- **Original**: शक्तियोंका समूह और मूलप्रकृति ईश्वरी हो। धारणाका कौन निवारण कर सकता है? मेरे शरीररूपिणी तथा त्रिगुणाधार-स्वरूपिणी भी तुम्हीं शरीरसे ही तुम्हारी मुरली बनी है और मेरे मनसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9380)
- **Original**: हो। मैं तुम्हारा आत्मा निरीह हूँ। तुम्हारा संयोग ही तुम्हारे चरणोंका निर्माण हुआ है। तात्पर्य यह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9381)
- **Original**: प्राप्त करके ही चेष्टावान्‌ होता हूँ। शरीरके बिना है कि मैं तुम्हारी मुरलीको अपना शरीर मानती
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9382)
- **Original**: आत्मा कहाँ? और आत्माके बिना शरीर कहाँ? हूँ और मेरा मन तुम्हारे चरणोंसे कभी बिलग
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9383)
- **Original**: देवि! शरीर और आत्मा दोनोंकी प्रधानता है। नहीं होता है। संसारमें कितने ही ऐसे स्त्री-पुरुष
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9384)
- **Original**: बिना दोके संसार कैसे चल सकता है? राधे ! हम हैं, जो सामने एक-दूसरेकी स्तुति करते हैं; परंतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9385)
- **Original**: दोनोंमें कहीं भेद नहीं है; जहाँ आत्मा है, वहाँ कहाँ भी अपने प्रियतममें निरन्तर आसक्त रहनेवाली
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9386)
- **Original**: शरीर है। वे दोनों एक-दूसरेसे अलग नहीँ हैं। मुझ-जैसी प्रेयसी नहीं है। तुम्हारे शरीरके आधे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9387)
- **Original**: जैसे दूधमें धवलता, अग्निमें दाहिका शक्ति, भागसे किसने मेरा निर्माण किया है? हम दोनोंमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9388)
- **Original**: पृथ्वीमें गनध और जलमें शीतलता है, उसी तरह भेद है ही नहीं। अतः मेरा मन निरन्तर तुम्हींमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9389)
- **Original**: तुममें मेरी स्थिति है। धवलता और दुग्धमें, लगा रहता है। मेरी आत्मा, मेरा मन और मेरे प्राण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9390)
- **Original**: दाहिका शक्ति और अग्रिमें, पृथ्वी और गन्धमें जिस तरह तुममें स्थापित हैं, उसी तरह तुम्हारे
- **Translation**: 

---

