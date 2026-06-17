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

### Verse 1 (Vaivtpuran 23.2182)
- **Original**: इृदयमें सदा मेरी भक्ति बनी रहेगी। तुम मेरे परंतु मैं जबतक जीऊँ, तबतक आपमें मेरी अटल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2183)
- **Original**: परम सुन्दर स्व॒रूपको ध्यानके द्वारा निरन्तर देख श्रद्धा बनी रहे। इस लोकमें जो पुरुष आपका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2184)
- **Original**: सकोगे, यह निश्चित है। तुम्हारी कमनीया माता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2185)
- **Original**: 100 « संक्षिम स्रहॉ्वेलेतपुराणा « श्र %%%%$%$%$%$%%$#%$%%%%%%%क$%%%$%%$%%क%$%%%$%%%%%$%ऋ%क$$%$%%5%%$%%%$%क%%%$%$%%%$%%%%%$%%%%%%$%$%54%% कक्ष मेरे बक्ष:स्थलपर विराजमान रहेगी। उसकी भी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2186)
- **Original**: करनेपर भी वे पद्मजन्मा ब्रह्मा पद्मनाभकी नाभिसे झाँकी तुम प्राप्त कर सकोगे। वत्स! अब मैं अपने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.2187)
- **Original**: उत्पन्न हुए कमलदण्डके अन्ततक जानेमें सफल गोलोकमें जाता हूँ। तुम यहीं ठहरो। न हो सके। तब उनके मनमें चिन्ता घिर आयी। इस प्रकार उस बालकसे कहकर भगवान्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.2188)
- **Original**: वे पुनः अपने स्थानपर आकर भगवान्‌ श्रीकृष्णके श्रीकृष्ण अन्तर्धान हो गये और तत्काल वहाँ
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.2189)
- **Original**: [चरण-कमलका ध्यान करने लगे। उस स्ितिमें पहुँचकर उन्होंने सृष्टिकी व्यवस्था करनेबाले
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.2190)
- **Original**: उन्हें दिव्य दृश्टिके द्वारा भ्रुद्र बिराट्‌ पुरुषके दर्शन ब्रह्माोको तथा संहारकार्यमें कुशल रुद्रको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.2191)
- **Original**: प्राप्त हुए। ब्रह्माण्ड-गोलकके भीतर जलमय आज्ञा दी। शब्यापर वे पुरुष शयन कर रहे थे। फिर जिनके भगवान्‌ श्रीकृष्णने कहा--वत्स! सृष्टि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.2192)
- **Original**: रोमकूपमें बह ब्रह्माण्ड था, उन महाविराट्‌ पुरुषके रचनेके लिये जाओ। विधे! मेरी बात सुनो, तथा उनके भी परम प्रभु भगवान्‌ श्रीकृष्णके भी महाविराट्के एक रोमकूपमें स्थित क्षुद्र विराट्‌ दर्शन हुए। साथ हों गोपों और गोपियोंसे पुरुषके नाभिकमलसे प्रकट होओ। फिर रुद्रको सुशोभित गोलोकधामका भी दर्शन हुआ। फिर संकेत करके कहा-'वत्स महादेव! जाओ।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.2193)
- **Original**: तो उन्होंने श्रीकृष्णजी स्तुति की और उनसे महाभाग! अपने अंशसे ब्रह्मके ललाटसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.2194)
- **Original**: वरदान पाकर सृष्टिका कार्य आरम्भ कर दिया। प्रकट हो जाओ और स्वयं भी दीर्घकालतक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.2195)
- **Original**: सर्वप्रथम ब्रह्मासे सनकादि चार मानसपुत्र हुए। तपस्या करो।'
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.2196)
- **Original**: फिर उनके ललाटसे शिवके अंशभूत ग्यारह रुद्र नारद! जगत्पति भगवान्‌ श्रीकृष्ण यों कहकर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.2197)
- **Original**: प्रकट हुए। फिर श्षुद्र विराट्‌ पुरुषके वामभागसे चुप हो गये। तब ब्रह्म और कल्याणकारी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.2198)
- **Original**: जगत्‌की रक्षाके व्यवस्थापक चार भुजाधारी शिव-दोनों महानुभाव उन्हें प्रणाम करके बिदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.2199)
- **Original**: भगवान्‌ श्रीविष्णु प्रकट हुए। बे श्वेतद्वीपमें हो गये। महाविराट्‌ पुरुषके रोमकृपमें जो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2200)
- **Original**: निवास करने लगे। क्षुद्र विराट्‌ पुरुषके नाभिकमलमें ब्रह्माण्ड-गोलकका जल है, उसमें बे महाविराट्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2201)
- **Original**: प्रकट हुए ब्रह्माने विश्वकी रचना की। स्वर्ग, मर्त्य पुरुष अपने अंशसे क्षुद्र विराट्‌ पुरुष हो गये,
- **Translation**: 

---

