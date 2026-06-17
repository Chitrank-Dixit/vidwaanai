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

### Verse 1 (Sama Ved 0.701)
- **Original**: असुरजयी, धन प्रदान करने वाले, समर्थ संरक्षण वाले, वेगवान्‌ रथ के समान उमंग देने वाले स्तोत्रों का विधिपूर्वक उच्चारण किया जाता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.702)
- **Original**: 252.यथा गौरो अपा कृत॑ तृष्यन्नेत्यवेरिणम्‌ । आपित्वे नः प्रपित्वे तूयमा गहि कण्वेषु सु सचा पिय
- **Translation**: 

---

### Verse 3 (Sama Ved 0.703)
- **Original**: हे इन्द्रदेव ! प्यासे गौर वर्ण के पशु जिस तरह पानी से भरे तालाब के निकट जाते हैं, उसी प्रकार हे इद्धदेव ! आप सहचर बनकर इस हमारे -काण्व के यज्ञ में तीव गति से आएँ और सोमपान कर तृप्त हों
- **Translation**: 

---

### Verse 4 (Sama Ved 0.704)
- **Original**: इति चतुर्दश: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.705)
- **Original**: झ्.ढ सामवेद-संहिता
- **Translation**: 

---

### Verse 6 (Sama Ved 0.706)
- **Original**: पञ्चदश: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.707)
- **Original**: 253. शब्ध्यू3षु शचीपत इन्द्र विश्वाभिरूतिभि: । भरगं न हि त्वा यशसं वसुत्रिदमनु शूर चरामसि
- **Translation**: 

---

### Verse 8 (Sama Ved 0.708)
- **Original**: है शचीपते शुर इन्द्रदेव ! सब प्रकार के रक्षा साधनों के साथ आप हमें अभीष्ट फल प्रदान करें । सौभाग्य युक्‍त धन प्रदान करने बाले आपकी हम आराधना करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.709)
- **Original**: 254. या इन्द्र भुज आभर: स्वर्वी असुरेध्य: । स्तोतारमिन्मघवन्नस्य वर्धय ये च त्वे वृक्‍्तबर्हिष:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.710)
- **Original**: है आत्मशक्ति सम्पन इद्धदेव ! राक्षसों से जीतकर लाये गये धन से स्तोताओं का संरक्षण करें और जो आपका आवाहन करते हैं, उनकी वृद्धि करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.711)
- **Original**: 255. प्र मित्राय प्रार्यम्णे सचथ्यमृतावसों । वरूथ्ये3वरुणे छन्हं बच: स्तोत्र राजसु गायत
- **Translation**: 

---

### Verse 12 (Sama Ved 0.712)
- **Original**: है परमार्थी याज्ञिको ! मित्र, वरुण और अर्यमा देवों के यज्ञशाला में प्रतिष्ठित होने के बाद छन्दबद्ध गेय श्तोज्रों से उनकी प्रार्थना करो
- **Translation**: 

---

### Verse 13 (Sama Ved 0.713)
- **Original**: 256.अभि त्वा पूर्वपीतय इन्द्र स्तोमेभिरायव: । समीचीनास ऋभव: समस्वरच्रुद्रा गृणन्त पूर्व्यम्‌ू
- **Translation**: 

---

### Verse 14 (Sama Ved 0.714)
- **Original**: एकत्रित हुए ऋभुओं, मरुतों आदि पुरुषों के समान हे इन्रदेव ! सबसे पहले सोमरस पान के लिए याज्ञिकजन आपको स्तुति, स्तोत्रों से करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.715)
- **Original**: 257.प्र व इन्द्राय बृहते मरुतों ब्रह्मार्चत। बृत्रं हनति वृत्रहा शतक्रतुर्वज़ेण शतपर्वणा
- **Translation**: 

---

### Verse 16 (Sama Ved 0.716)
- **Original**: सैकड़ों धार वाले वश् से वृत्र को मारने वाले, शतकर्मा इन्द्रदेव को हे याजको ! स्तोत्र सुनाओ
- **Translation**: 

---

### Verse 17 (Sama Ved 0.717)
- **Original**: 258, बृहदिन्द्राय गायत मरुतो वृत्रहन्तमम्‌ । * येन ज्योतिरजनयन्नृताबृधो देवं देवाय जागृवि
- **Translation**: 

---

### Verse 18 (Sama Ved 0.718)
- **Original**: है बाजकों ! इन्धदेव के निमित्त वृत्र (अज्ञानी) का विनाश करने वाले बृहत्‌ सामर का गायन करो । यज्ञ के विशेषज्ञ विद्वानों ने उसी के सहयोग से दिव्य जायति लाने बाली ज्योति उत्पन्न की है.
- **Translation**: 

---

### Verse 19 (Sama Ved 0.719)
- **Original**: 259. इन्द्र क्रतुंन आ भर पिता पुत्रेभ्यो यथा
- **Translation**: 

---

### Verse 20 (Sama Ved 0.720)
- **Original**: शिक्षा णो अस्मिन्पुरुहूत यामनि जीवा ज्योतिरशीमहि
- **Translation**: 

---

