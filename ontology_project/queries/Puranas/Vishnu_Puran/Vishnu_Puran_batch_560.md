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

### Verse 1 (Vishnu Puran 0.11181)
- **Original**: सम्णणन्‍नन है अमन इ्ति श्रीविष्णुपुराणे पञ्चमेंजज्ञे ब्रिशोड्ध्याय:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11182)
- **Original**: जज 5 औ न
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11183)
- **Original**: श्रीविष्णुपुराण [ अ« 36 इकतीसवाँ अध्याय भगबानका द्वारकापुरीमें लौटना और सोलह हजार एक सौ कन्याओंसे विवाह करना श्रीफ़राशर उवाच संस्तुतो भगवानित्थ देवराजेन केशवः । प्रहस्थ॒ भावगश्मीरमुवाचेन्द्र द्विजोत्तम
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11184)
- **Original**: 91 श्रीकृष्ण उजच देवराजो भवानिन्द्रो बयं मर्त्या जगत्पते । क्षन्तव्य॑ भकतैवेदमपराध॑ कृत मम
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11185)
- **Original**: 2 पारिजाततरुक्षायं नीयतामुचितास्पदम्‌ । गृहीतो5यं मयां शक्र सत्यावजनकारणात्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11186)
- **Original**: 3 बज चेद गृहाण त्व॑ यदत्र प्रहिते त्वया। तबवैवैतठाहरणं शक्र. वैरिविदारणम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11187)
- **Original**: 4 इन्र उवाच विमोहयसि मामीश मत्यों5हमिति कि वदन्‌ । जानीमस्त्वां भगवतो न तु सूक्ष्मविदों बयम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11188)
- **Original**: 5 योउसि सो5सि जगत्व्राणप्रवृत्तो नाथ संस्थित: । जगतइदइल्यनिष्कप॑. करोष्यसुरसूदन
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11189)
- **Original**: 6 नीयतां पारिजातो5यं कृष्ण द्वारवर्ती पुरीम्‌। मर्व्यलोके त्वया त्यक्ते नाय॑ संस्थास्यते भुवि
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11190)
- **Original**: 7 देव देव जगन्नाथ कृष्ण विष्णों महाभुज । शद्भुचक्रगदापाणे क्षमस्वैतद्व्यतिक्रमम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11191)
- **Original**: 8 औपराशर उवाच तथेत्युक्त्वा च॒ देवेद्रमाजगाम भुवं हरि: । प्रसक्तैः सिद्धगन्धर्व: स्तूयमान: सुर्षिभि:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11192)
- **Original**: 9 ततइद्द्भुमुपाध्याय द्वारकोपरि संस्थितः । हर्षमुत्पादयामास द्वारकावासिनां द्विज
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11193)
- **Original**: 10 अवतीर्याथ गरुडात्सत्यभामासहायबान्‌ । निष्कुटे स्थापयामास पारिजातं महातरुम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11194)
- **Original**: 11 यमभ्येत्य जनस्सवों जाति स्मरति पौर्विकीम्‌ । बास्यते यस्य पुष्पोत्थगश्धेनोर्बी त्रियोजनम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11195)
- **Original**: 12 श्रीपराझरजी खोल्छे--हे ट्विजोत्तम ! इद्धने जब इस प्रकार स्तुति की तो भगवान्‌ कृष्णचन्द्र गम्भीर भावसे हंसते हुए इस प्रकार बोले--
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11196)
- **Original**: श्रीकृष्णजी बोले--हे जगत्पते ! आप देवराज इन्द्र हैं और हम मरणधघर्मा मनुष्य हैं। हमने आपका जो अपराध किया है उसे आप क्षमा करें
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11197)
- **Original**: मैंने जो यह पारिजात-वृक्ष लिया था इसे इसके योग्य स्थान (नन्दनवन) को ले जाइये। हे शक्र ! मैंने तो इसे सत्यभामाके वकनेसे ही ले लिया था
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11198)
- **Original**: और आपने जो वद्र फेंका था उसे भी ले लीजिये, क्योंकि हे शक्र ! यह अषुओँको नष्ट करनेबात्म छास्ध आपहोका है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11199)
- **Original**: इन्द्र बोले--हे ईइ ! “मैं मनुष्य है" ऐसा कहकर मुझे क्यों मोहित करते हैं ? हे भगवन्‌ ! मैं तो आपके इस सगुण स्वरूपको ही जानता हूँ, हम आपके सूक्ष्म स्वरूपको जाननेवाले नहीं हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11200)
- **Original**: हे नाथ ! आप जो हैं वही है,
- **Translation**: 

---

