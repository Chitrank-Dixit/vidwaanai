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

### Verse 1 (Sama Ved 0.1741)
- **Original**: के के के
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1742)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1743)
- **Original**: 672.उच्चा ते जातमन्धसो दिवि सदभूम्या ददे । उग्र शर्म महि श्रव:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1744)
- **Original**: हे सोमदेव ! शौर्यवर्द्धल, सुखदायक, महान्‌ यशस्वी, पोषक तत्व के रूप में आपको, भू लोक में हम प्राप्त करते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1745)
- **Original**: 673.स न इन्द्राय यज्यवे वरुणाय मरुदभ्य: । वरिवोवित्परि सत्रव
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1746)
- **Original**: हे ऐश्वर्य प्रदाता सोमदेव ! हमारे पूज्य इन्द्र, वरुण और मरुतों के लिए आप खबित हों
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1747)
- **Original**: 674.एना विश्वान्यर्य आ द्युम्नानि मानुषाणाम्‌। सिषासन्तो वनामहे
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1748)
- **Original**: हे सोमदेव ! मानवोचित ऐश्वर्य प्राप्त करके हम आपकी सेवा की इच्छा से आपकी अभ्यर्थना करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1749)
- **Original**: 675.पुनान: सोम धारयापो वसानो अर्पसि । आ रलधा योनिमृतस्य सीदस्युत्सो देवों हिरण्ययः
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1750)
- **Original**: हे ऐश्वर्यदाता, स्वर्ण के समान दमकने वाले. स्वच्छ, सोमदेव ! शोधन क्रम में जल से संयुक्त होकर, अविरल धारा के रूप में आप निश्चित ही यज्ञ- पात्र में प्रतिष्ठित होते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1751)
- **Original**: 676.दुहान ऊरधर्दिव्यं मधु प्रियं प्रततं सधस्थमासदत्‌ । आपृच्छ््यं धरुणं वाज्यर्षप्ति नृभिधौंतो विचक्षण:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1752)
- **Original**: यज्ञ कर्ताओं द्वारा परिष्कृत किया गया मधुर, आह्वादक, दिव्यरस सोम, यज्ञ वेदी पर स्थापित है । साधकों का निरीक्षक यह सोम, श्रेष्ठ यज्ञीय-भाव-सम्पन्न याजकों को प्राप्त होता है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1753)
- **Original**: 677.प्र तु द्रव परि कोशं नि षीद नृभिः पुनानो अभि वाजमर्ष । अष्टवं न त्वा वाजिनं मर्जयन्तो5च्छा बही रशनाभिर्नयन्ति
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1754)
- **Original**: याजकों द्वारा शोधित हे सोमदेव ! हविरूप पोषक आहार के रूप में आप शीघ्र हो कलश में स्थापित हों बलवान्‌ घोड़े को स्वच्छ करने वालों की तरह आपको शोधित करते वाले क़्म्रल्वजू, अँगुलियों के माध्यम से आपको यज्ञ स्थान पर ले जाते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1755)
- **Original**: 678.स्वायुधः पवते देव इन्दुरशस्तिहा वृजना रक्षमाण: ।
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1756)
- **Original**: श््ड सापवेद- संहिता पिता देवानां जनिता सुदक्षो विष्टम्भो दिवो घरुण: पृथिव्या:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1757)
- **Original**: उत्तप आयुधों से युक्त, शत्रुनाशक, विघ्नों को दूर कर उनसे रक्षा करने वाला, पालक, दिव्यता का विकास करने वाला, उत्तम बलवान, आकाश तथा पृथ्वी का धारक दिव्य सोम शोधित किया जाता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1758)
- **Original**: 679.ऋषिरिंप्र: पुर एता जनानामृभुर्धीर उशना काव्येन । स चिद्विवेद निहित॑ यदासामपीच्यां3 गुह्मां नाम गोमाम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1759)
- **Original**: नेतृत्त्व प्रदान करने वाले, प्रखर, परमज्ञानी, धैर्यवान्‌ उशना ऋषि द्वारा, गौओं में गुप्त रूप से रहने वाले सोम को यल्नपूर्वक प्राप्त किया गया
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1760)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

