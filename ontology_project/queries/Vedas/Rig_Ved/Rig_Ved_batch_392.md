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

### Verse 1 (Rig Ved 0.7821)
- **Original**: 3406, अस्माकमुत्तमं कृधि श्रवो देवेषु सूर्य । वर्षिष्ठं द्याभिवोपरि
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7822)
- **Original**: सबके प्रेरक हे सूर्यदेव ! जिस तरह आपने अत्यधिक ओजस्वी द्युलोक की स्थापना ऊपर की है, उसी प्रकार देवताओं के बीच में हमारे यज्ञों को श्रेष्ठता प्रदान करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7823)
- **Original**: मं0 ड सुक्त 32 पे [ सूक्त - 32 ] [ऋषि - वामदेव गौतम । देवता - इद्ध, 23-24 इन्द्राश्व
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7824)
- **Original**: छन्द - गायत्री ] 3407. आ तू न इन्द्र वृत्रहन्नस्माकमर्थधमा गहि। महान्महीभिरूतिभि:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7825)
- **Original**: हे वृत्रहन्ता ! आप महान्‌ बनकर, संरक्षण के विविध साधनों सहित हमारे पास आएँ
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7826)
- **Original**: 3408. भृमिश्चिद्घासि तूतुजिरा चित्र चित्रिणीष्वा। चित्रं कृणोष्यूतये
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7827)
- **Original**: हे इन्द्रदेव ! आप पुरुषार्थ करने वाले तथा हमें समृद्ध करने वाले हैं । हे अद्भुत शक्तिशाली इन्धदेव ! आप अद्भुत कर्म करने वाले मनुष्यों को, सुरक्षा के लिए विलक्षण बल प्रदान करते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7828)
- **Original**: 3409, दश्नेभिश्चिच्छशीयांसं हंसि ब्राथन्तमोजसा । सखिभियें त्वे सचा
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7829)
- **Original**: है इन्रदेव ! जो बाजक आपके साथ निवास करते हैं, उन थोड़े से मित्रों के सहयोग से आप उच्छृंखलता बरतने वाले बड़े-बड़े रिपुओं को भी विनष्ट कर देते हैं
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7830)
- **Original**: 3410. वयभिन्द्र त्वे सचा वयं त्वाभि नोनुमः
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7831)
- **Original**: अस्माँ अस्माँ इृदुदव
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7832)
- **Original**: हे इद्धदेव ! हम आपके साथ निवास करते हैं तथा आपको प्रार्थना करते हैं, अत: आप हमें विशेष रूप से संरक्षण प्रदान करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7833)
- **Original**: 3411. स नश्नित्राभिरद्विवो5नवद्याभिरूतिभि: । अनाधृष्टाभिरा गहि
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7834)
- **Original**: हे वज़धारी इद्धदेव ! आप अनेक प्रकार के प्रार्थनीय तथा रिपुओं द्वारा परास्त न किये जाने योग्य रक्षण- साधनों से सम्पन्न होकर हमारे समीप पथारें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7835)
- **Original**: 3412. भूयामो घु त्वावत: सखाय इन्द्र गोमत: । युजो वाजाय घृष्वये
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7836)
- **Original**: है इन्द्रदेव ! हम आपके समान गौओं से सम्पन्र व्यक्तियों के मित्र हों । प्रचुर अन्न- धन के निर्मित हम आपके साथ मिलते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7837)
- **Original**: 3413. त्वं होक ईशिष इन्द्र वाजस्य गोमत: । स नो यन्धि महीमिषम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7838)
- **Original**: हे इन्धदेव ! गौओं (प्रकाशयुक्त किरणों) से पैदा हुए अन्न पर आप अकेले ही शासन करते हैं; अत: आप हमें प्रचुर अन्न प्रदान करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7839)
- **Original**: 3414. न त्वा वरन्ते अन्यथा यहद्दित्ससि स्तुतो मघम्‌। स्तोतृभ्य इन्द्र गिर्वणः
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7840)
- **Original**: हे प्रार्थनीय इद्धदेव ! जब आप प्रशंसित होकर स्तुति करने वालों को ऐश्वर्य प्रदान करने की अभिलाषा करते हैं, तव कोई भी किसी तरह आपको रोक नहीं सकता
- **Translation**: 

---

