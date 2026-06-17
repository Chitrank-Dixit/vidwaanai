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

### Verse 1 (Vishnu Puran 0.11701)
- **Original**: ड1्2 [ अ* 37 भगवन्यन्यया कार्य तदाज्ञापय साम्प्रतम्‌। पन्ये कुलमिदं सर्व भगवान्संहरिष्यति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11702)
- **Original**: 32 नाशायास्य निमित्तानि कुलस्यथाच्युत लक्षये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11703)
- **Original**: 33 नरनारायणस्थाने. तत्पतित्र महीतले
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11704)
- **Original**: 34 मच्मना मत्मसादेन तन्न सिद्धिमवाप्स्यसि । अहं स्वर्ग गमिष्यामि ह्यपसंहत्य वै कुछम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11705)
- **Original**: 35 द्वारकां च मया त्यक्तां समुद्र: प्रावविष्यति । मद्देइ्म चैक॑ मुक्त्वा तु भयान्मत्तो जलाशये । तत्र सन्निहितश्चाह॑ भक्तानां हितकाम्यया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11706)
- **Original**: 36 श्रीपराहर उवाच इत्युक्त: प्रणिपत्यैंन जगामाशु तपोबनम्‌। नरनारायणस्थान॑_ केशवेनानुमोदितः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11707)
- **Original**: 37 ततस्ते यादवास्सवें रथानारुह्य शीघ्रगान्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11708)
- **Original**: प्रभास॑ प्रययुस्सारँ. कृष्णरानादिभिद्दिज
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11709)
- **Original**: 38 प्रभास॑ समनुप्राप्ता: कुकुरान्थकवृष्णय: । चक्कुस्तत्र महापानं वासुदेबेन चोदिता:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11710)
- **Original**: 39 पिखतां तत्र चैतेषां सल्डरेंण परस्परम्‌। अतिवादेन्धनो जज्ञे कलहाम्रिः क्षयावहः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11711)
- **Original**: 40 अ्रीमैत्रेय उवाच सं स्व॑ वै भुझतां तेषां कलह: किन्निमित्तक: । सद्बूर्षो वा द्विजश्रेष्ठ तन्‍्ममाख्यातुमहसि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11712)
- **Original**: 41 औपराशर ठवाच मृष्टं मदीयमन्न॑ ते न मृष्टमिति जल्पताम्‌। मृष्ठापृष्ठकथा जज्ञे सद्बर्धकलहो ततः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11713)
- **Original**: डर ततश्ञान्योन्यमभ्येत्य क्रोधसंरक्तछोचना: । जश्चुः परस्परं ते तु शस्त्रैदेंबबलात्कृता:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11714)
- **Original**: 43 क्षीणशस्त्राश्न जगृहु: प्रत्यासन्नामथैरकाम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11715)
- **Original**: 44 कहा--
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11716)
- **Original**: “भगवन्‌ ! मुझे ऐसा भ्रतोत होता है कि अब आप इस कुलछका नाश करेंगे, क्योंकि हे अच्युत ! इस समय सब ओर इसके नाइके सूचक कारण दिखायी दे रहे हैं; अत: मुझे आज्ञा दीजिये कि मैं क्या कहूँ 2”
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11717)
- **Original**: श्रीभगवान्‌ खोले--हे उद्धव ! अब तुम मेरी कृपासे प्राप्त हुई दिव्य गतिसे नर-नारायणके निवासस्थान गन्धमादनपर्वतपर जो पत्रित्र बदरिकाश्रम क्षेत्र है वहाँ जाओ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11718)
- **Original**: पृथिवीतलूपर वही सबसे पावन स्थान है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11719)
- **Original**: वहाँपर मुझमें चित्त लगाकर तुम मेरी कृपासे सिद्धि प्राप्त करोगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11720)
- **Original**: अब मैं भी इस कुलका संहार करके स्वर्गस्थ्रेकको अल्म जाऊँगा
- **Translation**: 

---

