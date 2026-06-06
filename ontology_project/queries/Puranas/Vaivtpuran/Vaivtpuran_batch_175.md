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

### Verse 1 (Vaivtpuran 12.9986)
- **Original**: विषाग्निसर्पशत्रुभ्यों भयं तस्य न वखिद्यते । जले स्थले चान्तरिक्षे निद्रायां रक्षतीश्वरः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.9987)
- **Original**: ( श्रीकृष्णजन्मखण्ड 12। 15-36)
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.9988)
- **Original**: « श्रीकृष्णजन्पखण्ड * डड9 न न उ]]]]4400]20 00 / 0040 0 0 0 024 44
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.9989)
- **Original**: 44 /44.
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.9990)
- **Original**: मानो चारों वेदोंका तेज मूर्तिमान्‌ हो गया हो।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.9991)
- **Original**: पुरुष प्रसन्नमनसे शिशुकों आशीर्वाद देने योग्य उनके कण्ठमें साक्षात्‌ सरस्वतीका वास था। वे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.9992)
- **Original**: हैं। निश्चय ही ब्राह्मणोंका आशीर्वाद तत्काल पूर्ण शास्त्रीय सिद्धान्तके एकमात्र विशेषज्ञ थे और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.9993)
- **Original**: मड्जलकारी होता है।' दिन-रात श्रीकृष्णचरणारविन्दोंके ध्यानमें तत्पर 27 स््ऋछ रहते थे। उन्हें जीवन्मुक्त अवस्था प्राप्त थी। वे भ/ 07 ज चजा ्छध सिद्धोंके स्वामी, सर्वज्ञ और सर्वदर्शी थे। ' उन्हें देखकर यशोदाजी खड़ी हो गयीं। " ] रा! उन्होंने मस्तक झुकाकर मुनिके चरणोंमें प्रणाम हं।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.9994)
- **Original**: # किया और उन्हें बैठनेके लिये सोनेका सिंहासन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.9995)
- **Original**: देकर आतिथ्यके लिये पाद्य, अर्घ्य, गौ तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.9996)
- **Original**: मधुपर्क निवेदन किया। मुस्कराती हुई नन्दरानीने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.9997)
- **Original**: (€7 अपने बालकसे मुनीन्द्रकी वन्दना करवायी। मुनिने भी मन-ही-मन श्रीहरिको सौ-सौ प्रणाम के किये और प्रसन्नतापूर्वक वेदमन्त्रोंक अनुकूल
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.9998)
- **Original**: ब्ड आशीर्वाद दिया। यशोदाजीने मुनिके शिष्योंको ऐसा कहकर नन्‍्दरानी भक्तिभावसे भी प्रणाम किया तथा भक्तिभावसे उन सबके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.9999)
- **Original**: सामने खड़ी हो गयीं। उस सतीने नन्‍्दरायजीको लिये पृथक्‌-पृथक्‌ पाद्य आदि अर्पित किये। उन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.10000)
- **Original**: बुलानेके लिये चर भेजा। यशोदाजीकी पूर्वोक्त शिष्योंने यशोदाजीको आशीर्वाद दिया। मुनि बातें सुनकर मुनिवर गर्ग हँसने लगे। उनके अपने शिष्योंके साथ पैर धोकर जब सिंहासनपर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.10001)
- **Original**: शिष्य-समूह भी हास्यकी छटासे दसों दिशाओंको बैठे, तब सती-साध्वी यशोदा बालकको गोदमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.10002)
- **Original**: प्रकाशित करते हुए जोर-जोरसे हँस पड़े। तब ले भक्तिभावसे मस्तक झुकाकर दोनों हाथ जोड़
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.10003)
- **Original**: उन शुद्धबुद्धि महामुनि गर्गने यथार्थ हितकर, मुनिके आगमनका कारण पूछनेको उद्यत हुईं। वे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.10004)
- **Original**: नीतियुक्त एवं अत्यन्त आनन्ददायक बात कही। बोलीं-' मुने! आप स्वात्माराम महर्षि हैं, आपसे श्रीगर्गजी बोले--देवि ! तुम्हारा यह समयोचित कुशल-मज्जल पूछना यद्यपि उचित नहीं है,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.10005)
- **Original**: वचन अमृतके समान मधुर है। जिसका जिस तथापि इस समय मैं आपका कुशल-समाचार कुलमें जन्म होता है, उसका स्वभाव भी वैसा पूछ रही हूँ। अबला बुद्धिहीना होती है। अतः
- **Translation**: 

---

