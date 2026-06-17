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

### Verse 1 (Sama Ved 0.2821)
- **Original**: के के के
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2822)
- **Original**: 78 सामवेद-संहिता
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2823)
- **Original**: षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2824)
- **Original**: । 1093.परि स्वानो गिरिष्ठा: पवित्रे सोमो अक्षरत्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2825)
- **Original**: मदेषु सर्वधा असि
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2826)
- **Original**: गिरि- शिखरों पर रहने वाले, प्रसनतादायक पदार्थों में सर्वश्रेष्ठ हे सोमदेव ! आपकी रस धारा शोधन-यन्त्र द्वारा पवित्र होकर स्थिर हो रही है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2827)
- **Original**: 1094.त्वं विप्रस्त्व॑ कविर्मधु प्र जातमन्धस: । मदेघु सर्वधा असि
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2828)
- **Original**: हे सोमदेव ! आप ज्ञानवान्‌ हैं, दूरदर्शी हैं तथा आप अन्न से पैदा हुए पोषक-तत्वों को देते हैं । आनैन्दप्रद रसों में आपका स्थान सर्वोपम है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2829)
- **Original**: 1095.त्वे विश्वे सजोषसो देवासः पीतिमाशत
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2830)
- **Original**: मदेषु सर्वधा असि
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2831)
- **Original**: है सोमदेव ! संगठन-शवित से क्रियाशील, सभी देवता आपके रस का सेवन करने की कामना करते हैं । आनन्द-प्रदाताओं में आप ही सर्वोत्कृष्ट हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2832)
- **Original**: 1096. स सुन्वे यो वसूनां यो रायामानेता य इडानाम्‌। सोमो यः सुक्षितीनाम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2833)
- **Original**: जो सोम, धन-धान्य, गौएँ एवं श्रेष्ठ सन्‍्तति के रूप में अपार वैभव प्रदान करने वाले हैं, उस सोम के रस को हम निचोड़ने एवं पवित्र करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2834)
- **Original**: 1097.यस्य त इन्द्र: पिबाद्यस्थ मरुतो यस्य वार्यमणा भग:। आ येन मित्रावरुणा करामह एन्द्रमवसे महे
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2835)
- **Original**: । है सोम (आपके दिव्य रस को इन्द्र, मत्द्गण, अर्यमा, भग आदि देवता सेवन करते हैं । जिस प्रकार सोम द्वारा सुरक्षा के लिए मित्र और वरुण देवों को बुलाया जाता है; उसी प्रकार इन्द्रदेव को भी आमंत्रित करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2836)
- **Original**: 1098. तं व: सखायो मदाय पुनानमभि गायत । शिशुं न हव्यैः स्वदयन्त गूर्तिभि:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2837)
- **Original**: हे ऋत्विजो ! आप देवताओं की प्रसन्‍नता के लिए शुद्ध होने वाले सोमरस का गुणगान करो । जिस प्रकार मातृ-शक्ति बालक को शोभायुक्त करती है । उसी प्रकार सोम को आहुतियों और प्रार्थनाओं द्वारा सुस्वादु (स्वादयुक्त) बनाओ
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2838)
- **Original**: 1099.सं बत्स इब मातृभिरिन्दुर्हिन्बानो अज्यते
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2839)
- **Original**: देवावीर्मदो मतिभि: परिष्कृत:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2840)
- **Original**: देव-संरक्षक, प्रसनतादायक, स्तुतियों से शोधित और याजकों के प्रेरक सोमरस को जल से मिश्रित करते हैं। माता के द्वारा शिशु को नहलाने-धुलाने की तरह, सोमरस जल के द्वारा शुद्ध किया जाता है
- **Translation**: 

---

