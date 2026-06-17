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

### Verse 1 (Vishnu Puran 0.941)
- **Original**: हे देव ! वसुगण, मरुद्रण, साध्यगण और विश्वेदेवणण भी आप ही हैं तथा आपके सम्मुख जो यह देवसमुदाय है, हे जगत्स्रष्टा ! वह भी आप ही हैं क्योंकि आप सर्वत्र परिपूर्ण हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.942)
- **Original**: आप ही यज्ञ हैं, आप ही वषद्कार हैं तथा आप ही ऑकार और प्रजापति हैं। हे सर्वात्मन्‌ ! विद्या, वेद्य और सम्पूर्ण जगत्‌ आपहीका स्वरूप तो है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.943)
- **Original**: हे विष्णों ! दैल्योंसे परास्त हुए हम आतुर होकर आफ्की शरणमें आये हैं; है सर्वस्वक्ृप ! आप हमपर प्रसन्न होइये और अपने तेजसे हमें सश्कक्त कीजिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.944)
- **Original**: हे प्रभो। जबठक जीव सम्पूर्ण पापोंकों नष्ट करमेब्राले आपकी शरणमें नहीं जाता तभीतक उसमें दीनता, इच्छा, मोह और दुःख आदि रहते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.945)
- **Original**: हे प्रसन्नात्मन्‌ ! हम झरणागतोंपर आप प्रसन्न होइये और हे नाथ ! अपनी दक्तिसे हम सब
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.946)
- **Original**: एवं संस्तूयमानस्तु प्रणतैरमरैहीरि: । असन्नदृष्टिभगवानिदमाह स॒ विश्वकृत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.947)
- **Original**: 75 तेजसो भवतां देवा: करिष्याम्युपबृंहणम्‌ । बदाप्यहै यत्क्रियतां भवद्धिस्तदिद सुरा:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.948)
- **Original**: 76 आनीय सहिता दैल्वै: क्षीराव्धौं सकल्तैषधी: । प्रक्षिप्यात्रामृतार्थ ता: सकला दैत्यदानलै: । मन्धान मन्दरं कृत्वा नेत्र कृत्वा च वासुकिम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.949)
- **Original**: 77 मध्यताममृतं देवा: सहाये मय्यवस्थिते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.950)
- **Original**: 78 सामपूर्व चर दैतेयास्तत्र साहाव्यकर्मणि । सामान्यफलभोक्तारो यूयं वाच्या भविष्यथ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.951)
- **Original**: 79 मध्यमाने च तत्राब्धौ यत्समुत्पत्स्यतेडमृतम्‌ । तत्पानाइलिनो यूयममराश्ष॒भविष्यथ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.952)
- **Original**: 80 तथा चाह करिष्यामि ते यथा त्रिदशद्विषः । न प्राप्स्यन्यमृतं देवा: केवल ख्लेझभागिन:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.953)
- **Original**: 819 श्रीफाझर उवाच इत्युक्ता देवदेवेन सर्व एवं तदा सुराः। सन्धानमसुरैः कृत्वा यत्रवन्तोउमृते3$भवन्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.954)
- **Original**: 82 नानोषधी: समानीय देवदैतेयदानवा: । क्षिप्वा क्षीराव्थिपयसि शरदअभ्रामरूत्विषि
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.955)
- **Original**: 83 मन्धान॑ मन्दरं कृत्वा नेत्र कृत्वा च वासुकिम्‌ । ततो मथितुमारब्धा मैत्रेय तरसाउमृतम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.956)
- **Original**: 84 कृष्णेन बासुकेर्देत्या: पूर्वकाये निवेशिता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.957)
- **Original**: 85 ते तस्य मुखनिश्चासवह्धितापह्तत्विष: । निस्तेजसोउसुरा: सर्वे बरभूवुरमितौजस:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.958)
- **Original**: 86 तेनैव. मुखनिश्वासवायुनास्तबलाहकै: । पुच्छप्रदेशे वर्षद्धिस्तदा चाप्यायिताः सुरा:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.959)
- **Original**: 87 क्षीरोदमध्ये भगवान्कूर्मरूपी स्वयं हरिः । मन्थनाद्रेरध्िष्टानं.. भ्रमतो5भून्यहामुने
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.960)
- **Original**: 88 रूपेणान्येन देवानां मध्ये चक्रगदाधर: । चकर्ष नागराजानं दैत्यमध्येषपपरेण च
- **Translation**: 

---

