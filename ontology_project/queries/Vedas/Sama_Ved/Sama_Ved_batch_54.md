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

### Verse 1 (Sama Ved 0.1061)
- **Original**: हे इन्धदेव ! आए जन्म से ही भाइयों के संघर्ष से मुक्त हैं, ध आप पर शासन करने वाले कोई बन्धु है और न सहायता करने वाले कोई बन्धु । आप युद्ध (जनसंरक्षण) द्वारा अपने सहयोगियों (बन्धुओं) भक्तों को पाने की कामना करते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1062)
- **Original**: 400, यो न इदमिदं पुरा प्र वस्य आनिनाय तपु व स्तुषे । सखाय इन्द्रमूतये
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1063)
- **Original**: हे भित्रो ! पूर्वकाल से हो जो धन देने वाले है, उन इन्द्र की हम आपके कल्याण के लिए स्तुति करते हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1064)
- **Original**: 401. आ गन्ता मा रिषण्यत प्रस्थावानों माप स्थात समन्यव: । दृढा चिद्यममयिष्णव:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1065)
- **Original**: गतिशील परुद्गण हमें हानि न पहुँचाते हुए हमारे निकट आएँ
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1066)
- **Original**: वे मन्यु (प्रतिरोध की क्षमता) युक्त बलशाली शत्रुओं को भो संताप पहुँचाने वाले हैं, वे हमसे दूर न रहें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1067)
- **Original**: 402. आ याह्वयमिन्दवे5 श्वपते गोपत उर्वरापते । सोम॑ सोमपते पियर
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1068)
- **Original**: अश्वों एवं गौओं के स्वामी, भूमिपालक, सोमरस का पान करने वाले हे इन्द्रदेव ! निचोड़े गये सोमरस का पान करने के लिए हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1069)
- **Original**: 403. त्वया ह स्विद्युजा बयं प्रति श्वसन्तं वृषभ ब्रुवीमहि। संस्थे जनस्य गोमत:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1070)
- **Original**: हे वृषभ के समान बलशाली इन्द्र ! गौ आदि उपकार करने वाले पशुओं के पालक के प्रति क्रोध व्यक्त करने बालों को, हम आपकी सहायता से उचित प्रत्युत्तर देकर दूर हटा दें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1071)
- **Original**: * 404. गावश्चिद्घा समन्यव: सजात्येन मरुत: सबन्धवः ।रिहते ककुभो मिथ:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1072)
- **Original**: 6 हे समान उमंगों से युक्त मरुतो
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1073)
- **Original**: गौएँ सजातीय होने के कारण परस्पर बहिन के समान, विभिन्‍न दिशाओं में विचरण करती हुई भी, परस्पर चाटकर प्रेम प्रकट करने वाली हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1074)
- **Original**: [ भाव यह है कि मनुष्य-पात्र भी ऐसा ही करें ।] 405, त्व॑ं न इन्द्रा भर ओजो नृग्णं शतक्रतो विचर्षणे ।आ बीर॑ पृतनासहम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1075)
- **Original**: । है अनेक कार्यों के सम्पादनकर्ता-ज्ञानी इन्द्रदेव ! आप रमें शक्ति एवं ऐश्वर्य से पूर्ण करें तथा शत्रु को जीतने वाला पुत्र भी प्रदान करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1076)
- **Original**: 406. अधा हीन्द्र गिर्वण उप त्वा काम ईमहे ससृग्महे
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1077)
- **Original**: उदेव ग्मन्त उदभि:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1078)
- **Original**: जैसे जल के साथ जाते हुए लोग (आवश्यकतानुसार जल से तृप्त होते हैं, वैसे हे प्रशंसा के योग्य इन्द्र !अपनी इच्छाओं को पूर्ण करने के लिए हम आपसे प्रार्थना करते हैं, निकट आकर आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1079)
- **Original**: 407. सीदन्तस्ते बयो यथा गोश्रीते मधौ मदिरे विवक्षणे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1080)
- **Original**: अभि ल्वामिद्र नोनुम:
- **Translation**: 

---

