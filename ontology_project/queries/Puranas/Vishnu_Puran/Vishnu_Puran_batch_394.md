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

### Verse 1 (Vishnu Puran 0.7861)
- **Original**: अक्रूरजी भी भगबद्धयान-परायण रहते हुए उस मणि- रत्से प्राप्त सुवर्णके द्वारा निरन्तर यज्ञानुष्ठान करने लगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7862)
- **Original**: यज्ञ-दोक्षित क्षत्रिय और चैक्र्योंके मारनेसे ब्रह्महत्या होती है, इसलिये अक्रूरजी सदा यञ्ञदीक्षारूप क्रवथ धारण ही किये रहते थे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7863)
- **Original**: उस मणिके प्रभावसे बासठ वर्षतक द्वारकामें रोग, दुर्भिक्ष, महामारी या मृत्यु आदि नहीं हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7864)
- **Original**: फिर अक्कूर-पशक्षीय भोज- वंदियोंद्रार सात्वतके प्रफैत्र झत्रुक्तके मारे जानेपर भोजोकि साथ अक्ूर भो द्वास्काकों छोड़कर चले गये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7865)
- **Original**: उनके जाते ही, उसी दिलसे द्वास्कामें रोग, दुर्भिक्ष, सर्प अनावृष्टि और मरी आदि उपद्रव होने करो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7866)
- **Original**: तब गरुडध्वज भगकजान्‌ कृष्ण बलभद्र और उप्रसेन आदि यदुवंशियोंके साथ मिलकर सलाह करने लगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7867)
- **Original**: “इसका क्या कारण है जो एक साथ ही इतने उपद्रबॉकमा आगमन छुआ, इसपर बिचार करना चाहिये ।' उनके ऐसा कहनेपर अन्धक नामक एक वृद्ध यादवने कहा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7868)
- **Original**: “अक्रूरके पिता धफल्क जहाँ-जहाँ रहते थे वहाँ-वहाँ दुर्भिक्ष, महामारों और अनावुष्टि आदि उपद्रब कभी नहीं होते थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7869)
- **Original**: एक बार काविराजके देशामें अनावष्टि हुई थीं। तब
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7870)
- **Original**: 278 नीतः ततश् तत्क्षणाह्ेज्ो लजर्ष
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7871)
- **Original**: काशिराजपफ्त्याक्ष गर्भे कन्यारलत्नै पूर्वपासीत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7872)
- **Original**: सा च कन्या पूर्णेफपि प्रसूतिकाले नैव निश्चक्राम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7873)
- **Original**: एवं च तस्थ गर्भस्य ययु;
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7874)
- **Original**: काशिराजश्न तामात्मजां गर्भस्थामाह
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7875)
- **Original**: पुत्रि कस्मानज्न जाबसे निष्क्रम्यतामास्यं॑ ते द्रष्टडुभिच्छामि एतां च्व मातरं किमिति चिरं क्लेशवसीत्युक्ता गर्भस्थैव व्याजहार
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7876)
- **Original**: तात यश्येकैकां गां दिने दिने ब्राह्मणाय प्रयच्छसि तदाहमन्यैस्तरिभिर्वरैरस्मा द्र्भात्तावदवइयं निष्क्रमिष्यामीत्येतद्वचनमाकर्ण्य राजा दिने दिने ज्राह्मणाय गां प्रादात्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7877)
- **Original**: सापि तावता कालेन जाता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7878)
- **Original**: ततस्तस्थाः पिता गान्दिनीति नाम चकार
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7879)
- **Original**: ता च गान्दिनीं कन्यां श्रफल्कायोप- कारिणे गृहमागतायार्घ्यभूतां प्रादात्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7880)
- **Original**: तस्यामयमक्र्ूरः श्रफल्काजज्े
- **Translation**: 

---

