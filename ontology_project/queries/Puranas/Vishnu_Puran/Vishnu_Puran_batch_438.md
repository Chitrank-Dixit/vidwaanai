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

### Verse 1 (Vishnu Puran 0.8741)
- **Original**: 115 ज्राह्मणा: क्षत्रिया वेश्याइशुद्राश ट्विजसत्तम
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8742)
- **Original**: युगे युगे महात्मानः समतीतास्सहस्नहाः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8743)
- **Original**: 116 बहुत्वान्नामध्षेयानां परिसंख्या कुले कुले । पौनरुक्त्याद्धि साम्याक्ष न मया परिकीर्त्तिता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8744)
- **Original**: 117 देवापि: पौरवो राजा पुरुक्षेक्षबाकुवंशज: । महायोगबलोपेता कल्ापग्रामसंश्रितो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8745)
- **Original**: 118 कृते युगे त्विहागम्य क्षत्रप्रवर्त्तको हि तो । भ्रविष्यतो मनोर्वशबीजभूतो व्यवस्थितो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8746)
- **Original**: 119 एतेन क्रमयोगेन मनुपुन्रै्वसुन्थरा । कृतत्रेताद्वापराणि युगानि त्रीणि भुज्यते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8747)
- **Original**: 120 कलौ ते बीजभूता वै केचित्तिष्ठन्ति ते मुने । यथैव देवापिपुरू साम्प्रते समधिष्ठितों
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8748)
- **Original**: 121 एष तुूद्देदातो बंझस्तवोक्तों भूभुजां मया। निखिलो गदितुं शक्यो नैष वर्षशतैरपि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8749)
- **Original**: 122 एते चानये च भूपाला यैरत्र क्षितिमण्डले । कृत ममत्व मोहान्वैर्नित्ये हेयकलेखरे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8750)
- **Original**: 123 कर्थ मपेयमचला मत्पुत्रस्य कथ्थ मही
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8751)
- **Original**: मद्गृंशस्पेति चित्तार्त्ता जग्मुरन्तमिमे नुपा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8752)
- **Original**: 124 तेभ्यः पूर्वतराश्षान्ये तेभ्यस्तेभ्यस्तथा परे । भविष्याश्षैव यास्यन्ति तेषामन्ये च बेडप्यनु
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8753)
- **Original**: 125 बिलोक्यात्मजयोद्योग॑ यात्राव्यप्राश्नराधिपान्‌ । पुष्पप्रहासइशरदि हसन्तीब बसुत्धरा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8754)
- **Original**: 126 मैत्रेय पृथिवीगीताब्छलोकांश्षात्र निबोध मे । यानाह धर्मध्वजिने जनकायासितो मुनि:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8755)
- **Original**: 127 चतुर्थ अंश 303 कल्युणका प्रभाव बढ़ेगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8756)
- **Original**: जिस दिन भगवान्‌ कृष्णचन्द्र पस्मघामको गये थे उसी दिन कलियुग उपस्थित हो गया था। अब तुम कलियुगकी नर्ष-सेख्या सुनो--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8757)
- **Original**: 613 । है द्विज ! मानवी वर्षगणनाके अनुसार कलियुग तीन स्थख साठ हजार वर्ष रहेगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8758)
- **Original**: इसके पश्चात्‌ वारह सौ दिव्य वर्षपर्यन्त कृतयुग रहेगा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8759)
- **Original**: हे द्विजश्रेष्ठ ! प्रत्येक युगमें हजारों ब्राह्मण, क्षत्रिय, वैश्य और शूद्र हात्मागण हो गये हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8760)
- **Original**: उनके बहुत अधिक संख्यामें होनेसे तथा समानता होनेके कारण कुलॉमें पुनरुक्ति हो जानेफे भयसे मैंने उन सबक्ते नाम नहीं बतलाये हैं
- **Translation**: 

---

