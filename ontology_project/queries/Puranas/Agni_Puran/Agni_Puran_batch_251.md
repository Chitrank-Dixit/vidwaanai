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

### Verse 1 (Agni Puran 0.5001)
- **Original**: *जो कृष्माण्ड, यक्ष, राक्षस, प्रेत, विनायक, क्रूर मनुष्य, शिकारी पक्षी, सिंह आदि पशु एवं डँसनेवाले सर्प हों, वे सब-के-सब सच्चविदानन्दस्वरूप श्रीकृष्णके शद्भुनादसे आहत हो सौम्यभावको प्राप्त हो जायँ। जो मेरी चित्तवृत्ति और स्मरणशक्तिका हरण करते हैं, जो मेरे बल
- **Translation**: 

---

### Verse 2 (Agni Puran 0.5002)
- **Original**: *+* अध्याय 271 * ध4ढ7 ढेहेह कक केक केकेक के कूबू6टूबूब्6,बब्लल्-_न छल ऋ क ऋ ऋऋ कफ कफ कफ कफ ऋ 4 फेक # 4 7 967 छा बन का89 «69 छू 58 ढ &क ऋ कक कक 14% % ##% # # # और तेजका नाश करते हैं-तथा जो मेरी कान्ति
- **Translation**: 

---

### Verse 3 (Agni Puran 0.5003)
- **Original**: जगह जनार्दन श्रीहरिका निवास हो
- **Translation**: 

---

### Verse 4 (Agni Puran 0.5004)
- **Original**: सबके पूजनीय, या तेजको विलुप्त करनेवाले हैं, जो उपभोग-
- **Translation**: 

---

### Verse 5 (Agni Puran 0.5005)
- **Original**: मर्यादासे कभी च्युत न होनेवाले अनन्तरूप परमेश्वर सामग्रीको हर लेनेवाले तथा शुभ लक्षणोंका नाश
- **Translation**: 

---

### Verse 6 (Agni Puran 0.5006)
- **Original**: जनार्दनके चरणोंमें प्रणण होनेवाला कभी दुखी करनेवाले हैं, वे कृष्माण्डगण श्रीविष्णुके सुदर्शन-
- **Translation**: 

---

### Verse 7 (Agni Puran 0.5007)
- **Original**: नहीं होता। जैसे भगवान्‌ श्रीहरि परल्रह्म हैं, उसी चक्रके बेगसे आहत होकर विनष्ट हो जाय॑ं।
- **Translation**: 

---

### Verse 8 (Agni Puran 0.5008)
- **Original**: प्रकार बे परमात्मा केशव भी जगत्स्वरूप हैं-- देवाधिदेव भगवान्‌ वासुदेवके संकीर्तनसे मेरी बुद्धि,
- **Translation**: 

---

### Verse 9 (Agni Puran 0.5009)
- **Original**: इस सत्यके प्रभावसे तथा भगवान्‌ अच्युतके मन और इन्द्रियोंको स्वास्थ्यलाभ हो। मेरे आगे-
- **Translation**: 

---

### Verse 10 (Agni Puran 0.5010)
- **Original**: नामकीर्तनसे मेरे त्रिविध पापोंका नाश हो पीछे, दायें-बायें तथा कोणवर्तिनी दिशाओंमें सब
- **Translation**: 

---

### Verse 11 (Agni Puran 0.5011)
- **Original**: इस प्रकार आदि आग्रेय महाएुराणमें “विष्णुपञजरस्तोत्रका कथन” नामक दो सौँ सत्ततवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 12 (Agni Puran 0.5012)
- **Original**: 270 # बेबांकाधांधांधा। भा दो सौ एकहत्तरवाँ अध्याय वेदोंके मन्त्र और शाखा आदिका वर्णन तथा बेदोंकी महिमा पुष्कर कहते हैं-- परशुराम ! वेदमन्त्र सम्पूर्ण
- **Translation**: 

---

### Verse 13 (Agni Puran 0.5013)
- **Original**: और दूसरी शाखा “आश्वलायन' है। इन दो विश्वपर अनुग्रह करनेवाले तथा चारों पुरुषार्थोके
- **Translation**: 

---

### Verse 14 (Agni Puran 0.5014)
- **Original**: शाखाओँमें एक सहस्न तथा ऋग्वेदीय ब्राह्मणभागमें साधक हैं। ऋग्वेद, यजुर्वेद, सामवेद तथा
- **Translation**: 

---

### Verse 15 (Agni Puran 0.5015)
- **Original**: दो सहस्न मन्त्र हैं। श्रीकृष्णद्रैपायन आदि महर्पियोंने अथर्ववेद--ये चार वेद हैं। इनके मन्त्रोंकी संख्या
- **Translation**: 

---

### Verse 16 (Agni Puran 0.5016)
- **Original**: ऋग्वेदको प्रमाण माना है। यजुर्वेदमें उन्‍्नीस सौ एक लाख है। ऋग्वेदकी एक शाखा “सांख्यायन'
- **Translation**: 

---

### Verse 17 (Agni Puran 0.5017)
- **Original**: मन्त्र हैं। उसके ब्राह्मण-प्रन्थोंमें एक हजार मन्त्र * श्रीविष्णुपकआरस्तोत्र चुष्कर उवाच-- ऊलुप:. पूर्0त।- ऋण विष्णुपक्षस्पू। शंकरस्थ द्विजश्रेश. रक्षणाय.. निरूपितम्‌
- **Translation**: 

---

### Verse 18 (Agni Puran 0.5018)
- **Original**: शक्रस्प बल॑. हमस्ुं. प्रयास्वत:
- **Translation**: 

---

### Verse 19 (Agni Puran 0.5019)
- **Original**: तस्य स्वरूप यक्ष्यामि ता त्व शृणु जयादिमतू#
- **Translation**: 

---

### Verse 20 (Agni Puran 0.5020)
- **Original**: ग्राच्यां स्थिताक्षक्री. हरिदेक्षिणतों. गदी । प्रतोच्यां शाम्रैधूगू विष्णुर्जिष्णु: खड़ी ममोत्तरे
- **Translation**: 

---

