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

### Verse 1 (Rig Ved 0.7841)
- **Original**: 3415, अभि त्वा गोतमा गिरानूषत प्र दावने । इन्द्र वाजाय घृष्यये
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7842)
- **Original**: हे इन्द्रदेव ! ऋषि 'गौतम' अपनी प्रार्थनाओं के द्वारा आपको समृद्ध करते हैं तथा श्रेष्ठ अन्न दान करने के निमित्त आपकी प्रार्थना करते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7843)
- **Original**: 3416. प्र ते वोचाम वीर्या3 या मन्दसान आरुज: । पुरो दासीरभीत्य
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7844)
- **Original**: , हे इन्धदेव ! सोमरस पान से हर्षित होकर आपने दासों की पुरियों पर चढ़ाई करके उन्हें विदीर्ण कर दिया; अत: हम आपके उस शौर्य का वर्णन करते हैं
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7845)
- **Original**: 3417, ता ते गृणन्ति वेधसो यानि चकर्थ पौंस्या। सुतेष्विन्द्र गिर्वण:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7846)
- **Original**: पड ऋग्वेद संहिता घाग - 2 हे प्रशंसनीय इन्द्रदेव ! आपने जिस शौर्य को प्रकर किया । सोम रस तैयार होने पर ज्ञानी जज आपके उस शौर्य की प्रशंसा करते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7847)
- **Original**: 3418. अवीबृथधन्त गोतमा इन्द्र त्वे स्तोमवाहस: । ऐषु धा वीरवद्यश:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7848)
- **Original**: हे इद्धदेव ! प्रशंसा करने वाले 'गौतम' क्रग्रषि आपकी कीर्ति को समृद्ध करते हैं । इसलिए आप इन्हें सन्तानों से सम्पन्न करें तथा अन्न प्रदान करें 2
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7849)
- **Original**: 3419, यच्चिद्धि शश्वतामसीन्द्र साधारणस्त्यम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7850)
- **Original**: तं त्या ययं हवामहे
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7851)
- **Original**: हे इद्धदेव ! यद्यपि समस्त याजकों के लिए आप सहज उपलब्ध देव हैं, फिर भी हम स्तुति करने वाले आपको विशेष रूप से आहूत करते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7852)
- **Original**: 3420, अर्वाचीनो बसों भवास्मे सु मत्स्वान्धस:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7853)
- **Original**: सोमानामिन्द्र सोमपा:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7854)
- **Original**: सबको निवास प्रदान करने वाले है इद्धदेव ! आप सोमरस पान करने वाले हैं । आप हम याजकों के सम्मुख पथधारें तथा सोमरस पान करके हर्षित हों
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7855)
- **Original**: 3421, अस्माकं त्वा मतीनामा स्तोम इन्द्र यच्छतु । अर्वागा वर्तया हरी
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7856)
- **Original**: हे इद्धदेव ! हम आपकी स्तुति करने वाले हैं । हमारी स्तुतियाँ आपको हमारे समीप ले आएँ । आप अपने अश्वों को हमारी ओर ग्रेरित करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7857)
- **Original**: 3422. पुरोढाशं च नो घसो जोषयासे गिरश्न न:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7858)
- **Original**: वधूयुरिव योषणाम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7859)
- **Original**: . हे इन्द्रदेव
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7860)
- **Original**: आप हमारे पुरोडाश रूपी अन्न का सेवन करें । जिस तरह स्त्री की अभिलाषा करने वाले पुरुष स्त्री के बचनों को ध्यानपूर्वक सुनते हैं, उसो प्रकार आप हमारी प्रार्थनाओं को सुनें
- **Translation**: 

---

