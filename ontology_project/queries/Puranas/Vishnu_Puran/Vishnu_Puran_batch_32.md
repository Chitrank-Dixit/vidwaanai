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

### Verse 1 (Vishnu Puran 0.621)
- **Original**: 49 विनिन्‍्दकानां वेदस्य यज्ञव्याघातकारिणाम्‌ । स्थानमेतत्समाख्यात॑ स्वधर्मत्यागिनश्व ये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.622)
- **Original**: पाते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.623)
- **Original**: चन्द्र और सूर्य आदि ग्रह भी अपने-अपने व्त्रेकॉमें जाकर फिर लौट आते हैं, किन्तु द्रादझाक्षर मनन्‍ल (73% नमो भगवते वासुदेवाय) का चिन्तन करनेवाले अभीतक मोक्षफदसे नहीं लौटे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.624)
- **Original**: वापिस, अशख्तामिस््र, महारौरव, रौरब, असिपत्रवन, घोर, काल्सूत्र और अलीचिक आदि जो नरक हैं, लें वेदोंकी निन्‍्दा और यज्ञॉका उच्छेद करनेयाले तथा स्वधर्म-बिमुख पुरुषोंके स्थान कहे गये हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.625)
- **Original**: '41-डर
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.626)
- **Original**: अपन "री अलअ>-»न इति श्रीविष्णुपुराणे प्रथमेंडशे षष्ठोउघ्यायः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.627)
- **Original**: क्ततत बट तततन सातवाँ अध्याय मरीचि आदि प्रजापतिगण, तामसिक सर्ग, स्वायम्भुवमनु और झतरूपा तथा उनकी सनन्‍्तानका वर्णन आपयाशर उवाच ततो5भिध्यायतस्तस्य जज्ञिरे मानसाः प्रजा: । तच्छरीरसमुत्पन्नै: कार्यस्‍तै: करणै: सह । क्षेत्रज्ञा: समवर्त्तन्त गाश्नेभ्यस्तस्थ धीमत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.628)
- **Original**: 91 ते सर्बे समवर्त्तत्त ये मया प्रागुदाहता: । देवाह्या: स्थावरात्ताश् त्रैगुण्यतिषये स्थिता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.629)
- **Original**: 2 एवंभूतानि सृष्टानि चराणि स्थावराणि च
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.630)
- **Original**: 3 यदास्य ता: प्रजा: सर्वा न व्यवर्धन्त धीमत: । अधान्यान्पानसाय्पुत्रान्सदृशानात्मनो इसुजत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.631)
- **Original**: 4 भूर्गु पुलस्त्य॑पुलहँ क्रतुमड्विस्स तथा। मरीचिं दक्षपत्रिं चर वसिष्ठं चैव मानसान्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.632)
- **Original**: 5 नव ब्रह्माण इत्येते पुराणे निश्चय गता:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.633)
- **Original**: 6 ख्याति भूति च सम्भूति क्षमां प्रीति तयैस च । सन्नति चर तथैवोर्जामनसूयां तथेव च
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.634)
- **Original**: 7 प्रसूर्ति च ततः सृ्ठा ददो तेषां महात्मनाम्‌ । पत्यो भवध्वमित्युक्त्वा तेषामेव तु दत्ततान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.635)
- **Original**: 8 सननन्‍्दनादयो ये चर पूर्वसृष्टास्तु बेघसा। न ते स्लेकेघ्नसज्जन्त निरपेक्षा: प्रजासु ते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.636)
- **Original**: 9 सर्वे तेउभ्यागतज्ञाना खीतरागा बविमत्सरा: । तेप्वेज॑ निरपेक्षेषु व्थ्रेकसृष्टो. महात्मनः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.637)
- **Original**: 90 श्रीपराश्षस्जी बोछे--फिर उन प्रजापतिके ध्यान करनेपर उनके देहस्वरूप भूतोंसे उत्पन्न हुए शरीर और इच्द्रियॉँके सहित मासस प्रजा उत्पन्न हुई। उस समय मतिमान्‌ क्रह्माजीके जड शरीरसे ही चेतन जीवॉका प्रादुर्भाव हुआ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.638)
- **Original**: मैंगे पहले जिसका वर्णन क्रिया है, देवताओँसे लेकर स्थावरपर्यन्त वे सभी त्रिगुणात्मक चर और अचर जीव इसी प्रकार उत्पन्न हुए्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.639)
- **Original**: जब महाबुद्धिमान्‌ प्रजापतिकी वह प्रजा पुत्र- फौत्रादि-क्रमसे और न बढ़ी तब उन्होंने भृगु, पुलूस्त्य, पुलह, क्रतु, अंगिण, मरीचि, दक्ष, अञ्नि और वसिष्ठ-- इन अपने ही सदृश अन्य मानस-पुत्रोंकी सृष्टि की। पुराणोंसें ये नौ ब्रह्म माने गये हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.640)
- **Original**: ऊर्ज्ज, अनसूया तथा प्रसूति इन नौ कन्याओंको उत्पन्न कर, इन्हें उन महात्माओंको 'तुम इनकी पत्नी हो' ऐसा कहकर सौंप दिया
- **Translation**: 

---

