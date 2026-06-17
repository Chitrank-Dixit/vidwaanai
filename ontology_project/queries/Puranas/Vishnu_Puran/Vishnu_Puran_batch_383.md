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

### Verse 1 (Vishnu Puran 0.7641)
- **Original**: है मैत्रेय ! इस प्रकार ज्यामघकी सन्तानका श्रद्धापूर्वक भल्‍्जी प्रकार श्रवण करनेसे मनुष्य अपने समस्त पापोंसे मुक्त हो जाता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7642)
- **Original**: 0 8--->-_-+>. है 4 हि अब इति श्रीविष्णुपुराणे चतुर्थेंछडनो ढ्वादशोड्ध्याय:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7643)
- **Original**: ््््् हब रा ततेरहवाँ अध्याय सत्यतकी सनन्‍्ततिका वर्णन और स्यमच्तकमर्णिकी कथा वृष्णिसंज्ञास्सत्वतस्य पुत्रा बभूलु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7644)
- **Original**: भजमानस्य नििकृकणवृष्णयस्तथान्ये द्वैमात्रा: शतजित्सहस्र जिदयुतजित्सज्ञाखय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7645)
- **Original**: देवावृधस्यापि यश: पुत्रो&भवत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7646)
- **Original**: तयोश्चायं इलोको गीयते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7647)
- **Original**: यथैव श्रृणुमो दूरात्सम्पश्यामस्तथान्तिकात्‌ । बच्चुः श्रेष्ठो मनुष्याणां देवेदेंबायूधस्सम:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7648)
- **Original**: 5 पुरुषा: घट च पष्टिश्न पट सहस्नाणि चाष्ट च । तेडमृतत्वमनुप्राप्ता.. बच्रोदेंबावृधादपि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7649)
- **Original**: 6 श्रीपराझरजी बोले--सत्वतके भजन, भजमान, दिव्य, अश्वक, देवावृध महाभोज नामक पूत्र हृए
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7650)
- **Original**: भजमानके निभि, ककण वृष्णि तथा इनके तोन सौतेके भाई दातजित, सहस्लजित्‌ और अयुतजित्‌ू--ये छः पुत्र हुए
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7651)
- **Original**: देवावघके बच्नु नामक पुत्र हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7652)
- **Original**: इन दोनों (पिता-पुत्रों) के विषयमें यह इल्मेक प्रसिद्ध है--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7653)
- **Original**: “जैसा हमने दूरसे सुना था बैसा ही पास जाकर भी देखता, वास्तवमें बच मनुष्योंमें श्रेष्ठ है और देवावृध तो देवताओंके समान है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7654)
- **Original**: बच्चु और देवावृध [के उपदेदा किये हुए मार्गका अवल्ण्यन करने] से क्रमशः छः हजार (6074) मनुष्योनि अमरपद प्राप्त किया था'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7655)
- **Original**: अ0् शह़ ] महाभोजस्त्वतिधर्मात्मा तस्थान्वये. भोजा मृत्तिकावरपुरनिवासिनो मारत्तिकावरा बभूवुः चतुर्थ अंदा 279 महाभोज बड़ा धर्मात्मा था, उसकी सन्तानमें भोजलैशी तथा मृत्तिकावस्पुर निवासी मार्त्तिकावर नृपतिगण
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7656)
- **Original**: वृष्णे: सुमित्रों युधाजिध्य पुत्रावभूताम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7657)
- **Original**: वृष्णिके दो पुत्र सुमित्र और युधाजित्‌ हुए,
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7658)
- **Original**: ततश्वानमित्रस्तथानमित्रान्निष्नः निप्नस्य प्रसेनसत्राजितों
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7659)
- **Original**: तस्य च सत्राजितों भगवानादित्य: सखाभवत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7660)
- **Original**: एकदा त्वम्भोनिधितीरसंश्रय: सूर्य सन्नाजिसुष्टाब तन्पनस्कतया च भास्वानभिष्टूय' मानो5ग्रतस्तस्थो
- **Translation**: 

---

