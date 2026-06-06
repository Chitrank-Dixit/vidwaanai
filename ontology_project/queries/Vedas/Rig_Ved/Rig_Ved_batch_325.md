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

### Verse 1 (Rig Ved 0.6481)
- **Original**: [ सूक्त - 41 ] [ ऋषि- विश्वामित्र गाथिन । देवता- इद्ध
- **Translation**: 

---

### Verse 2 (Rig Ved 0.6482)
- **Original**: छत्द- गायत्री । ] 2840. आ तू न इन्द्र मक््यग्घुवान: सोमपीतये । हरिभ्यां याहाद्विव:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.6483)
- **Original**: हे इन्द्रदेव !सोमपान के लिए हम आपका आवाहन करते हैं, हमारे निकट हरिसंज्ञक अश्वों के साथ आये
- **Translation**: 

---

### Verse 4 (Rig Ved 0.6484)
- **Original**: 2841. सत्तो होता न ऋ्वियस्तिस्तिरे बर्हिरानुषक्‌। अयुश्रन्यातरद्रयः
- **Translation**: 

---

### Verse 5 (Rig Ved 0.6485)
- **Original**: हमारे यज्ञ में ऋतु के अनुसार यज्ञकर्त्ता होता बैठे हैं । उन्होंने कुश के आसन बिछाये हैं और सोम-अभिषव॒ के लिए पाषाण खण्ड को संयुक्त किया है । हे इद्धदेव ! आप सोमपान के निमित्त आयें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.6486)
- **Original**: 2842. इमा ब्रह्म ब्रह्मवाह: क्रियन्त आ बहिं: सीद
- **Translation**: 

---

### Verse 7 (Rig Ved 0.6487)
- **Original**: वीहि शूर पुरोछाशम्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.6488)
- **Original**: हे शुरवीर इन्द्रदेव ! स्तोतागण इन स्तुतियों को सम्पादित करते हैं । अतएव आप इस आसन पर बैठें और पुरोडाश का सेवन करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.6489)
- **Original**: 2843. रारन्धि सबनेषु ण एपु स्तोमेषु वृत्रहन्‌। उक्थेष्विन्द्र गिर्वण:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.6490)
- **Original**: हे स्तुति-योग्य, वृत्रहन्ता इन्द्रदेव ! आप यज्ञ में तीनों सवनों में किये गये स्तोत्रों और मंत्रों में रमण करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.6491)
- **Original**: 2844. मतयः सोमपामुरुं रिहन्ति शवसस्पततिम्‌। इन्द्रं वत्सं न मातर:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.6492)
- **Original**: हमारी ये स्तुतियाँ महान्‌ सोमपायी और बलों के अधिपति इन्धदेव को उसो प्रकार प्राप्त होतो हैं, जिस प्रकार गौएँ अपने बहड़ों को प्राप्त होती हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.6493)
- **Original**: 2845, स मन्दस्वा ह्ान्धसो राधसे तन्वा महे। न स्तोतार॑ निदे कर:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.6494)
- **Original**: हे इन्द्रदेव
- **Translation**: 

---

### Verse 15 (Rig Ved 0.6495)
- **Original**: विपुल धनराशि दान देने के लिए आप सोम युक्त हविष्यात्र से अपने शरोर को प्रसन्न करें । हम स्तोताओं को निन्दित न होने दें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.6496)
- **Original**: 2846. वयमिन्द्र त्वायवो हविष्मन्तो जरामहे । उत त्वमस्मयुर्वसो
- **Translation**: 

---

### Verse 17 (Rig Ved 0.6497)
- **Original**: है सबके आश्रय प्रदाता इन्द्देव ! आपकी अभिलाषा करते हुए हम हवियों से युक्त होकर आपको स्तुति करते हैं। आप हमारी रक्षा करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.6498)
- **Original**: 60 ऋग्वेद संहिता भाग - 2 2847, मारे अस्मद्ठि मुप्ुचो हरिप्रियार्वाडः याहि। इन्द्र स्वधावों मत्स्वेह
- **Translation**: 

---

### Verse 19 (Rig Ved 0.6499)
- **Original**: हे हरि संज्ञक अश्रों के प्रिय स्वामी इन्द्रदेव ! आप अपने घोड़ों को हमसे दूर जाकर न खोलें । हमारे पास आयें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.6500)
- **Original**: इस यज्ञ में आकर हर्षित हों
- **Translation**: 

---

