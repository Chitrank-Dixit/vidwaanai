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

### Verse 1 (Vishnu Puran 0.1561)
- **Original**: महता राजराज्येन पृथुर्वैन्य: प्रतापवान्‌। इस प्रकार महातेजस्वी और परम प्रतापी वेनपुत्र सो5भिषिक्तो महातेजा विधिवद्धर्मकोबिदेः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1562)
- **Original**: धर्मकृडल महानुभावोंद्वारा विधिपूर्वक्त अति महान्‌ पित्राउपरक्चितास्तस्थ प्रजास्तेनानुरस्चिता: राजराजेश्वरफ्दपर अभिषिक्त हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1563)
- **Original**: जिस प्रजाको राजतास्तस्थ नुरक्षिता: । पिताने अपरक्त (अप्रसन्न) किया था उसीको उन्होंने अनुरागात्ततस्तस्थ नाम राजेत्यजायत
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1564)
- **Original**: अनुरक्षित (प्रसन्न) किया, इसलिये अनुरक्षन करनेसे आपस्तस्तम्भिरे चास्थ समुद्रमभियास्यत:ः । उनका नाम 'राजा' हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1565)
- **Original**: जब वे ससुद्रगें चलते पर्वताश्न॒दर्दुर्मार्ग थे, तो जल यहनेसे रुक जाता था, पर्वत उन्हें मार्ग देते थे व्जभजध नमतत
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1566)
- **Original**: 2, उनकी ध्वजा कभी भंग नहीं हुई
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1567)
- **Original**: पृथियी अकृष्टपच्या पृथिवी सिद्धघन्यन्नानि चित्तया। बिना जोते-नोये धान्य पकानेबाली थी; केशरू चिष्तन- सर्वकामदुघा गाव: पुटके पुटके मधु
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1568)
- **Original**: सात्रसे हीं अन्न सिद्ध हो जाता था, गौएँ कामधेनु- तस्य ये जातमात्रस्य यज्ञे पैतामहे शुभे।
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1569)
- **Original**: रूपा थों और पत्ति-पत्तेमें मधु भरा रहता था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1570)
- **Original**: 5 साला है द राजा पृथुने उत्पन्न होते ही पैतामह यज्ञ किया; उससे सूतः सूत्यां समुत्यन्न: सौत्येडहनि पहामति:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1571)
- **Original**: 51 तोमा न ये सम कप के वजमस गह डिक कल तस्मिश्नेव महायज्ले जज्ञे प्राज्ञोडथ मागधः । जमा न सोमाभिषवर्ूमि) सूतको उत्पत्ति हुई
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1572)
- **Original**: उसी महायज्ञषमें बुद्धिमात्‌ प्रोक्तौ तदा मुनिवरैस्ताबुभौ सूतमागधौं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1573)
- **Original**: मागधका भी जन्म हुआ। तब मुनिवरोनि उन दोनों सृत स्तूयतामेष नृषतिः पृथुर्वैन्य: प्रतापबान्‌। और मागधोंसे कहा--
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1574)
- **Original**: "तुम इन प्रतापवान्‌ कर्ेतदनुरूप वां पाए बैन महाराज पृथुकी स्तुति करो । तुम्हारे योग्य यही कार्य कर्मैतदनुरूप वां पात्र स्तोत्रस्य चापरम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1575)
- **Original**: 53 है और राजा भी स्तुतिके ही योग्य हैं'
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1576)
- **Original**: तब उन्जेंनि ततस्तावूचतुर्विप्रास्सबनिव._ कृताझली । हाथ जोड़कर सब्र क्राह्मणॉसे कहा--'ये महाराज तो अद्य जातस्थ नो कर्म ज्ञायतेउस्थ महीपतेः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1577)
- **Original**: आज हो उत्पन्न हुए हैं, हम इनके कोई कर्म तो जानते ही शुणा न चास्य ज़ायन्ते न चास्य प्रथितं यहा: । नहीं हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1578)
- **Original**: अभी इनके न तो कोई गुण प्रकट हए 4 स्तोत्रे किमाश्रयं त्वस्य कार्यमस्माभिरुच्यताम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1579)
- **Original**: रे ते यज्ञ ही सस्क गत, हुआ है; फिर कहिये, हम किस बराक आधारपर 40 2
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1580)
- **Original**: 8 ऋषिगण बोले--ये महाबली चक्रवर्ती महाराज करिष्यत्येष यत्कर्म चक्रवर्ती महाब॒ल: । भविष्यमें जजे-जों कर्म करेंगे और इनके जो-जो भावी गुण गुणा भविष्या ये चास्य तैरयं स्तूयतां नृपः
- **Translation**: 

---

