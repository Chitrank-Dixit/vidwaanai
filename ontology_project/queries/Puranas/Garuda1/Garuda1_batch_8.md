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

### Verse 1 (Garuda1 0.141)
- **Original**: शीरहा च॒ बाहद्दीरी वन्दितः परमेश्चर:। आत्मा च परमात्मा च॒ प्रत्यगात्मा वियत्पर:
- **Translation**: 

---

### Verse 2 (Garuda1 0.142)
- **Original**: 'पदानाथः पद्मतनिधि: पणाहस्तो गदाथर: ( धराथर: )। परम: परभूतश पुरुषोत्तम ईश्वर:
- **Translation**: 

---

### Verse 3 (Garuda1 0.143)
- **Original**: पशजकुः पुण्डरीक:ः पशमालाधरः: प्रिय:। भक्षाक्ष, पद्गर्भक्ष पर्जन्यः पदासंस्थित:
- **Translation**: 

---

### Verse 4 (Garuda1 0.144)
- **Original**: अपार: परमार्थक्ष॒ पराणां ज्ञ॒ परः प्रभु:। पण्डित:ः पण्डितेडबश पवित्र: पापपर्दक:
- **Translation**: 

---

### Verse 5 (Garuda1 0.145)
- **Original**: शुद्ध: प्रकाशरूपश्ष॒ पत्ित्र: परिरक्षक:। पिपासावर्जित: पाद्य:ः पुरुष: प्रकृतिस्तशा
- **Translation**: 

---

### Verse 6 (Garuda1 0.146)
- **Original**: प्रधान॑ पृथिवीपश्व॑ पद्मनाभ: प्रियप्रदः ( प्रियंजद: )। सर्वेश: सर्वग: सर्य: सर्ववित्‌ सर्द: सुरः ( परः )
- **Translation**: 

---

### Verse 7 (Garuda1 0.147)
- **Original**: सर्वस्थ जगतो थाम सर्वदर्शो चर सर्वभृत्‌। सर्वॉनुग्रहकृद्देव: सर्वंभूतदृदि स्थित:
- **Translation**: 

---

### Verse 8 (Garuda1 0.148)
- **Original**: सर्वपूस्यश्ष सर्वाद्य: सर्वदेवनमस्कृत:
- **Translation**: 

---

### Verse 9 (Garuda1 0.149)
- **Original**: सर्वस्थ जगतो मूल सकलो निष्कलोउनल:।
- **Translation**: 

---

### Verse 10 (Garuda1 0.150)
- **Original**: सर्वगोप्ता सर्वनिष्ठ: सर्वकारणकारणम्‌। सर्वध्येय: सर्वमित्र: सर्वदेवस्वकृपधूक्‌
- **Translation**: 

---

### Verse 11 (Garuda1 0.151)
- **Original**: सर्वाध्यक्ष: सुगाध्यक्ष: सुरासुरनमस्कृत:। 1, “विज्ञान '- परमार्थज्ञान
- **Translation**: 

---

### Verse 12 (Garuda1 0.152)
- **Original**: 2, ' ज्ञान'- स्यावहारिक ज्ञान 3, युभुक्षा व पिपासा थ प्राणस्य ( शब्दकल्पद्रम)
- **Translation**: 

---

### Verse 13 (Garuda1 0.153)
- **Original**: ड. 'दृएरूप' का तात्पर्य यह है-- समस्त प्रपक्ष दरष्टा, दृश्य एवं दृष्टि-- इन तौनॉमें अन्तर्हित है। परमेश्वर विष्णु हो द्र्टा हैं, वे हो दृश्य हैं, दृष्टि भी वे हो हैं; यह दृष्टि ही 'दृग्‌' शब्दसे कहो जाती है।
- **Translation**: 

---

### Verse 14 (Garuda1 0.154)
- **Original**: 36 * पुराण गारुड़े वक्ष्ये साईं विष्णुकथाअयम्‌ * [ संक्षिप्त गरड़पुराणाडू दुष्टानां चासुराणां चर सर्वदा थातकोउन्तक:ः
- **Translation**: 

---

### Verse 15 (Garuda1 0.155)
- **Original**: शरंणं जगतश्ैय श्रेय: क्षेमस्तश्चैव अ। शुभकृच्छोभन: सौध्य: सत्य: सत्यपराक्रम:
- **Translation**: 

---

### Verse 16 (Garuda1 0.156)
- **Original**: सत्यस्थ: सत्यसड्डुस्पः सत्यवित्‌ सत्य( त्प्र)दस्तथा। धर्मों धर्मी च् कर्मी ज्ञ॒ सर्वकर्मविवर्जित:
- **Translation**: 

---

### Verse 17 (Garuda1 0.157)
- **Original**: कर्मकर्ता ज्ञ कर्यत क्रिया कार्य तथैव च। अ्रीपतिनुपति:. श्रीपातू सर्वस्य पतिरूरजित:
- **Translation**: 

---

### Verse 18 (Garuda1 0.158)
- **Original**: सदेवानां. पतिश्लैव वृष्णीनां. पक्तिड़ित:। पत्िहिरण्यगर्धस्य त्रिपुरालपतिस्तथा
- **Translation**: 

---

### Verse 19 (Garuda1 0.159)
- **Original**: पशूत्रां ख पति: प्रायों बसूनां पतिरेव ज्ञा 'पतिराखण्डलस्यैल वरहूणस्य परतिस्तधा
- **Translation**: 

---

### Verse 20 (Garuda1 0.160)
- **Original**: खनस्पतीना जा पतिरभिलस्थ पतिस्तथा। अनलस्य पतिश्षेजय यपस्य पतिरेव च
- **Translation**: 

---

