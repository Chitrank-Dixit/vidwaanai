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

### Verse 1 (Vaivtpuran 36.7982)
- **Original**: कवचकी याचना करूँगा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.7983)
- **Original**: ब्राह्मणकी बात सुनकर चाहा; इतनेमें भगवान्‌ नारायण ब्राह्मणका वेष
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.7984)
- **Original**: परशुरामका मन भयभीत हो गया, तब वे दुःखी धारण करके वहाँ प्रकट हो गये और बोले।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.7985)
- **Original**: हृदयसे उस वृद्ध ब्राह्मणसे बोले। ब्राह्मणवेषधारी नारायणने कहा--वत्स। परशुरामने कहा--' महाप्राज्ञ! ब्राह्मणरूपधारी भार्गव! यह क्‍या कर रहे हो? तुम तो ज्ञानियोंमें। आप कौन हैं, मैं यह नहीं जान पा रहा हूँ; श्रेष्ठ हो; फिर भ्रमवश क्रोधावेशमें आकर मनुष्यका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.7986)
- **Original**: अत: मुझ अनजानको शीघ्र ही अपना परिचय वध करनेके लिये पाशुपतका प्रयोग क्‍यों कर रहे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.7987)
- **Original**: दीजिये, तत्पश्चात्‌ राजाके पास जाइये।' परशुरामका हो? इस पाशुपतसे तो तत्काल ही सारा विश्व वचन सुनकर ब्राह्मणको हँसी आ गयी, वे 'मैं भस्म हो सकता है; क्योंकि यह शस्त्र परमेश्वर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.7988)
- **Original**: विष्णु हूँ” यों कहकर राजाके पास याचना करनेके श्रीकृष्णेक अतिरिक्त और सबका विनाशक है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.7989)
- **Original**: लिये चले गये। उन दोनोंके संनिकट जाकर अहो! पाशुपतकों जीतनेकी शक्ति तो सुदर्शनमें ही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.7990)
- **Original**: विष्णुने उससे कबचकी याचना कौ। तब विष्णुकी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.7991)
- **Original**: + गणपतिखण्ड * 377 ###&#&####ऋ#ऋ#ऋऋऊऋऊऋऊऋकऋकऋककऋऋ कक कऋकऋक्ऋ्ऋ्ऋ्ऋऋऋऋऊऋडऋफऋऋक 8 # 6
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.7992)
- **Original**: 55% ###&&###%$$5$5%5$5% मायासे मोहित होकर उन्होंने विष्णुकों दोनों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.7993)
- **Original**: वृद्धि करनेवाली हैं और मुस्कराती हुई जो कवच दान कर दिये। भगवान्‌ विष्णु उन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.7994)
- **Original**: कमल-वनकी ओर निहार रही हैं; उन पद्मिनी कबचोंको लेकर वैकुण्ठकों चले गये। देवीका मैं आनन्दपूर्वक भजन करता हूँ। नारदजीने पूछा--महामुने ! भूपाल पुष्कराक्षको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.7995)
- **Original**: . साधकको चाहिये कि चन्दनका अष्टदल- महालक्ष्मीका कवच किसने दिया था? तथा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.7996)
- **Original**: कमल बनाकर उसपर कमल-पुष्पोंद्वाग महालक्ष्मीको पुष्कराक्षके पुत्रकों दुर्गाका दुर्लभ कवच किसने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.7997)
- **Original**: पूजा करे। फिर “गण' का भलीभाँति पूजन करके बताया था? आप इसे बतलानेकी कृपा करें;
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.7998)
- **Original**: उन्हें षोडशोपचार समर्पित करे। तदनन्तर स्तुति क्योंकि इसे सुननेकी मेरी प्रबल उत्कण्ठा है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.7999)
- **Original**: करके भक्तिपूर्वक उनके सामने सिर झुकावे। जगदुरो! साथ ही मुझे यह भी बताइये कि उन
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.8000)
- **Original**: ब्रह्म! अब सबका साररूप कबच तुम्हें बतलाता दोनोंके कबच कैसे थे, उनका क्या फल है और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.8001)
- **Original**: हूँ; सुनो। वे दोनों मन्त्र किस तरहके थे? श्रीनारायण आगे कहते हैं--विप्रवर! श्रीनारायणने कहा--नारद! बुद्धिमान्‌ भगवान्‌ पद्मनाभने अपने नाभिकमलपर स्थित पुष्कराक्षको महालक्ष्मीका कवच और दशाक्षर-
- **Translation**: 

---

