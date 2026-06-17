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

### Verse 1 (Vishnu Puran 0.4121)
- **Original**: 3 भस्तः स महीपाल: शालग्रामेश्वसत्किल । योगयुक्त: समाधाय बासुदेबे सदा मन:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4122)
- **Original**: 4 पुण्यदेज्ञप्रभावेण ध्यायतश्न सदा हरिम्‌। कर्थ तु ना3भवन्युक्तियदभूत्स द्विज: पुन:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4123)
- **Original**: 5 विप्रत्वे च कृत॑ तेन यद्भुयः सुमहात्पना । भ्रस्तेन मुनिश्रेष्ठ तत्सर्व॑ वक्तुमहसि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4124)
- **Original**: 6 औपरराझर उताच आालग्रामे महाभागो भगवज््यस्तमानस: । स उवास चिरं काल मैत्रेय पृथिवीपति:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4125)
- **Original**: 7 अहिंसादिषृश्नेषेषु गुणेषु गुणिनां वर: । अबाप परमां क्राष्ठां मनसश्चापि संयमे । 8 चज्ञेशाच्युत गोविन्द माधवानन्त केशव । कृष्ण विष्णो हृषीकेश बासुदेव नमोउस्तु ते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4126)
- **Original**: 9 डति राजाह भरतों हरेनामानि केवलम्‌। नान्यज्जगाद मैत्रेय किद्धित्स्वप्नान्तरेषपि च । एतत्पदत्तदर्थ च बिना नान्यदचिन्तयत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4127)
- **Original**: 10 समित्पुष्पकुशादानं॑ चक्रे देवक्रियाकृते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4128)
- **Original**: नान्यानि चक्रे कर्माणि निस्सड़ो योगतापसः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4129)
- **Original**: 11 जगाम सो5भिषेकार्थमेकदा तु महानदीम्‌ । सस्त्रौ तत्र तदा चक्रे स्त्रानस्थानन्तरक्रिया:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4130)
- **Original**: 12 अथाजगाम तत्तीर॑ जले पातुं पिपासिता । आससन्नप्रसवा ब्रह्मत्नेंकक हरिणी वनात्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4131)
- **Original**: 13 कुछ पूछा था सो सब आपने वर्णन कर दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4132)
- **Original**: उसके साथ ही आपने यह भी बतला दिया कि किस प्रकार यह समस्त त्रित्त्ेकी भगवान्‌ विष्णुके ही आश्रित है और कैसे परमार्थस्वरूप ज्ञान ही सबमें प्रधान है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4133)
- **Original**: किन्तु भगवन्‌ ! आपने पहले जिसकी चर्चा की थीं वह राजा भरतका चरित्र मैं सुनना चाहता हूँ, कृपा करके कहिये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4134)
- **Original**: कहते हैं, वे राजा भरत निरन्तर योगयुक्त होकर भगवान्‌ वासुदेवमं चित्त लगाये शालगम क्षेत्रमें रहा करते थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4135)
- **Original**: इस प्रकार पुण्यदेशके प्रभाव और हरि- चिन्तनसे भी उनकी मुक्ति क्यों नहीं हुईं, जिससे उन्हें फिर ब्राह्मणका जन्म लेना पड़ा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4136)
- **Original**: हे सुनिश्चेष्ठ ! ब्राह्मण होकर भी उन महात्मा भरतजीने फिर जो कुछ किया बह सब्र आप कृपा करके मुझसे कहिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4137)
- **Original**: श्रीपराशरजी बोल्ले--हें मैत्रेय! वे महाभाग पृथिवोपति भरतजी भगवानूमें चित्त छगाये चिरकाछ््तक शाल्पग्रामक्षेत्रमें रहे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4138)
- **Original**: गुणवानोमें श्रेष्ठ उन भरतजीने अहिंसा आदि सम्पूर्ण गुण और मनके संयममें परम उत्कर्ष लाभ किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4139)
- **Original**: हे यज्ञेश ! हे अच्युत ! हे गोविन्द ! है माधव ! हे अनन्त ! है केशव ! हे कृष्ण ! हे विष्णो ! है इषोकेशा ! हे वासुदेव ! आपको नमस्कार है'--इस प्रकार राजा भरत निरन्तर केवछ भगवन्नामोंका हो उच्चारण किया करते थे। हे मैत्रेय ! थे स्वप्तमें भी इस पदके अतिरिक्त और कुछ नहीं कहते थे और न कभी इसके अर्थके अतिरिक्त और कुछ चिन्तन हो करते थे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4140)
- **Original**: के निःसंग, योगयुक्त और तपस्वी राजा भगवानूव पूजाके लिये केवऊ समिघ, पुष्प और कुशाका ही सझय करते थे। इसके अतिरिक्त ने और कोई कर्म नहीं करते थे
- **Translation**: 

---

