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

### Verse 1 (Vishnu Puran 0.9441)
- **Original**: 72 यथाहँ भवता सुष्टो जात्या रूपेण चेश्वर । स्वभावेन च॒ संयुक्तस्तथेदं चेट्स्ति मया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9442)
- **Original**: 73 यहद्यन्यथा प्रवर्तेये देवदेव ततो मयि। न्याय्यो दण्डनिपातो वै तवैख बचने यथा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9443)
- **Original**: छड तथाप्यज्ञे जगत्स्वामिन्दण्ड पातितवान्मयि । स इलाघ्यो5यं परो दण्डस्त्वत्तो मे नान्‍यतो वर:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9444)
- **Original**: 75 हतवीयों हतविषो दमितो5ह त्वयाच्युत । जीवित दीयतामेकमाज्ञापप करोमि किम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9445)
- **Original**: 76 औ्रीभगवानुबाच नात्र स्थेयं त्वया सर्प कदाचिद्ममुनाजले । सपुतन्नपरिवारस्त्व॑ समुद्रसलिलं.. ब्रज
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9446)
- **Original**: 77 मत्यदानि च ते सर्प दृष्टा मूर्द्धनि सागरे। गरुड: पन्नगरिपुस्त्वयि न ॒प्रहरिष्यति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9447)
- **Original**: 78 श्रीपराशर डवाच 4 इत्युक्त्वा सर्पराज ते मुमोच भगवान्हरिः । प्रणष्य सो5पि कृष्णाय जगाम पयसां निधिम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9448)
- **Original**: 79 पह्यतां सर्वभूतानां सभृत्यसुतबान्धव: । समस्तभार्यासहित: परित्यज्य स्वकं हृदम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9449)
- **Original**: 80 गते सर्पे परिष्रृज्य मृत पुनरिवागतम्‌। गोपा मूर्द्धनि हार्देन सिषिचुरनेत्रजैर्जकः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9450)
- **Original**: 89 कृष्णमक्लिप्टकर्माणमन्ये. विस्मितचेतस: । तुष्ठुवुर्मुदिता गोपा दृष्ठा शिवजलां नदीम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9451)
- **Original**: 82 गीयमान: स गोपीभिश्चरितैस्साधुचेष्टितैः । संस्तूयमानो गोपैश्ञ कृष्णो ब्रजमुपागमत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9452)
- **Original**: 83 सर्वथा असमर्थ हूँ, मेरी चित्तवृत्ति तो केवल आपकी कृपाकी ओर ही लगी हुई है, अतः आप मुझपर असन्न होइये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9453)
- **Original**: हे केद्ञाथ ! मेरा जिसमें जन्म हुआ है बह सर्पजाति अत्यन्त क्रूर होती है, यह मेरा जातीय स्वभाव है । है अच्युत ! इसमें मेरा कोई अपराध नहीं है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9454)
- **Original**: इस सम्पूर्ण जगत॒की रचना और संहार आप हो करते हैं। सैसारकी रचनाके साथ उसके जाति, रूप और स्वरभावोंको भी आप ही बनाते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9455)
- **Original**: है ईश्वर ! आपने मुझे जाति, रूप और स्वभावसे युक्त करके जैसा बनाया है उसीके अनुसार मैंने यह चेष्टा भी को है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9456)
- **Original**: है देवदेव ! यदि मेरा आचरण विपरीत हो ठब तो अवश्य आपके कथनानुसार मुझे दण्ड देना उचित है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9457)
- **Original**: तथापि हे जगत्स्वापिन्‌ ! आपने मुझ अज्ञको जो दण्ड दिया है बह आपसे मिला हुआ दण्ड पेंरे लिये कहीं अच्छा है, किन्तु दूसरेक््र बर भी अच्छा नहीं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9458)
- **Original**: हे अच्युत ! आपने मेरे पुरुषार्थ और विषको नष्ट करके मेश भली प्रकार मानमर्दन कर दिया है । अब केवल मुझे प्राणदान दीजिये और आज्ञा कोजिये कि मैं क्या करूँ 7
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9459)
- **Original**: श्रीभगवान्‌ बोले--है सर्प! अब तुझे इस यमुनाजलमें नहीं रहना चाहिये । तू द्घ्र ही अपने पुत्र और परिवारके सहित समुद्रके जलमें चला जा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9460)
- **Original**: तेरे मस्तकपर मेरे चरण चिह्ोंको देखकर समुद्रमें रठते हुए भी सर्पोंका शत्रु गरुड तुझपर प्रहार नहीं करेगा
- **Translation**: 

---

