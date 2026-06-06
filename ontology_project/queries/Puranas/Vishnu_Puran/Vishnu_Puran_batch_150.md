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

### Verse 1 (Vishnu Puran 0.2981)
- **Original**: मर 1 ] विपर्ययो न तेघ्ृस्ति जरामृत्युभर्य न चना । धर्माश्वर्मो न तेप्ास्तां नोत्तमाधममध्यमा: । न तेषृस्ति युगावस्था क्षेत्रेष्नाट्सु सर्वदा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2982)
- **Original**: 26 हिमाद्वय तु जै वर्ष नाभेरासीन्महात्मन: । तस्वर्षभो5भवत्पुत्रो मेरुदेव्यां महाह्युति:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2983)
- **Original**: 27 ऋषभाद्धरतो जज्ञे ज्येष्ठ: पुत्रशतस्यथ स: । कृत्वा राज्य स्वधर्मेंण तथेष्टठा विविधान्मखान्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2984)
- **Original**: 28 अभिषिच्य सुतं बीर॑ भरत पृथिवीपति: । तपसे स महाभाग: पुलहस्याभ्रम॑ ययौं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2985)
- **Original**: 29 वानप्रस्थविधानेन तत्रापि कृतनिश्चयः । तपस्तेपे यथान्यायमियाज स महीपतिः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2986)
- **Original**: 30 तपसा कर्षितोउत्यर्थ कृझो धमनिसन्ततः । नो वीटां मुखे कृत्या वीराध्वानं ततो गत:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2987)
- **Original**: 31 ततक्ष भारत बर्षमेतल्ल्ोकेषु गीयते। भरताय यतः पित्रा दत्त प्रातिष्ठता वनम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2988)
- **Original**: 32 सुमतिर्भरतस्याभूत्पुत्र:.. परमधार्मिक: । कृत्वा सम्यग्ददौ तस्मै राज्यमिष्टमख्र: पिता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2989)
- **Original**: 33 पुत्रसडक्रामितश्रीस्तु भरत: स महीपति: । योगाभ्यासरतः प्राणाउ्द्वालग्रामेउत्यजन्पुने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2990)
- **Original**: 34 अजायत च विप्रोडसौ योगिनां प्रवरे कुले । मैत्रेय तस्थ चरित॑ कथयिष्याम्ति ते पुन:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2991)
- **Original**: 35 सुमतेस्तेजसस्तस्मादिन्द्रद्य्ने. व्यजायत । परमेष्ठी ततस्तस्मात्मतिहारस्तटन्‍्वय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2992)
- **Original**: 36 प्रतिहर्तेति विख्यात उत्पन्नस्तस्य चात्मज: । भवस्तस्मादथोद्वीथ: प्रस्तावस्तत्सुतो विभुः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2993)
- **Original**: 37 पृथुस्ततस्ततो नक्तो नक्तस्थापि गयः सुतः । नरो गयस्यथ तनयस्तत्पुत्रो5भूद्विरादू ततः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2994)
- **Original**: 38 तस्य पुत्रों महावीयों धीमांस्तस्मादजायत। महान्तस्तत्सुतश्राभून्मनस्युस्तस्थ चात्मज:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2995)
- **Original**: 39 त्वष्टा त्वष्ुश्न बिरजो रजस्तस्याप्यभूत्सुतः । झतजिद्रजसस्तस्थ॒ जज्ञे पुत्रशत॑ मुने
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2996)
- **Original**: 40 द्वितीय अंश 103 ही समस्त भोग-सिद्धियाँ प्राप्त हो जाती हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2997)
- **Original**: उनमें किसी प्रकारके ल्रिपर्यय (असुख या अकाल-मृत्यु आदि) तथा जरा-मृत्यु आदिका कोई भय नहीं होता और न धर्म, अधर्म अथवा उत्तम, अधम और मध्यम आदिका ही भेट है। उन आठ वर्षो्में कभी कोई युगपरिवर्तन भी नहीं होता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2998)
- **Original**: महात्मा नाभिका हिम नाप्रक चर्ष था; उनके मेरुदेवीसे अतिशय क्म्रन्तिमानू ऋषभ नामक पुत्र न
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2999)
- **Original**: ऋषभजीके भस्तका जन्म हुआ जो उनके पुओ्रॉमें सबसे बड़े थे। महाभाग पृचिवीपति ऋषभदेवजी धर्मपूर्वक राज्य-दासन तथा विविध यज्ञॉका अनुष्ठान करनेके अनन्तर अपने वीर पुत्र भरतकों राज्याधिकार सौंपकर तपस्याके लिये पुलडाश्रमक्तों चले गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3000)
- **Original**: महाराज ऋषभने बहाँ भी बानप्रस्थ आश्रमकी लिधिसे रहते हुए निश्चयपूर्चक तपस्या को तथा नियमानुकूल चच्नानुष्टान किये
- **Translation**: 

---

