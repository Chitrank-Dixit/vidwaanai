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

### Verse 1 (Vishnu Puran 0.10021)
- **Original**: 21 तुरड्डस्थास्य शक्रोउपि कृष्ण देवाश्न बिभ्यति । धुतकेसरजालस्थ॒ हेषतो5भ्रावल्थेकिन:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10022)
- **Original**: 22 यस्मात्त्वयैष दुष्टात्मा हतः केशी जनार्दन । तस्मात्केशवनाप्रा त्वे लोके ख्यातो भविष्यसि
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10023)
- **Original**: 23 स्वस्यस्तु ते गमिष्यापि कंसयुद्धेउथुना पुनः । परश्रो5ह॑समेष्यामि त्वया केशिनिषृदन
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10024)
- **Original**: 24 कंसे सानुगे बिनिपातिते। भारावतारकर्ता लव पृथिव्या: पृथ्चिबीधर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10025)
- **Original**: 25 तत्रानेकप्रकाराणि युद्धानि पृथिवीक्षिताम्‌। ड्रष्ट्यानि मयायुष्मत्रणीतानि जनार्दन
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10026)
- **Original**: 26 सो5हं वास्थामि गोविन्द देवकार्य महत्कृतम्‌। स्वयैव विदितं सर्व स्वस्ति तेउस्तु ब्रजाम्यहम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10027)
- **Original**: 27 नारदे तु गते कृष्णस्सह गोपैस्सभाजित: । विवेश गोकुलं गोपीनेत्रपानैकभाजनम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10028)
- **Original**: 28 पसीनेसे भरकर ठण्डा पड़ गया और बह निश्वेष्ठ हो गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10029)
- **Original**: इस प्रकार श्रीकृष्णचदद्रक्री भुजासे जिसके मुख्कका बिद्दाल रन्भ्र फैलाया गया है बह महान्‌ असुर मरकर वजपातसे गिरे हुए वृक्षके समान दो खण्ड होकर पृथिवीपर गिर पड़ा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10030)
- **Original**: केशीके दारीस्के वे दोनों खण्ड दो पाँव, आधी पीठ, आधी मैछ तथा एक एक कान-आँख और नासिकास्श्रके सहित सुशोभित हुए
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10031)
- **Original**: इस प्रकार केशीको मारकर प्रसत्रचित्त व्वालबात्मेंसे घिरे हुए श्रीकृष्णचन्द्र बिना श्रमके स्वस्थचित्तसे हँसते हुए यहां खड़े रहे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10032)
- **Original**: केशीके मारे जानेसे विस्मित हुए गोप और गोपियोंने अनुग्रगवश्ञ अत्यन्त मनोहर लूगनेबाले कमलनयन श्रोश्यामसुन्दस्की स्तुति को
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10033)
- **Original**: है विप्र ! उसे मरा देसख्त मेघपटलमें छिपे हुए श्रीनारदजी हर्षितचित्तते कहने लगे--
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10034)
- **Original**: “हे जगन्नाथ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10035)
- **Original**: हे अच्यूत !! आप धन्य हैं, घन्य हैं। अहा ! आपने देवताओंको दुःख देनेवाछे इस केशीक्ो लील्मसे ही मार डाला
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10036)
- **Original**: मैं मनुष्य और अश्वके इस पहले और कहीं न होनेवाले युद्धकों देशनेके छिये हो अत्य्त उत्कण्ठित होकर स्वर्गसे यहाँ आया था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10037)
- **Original**: हे मधुसूदन ! आपने अपने इस अबतारमें जो-जो कर्म किये हैं उनसे मेस चित्त अत्यन्त विस्मित और सन्तुष्ट हो रहा है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10038)
- **Original**: है कृष्ण ! जिस समय यह अश्व अपनी स्रटाओंकों हिल्जता और हींसता हुआ आकाइशकी ओर देखता था तो इससे सम्पूर्ण देबगण और इन्द्र भी डर जाते थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10039)
- **Original**: हे जनार्दन ! आपने इस दुष्टात्मा केशीकों मारा है; इसलिये आप ल्लेकमें 'केशव' नामसे विख्यात होंगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10040)
- **Original**: हे केशिनिषृदन ! आफ्का कल्याण हो, अब मैं जाता हूँ। परसों कंसके साथ आपका युद्ध होनेके समय मैं फिर आकँगा
- **Translation**: 

---

