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

### Verse 1 (Rig Ved 0.7741)
- **Original**: हे इन्द्रदेव ! जिस संग्राम में आपने ऋषि 'एतश' के लिए सूर्य पर भी चढ़ाई की थी, उस संग्राम में लड़ाई करके आपने 'एतश' की सुरक्षा की थी
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7742)
- **Original**: 3374 किमादुतासि बृत्रहन्मघवन्मन्युपत्तम:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7743)
- **Original**: अत्राह दानुमातिर:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7744)
- **Original**: बृत्र का संहार करने वाले ऐश्वर्यवान्‌ हे इन्रदेव ! उसके याद क्या आप अत्यधिक क्रोधित हुए थे ? इस आकाश में आपने 'दानु' के पुत्र 'वृत्र' का संहार किया था
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7745)
- **Original**: 3375, एतद्घेदुत वीर्य1मिन्द्र चकर्थ पौंस्यम्‌ । स्त्रियं यहुर्ईणायुव॑ वर्धीर्दुहितरं दिवः
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7746)
- **Original**: 50 ऋग्वेद संहिता भाग - 2 हे इन्द्रदेव ! आपने बल से सम्पत्र पुरुषार्थ किया था । जिस प्रकार सूर्यदेव चुलोक की पुद्दी उधा का नाश करते हैं, उसी प्रकार आप विशाल शत्रु सेना का संहार करते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7747)
- **Original**: 3376. दिवश्चिद्घा दुहितरं महान्महीयमानाम्‌। उषघासमिन्द्र सं पिणक्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7748)
- **Original**: हे इन्द्रदेव ! आप महान्‌ हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7749)
- **Original**: विशाल शत्रुसेना को उसी प्रकार चूर-चूर कर दें, जिस प्रकार सूर्यदेव उपा को 'छिक्न-भिन्न कर देते हैं
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7750)
- **Original**: 3377, अपोधा अनस:ः सरत्संपिष्टादह बिभ्युषी। नि यत्सीं शिश्नथद्वृषा
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7751)
- **Original**: बलशाली इन्धदेव ने जब उषा के रथ को विदीर्ण कर दिया था, तब भयभीत होने वाली उपा विदीर्ण रथ से दूर होकर प्रकट हुई थी
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7752)
- **Original**: 3378, एतदस्था अनः शये सुसम्पिष्टं विपाश्या । ससार सीं परावत:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7753)
- **Original**: उस उषा देवी का इन्धदेव द्वारा विदीर्ण हुआ रथ 'विपाशा' नदी के किनारे गिर पड़ा और उस स्थान से उषा देवी दूर देश में चली गई
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7754)
- **Original**: 3379, उत सिन्धुं विबाल्य॑ वितस्थानामधि क्षप्ति
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7755)
- **Original**: परि ष्ठा इन्द्र मायया
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7756)
- **Original**: हे इन्द्रदेव ! आपने समस्त जल को तथा परिपूर्ण रूप से भरी हुई वेग से प्रवाहित होने वाली सिन्धु नदी को अपनी बुद्धि के द्वारा धरती पर सब जगह स्थापित किया था
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7757)
- **Original**: 3380. उत शुष्णस्य धृष्णुया प्र मृक्षो अभि वेदनम्‌ । पुरो यदस्य संपिणक्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7758)
- **Original**: हे इन्भधदेव ! आप वर्षण करते वाले हैं। जब आपने 'शुष्ण' नामक असुर के नगरों को विदीर्ण किया था; तब आपने उसके ऐश्वर्य का भी अपहरण किया था
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7759)
- **Original**: 3381. उत दासं कौलितरं बृहत: पर्वतादधि । अवाहन्निन्द्र शम्बरम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7760)
- **Original**: है इद्धदेव ! आपने 'कुलितर' के पुत्र विनाशक 'शम्बर' को विशाल पर्वत के ऊपर से नीचे की ओर धकेल कर मार डाला था
- **Translation**: 

---

