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

### Verse 1 (Bramha 0.2681)
- **Original**: स्वर्णवर्णप्रधे देव बाससी तव केशव
- **Translation**: 

---

### Verse 2 (Bramha 0.2682)
- **Original**: मधुसूदन!!! आपके चरणोंमें यह पाद्य (पाँव
- **Translation**: 

---

### Verse 3 (Bramha 0.2683)
- **Original**: 3» नमो नारायणाय नमः पखारनेके लिये जल) समर्पित है, आप इसे
- **Translation**: 

---

### Verse 4 (Bramha 0.2684)
- **Original**: 'देवतत्त्वसमायुक्त, यज्ञवर्णसमन्वित केशव! स्वीकार करें। सच्विदानन्दस्वरूप श्रीनारायणको
- **Translation**: 

---

### Verse 5 (Bramha 0.2685)
- **Original**: मैं सुनहरे रंगके दो वस्त्र आपकी सेकामें नमस्कार है।' समर्पित करता हूँ। सच्चिदानन्दस्वरूप श्रीनारायणको मधुपर्क-मन्त्र
- **Translation**: 

---

### Verse 6 (Bramha 0.2686)
- **Original**: नमस्कार है।' प्रधुपक॑ महादेव ब्रह्मा: कल्पितं तब।
- **Translation**: 

---

### Verse 7 (Bramha 0.2687)
- **Original**: विलेपन-मन्त्र मभया निवेदित॑ भकक्‍त्या गृहाण पुरुषोत्तम
- **Translation**: 

---

### Verse 8 (Bramha 0.2688)
- **Original**: शरीर ते न जातामि चेष्टों चैव न केशव। 3» जमो भारायणाय नमः मया निवेदितो गन्ध: प्रतिगृष्टा विलिप्यतामू # “महादेव! पुरुषोत्तम! ब्राद्या आदि देवताओंने 3 जपो नारायणाय नमः आपके लिये जिसकी व्यवस्था की थी, बही! “केशव! मुझे आपके शरीर और चेष्टाका ज्ञान मधुपर्क मैं भक्तिपूर्वक्क आपको निवेदन करता हूँ,
- **Translation**: 

---

### Verse 9 (Bramha 0.2689)
- **Original**: नहीं है; मैंने जो यह गन्ध (रोली-चन्दन आदि) कृपया स्वीकार कौजिये। सच्चिदानन्दस्वरूप
- **Translation**: 

---

### Verse 10 (Bramha 0.2690)
- **Original**: निवेदन किया है, इसे लेकर अपने अड्भमें लगा श्रीनारायणको नमस्कार है।' लें। सच्चिदानन्दस्वरूप श्रीनारायणको नमस्कार है।' आचमनीय-मन्त्र
- **Translation**: 

---

### Verse 11 (Bramha 0.2691)
- **Original**: यज्ञोपवीत-मजत्र मन्दाकिन्या: सिर बारि सर्वपापहरं शिवम।
- **Translation**: 

---

### Verse 12 (Bramha 0.2692)
- **Original**: ऋग्यजुःसाममन्त्रेण बत्िबृत॑ पद्चयोगित्रा। गृहाणाचमनीय त्थ॑ मया भकत्या निवेदितम्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.2693)
- **Original**: सावित्रीग्रन्थिसंयुक्तमुपवी्त तवापँये
- **Translation**: 

---

### Verse 14 (Bramha 0.2694)
- **Original**: 3» नमो नारायणाय नमः 3» नमो नारायणाय नमः *भगवन्‌! मैंने गड्भाजीका स्वच्छ जल, जो
- **Translation**: 

---

### Verse 15 (Bramha 0.2695)
- **Original**: 'भगवन्‌! ब्रह्मजीने ऋछू, यजु: और सामबेदके सब पापोंको दूर करनेवाला तथा कल्याणमय है, ' मन्त्रोंसे जिसको त्रिवृत्‌ (त्रिगुण) बनाया है, वह आचमनके लिये भक्तिपूर्वक आपको अर्पित किया
- **Translation**: 

---

### Verse 16 (Bramha 0.2696)
- **Original**: साविम्नी-ग्रन्धिसे युक्त यज्ञोपवीत मैं आपकी सेवामें है; कृपया ग्रहण कौजिये। सच्चिदानन्दस्वरूप
- **Translation**: 

---

### Verse 17 (Bramha 0.2697)
- **Original**: अर्पित करता हूँ। सच्विदानन्दस्वरूप श्रीनारायणको श्रीनारायणको नमस्कार है।' नमस्कार है।' स्त्रान-मन्त्र अलंकार-मजत्र त्वमाप: पृथियी चैव ज्योतिस्त्व॑ वाय्रेव च। दिव्यरत्रसपमायुक्त वद्लिभानुसमप्रभ। लोकेश चृत्तिपात्रेण बारिणा ख्रापयाम्यहम्‌
- **Translation**: 

---

### Verse 18 (Bramha 0.2698)
- **Original**: गात्राणि तव शोभन्तु सालंकाराणि माथव
- **Translation**: 

---

### Verse 19 (Bramha 0.2699)
- **Original**: 3» नमो वारायणाय नमः 3» नप्तो नारायणाय नमः “लोकेश्वर! आप ही जल, पृथ्वी तथा अप्रि
- **Translation**: 

---

### Verse 20 (Bramha 0.2700)
- **Original**: “अग्नि और सूर्यके समान प्रभावाले, और वायुरूप हैं। में जीवनरूप जलके द्वारा
- **Translation**: 

---

