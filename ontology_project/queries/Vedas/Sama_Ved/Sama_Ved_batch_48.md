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

### Verse 1 (Sama Ved 0.941)
- **Original**: जसिसहरेन 0 --यरन2-.30->--+_
- **Translation**: 

---

### Verse 2 (Sama Ved 0.942)
- **Original**: अथ चतुर्थो5 ध्याय:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.943)
- **Original**: पंचर्विश: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.944)
- **Original**: 352. प्रत्यस्मै पिपीषते विश्वानि खिदुषे भर । अरड्रमाय जग्मयेउपश्चादध्यने नर:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.945)
- **Original**: है यज़मान ! यज्ञ के संचालक, सोम पीने के इच्छुक, सर्वज्ञ, निश्चित समय पर उचित स्थान को प्राप्त कराने वाले, यज्ञ में जाने की कामना वाले, सर्वप्रथम यज्ञ वेदिका पर उपस्थित होने वाले इन्द्र को सोमरस से तृप्त करो
- **Translation**: 

---

### Verse 6 (Sama Ved 0.946)
- **Original**: 1 । 353. आ नो वयो वयःशयं महान्तं गद्दरेष्ठाम्‌ । महान्तं पूर्विणेष्ठामुग्रं बंचो अपावधी:ः ( हे इन्द्र) विशाल पर्वतों पर स्थित, सर्वत्र प्राप्त होने वाले, सोमरूपी अल से हमें परिपूर्ण कर दें । अत्यधिक प्रचलित निन्दित कथनों को आप हमसे दूर करें हम निन्‍्दनीय न बनें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.947)
- **Original**: 354. आ त्वा रथं यथोतये सुम्नाय वर्तयामसि । तुविकूर्मिमृतीषहमिन्द्रं शविष्ठ सत्पतिम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.948)
- **Original**: शत्रुओं को पराजित करने वाले, शौर्ययुक्त, यजगानों के पोषक हे शक्तिशाली इन्द्र ! संरक्षण एवं सुख के निमित्त, गतिशील रथ के समान, सब जगह घुमाते हुए, आप को हम (यजमानगण) यज्ञस्थल पर ले आते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.949)
- **Original**: 355. स पूर्व्यों महोनां बेन: क्रतुभिरानजे । यस्य द्वारा मनु: पिता देवेषु धिय आनजे
- **Translation**: 

---

### Verse 10 (Sama Ved 0.950)
- **Original**: याज्ञिक की सहायता से हतिष्यान्न सेवन करने के लिए, कर्मशील, सभी देवताओं के पोषक, चिन्तनशील, श्रेष्ठ इन्द्रदेव यज्ञ-स्थल पर उपस्थित होते हैं.
- **Translation**: 

---

### Verse 11 (Sama Ved 0.951)
- **Original**: 356, यदी वहन्त्याशवो भ्राजमाना रथेष्वा ।पिबन्तो मदिरं मधु तत्र श्रवांसि कृण्बते
- **Translation**: 

---

### Verse 12 (Sama Ved 0.952)
- **Original**: 5 हर्षवर्द्धक, मधुर सोमरस को पीने वाले, अन्न उत्पन्न करने वाले, तेजयुक्त, शीघ्र गतिशील मरुद्‌गण, इन्द्रदेव को यज्ञ वेदिका पर पहुँचाते है.
- **Translation**: 

---

### Verse 13 (Sama Ved 0.953)
- **Original**: 357. त्यमु वो अप्रहणं गृणीषे शवसस्पततिम्‌ । इन्द्र विश्वासाहं नरं शचिष्ठं विश्ववेदसम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.954)
- **Original**: यजमानों के हित के लिए कल्याणकारक, बल एवं अल के अधिपति, शत्रुओं को पराजित करने बाले, यज्ञ के नायक, शक्तिसम्पन्न, सर्वज्ञ इन्रदेव की (हम) स्तुति करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.955)
- **Original**: 358, दथिक्राव्णो अकारिषं जिष्णोरश्वस्थ वाजिन: । सुरभि नो मुखा करत्य ण आयूंषि तारिषत्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.956)
- **Original**: विजयशील, अश्व के समान तीव्र गतिशील, द्चिक्राव (कऋ्रषि) की हम स्तुति करते हैं, जो शारीरिक अंगों के पोषक और हमारी आयु में वृद्धि करने वाले हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.957)
- **Original**: 359. पुरां भिन्दुर्युवा कविरमितोजा अजायत । इन्द्रो विश्वस्य कर्मणो धर्ता बच्री पुरुष्ठतः
- **Translation**: 

---

### Verse 18 (Sama Ved 0.958)
- **Original**: वह (इन्द्र) शत्रु के नगरों का विध्व॑ंस करने वाला, युवा, ज्ञाता, अतिशक्तिशाली, शुभ कार्यों का आश्रयदाता, सर्वाधिक कीर्तियुकत होकर उत्पन्न हुआ है.
- **Translation**: 

---

### Verse 19 (Sama Ved 0.959)
- **Original**: इति पंचर्विशः खण्ड: 5
- **Translation**: 

---

### Verse 20 (Sama Ved 0.960)
- **Original**: डर सापवेद-संहिता
- **Translation**: 

---

