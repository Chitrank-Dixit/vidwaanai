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

### Verse 1 (Bramha 0.8321)
- **Original**: हटकर जनलोकमें प्रवेश करते हैं। मुनिवरों! अविनाशी भगवान्‌ विष्णु जगत्‌का संहार करनेके
- **Translation**: 

---

### Verse 2 (Bramha 0.8322)
- **Original**: इसके बाद रुद्ररूपधारी श्रीजनार्दन सम्पूर्ण जगत्‌को लिये सम्पूर्ण प्रजाको अपनेमें लीन कर लेनेका
- **Translation**: 

---

### Verse 3 (Bramha 0.8323)
- **Original**: दग्ध करके अपने मुखके निःश्राससे मेघोंको यत्न करते हैं। मुनिबरो ! उस समय भगवान्‌ विष्णु
- **Translation**: 

---

### Verse 4 (Bramha 0.8324)
- **Original**: प्रकट करते हैं। उस समय आकाशमें घोर सूर्यकी सातों किरणोंमें स्थित होकर पृथ्वीका
- **Translation**: 

---

### Verse 5 (Bramha 0.8325)
- **Original**: संवर्तक मेघ उमड़ आते हैं, जो बड़े-बड़े सम्पूर्ण जल सोख लेते हैं। सम्पूर्ण प्राणियों और
- **Translation**: 

---

### Verse 6 (Bramha 0.8326)
- **Original**: गजराजोंके समान प्रतीत होते हैं । बे बिजलीकी पृथ्वीमें स्थित समस्त जलकों सोखकर वे
- **Translation**: 

---

### Verse 7 (Bramha 0.8327)
- **Original**: गड़गड़ाहटके साथ भयंकर गर्जना करते हैं। समूची बसुधाको सुखा डालते हैं। समुद्र, नदी,
- **Translation**: 

---

### Verse 8 (Bramha 0.8328)
- **Original**: उनका आकार विशाल होता है, अपनी बिकट पर्वतीय नदी, झरने तथा पातालॉमें जो जल होता
- **Translation**: 

---

### Verse 9 (Bramha 0.8329)
- **Original**: गर्जनासे वे सम्पूर्ण आकाशको व्याप्त कर लेते हैं है, यह सब वे सुखा देते हैं। तत्पश्चात्‌ भगवानके
- **Translation**: 

---

### Verse 10 (Bramha 0.8330)
- **Original**: और मूसलाधार पानी बरसाकर त्रिलोकीके भीतर प्रभावले और सब जगहके जलका शोषण
- **Translation**: 

---

### Verse 11 (Bramha 0.8331)
- **Original**: फैले हुए उस अत्यन्त भयंकर अग्निको पूर्णरूपसे करनेसे परिपुष्ट हुईं वे सूर्यको सात रश्मियाँ सात
- **Translation**: 

---

### Verse 12 (Bramha 0.8332)
- **Original**: बुझा देते हैं। रथकी धुरीके समान स्थूल सूर्योंके रूपमें प्रकट होती हैं। उस समय ऊपर-
- **Translation**: 

---

### Verse 13 (Bramha 0.8333)
- **Original**: धाराओंकी वर्षा करते हुए सम्पूर्ण जगत्‌को नीचे सब ओर जाण्वल्यमान होकर वे सातों सूर्य
- **Translation**: 

---

### Verse 14 (Bramha 0.8334)
- **Original**: जलसे आप्लाबित कर देते हैं। सम्पूर्ण भूतलको पाताललोकसहित सम्पूर्ण त्रिलोकीकों जला डालते
- **Translation**: 

---

### Verse 15 (Bramha 0.8335)
- **Original**: जलमग्न करनेके पश्चात्‌ वे भुवलोककों भी डुयो हैं। उन तेजस्वी सूर्योकी किरणोंसे जलती हुई
- **Translation**: 

---

### Verse 16 (Bramha 0.8336)
- **Original**: देते हैं। उस समय संसारमें सब ओर अन्धकार त्रिलोकी पर्वत, नदी और समुद्र आदिके सहित
- **Translation**: 

---

### Verse 17 (Bramha 0.8337)
- **Original**: छा जाता है। चर और अचर सब नष्ट हो जाते नौरस हो जाती है। तीनों लोकोंके जल और
- **Translation**: 

---

### Verse 18 (Bramha 0.8338)
- **Original**: हैं। उस अवस्थामें ये महान्‌ संवर्तक मेघ सौ वृक्ष दग्ध हो जानेके कारण यह पृथ्वी कछुएकी
- **Translation**: 

---

### Verse 19 (Bramha 0.8339)
- **Original**: वर्षोसे अधिक कालतक वर्षा करते रहते हैं। पीठकी भाँति दिखायी देती है। द्विजवरो ! जब सारा जल सप्तर्षियोंके स्थानतक तदनन्तर भूतसर्गका संहार करनेवाले कालाग्रिरुद्र-
- **Translation**: 

---

### Verse 20 (Bramha 0.8340)
- **Original**: पहुँचकर स्थिर होता है, उस समय सप्पूर्ण रूपधारी श्रीहरि शेषनागके श्वासजनित तापसे
- **Translation**: 

---

