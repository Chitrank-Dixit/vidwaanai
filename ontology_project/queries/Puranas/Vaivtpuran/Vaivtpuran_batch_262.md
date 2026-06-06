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

### Verse 1 (Vaivtpuran 13.11382)
- **Original**: इन्द्रियोंके अधिदेवता, आवासस्थान और सर्वेन्द्रिय- उस तेजके भीतर अत्यन्त मनोरम रूप था, दो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11383)
- **Original**: स्वरूप हैं; उन विराट्‌ परमेश्वरकों मैं नमस्कार भुजाएँ, हाथमें मुरली और पीताम्बरभूषित श्रीअज्गज
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11384)
- **Original**: करता हूँ। जो वेद, वेदेंकि जनक तथा सर्ववेदाड़ुस्वरूप कानोंके मूलभागमें पहने गये मकराकृति कुण्डल
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11385)
- **Original**: हैं; उन सर्वमन्त्रमय परमेश्वरको मैं नमस्कार करता अपनी उज्वल आभा बिखेर रहे थे। प्रसन्न हूँ।जो सारसे सारतर द्रव्य, अपूर्व, अनिर्वचनीय, मुखारविन्दपर मन्द हास्यकी छटा छा रही थी।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11386)
- **Original**: स्वतन्त्र और अस्वतन्त्र हैं; उन यशोदानन्दनका मैं भगवान्‌ भक्तपर अनुग्रह करनेके लिये कातर जान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11387)
- **Original**: भजन करता हूँ। जो सम्पूर्ण शरीरोंमें शान्तरूपसे पड़ते थे। ब्रह्माजीने ब्रह्मरन्ध्रमें जिस रूपको देखा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11388)
- **Original**: विद्यमान हैं, किसीके दृष्टिपथमें नहीं आते, तर्कके और हृदयकमलमें जिसकी झाँकी की, वही रूप
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11389)
- **Original**: अविषय हैं, ध्यानसे वशमें होनेवाले नहीं हैं तथा बाहर भी दृष्टिगोचर हुआ। वह परम आश्चर्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11390)
- **Original**: नित्य विद्यमान, हैं; उन योगीद्धोंक भी गुरु देखकर उन्होंने उन परमेश्वरकी स्तुति की। मुने !
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11391)
- **Original**: गोविन्दका मैं भजन करता हूँ। जो रासमण्डलके पूर्वकालमें एकार्णवके जलमें शयन करनेवाले
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11392)
- **Original**: मध्यभागमें विराजमान होते हैं, रासोल्लासके लिये श्रीहरिने ब्रह्माजीको जिस स्तोत्रका उपदेश दिया
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11393)
- **Original**: सदा उत्सुक रहते हैं तथा गोपाड्नाएँ सदा जिनकी था, उसीके द्वारा विधाताने भक्तिभावसे मस्तक
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11394)
- **Original**: सेवा करती हैं; उन राधावल्लभकों मैं नमस्कार करता झुकाकर उन परमेश्वरका विधिवत्‌ स्तवन किया।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11395)
- **Original**: हूँ। जो साधु पुरुषोंकी दृष्टिमें सदैव सत्‌ और ब्रह्माजी बोले--जो सर्वस्वरूप, सर्वेश्वर,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11396)
- **Original**: असाधु पुरुषोंके मतमें सदा ही असत्‌ हैं, भगवान्‌ समस्त कारणोंके भी कारण तथा सबके लिये
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11397)
- **Original**: शिव जिनकी सेवा करते हैं; उन योगसाध्य अनिर्वचनीय हैं; उन कल्याणस्वरूप श्रीकृष्णको
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11398)
- **Original**: योगीश्वर श्रीहरिकों मैं प्रणाम करता हूँ। जो मैं नमस्कार करता हूँ। जिनका श्रीविग्रह नवीन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11399)
- **Original**: मन्त्रबीज, मन्त्रराज, मन्त्रदाता, फलदाता, फलरूप, मेघमालाके समान श्याम एवं सुन्दर है, जो सम्पूर्ण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11400)
- **Original**: मन्त्रसिद्धिस्वरूप तथा परात्पर हैं; उन श्रीकृष्णको जीवोंमें स्थित रहकर भी उनसे लिप्त नहों होते,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11401)
- **Original**: मैं नमस्कार करता हूँ। जो सुख-दुःख, सुखद- जो साक्षीस्वरूप हैं, स्वात्माराम, पूर्णकाम, विश्वव्यापी,
- **Translation**: 

---

