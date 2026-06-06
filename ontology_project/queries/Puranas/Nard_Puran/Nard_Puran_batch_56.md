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

### Verse 1 (Nard Puran 0.1101)
- **Original**: द्वितीयश्ष तृतीयश्च चतुर्थ: षष्ठपद्चमौ। उसे लज्जित कहते हैं)। नारदजी ! यदि बहुतोंमेंसे
- **Translation**: 

---

### Verse 2 (Nard Puran 0.1102)
- **Original**: एकादश: कतिपयथ: कतिथ्: कति नारद
- **Translation**: 

---

### Verse 3 (Nard Puran 0.1103)
- **Original**: किसी एककी अधिक विशेषता बतानी हो तो तम दोमेंसे एकका और बहुतोंमेंसे एकका निश्चय और इष्ठ प्रत्यय होते हैं और दोमेंसे एककी
- **Translation**: 

---

### Verse 4 (Nard Puran 0.1104)
- **Original**: करनेके लिये “किम्‌' “यतू' और “तत्‌' शब्दोंसे विशेषता बतलानी हो तो तर और ईयसु प्रत्यय
- **Translation**: 

---

### Verse 5 (Nard Puran 0.1105)
- **Original**: क्रमशः डतर और डतम प्रत्यय होते हैं। यथा-- भवतो: होते हैं। ईयसुमें उकार इत्संज्ञक है। अयम्‌ एषां
- **Translation**: 

---

### Verse 6 (Nard Puran 0.1106)
- **Original**: कतर:' श्याम: (आप दोनोंमें कौन श्याम है?) अतिशयेन प्रशस्य: श्रेष्ठ: (यह इन सबमें अधिक
- **Translation**: 

---

### Verse 7 (Nard Puran 0.1107)
- **Original**: भवतां कतम: श्रीराम: ? (आपलोगोंमें कौन श्रीराम प्रशंसनीय है, अत: श्रेष्ठ है)
- **Translation**: 

---

### Verse 8 (Nard Puran 0.1108)
- **Original**: ट्रयो: प्रशस्य श्रेयान्‌
- **Translation**: 

---

### Verse 9 (Nard Puran 0.1109)
- **Original**: संख्या (गणना) करनेयोग्य वस्तुविशेषका (दोमेंसे जो एक अधिक प्रशंसनीय है, वह श्रेयान्‌
- **Translation**: 

---

### Verse 10 (Nard Puran 0.1110)
- **Original**: निश्चय करनेके लिये ट्वि-शब्दसे द्वितीय, त्रि- कहलाता है। यहाँ भी प्रशस्य+ईयस्‌* श्रेयस्‌ ( पूर्ववत्‌
- **Translation**: 

---

### Verse 11 (Nard Puran 0.1111)
- **Original**: शब्दसे तृतीय", चतुर्‌-शब्दसे चतुर्थ और षषू- श्र आदेश हुआ)
- **Translation**: 

---

### Verse 12 (Nard Puran 0.1112)
- **Original**: इसके रूप इस प्रकार हैं-- श्रेयान्‌
- **Translation**: 

---

### Verse 13 (Nard Puran 0.1113)
- **Original**: शब्दसे षष्ठ रूप बनते. हैं। इनका अर्थ क्रमश: इस श्रैयांसौ श्रेयांस: । श्रेयांसम्‌ श्रेयांसौ श्रेयस:
- **Translation**: 

---

### Verse 14 (Nard Puran 0.1114)
- **Original**: श्रेयसा
- **Translation**: 

---

### Verse 15 (Nard Puran 0.1115)
- **Original**: प्रकार है-दूसरा,.. तीसरा, चौथा और छठा। श्रेयोभ्याम्‌ श्रेयोभि; इत्यादि। इसी प्रकार जो
- **Translation**: 

---

### Verse 16 (Nard Puran 0.1116)
- **Original**: पञ्चनू, सप्तनू, अषप्टनू, नवनू और दशनू-इन दोमेंसे एक अधिक कृष्ण है, उसे कृष्णतर और
- **Translation**: 

---

### Verse 17 (Nard Puran 0.1117)
- **Original**: शब्दोंके 'न्‌' कास्को मिटाकर '“म'कार बढ़ जाता जो बहुतोंमेंसे एक अधिक शुक्ल है, उसे शुक्लतम
- **Translation**: 

---

### Verse 18 (Nard Puran 0.1118)
- **Original**: है, जिससे पञ्षम, सप्तम, अष्टम, नवम, दशम रूप कहते हैं। कृष्ण+ तर-कृष्णतर। शुक्ल *तम-शुक्लतम ।
- **Translation**: 

---

### Verse 19 (Nard Puran 0.1119)
- **Original**: बनते हैं। एकादेशन्से अष्टादशन्‌तक उक्त अर्थमें किम, क्रियावाचक शब्द (तिडन्त) और अव्ययसे
- **Translation**: 

---

### Verse 20 (Nard Puran 0.1120)
- **Original**: “न्‌' कारका लोप॑ 'होकर सभी शब्द अकारान्त हो परे जो तम और तर प्रत्यय हैं, उनके अन्तमें आम्‌
- **Translation**: 

---

