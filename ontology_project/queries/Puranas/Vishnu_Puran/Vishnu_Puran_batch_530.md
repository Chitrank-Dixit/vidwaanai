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

### Verse 1 (Vishnu Puran 0.10581)
- **Original**: 91 महाबलपरीवारो प्रगधाधिपतिर्बल्ली । हन्तुमभ्याययों कोपाज्जरासन्धस्सयादबम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10582)
- **Original**: 2 उपेत्य मथुरां सोडईथ रुरोध मगधेश्वर:। अक्षौहिणीभिस्सैन्यस्थ त्रयोबिंशतिभिर्वुत:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10583)
- **Original**: 3 ततो रामभ्न कृष्णअ्र मति चक्रतुरझसा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10584)
- **Original**: आयुधानां अनन्तरं हरेइशा् तृणो चाक्षयसायकौ। आकाशादागतौो विप्र तथा कौमोदकी गदा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10585)
- **Original**: 6 हलं। से बलभद्गस्थ गगनादागतं महत्‌। मनसो5भिमतं विप्र सुनन्‍्द पुसले तथा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10586)
- **Original**: । 7 ततो युद्धे पराजित्य ससैन्यं पगधाधिपम्‌। पुरी बविविशतुर्वीरावुभो रामजनार्दनो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10587)
- **Original**: 8 जिते तस्मिन्सुदुर्वत्ते जरासन्थे महामुने। जीबपाने गले कृष्णस्तेनामन्यत नाजितम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10588)
- **Original**: 9 मुनिसत्तम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10589)
- **Original**: 5 श्रीपराद्ररजी बोले--हे मैत्रेय ! महाबली कंसने जरासन्थकी पुत्री अस्ति और प्राप्तिसे खिलाह किया था, अत: बह अत्यन्त बलिष्ठ मगधराज क्रोधपूर्वक एक बहूत बड़ी सेना लेकर अपनी पृत्रियोंके स्वामी कंसको मारनेवाले श्रीहरिको यादवोंके सहित मारनेकी इच्छासे मथुणपर चढ़ आया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10590)
- **Original**: मगधेश्वर जरासखने तेईस अक्षौहिणी सेनाके सहित आकर मथुराकों चारों ओरसे चेर छिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10591)
- **Original**: तब महाबलछी राम और जनार्दन धोड़ी-सी सेनाके साथ नगरसे निकरूकर जरासख्थके प्रवल सैनिकॉसे युद्ध करने लगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10592)
- **Original**: हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10593)
- **Original**: उस समय राम और किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10594)
- **Original**: हे विप्र ! हरिके स्मरण करते ही उनका शार्ड घन्‌ष, अक्षय बराणयूक्त दो तरकश और कौमोदकी नामकी गदा आकाशसे आभाकर उपस्थित हो गये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10595)
- **Original**: हे द्विज ! बलूभद्रजीके पास भी उनका मनोवाज्छित महान्‌ हल और सुनन्‍द नामक मूसलू आकाइझसे आ गये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10596)
- **Original**: तदनन्तर दोनों खीर गम और कृष्ण सेनाके सहित सगधरांजको युद्धमें हराकर मथुराफुरीमें चले आये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10597)
- **Original**: है महामुने ! दृराचारी जरासन्धको जीत लेनेपर भी उसके जीवित चले जानेके कारण कृष्णचन्द्रने अपनेको अपराजित नहीं समझा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10598)
- **Original**: आ0 रह ) पुनरप्याजगामाथ जरासन्थो बल्लान्वित: । पश्चम अंश 373 है ट्विजोत्तप ! जरणासन्ध फिर उतनी ही सेना लेकर जितश्ष रामकृष्णाभ्यामपक्रान्तो द्विजोत्तम
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10599)
- **Original**: आया, कित्तु राम और कृष्णसे पराजित होकर भाग दश चाष्टी च सदय्मामानेवमत्यन्तदुर्पद: । यदुभिर्मागथो राजा चक्रे कृष्णपुरोगमै:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10600)
- **Original**: 11 अपक्रान्तो जरासन्धस्स्वल्पसैन्यैर्बलाधिक:
- **Translation**: 

---

