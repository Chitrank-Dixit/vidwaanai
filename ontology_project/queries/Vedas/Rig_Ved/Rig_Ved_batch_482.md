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

### Verse 1 (Rig Ved 0.9621)
- **Original**: 4182. उत त्वा खत्री शशीयसी पुंसो भवति वस्यसी । अदेवत्रादराधस:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.9622)
- **Original**: जो पुरुष देवो की उपासना नहीं करता है, धनादि दान नहीं करता है, उसको अपेक्षा ख्री शशीयसी सब प्रकार से श्रेष्ठ है
- **Translation**: 

---

### Verse 3 (Rig Ved 0.9623)
- **Original**: 4183. वि या जानाति जसुरिं वि तृष्यन्त॑ वि कामिनम्‌ । देवत्रा कृणुते मन:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.9624)
- **Original**: में0 5 सु0 61 9 वे शशीयसी देवी प्रताड़ितों को जानती हैं, प्यासों को भी जानती हैं, धन की कामना वालों को जानती हैं और वे चिरन्तन देव पूजा में अपने चित्त को लगातौ हैं
- **Translation**: 

---

### Verse 5 (Rig Ved 0.9625)
- **Original**: 4184. उत घा नेमो अस्तुतः पुमाँ इति ब्रुबे पणि: । स वैरदेय इत्समः
- **Translation**: 

---

### Verse 6 (Rig Ved 0.9626)
- **Original**: उन शशीयसी के अर्धाग पुरुष तसन्‍त की स्तुति करके भी हम कहते हैं कि स्तुति ठीक प्रकार नहीं हुई; क्योंकि दान के क्रम में वे सदैव समान हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.9627)
- **Original**: 4185, उत मेउरपद्युवतिर्ममन्दुधी प्रति श्यावाय वर्तनिम्‌। बि रोहिता पुरुमीव्हाय येमतुर्विप्राय दीर्घयशसे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.9628)
- **Original**: सर्वदा प्रमुदित रहने वाली युवती शशीयसी ने श्यावाश्र का मार्ग प्रदर्शित किया धा । उनके रोहित वर्णवाले अख्व उन्हें बहुप्रशंसित, महान्‌ यशस्वी विप्र के मार्ग की ओर वहन करते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.9629)
- **Original**: 4186. यो मे थेनूनां शतं वैददश्चिर्यथा ददत्‌ । तरन्तड़व मंहना
- **Translation**: 

---

### Verse 10 (Rig Ved 0.9630)
- **Original**: विददश्व के पुत्र ने भी हमें तरन्त के समान सौ गाय और तेजस्वी धन प्रदान किया
- **Translation**: 

---

### Verse 11 (Rig Ved 0.9631)
- **Original**: 10 । 4187. य ईं वहन्त आशुभि: पिबन्तों मदिरं मधु। अत्र श्रवांसि दधिरे
- **Translation**: 

---

### Verse 12 (Rig Ved 0.9632)
- **Original**: वे मरुद्गण द्रुतगाम्ी अश्वों पर अधिष्ठित होकर अत्यन्त हर्षप्रद मधुर सोमपान करने के निमित्त आते हैं और हमें विषुल अन्न प्रदान करते हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.9633)
- **Original**: 4188. येषां श्रियाधि रोदसी विश्राजन्ते रथेष्वा । दिवि रुक्मइवोपरि
- **Translation**: 

---

### Verse 14 (Rig Ved 0.9634)
- **Original**: जिन मस्तों की शोभा से चयावा-पृथिवी भी परिव्याप्त होती हैं। वे मकदूगण ऊपर आकाश में प्रकाशमान सूर्यदेव के सदृश रथों में विशिष्ट आभा विस्तारित करते हैं
- **Translation**: 

---

### Verse 15 (Rig Ved 0.9635)
- **Original**: 4189. युवा स मारुतो गणस्त्वेषरथों अनेद्य:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.9636)
- **Original**: शुभंयावाप्रतिष्कुत:
- **Translation**: 

---

### Verse 17 (Rig Ved 0.9637)
- **Original**: यह मरुदगणों का समुदाय सदा तरूण और अनिन्दनीय है । ये तेजस्वी रथ में विराजित होकर वृश्टि आदि शुभ कार्य के निभित्त अवाधगति से गमन करते हैं
- **Translation**: 

---

### Verse 18 (Rig Ved 0.9638)
- **Original**: 4190. को बेद नूनमेषां यत्रा मदन्ति धूतय: । ऋजाता अरेपस:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.9639)
- **Original**: यज्ञादि कर्मों से उत्पन्न हुए ये मरदगण शत्रुओं को कैंपाने वाले और पाप रहित हैं । ये जहाँ हर्षित होते हैं, उस स्थान को कौन जानता है ?
- **Translation**: 

---

### Verse 20 (Rig Ved 0.9640)
- **Original**: 4191. यूयं मत विपन्यव: प्रणेतार इत्था धिया। श्रोतारो यामहूतिषु
- **Translation**: 

---

