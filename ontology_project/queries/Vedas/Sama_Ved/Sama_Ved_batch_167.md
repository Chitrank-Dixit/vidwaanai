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

### Verse 1 (Sama Ved 0.3321)
- **Original**: वह सोम त्रितयज्ञ (अंतरिक्ष, प्रकृति और जीवों के मध्य आदान- प्रदान करने वाले यज्ञ) में संस्कारित होकर अपने महान्‌ तेज से सूर्यदेव को प्रकाशित करता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3322)
- **Original**: 1296. स वृत्रह वृषा सुतो वरिवोविददाभ्य:। सोमो वाजमिवासरत्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3323)
- **Original**: शत्रुओं का नाश करने वाला, बलवर्धक, निचोड़कर निकाला गया, धन देने वाला सोम अश्व के वेग के समान कलश में प्रविष्ट होता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3324)
- **Original**: 10.6 सामवेद-संहिता 1297. स देवः कविनेषितो35भि द्रोणानि धावति। इन्दुरिन्द्राय मंहयन्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3325)
- **Original**: चुलोक में प्रकाशवान्‌ वह सोम याजकों के द्वारा प्रवाहित होकर, इन्धादि देवों की महत्ता बढ़ाने के लिए, वेग-पूर्वक, कलश (विश्वघर) में प्रविष्ट होता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3326)
- **Original**: डति षष्ठ:खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3327)
- **Original**: के के के
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3328)
- **Original**: सप्तम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3329)
- **Original**: 1298, यः पावमानीरध्येत्यूषिभि: संभूत॑ रसम्‌ । सर्व॑ स पूतमश्नाति स्वदित॑ मातरिश्चवना
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3330)
- **Original**: ऋषियों द्वारा संगृहीत (जीवन सूत्रों) में रस लेने वाला, पवित्र करने वाले सूकतों का पाठ करने वाला, याजक (यज्ञ के प्रभाव से) वायु में संव्याप्त पोषक अननादि का सेवन करता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3331)
- **Original**: 1299. पावमानीरयों अध्येत्यूषिभि: संभृत॑ रसम्‌ । तस्मै सरस्वती दुहे क्षीरं सर्पिमधूदकम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3332)
- **Original**: जो ऋषियों द्वारा प्रणीत वेदों की ऋचाओं का अध्ययन करता है, उसके लिए (उसके ज्ञान को पुष्ट करने के लिए) देवी सरस्वती, दुग्ध, घृत, शहद जैसे पोषक तत्त्व स्वयं उपलब्ध कराती हैं । 2
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3333)
- **Original**: 1300. पावमानी:ः स्वस्त्ययनीः सुदुघा हि घृतश्चुतः । ऋषिभि: संभूतो रसो ब्राह्मणेष्वमृतं हितम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3334)
- **Original**: ऋषियों द्वारा सम्पादित पावमानी (पवित्र बनाने वाले) मंत्र कल्याण कारक, उत्तम फलदायक एवं स्नेह- वर्षक हैं । वेदपाठी ब्राह्मणों के बीच मानों उन्होंने हितकारी अमृत ही रख दिया है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3335)
- **Original**: 1301. पावमानीर्दधन्तु न इमं लोकमथो अमुम्‌ । कामान्त्समर्धयन्तु नो देवीदेंवै: समाहता:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3336)
- **Original**: देवताओं द्वारा सम्पादित देवी ऋचाएँ हमें इहलोक और परलोक में सुख पहुँचाएँ और हमारे अभीष्ट मनोर॒थ फलित हों
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3337)
- **Original**: 1302. येन देवाः पवित्रेणात्मानं पुनते सदा । तेन सहस्नधारेण पावमानीः पुनन्तु नः
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3338)
- **Original**: देवगण अपने को पवित्र करने के जिन साधनों को प्रयुक्त करते हैं, उय हजारों प्रकार के साधनों से पवित्र करने वाली यह ऋचाएँ हमें भी निर्मल बनाएँ
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3339)
- **Original**: 130 3. पावमानी: स्वस्त्ययनीस्ताभिर्गच्छति नान्दनम्‌ । पुण्याँश्च भक्षान्भक्षय॑त्यमृतत्वं च गच्छति
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3340)
- **Original**: पवित्रता प्रदान करने वाली एवं कल्याणकीरिणी ऋचाओं से प्रेरित होकर साधक, आनन्द की स्थिति को प्राप्त करता है । वह पवित्र (पुण्यार्जित) अन्न खाता और अमरता प्राप्त करता है
- **Translation**: 

---

