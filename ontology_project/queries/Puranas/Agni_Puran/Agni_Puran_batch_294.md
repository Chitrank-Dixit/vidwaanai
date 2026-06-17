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

### Verse 1 (Agni Puran 0.5861)
- **Original**: आठ देवियोंका पूर्वादि दिशाके कमल-दलोंमें
- **Translation**: 

---

### Verse 2 (Agni Puran 0.5862)
- **Original**: '3» छं (ऐं) नित्यक्लिन्ने मदद्रवे ओं पूजन करे। ['श्रीविद्यार्णवतन्त्र' में ये नाम इस
- **Translation**: 

---

### Verse 3 (Agni Puran 0.5863)
- **Original**: ओं (स्वाहा) अआ इई उऊ ऋऋ लू लृ प्रकार मिलते हैं-नित्या, सुभद्रा, समड्रला,
- **Translation**: 

---

### Verse 4 (Agni Puran 0.5864)
- **Original**: एऐ ओ औ अं अ: क ख गघडच छ ज वनचारिणी, सुभगा, दुर्भा, मनोन्‍न्मनी तथा
- **Translation**: 

---

### Verse 5 (Agni Puran 0.5865)
- **Original**: झ जटठडडढणतथदधनपफबभ रुद्ररपिणी।] इनके बाह्मभागमें पाँच दलोंमें
- **Translation**: 

---

### Verse 6 (Agni Puran 0.5866)
- **Original**: मय रल वश घसह कक्ष: 3» छं (ऐं) कामदेवोंका पूजन होता है। “37 हीं अनड्राय
- **Translation**: 

---

### Verse 7 (Agni Puran 0.5867)
- **Original**: नित्यक्लिन्ने मदद्गवे स्वाहा।' यह 'नित्यक्लिन्ना- नमः। 3» हीं स्मराय नमः। 3 हीं मन्मथाय
- **Translation**: 

---

### Verse 8 (Agni Puran 0.5868)
- **Original**: विद्या' है
- **Translation**: 

---

### Verse 9 (Agni Puran 0.5869)
- **Original**: नमः। 3» हीं माराय नमः। 3» हीं कामाय
- **Translation**: 

---

### Verse 10 (Agni Puran 0.5870)
- **Original**: सिंहासनपर आधारशक्ति तथा पद्मका पूजन नमः।' ये ही पाँच काम हैं। कामदेवोंके हाथोंमें
- **Translation**: 

---

### Verse 11 (Agni Puran 0.5871)
- **Original**: करके उसके दलोंमें हृदय आदि अड्भोंकी स्थापना पाश, अड्रकुश, धनुष और बाणका चिन्तन करें।
- **Translation**: 

---

### Verse 12 (Agni Puran 0.5872)
- **Original**: एवं पूजन करनेके अनन्तर मध्यकर्णिकामें देवीकी इनके भी बाह्यभागमें दस दलोंमें क्रमश: रति-
- **Translation**: 

---

### Verse 13 (Agni Puran 0.5873)
- **Original**: पूजा करनी चाहिये
- **Translation**: 

---

### Verse 14 (Agni Puran 0.5874)
- **Original**: विरति, प्रीति-विप्रीति, मति-दुर्मति, धृति-विधृति, गौरीमन्त्र (2) तुष्टि-वितुष्टि--इन पाँच कामवललभाओंका पूजन
- **Translation**: 

---

### Verse 15 (Agni Puran 0.5875)
- **Original**: '30 हु गौरि रुद्रदयिते योगेश्वरि हूं फट्‌ करे
- **Translation**: 

---

### Verse 16 (Agni Puran 0.5876)
- **Original**: 27--33
- **Translation**: 

---

### Verse 17 (Agni Puran 0.5877)
- **Original**: स्वाहा '
- **Translation**: 

---

### Verse 18 (Agni Puran 0.5878)
- **Original**: इस प्रकार आदि आग्रेव महापुराणमें “नाता प्रकारके मन्त्रोंका वर्णन” नामक तौन सौँ तेरहवाँ अध्याय पूद्ध हुआ# 3134 '
- **Translation**: 

---

### Verse 19 (Agni Puran 0.5879)
- **Original**: 4” तह तीन सौ चौदहवाँ अध्याय त्वरिताके पूजन तथा प्रयोगका विज्ञान निग्रहयन्त्र करके मण्डलमें प्रणीता तथा गायत्रीकी पूजा करे। अग्रिदेव कहते हैं-- मुने! “30 हीं हूं खे च
- **Translation**: 

---

### Verse 20 (Agni Puran 0.5880)
- **Original**: (देवीके अग्रभागके केसरसे लेकर प्रदक्षिणक्रमसे चछे क्षः स्त्री हूं क्षे हीं फद्‌ त्वरितायै नमः ।'--इस
- **Translation**: 

---

