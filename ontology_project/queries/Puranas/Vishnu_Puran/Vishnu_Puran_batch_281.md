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

### Verse 1 (Vishnu Puran 0.5601)
- **Original**: 20 नासमझसशीलैस्तु सहासीत कथझ्न। सदवृत्तसन्निकर्षो हि क्षणार्द्धमपि झस्यते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5602)
- **Original**: 29 विरोध॑ नोत्तमैर्गस्छेन्नाधमैश्ञ सदा बुध: । विवाहश्च॒ विवाद ॒तुल्यशीलैनुपेष्यते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5603)
- **Original**: 22 नारभेत कलि प्राज्ञइशुष्कवैरं च॒ वर्जयेत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5604)
- **Original**: अप्यल्पहानिस्सोढवब्या बैरेणार्थागर्म त्यज़ेत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5605)
- **Original**: 23 स््रातो नाड्रानिसम्माजेंत्त्रानश्ञास्था नपाणिना । न च निर्धुनयेत्केशान्नाचामेचैब चोत्थित:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5606)
- **Original**: 24 पादेन नाक्रमेत्पाद न पूज्याभिमुर्ख नयेत । नोघासन गुरोग्ये भजेताविनयान्वित:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5607)
- **Original**: 25 अपसब्धं न गच्छेन्च देवागारचतुष्पथान्‌। माड़ल्यपूज्यांश तथा विपरीतात्न दक्षिणम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5608)
- **Original**: 26 तृतीय अंझ 201 हे प्रभो ! बिचक्षण पुरुष मुँछ-दाढ़ीके आत्त्रेंको न चबाये, दो ढेलॉंकों परस्पर न रगड़े और अपवित्र एवं निन्दित नक्षत्रोंको न देखे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5609)
- **Original**: नग्न परखीको और उदय अथवा अस्त होते हुए सूर्यको न देखे तथा राव और हाल-गख्से घणा न करे, क्योंकि शाव-गश्ध सोमका औद्द है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5610)
- **Original**: चौराहा, चैत्यवृक्ष, उ्मशान, उपवन और दुष्टा खीकों समीपता--इन सबका रात्रिके समय सर्वदा त्याग करे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5611)
- **Original**: बुद्धिमान्‌ पुरुष अपने पूजनोय देवता, ब्राह्मण और तेजोमय पदार्थोक्ती छायाकों कभी न ह्मघरे तथा शून्य वनखण्डी और शून्य घरमें कभी अकेला न रहे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5612)
- **Original**: केगा, अस्थि, कण्टक, अपचित्र वस्तु, बलि, भस्म, तुष तथा स्रानके कारण भीगी हुई पृथिवीका दूरहीसे त्याग करे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5613)
- **Original**: प्राज्ञ पुरुषको चाहिये कि अनार्य व्यक्तिका सह्ढ न करे, कुटिल् पुरुषमें आसक्त न हो, सर्पके पास न जाय और जग पड़नेपर अधिक देरतक केटा न रहे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5614)
- **Original**: हे नरेश्वर ! बुद्धिमान्‌ पुरुष जागने, सोने, स्नान करने, बैठने, शाय्यासेवन करने और व्यायाम करनेमें अधिक समय न लगाये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5615)
- **Original**: हे राजेन्द्र ! प्राज्ञ पुरुष दाँत और सींगवाले पशुओंको, ओसको तथा सामनेकी वायु और घूपको सर्वदा परित्याग करे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5616)
- **Original**: नम्म होकर स्नान, शयत और आचमन न करे तथा केश खोलकर आचमन और देव-पूजन न करे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5617)
- **Original**: होम तथा देवार्चन आदि क्रियाऑँमें, आचमनमें, पुण्याहवाचनमें और जपमें एक वख््र धारण करके प्रवुत्त न हो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5618)
- **Original**: संशयशोल ब्यक्तियोंके साथ कभी न रहे। सदाचारी पुरुषोंका तो आधे क्षणका सज्ष भी अति प्रशंसनीय होता है।215
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5619)
- **Original**: बुद्धिमान्‌ पुरुष उत्तम अथबा अधम व्यक्तियॉंसे विरोध न करे । है राजन्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5620)
- **Original**: खि्ाह और विवाद सदा समान व्यक्तियोंसे ही होना चाहिये
- **Translation**: 

---

