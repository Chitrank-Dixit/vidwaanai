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

### Verse 1 (Vishnu Puran 0.1101)
- **Original**: उनके घरमें निर्धनता कभी नहीं रह सकेगी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1102)
- **Original**: >जू-_->ऊ>, है जी इति श्रीविष्णुपुराणे प्रथमेंड्ञों नवमो5ध्याय:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1103)
- **Original**: बज औ ॑॑+न दसवाँ अध्याय भूगु, अभि और अभ्रिष्वात्तादि पितरॉकी सनन्‍्तानका वर्णन श्रीमेत्रेय उवाच कथित मे त्वया सर्व यत्पृष्टोडईसि मया मुने । भृगुसगगाँठ्मभृत्येष सर्गो मे कथ्यतां पुनः:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1104)
- **Original**: 1 अपरशर उवाच भृगोः स्थात्यां समुत्यन्ना रक्ष्मीर्विष्णुपरिग्रह: । तथा धातृविधातारी ख्यात्यां जाती सुतो भूगो:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1105)
- **Original**: 2 भारये धातृविधात्रोस्ते तयोर्जातों सुतावुभौ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1106)
- **Original**: 3 प्राणश्जैव मृकण्डुश्ष मार्कण्डेयो मृकण्डुत: । ततो वेदशिरा जज्ञे प्राणस्यापि सुतं श्रूणु
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1107)
- **Original**: 4 प्राणस्य॒ दुतिमान्पुन्नो राजबांश्न ततो5भवत्‌ । ततो वँशों महाभाग विस्तरं भार्गवो गत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1108)
- **Original**: 5 पत्नी मरीचे: सम्भूति: पौर्णमासमसूयत
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1109)
- **Original**: विरजाः पर्वतश्लैज तस्थ पुत्रों महात्ममः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1110)
- **Original**: 6 वंशसंकीर्तने पुत्रान्वदिष्ये5ह॑ततो द्विज । स्मृतिश्राड्टिरिस: पत्नी प्रसूता कन्यकास्तथा । सिनीबाली कुहृझ्षैव राका चानुमतिस्तथा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1111)
- **Original**: 7 अनसूया तथैवात्रेर्जज्े निष्कल्मषान्सुतान्‌। सोम॑ दुर्वाससं चैव दत्तात्रेय नर योगिनम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1112)
- **Original**: 8 प्रीत्यां पुलस्त्यभार्यायां दत्तोलिस्तत्सुतो5भवत्‌ । पूर्वजन्मनि यो5गस्त्य: स्मृत: स्वायम्भुवेउन्तरे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1113)
- **Original**: 9 कर्दमश्षोर्वरीयांश्व॒सहिष्णुश्न॒सुताखय: । क्षमा तु सुषुवे भार्या पुलहस्य प्रजापतेः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1114)
- **Original**: 10 श्रीमैत्रेयजी ओले--हे मुने ! मैंने आपसे जो कुछ पूछा था बह सब आपने वर्णन किया: अब भृगुजीकी सन्‍्तानसे लेकर सम्पूर्ण सृष्टका आप मुझसे फिर वर्णन क्यैजिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1115)
- **Original**: श्रीपराशस्जी खोले--भृगूजीके द्वारा ख्यातिसे विष्णुपल्री लक्ष्मीजी और घाता, विधाता नामक दो पुत्र उत्पन्न हुए
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1116)
- **Original**: महात्मा मेरूकी आयति और नियति- नाप्नी कन्याएँ घाता और विधाताकी र्तियाँ थीं; उनसे उनके प्राण और मुकण्डु नामक दो पुत्र हुए । मुकप्ड्से मार्कप्डेय और उनसे वेदशिराका जन्म हुआ। अब प्राणकी सन्तानका वर्णन सुनो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1117)
- **Original**: प्राणका पुत्र द्युतिमान्‌ और उसका पुत्र राजवान्‌ हुआ। हे महाभाग ! उस राजवानसे फिर भृगुबंशका बड़ा विस्तार हुआ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1118)
- **Original**: मरीचिकी पत्नी सम्भूतिने पौर्णमासक्वे उत्पन्न किया । उस महात्माके विस्जा और पर्वत दो पुत्र थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1119)
- **Original**: हे द्विज ! उनके लंद्ठाका वर्णन करते समय मैं उन दोनॉकी सन्तानका वर्णन करूँगा । अगिराकी पत्नी स्मृति थी, उसके सिनीवाली, कुह्दू, गका और अनुमति नामकी कन्याएँ हुई
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1120)
- **Original**: अतन्रिकी भार्या अनसूयाने चन्द्रमा, दुर्वासा और योगी दत्ताज्रेय--इन निष्पाप पुत्रोंको जन्म दिया
- **Translation**: 

---

