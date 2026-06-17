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

### Verse 1 (Sama Ved 0.301)
- **Original**: 100. अग्ने यजिष्ठा अध्वरे देवां देवयते यज । होता मन्द्रो वि राजस्यति स्रिध:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.302)
- **Original**: यज्ञ में पूजनीय, देवों को बुलाने वाले, शत्रुजयी हे अग्निदिव ! आप याजकों एवं देवों के (कल्याण हेतु) यज्ञ करते हुए सुशोभित होते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.303)
- **Original**: 1091. जज्ञानः सप्त मातृभिमेंधामाशासत श्रिये ।अयं धुवो रयीणां चिकेतदा
- **Translation**: 

---

### Verse 4 (Sama Ved 0.304)
- **Original**: सात माताओं (ज्वालाओं) से समुत्पन, (वृद्धि को प्राप्त याजकों की) मेधाशवित वर्धन हेतु प्रयलशील, ये अग्निदेव धन-सम्पदाओं को भलीप्रकार जानने वाले हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.305)
- **Original**: [फ्लतुत सदर्ध में माठृपद नदी अर्थ का धी वोघक है। सप्त का आशय सात नदियों से है, जो सतलज, व्यास रावी, जिस झ्ेल्कय्‌ सरस्वती और सिन्‍्धु को घिलाकर सिद्ध होती हैं।] 102.उत स्था नो दिवा मतिरदितिरूत्यागमत्‌ ।सा शन्ताता मयस्करदप स्त्रिध:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.306)
- **Original**: हे देवों को माता अदिति ! पूर्ण रक्षा-साधनों सहित आप हमारे समक्ष पधारें तथा शत्रुओं का हनन करें और हमें सुस्क-शान्ति प्रदान करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.307)
- **Original**: पूर्वार्चिक आम्नेयपर्वाणि प्रथपो5व्याय: 1.15 103. ईडिप्वा हि प्रतीत्यां 3 यजस्व जातवेदसम्‌ । चरिष्णुधृममगृभीतशोचिषम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.308)
- **Original**: है स्तोताओ ! शत्रुजयी अदम्य तेजयुक्त, सर्वव्यापी धूप वाले, सर्वज्ञ, अग्निदेव की अर्चना करो
- **Translation**: 

---

### Verse 9 (Sama Ved 0.309)
- **Original**: 104 ,न तस्य मायया च न रिपुरीशीत मर्त्य: ।यो अग्नये ददाश हव्यदातये
- **Translation**: 

---

### Verse 10 (Sama Ved 0.310)
- **Original**: अग्निदेव को हविष्यान्म (की आहुति) प्रदान करने वाले यज़मान पर, किसी भी दुष्ट को माया (छल-छद्म) का प्रभाव नहीं पड़ता
- **Translation**: 

---

### Verse 11 (Sama Ved 0.311)
- **Original**: 105. अप त्यं वृजिनं रिपुं स्तेनमग्ने दुराध्यम्‌। दविष्ठमस्य सत्पते कृधी सुगम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.312)
- **Original**: हे सत्यरक्षक अग्निदेव ! आप मायावी शत्रुओं एवं दुर्थर्ष चोएों को दूर हटाते हुए, हमारे श्रेष्ठ कल्याणकारी मार्ग को सुगम बनाएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.313)
- **Original**: 1906. श्रुप्टयग्ने नवस्य में स्तोमस्य वीर विश्पते । नि मायिनस्तपसा रक्षसो दह
- **Translation**: 

---

### Verse 14 (Sama Ved 0.314)
- **Original**: हे प्रजापालक अग्ने ! हमारे इस नूतन स्तोत्र को सुनकर उत्साही हुए आप, छली और कपटी दुष्टों को अपने प्रस्वर तेज से भस्म कर दें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.315)
- **Original**: इति एकादश: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.316)
- **Original**: #ऊं के
- **Translation**: 

---

### Verse 17 (Sama Ved 0.317)
- **Original**: द्वादश: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.318)
- **Original**: 107. प्र मंहिष्ठाय गायत ऋाव्ने बृहते शुक्रशोचिषे । उपस्तुतासो अग्नये
- **Translation**: 

---

### Verse 19 (Sama Ved 0.319)
- **Original**: है स्तोताओ ! आप श्रेष्ठ स्तोत्रों द्रारा अग्निदेव की स्तुति करें । वे महान्‌ सत्य और यज्ञ के पालक, महान्‌ तेजस्वी और रक्षक हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.320)
- **Original**: 108. प्र सो अग्ने तवोतिभिः सुबीराभिस्तरति वाजकर्मभि: । यस्य त्व॑ सख्यमाविथ
- **Translation**: 

---

