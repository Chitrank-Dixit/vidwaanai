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

### Verse 1 (Sama Ved 0.2901)
- **Original**: प्रशंसित राजा तथा सात याजकों द्वारा जिस प्रकार यज्ञ प्रतिष्ठित होता है, उसी प्रकार गोघृतादि से यह सोम संस्कारयुक्त होता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2902)
- **Original**: 1122. परि स्वानास इन्दवो मदाय बर्हणा गिरा। मथो अर्थन्ति धारया
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2903)
- **Original**: श्रेष्ठ स्तवनों से प्रशंसित, सवित सोम, देवताओं की आनन्दवृद्धि के लिए मधुर रस की धारा के साथ पात्र में गिरता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2904)
- **Original**: * 1123. आपानासो विवस्वतो जिन्वन्त उषसो भगम्‌ । सूरा अण्वं वि तन्वते
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2905)
- **Original**: उषा को तेजस्वी बनाता हुआ सोमरस इद्धदेव के पान हेतु ध्वनि करता हुआ शोधित हो रहा है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2906)
- **Original**: <.2 सामवेद-संहिता 1124. अप द्वारा मतीनां प्रत्ता ऋण्वन्ति कारवः । वृष्णो हरस आयब:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2907)
- **Original**: प्राचीन, शक्तिशाली सोम का आवाहन करने बाले ब्रप्रत्विज्‌ स्तोता, यज्ञ द्वारों को उद्घाटित करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2908)
- **Original**: 1125. समीक्षीनास आशत होतार: सप्तजानय: । पदमेकस्य पिप्रतः
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2909)
- **Original**: उत्कृष्ट जाति के, एक मात्र सोम को पूर्णता प्रदान करते हुए, सात याज्ञिक, यज्ञ- कर्मानुष्ठान के लिये उपस्थित होते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2910)
- **Original**: 1126. नाभा नाभिं न आ ददे चक्षुषा सूर्य दृशे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2911)
- **Original**: कवेरपत्यमा दुहे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2912)
- **Original**: नेत्रों से सूर्य दर्शन के निमित्त, यज्ञ की नाभि सदृश सोम को, निज नाभि के निकट अर्थात्‌ उदर के समीप स्थापित करते हैं, इस्र प्रकार सोम से उत्पन्न तेजस्विता को हम पूर्णता प्रदान करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2913)
- **Original**: 1127. अभि प्रियं दिवस्पदमध्वर्युभिर्गुह्ा हितम्‌ । सूर: पश्यति चक्षसा
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2914)
- **Original**: बलवबान्‌ इन्द्रटेंब अपने नेत्रों से दिव्यलोक में प्रिय और अध्यवर्युओं द्वारा हृदयस्थ सोम को देखते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2915)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2916)
- **Original**: के के के
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2917)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2918)
- **Original**: 1128. असुग्रमिन्दवः पथा धर्मन्नतस्य सुश्रियः । विदाना अस्य योजना
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2919)
- **Original**: यजमान एवं देवताओं के सम्बन्ध में भली-भाँति जानते हुए, यशस्वरी सोम धर्म-कार्यों की तरह यज्ञ मार्ग में आरूढ़ होता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2920)
- **Original**: 1129. प्र धारा मधों अग्रियो महीरपो वि गाहते । हवि्वि:घु वन्द्य:
- **Translation**: 

---

