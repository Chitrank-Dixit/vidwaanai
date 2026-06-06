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

### Verse 1 (Vishnu Puran 0.2481)
- **Original**: 39 विद्याबुद्धिरविद्यायामज्ञानात्ताता जायते । तत्कर्म यन्न बन्धाय सा विद्या या विमुक्तये । आयासायापर कर्म विद्यान्या शिल्पनैपुणम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2482)
- **Original**: 49 तदेतदवगम्याहमसारं सारमुत्तमम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2483)
- **Original**: निशामय महाभाग प्रणिपत्य ब्रवीमि ते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2484)
- **Original**: 42 न चिन्तयति को राज्य को धन नाभिवाज्छति । तथापि भाव्यमेवेतदुभर्य॑ प्राप्यते नरें:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2485)
- **Original**: 43 सर्व एव महाझाग महत्त्वं प्रति सोह्यमा: । तथापि घुसा भाग्यानि नोद्यमा भूतिहेतवः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2486)
- **Original**: 4ड जडानामविवेकानामश्राणामपि_ प्रभो। बआाग्यधोज्यानि राज्यानि सन्तयनीतिमतामपि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2487)
- **Original**: 45 तस्माद्यतेत पुण्येषु य इच्छेन्पहतीं श्रियम्‌ । यतितव्य समत्वे च निर्वाणमपि चेच्छता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2488)
- **Original**: 46 कैसे निकाले ?
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2489)
- **Original**: यह सब तथा और भी जो कुछ तूने पढ़ा हो वह सब मुझे सुना, मैं तेरे मनके भावोंकों जाननेके लिये बहुत उत्सुक हूँ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2490)
- **Original**: श्रीपराहरजी कोले--तब विनयभूषण प्रह्लादजीने पिताके चरणोंगें प्रणाग कर दैत्यराज हिरण्यकशिपुरों हाथ जोड़कर कहा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2491)
- **Original**: प्रद्धादजी खोले--पिताजी ! इसमें सन्देह नहों, गुरुजोने तो मुझे इन समी विषयोंकी शिक्षा दी है, और में उच्हें समझ भी गया हूँ; परत्तु मेरा विचार है कि वे नीतियाँ अच्छी नहीं हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2492)
- **Original**: साम, दान तथा दण्ड और ग्रेद--ये सब उपाय मिऋ्रदिके साधनेके छिये बतत्खये गये हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2493)
- **Original**: किन्तु, पिताजी ! आप क्रोध न करें, मुझे तो कोई झत्रु-मित्र आदि दिखायी ही नहीं देते; और हे महायाहो ! जब कोई साध्य ही नहीं है तो इन साधनोंसे लेना ही क्‍या है?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2494)
- **Original**: हे तात ! सर्वभूतात्गक जगन्नाथ जगच्मय परमात्मा गोविन्दमें भत्त्र शत्रु-मित्रकी बात डी कहाँ है 7
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2495)
- **Original**: भगवान्‌ तो आपमें, मुझमें और अन्यत्र भी सभी जगह वर्तमान हैं, फिर 'यह मेरा पित्र है और यह दाल्रु है' ऐसे भेदभावको स्थान ही कहाँ है 2
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2496)
- **Original**: इसलिये, हे तात ! अविद्याजन्य दुष्कर्मोंमें प्रवत्त करनेवाऊे इस बाग्जालको सर्वथा छोड़कर अपने शुभके छिये ही यत्न करना चाहिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2497)
- **Original**: हे दैत्यराज ! अज्ञानके कारण हो मनुष्योंकी अलिशाामे दिद्या बुद्धि होती है। बालक क्या अज्ञानबद्ा लथोतको ही आंग्र नहों समझ लेता ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2498)
- **Original**: कर्म वहां है जो बन्धनका कारण न हो और विद्या भी वही है जो मुक्तिकी साधिका हो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2499)
- **Original**: इसके अतिरिक्त और कर्म तो परिश्रमरूप तथा अन्य विद्या कला कौदलमात्र ही हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2500)
- **Original**: है महाभाग ! इस प्रकार इन सखको असार समझकर अब आपको प्रणाम कर मैं उत्तम सार बतल्मता हूँ, आप श्रवण फीजिये
- **Translation**: 

---

