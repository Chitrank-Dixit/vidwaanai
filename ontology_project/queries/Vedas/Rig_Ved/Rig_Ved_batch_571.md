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

### Verse 1 (Rig Ved 0.11401)
- **Original**: जो करम्भ (दही, घृतयुक्त अन्न विशेष अथवा करों-किरणों से जल) का सेवन करने वाले पृषादेव की स्तुति करता है, उसे अन्य देवताओं की स्तुति करने की आवश्यकता नहीं पड़ती है
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11402)
- **Original**: 4962. उत घा स रधीतम: सख्या सत्पतिर्युजा । इन्द्रो वृत्राणि जिघ्नते
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11403)
- **Original**: बास्तव में ज़ो श्रेष्ठ रथी हैं, उन पृषादेव की मित्रवत्‌ सहायता से सज्जनों के रक्षक इन्द्रदेव शत्रुओं का संहार करते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11404)
- **Original**: 4963. उताद: परुषे गवि सूस्क्षक्रं हिरण्ययम्‌। न्यैरयद्रथीतम:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11405)
- **Original**: वे श्रेष्ठ रथी पृषादेव सूर्यदेव के हिरण्यमय रथ चक्र को उत्तम रीति से घुमाते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11406)
- **Original**: 4964. यदद्य त्वा पुरुष्ठुत ब्रवाम दस्र मन्तुम:। तत्सु नो मन्म साधय
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11407)
- **Original**: हे पृषादेव ! आप बहुतों द्वारा प्रशंसित, दर्शनीय और माननीय हैं । हम जिस धन की इच्छा से आपको स्तुति करते हैं, बह आप हमें दिलाएँ
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11408)
- **Original**: 4965. इमं च नो गवेषर्ण सातये सीषधो गणम्‌। आरात्‌ पूषन्नसि श्रुतः
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11409)
- **Original**: हे पूक्ननूदेव ! आप समीप से और दूर से भी प्रसिद्ध हैं, अर्थात्‌ आप सर्वव्यापक हैं । आप गौओं के खोजने वालों को धन प्रदान करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11410)
- **Original**: 4966. आ ते स्वस्तिमीमह आरे अधामुपावसुम्‌। अद्या च सर्वतातये श्वश्न सर्वतातये
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11411)
- **Original**: हे पूषन्देव ! हम आपकी स्तुति करते हैं, जिससे हमारा आज और कल (सर्वदा) कल्याणकारी हो । आप हमें धन प्रदान करें और पाप से बचाएँ
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11412)
- **Original**: [ सूक्त - 57 ] [ऋषि - भरद्वाज बा्स्पत्य । देवता - इन्ध पूषा । छत्द -वरिष्टुप्‌ , 2 जगती
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11413)
- **Original**: 4967. इन्द्रा नु पृषणा व्यं सख्याय स्वस्तये
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11414)
- **Original**: हुवेम वाजसातये
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11415)
- **Original**: हम अश्न प्राप्ति की कामना से, अपने कल्याण के लिए मित्रस्वरूप इन्द्र और पूषा देवताओं को स्तुतियों के द्वारा बुलाते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11416)
- **Original**: प्रं0 6 सू0 58 81 4968. सोममन्य उपासदत्पातवे चम्वो: सुतम्‌। करम्भमन्य इच्छति
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11417)
- **Original**: आसन पर बैठे देवों में इन्द्रदेव अभिषुत सोमसस को पीने की इच्छा करते हैं एवं पृषादेव करम्भ (सत्तू युक्त खाद्य पदार्थ ) की इच्छा करते हैं
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11418)
- **Original**: 4969. अजा अन्यस्थ वहयो हरी अन्यस्य सम्धृता। ताभ्यां वृत्राणि जिध्नते
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11419)
- **Original**: इन््रदेव के रथ में घोड़े एवं पृषादेव के रथ में छाग (बकरी) युक्त (जुते) हैं । ये दोनों मिलकर वृत्रों (शत्रुओं) का नाश करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11420)
- **Original**: 4970. यदिद्धों अनयद्वितो महीरपो वृषन्तम: । तत्र पृूषाभवत्सचा
- **Translation**: 

---

