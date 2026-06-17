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

### Verse 1 (Rig Ved 0.621)
- **Original**: “7117777477777777777774एएए को भो जानति हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.622)
- **Original**: ढ2 ऋण्वेद संहिता धाण-3 277, बेद वातस्य वर्तनिमुरो्ऋष्वस्य बृहत:। वेदा ये अध्यासते
- **Translation**: 

---

### Verse 3 (Rig Ved 0.623)
- **Original**: वे वरुणदेव अत्यन्त विस्तृत, दर्शनीय और अधिक गुणवान्‌ वायु के मार्ग को जानते हैं । वे ऊपर घुलोक में रहने वाले देवों को भी जानते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.624)
- **Original**: 278. नि षसाद थृतब्बतो वरुण: पस्त्या3स्वा। साप्राज्याय सुक्रतु:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.625)
- **Original**: प्रकृति के नियमों का विधियत्‌ पालन कराने वाले, श्रेष्ठ कर्मों में सदैव निरत रहने वाले वरुणदेव प्रजाओं में साप्राज्य स्थापित करने के लिए बैठते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.626)
- **Original**: 279. अतो विश्वान्यद्धुता चिकित्वाँ अभि पश्यति। कृतानि या च कर्त्या
- **Translation**: 

---

### Verse 7 (Rig Ved 0.627)
- **Original**: सब अद्भुत कर्मों को क्रिया-विधि जानने वाले वरुणदेव, जो कर्म सम्पादित हो चुके हैं और जो किये जाने हैं, उन सबको भली-भाँति देखते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.628)
- **Original**: 280. स नो विश्वाहा सुक्रतुरादित्य: सुपथा करत्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.629)
- **Original**: प्रण आयूंषि तारिषत्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.630)
- **Original**: वे उत्तम कर्मशील अदिति पुत्र वरुणदेव हमें सदा श्रेष्ठ मार्ग की ओर प्रेरित करें और हमारी आयु को अढ़ाएँ
- **Translation**: 

---

### Verse 11 (Rig Ved 0.631)
- **Original**: 281. बिश्रद्द्रापिं हिरण्ययं वरुणो वस्त निर्णिजम्‌। परि स्पशो नि षेदिरे
- **Translation**: 

---

### Verse 12 (Rig Ved 0.632)
- **Original**: सुवर्णमय कवच धारण करके वरुणदेव अपने हुए-पुष्ट शरीर को सुसज्जित करते हैं । शुअ्र प्रकाश किरणें उनके चारों ओर विस्तीर्ण होती हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.633)
- **Original**: 282. न य॑ दिप्सन्ति दिप्सवो न द्ुह्कणो जनानाम्‌। न देव॑मभिमातय:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.634)
- **Original**: हिंसा करने की इच्छा वाले शत्रु-जन/भयाक्रान्त होकर ) जिनकी हिंसा नहीं कर पाते, लोगों के प्रति द्रेष रखने वाले, जिससे द्रेष नहीं कर पाते- ऐसे (वरुण) देव को पापीजन स्पर्श तक नहीं कर पाते
- **Translation**: 

---

### Verse 15 (Rig Ved 0.635)
- **Original**: 283. उत यो मानुषेष्वा यशश्नक्रे असाम्या। अस्माकमुदरेष्वा
- **Translation**: 

---

### Verse 16 (Rig Ved 0.636)
- **Original**: जिन वरुणदेव ने मनुष्यों के लिए बिपुल अन्न - भंडार उत्पन्न किया है; उन्होंने ही हमारे उदर में पाचन सामर्थ्य भी स्थापित की है
- **Translation**: 

---

### Verse 17 (Rig Ved 0.637)
- **Original**: 287 परा में यन्ति धीतयो गावो न गव्यूतीरनु । इच्छन्तीरुरुचक्षसम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.638)
- **Original**: उस सर्वद्रष्ट वरुणदेव की कामना करने वाली हमारी बुद्धियाँ, वैसे हो उन तक पहुँचतो हैं, जैसे गौएँ गोष्ठ (बाड़े) की ओर जाती हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.639)
- **Original**: 285 स॑ नु वोचावहै पुनर्यतो पे पध्वाभृतम्‌। होतेव क्षदसे प्रियम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.640)
- **Original**: होता (अग्निदेव) के समान हमारे द्वारा लाकर समर्पित की गई हवियों का आप अग्निदेव के समान भश्षण करें, फिर हम दोनों वार्ता करेंगे
- **Translation**: 

---

