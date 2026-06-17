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

### Verse 1 (Vishnu Puran 0.7341)
- **Original**: गृत्समदस्य ज्ौनकश्चातुर्वर्ण्यप्रवर्तयिताभूत्‌ ।। 6
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7342)
- **Original**: काइयस्य काशेय: काशिराज: तस्माद्राष्ट्र:, राष्ट्रस्य दीर्घतपा: पुत्रो3भवत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7343)
- **Original**: धन्वन्तरिस्तु दीर्घतपस: पुत्रो5भवत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7344)
- **Original**: स हिसंसिद्धकार्य- करणस्सकलसम्भूतिषुशेषज्ञानविद_ भगकता नारायणेन चातीतसम्भूतो तस्मै बरो दत्त:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7345)
- **Original**: काहिराजगोत्रेश्वतीर्य त्वमष्टधा सम्यगायुर्वेदं करिष्यपि यज्ञभागभुग्भविष्यसीति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7346)
- **Original**: श्रीपराह्यरजी खोले--आयु नामक जो पुरूरवाका ज्येष्ठ पुत्र था उसने राहुकी कन्यासे बिलाह किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7347)
- **Original**: उससे उसके पाँच पुत्र हुए जिनके नाम क्रमषाः नह॒ष, क्षत्रव॒द्ध, रम्भ, रजि और अनेना थे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7348)
- **Original**: क्षत्रवृद्धके सुह्दोत्र नामक पुत्र हुआ और सुह्षेत्रके काइ्य, काश तथा 'मृत्समद नामक तीन पुत्र हुए। गृत्समदका पुत्र शौनक चातुर्वर्ण्यका प्रवर्तक हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7349)
- **Original**: '4-- 6
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7350)
- **Original**: काआयका पूत्र काशिराज काशेय हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7351)
- **Original**: उसके राष्ट्र, राष्ट्रके दीर्घतपा और दीर्घतपाके धन्वन्तरि नामक पुत्र हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7352)
- **Original**: इस धन्वन्तरिके शरीर और इन्द्रियाँ जरा आदि विकारोंसे रहित थीं--तथा सभी जल्मोमें यह सम्पूर्ण शाल्नॉका जाननेवाला था। पूर्वजन्ममें भगवान्‌ गाराबणने उसे यह वर दिया था कि 'काशिराजके बंशमें उत्पन्न होकर तुम सम्पूर्ण आयुर्वेद आठ भागों विभक्त करोगे और यज्ञ-भागके भोक्ता
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7353)
- **Original**: शध2 तस्थ च धन्वन्तरेः पुत्रः केतुमान्‌ केतुमतो भीमरथस्तस्पापि दिवोदासस्तस्थापि प्रतर्दनः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7354)
- **Original**: स अर मद्रश्रेण्यवंशविनाइनादशेष- शत्रवोइनेन जिता डति शत्रुजिदभवत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7355)
- **Original**: तेन च्॒ प्रीतिमतात्मपुत्रो वत्सवत्सेत्यभिह्ितो बत्सो5भवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7356)
- **Original**: सत्यपरतया ऋतध्वज- संज्ञामवाप
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7357)
- **Original**: ततश्र कुबलबनामानमश्न लेभे तत: कुवलयाश्व इत्यस्थां पृथिव्यां प्रधित:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7358)
- **Original**: तस्य चर वत्सस्य पुत्रोडलर्कनामाभवद्‌ यस्थायमद्यापि इलोको गीयते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7359)
- **Original**: वष्टिवर्ससहस्नाणि पष्टिवर्षततानि च। अलकदपरो नान्‍्यो युभुजे मेदिनीं युवा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7360)
- **Original**: 17 तस्याप्यलर्कस्थ सन्नतिनामाभवदात्मज:
- **Translation**: 

---

