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

### Verse 1 (Sama Ved 0.101)
- **Original**: परो यदिध्यते दिवि
- **Translation**: 

---

### Verse 2 (Sama Ved 0.102)
- **Original**: चुलोक से भी परे स्वप्रकाशित (सविता) तथा दिन में दृश्यमान सुर्यदेव इन सभी प्राचीनतम तेजस्वी स्वरूपों में द्रष्टा परमात्मा का ही तेज देखते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.103)
- **Original**: [विज्ञान जगत्‌ में पदार्थ की अनन्तता का आधार अज्ञात है । जबकि ऋषियों ने इस आार को प्रसूत करने वाली शक्ति को 'सविता' नाम दिया है ।] ह
- **Translation**: 

---

### Verse 4 (Sama Ved 0.104)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.105)
- **Original**: के के के
- **Translation**: 

---

### Verse 6 (Sama Ved 0.106)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.107)
- **Original**: 21.अग्नि वो वृधन्तमध्वराणां पुरूतमम्‌ । अच्छा नप्जे सहस्वते
- **Translation**: 

---

### Verse 8 (Sama Ved 0.108)
- **Original**: हे ऋत्विजो ! अपने अहिंसक पसमार्थ कार्यों (यज्ञों) में सहायक, अतिश्रेष्ठ, सबके हितैपी, बलशाली आ ग्मदेव का सानिलध्य प्राप्त करो
- **Translation**: 

---

### Verse 9 (Sama Ved 0.109)
- **Original**: 22. अग्निस्तिग्मेन शोचिषा य॑ सद्दिश्व॑ न्‍्य3त्रिणम्‌ । अग्निनों बंसते रयिम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.110)
- **Original**: है अग्निदिव ! आप अपनी प्रज्वलित तीक्ष्ण ज्वालाओं से विध्नकारक तत्वों को-शत्रुओं को नष्ट करें और जो आपकी उपासना तथा स्तृति करते हैं, उनको बल और ऐश्वर्य श्रदान करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.111)
- **Original**: 23. अग्ने मृड महाँ अस्थय आ देवयुं जनम्‌ । इयेथ बर्हिरासदम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.112)
- **Original**: है अगने ! आप उपासकों को समृद्ध और सुखी बनाएँ, क्योंकि आप सामर्थ्यवान्‌ हैं-महान # + उपासक यजमानों के समीप पवित्र आसन पर बैठने के लिए आप पधारें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.113)
- **Original**: 24. अग्ने रक्षा णो अंहसः प्रति सम देव रीषत: । तपिष्ठैरजरों दह
- **Translation**: 

---

### Verse 14 (Sama Ved 0.114)
- **Original**: है अप्ने ! पाप से आप हमें बचाएँ । हमारी रक्षा कर आप अपने अज़र-अप्र-प्रखर तेज़ से हिंसक शत्रुओं की कामनाओं को भस्मीभूत करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.115)
- **Original**: 25. अग्ने युड्क्ष्वा हि ये तवाश्रासो देव साधव: । अरं बहन्त्याशव:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.116)
- **Original**: हे अग्ने
- **Translation**: 

---

### Verse 17 (Sama Ved 0.117)
- **Original**: द्रुतिगति से चलने वाले श्रेष्ठ, कुशल अपने अश्वों (बलवान, कर्मठ, इन्द्रियाटिकों) को आप रथ में नियोजित करें । (अपने नियंत्रण में संचालित करें)
- **Translation**: 

---

### Verse 18 (Sama Ved 0.118)
- **Original**: 26. नि त्वा नक्ष्य विश्पते द्युमन्तं धीमहे वयम्‌ । सुबीरमग्न आहुत
- **Translation**: 

---

### Verse 19 (Sama Ved 0.119)
- **Original**: हे अग्ने
- **Translation**: 

---

### Verse 20 (Sama Ved 0.120)
- **Original**: हे सवारी ! हम आपको इस पावन पुनीत स्थल पर प्रतिष्ठापित करते हैं । आप अनेकों यजमानों
- **Translation**: 

---

