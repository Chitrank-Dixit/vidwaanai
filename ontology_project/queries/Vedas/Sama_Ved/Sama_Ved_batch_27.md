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

### Verse 1 (Sama Ved 0.521)
- **Original**: अष्टम: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.522)
- **Original**: 185, य॑ रक्षन्ति प्रचेतसो वरुणों मित्रो अर्यमा । न किः स दभ्यते जन:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.523)
- **Original**: जिस याजक को, ज्ञाससम्पन्स वरुण, मित्र और अर्यमा देवों का संरक्षण प्राप्त है, उसे कोई भी नहीं दबा सकता
- **Translation**: 

---

### Verse 4 (Sama Ved 0.524)
- **Original**: 186. गव्यो षु णो यथा पुराश्चयोत रथया । वरिवस्था महोनाम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.525)
- **Original**: हे इन्द्रदेव ! सदैव की तरह हमें उत्तम गौओं, श्रेष्ठ घोड़ों से युक्त रथ तथा ग्रतिष्ठापूर्ण धन देने को इच्छा से हमारे पास आएँ
- **Translation**: 

---

### Verse 6 (Sama Ved 0.526)
- **Original**: 187, इमास्त इन्द्र पृश्नयो घृतं दुहत आशिरम्‌ । एनामृतस्य पिप्युषी:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.527)
- **Original**: है इद्धदेव ! आपकी ये गौएँ सत्यरूप यज्ञ का विस्तार करने वाली हैं। ये गौएँ हमें घृत और दुध प्रदान करती हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.528)
- **Original**: 188. अया धिया च गव्यया पुरुणामन्पुरुष्टत । यत्सोमेसोम आभुवः
- **Translation**: 

---

### Verse 9 (Sama Ved 0.529)
- **Original**: है बहुत नामों से युक्त, बहु प्रशंसित इन्धदेव ! प्रत्येक सोमयश्ञ में जहाँ आप पहुँचते हैं, वहाँ गौओं की कामना वाली बुद्धि से हम आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.530)
- **Original**: 189. पावका नः सरस्वती वाजेभिवाजिनीवती । यज्ञ वष्टु धियावसु:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.531)
- **Original**: पवित्र बनाने वाली, पोषण देने वाली, बुद्धिमत्तापूर्वक धन देने वाली सरस्वती, ज्ञान और कर्म से हमारे यज्ञ को सफल बनायें
- **Translation**: 

---

### Verse 12 (Sama Ved 0.532)
- **Original**: 190. क इम॑ नाहुषीष्वा इन्द्र सोमस्य तर्पयातू। स नो बसून्या भरात्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.533)
- **Original**: मनुष्यों में ऐसा कौन है, जो इन इद्धदेव को तृप्त कर सके ? वे इन्द्रदेव हमारे यज्ञ में आएँ और हमें ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.534)
- **Original**: पूर्वार्चिके ऐज्रपर्वीणि द्वितायोंध्याय: 2.9 191, आ याहि सुधुमा हि त इन्द्र सोम॑ पिबा इमम्‌। एदं ब्हिं: सदो मम
- **Translation**: 

---

### Verse 15 (Sama Ved 0.535)
- **Original**: हे इन्द्रदेव ! आप हमारे इस यज्ञ में पधारें । अपने लिए निकाले गये इस सोमरस का पान कर, श्रेष्ठ आसन पर बिराजें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.536)
- **Original**: 192. महि त्रीणामवरस्तु झुक्ष॑ मित्रस्यार्यम्ण: । दुराधर्ष वरुणस्य
- **Translation**: 

---

### Verse 17 (Sama Ved 0.537)
- **Original**: मित्र, वरूण और अर्यमा इन तीनों देवों का संयुक्त तेजस्वी महान्‌ संरक्षण हमें प्राप्त हो, जिससे हम दूसरों को पराजित करने में समर्थ हों
- **Translation**: 

---

### Verse 18 (Sama Ved 0.538)
- **Original**: 193. त्वावतः पुरूवसो वयमिन्द्र प्रणेत: । स्मसि स्थातहरीणाम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.539)
- **Original**: हे ऐश्वर्य के स्वामी, श्रेष्ठ कर्म करने वाले, घोड़ों पर विराजमान इन्द्रदेव ! आपसे संरक्षित होकर हम हर तरह से सुरक्षित रहें
- **Translation**: 

---

### Verse 20 (Sama Ved 0.540)
- **Original**: इति अष्टम: खण्ड:
- **Translation**: 

---

