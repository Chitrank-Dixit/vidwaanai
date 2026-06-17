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

### Verse 1 (Sama Ved 0.1701)
- **Original**: जैसे युद्ध भूमि में यशस्त्री शूरबोर घूमते हैं, उसी प्रकार याजकों. से प्रशंसित, बलबर्द्धक, सबका हितकारी, संस्कारित सोम यज्ञ भूमि में प्रतिप्ठा पाता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1702)
- **Original**: 656.ऋधक्सोम स्वस्तये संजग्मानो दिवा कवे
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1703)
- **Original**: पवस्व सूर्यो दृशे
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1704)
- **Original**: हे ज्ञानयुकत सोमदेव ! आप तेजस्वों सूर्य के सदश, दिव्य आभा युक्त होकर सब्रके कल्याण के लिए संस्कारित हों
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1705)
- **Original**: 657.पवमानस्य ते कवे वाजिन्त्सर्गा असक्षत । अर्वन्तो न श्रवस्थवः
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1706)
- **Original**: हे बलवर्द्धक सोम ! शुद्ध होते समय आपकी यशस्वरी धारा छुड़साल से निकलने वाले दरुतमामी अश्रों के समान वेगव्ती होतो है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1707)
- **Original**: 658.अच्छा कोशं मधुश्चुतमस्‌ग्रं बारे अव्यये
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1708)
- **Original**: अवावशन्त धीतय:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1709)
- **Original**: 5 मधुरस के कलश में हृम सोमस्स को छानते हैं, जिसे हमारी अगुलियोँ बार-बार शुद्ध करती हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1710)
- **Original**: 5.2 सामवेद- संहिता 659. अच्छा समुद्रमिन्दवो 5स्तं गावो न थेनव:। अग्मन्तृतस्थ योनिमा
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1711)
- **Original**: जल युवत कलश में छाना गया सोमरस यज्ञ स्थान में उसी प्रकार (स्वभावत:) जाता है, जैसे दुधारू गाय अपने स्थान में जाती है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1712)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1713)
- **Original**: क्रेकेके द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1714)
- **Original**: 660,अग्न आ याहि बीतये गृणानों हव्यदातये। नि होता सत्सि बर्हिषि
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1715)
- **Original**: हे अग्निदेव ! आप स्तुति के बाद आहुतियों को ग्रहण कर, उन्हें देयों तक पहुँचाने के लिये, देयों के प्रतिनिधि रूप में आसन ग्रहण करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1716)
- **Original**: 661.तं त्वा समिदिभरड्विरो घृतेन वर्धवामसि । बृहच्छोचा यविष्ठ्य
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1717)
- **Original**: हे प्रकाश स्वरूप परमात्मन्‌ ! हम आपको समिधाओं तथा घृत द्वारा प्रदीष्त करते हैं । अत: हे सामर्थ्यवान्‌ ! आप अधिक प्रखर हों
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1718)
- **Original**: 662.स नः पृथु श्रवाय्यमच्छा देव विवासस्ति । बृहदग्ने सुवीर्यम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1719)
- **Original**: है अग्निदेव ! आप ऐसी कृपा करें कि हमें महान्‌ पराक्रम और श्रेष्ठ यशदायी सामर्ध्य प्राप्त हो
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1720)
- **Original**: 663.आ नो मित्रावरुणा घृतैर्गव्यूतिमुक्षतम्‌। मध्वा रजांसि सुक्रतू
- **Translation**: 

---

