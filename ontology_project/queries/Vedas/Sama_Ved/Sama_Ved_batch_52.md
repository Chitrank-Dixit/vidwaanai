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

### Verse 1 (Sama Ved 0.1021)
- **Original**: 384 .यत्सोममिन्द्र विष्णावि यद्वा घ त्रित आत्त्ये ।यद्वा मरुत्सु मन्दसे समिन्दुभि:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1022)
- **Original**: 4 हे इन्द्रदेव ! यज्ञों में विष्णु के उपस्थित होने के बाद आपने जो सोमपान किया अथवा आप्त्य-त्रित के अथवा मरुदगणों के साथ अथवा अन्य यज्ञों में सोमरस के सेवन से आनन्दित होने वाले आप, हमारे यज्ञ में (भी) सोमपान करके आनन्दित हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1023)
- **Original**: 385. एदु मधोर्मदिन्तरं सिज्ञाध्वर्यों अन्धसः
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1024)
- **Original**: एवा हि वीरस्तवते सदावृधः
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1025)
- **Original**: हे कऋद्रत्विग्गण ! मधुर सोमपान से आनन्दित होने वाले इन्द्रदेव को यह रस समर्पित करो । पराक्रमी एवं निरन्तर वृद्धि को प्राप्त होने वाले इन्द्रदेव ही स्तोताओं द्वारा सर्वदा प्रशंसित होते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1026)
- **Original**: 386. एन्दुमिन्द्राय सिज्ञत पिबाति सोम्य॑ मधु । प्र राधांसि चोदयते महित्वना
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1027)
- **Original**: 6 । । हे ऋत्विजो ! इन्द्रदेव के निमित्त सोमरस समर्पित करो, जिस मधुर सोमरस-पान के बाद वे अपने प्रभाव से याजकों को विपुल धन प्रदान करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1028)
- **Original**: 387. एतो न्विन्द्रं स्‍्तवाम सखाय: स्तोम्यं नरम्‌ ।कृष्टीयों विश्वा अभ्यस्त्येक डत्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1029)
- **Original**: हे मित्रो ! शीघ्र आओ, हम उस स्तुत्य, श्रेष्ठ नायक इन्द्रदेव की प्रार्थना करें, जो अकेले ही सभी शत्रुओं को परास्त करने में सक्षम हैं.
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1030)
- **Original**: 388. इन्द्राय साम गायत विप्राय बृहते बृहत्‌ । ब्रह्मकृते विपश्चिते पनस्यवे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1031)
- **Original**: है उद्गाताओ ! विवेक सम्पन्न, महान, स्तुत्य, ज्ञानवान्‌ इन्द्रदेव के निमित्त आप लोग बृहत्साम (नामक स्तोत्रों) का गायन करो
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1032)
- **Original**: 389. य एक इद्विदयते बसु मर्ताय दाशुषे । ईशानो अप्रतिष्कुत इन्द्रो अड़
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1033)
- **Original**: हे प्रिय याजको ! दानशील होने के कारण मनुष्यों को धन देने वाले, प्रतिकार न किये जाने वाले, वे अकेले इन्द्रदेव ही सभी (प्राणियों) के अधिपति हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1034)
- **Original**: 390. सखाय आ शिषामहे ब्रह्मोन्द्राय बच्रिणे। स्तुष ऊ घु वो नृतमाय धृष्णवे
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1035)
- **Original**: 4.6 सामवेद-संहिता है मित्रो ! वज़धारण करने वाले इन्द्रदेव की हम स्तोत्रों से स्तुति करते हुए , उनसे आशीर्वाद की याचना करते हैं श्रेष्ठवीर तथा शत्रुओं को पराजित करने वाले इन्द्रदेव की, हम आप सभी के कल्याण के लिए स्तुति करते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1036)
- **Original**: इति अष्टाविंश: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1037)
- **Original**: के के के
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1038)
- **Original**: एकोनत्रिंश: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1039)
- **Original**: 3991. गृणे तदिन्द्र ते शव उपमां देवतातये । यद्धंसि वृत्रमोजसा शचीपते
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1040)
- **Original**: है शचीपते इन्द्रदेव ! हम उस निकट ही सम्पन्न होने वाले यज्ञ में आपकी शक्ति की स्तुति करते हैं, जिसके कारण आप चृत्र वध करने में सक्षम हैं
- **Translation**: 

---

