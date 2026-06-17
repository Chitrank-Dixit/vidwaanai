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

### Verse 1 (Vaivtpuran 12.6494)
- **Original**: ब्रह्मज्योति:स्वरूप आपका स्तवन करना चाहता उत्पन्न हुए स्वादिष्ट एवं मधुर पके हुए फल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6495)
- **Original**: हूँ, परंतु आपके अनुरूप निरूपण करनेमें मैं थे, उन्हें भी महामायाने समर्पित किया। पुनः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6496)
- **Original**: सर्वथा असमर्थ हूँ; क्योंकि आप इच्छारहित, आचमन और पान करनेके लिये अत्यन्त निर्मल
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6497)
- **Original**: सम्पूर्ण देवोंमें श्रेष्ठ, सिद्धों और योगियोंके गुरु, कर्पूर आदिसे सुवासित स्वच्छ गड्भाजल दिया।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6498)
- **Original**: सर्वस्वरूप, सर्वेश्वर, ज्ञानराशिस्वरूप, अव्यक्त, नारद! इसके बाद उसी प्रकार सुवासित उत्तम
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6499)
- **Original**: अविनाशी, नित्य, सत्य, आत्मस्वरूप, वायुके रमणीय पानके बीड़े और बायनसे परिपूर्ण सैकड़ों
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6500)
- **Original**: समान अत्यन्त निर्लेप, क्षतरहित, सबके साक्षी, स्वर्णपात्र दिये। संसार-सागरसे पार होनेके लिये परम दुर्लभ तदनन्तर मेनका, हिमालय, हिमालयके पुत्र
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6501)
- **Original**: मायारूपी नौकाके कर्णधारस्वरूप, भक्तोंपर अनुग्रह और प्रिय अमात्योंने गिरिजाके पुत्रका पूजन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6502)
- **Original**: करनेवाले, श्रेष्ठ, वरणीय, वरदाता, वरदानियोंके किया। वहाँ उपस्थित ब्रह्मा, विष्णु और शिव
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6503)
- **Original**: भी ईश्वर, सिद्ध, सिद्धिस्वरूप, सिद्धिदाता, सिद्धिके आदि सभी देवता- साधन, ध्यानसे अतिरिक्त ध्येय, ध्यानद्वारा असाध्य, 37 श्रीं हीं क्लीं गणेश्वराय ब्रह्मरूपाव चारवे।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6504)
- **Original**: धार्मिक, धर्मस्वरूप, धर्मके ज्ञाता, धर्म और सर्वसिद्धिप्रदेशाय विध्लेशाय नमो नमः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6505)
- **Original**: अधर्मका फल प्रदान करनेवाले, संसार-वृक्षके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6506)
- **Original**: + गणपतिखण्ड + क2के है 8030 बीज, अंकुर और उसके आश्रय, स्त्री-पुरुष और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6507)
- **Original**: अब मुझे जन्म-मृत्युके चक्रसे छुड़ानेवाले कवचके नपुंसकके स्वरूपमें विराजमान तथा इनकी इन्द्रियोंसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6508)
- **Original**: सुननेकी इच्छा है। परे, सबके आदि, अग्रपूज्य, सर्वपूज्य, गुणके श्रीनारायणने कहा--नारद ! उस देवसभाके सागर, स्वेच्छासे सगुण ब्रह्म तथा स्वेच्छासे ही
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6509)
- **Original**: मध्य जब गणेशकी पूजा समाप्त हुई, तब शनैश्वरने निर्गुण ब्रह्मका रूप धारण करनेवाले, स्वयं प्रकृतिरूप
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6510)
- **Original**: सबके तारक जगदुरु विष्णुसे कहा। और प्रकृतिसे परे प्राकृतरूप हैं। शेष अपने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6511)
- **Original**: । शनैश्वर बोले--वेदवेत्ताओंमें श्रेष्ठ भगवन्‌! सहस्रों मुखोंसे भी आपकी स्तुति करनेमें असमर्थ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6512)
- **Original**: सम्पूर्ण दुःखोंके विनाश और दुःखकोी पूर्णतया हैं। आपके स्तवनमें न पञ्ममुख महेश्वर समर्थ हैं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6513)
- **Original**: शान्तिके लिये विप्नहन्ता गणेशके कवचका वर्णन न चतुर्मुख ब्रह्मा ही; न सरस्वतीकी शक्ति है और
- **Translation**: 

---

