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

### Verse 1 (Sama Ved 0.2781)
- **Original**: हे मधुर सोमदेव ! यज्ञशाला के श्रेष्ठ स्थान पर आसीन होने के लिए, मरुद्गणों के साथ आने वाले इन्द्रदेव के निमित्त, आप पवित्र होकर स्थिर हों
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2782)
- **Original**: 1077. त॑ त्वा विप्रा बचोविद: परिष्कृण्वन्ति धर्णसिम्‌। सं त्वा मृजन्त्यायव:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2783)
- **Original**: अखिल विश्व को धारण करने वाले, हे सोमदेव ! वाणी के विशेषज्ञ याजक, स्तुतियों से आपकी शोभा-बढ़ाते हुए भली-भाँति पवित्र कर रहे हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2784)
- **Original**: 1078.रस॑ ते मित्रो अर्यमा पिबन्तु वरुण: कवे। पवमानस्थ मरुत:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2785)
- **Original**: हे नूतन तत्वदर्शी सोम ! पवित्रतायुक्त आपके रस को मित्रवरुण,अर्यमा और मरुद्गण सेवन करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2786)
- **Original**: 1079, मृज्यमान: सुहस्त्या समुद्रे वाचमिन्वसि । रविं पिशड़ूं बहुल॑ पुरुस्पृहं पवमानाभ्यर्षसि
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2787)
- **Original**: श्रेष्ठ हाथों से शोधित सोमरस कलश पात्र में शब्द करते हुए गिरता है । हे पावन सोमदेव ! आप स्वर्ण-रंग से युक्त तथा अनेक लोगों दारा इच्छित प्रचुर धन हमें प्रदान करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2788)
- **Original**: 1080.पुनानो वारे पवमानो अव्यये वृषो अचिक्रदद्वने । देवानां सोम पवमान निष्कृतं गोभिरज्जानो अर्पसि
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2789)
- **Original**: बलवर्द्धक, पवित्रतायुक्त, शोधक द्वारा शोधित हुआ सोमरस, जल में अतिवेग से प्रवाहित होता है । हे शुद्धता से युक्त सोमदेव ! आप देवों के लिए गो-दुग्ध के साथ मिश्रित किये जाते हैं और पवित्र पात्र (द्रोण कलश) में स्थापित किये जाते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2790)
- **Original**: 1081.एतमु त्य॑ दश क्षिपो मृजन्ति सिन्धुमातरम्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2791)
- **Original**: समादित्येभिरख्यत
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2792)
- **Original**: जिस सोम की जननी समुद्र है, ऐसे सोम को शुद्ध करने में दसों अँगलियाँ सहायक हैं । ऐसा सोम, देवताओं को उपलब्ध होता है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2793)
- **Original**: 1082. समिन्द्रेणोत वायुना सुत एति पवित्र आ। सं सूर्यस्य रश्मिभि:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2794)
- **Original**: सूर्य रश्मियों से प्रकाशित हे सोम ! सुपात् में स्थिर हुए आप इन्द्रदेव और वायुदेव को प्राप्त होते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2795)
- **Original**: 1083.स नो भगाय वायदवे पृष्णे पवस्व मंधुमान्‌। चारुमित्रे वरुणे च
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2796)
- **Original**: हे मधुर और मनोहर सोम ! हमारे यज्ञ में भग, वायु, पूषा, मित्र और बरुण देवों के लिए आप शुद्ध हों
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2797)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2798)
- **Original**: केक ऊे
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2799)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2800)
- **Original**: 1084 रेवतीर्न: सधमाद इन्द्रे सन्तु तुविवाजा:। क्षुमन्तो याभिर्मदेम
- **Translation**: 

---

