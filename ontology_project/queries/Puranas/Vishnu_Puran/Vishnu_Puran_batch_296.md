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

### Verse 1 (Vishnu Puran 0.5901)
- **Original**: और हे नरेंधर ! इसके पीछे भक्तिभावसे तन्‍्मय होकर पहले पितपक्षीय त्राह्मणोंका 'सुस्वधा' यह आज्नञीर्वाद ऋहण करता हुआ यथाझक्ति दक्षिणा दे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5902)
- **Original**: फिर वैश्वदेषिक ब्राह्मणोंके निकट जा उन्हें दक्षिणा देकर कड़े कि “इस दक्षिणासे विश्वेदेवगण प्रसन्न हों
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5903)
- **Original**: उन ब्राह्मणोंके कहनेपर उनसे आशीर्वादके लिये प्रार्थना फिर पहले पितृपक्षके और पीछे देवपक्षके ब्राह्मगोंकों खिदा करें
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5904)
- **Original**: विश्लेदेवगणके सहित मातामह आदिके श्राद्में भी ब्राह्मण-भोजन, दान और विसर्जन आदिकी यही निधि बतलायी गयी है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5905)
- **Original**: पितु और मातामह दोनों हो पक्षोंके श्राद्धोंमें पादशौच आदि सभी कर्म पहले देवपक्षके त्राह्मणोंके करे परन्तु विदा पहले पितृपक्षीय अधवा मातामहपक्षीय ब्राह्मणोंको ही करे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5906)
- **Original**: 48 । तदनन्तर, प्रीतिकचन और सम्मानपूर्वक ब्राह्मणोंको विदा करें और उनके जानेके समय द्वारतक उनके पीछे-पीछे जाय तथा जब वे आज्ञा दें तो लौट आवखे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5907)
- **Original**: फिर विज्ञ पुरुष वैश्वदेव नामक निशत्यकर्म करे और अपने पूज्य पुरुष, बन्धुजन तथा भृत्यगणके सहित स्वये भोजन करें
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5908)
- **Original**: युद्धिमान्‌ पुरुष इस प्रकार पैत््य और मातामह-श्राद्धका अनुष्ठान करे। श्राद्धसे तृप्त होकर पित॒गण समस्त
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5909)
- **Original**: आ0 16 ) त्रीणि श्राद्धे पवित्राणि दोहिजर: कुतपस्तित्ठा: । रजतस्य तथा दान॑ कथासड्डीर्तनादिकम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5910)
- **Original**: 52 बर्ज्यानि कुर्वता श्राद्ध क्रोधो5ध्वगमन त्वरा । भोक्तुरप्यत्र राजेद्र तअयमेतज्न झास्यते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5911)
- **Original**: 53 विश्वेदेबास्सपितरस्तथा मातामहा नृप । कुल चाप्यायते युंसां सर्व॑ श्राद्ध प्रकुर्बताम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5912)
- **Original**: 54 सोमाधार: पितृगणो योगाधारश्न चन्द्रमा: । श्राद्धे योगिनियोगस्तु तस्माद्धपाल झस्यते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5913)
- **Original**: 55 सहस््रस्थापि विध्राणां योगी चेत्पुरत: स्थित: । सर्वान्भोक्तृंस्तारयति यजमानं तथा नृप
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5914)
- **Original**: 56 तृतीय अं 213 कामनाओंको पूर्ण कर देते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5915)
- **Original**: दौहिल् (छड़कीका लड़का) , कुतप (दिनका आठमों मुहूर्त) और तिछ--ये तीन तथा चाँदीका दान और उसकी बातचीत करना--ये सब श्राद्धकालमें पवित्र माने गये हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5916)
- **Original**: हे राजेन्द्र ! श्राद्धकर्ताके लिये क्रोध, मार्गगमन और उतावलापन---ये तीन बातें वर्जित हैं; तथा श्राद्में भोजन करनेबात्मेंको भी इन तीनॉका करना उचित नहीं है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5917)
- **Original**: पितृगण, मातामह तथा कुट्म्बीजन--सभी सन्तृष्ट हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5918)
- **Original**: हे घूपाछ ! पित॒गणक्ध्र आधार चन्रमा है और चन्द्रमाका आधार योग है, इसल्थयि श्राद्धपें योगिजनकों नियुक्त करना अति उत्तम है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5919)
- **Original**: हे राजन्‌! यदि श्राद्धभोजी एक सहस्र ्राह्मणोंके सम्मुख एक योगी भी हो तो जसह यजमानके सहित उन सबका उद्धार कर देता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5920)
- **Original**: 56 ।! वतन कै तन इति श्रीविष्णुपुराणे ठृत्तीयेंडशे पद्धदशो5ध्याय:
- **Translation**: 

---

