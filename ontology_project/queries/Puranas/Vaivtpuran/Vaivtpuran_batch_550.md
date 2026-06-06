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

### Verse 1 (Vaivtpuran 38.8067)
- **Original**: “कुबेरमाता' और ईशानकोणमें 'ईश्वरी' सदा- कवचके प्रजापति ऋषि हैं। गायत्री छन्द है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 38.8068)
- **Original**: सर्वदा रक्षा करें। ऊर्ध्वभागमें 'नारायणी' रक्षा दुर्गतिनाशिनी दुर्गा देवी हैं और ब्रह्माण्डविजयके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 38.8069)
- **Original**: करें और अधोभागमें सदा 'अम्बिका' रक्षा करें। लिये इसका विनियोग किया जाता है। यह परम
- **Translation**: 

---

### Verse 4 (Vaivtpuran 38.8070)
- **Original**: जाग्रत॒कालमें ज्ञानप्रदा रक्षा करें और सोते समय अद्भुत कबच महापुरुषोंका पुण्यतीर्थ है। [निद्रा सदा रक्षा करें। इति ते कथित वत्स सर्वमन्त्रौषविग्रहम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 38.8071)
- **Original**: सर्वेश्चर्ययरद नाम कव्च॑ परमाद्धुतम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 38.8072)
- **Original**: सुवर्णपर्वत॑ दत्वा मेरुतुल्य॑ ट्विजातये । यत्‌ फल॑ लभते धर्मी कवचेन ततो5घिकम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 38.8073)
- **Original**: गुरुमभ्यर्य विधिवत्‌_ कबच॑ धारयेतु यः:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 38.8074)
- **Original**: कण्ठे वा दक्षिणे बाहौँ स श्रीमान्‌ प्रतिजन्मनि
- **Translation**: 

---

### Verse 9 (Vaivtpuran 38.8075)
- **Original**: अस्ति लक्ष्मीगृहे तस्प निश्षला शतपूरुषम्‌ । देवेन्द्रश्वासुरेन्द्रैठ सोउवध्यो निश्चित भवेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 38.8076)
- **Original**: स॒ सर्वपुण्यवात्‌ धौमान्‌ सर्वयज्ञेपु दीक्षित:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 38.8077)
- **Original**: स ख्लात: सर्वतीर्थेषु यस्येद॑ कवच गले
- **Translation**: 

---

### Verse 12 (Vaivtpuran 38.8078)
- **Original**: यसमै कस्से न॒ दातव्य॑ लोभमोहभयैरपि । गुरुभक्तायः शिष्याय. शरणाय प्रकाशयेतू
- **Translation**: 

---

### Verse 13 (Vaivtpuran 38.8079)
- **Original**: इद॑_ कवचमज्ञात्वा जपेल्लक्ष्म._ जगत्प्रसूमू। कोटिसंख्यप्रजप्तोतपि न मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 38.8080)
- **Original**: (गणपतिखण्ड 38। 57-82)
- **Translation**: 

---

### Verse 15 (Vaivtpuran 38.18220)
- **Original**: <02 + संक्षिप्त ब्रह्मवैयर्तुपुराण « महालक्ष्म्या मन्त्रों ध्यानं च महालक्ष्म्याश्न पन्त्रं च श्रृणु त॑ कथयामि ते । 30 श्री कमलवासिन्य स्वाहेति परमाद्भुतम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 38.18221)
- **Original**: ध्यानं चर सामवेदोक्त श्रूणु पूजाविधिं मुने । दत्त तस्मै कुमारेण पुष्कराक्षाय भधीमते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 38.18222)
- **Original**: सहस््रदलपचास्थां.. पदानाभप्रियां. सतीम्‌ । पौद्मालयां पंद्यवक्त्रां पौद्चपत्राभलोचनाम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 38.18223)
- **Original**: पद्दापुष्पप्रियां पद्मपुष्पतल्पविशायिनीम्‌ । पद्चिनीं पद्महस्तां . च पद्ममालाविभूषिताम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 38.18224)
- **Original**: पद्मभूषणभूषाद्यां पद्मशोभाविवर्थिनीम्‌ू । पद्यकानन पश्यन्तीं सस्मितां तां भजे मुदा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 38.18225)
- **Original**: डति श्रीब्रह्मवैवर्ते मन्त्रसाहितं महालक्ष्प्या ध्यान सम्पूर्णम्‌। (गणपतिखण्ड 38। 45--49) #/*हरियलिय 28-00 देवा ऊचु: च. कोपादिपरिवर्जिते
- **Translation**: 

---

