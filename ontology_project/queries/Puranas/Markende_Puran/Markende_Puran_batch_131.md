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

### Verse 1 (Markende Puran 0.2601)
- **Original**: देवता बोलें--
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2602)
- **Original**: भमवतीने हपारी सब इच्छा पूर्ण कर दी, अब कुछ भी बाकी नहीं हैं
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2603)
- **Original**: क्योंकि हमारा यह शत्रु महिषासुर मारा गया। मसहेश्वरिं! इतनेपर भी यदि आप हमें और बर देना चाहतों हैं
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2604)
- **Original**: तो हम जब-जब आपका स्मरण करें, तब-तब आप दर्शन देकर हमलोगोंके पहान्‌ संकट दूर कर दिया करें तथा प्रसन्नसुखी अम्बिके। जो मनुष्य इन स्तोब्रोंद्रारा आपको स्तुति करे, उसे वित्त, समृद्धि और तैभव देनेके साथ ही उसकी धन और स्त्री आदि सम्पत्तिक्ों भों बढ़ानेके लिये आप सदा हमपर ग्रस्नन्न रहें
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2605)
- **Original**: 1, वा0--मैं; सुधृुपिता। 2.गार्कण्डेयपुराणकी आधुनिक प्रतियॉमें--टदाम्पहपतिप्रीत्था स्वर्वरेभि; सुपूर्निता।-- इतना पाठ अधिक है। किसो -किसी प्रत्तिमें--कर्त्तव्यगएरं यत्य दुष्करं पन्‍त बिंद्सहें। उत्याक्र्ण्य बचौ देब्या: प्रतपूचुल्ते दिनौकस:
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2606)
- **Original**: '-इृठना और अग्लित्ष पाठ हैँ।
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2607)
- **Original**: “इन्द्रादि देखताओंद्वारा देखीकी स्तुति + ऋषिरयाज
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2608)
- **Original**: 32 # इति प्रसादिता देखर्जगतो5र्शे लथाउ5त्मन:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2609)
- **Original**: तथेत्युक्‍त्ता भद्कक्ताली अभूवान्तरहिता नूप
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2610)
- **Original**: इत्येतत्कशित्त॑ भूप सम्भूता सा यश्रा पुरा। देवी देवशरीरिंभ्यो जगल्वयहितैधिणी
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2611)
- **Original**: र्ण्व पुनश्न गॉरीदेहात्सा' समुद्धूता बथाभवत्‌। सथाय दुष्टदयानां तथा शुम्भनिशुम्भयो:
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2612)
- **Original**: रक्षणाय तञ्ञ लोकार्ना देवानामुपकारिणी। तच्छृणुष्व॒ मया55ख्वातरं त्रयानत्कक्षयापि ते।
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2613)
- **Original**: ह्री 30
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2614)
- **Original**: ऋषि कहते हैं --
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2615)
- **Original**: राजन्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2616)
- **Original**: देवताओं ने जब आपने तथा जगत्के कल्याणके लिये भद्गकाली देबीको इस प्रकार प्रसन्न किया, तब वे 'तथास्तु' कहकर वहाँ अन्तर्धान हों गयी
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2617)
- **Original**: भूपाल! इस प्रकार पूर्वक्रालमें तीनों लोकोंका हित चाहनेवाली देवी जिस प्रकार देवताओंके शरीरोंसे प्रकट हुई थीं, वह सब कथा मैंने कह सखुनायों
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2618)
- **Original**: अब पुन: देवताओंका उपकार करनेवाली वे देवी दुष्ट दैत्यों तथा शुम्भ-निशुम्भका वध करने एवं सब लोकोंकी रक्षा करनेके लिये गौरादेवीके शरीस्से जिस प्रकार प्रकट हुई थीं, वह सब्र प्रसद्भः मेरे मुँहसे सुनो। मैं उसका तुमसे बथावत्‌ वर्णन करता इगि श्रोमार्काप्डेगपएसपे स्रादार्गिके गन्तन्तरे वैदोगाहात्ममे शक्रादिस्तुति्ाम चतुर्थोज ध्यायः / 4
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2619)
- **Original**: उाच 5, अफसलोको 2, इलोका: 35, दृकपू 42, दृत्रणावितः
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2620)
- **Original**: डइंस प्रकार श्रीपाकंण्डेयपुराणमें सावर्णिक मन्वन्तरकी कथ्चाके अन्तर्गत देवीभाहात्मयपें 'श़क्रादिस्तुति ' नायक चौथा अध्याय पूरा हुआ
- **Translation**: 

---

