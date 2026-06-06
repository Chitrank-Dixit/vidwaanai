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

### Verse 1 (Vishnu Puran 0.3361)
- **Original**: पृष्करद्वीप चारों ओरसे अपने ही समान विस्तारवाले मीठे पानीके समुद्रसे मण्डरूके समान घिरा हुआ है।
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3362)
- **Original**: इस प्रकार सातों ट्वीप सात समुद्रोंसे धिरे हुए हैं और वे द्वीप तथा [उन्हें घेरनेवाले] समुद्र परस्पर समान हैं, और उत्तरोत्तर दूने होते गये हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3363)
- **Original**: सभी समुद्रोंमें सदा समान जल रहता है, उसमें कभी न्यूनता अथवा अधिकता नहों छोतो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3364)
- **Original**: हे घुनिश्रेष्ठ ! पात्रका जल जिस प्रकार अभ्रिका संयोग होनेसे उबलने लूगता है उसी प्रकार चन्द्रमाकी कत्म्रओंके बवुनेसे समुद्रका जल भी बढ़ने लगता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3365)
- **Original**: कुक और कृष्ण पक्मॉंपें चन्द्रमाके उदय और अस्तसे न्यूनाधिक न होते हुए हो जल घटता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3366)
- **Original**: 120 दक्षोत्तराणि पञ्चैव ह्ुजुलानां झतानि वै। अपां वृद्धिक्षयों दृष्टो सामुद्रीणां महापुने
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3367)
- **Original**: 91 भोजन पुष्करद्वीपे तत्र स्वयमुपस्थितम्‌। षड़स भुझते विप्र प्रजा; सर्वा: सदैव हिं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3368)
- **Original**: 92 स्वादूदकस्य परितो दृश्यतेडलोकसंस्थिति: । द्विगुणा काञ्ननी भूमि: सर्व॑जन्तुविवर्जिता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3369)
- **Original**: 93 लोकात्त्रेकस्ततइदौल्ओे योजनायुतबिस्तृत: । उच्छुयेणापि तावन्ति सहस्नाण्यचलो हि सः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3370)
- **Original**: 94 ततस्तमः समावृत्य त॑ शैलें सर्वतः स्थितम्‌। त्तमश्नाण्डकटाहेन. समत्तात्परिवेष्टितम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3371)
- **Original**: 95 पञ्चाशत्कोटिविस्तारा सेयमुर्वी महामुने । सहैवाण्डकटाहेन. सद्दीपाब्धिमहीधरा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3372)
- **Original**: 96 सेय॑ धात्री विधात्री न सर्वभूतगुणाधिकरा । आधारभूता सर्वेषां मैन्नेय जगतामिति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3373)
- **Original**: 97 श्रीम्रिष्णुपुराण (अण्5 और बढ़ता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3374)
- **Original**: हे महामुने ! समुद्रके जल्की वर्धि और क्षय पाँच सौ दस (510) अंगुल्तक देखी जाती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3375)
- **Original**: है विप्र ! पुष्करद्वीपमें सम्पूर्ण प्रजाबर्ग सर्वदा [बिना प्रयक्रके) अपने-आप हो श्राप्त हुए षड्रस भोजनका आहार करते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3376)
- **Original**: स्वादूदक (मीठे पानीके) समुद्रके चारों ओर व्लेक- निवाससे शून्य और समस्त जीवॉंसे रहित उससे दूनों सूबर्णमयी भूमि दिखायी देती है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3377)
- **Original**: वहाँ दस सहस्न विस्तारवास्म ल्लेकालोक-पर्बत है। वह पर्वत ऊँचाईमें भी उतने ही सहस्न योजन है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3378)
- **Original**: उसके आगे उस पर्बतको सब ओरसे आवुतकर घोर अन्धकार छाया हुआ है, तथा यह अन्धकार चारों ओरसे बह्याप्ड-कटाहसे आवृत है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3379)
- **Original**: हे महामुने ! अणप्डकटाहके सहित समुद्र और पर्वतादियुक्त यह समस्त भूमण्डल पचास करोड़ योजन विस्तारवात्म है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3380)
- **Original**: हे मैत्रेय ! आकाशादि समस्त भूतोंसे अधिक गुणवाल्मी यह पृथिवी सम्पूर्ण जगत्की आधारघृता और उसका पालन तथा उद्धव करनेवाली है
- **Translation**: 

---

