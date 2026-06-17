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

### Verse 1 (Vishnu Puran 0.10201)
- **Original**: 39--41
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10202)
- **Original**: [अक्रूरजीने यह भी देशा कि] सनकादि मुनिजन और निष्पाप सिद्ध तथा योगिजन उस जल्यें हो स्थित होकर नासिकाग-टुष्टिसे उन (श्रीकृष्णचर्ध) का ही चित्तन कर रहे है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10203)
- **Original**: आ> 18 ] पञ्चम अंश 359 बलकृष्णौ तथाक्रूरः प्रत्यभिज्ञाय विस्मित: । इस प्रकार वहाँ राम और कृष्णको पहचानकर अक्रूरजो अचिन्तयंद्रथाच्छीघ्र. कथमत्रागताविति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10204)
- **Original**: बड़े ही विस्मित हुए और सोचने लगे कि ये यहाँ इतनी विवक्षो: स्तप्भयामास वाच्न॑ तस्य जनार्दन: । ततो निष्क्रम्य सलिलाद्रथमभ्यागत: पुन:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10205)
- **Original**: 44 दरदर्श तन्र चैबोभौ रथ्स्थोपरि निष्ठितो । रामकृष्णा यथापूर्व मनुष्यवपुषान्खितौ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10206)
- **Original**: 45 निमभझश्च पुनस्तोये ददर्श च तथैव तो। संस्तृयमानो. गन्धर्वैर्पुनिसिद्धमहोरगै:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10207)
- **Original**: 46 ततो विज्ञातसद्धावस्स तु दानपतिस्तदा। तुष्ठावा. सर्वविज्ञानमयमच्युतमीश्वरम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10208)
- **Original**: 47 व्यापिने नेकरूपेकस्वरूपाय नमो नमः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10209)
- **Original**: 48 सर्वरूपाय ते5चिन्त्य हविर्भूताय ते नमः । नमो विज्ञानपाराय पराय प्रकृतेः प्रभो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10210)
- **Original**: 492 भूतात्मा चेन्द्रियात्मा च प्रधानात्मा तथा भवान्‌ आत्मा च परमात्मा च त्वमेकः पञ्चधा स्थित:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10211)
- **Original**: 50 प्रसीद सर्ब॑सर्त्रात्मन्‌ क्षराक्षसमयेश्वर ।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10212)
- **Original**: 59 अनाख्येयस्वरूपात्मन्ननाख्येयप्रयोजन॒ । अनाख्येयाभिधान त्वां नतोउस्मि परमेश्वर
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10213)
- **Original**: 52 न यत्र नाथ दिद्वान्ते नामजात्यादिकल्पना: । तक़हा परम नित्यमविकारि भवानज:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10214)
- **Original**: 53 न कल्पनामृते<र्थस्य सर्वस्याधिगमो यत: । ततः कृष्णाच्युतानन्तविष्णु्सज्ञाभिरीड्यते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10215)
- **Original**: एड सर्वार्थास्व्मज विकल्पनाभिरेते .._स्सर्वस्मिन्न हि भवतोउस्ति किल्निदन्यत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10216)
- **Original**: 55 त॑ ब्रह्म पशुपतिर्यमा विधाता तोयेशो. धनपतिरन्तकस्त्वमेको . भन्नार्थर्जजदभिपासि शक्तिभेदे:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10217)
- **Original**: 56 जौघतासे रथसे कैसे आ गये ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10218)
- **Original**: जब उन्होंने कुछ कहना चाहा तो भगवानने उनकी ज्राणी रोक दी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10219)
- **Original**: तन ये जलसे निकलकर रथके पास आये और देखा कि वहाँ भी सम और कृष्ण दोनों ही मनुष्य-शरीरसे पूर्वबत्‌ रथपर बैठे दुए है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10220)
- **Original**: तदनन्तर, उन्होंने जलमें घुसकर उत्कें फिर गन्धर्व, सिद्ध, मुनि और नागादिकॉसे स्तुति किये जाते देखा
- **Translation**: 

---

