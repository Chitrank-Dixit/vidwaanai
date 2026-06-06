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

### Verse 1 (Vaivtpuran 36.7942)
- **Original**: करे। पूर्वमें 'महाकाली' और अग्निकोणमें लिया। अब मैं कवच सुनना चाहता हूँ, वह
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.7943)
- **Original**: “रक्तदन्तिका' रक्षा करें। दक्षिणमें चामुण्डा रक्षा मुझसे वर्णन कीजिये। करें। नैक्रत्यकोणमें "कालिका' रक्षा करें। पश्चिममें श्रीनारायण बोले--विप्रेन्द्र! पूर्वकालमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.7944)
- **Original**: 'श्यामा' रक्षा करें। वायव्यकोणमें “चण्डिका', त्रिपुर-वधके भयंकर अवसरपर शिवकी विजयके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.7945)
- **Original**: उत्तरमें 'विकटास्था' और ईशानकोणमें ' अट्टहासिनी ' लिये नारायणने कृपा करके शिवको जो परम [ रक्षा करें। ऊर्ध्वभागमें 'लोलजिद्ना' रक्षा करें। अद्भुत कबच प्रदान किया था, उसका वर्णन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.7946)
- **Original**: अधोभागमें सदा 'आधद्यामाया' रक्षा करें। जल, करता हूँ, सुनो। मुने! वह कवच अत्यन्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.7947)
- **Original**: स्थल और आन्तरिक्षमें सदा 'विश्वप्रस्‌' रक्षा करें। गोपनीयोंसे भी गोपनीय, तत्त्वस्वरूप तथा सम्पूर्ण. वत्स! यह कवच समस्त मन्त्रसमूहका मन्त्रसमुदायका मूर्तिमान्‌ स्वरूप है। उसीको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.7948)
- **Original**: मूर्तरूप, सम्पूर्ण कवचोंका सारभूत और उत्कृष्टसे पूर्वकालमें शिवजीने दुर्वासाकों दिया था और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.7949)
- **Original**: भी उत्कृष्टतर है; इसे मैंने तुम्हें बतला दिया। दुर्वासाने महामनस्वी राजा सुचन्द्रको प्रदान
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.7950)
- **Original**: इसी कवचको कृपासे राजा सुचन्द्र सातों ट्वीपोंके किया था। अधिपति हो गये थे। इसी कवचके प्रभावसे '37 हुँ श्रीं क्‍्लीं कालिकाय॑ै स्वाहा' मेरे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.7951)
- **Original**: पृथ्वीपति मान्धाता सप्तद्वीपवती पृथ्वीके अधिपति मस्तककी रक्षा करे। 'क्लीं' कपालकी तथा 'ह्लीं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.7952)
- **Original**: हुए थे। इसीके बलसे प्रचेता और लोमश सिद्ध हीं हीं! नेत्रोंकी रक्षा करे। '30 हीं त्रिलोचने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.7953)
- **Original**: हुए थे तथा इसीके बलसे सौभरि और स्वाहा' सदा मेरी नासिकाकी रक्षा करे। “क्री
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.7954)
- **Original**: पिप्पलायन योगियोंमें श्रेष्ठ कहलाये। जिसे यह कालिके रक्ष रक्ष स्वाहा' सदा दाँतोंकी रक्षा करे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.7955)
- **Original**: कवच सिद्ध हो जाता है, वह समस्त सिद्धियोंका “डह्लीं भद्रकालिके स्वाहा' मेरे दोनों ओठोंकी रक्षा [स्वामी बन जाता है। सभी महादान, तपस्या करे। '» हीं हीं क्लीं कालिकायै स्वाहा' सदा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.7956)
- **Original**: और ब्रत इस कवचकी सोलहवीं कलाकी भी कण्ठकी रक्षा करे। '3» ह्रीं कालिकाय॑ स्वाहा'
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.7957)
- **Original**: बराबरी नहीं कर सकते, यह निश्चित है। जो सदा दोनों कानोंकी रक्षा करें। ' 30 क्वीं क्री क्‍्लीं
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.7958)
- **Original**: इस कवचको जाने बिना जगज्जननी कालीका काल्यै स्वाहा” सदा मेरे कंधोंकी रक्षा करे। '37
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.7959)
- **Original**: भजन करता है, उसके लिये एक करोड़ जप क्री भद्रकाल्यै स्वाहा' सदा मेरे वक्ष:स्थलकी रक्षा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.7960)
- **Original**: करनेपर भी यह मन्त्र सिद्धिदायक नहीं होता। करे। '37 क्रीं कालिकायै स्वाहा' सदा मेरी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.7961)
- **Original**: (अध्याय 37)
- **Translation**: 

---

