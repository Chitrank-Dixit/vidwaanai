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

### Verse 1 (Vishnu Puran 0.5001)
- **Original**: 28 आयुर्वेदो धनुर्वेदो गान्धर्वश्षेव ते त्रयः । अर्थशार्त्रं चतुर्थ तु विद्या ह्ाष्टादशैव ता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5002)
- **Original**: 29 ज्ञेया ब्रह्मर्षय: पूर्व तेभ्यो देवर्षय: पुनः । राजर्षय: पुनस्तेभ्य ऋषिप्रकृतयस््रय:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5003)
- **Original**: 30 इति झाखास्समाख्याताशशाखाभेदास्तथैव च। कतरश्चैब झास्तानां भेव्ह्ेतुस्तथोदित:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5004)
- **Original**: 39 सर्वमन्वन्तरेष्रेब शास्वराभेदास्समा: स्मृता: । प्राजापत्या श्रुतिर्नित्या तहिकल्पास्त्िमे द्विज
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5005)
- **Original**: 32 एतत्ते कथित सर्व यत्पृष्टोडहमिह त्वया। मार्कप्डेय है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5006)
- **Original**: इसी प्रकार आठनाँ आग्रेय, नवाँ भविष्यत्‌, दसवाँ त्रह्मवैकर्त और ग्यारहवाँ पुराण लैज़ कहा जाता ऐै
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5007)
- **Original**: तथा ब्ारहवाँ याराह, तेरहयाँ स्कात्द, चौदहताँ वामन, पद्धहवाँ कौर्म तथा इनके पश्चात्‌ मात्स्य, गारुढ़ और ग्रह्माण्डपुराण हैं। हे महाम॒ने ! ये हो अठारह महापुराण हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5008)
- **Original**: इनके अतिरिक्त मुनिजनोनि और भी अनेक उपपुराण बतस्म्ये हैं। इन सभीमें सृष्टि, प्रकय, देवता आदिकोंके बंद, मन्वन्तर गया है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5009)
- **Original**: है मैत्रेय ! जिस पुराणको मैं तुम्हें सुना रहा हूँ वह पाद्मपुराणके अनन्तर कहा हुआ वैष्णव नामक महापुराण है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5010)
- **Original**: हे साधुश्रेष्ठ ! इसमें सर्ग, प्रतिसर्ग, वंश और मन्वन्तरादिका वर्णन करते हुए सर्वत्र केवल विष्णु- भगवानका ही वर्णन किया गया है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5011)
- **Original**: छः: बेदाड़, चार वेद, मीमांसा, न्याय, पुणण और धर्मझाख्र--ये हो चौदह बिद्याएँ हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5012)
- **Original**: इन्हींमें आयुर्वेद, धनुर्वेद और गान्धर्व इन तीनोंक्य्रे तथा चौथे अर्थजास्त्रको मिल्य लेनेसे कुल अठारह विद्या हो जाती है। ऋषियोंके तीन भेद हैं--प्रथम बद्मर्षि, द्वितीय देवर्षि और फिर राजर्षि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5013)
- **Original**: इस प्रकार मैंने तुमसे केदोंकी शाखा, शाखाओंके भेद, उनके स्चयिता तथा शाखा-भेदके कारणोंका भी सर्णन कर दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5014)
- **Original**: इसी प्रकार समस्त मन्वन्तरोंमें एक-से शाखाभेद रहते हैं; हे द्विज
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5015)
- **Original**: प्रजापति ब्रह्माजोसे प्रकट होनेवास्प्रै श्रुति तो नित्य है, ये तो उसके विकल्पमात्र हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5016)
- **Original**: हे मैत्रेय ! येदके सम्बन्धें तुमने मुझसे जो कुछ पूछा था बह मैंने भैत्रेय वेदसम्बन्ध: किमन्यत्कथयामि ते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5017)
- **Original**: सुना दिया; अब और क्या कहूँ ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5018)
- **Original**: हे व कि 7 कम ल्‍ा इति श्रीविष्णुपुराणे तृतीयेंडशे षष्ठोउध्यायः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5019)
- **Original**: का जः ल्नज- ता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5020)
- **Original**: अण्7 ) 02 तृतीयअश रृः॑ःऋ र79 सातवाँ अध्याय खमगीता अमैत्रेय उवाच श्रीमैत्रेयजी बोले--हे गुरों ! मैंने जो कुछ पूछा था यथावत्कथितं सर्व यत्पृष्येउसि मया गुरो । वह सब आपने यथावत्‌ वर्णन किया । अब मैं एक बात श्रोतुमिच्छाम्यहं त्वेके तद्धवाग्रत्रवीतु मे
- **Translation**: 

---

