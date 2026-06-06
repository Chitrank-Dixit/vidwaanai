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

### Verse 1 (Vaivtpuran 543.12374)
- **Original**: सर्वमज्जलमब्जल्ये सर्वमज़लसंयुते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12375)
- **Original**: सर्वमज़लबीजे च नमस्ते. सर्वमजजले
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12376)
- **Original**: सर्वप्रिये सर्वबीजे सर्वाशुभविनाशिनि
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12377)
- **Original**: सर्वेशे. सर्वजनके.. नमस्ते. शंकरप्रिये
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12378)
- **Original**: परमात्मस्वरूपे च तित्यरूपे . सनातनि । सराकारें च निराकारे सर्वरूपे नमोउस्तु ते
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12379)
- **Original**: क्षुतृष्णेच्छा दया श्रद्धा निद्रा तन्द्रा स्मृति: क्षमा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12380)
- **Original**: एतास्तव कला: सर्वा नारायणि नमोउस्तु ते
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12381)
- **Original**: लखज्या मेधा तुष्टिपुष्टिशान्तिसम्पत्तिवृद्धध: । एतास्तव कला: सर्वा: सर्वरूपे नमोउस्तु ते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12382)
- **Original**: दृशदृष्टस्वरूपे च तयोबीजफलप्रदे । सर्वानिर्वचनीये च॑ महामाये नमोउस्तु ते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12383)
- **Original**: शिवे शंकरसौभाग्ययुक्ते सौभाग्यदायिनि । हरि कान्‍्त॑ च सौभाग्यं देहि देवि नमोस्तु ते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12384)
- **Original**: स्तोग्रेणनेन या: स्तुत्वा समाप्तिदिवसे शिवाम्‌ । नमन्ति परया भकत्या ता लभन्ति हरि पतिम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12385)
- **Original**: इह कान्तसुखं धुक्‍्त्वा पतिं प्राप्य परात्परम्‌ । दिव्य॑ स्यन्दनमात्हा यान्त्यन्ते कृष्णसंनिधिम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12386)
- **Original**: (27। 173--184)
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12387)
- **Original**: एडड * संक्षिप्त श्रह्मवैचर्तपुराण « %ऋ%6###4# 856 88 8# 44484 ##4 44444 88% % 44 # कक कक 4 ऋ 4 कक ऋऋ कक कड़क कक कह अक कक क # श्र क कक मुखारविन्दसे राधिकाकों सम्बोधित करके क्‍ ।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12388)
- **Original**: भस्म करनेको उद्यत हुई, तब हे ईश्वरि! मेरी पार्वती बोलीं--राधे ! तुम सर्वेश्वर श्रीकृष्णको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12389)
- **Original**: प्रसन्नताके लिये तुमने स्वयं आकंर उनकी रक्षा प्राणोंसे भी बढ़कर प्रिय हो। जगदम्बिके ! तुम्हारा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12390)
- **Original**: की; फिर तुम मानुषी कैसे हो? श्रीकृष्ण प्रत्येक कल्पमें यह ब्रत लोकशिक्षाके लिये है। तुम मायासे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12391)
- **Original**: तथा जन्म-जन्ममें तुम्हारे पति हैं। जगन्मातः! मानवरूपमें प्रकट हुई हो। सुन्दरि! क्‍या तुम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12392)
- **Original**: तुमने लोकहितके लिये ही यह व्रत किया है। गोलोकनाथ, गोलोक, श्रीशैल, विरजाके तटप्रान्त,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12393)
- **Original**: अहो! श्रीदामके शापसे और भूमिका भार उतारनेके श्रीरासमण्डल तथा दिव्य मनोहर वृन्दावनको
- **Translation**: 

---

