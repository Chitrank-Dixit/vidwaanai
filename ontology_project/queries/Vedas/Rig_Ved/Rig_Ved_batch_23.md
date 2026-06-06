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

### Verse 1 (Rig Ved 0.441)
- **Original**: 197 तक्षन्नासत्याभ्यां परिज्मानं सुखं रथम्‌। तक्षन्थेनुं सबर्दुधाम्‌
- **Translation**: 

---

### Verse 2 (Rig Ved 0.442)
- **Original**: उन ऋभुदेयों ने अश्विनोकुमारों के लिए अति सुखप्रद, सर्वत्र गमनशील रथ का निर्माण किया और गौओं को उत्तम दूध देने वाली बनाया
- **Translation**: 

---

### Verse 3 (Rig Ved 0.443)
- **Original**: 198. युवाना पितरा पुनः सत्यमनत्रा ऋनूयव:। ऋभयो विष्ट्यक्रत
- **Translation**: 

---

### Verse 4 (Rig Ved 0.444)
- **Original**: अमोघ मन्त्र सामर्थ्य से युक्त, सर्वत्र व्याप्त रहने वाले ऋषुदेवों ने माता-पिता में स्नेहभाव संचरित कर उन्हें पुतः जवान बनाया
- **Translation**: 

---

### Verse 5 (Rig Ved 0.445)
- **Original**: (यहाँ जरावस्था दूर करने की मन्र - विद्या का संकेत है ] 199, स॑ वो मदासो अग्मतेन्द्रेण च मरुत्वता। आदित्येभिश्व राजभि:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.446)
- **Original**: हे ऋभुदेवो ! यह हर्षप्रद सोमरस इन्द्रदेव, मझुतों और दीप्तिमान्‌ आदित्यों के साध आपको अर्पित किया जाता है
- **Translation**: 

---

### Verse 7 (Rig Ved 0.447)
- **Original**: मं0 1 सू0 21 23 200. उत त्य॑ चमसं नवं त्वष्टुदेंवस्थ निष्कृतम्‌। अकर्त चतुरः पुनः
- **Translation**: 

---

### Verse 8 (Rig Ved 0.448)
- **Original**: त्वष्टदेव के द्वारा एक ही चपस तैयार किया गया था, क्रभुदेवों ने उसे चार प्रकार का बनाकर प्रयुक्त किया
- **Translation**: 

---

### Verse 9 (Rig Ved 0.449)
- **Original**: 201. ते नो रत्नानि धत्तन त्रिरा साप्तानि सुन्वते। एकमेकं सुशस्तिभि:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.450)
- **Original**: वे उत्तम स्तुतियों से प्रशंसित होने वाले ऋभुदेव ! सोमयाग करने वाले प्रत्येक याजक को तीनों कोटि के सप्तरलों अर्थात्‌ इक्कीस प्रकार के रलों (विशिष्ट यज्ञ कर्मों ) को प्रदान करें (यज्ञ के तीन विभाग हैं- हविर्यज्ञ, पाकयज्न एवं सोमयज्ञ । तीनों के सात-सात प्रकार हैं । इस प्रकार यज्ञ के इक्कीस प्रकार कहे गये हैं.)
- **Translation**: 

---

### Verse 11 (Rig Ved 0.451)
- **Original**: 202. अधारयन्त वह्लयो5 भजन्त सुकृत्यया। भागं देवेधु यज्ञियम्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.452)
- **Original**: तेजस्वी ऋभुदेयों ने अपने उत्तम कर्मों से देवों के स्थान पर अधिष्ठित होकर यज्ञ के भाग को घारण कर उसका सेवन किया
- **Translation**: 

---

### Verse 13 (Rig Ved 0.453)
- **Original**: [ सूक्त - 21 ] [अर्प्रषि - मेघातिधि काण्व । देवता-इन्द्राग्नी । छन्द-गायत्री
- **Translation**: 

---

### Verse 14 (Rig Ved 0.454)
- **Original**: ] 203. इड्टेन्द्राग्नी उप ह्यये तयोरित्स्तोममुश्मसि
- **Translation**: 

---

### Verse 15 (Rig Ved 0.455)
- **Original**: ता सोम॑ सोमपातमा
- **Translation**: 

---

### Verse 16 (Rig Ved 0.456)
- **Original**: इस यज्ञ स्थल पर हम इन्द्र एवं अग्निदेवों का आवाहन करते हैं, सोमपान के उन अभिलाषियों की स्तुति करते हुए सोमरस पीने का निवेदन करते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.457)
- **Original**: 204 ता यज्ञेषु प्र शंसतेन्द्राम्नी शुम्भता नर: । ता गायत्रेषु गायत
- **Translation**: 

---

### Verse 18 (Rig Ved 0.458)
- **Original**: हे ऋत्विजो ! आप यज्ञानुष्ठान करते हुए इन्द्र एवं अग्निदेवों की शख्त्रों (स्तोत्रों) से स्तुति करें, विविध अलंकारों से उन्हें विभूषित करें तथा गायत्री छन्दवाले सामगान (गायत्र साम) करते हुए उन्हें प्रसन्‍न करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.459)
- **Original**: 205, ता मित्रस्थ प्रशस्तय इन्द्राग्गी ता हवामहे। सोमपा सोमपीतये
- **Translation**: 

---

### Verse 20 (Rig Ved 0.460)
- **Original**: सोमपान की इच्छा करने वाले मित्रता एवं प्रशंसा के योग्य उन इन्द्र एवं अग्निदेवों को हम सोमरस पीने के लिए बुलाते हैं
- **Translation**: 

---

