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

### Verse 1 (Vishnu Puran 0.1121)
- **Original**: पुलस्त्यकी स्त्री प्रीतिसे दत्तोलिका जन्म हुआ जो अपने पूर्व जन्ममें स्वायम्भुव मन्वन्तरमें अगस्त्य कहा जाता था
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1122)
- **Original**: प्रजापति पुलहकी पत्नी क्षमासे कर्दम, उर्वरीयान्‌ और सहिष्णु ये तीन पुत्र हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1123)
- **Original**: डु0 क्रतोश्न सन्ततिर्भा्या वालखिल्यानसूयत । षष्टिफुन्‍सहस्नाण. मुनीनामूर्ध्वरेतसाप्‌ । अड्जुष्ठपर्वमात्राणां ज्वलद्धास्करतेजसाम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1124)
- **Original**: 11 ऊर्जायां तु बसिष्ठस्य सप्ताजायन्त बै सुता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1125)
- **Original**: 12 रजो मोत्रोर्द्धतबाहुश्न॒ सवनश्चानघस्तथा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1126)
- **Original**: सुतपाः शुक्र इत्येते सर्वे सप्तर्षयोउमला:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1127)
- **Original**: 13 योउसावम्यभिमानी स्याद ब्रह्मणस्तनयो5प्रज: । तस्मात्खाहा सुताँल्‍लेभे त्रीनुदारौजसो द्विज
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1128)
- **Original**: 14 पावकं पवमान तु शु्चिं चापि जलाशिनम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1129)
- **Original**: 15 तेषां तु सन्‍्ततावन्ये चत्वारिशध् पल्ञ चल । कथ्यन्ते वह्ययश्चैते पितापुत्रत्रयं च यत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1130)
- **Original**: 16 एबमेकोनपश्चाशहद़्य: परिकीर्तिता:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1131)
- **Original**: 17 पितरो ब्रह्मणा सुष्टा व्याख्याता ये मया द्विज । अम्रिष्वात्ता बर्हिषदोइनम्यः साम्रवश्च बे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1132)
- **Original**: 18 तेध्य: स्वधा सुते जज्ञे मेनां वै धारिणीं तथा । ते उभे ब्रह्मवादिन्यों योगिन्याबष्युभे द्विज
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1133)
- **Original**: 19 उत्तमज्ञानसम्पन्ने सर्व: समुदिलैर्गुणैः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1134)
- **Original**: 20 इत्येषा दक्षकन्यानां कथितापंत्यसन्तति:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1135)
- **Original**: श्रद्धावान्संस्मरन्नेतामनपत्यों न जायते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1136)
- **Original**: 29 प्रीविष्णुपुराण [ अ* 11 क्रतुकी सन्तति नामक भार्याने अँगूठेके पोरुओऑंके समान शरीरवाले तथा प्रखर सूर्यके समान तेजस्वो वालखित्यादि साठ हजार ऊर्ध्यरिता मुनियोक्त्रे जन्म दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1137)
- **Original**: बसिष्ठकी ऊर्जा नामक खोसे रज, गोत्र, ऊर्ध्वबाहु, सवन, अनथ, सुतपा और शुक्र ये सात पुत्र उतान्न हुए । ये निर्मल स्वभाववाले समस्त मुनिगण [तीसरे मन्वन्तरमें] सम्रर्थि हुए
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1138)
- **Original**: है द्विज ! अग्रिका अभिमानी देव, जो त्रह्माजीका ज्येष्ठ पुत्र है, उसके ड्वारा स्वाह्म नामक पलीसे अति तेजस्वी पावक, पवमान और जल्कों भक्षण करनेवाला शुचि--ये तीन पुत्र हुए
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1139)
- **Original**: इन तीनोंके (प्रत्येकके प्रह-पन्द्रह पुत्रके क्रमसे] पैंतालीस सन्तान हुईं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1140)
- **Original**: पिता अप्रि और उसके तीन पुओ्रेंको मिलाकर ये सब अग्रि हो कहलाते हैं । इस प्रकार कुल उनचास (49) अग्रि कहे गये हैं
- **Translation**: 

---

