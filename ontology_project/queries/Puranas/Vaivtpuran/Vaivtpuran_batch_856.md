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

### Verse 1 (Vaivtpuran 543.15434)
- **Original**: भोगने पड़ते हैं; इसमें तनिक भी संशय नहीं रहता है। (पिण्डदान आदि) कर्मके अवसरपर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15435)
- **Original**: है। अतिथि जिसके घरसे निराश होकर लौट पितर और अतिथि-पूजनके समय सारे देवता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15436)
- **Original**: जाता है, उसके घरका उसके पितर, देवता और उसी प्रकार गृहस्थके पास आते हैं, जैसे गौएँ अग्रियाँ भो परित्याग कर देती हैं तथा वह अतिथि पानीसे भरे हुए हौजके पास जाती हैं। भूखा उसे अपना पाप देकर और उसका पुण्य लेकर * 352 नमः कान्ताय भर्त्रे च शिरश्चन्रस्वरूपिणे! नम: शान्ताय दान्ताय सर्वदेवाश्रयाय च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15437)
- **Original**: नमो ब्रह्मस्वरूपाय. सतोप्राणपय च । नमस्यथाय च॒ पृज्याय हृदाधाराय ते नमः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15438)
- **Original**: पश्प्राणाधिदेवाय चश्लुपस्तारकाय च । ज्ञानाधाराय पत्नीनां परमानन्दरूपिणे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15439)
- **Original**: पतिर्विष्णु:. पतिरेव.. महेश्वरः । पतिश्व निर्गुणाधारो ब्रह्मरूपो नमोउस्तु ते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15440)
- **Original**: क्षपस्व ॒भगवन्‌ दोष॑ जक्ञानाज्ञाकृतं च यत्‌ । पत्नीबन्धो दयासिन्धो दासीदोष॑ क्षमस्व मे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15441)
- **Original**: इद॑ स्तोत्र महापुण्य सृष्ठयादी पढ़ाया कृतम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15442)
- **Original**: सरस्थत्या च धरया गड्अया च पुरा ब्रज
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15443)
- **Original**: सावित्रवा च कृत॑ पूवव॑ ब्रह्मणे चापि नित्यश; । पार्वत्या च कृत॑ भक्‍त्या कैलासे शंकराय च
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15444)
- **Original**: मुनोताों च सुराणां चर पत्रीभिकश्ष कृतं॑ पुरा । पतिक्रतानां. सर्वासां. स्तोत्रमेतच्छुभावहम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15445)
- **Original**: इद स्तोत्र महापुण्यं॑ या श्रृेणोति पतिब्रता । नरोउन्यों वापि नारी वा लभते सर्ववाज्छितम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15446)
- **Original**: अपुत्रो. लभते पुत्र निर्धनो लभते धनम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15447)
- **Original**: रोगी च मुच्यते रोगाद्‌ बद्धों मुच्येत बन्धनातू
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15448)
- **Original**: पतिव्रता च स्तुत्वा च तीर्थश्नानफल॑ लभेत्‌। फल॑ च सर्वतपसां ब्रतानां च ब्जेश्वर। (83
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15449)
- **Original**: 136-146)
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15450)
- **Original**: * श्रीकृष्णजन्मस्ण्ड * 673 ऋड़ऋक कक क्ऋ्ऋऋऋ्ऋ ऋ्ऋ्ऋ ऋऋ %% ;% %%%%%%#%#%$%%%$%% 47% # 79%; ####% # #%ऋक चला जाता है। इसलिये उत्तम विचारसम्पन्न धर्मज्ञ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15451)
- **Original**: उसमें वे सारी पतिब्रताएँ और भी पावन मानी गृहस्थ पहले देवता आदि सबकी सेवा करके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15452)
- **Original**: जाती हैं। सृष्टिके आदियमें ब्रह्माने एक ही प्रकारसे फिर आश्रितवर्गकका भरण-पोषण करनेके पश्चात्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15453)
- **Original**: सारी जातियोंकी रचना की थी। वे सभी उत्तम स्वयं भोजन करता है। जिसके घरमें माता नहीं
- **Translation**: 

---

