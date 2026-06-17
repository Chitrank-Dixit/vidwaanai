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

### Verse 1 (Sama Ved 0.81)
- **Original**: है अग्ने ! आप सामर्थ्यवान्‌ एवं अतुलनीय पराक्रम वाले हैं, इसलिये समस्त साधक जन आपको नमस्कार करते हैं। आप अहितकारियों के विनाशक हैं, उनका संहार करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.82)
- **Original**: 12.दूतं वो विश्ववेद्सं हव्यवाहममर्त्यम्‌। यजिष्ठमृझ्ञसे गिरा
- **Translation**: 

---

### Verse 3 (Sama Ved 0.83)
- **Original**: ज्ञान सम्पन्न हे अग्निदेव ! आप हवि वाहक हैं। समस्त देव शक्तियों के प्रतिनिधि हैं, यज्ञ के साधन रूप हैं । हम आपसे स्तुति के माध्यम से अनुकूल होने की प्रार्थना करते हैं। आप सदा कृपायान्‌ बने रहें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.84)
- **Original**: 313.उप त्वा जामयो गिरो देदिशतीईविष्कृत:ः । बायोरनीके अस्थिरन्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.85)
- **Original**: है अग्ने ! यजमान की वाणी से प्रकट होने वाली भ्रिय स्तुतियाँ, आपके गुणों को प्रकट करती हैं और वायु के सहयोग से आपको प्रदीप्त करती हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.86)
- **Original**: 14.उप त्वाग्ने दिवेदिवे दोषावस्तर्थिया वयम्‌ । नमो भरन्त एमसि
- **Translation**: 

---

### Verse 7 (Sama Ved 0.87)
- **Original**: है जाज्वल्यमान देव ! हम आपके सच्चे उपासक हैं । श्रेष्ठ बुद्धि द्वारा आपकी स्तुति करते हैं । दिन और रात्रि में सतत आपका गुणगान करते हैं । हे देव ! हमें आपका सानिध्य प्राप्त हो
- **Translation**: 

---

### Verse 8 (Sama Ved 0.88)
- **Original**: 15. जराबोध तद्विविड्डि विशेविशे यज्ञियाय
- **Translation**: 

---

### Verse 9 (Sama Ved 0.89)
- **Original**: स्तोम॑ रुद्राय दृशीकम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.90)
- **Original**: स्तुतियों से समझे जाने वाले हे अग्निटेव ! यजमान पुनीत यज्ञस्थल में आपके दुष्ट-विनाशक स्वरूप के आवाहन हेतु सुन्दर प्रार्थना करते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.91)
- **Original**: 36. प्रति त्यं चारुमध्वरं गोपीथाय प्र हृयसे । मरुद्धिरग्न आ गहि
- **Translation**: 

---

### Verse 12 (Sama Ved 0.92)
- **Original**: है अग्ने ! यज्ञ की गरिमा के संरक्षण के लिए हम आपका आबाहन करते हैं। आपको मरुतों के साथ आमच्रित करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.93)
- **Original**: देवताओं के इस यज्ञ में आप पधारें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.94)
- **Original**: 6 6 17.अश्व न त्वा वारवन्तं वन्दध्या अर्ग्नि नमोभिः । सप्राजन्तमध्वराणाम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.95)
- **Original**: सूर्य के समान तमनाशक एवं शक्तिशाली है अग्ने ! निर्विध्न और हिंसारहित यज्ञ में आप पधारें । हम सभी आपको नमन करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.96)
- **Original**: पूर्वार्चिकि आप्नेयपर्वाणि प्रथमों5ध्याय: 1.3 18. और्वभूगुवच्छुचिमप्नवानवदा हुवे । अग्नि समुद्रवाससम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.97)
- **Original**: हे समुद्र में वास करने वाले अग्निदेव ! (बड़वाग्नि) भूगु और अप्नवान्‌ आदि ज्ञानी ऋषियों ने सच्चे मन से आपकी प्रार्थना की है । हम भी हृदय से आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.98)
- **Original**: 19, अग्निमिन्धानो मनसा थियं सचेत मर्त्य; । अग्निमिन्धे विवस्थप्रि:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.99)
- **Original**: मनोयोगपूर्वक अमन प्रदीष्त करने वाला साधक अपनी श्रद्धा को भी प्रदीप्त करता है । अस्तु , सूर्य किरणों के साथ (सूर्योदय के साथ) ही अग्निहोत्र की व्यवस्थ; करता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.100)
- **Original**: [सूर्य ऊर्जा से शरीर में विशेष पदार्थ का निर्माण होता है-यह विज्ञाससिद्ध सिद्धानत है। ऋषि प्रतिपादित असिहोत्र करने का समय धी यही है ।] 20. आदित्मत्नस्य रेतसो ज्योत्ति: पश्यन्ति वासरम्‌
- **Translation**: 

---

