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

### Verse 1 (Vishnu Puran 0.6481)
- **Original**: भो भो क्षत्रियवर्यास्माभिरभ्यर्थितेन भवतास्माक- मरातिवधोद्यतानां कर्तव्य॑ साहाय्यमिच्छाम- स्तद्भ॒बतास्माक्रमभ्यागतानां प्रणयभड्ढो न कार्य इत्युक्त: पुरञझ्रयः प्राह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6482)
- **Original**: त्ैलोक्यनाथो योडयं : शातक्रतुरस्थ यचयहं स्कन्चाधिरूढो युध्माकमरातिभिस्सह योत्स्पे तदहं भवतां सहाय: स्थाम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6483)
- **Original**: कुर्व अं 233 अड़तालीस दक्षिणापथके शासक हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6484)
- **Original**: 12--ह14
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6485)
- **Original**: इक्ष्वाकुने अष्टकाश्राद्धक्षा आरम्भ कर अपने पुत्र विकुक्षिकों आज्ञा दी कि आद्धके योग्य मांस क्नओ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6486)
- **Original**: उसने 'बहुत अच्छा' कह उनकी आज्ञाको शिरोधार्य किया और घनुष-बाण लेकर बनमें आ अनेक्यों मुगॉका वध कारण विकुद्धिने उनमेंसे एक शणक (खरगोश) खा लिया और बचा हुआ मांस ल्त्रकर अपने पिताको निवेदन क्रिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6487)
- **Original**: उस मांसका प्रोक्षण करनेके लिये प्रार्थना किये जानेपर इक्ष्वाकुक॑ कुल-पुरोह्ित असिष्ठजीने कहा--''इस अपवचित्र मोसकी क्या आयश्यकता है ? तुम्हारे दुरात्मा पुतने इसे भ्रष्ट कर दिया है, क्योंकि उसने इसमेंसे एक डाइक खा लिया है”
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6488)
- **Original**: गुरुके ऐसा कहनेपर, तभीसे विकुक्षिका नाम झाह्ाद पड़ा और पिताने उसको स्याग दिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6489)
- **Original**: पिताके मरनेके अनन्तर उसने इस पृथिवीका घर्मानुसार शासन किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6490)
- **Original**: उस शञ्ञादके पुरञ्ञय नामक पूत्र हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6491)
- **Original**: पुरक्षबक्ता भी यह एक दूसरा नाम पड़ा--
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6492)
- **Original**: पूर्वकाल्में त्रेतायुगमें एक बार अति भीषण देवासुरसंग्राम हुआ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6493)
- **Original**: उसमें महाबलबान्‌ दैत्यगणसे पराजित हुए देवताओंने भगवान्‌ विष्णुकी आराधना की
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6494)
- **Original**: तथ आदि-अन्त-शुन्य, अवोष जगल्मतिपाऊक, श्रीनारायणने देवताओंसे प्रसन्न होकर कहा---
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6495)
- **Original**: “'आप- स्त्रेगॉंका जो कुछ अभी है वह मैंने जान ल्थया है। उसके विषयमें यह यात सुनिये--
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6496)
- **Original**: राजर्षि शशादका जो पुरक्षय नामक पुत्र है उस क्षत्रियश्रेष्ठके झरीरमें मैं अश्मात्रसे स्वयं अवतीर्ण होकर उन सम्पूर्ण दैल्योंका नाहा करूँगा। अतः तुमल्तेग पुर्षयकों टैत्योंके वधके लिये तैयार करो''
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6497)
- **Original**: यह सुनकर देवताओनि विष्णुभगवानको प्रणाम किया और पुरक्षयके पास आकर उससे कहां---
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6498)
- **Original**: “हे क्षत्रियश्रेष्ट
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6499)
- **Original**: हमलोग चाहते हैं कि अपने झात्रुओंके बधमें प्रकृत हमलोगोंक्री आप सहायता करें। हम अभ्यागत जनोंका आप मानभंग न करें ।” यह सुनकर पुरझयने कहा--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6500)
- **Original**: “ये जो जैलोक्यनाथ शतक़दु आपसल्टेगोके इन्द्र हैं यदि मैं इनके कन्धेपर चढ़कर आपके जत्ुओंसे युद्ध कर सकूँ तो आपलोगोंका सहायक हो सकता हूँ”
- **Translation**: 

---

