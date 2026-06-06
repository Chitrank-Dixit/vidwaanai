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

### Verse 1 (Vishnu Puran 0.1521)
- **Original**: 27 यो यज्ञपुरुष॑ विष्णुमनादिनिथन प्रभुम्‌। विनिन्दत्यधमाचारो न स योग्यो भुवः पति;
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1522)
- **Original**: 28 इत्युक्त्वा मन्त्रपुतैस्तै: कुशैर्मुनिगणा नृपम्‌। निजलुर्निहते॑ पूर्व. भगवच्निन्दनादिना
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1523)
- **Original**: 29 ततश्न मुनयो रेणुं ददृशुः सर्वतो द्विज। किमेतदिति चासत्नान्यप्रच्छुस्ते जनांस्तदा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1524)
- **Original**: 30 आख्वयात॑ क् जनैस्तेषां चोरीधूतैरराजके । रष्ट्रे तु लोकैरारब्धं॑ परस्वादानमातुरैः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1525)
- **Original**: 39 तेषामुदीर्णवेगानां चोराणां मुनिसत्तमा:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1526)
- **Original**: सुमहान्‌ दृश्यते रेणुः परवित्तापहारिणाप्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1527)
- **Original**: 32 ततः सम्मन्त्य ते सर्वे मुनयस्तस्य भूभृत: । ममन्धुरूरे. पुत्रार्थमनपत्यस्थ यत्रतः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1528)
- **Original**: 33 मशथ्यमानात्समुत्तस्थौ तस्योरो: पुरुष: किल्‍्ड । दग्धस्थृणाप्रतीकाझ: खर्व्वाटास्योउतिहुस्वकः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1529)
- **Original**: 34 कि करोमीति तान्सर्बान्स विप्रानाह चातुरः । निषीदेति तमूचुस्ते निषादस्तेन सोउडभवत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1530)
- **Original**: 35 ततस्तत्सम्यवा जाता विन्ध्यदौलनिवासिन: । निषादा मुनिशार्द्ल पापकर्मोपलक्षणा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1531)
- **Original**: 36 तेन द्वारेण तत्पाप॑ निष्क्रार्स तस्य भूफ्तेः । निषादास्ते ततो जाता वेनकल्मषनाझना:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1532)
- **Original**: ! 37 तस्वैब दक्षिणं हस्त॑ ममन्थुस्ते ततो द्विजा:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1533)
- **Original**: 38 मध्यमाने च तत्राभूत्युथुवैन्य: प्रतापवान। दीप्यमान: स्ववपुषा साक्षादभिरिव ज्वलन्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1534)
- **Original**: 39 आद्यमाजगवं नाम खात्पपात ततो धनु: । शराश्व दिव्या नभस: कवर्च चर पपात ह
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1535)
- **Original**: 40 [ अ* 13 ऋषिगण खोले--महाराज ! आप ऐसी आज्ञा दीजिये, जिससे धर्मका क्षय न हो। देखिये, यह सास जगत्‌ हवि (यज्ञमें हवन की हुई सामग्री) का ही परिणाम है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1536)
- **Original**: अीपराशरजी खोले--महर्षियोंके इस प्रकार बास्म्बार समझाने और कहने-सुननेपर भी जब वेनने ऐसी आज्ञा नहीं दी तो वे अत्यन्त क़ुद्ध और अमर्षयुक्त होकर आपसमें कहने लगे--'इस पापीको मारो, माय!
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1537)
- **Original**: जो अनादि और अनन्त यज्ञपुरुष प्रभु विष्णुकी निनदा करता है वह अनाचारी किसी प्रकार पृथिवोषति होनेके योग्य नहीं है'
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1538)
- **Original**: ऐसा कह मुनिगणोोने, भगवानकी निन्‍दा आदि करनेके कारण पहल्ले ही मरे हुए ठस राजाकों मन्त्रसे पवित्र किये हुए कुशाओंसे मार डाल्थ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1539)
- **Original**: है ट्विज ! तदनन्तर उन मुनीश्चरोने सब ओर बड़ी घूलि उठती देखी, उसे देख्ककर उन्होंने अपने निकटलतों स्तेगोंसे पूछा-- “यह क्या है ?”
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1540)
- **Original**: उन पुरुषोंने कहा-- राष्ट्रके राजाहीन हो जानेसे दीन-दुःखिया स्प्रेगोनि चोर बनकर दूसरोंका धन लूटना आरम्भ कर दिया है
- **Translation**: 

---

