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

### Verse 1 (Vishnu Puran 0.8901)
- **Original**: 390 श्रीविष्णुपुराण ( अ9 1 त्वमव्यक्तमनिर्देशयमचिन्त्यानामवर्णवत्‌.। आप अव्यक्त, अनिर्वाच्य, अचिन्त्य, नामवर्णसे अपाणिपादरूर् ञ्व शुद्ध निर्य परात्यरम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8902)
- **Original**: रहित, हाथ-पाँव तथा रूपसे हीन, शुद्ध, सनातन और अपदालों अल उत > ग्रहीता ...._ल्व॑ वेत्सि सर्व न च सर्ववेद्य:ः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8903)
- **Original**: 41 अणोरणीयांसमसत्स्वरूप॑ 7 कह्वे पत्यतोज्ञाननिवृत्तिस्ग॒या । धीरस्य धीरस्य बिभर्त्ति नान्‍्य- .. देरेण्यरूपात्परत: .परात्मन्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8904)
- **Original**: 42 उसमे, जकत: परालात
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8905)
- **Original**: 4 : परस्तात्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8906)
- **Original**: 43 सकथ्त ददासि । सा स धातः पा पर जे पर्ट त्वे धातः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8907)
- **Original**: 44 यथाभिरेको :4::-+ न सन तथा भवान्सर्वगतेकरूपी एके ल्वमग्न्य परम॑ पद य- त्पश्यन्ति त्वां सूरयो ज्ञानवृश्यम्‌ । त्वत्तो नान्यत्किश्निदस्ति स्वरूप यद्वा भूत यज्न भव्य परात्पन्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8908)
- **Original**: 486 व्यक्ताव्यक्तस्वरूपस्त॑ समष्टिव्यष्टिरूपवान्‌ सर्वज्ञस्सवचित्सर्वशक्तिज्ञानवलर्डमान्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8909)
- **Original**: 47 अन्यूनश्वाप्यवृद्धिश्व स्वाधीनो नादिमान्वशी । क्मतन्द्राभवक्रोधकामादिभिरसंयुत:...
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8910)
- **Original**: 48 निरवह्य: परः प्राप्तेनिरिधिष्ठो5क्षर: क्रमः । सर्वेश्चरः पराघारों धारा धामात्मकोउक्षयः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8911)
- **Original**: 45 परसे भी पर हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8912)
- **Original**: आप कर्णहीन होकर भी सुनते हैं, नेत्रहोन होकर भी देखते हैं, एक होकर भी अनेक रूपॉमें प्रकट होते हैं, हस्तपादादिसे रहित होकर भी बड़े बेगशाली और ग्रहण करनेवाएे हैं तथा सबके अवेचय होकर भी सबक्तों जाननेवाले हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8913)
- **Original**: हे परात्मत्‌ ! जिस धीोर पुरुषकी युद्धि आपके श्रेष्ठतम रूपसे पृथक्‌ और कुछ भी नहीं देखती, आपके अणुसे भी अणु और दृश्य-स्वरूपको देखनेबाले उस पुरुषकी आत्यन्तिक अज्ञाननिवत्ति हो जाती है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8914)
- **Original**: आप विश्वके केन्द्र तथा जो कुछ भूत, भविष्यत्‌ और अपुसे भी अणु है वह सत्र आप प्रकृतिसे परे एकमात्र परमपुरुष ही हैं।43
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8915)
- **Original**: आप ही चार प्रकारका अप्ि होकर संसारकों तेज और विधृति दान करते हैं। हे अनन्तमूर्ते ! आपके नेत्र सब्र ओर हैं। हे घात: ! आप ही [ त्रिविक्रमाखतारमें
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8916)
- **Original**: तीनों ल्लेकमें अपने तीन पग रखते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8917)
- **Original**: 44। हे ईश! जिस प्रकार एक ही होता है उसी प्रकार सर्वशतरूप एक आप ही अनन्त रूप धारण कर लेते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8918)
- **Original**: एकमात्र जो श्रेष्ठ परमपद है; खह आप ही हैं, ज्ञाती पुरुष ज्ञानट्ष्टिसे देखे जाने योग्य आपको ही देखा करते हैं। हे परात्मन्‌ ! भूत और भविष्यत्‌ जो कुछ स्वरूप है वह आपसे अतिरिक्त और कुछ भी नहीं है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8919)
- **Original**: आप व्यक्त और अव्यक्तस्वरूप हैं, समष्टे और व्यक्तिरूप हैं तथा आप ही सर्वज्ञ, सर्वसाक्षी, सर्वशक्तिमान्‌ एवं सम्पूर्ण ज्ञान, बल और ऐश्वर्यसे युक्त हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8920)
- **Original**: आप हास और वदिसे रहित, स्वाधीन, अतादि और जितेन्द्रिय हैं तथा आपके अन्दर श्रम, तन्द्रा, भय, क्रोध और काम आदि नहीं हैं
- **Translation**: 

---

