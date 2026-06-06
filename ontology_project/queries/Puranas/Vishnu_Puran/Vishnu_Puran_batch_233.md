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

### Verse 1 (Vishnu Puran 0.4641)
- **Original**: और हे द्विज
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4642)
- **Original**: इस चबैवस्वत- सन्वन्तस्के प्राप्त होनेषर भगवान्‌ दिप्णु कइुयपजीद्वारा अददितिके गर्भसे लामनरूप होकर प्रकट हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4643)
- **Original**: उन महात्मा खामनजीने अपनी तीन डर्गोंसे सम्पूर्ण लोकॉको जीतकर यह निष्काटक त्रिस्थ्रेकी इन्द्रकों दे दी थी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4644)
- **Original**: 166 श्रीविष्णुपुराण [ आन 2 इत्येतास्तनवस्तस्थ सप्नमन्वन्तरेषु . वे । है खिप्र ! इस प्रकार सातों मन्वन्तरोंमें भगवान्‌की ये सप्रस्वेबाभवन्विष्र याभ्रि: संवर्द्धिता: प्रजा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4645)
- **Original**: सात मूर्तियाँ प्रकट हुई, जिनसे (भविष्यमें) सम्पूर्ण यस्माद्विष्टमि्द विश्व तस्य शक्त्या महात्मनः । प्रजाकी युद्धि हुई
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4646)
- **Original**: यह सम्पूर्ण सिश्व उन तस्मात्स प्रोच्यते किष्णुरविश्रेर्धातो: प्रवेशनात्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4647)
- **Original**: परमात्पाकी ही शक्तिसे व्याप्त है; अतः खे 'विष्णु' कहल्लते सर्वे च॒ देवा मनवस्समस्ता .. सप्तर्षषों ये मनुसूनवश्ष। इन्द्क्ष योज्य त्रिदशेझ्भूतों... हैं, क्योंकि विद्ञ' धातुक् अर्थ प्रवेश करना है.
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4648)
- **Original**: समस्त देवता, मनु, सप्तर्षि तथा मनुपुत्र और देवताओंके अधिपति इन्द्रणण--ये सब भगवान्‌ विष्णुकी ही _ विष्णोरशेषास्तु विभूतयस्ता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4649)
- **Original**: विभूतियाँ हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4650)
- **Original**: _ ण-ण जुर उपाय इति श्रीविष्णुपुराणे तृतीयेंडदो प्रथमोड्ध्यायः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4651)
- **Original**: जज+ हऔ दूसरा अध्याय सावर्णिमनुकी उत्पत्ति तथा आगामी सात मन्‍्वन्तरोंके मनु, मनुपुत्र, देवता, इन्द्र और सप्नर्षियोंका वर्णन अऔमेतज्ेय उवबाच प्रोक्तान्येतानि भवता सप्ममन्वन्तराणि से । भविष्याण्यपि विप्र्षे ममाख्यातुं त्वमईसि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4652)
- **Original**: औपराशर उवाच सूर्यस्थ पत्नी संज्ञाभृत्तनया विश्वकर्मण: । मनुर्यमो यमी चैव तदपत्यानि कै सुने
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4653)
- **Original**: असहन्ती तु सा भर्तुस्तेजइछायां युयोज ये । भर्तुशुभ्रूषणे3रण्य स्वर्य चर तपसे ययों
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4654)
- **Original**: संज्ञेयमित्यथार्कश्ष॒ छायायामात्मजत्रयम्‌ । आनैश्वरं मनुं चान्ये तपतीं चराप्यजीजनत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4655)
- **Original**: छायासंज़ा ददो शाप॑ यमाय कुपिता यदा । तदान्येयमसौ.. बुद्धिरित्यासीछपसूर्ययो:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4656)
- **Original**: ततो विवस्वानाख्याते तयैवारण्यसंस्थिताम्‌ । समाधिदृष्टधा तदुशे तामश्चां तपसि स्थिताम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4657)
- **Original**: वाजिरूपधर: सो5थ तस्यां देवावधाश्विनो । जनयामास रेवन्तं रेतसोउन्ते च भास्कर:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4658)
- **Original**: आनिनये च पुन: संज्ञां स्वस्थानं भगवात्रवि: । तेजसइ्शमन चास्य विश्वकर्मा चकार ह
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4659)
- **Original**: श्रीमैत्रेयजी कोस्ठे--हे विप्रें ! आपने सह सात अतीत मन्बत्तरॉज्वी कथा कही, अब आप मुझसे आगामी 1
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4660)
- **Original**: मन्चन्तरोंका भी वर्णन कोजिये
- **Translation**: 

---

