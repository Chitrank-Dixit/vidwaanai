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

### Verse 1 (Vishnu Puran 0.7081)
- **Original**: तन और चतततन
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7082)
- **Original**: (आश 6 छठा अध्याय सोमखंद्ाका वर्णन; चन्द्रमा, खुध और पुरूरखाका चरित्र श्रीमैजेव उवाच सूर्यस्थ वेश्या भगवन्कथिता भवता मप्त। सोमस्याप्यखिलान्वंश्याउ़्ेतुमिच्छामि पार्धिवान्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7083)
- **Original**: 9 कीर्व्यते स्थिरकीर्तीनां येषामद्यापि सन्तति: । प्रसादसुमुखस्तान्पे..ब्रह्मन्नाख्यातुमहसि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7084)
- **Original**: 2 अआरीपएशर उजाच श्रूयतां मुनिदार्दूल बंहा: प्रथिततेजस: । सोमस्यानुक्रमात्ख्याता यत्रोर्वीपतयो5भवन्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7085)
- **Original**: 3 अय॑ हि बंशो5तिबलपराक्रमदुतिशीलब्ेष्टा- वद्धिरतिगुणान्वितैर्नहुषययातिकार्तवीर्यार्जुनादि- भिर्भुपालैरलडइ-कृतस्तमहं कथयामि श्रूयताम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7086)
- **Original**: अखिलजगत्स्ष्टर्भगवतो नारायणस्य नाभिसरोजसमुद्धवाब्जयोनेग्रह्वण: पुत्रोउत्रिः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7087)
- **Original**: अभ्रेस्सोम:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7088)
- **Original**: तें च भगवानब्ज- योनि: अधोषौषशधिद्ठिजनक्षत्राणामाधिपत्ये- उभ्यषेचयत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7089)
- **Original**: स च राजसूयमकरोत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7090)
- **Original**: तत््रभावाद्त्युत्कृष्टाधिपत्याधिष्ठातृत्वाश्वन॑_ मद आविवेश
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7091)
- **Original**: पम्रदावलेपाच्च सकलदेबगुरो- बुहस्पतेस्तारां नाम पत्नीं जहार
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7092)
- **Original**: बहुशश्च॒बृहस्पतिचोदितेन भगवता ब्रह्मणा चोद्यमान: सकलैश्न देवर्षिभिर्याच्यमानोउपि न मुमोच
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7093)
- **Original**: तस्य चद्रस्य च बृहस्पतेद्रेघादुशना पार्षिणि- आहो5भूत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7094)
- **Original**: अड्विसअ्॒ सकाशादुप- लब्धविद्यो भगवान्स्त्रो बृहस्पतेः साहाय्य- मकरोत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7095)
- **Original**: यतश्चोशना ततो जम्मकुम्भाद्या: समस्‍्ता एव दैत्यदानबनिकाया महान्तमुद्यर्म चक्र:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7096)
- **Original**: मैत्रेयजी ओले--भगवन्‌ ! आपने सूर्यबंशीय राजाओंका यर्णन तो कर दिया, अब मैं सम्पूर्ण चन्द्रबंशीय भूषतियोंका युत्तान्त भी सुनना चाहता हूँ। जिन स्थिरकीर्ति महाराजोंकी सन्‍्तत्तिका सुयश आज भी गान किया जाता है, हे अ्रह्मन्‌ ! प्रसन्न-मुखसे आप उन्हींका वर्णन मुझसे कीजिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7097)
- **Original**: श्रीपराझ्षरजी बोले--हे मुनिश्लार्दूल ! परम तेजस्वी चद्धमाके बंदाका क्रमशः श्रवण करो जिसमें अनेकों बिख्यात राजालोग हुए हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7098)
- **Original**: यह वंज्ञ नहुष, ययात्ति, कार्तवीर्य और अर्जुन आदि अनेकों अति बल-पराक्रमशील, कान्तिमान्‌, क्रियावान्‌ और सदगुणसम्पत्न राजाओँसे अलड्डूत हुआ है। सुनो, मैं उसका वर्णन करता हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7099)
- **Original**: सम्पूर्ण जगत्‌के रचयिता भगवान्‌ नारायणके नाभि- कमलपसे उत्पन्न हुए भगवान्‌ ब्रह्मजीके पुत्र अत्रि प्रजापति थे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7100)
- **Original**: इन अभ्िके पुत्र चन्द्रमा हुए
- **Translation**: 

---

