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

### Verse 1 (Vishnu Puran 0.6221)
- **Original**: पाषण्डालापजातो5यं दोषो यद्गृघ्नतां गत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6222)
- **Original**: 80 ततः काकत्वमापन्न॑ समनन्तरजन्यनि । उवाच तन्बी भत्तरिमुपलभ्यात्मयोगत:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6223)
- **Original**: 81 अशद्देषभूभृतः पूर्व वइया यस्मै बलिं ददु: । स॒ त्व॑ काकत्वमापन्नो जातोउश बलिभुक्‌ प्रभो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6224)
- **Original**: 82 एवमेव चर काकत्वे स्मारितस्स पुरातनम्‌। तत्याज भूषतिः प्राणान्मयूरत्वमवाप च
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6225)
- **Original**: 83 मयूरत्वे ततस्सा जै चकारानुगति झुभा। द्ततैः प्रतिक्षणं भोज्वै्बाला तजञातिभोजनैः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6226)
- **Original**: 84 ततस्तु जनको राजा वाजिमेधं महाक्रतुम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6227)
- **Original**: चकार तस्यावभूथे स्रापयामास त॑ तदा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6228)
- **Original**: 85 सस्त्रौ स्वयं च तन्वड्डी स्पारयामास चापि तम्‌ । यथासो श्रम्तगालादियोनिं जग्राह पार्थिव:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6229)
- **Original**: 86 स्मृतजन्पक्रमस्सो5थ तत्याज स्वकलेवरम्‌ । जल्ले स जनकस्वैव पुन्नोउसों सुमहात्मन:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6230)
- **Original**: 87 ततस्सा पितर॑ तन्‍वी विवाहार्थमत्रोत्यत्‌ । स चापि कारयामास तस्या राजा स्वयंवरम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6231)
- **Original**: 88 स्वयंवरे कृते सा ते सप्प्राप्तं पतिमात्मनः । यरयापास भूयोअपि भर्त्तभावेन भाभमिनी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6232)
- **Original**: 89 बुभुजे च तया सा्ँ सम्भोगान्रपनन्दन: । पितर्युपरते राज्य विदेहेघषु चकार सः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6233)
- **Original**: 90 डइयाज यज्ञान्सुबहन्ददी दानानि चार्थिनाम्‌। पुन्नानुत्पाद्यामास युयुथ्े च सहारिभिः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6234)
- **Original**: 91 राज्यं भुक्लवा यथान्यायय पालयित्वा वसुखराम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6235)
- **Original**: तत्याज स प्रियाग्राणास्संग्रामे धर्मतो नृपः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6236)
- **Original**: 92 श्रीविष्णुपुराण [ अ* 18 फिर वह एक भेड़िया हुआ; ठस समय भी अनिन्दिता राजकन्याने उस निर्जन बनमें जाकर अपने पतिको उसके पूर्वजत्मका वृत्तान्त स्मरण कराया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6237)
- **Original**: [ उसने कहा-- ] “हे महाभाग ! तुम भेड़िया नहीं हो, तुम राजा शतघनु हो। तुम [ अपने पूर्वजन्मोंमें ] क्रमदा: कुकर और श्रृगाल होकर अब भेड़िया हुए हो'
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6238)
- **Original**: इस प्रकार उसके स्मरण करानेपर शजाने जब भेड़ियेके शरीरको छोड़ा तो गृध-योनिमें जन्म लिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6239)
- **Original**: उस समय भी उसकी निष्पाप भागने उसे फिर बोध कराया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6240)
- **Original**: 'हे नरेन्द्र । तुम अपने स्वरूपका स्मरण करो; इन गुप्न- चेष्टाओंको छोड़ों। पाशण्डके साथ यातालाप करनेके दोषसे हो तुम गृध हुए हो'
- **Translation**: 

---

