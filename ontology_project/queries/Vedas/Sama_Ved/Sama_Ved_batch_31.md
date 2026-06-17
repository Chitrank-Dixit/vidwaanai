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

### Verse 1 (Sama Ved 0.601)
- **Original**: 2.12 सापवेद-संहिता 218. ऋजुनीती नो वरुणो मित्रो नयति विद्वान्‌ । अर्यमा देवेः सजोघा:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.602)
- **Original**: ! ज्ञानी देव, मित्र और वरुण हमें सरल नीति-पथ पर बढ़ाते हैं । देवों के सहचर अर्यमा हमें सरल मार्ग से उनततिशौल बनायें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.603)
- **Original**: 2919. दूरादिहेव यत्सतो5रुणप्सुरशिश्चितत्‌ । वि भानुं विश्वथातनत्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.604)
- **Original**: । दूर से पास आने वाली अरुणाभ उषा, जब दिखाई देकर रश्मियों को फैलाती है, तब उसके प्रकाश से समूचा विश्व प्रकाशित हो जाता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.605)
- **Original**: 220. आ नो मित्रावरुणा घृतर्गव्यूतिमुक्षतम्‌। मध्वा रजांसि सुक्रतू
- **Translation**: 

---

### Verse 6 (Sama Ved 0.606)
- **Original**: हे भित्रावरुण ! हमारी गौओं (इन्द्रियों) को घृत (स्नेह) से युक्त करें और ऊर्ध्वलोकों को भी श्रेष्ठ रसों (भावों) से सिंचित करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.607)
- **Original**: 221. उदु त्ये सूनवो गिर: काष्ठा यज्ञेष्वत्तत
- **Translation**: 

---

### Verse 8 (Sama Ved 0.608)
- **Original**: वाश्रा अभिज्ु यातवे
- **Translation**: 

---

### Verse 9 (Sama Ved 0.609)
- **Original**: शब्दनाद करने वाले मरुतों ने यज्ञार्थ जल को नि:सृत किया । प्रवाहित जल का पान करने के लिए रैंभाती गौएँ, घुटने तक पानी में जाने के लिए प्रेरित होती हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.610)
- **Original**: [ शब्द नाद-शब्दों के एक विशेष आयाम से परिचय करता है, विज्ञान जगतू अभी इस आयाम से तव्रिक भी परिचित नहीं ।] 222. इदं विष्णुर्वि चक्रमे त्रेथा नि दे पदम्‌ । समूढमस्य पांसुले
- **Translation**: 

---

### Verse 11 (Sama Ved 0.611)
- **Original**: इस विश्व के। भगवान्‌ विष्णु (बामन) देव ने तीन पगों से नापा । उनके घूल भरे पाँव में समूचा संसार समाया हुआ है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.612)
- **Original**: [ क. परमात्पा ने तीन चरण वाले (ब्रिआयामी) विश्व की संरचना की है । इसका वास्तविक स्वरूप आकाश ( अदृश्यपद) में किया हुआ है। ख. खगोल विज्ञान की नवीनतप शोध (सब पार्टिकल्स) के अनुसार भी उक्त वर्णन युक्तिसंगत स्पद्व होते हैं।]
- **Translation**: 

---

### Verse 13 (Sama Ved 0.613)
- **Original**: इति एकादश: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.614)
- **Original**: क्र कक
- **Translation**: 

---

### Verse 15 (Sama Ved 0.615)
- **Original**: द्वादश: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.616)
- **Original**: 223. अतीहि मन्युषाविणं सुधुवांसमुपेरय। अस्य रातौ सुतं पिब
- **Translation**: 

---

### Verse 17 (Sama Ved 0.617)
- **Original**: हे इन्द्रदेव ! जो साधक क्रोधित होकर सोमरस निकालता है, आप उसे न ब्हण करें । उत्तम विधि से जो साधक सोमरस तैयार करता है, उसके यज्ञ में पहुँच कर आप सोमरस का पान करें
- **Translation**: 

---

### Verse 18 (Sama Ved 0.618)
- **Original**: 224. कदु प्रचेतसे महे वचो देवाय शस्यते । तदिद्ध्यस्य वर्धनम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.619)
- **Original**: इन्द्रदेव के गुणों का गान करने वाले, हमारे तुच्छ से दिस्बाई देने वाले स्तोत्रों से भी महाज्ञानी इन्द्रदेव प्रसन्‍न होते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.620)
- **Original**: 225. उक्थ॑ं च न शस्यमान नागो रयिरा चचकेत । न गायत्रं गीयमानम्‌
- **Translation**: 

---

