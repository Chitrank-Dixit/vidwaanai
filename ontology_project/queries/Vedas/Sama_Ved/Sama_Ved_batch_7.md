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

### Verse 1 (Sama Ved 0.121)
- **Original**: श्4ड सामवेद-संहिता द्वारा आहूत किये जाते हैं । कोई भी प्रखर-तेजस्वी, जो आपकी स्तुति करते हैं, उनको सब सुख प्राप्त होते हैं । हम हृदय से आपका वरण करते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.122)
- **Original**: 27. अम्निर्मूर्द्धा दिव: ककुत्पतिः पृथिव्या अयम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.123)
- **Original**: अपां रेतांसि जिन्वति
- **Translation**: 

---

### Verse 4 (Sama Ved 0.124)
- **Original**: 7।। अम्निदेव द्ुलोक से पृथ्वी तक संव्याप्त जीवों के पालनकर्त्ता हैं, जल को रूप एवं गति देने में समर्थ हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.125)
- **Original**: [बह भाव वैज्ञानिक सन्दर्भ में भी प्रयुक्त होता है । हाइड्रोजन आकसीजन ऊर्जा से जल उत्पन्न होता है। ऊर्जा ही जल को मेष बनाकर प्रकृति का पोषण करती है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.126)
- **Original**: विज्ञान जगत्‌ में यह तथ्य 'कण्डेस्ड सुपर हीटेड स्कीम' के अन्तर्गत आता है ।] 28. इममू घु त्वमस्माक॑ सनि गायत्रं नव्यांसम्‌। अग्ने देवेषु प्र वोच:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.127)
- **Original**: है अग्निदेव ! आप हमारे गायत्री परक, प्राण-पोषक स्तोत्रों (भावों) एवं नवीन अन (हव्य) को देवों तक (देव वृत्तियों के पोषण हेतु) पहुँचाएँ
- **Translation**: 

---

### Verse 8 (Sama Ved 0.128)
- **Original**: 29. त॑ त्वा गोपवनो गिरा जनिष्ठदग्ने अड्डिर:। स पावक श्रुधी हवम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.129)
- **Original**: गोपवन क्रषि को स्तुति से प्रकट हुए, शरीरावयवों में सृक्ष्मरूप से विद्यमान, सबको पवित्र करने वाले हे अग्निदेव ! आप हमारी प्रार्थना ध्यान से सुनें । मानव शरीरावयवों में चेतना के सूक्ष्म केन्द्र विद्यमान होते हैं, स्वास्थ्य के रहस्य वे ही हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.130)
- **Original**: 30, परि वाजपति: कविरम्निईव्यान्यक्रमीत्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.131)
- **Original**: दधद्गलानि दाशुषे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.132)
- **Original**: सर्वज्ञ, अन्नों के स्वामी अग्निदेव, याज़कों द्वारा दिये गये हवनीय पदार्थों को स्वीकार करते हैं तथा परमार्थ प्रायणों को धन-धान्य से परिपूर्ण बनाते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.133)
- **Original**: 39. उदु त्यं जातवेदसस देव॑ वहन्ति केतवः । दृशे विश्वाय सूर्यम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.134)
- **Original**: संसार को सूर्य का बोध (दर्शन) कराने के लिए , उसकी किरणें, जातवेद (सूर्य) से जिसकी उत्पत्ति समझी जाती है-- ऐसे अग्निदेव को भलीप्रकार धारण किये रहती हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.135)
- **Original**: 32. कविमम्निमुप स्तुहि सत्यथर्माणमध्वरे
- **Translation**: 

---

### Verse 16 (Sama Ved 0.136)
- **Original**: देवममीवचातनम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.137)
- **Original**: हे कत्विजो ! लोकहितकारी यज्ञ में रोगों को नष्ट करने वाले, ज्ञानवान्‌ अग्निदेव की स्तुति आप सब विशेष रूप से करें
- **Translation**: 

---

### Verse 18 (Sama Ved 0.138)
- **Original**: 33. शं नो देवीरभिष्टये शं नो भवन्तु पीतये । शं योरभि ख्नरवन्तु नः
- **Translation**: 

---

### Verse 19 (Sama Ved 0.139)
- **Original**: हमें, सुख-शान्ति प्रदान करने वाला जल-प्रवाह प्रकट हो
- **Translation**: 

---

### Verse 20 (Sama Ved 0.140)
- **Original**: वह जल पीने योग्य, कल्याणकारी एवं सुखकर हो
- **Translation**: 

---

