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

### Verse 1 (Sama Ved 0.3081)
- **Original**: जैसे गौएँ बछड़ों की ओर रैभाती हुई जाती हैं. उसी प्रकार शब्द करते हुए सोम कलश में प्रवेश करता है और हाथों में धारण किया जाता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3082)
- **Original**: 1194. जुष्ट इन्द्राय मत्सर: पवमान: कनिक्रदत्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3083)
- **Original**: विश्वा अप द्विषो जहि
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3084)
- **Original**: हे इन्द्रदेव को तृप्त करने वाले सोमदेव ! आप पवित्र होकर शब्द करते हुए सब शत्रुओं का विनाश करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3085)
- **Original**: 31195, अपघ्नन्तो अराग्ण: पवमाना:ः स्वर्देशः
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3086)
- **Original**: योनावृतस्य सीदत
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3087)
- **Original**: है दिव्य सोमदेव ! दान न देने वाले स्वार्थियों का नाश करते हुए, अपने तेजस्वी रूप में, आप यज्ञस्थल पर विराजमान हों
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3088)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3089)
- **Original**: केक के
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3090)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3091)
- **Original**: 1196. सोमा असुग्रमिन्दवः सुता ऋतस्य धारया । इन्द्राय मधुमत्तमा:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3092)
- **Original**: यज्ञ के लिए शोधकर तैयार किये गये, मधुर रस-संयुक्त सोम को इन्द्रदेव के निमित्त प्रस्तुत करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3093)
- **Original**: 1197. अभि विप्रा अनूषत गावो वत्सं न धेनवः। इन्द्र सोमस्य पीतये
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3094)
- **Original**: हे ऋत्विजो ! जिस प्रकार गौएँ अपने बछड़ों के लिए व्याकुल हो जाती हैं, उसी भाव से सोम पीने के लिए इन्द्रदेव की स्तुति करो
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3095)
- **Original**: 1198. मदच्युत्क्षेति सादने सिन्धोरूर्मा विपश्चित्‌ । सोमो गौरी अधि श्रित:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3096)
- **Original**: हर्ष बढ़ाने वाला सोमरस यज्ञ स्थान में प्रतिष्ठित होता है । नदी की तरंगों के समान यह बाणी को तरंगित करता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3097)
- **Original**: 9199. दिवो नाभा विचक्षणो5व्या वारे महीयते
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3098)
- **Original**: सोमो यः सुक्रतु: कवि:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3099)
- **Original**: श्रेष्ठकर्मा, ज्ञानयुक्त यह दिव्य सोम है, जो अन्तरिक्ष की नाभि के समान छले में शुद्ध होकर महिमा - मण्डित होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3100)
- **Original**: 1200. यः सोम: कलशेष्वा अन्त: पवित्र आहितः । तमिन्दु: परि षस्वजे
- **Translation**: 

---

