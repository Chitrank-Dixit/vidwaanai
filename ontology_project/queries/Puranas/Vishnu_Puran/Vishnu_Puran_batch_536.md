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

### Verse 1 (Vishnu Puran 0.10701)
- **Original**: हे नाथ ! जलूको आशासे मृगतृष्णाके समान मैंने दुःखोंको ही सुस्त समझकर ग्रहण किया था; परन्तु वे मेंरे सन्‍्तापके ही कारण हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10702)
- **Original**: हे प्रभो ! राज्य, पूथिवी, सेना, कोदा, मित्रपक्ष, पुत्रगण, सखी तथा सेवक आदि और हाव्दादि खिषय इन सबको मैंने अविनाज्ञों तथा सुख-सुद्धिसे हो अपनाया था; किन्तु हे ईश
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10703)
- **Original**: परिणाममें वे ही दुःखरूप सिद्ध हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10704)
- **Original**: है नाथ ! जब देवस्प्रेक प्राप्त करके भी देवताओँको मेरी सहायताकी इच्छन्न हुई तो उस (स्वर्गलोक) में भी नित्य-शान्ति कहाँ है 7
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10705)
- **Original**: हे परमेश्वर
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10706)
- **Original**: सम्पूर्ण जगत्‌की उत्पत्तिके आदि-स्थान आपकी आराधना किये ब्रिना कौन शाश्वत शान्ति प्राप्त कर सकता है ?
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10707)
- **Original**: हे प्रभो ! आपकी मायासे मूढ हुए. पुरुष जन्म, मृत्यु और जरा आदि सन्तापोंक्ी भोगते हुए अन्त्में यमराजका दर्शन करते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10708)
- **Original**: आपके स्वरूपको न जाननेवाले पुरुष नरकोंमें पड़कर अपने कर्मोंके फलस्वरूप नाना मकारके दारुण क्वेश पाते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10709)
- **Original**: हे परमेश्वर ! मैं अत्यन्त विषयी हूँ. और आपकी मायासे मोहित होकर मसत्वाधिमानके गड्ठेपें भटकता रहा हूँ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10710)
- **Original**: वही मैं आज अपार और अप्रपेय परमपदरूप आप परमेश्वस्की झरणगें आया हूँ जिससे भिन्न दूसरा कुछ भी नहीं है, और संसारभ्रमणके स्तेदसे खिलन्न-चित्त होकर मैं निरतिशय तेजोमय निर्वाणस्वरूप आपका हो अभिहय्रणी हूँ”
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10711)
- **Original**: अफसर जौ कफसः जति श्रीविष्ण॒पुराणे पड्ममेंडश्े त्योविशोष्ष्याय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10712)
- **Original**: जन जुट ऑन
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10713)
- **Original**: अ0 24 ] पद्चम अंश चोबीसवाँ अध्याय मुचुकुन्दका तपस्याके लिये प्रस्थान और बलरामजीकी क्रजयात्रा अीपराशर उदाच इल्थे स्तुतस्तदा तेन मुचुकुन्देन धीमता। प्राहेश: सर्वभूतानामनादिनिधनो हरिः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10714)
- **Original**: 9 औभगयातुवाच यथाभिवाञिततान्दिव्यानाच्छ लोकान्नराध्रिप । अव्याहतपरैश्नयों मत्प्तादोपबृंहित:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10715)
- **Original**: 2 भुक्त्वा दिव्यात्महाभोगान्भविष्यसि महाकुले । जातिस्मरो मत्प्रसादात्ततों मोक्षमवाप्स्यसि
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10716)
- **Original**: 3 शऔपयाशर उवाच इत्युक्त: प्रणिपत्येश॑ जगतामच्युतं॑ नृप: । शुहामुखाद्विनिषक्रात्तस्स ददर्शाल्पकाज़्रान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10717)
- **Original**: 4 ततः कलियुग मत्वा प्राप्त तप्तुं नृपस्तप: । नरनारायणस्थान॑ प्रययौ गन्धमादनम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10718)
- **Original**: 5 कृष्णो5षपि घातयित्वारिमुपायेन हि तदलम्‌। जग्राह मथुरामेत्य हस्त्यश्वस्यन्दनोग्ज्वलम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10719)
- **Original**: 6 आनीय चोग्रसेनाय द्वारवत्यां न्यवेदयत्‌। पराभिभवनिदशडुं बभूब चर यदो: कुलम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10720)
- **Original**: 7 बलदेबो5पि मैत्रेय प्रश्मान्तासिलविग्रह: । ज्ञातिदर्शनसोत्कण्ठ: प्रययो ननन्‍्दगोकुलम
- **Translation**: 

---

