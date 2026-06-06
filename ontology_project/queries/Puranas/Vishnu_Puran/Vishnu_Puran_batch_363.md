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

### Verse 1 (Vishnu Puran 0.7241)
- **Original**: श्जा बोले--“'पैंने समस्त झत्रुओंकों जीत लिया है, मेरी इन्द्रियोंकी सामर्थ्य नष्ट नहीं हुई है, मैं बन्चुजन, असंख्य सेना और कोदासे भी सम्पन्न हूँ, इस समय उर्वशीके सहवासके अतिरिक्त मुझे और कुछ भी प्राप्तव्य नहों है । अतः मैं इस डर्वशीके साथ ही काछ-यापन करना चाहता हूँ।" राजाके ऐसा कहनेपर गन्धर्योंनि उन्हें एक अभ्रिस्थाली (अग्नियुक्त पात्र) दी और कहा-- “इस अग्निके जैदिक विधिसे गारईपल्य, आहवनीय और दक्षिणाप्रिकृप तीन भाग करके इसमें उर्वज्ञीके सहकसकी कामनासे भव्जैभाँति यजन करो तो अवदय हो तुम अपना अभीष्ट प्राप्त कर स्थ्रेगे।” गन्ध्वोकि ऐसा कहनेपर राजा उस अम्रिस्थालीको लेकर चल दिये।
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7242)
- **Original**: 76--78
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7243)
- **Original**: [मार्गमें] बनके अन्दर उन्होंने सोचा--'अहो ! मैं कैसा मूर्ख हूँ ? सैंने यह क्या किया जो इस अग्रिस्थालीको तो ले आया और उर्वश्ीको नहीं स्थया'
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7244)
- **Original**: ऐसा सोचकर उस अग्रिस्थाल्गैको बनमें हो छोड़कर ने अपने नगरमें चले आये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7245)
- **Original**: आधीणशत बोत जानेके बाद निद्रा टूटमेपर राजाने सोचा--
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7246)
- **Original**: अ“र्वशीकी सन्निधि प्राप्त करनेके लिये हो गन्चबोनि मुझे वह अग्रिस्थाली दी थी और मैंने उसे वनमें ही छोड़ दियां
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7247)
- **Original**: अतः अब मुझे उसे लानेके लिये जाना चाहिये' ऐसा सोच उठकर ये वहाँ गये, किन्तु उन्होंने उस स्थाल्बैको बहाँ न देखा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7248)
- **Original**: अग्रिस्थाल्गेके स्थानपर राजा पुरूरवाने एक ज्ञामीगर्भ पीपलके वृक्षकों देखकर सोचा--
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7249)
- **Original**: "मैंने यहीं तो बह अग्रिस्थाली फेंकी थी। बह स्थाली ही शामीगर्भ पीपल हो गयी है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7250)
- **Original**: अतः इस अग्रिरूप अश्वत्थको ही अपने नगरमें ले जाकर इसकी अर्रण बनाकर उससे उत्पन्न हुए अग्रिकी ही उपासना करूँ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7251)
- **Original**: ऐसा सोचकर राजा उस्र अधत्थकों लेकर अपने नगरमें आये और उसकी अणणि बनायी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7252)
- **Original**: तदनन्तर उन्होंने उस काप्ठको एक-एक अँगुल करके गायत्री-मन्त्रका पाठ किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7253)
- **Original**: आ*छ ] चतुर्थ अंज् 279 पठत: तत्राभिं निर्मध्याप्रिन्नयमाप्तायानुसारी भूत्वा जुहाब
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7254)
- **Original**: उर्वशीसालोक्य फलमभि- संहितवान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7255)
- **Original**: तेनैब - चामप्रिविधिना बहुविधान्‌ वज्ञानिष्ठा गान्धर्वत्त्ेकानवाप्योर्बश्या सहावियोगमवाप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7256)
- **Original**: एको5ग्रिरादावभवत्‌ एकेन त्वत्र मन्वन्तरे त्रेधा प्रवर्तिता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7257)
- **Original**: आक्षरसंख्यान्येवाज़ुल्ान्यरण्यभवत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7258)
- **Original**: उसके पाठसे गायत्रीकी अक्षर-संख्याके बरायर एक-एक अंगुल्की अरणियाँ हो गयीं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7259)
- **Original**: उनके मन्थनसे तीनों प्रकारके अभ्रियोंको उत्पन्न कर उनमें वैदिक विधिसे हवन किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7260)
- **Original**: तथा उर्वशीके सहयासरूप फलकी इच्छा की
- **Translation**: 

---

