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

### Verse 1 (Vishnu Puran 0.5701)
- **Original**: मृतकके कुट्ुम्बका अन्न दस दिनतक न खाना चाहिये तथा अशौच कालमें दान, परिग्रह, होम और स्वाभ्याय आदि कर्म भी न करने चाहिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5702)
- **Original**: यह [दस दिनका) अज्ञौव ब्राह्मणका है; क्षत्रियकर अज्ञौद बारह दिन और वैश्यका पद्रह दिन रहता है तथा अर्धमासं तु बैश्यस्य मास शूद्रस्थ शुद्धये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5703)
- **Original**: शुद्रका अशौच-शुद्धि एक मासमें होती है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5704)
- **Original**: + अर्थात्‌ हमत्मेग अगुक नाग गोत्रवाले प्रेतके निमित, ये जहाँ कहीं भी हों, यह जल देते हैं । + समानोदक (तर्पणादिमें समान जत्माथिकारी अर्थात्‌ सगोत्र) और संफिष्ड (पिण्डाधिन्तरी) ज्ती न्याख्या कूर्मपुणमें इस प्रकार की है-- 'सपिप्डता हु पुरुष सप्तमे बिनिवर्तते।समानोंदकर्भावस्तु ऊन्मनाम्रोस्वेदने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5705)
- **Original**: अधांत--सातनीं पोड़ीगें पुरुषकी सपिण्डता नियूतत हो जाती है फिल्तु समानोदकभाव उसके जन्प और नामका पता न रहनेपर दूर होता है। £ परत्तु माला-पिताके विज्यमें यह नियम नहीं है; जैसा कि कहा है-- पिठये ज्यृतो स्थाता दूसस्थो5पि हि पुत्रकः । श्रुत्वा तद्दिनमारध्य दशाहे सृतकी भवेत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5706)
- **Original**: आ> 13 ] अयुजो भोजयेत्कामं द्विजानन्ते ततो दिने । दद्याद्रेंषु पिण्डं चर प्रेतायोच्छिप्टसब्निधौं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5707)
- **Original**: 20 वार्यायुथप्रतोदास्तु दण्डश्र द्विजभोजनात्‌ । स्प्रष्टव्योउनन्तरं वर्ण: शुद्धेरन्ते ततः क्रमात्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5708)
- **Original**: 21 ततस्स्ववर्णधर्मा ये विप्रादीनामुदाहता: । तान्कुर्बीत पुपाञ्जीवेश्निजघर्मार्जनैस्तथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5709)
- **Original**: 22 मृताहनि चर कर्तव्यमेकोहिष्टमत: परम्‌। आह्वानादिक्रियादेवनियोगरहित हि तत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5710)
- **Original**: 23 एकोउर्ध्यस्तत्र॒दातव्यस्तथैवैंकपवित्रकम्‌ । प्रेताय पिण्डो द्वतव्यो भुक्तवत्सु द्विजातियु
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5711)
- **Original**: 24 प्रश्कक्ष तत्राभिरतिर्यजमानै्दिजन्मनाम्‌ । अक्षय्यममुकस्येति वक्तव्य विरतो तथा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5712)
- **Original**: 25 एकोट्िप्टमयो धर्म इत्थमावत्सरात्स्मृत: । सपिण्डीकरणं तस्मिन्काले राजेन्द्र तच्छुणु
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5713)
- **Original**: 26 एकोहिष्टविधानेन कार्य तदपि पार्थिव । संवत्सरे5थ षट्ठे वा मासे वा द्वादशे हि तत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5714)
- **Original**: 27 तिलगन्धोदकैर्युक्ते तत्र पात्रचतुष्टयम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5715)
- **Original**: 28 पात्र॑ प्रेतस्थ तम्नैक पैजत्रें पात्रत्रयं तथा। सेचयेत्पितृपात्रेषु. प्रेतपात्रं ततसख्त्रिषु
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5716)
- **Original**: 29 ततः पितृत्वमापन्ने तस्मिग्प्रेले महीपते। श्राद्धूधरमैरशेषैस्तु. तत्पूर्वानर्चयेत्पितृन्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5717)
- **Original**: 30 पुत्र: पौत्र: प्रषोत्रो वा भ्राता वा भ्रातृसन्तति: । सपिण्डसन्ततिर्वापि क्रियाहों नृप जायते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5718)
- **Original**: 39 तेषामभावे सर्वेषां समानोदकसन्तति: । मातुपक्षसपिण्डेन सम्बद्धा ये जलेन वा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5719)
- **Original**: 32 कुलद्ये5पि चोक्तिन्ने ख्रीभि: कार्या: क्रिया नूप
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5720)
- **Original**: 33 सद्लतान्तर्गतैर्बापि कार्या: प्रेतस्थ चक्रिया: । उत्सन्नबन्धुरिक्थाद्या. कारयेदवनीपति:
- **Translation**: 

---

