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

### Verse 1 (Vishnu Puran 0.2501)
- **Original**: यज्य पानेकी चिन्ता किसे नहीं होती और घनकी अभिलाषा भी किसको नहीं है ? तथापि ये दोनों मिलते उन्होंको हैं जिन्हें मिलनेवारे होते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2502)
- **Original**: है महाभाग ! महत्त्व-प्राम्रिके लिये सभी यत्र करते हैं, तथापि वैभवका कारण तो मनुष्यका भाग्य ही है, उद्यम नहीं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2503)
- **Original**: हे प्रमो ! जड़, आंवेबेकी, निर्वलछ और अनोतिज्ञोंको भी भाग्यबद् नाना प्रकारक्े भोग और राज्यादि प्राप्त होते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2504)
- **Original**: इसफ़िये जिसे महान्‌ सैभवकी इच्छा हो उसे केवल पुण्यसल़यका ही यत्र
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2505)
- **Original**: श्रीविष्णुपुराण [ अ* 19 एतद्विजानता सर्व जगत्स्थावरजड्गडमम्‌ । द्रष्टव्यमात्मवद्धिष्णुर्यतो5य॑ विश्वरूपध॒क्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2506)
- **Original**: 48 एवं ज्ञात स भगवाननादि: परमेश्वर: । प्रसीदत्यच्युतस्तस्मिग्सन्ने._ क्ेशसह्बयः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2507)
- **Original**: 49 श्रोपराशर उकाच एतच्छुत्वा तु कोपेन समुत्थाय बरासनात्‌ । हिरण्यकहिपु: पुत्र पदा वक्षस्यताइयत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2508)
- **Original**: 50 उबाच च स कोपेन सामर्ष: प्रज्वल्न्निव । निष्पिष्य पाणिना पाणिं हन्तुकामो जगद्यथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2509)
- **Original**: 51 हिरण्यकशिपुरुवाच है विप्रचित्ते हे राहो हे बलैष महार्णवे । नागपादौदृदिर्वद्ध्वा क्षिप्यतां मा विलूम्ब्यताम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2510)
- **Original**: 52 अन्यथा सकला ल्त्रेकास्तथा दैतेयदानवा: । अनुयास्यन्ति मूढस्य मतमस्य दुरात्मन:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2511)
- **Original**: 53 बहुशो वारितोउस्माभिरयं पापस्तथाप्यरे: । स्तुति करोति दुष्टानां वध एबोपकारक:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2512)
- **Original**: 54 श्रीपपादार उकाच ततस्ते सत्वरा दैत्या बद्ध्वा ते नागबन्धनैः: । भर्तुराज्ञों पुरस्कृत्य चिक्षिपु: सलिलार्णवे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2513)
- **Original**: 55 ततश्चचाल चलता प्रह्लादेन महार्णव: । उद्देलो5भूत्परं क्षोभमुपेत्मय च समनन्‍्तत:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2514)
- **Original**: 56 भूलोकिमसिलं दृष्ठा प्राव्यमानं महाम्भसा । हिरण्यकशिपुर्देत्यानिदमाह॒ महामते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2515)
- **Original**: 57 हिरण्यकशिपृस्काच दैतेया: सकले: शैल्रत्रैव वरुणालये। निछिछड्रे: सर्वझ:ः सर्वैश्ञीयतामेष दुर्मति:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2516)
- **Original**: 5758 नाभ्रिर्दहति नैयायं शस्परैश्छिज्नो न चोरगैः । क्षय नीतो न बातेन न विषेण न कृत्यया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2517)
- **Original**: 59 न मायाभिर्न चैवोच्चात्पातितो न च दिमाजै: । बात्त्रेतिदुष्टचित्तो5य॑नानेनाथोंउस्ति जीवता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2518)
- **Original**: 60 करना चाहिये; और जिसे मोक्षको इच्छा हो उसेः्भी समत्वत्मथका ही प्रयल्ल करना चाहिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2519)
- **Original**: देव, मनुष्य, पशु, पक्षों, वृक्ष और सरोसुप---ये सब भगवान्‌ विष्णुसे भिन्न-से स्थित हुए. भी बास्तवमें श्रीअनन्तके ही रूप हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2520)
- **Original**: इस बातकों जाननेवाल्म् पुरुष सम्पूर्ण चराचर जगत्‌कों आत्मवत्‌ देखे, क्योंकि यह सब विश्व- रूपधारी भगवान्‌ विष्णु ही हैं
- **Translation**: 

---

