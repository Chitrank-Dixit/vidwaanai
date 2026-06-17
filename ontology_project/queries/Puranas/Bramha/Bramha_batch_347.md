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

### Verse 1 (Bramha 0.6921)
- **Original**: शरीर है। वे परम कान्तिमान्‌ और नाना प्रकारको विष्णुके प्रभावको सुननेमें जो तुम्हारा मन लगा
- **Translation**: 

---

### Verse 2 (Bramha 0.6922)
- **Original**: दीक्षाओंसे सम्पन्न हैं। दक्षिणा उनका हृदय है। वे है, यह बहुत बड़े सौभाग्यकी बात है। अत:
- **Translation**: 

---

### Verse 3 (Bramha 0.6923)
- **Original**: महान्‌ योगी और महायज्ञमय हैं। ठपाकर्म (वेदोंका श्रीविष्णुकी जो -जो लीलाएँ हैं, उन सबका वर्णन
- **Translation**: 

---

### Verse 4 (Bramha 0.6924)
- **Original**: स्वाध्याय) उनका हार और प्रवर्ग (एक प्रकारकी सुनो
- **Translation**: 

---

### Verse 5 (Bramha 0.6925)
- **Original**: वेदवेत्ता ब्राह्मण जिन्हें सहललमुख, सहसनेत्र,
- **Translation**: 

---

### Verse 6 (Bramha 0.6926)
- **Original**: होमाग्नि) उनका आभूषण है। नाना प्रकारके छन्‍्द सहख्रचरण, सहस्नशिरा, सहखकर, अविनाशी देव,
- **Translation**: 

---

### Verse 7 (Bramha 0.6927)
- **Original**: उनके चलनेके मार्ग हैं। गूढ उपनिषद्‌ उनके सहस्नजिह्न, भास्वानू, सहस्रमुकुट, प्रभु, सहस्नदाता,
- **Translation**: 

---

### Verse 8 (Bramha 0.6928)
- **Original**: बैठनेके लिये आसन हैं। पृथ्वोकी छायारूप पत्नी सहस्रादि, सहस्नबाहु, हवन, सबन, होता, हव्य,
- **Translation**: 

---

### Verse 9 (Bramha 0.6929)
- **Original**: सदा उनके साथ रहती हैं, वे मणिमय शिखरकी यज्ञपात्र, पवित्रक, वेदी, दीक्षा, समिधा, ख्ुवा,
- **Translation**: 

---

### Verse 10 (Bramha 0.6930)
- **Original**: भाँति पानीके ऊपर प्रकट हुए। समुद्र, पर्वत, बन स्तुकूु, सोम, सूप, मूसल, प्रोक्षणी, दक्षिणायन,
- **Translation**: 

---

### Verse 11 (Bramha 0.6931)
- **Original**: और काननोंसहित समस्त पृथ्वी एकार्णबके जलमें अध्वर्यु, सामग ब्राह्मण, सदस्य, सदन, सभा, यूप,
- **Translation**: 

---

### Verse 12 (Bramha 0.6932)
- **Original**: डूबी थी। सम्पूर्ण जगतूके आदि कारण और चक्र, ध्रुवा, दर्वी, चरु, उलूखल, प्राग्वंश, यज्ञभूमि,
- **Translation**: 

---

### Verse 13 (Bramha 0.6933)
- **Original**: सहस्नों मस्तकोंवाले भगवानने बाराहरूपमें प्रकट छोेटे-बड़े चराचर जीव, प्रायश्चित्त, अर्ध्य, स्थण्डिल,
- **Translation**: 

---

### Verse 14 (Bramha 0.6934)
- **Original**: होकर एकार्णबमें प्रवेश किया तथा सब लोकोंका कुश, मन्त्र, यज्षको वहन करनेवाले अग्निदेव,
- **Translation**: 

---

### Verse 15 (Bramha 0.6935)
- **Original**: हित करनेकी इच्छासे पृथ्वीको अपनी दाढ़पर अज्ञभाग, भागवाहक, अग्राशनभोजी, सोमभोक्ता,
- **Translation**: 

---

### Verse 16 (Bramha 0.6936)
- **Original**: उठा लिया। इस प्रकार समस्त जीवोंके हितैषी हुतार्चि, उदायुध तथा यज्ञमें सनातन प्रभु कहते हैं,
- **Translation**: 

---

### Verse 17 (Bramha 0.6937)
- **Original**: भगवान्‌ यज्ञवाराहने समुद्र-जलकों धारण करनेवाली उन श्रीवत्सचिहविभूषित देवेश्बर भगवान्‌ विष्णुके
- **Translation**: 

---

### Verse 18 (Bramha 0.6938)
- **Original**: समूची पृथ्बीका उद्धार किया। सहस्नों अवतार हो चुके है और समय-समयपर
- **Translation**: 

---

### Verse 19 (Bramha 0.6939)
- **Original**: द्विजवरों! यह वाराह-अवतारका वर्णन हुआ। होते रहते हैं। उनका जो बाराह अवतार है, वह
- **Translation**: 

---

### Verse 20 (Bramha 0.6940)
- **Original**: उसके बाद भगवान्‌का नरसिंह अवतार हुआ। बेदप्रधान यज्ञस्वरूप है। चारों वेद उनके चरण उस अवतारमें भगवान्‌ने नरसिंहरूप धारण करके और यूप उनकी दाढ़ें हैं। यज्ञ दाँत और चितियाँ हिरण्यकशिपु नामक दैत्यका वध किया था। मुख हैं। साक्षात्‌ अग्नि ही उनकी जिह्बा, कुश प्राचीन कालके सत्ययुगकी बात है, दैत्योंके रोमावलि और ब्रह्म मस्तक है। उनका तप महान्‌ , आदिपुरुष देवशत्रु बलाभिमानी हिरण्यकशिपुने है। दिन और रात्रि उनके नेत्र हैं। वे दिव्यस्वरूप
- **Translation**: 

---

