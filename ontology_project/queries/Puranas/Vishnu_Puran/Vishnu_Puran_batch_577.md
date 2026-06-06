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

### Verse 1 (Vishnu Puran 0.11521)
- **Original**: अराज्याह यदोर्वश्ञमवेक्ष्य मुसलायुधम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11522)
- **Original**: 12 भो भो किमेतद्धवता बलभद्रेरितं बच: । आज्ञां कुरुकुलोत्थानां यादव: कः प्रदास्यति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11523)
- **Original**: 13 उग्रसेनो5पि यद्याज्ञां कौरवाणां प्रदास्यति । तदले :
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11524)
- **Original**: 14 तद्च्छ बल मा वा त्व॑ साम्बमन्यायचेष्टितम्‌ । विमोक्ष्यामो न भवतश्नोग्रसेनस्थ शासनात्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11525)
- **Original**: 15 प्रणतिर्या कृतास्माक॑ मान्यानाँ कुकुरान्धकै: । ननाम सा कृता केयपमाज्ञा स्वामिनि भृत्यतः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11526)
- **Original**: 16 गर्वमारोपिता यूयं॑ सपरानासनभोजनै: । को दोषों भवतां नीतिर्य॑त्रीत्या नावलोकिता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11527)
- **Original**: 17 अस्माभिरघों भवतो यो5यं बल निवेदितः । प्रेम्णैतब्रैतदस्माक॑ कुलाध्युष्मत्कुलोचितम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11528)
- **Original**: 18 अपराशर उकाच इत्युक्त्वा कुरत: साम्बं मुझ्ामो न हरेस्सुतम्‌ । कृतैकनिश्चयास्तूर्ण बिविशुर्गजसाह्ृयम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11529)
- **Original**: 19 मत्त: कोपेन चाघूर्णस्ततो5थघिक्षेपजन्मना । उत्धाय पाष्ण्या वसुधां जघान स हलायुध:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11530)
- **Original**: 20 ततो विदारिता पृथ्वी पा्ष्णिघातान्पहात्मन: । आस्फोटबामास तदा दिद्वश्शब्देन पूरयन्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11531)
- **Original**: 21 उबाच चातिताग्राक्षो भुकुटीकुटिलाननः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11532)
- **Original**: 22 अहो मदावलेपोउयमसाराणां दुरात्मनाम्‌। कौरवाणां महीपत्वपस्मांकं किल कालजम्‌ । उम्रसेनस्य ये नाज्ञां मन्यन्तेडल्यापि छल्लनम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11533)
- **Original**: 23 उम्रसेन: समध्यास्ते सुधर्मो न शाचीपति: । धिझ्लनुषशतोच्छिष्टे. तुष्टिरिषां. नृपासने
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11534)
- **Original**: 24 तुस्त छोड़ दें"
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11535)
- **Original**: है द्विजससत्तम ! बलरामजीके इन वचनॉकों सुनकर भीष्ण, द्रोण, कर्ण और दुर्योधन आदि राजाओंको बड़ा क्षोभ हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11536)
- **Original**: और यदुवंदकों राज्यफदके अयोग्य समझ बाह्लिक आदि सभी क्वौरवगण कुपित होकर मूसलूधारी बलभद्रजीसे कहने लगे--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11537)
- **Original**: “हे बलभद्र ! तुम यह क्या कह रहे हो; ऐसा कौन यदुवंश्ञी है जो कुरुकुस्मेत्पन्न किसी वीरको आज्ञा दे ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11538)
- **Original**: यदि उग्रसेन भी कौस्वोंको आज्ञा दे सकता है तो राजाओंके योग्य कौरबोंके इस श्वेत छत्रका क्या प्रयोजन है 7
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11539)
- **Original**: अतः है बलराम ! तुम जाओ अधबा रहो, हमलोग तुम्हारी या उग्रसेनकी आज्ञासे अन्यायकर्मा साम्बको नहीं छोड़ सकते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11540)
- **Original**: पूर्वकालमें कुकुर और अन्धकवंश्ीय यादवगण हम माननीयोंको प्रणाम किया करते थे सो अब वे ऐसा नहीं करते तो न सही किन्तु स्वामीको यह सेवककी ओरसे आज्ञा देना कैसा?
- **Translation**: 

---

