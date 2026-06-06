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

### Verse 1 (Vishnu Puran 0.2301)
- **Original**: इसल्च्ये दैत्यभाककों छोड़कर हम और तुम ऐसा यल्न करें जिससे शान्ति व्थभ कर सकें
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2302)
- **Original**: जो [ परम शान्ति ) अग्नि, सूर्य, चद्भरमा, बायु, मेघ, वरुण, सिद्ध, राक्षस, यक्ष, दैत्यराज, सर्प, कित्नर, मनुष्य, पशु और अपने दोषोंसे तथा ज्बर, नेत्ररोग, अतिसार, प्लीहा (तिल्‍ली) और गुल्म आदि रोगोंसे एवं द्वेष, ईर्ष्या, मत्सर, राग, ल्लरेभ और किसी अन्य भावसे भी कभी क्षीण नहीं होती, और जो सर्वदा अत्यत्त निर्मल है ठसे मनुष्य अमलख्वरूप श्रीकेशवमें मनोनिवेश करनेसे प्राप्त कर लेता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2303)
- **Original**: 86--<9
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2304)
- **Original**: हे दैत्यो ! मैं आग्रहपूर्वक कहता हूँ. तुम इस असार संसारके विषयोमें कभी सन्तुष्ट मत होना। तुम सर्वत्र समदृष्टि करो, क्योंकि समता ही श्रीअच्युतकी [ वास्तविक ] आयाधना है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2305)
- **Original**: उन अच्युतके प्रसन्न होनेपर फिर संसारमें दुर्लभ ही क्या है? तुम घर्म, अर्थ और कामकी इच्छ्म कभी न करना; ये तो अह्यन्त सुच्छ हैं। उसे ब्रह्मकप महाव॒क्षका आश्रय लेनेपर तो तुम निःसन्देह [ मोक्षरूप
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2306)
- **Original**: महाफल प्राप्त न्रिःसंज्य प्राप्यथ वै महत्फलम
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2307)
- **Original**: कर लोगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2308)
- **Original**: हि अब ऋऔ 'इिाकेकंमम मर, इति श्रीविष्णुपुराणे प्रथमेंडशे सप्तदशो5्ध्याय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2309)
- **Original**: आ* 18 ] प्रथम अंश अठारहवाँ अध्याय अह्लादको मारनेके लिये जिष, हास्र और अभ्रि आदिका प्रयोग एवं प्रह्लादकृत भगबत-स्तुति औपरार उवाच तस्वैतां दानवाश्ेष्टो दृष्ठा दैत्यपतेर्भयात्‌ । आचचस्यु: स चोबाच सूदानाहुय सत्वर:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2310)
- **Original**: 1 हिरण्यकशिपुरुवाच है सूद्या मम पुन्नोइसाबन्येषामपि दुर्मति: । कुमार्गदेशिको दुष्टो हन्यतामविलम्बितम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2311)
- **Original**: 2 हालाहले विष तस्य सर्वभक्षेपु दीयताम्‌। अविज्ञातमसौ पापो हन्यतां मा बिचार्यताम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2312)
- **Original**: 3 श्रीपयारार उकाच ते तथैव ततश्नक्त: प्रह्लादाय महात्मने । विधदान यथाज्ञप्तं पिनत्रा तस्य महात्मन:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2313)
- **Original**: 4 हालाहलं बविर्ष घोरमनन्तोशारणेत सः। अभिमनत्रम सहान्नेन मैत्रेय बुभुजे तदा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2314)
- **Original**: 5 अविकारं स तद्भुकत्वा प्र्माद: स्वस्थमानस: । जरयामास तद्दिषम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2315)
- **Original**: 6 ततः सूदा भयत्रस्ता जी दृष्ठा महद्विषम्‌। दैल्येश्वरपुपागम्य अणिपत्येदमन्रुवन्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2316)
- **Original**: 7 दैत्यराज विष दत्तमस्माभिरतिभीषणम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2317)
- **Original**: जीर्ण तेन सहाप्नेन प्रह्वादेन सुतेन ते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2318)
- **Original**: 8 हिरण्यकशिपुरुवाच त्वय॑तां ल्वर्यतां हे हे सद्यो दैत्यपुरोहिता: । कृत्यां तस्य विनाशाय उत्पादयत मा चिरम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2319)
- **Original**: 9 श्रीपएसर उवाच सकाहामागम्य ततः प्रह्लादस्यथ पुरोहिता सामपूर्वमथोचुस्ते प्रह्मांद विनयान्क्तिम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2320)
- **Original**: 10 जातख्लैलोक्यविख्यात आयुष्मन्रह्मण: कुले दैत्वराजस्थ तनयो हिरण्यकशिपोर्भवान्‌
- **Translation**: 

---

