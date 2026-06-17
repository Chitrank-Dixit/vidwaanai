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

### Verse 1 (Bramha 0.2481)
- **Original**: हो। चाणूर और केशीके नाशक! आपकी जय जगप्नाथ श्रीकृष्णके मन्दिस्में प्रवेश करके तीन यार
- **Translation**: 

---

### Verse 2 (Bramha 0.2482)
- **Original**: हो। कंसनाशन! आपकी जय हो। कमललोचन! प्रदक्षिणा करे। फिर नाममखसे बलभद्रजीका भक्तिपूर्वक
- **Translation**: 

---

### Verse 3 (Bramha 0.2483)
- **Original**: आपकी जय हो। चक्रगदाधघर! आपकी जय हो। पूजन करके निम्नाद्भित रूपसे प्रार्था करे--._
- **Translation**: 

---

### Verse 4 (Bramha 0.2484)
- **Original**: नील मेघके समान श्यामवर्ण! आपकी जय हो। नमस्ते हलधुग्राम नमस्ते मुसलायुध।
- **Translation**: 

---

### Verse 5 (Bramha 0.2485)
- **Original**: सबको सुख देनेवाले परमेश्वर! आपकी जय हो। नमस्ते रेकतीकान्त नमस्ते भक्तवत्सल
- **Translation**: 

---

### Verse 6 (Bramha 0.2486)
- **Original**: जगत्पूम्य देव! आपकी जय हो। संसारसंहारक ! नमस्ते बलिनां श्रेष्ठ नमस्ते थरणीथर।
- **Translation**: 

---

### Verse 7 (Bramha 0.2487)
- **Original**: आपकी जय हो। लोकपते नाथ! आपकी जय प्रलाम्थारे नमस्तेउस्तु ज्राहि मां कृष्णपूर्वज
- **Translation**: 

---

### Verse 8 (Bramha 0.2488)
- **Original**: हो। मनोबाज्छित फल देनेवाले देवता! आपकी 'हलधारण करनेवाले राम! आपको नमस्कार
- **Translation**: 

---

### Verse 9 (Bramha 0.2489)
- **Original**: जय हो। यह भयड्डर संसारसागर सर्वथा नि:सार है। मूसलको आयुध रूपमें रखनेवाले! आपको
- **Translation**: 

---

### Verse 10 (Bramha 0.2490)
- **Original**: है। इसमें दुःखमय फेन भरा हुआ है। यह नमस्कार है। रेवतीरमण! आपको नमस्कार है।
- **Translation**: 

---

### Verse 11 (Bramha 0.2491)
- **Original**: क्रोधरूपी ग्राहसे पूर्ण है। इसमें विषयरूपी जलराशि भक्तवत्सल! आपको नमस्कार है। बलबानोंमें
- **Translation**: 

---

### Verse 12 (Bramha 0.2492)
- **Original**: भरी हुई है। भाँति-भाँतिके रोग ही इसमें उठती श्रेष्टट आपको नपस्कार है। पृथ्वीको मस्तकपर
- **Translation**: 

---

### Verse 13 (Bramha 0.2493)
- **Original**: हुई लहरें हैं। मोहरूपी भँवरोंक कारण यह धारण करनेवाले शेषजी! आपको नमस्कार है।
- **Translation**: 

---

### Verse 14 (Bramha 0.2494)
- **Original**: अत्यन्त दुस्तर जान पड़ता है। सुरश्रेष्ठ ! मैं इस घोर प्रलम्बशत्रो! आपको नमस्कार है। श्रीकृष्णके
- **Translation**: 

---

### Verse 15 (Bramha 0.2495)
- **Original**: संसाररूपी समुद्रमें डूबा हुआ हूँ। पुरुषोत्तम ! मेरी अग्रज! मेरी रक्षा कीजिये।'
- **Translation**: 

---

### Verse 16 (Bramha 0.2496)
- **Original**: रक्षा कोजिये।' इस प्रकार प्रार्था करके जो इस प्रकार कैलासशिखरके समान आकार
- **Translation**: 

---

### Verse 17 (Bramha 0.2497)
- **Original**: देवेश्वर, वरदायक, भक्तवत्सल, सर्वपापहारी, समस्त और चन्द्रमासे भी कमनीय मुखवाले, नीलवखधायी,
- **Translation**: 

---

### Verse 18 (Bramha 0.2498)
- **Original**: अभिलपित फलोंके दाता, मोटे कंधे और दो देवपूजित, अनन्त, अजेय, एक कुण्डलसे विभूषित,
- **Translation**: 

---

### Verse 19 (Bramha 0.2499)
- **Original**: भुजाओंबाले, श्यामवर्ण, कमलपत्रके समान विशाल फर्णोके द्वारा विकट मस्तकवाले, महाबली हलधरको ] नेन्नोंवाले, चौड़ी छाती, विशाल भुजा, पीत अस्त्र प्रसन्न करें। बलरामजीकौ पजाके पश्चात्‌ विद्वान. और सुन्दर मखबवाले, शक्ु-चक्र-गदाधर,
- **Translation**: 

---

### Verse 20 (Bramha 0.2500)
- **Original**: 120 » संक्षिप्त ख्रह्मपुराण « मुकुटाड्दभूषित, समस्त शुभ लक्षणोंसे युक्त , दर्शन करके मनुष्य दुर्लभ मोक्षतक प्राप्त कर और बनमालाविभूषित भगवान्‌ श्रीकृष्णका दर्शन
- **Translation**: 

---

