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

### Verse 1 (Vishnu Puran 0.1781)
- **Original**: “हे नृपतिगण ! आप क्रोध झ्ञान्त कीजिये और मैं जो कुछ कहता हूँ, सुनिये। मैं वृक्षोके साथ आपलोगॉकी सम्धि करा दूँगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1782)
- **Original**: वृक्षो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1783)
- **Original**: ंसे उत्पन्न हुई इस सुन्दर वर्णवाल्ली रत्नस्वरूपा कन्याका मैंने पहलेसे ही भविष्यको जानकर अपनी [ अमृतमयी ] किरणोंसे पाल्न-पोषण किया है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1784)
- **Original**: वृक्षोंकी यह कन्या मारिषा नामसे प्रसिद्ध है, यह महाभागा इसलिये ही उत्पन्न ब्त्ने गयी है कि निश्चय हो तुम्हारे वंशको बढ़ानेवाली तुम्हारी भार्या हो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1785)
- **Original**: मेंरे और तुम्हारे आधे-आधे तेजसे इसके परम निद्वान्‌ दक्ष नामक प्रजापति उत्पन्न होगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1786)
- **Original**: वह तुम्हारे तेजके सहित मेरे अंडसे अ्जाकी खूब वृद्धि करेगा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1787)
- **Original**: पूर्वकालमें वेदवेत्ताओँमें श्रेष्ठ एक कप्डु नामक मुनीधर थे। उन्होंने गोमती कदीके परम स्मणीक तटपर घोर तप किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1788)
- **Original**: ठब इच्रने उन्हें तपोभ्रष्ट करनेके लिये प्रम्त्थ्ेचा नामकी उत्तम अप्सणक् नियुक्त किया। उस मज्लुहासिनोने उन ऋषिश्रेष्ठकों विचलित कर दिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1789)
- **Original**: उसके द्वारा क्षुब्य होकर ले सौसे भी अधिक वर्षतक विषयासक्त-चित्तसे मन्दरावलकी कन्दारामें रहे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1790)
- **Original**: तब, हे महाभाग ! एक दिन उस अप्सराने कण्ड ऋषिसे कहा--'हे ब्रह्मन्‌ ! अब मैं स्वर्गलोकको जाना चाहती हूँ, आप श्रसन्नतापूर्वक मुझे आज्ञा दीजिये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1791)
- **Original**: उसके पेसा कहनेपर ठसमें आसक्त-चित्त हुए मुनिने कहा--“भद्रे! अभी कुछ दिन और रहो"
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1792)
- **Original**: उनके ऐसा कहनेपर उस सुन्दरीने महात्पा कप्छुके साथ अगले सौ वर्षतक और रहकर नाना प्रकारके भोग भोगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1793)
- **Original**: तब भी, उसके यह पूछनेपर कि 'भगवन्‌ ! मुझे स्वर्गल्लेककों जानेकी आज़ा दीजिये' ऋषिने यहो कहा कि 'अभी और उहरो'
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1794)
- **Original**: त्दनन्तर सौ वर्षसे कुछ अधिक ब्रीत जानेपर उस सुमुखीने प्रणययुक्त मुसकानसे सुशोभित बचनोंमें फिर कहा-- “ब्रह्मन्‌ ! अब मैं स्वर्गको जातो हूँ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1795)
- **Original**: यह सुनकर मुनिने उस विशाल्मक्षीकों आल्क्िनिकर कहा-- अयथि सुभु ! अब तो तू बहुत दिनॉके लिये चली जायगी इसलिये क्षणभर तो और ठहर”
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1796)
- **Original**: तब वह सुश्रोेणो (सुन्दर कमरवालली) उस ऋषिके साथ क्रीड़ा करतो हुई दो सौ वर्षसे कुछ कम और रही
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1797)
- **Original**: है महाभाग ! इस प्रकार जब-जन वह सुन्दरों
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1798)
- **Original**: द््ढड श्रीविष्णुपुराण [ अब 157 तस्य शञापभयाद्धीता दाक्षिण्येन च॒ दक्षिणा । ज्रोक्ता प्रणयभद्ढात्तिवेदिनी न जहौ मुनिम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1799)
- **Original**: 22 तया च॑ रमतस्तस्थ परमर्पेरहर्निशम्‌ । नव॑ नवमभूत्रेण मन्यथाविष्टन्ेतस:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1800)
- **Original**: 23 एकदा तु त्वरायुक्तो निश्चक्रामोटजान्पुनि: । निष्करामन्तं च कुत्रेति गम्यते प्राह सा शुभा
- **Translation**: 

---

