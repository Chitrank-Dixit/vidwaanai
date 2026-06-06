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

### Verse 1 (Vishnu Puran 0.4041)
- **Original**: जिस समय दो कल्ममात्र रहा हुआ चन्द्रमा सूर्यमण्डलमें प्रवेश करके उसकी अमा नामक किरणमें रहता है वह तिथि अमायास्या कहलाती है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4042)
- **Original**: उस दिन रात्रिमें वह पहले तो जलमें प्रवेश करता है, फिर वृक्ष-लता आदियें निजास करता है और तदनन्तर क्रमसे सूर्यमें चला जाता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4043)
- **Original**: वृक्ष और लता आदियें चन्भमाकी स्थितिके समय [अमाजास्याको] जो उन्हें काटता है अथवा उनका एक़ पत्ता भी तोड़ता है उसे ब्रह्महत्याका पाप लगता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4044)
- **Original**: केबल पन्द्रहवीं कलारूप यत्किश्लित्‌ भागके बच रहनेपर उस क्षीण
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4045)
- **Original**: हडड ओलिष्णुपुराण ([ अ« 12 पिबन्ति द्विकलाकारं शिष्टा तस्य कला तु या । सुधामृतमयी पुण्या तामिन्दो: पितरों मुने
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4046)
- **Original**: 12 निस्पृर्त तदमावास्यां गभस्तिभ्य: सुधामृतम्‌ । मासं तृप्तिमवाष्याग्र्यां पितर: सन्ति निर्बुता: । सौम्या बर्हिषदश्षेव अग्निष्ात्ताश्ष ते त्रिधा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4047)
- **Original**: 13 एबं देवान्‌ सिते पक्षे कृष्णपक्षे तथा पितृन्‌ । वीरुधश्षामृतमयेः. शीतैरप्परमाणुभि:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4048)
- **Original**: 14 वीरुधौषधिनिष्पत्या मनुष्यपशुकीटकान्‌ । आप्याययति शीतांशु: प्राकाश्याह्वादनेन तु
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4049)
- **Original**: 15 रथश्चद्धसुतक्ष॒च। पिशड्जैस्तुरगैयुक्त: सोउष्टाभिवांयुवेगिभि:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4050)
- **Original**: 16 सोपासड्रपताकस्तु शुक्रस्थापि रथो महान्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4051)
- **Original**: 17 अश्राश्व: काप्नन: श्रीमानभोमस्यापि रथो महान्‌ । पद्मरागारुणैरश्ै: संयुक्तो वहिसम्भवैः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4052)
- **Original**: 18 अष्टाभिः पाण्ड्रैयुक्तो वाजिभि: काझ्नो रथ: । तरस्मिस्तिष्ठति वर्षान्ते राशौ राशौ बृहस्पति:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4053)
- **Original**: 19 आकाशसम्भवैरश्वै: शबलै: स्पन्द्न युतम्‌। तमारुहय झनै्याति मन्दगामी झानैश्लर:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4054)
- **Original**: 20 स्वर्भानोस्तुरगा हष्टो भूड्ाभा धूसरें रथम्‌। सकृद्युक्तास्तु मैत्रेय बहन्त्यविरत॑ सदा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4055)
- **Original**: 29 आदिल्यक्निस्सृतो राहु: सोम॑ गच्छति पर्वसु । आदित्यमेति सोमाश्च॒ पुनः सौरेषु पर्ससु
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4056)
- **Original**: 22 तथा केतुरथस्याश्वा अप्यष्टो बातरंहसः। पलालधूमवर्णाभा लाक्षारसनिभारुणा:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4057)
- **Original**: 23 एते मया ग्रहाणां वै तवाख्याता रथा नव । सर्वे ध्रुवे महाभाग प्रबद्धा वायुरश्िमिभि:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4058)
- **Original**: 24 चजद्रमाको पितृगण मध्याड्रोत्तर काह्में चारों ओरसे घेर लेते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4059)
- **Original**: हे मुने ! उस समय उस टद्विकलाकार चन्द्रमाकी बची हुई अमृतमयी एक कल्त्रका चे पितृगणु, पान करते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4060)
- **Original**: अमावास्याके दिन चन्द्र-रर्मिसे निकले हुए उस सुधामृतका पान करके अत्यन्त तृप्त हुए सौम्य, बर्हिषद्‌ और अग्रिष्ाता तीन प्रकारके पितृगण एक मासपर्यन्त सन्‍्तुष्ट रहते हैं
- **Translation**: 

---

