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

### Verse 1 (Sama Ved 0.3681)
- **Original**: 1440. प्रत्यस्मै पिपीषते विश्वानि विदुषे भर ।अरड्डमाय जग्मये5पश्चादध्वने नर:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3682)
- **Original**: हे याजको ! यज्ञसंचालन कर्त्ता, सर्वज्ञाता, यज्ञकर्मा, अग्रगामी, प्रगतिशील तथा सोम -पान की कामना वाले इद्धदेव के लिए सोमरस (कलश पात्र में) भर दें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3683)
- **Original**: 1441. एमेन॑ प्रत्येतन सोमेभि: सोमपातमम्‌ । अमत्रेभिऋजीषिणमिन्द्र सुतेभिरिन्दुभि:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3684)
- **Original**: हे ऋत्विजो ! संस्कारित-रसयुक्त, दीप्तिमान्‌ सोमरस को रुचिपूर्वक सोम के पात्रों से ही अत्यधिक मात्रा में पान करने वाले इन इन्द्रदेव के पास जाकर प्रार्थना करो
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3685)
- **Original**: 1442. यदी सुतेभिरिन्दुभि: सोमेभि: प्रतिभूषथ । वेदा विश्वस्य मेथिरो धृषत्तन्तमिदेषते
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3686)
- **Original**: हे ऋत्विजो ! रसयुक्त, दीप्तिबान्‌ सोम को लेकर इन्द्रदेव की शरण में जाने पर, वे आपके मनोरथों को जानते हुए, विघ्नों को दूर करते हुए, सभी इच्छाओं को पूर्ण कर देंगे
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3687)
- **Original**: 13.2 .... सामवेद-संहिता 1443. अस्माअस्मा इदन्धसो5 ध्वयों प्र भरा सुतम्‌ । कुवित्समस्य जेन्यस्य शर्धतो5भिशस्तेरवस्वरत्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3688)
- **Original**: हे अध्वर्युगणो ! इन इन्द्रदेव के लिए प्राण-रूप सोमरस भरपूर प्रदान करो । वे इन््रदेव स्पर्धा योग्य, जीतने योग्य शत्रुओं को विनष्ट करके आपकी रक्षा करेंगे
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3689)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3690)
- **Original**: केकेके
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3691)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3692)
- **Original**: 1444. बश्रवे नु स्वतवसे5रुणाय दिविस्पूशे । सोमाय गाथमर्चत
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3693)
- **Original**: हे स्तुति करने वालो ! भूरे रंग के, बलशाली, अरुणिमायुक्त, आकाश में रहने वाले, दिव्य सोम की आप लोग स्तुति करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3694)
- **Original**: 1445, हस्तच्युतेभिरद्विभिःसुतं सोम॑ पुनीतन। मधावा धावता मधु
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3695)
- **Original**: हे ऋत्विजो ! पाषाणों से कूटकर निष्पनन सोमरस को शोधित करो । उस मधुर सोमरस में, मधुर गो-दुग्ध मिश्रित करो
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3696)
- **Original**: 1446. नमसेदुप सीदत दध्नेदभि श्रीणीतन । इन्दुमिन्द्रे दधातन
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3697)
- **Original**: हे क्त्विजो ! इस सोमरस को नमस्कारपूर्वक दही में मिलाकर रखो । इस दीप्तिमान्‌ सोमरस को इद्धदेव को पीने के लिए अर्पित करो
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3698)
- **Original**: 1447. अमित्रहा विचर्षणि: पवस्व॒ सोम शं गवे । देवेभ्यो अनुकामकृत्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3699)
- **Original**: हे दिव्य सोम ! शत्रुनाशक सर्वद्रष्टा, देवों की इच्छानुसार कार्य करने वाले, आप हमारी गौओं को सुख दें (सुख पूर्वक रखें)
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3700)
- **Original**: 1448. इन्द्राय सोम पातवे मदाय परि षिच्यसे
- **Translation**: 

---

