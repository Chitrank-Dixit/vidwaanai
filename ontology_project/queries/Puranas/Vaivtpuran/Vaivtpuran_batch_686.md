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

### Verse 1 (Vaivtpuran 113.19027)
- **Original**: त्वदंशा: प्रतिविश्वेषु. ब्रह्मविष्णुशिवात्मका:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 113.19028)
- **Original**: सर्वेषामपि विश्वेषामाश्रयों यो महान्‌ विराट ।स शेते च जले योगाद्‌ विश्वेशों गोकुले यथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 113.19029)
- **Original**: स॒ एव बासुर्भगवान्‌ तस्य देवों भवान्‌ परः। बासुदेव इति ख्यात: पुराविद्धि: प्रकीर्तितः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 115.617)
- **Original**: करे » संक्षिप्त ब्रह्मवैवर्तपुराण * ।48 ।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 115.618)
- **Original**: 9998 62048 4 24 ]84
- **Translation**: 

---

### Verse 6 (Vaivtpuran 115.619)
- **Original**: 6000 4 44 83 43434 0344344444»><ंयं< - 7]]]78872544/40004 2
- **Translation**: 

---

### Verse 7 (Vaivtpuran 115.620)
- **Original**: 6 66 80/ 2 .
- **Translation**: 

---

### Verse 8 (Vaivtpuran 115.621)
- **Original**: मुनिने भगवान्‌ सूर्यको प्रणाम किया और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 115.622)
- **Original**: गुरुके संसर्ग-दोषसे भी जो ब्राह्मण श्रीहरिसे तपस्याके क्षीण होनेके भयसे भयभीत हो
- **Translation**: 

---

### Verse 10 (Vaivtpuran 115.623)
- **Original**: विमुख हो जाते हैं, वे जीते-जी ही मुर्देके समान श्रीहरिकी सेवामें मन लगाकर गद्जातटको प्रस्थान
- **Translation**: 

---

### Verse 11 (Vaivtpuran 115.624)
- **Original**: हैं। बह कैसा गुरु, कैसा पिता, कैसा पुत्र, कैसा किया। तत्पश्चात्‌ भगवान्‌ सूर्य दोनों पुत्रोंक साथ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 115.625)
- **Original**: मित्र, कैसा राजा तथा कैसा बन्धु है, जो श्रीहरिके अपने धामको चले गये। भजनकी बुद्धि (सलाह) नहीं देता? विप्रवर! विद्वान्‌ हो या विद्याहीन, जो ब्राह्मण प्रतिदिन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 115.626)
- **Original**: अवैष्णव ब्राह्मणसे वैष्णव चाण्डाल श्रेष्ठ है; संध्यावन्दन करके पवित्र होता है, वही भगवान्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 115.627)
- **Original**: क्योंकि वह बैष्णव चाण्डाल अपने बन्धुगणोंसहित विष्णुके समान बन्दनीय है। यदि वह भगवानूसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 115.628)
- **Original**: संसार-बन्धनसे मुक्त हो जाता है और वह विमुख हो तो आदरका पात्र नहीं है। जो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 115.629)
- **Original**: अवैष्णव ब्राह्मण नरकमें पड़ता है*। ब्रह्मन्‌! जो एकादशीको भोजन नहीं करता और प्रतिदिन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 115.630)
- **Original**: प्रतिदिन संध्या-वन्दन नहीं करता अथवा भगवान्‌ श्रीकृष्णकी आराधना करता है, उस ब्नाह्मणका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 115.631)
- **Original**: विष्णुसे विमुख रहता है, वह सदा अपवित्र माना चरणोदक पाकर कोई भी स्थान निश्चय ही तीर्थ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 115.632)
- **Original**: गया है। जैसे विषहीन सर्पको सर्पाभासमात्र कहा बन जाता है। जो नित्यप्रति भगवान्‌को भोग
- **Translation**: 

---

### Verse 20 (Vaivtpuran 115.633)
- **Original**: गया है, उसी तरह संध्याकर्म तथा भगवद्धक्तिसे लगाकर उनका उच्छिष्ट भोजन करता है तथा
- **Translation**: 

---

