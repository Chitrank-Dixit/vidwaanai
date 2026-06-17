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

### Verse 1 (Vaivtpuran 67.6055)
- **Original**: कर्ममें पतिकी ही दक्षिणा दी जाती है, उस कर्मसे धर्मिष्ठे! वह धर्म-कर्ममें नित्य ही यश और फल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.6056)
- **Original**: मुझे क्या लाभ? मुने! दक्षिणा देनेसे तथा धर्म प्रदान करनेवाली है। प्रिये! देवकार्य, पितृकार्य
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.6057)
- **Original**: और पुत्रकी प्राप्तिसे भी मेरा कौन-सा प्रयोजन अथवा नित्य-नैमित्तिक जो भी कर्म दक्षिणासे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.6058)
- **Original**: सिद्ध होगा? भला, यदि भूमिकी पूजा न की रहित होता है, वह सब निष्फल हो जाता है जाय तो वृक्षेके पूजनसे क्या फल मिलेगा? और उस कर्मसे निश्चय ही दाता कालसूत्र नामक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.6059)
- **Original**: क्योंकि कारणके नष्ट हो जानेपर कार्यकी स्थिति नरकमें जाता है। तत्पश्चात्‌ वह शत्रुओंसे पीड़ित [कहाँ और फिर अन्न तथा फल कहाँसे प्राप्त होकर दीनताको प्राप्त होता है। ब्राह्मणके उद्देश्यसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.6060)
- **Original**: हो सकते हैं ? यदि स्वेच्छानुसार प्राणोंका ही त्याग संकल्प की हुई दक्षिणा यदि उसी समय नहीं
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.6061)
- **Original**: कर दिया जाय तो फिर शरीरसे क्‍या प्रयोजन दे दी जाती है तो वह बढ़ते-बढ़ते अनेक गुनी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.6062)
- **Original**: है? जिसको दृष्टिशक्ति ही नष्ट हो गयी है, उस हो जाती है। आँखसे क्या लाभ? सुरेश्वरो! पतिब्रताओंके लिये श्रीविष्णुने कहा--धर्मिष्ठे ! धर्मकर्मके विषयमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.6063)
- **Original**: पति सौ पुत्रोंके समान होता है। ऐसी दशामें तुम अपने धर्मकी रक्षा करो; क्योंकि धर्मज्ञे! यदि ब्रतमें पतिकों ही दे देना है तो उस ब्रतसे अपने धर्मका पूर्णतया पालन करनेपर सबकी रक्षा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.6064)
- **Original**: अथवा (बव्रतके फलस्वरूप) पुत्रसे क्‍या सिद्ध हो जाती है। होगा? माना कि पुत्र पतिका वंश होता है, किंतु ब्रह्माने कहा-- धर्मज्े! जो किसी कारणवश
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.6065)
- **Original**: उसका एकमात्र मूल तो पति हो है। भला, जहाँ धर्मकी रक्षा नहीं करता है तो धर्मके नष्ट हो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.6066)
- **Original**: मूलधन ही नष्ट हो जाय बहाँ उसका सारा जानेपर उसके कर्त्ताका बिनाश हो जाता है।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.6067)
- **Original**: व्यापार तो निष्फल हो हो जायगा। शर्मने कहा--साध्वि ! पतिको दक्षिणारूपमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.6068)
- **Original**: . इस प्रकार बाद-विबाद चल ही रहा था, देकर यत्रपूर्वक मेरी रक्षा करों। महासाध्वि! मेरे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.6069)
- **Original**: इसी बीच उस सभामें स्थित देवताओं और सुरक्षित रहनेपर सब कुछ कल्याण ही होगा। मुनियोंने आकाशमें बहुमूल्य रत्नोंके बने हुए एक देवताओंने कहा--महासाध्वि ! तुम धर्मकी रथको देखा, जो पार्षदोंद्वारा घिरा हुआ था। वे रक्षा करके अपने ब्रतकों पूर्ण करो। सती ! तुम्हारे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.6070)
- **Original**: सभी पार्षद श्याम रंगवाले तथा चार भुजाधारी ब्रतके पूरा हो जानेपर हमलोग तुम्हारे मनोरथकों
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.6071)
- **Original**: थे। उनके गलेमें वनमाला शोभा पा रही थी पूर्ण कर देंगे।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.6072)
- **Original**: और वे रक्नाभरणोंसे विभूषित थे। तत्पश्चात्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.6073)
- **Original**: 306 + संक्षिप्त ब्रह्मवैवर्तपुराण * अंक कक कक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.6074)
- **Original**: क 48 4 4 644 44 44 446 8£ 48 8 # 8 46 88 88 8844 544 6 % 5 5 % 4 5 4 5 4 55 5 55% 4 44 4 4 8 488 #4 # 8 वैकुण्ठवासी भगवान्‌ उस विमानसे उतरकर
- **Translation**: 

---

