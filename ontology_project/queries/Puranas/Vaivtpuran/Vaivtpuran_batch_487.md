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

### Verse 1 (Vaivtpuran 27.17987)
- **Original**: परमात्मस्वरूपे च नित्यछपे सनातनि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 27.17988)
- **Original**: साकारे चर निराकारे सर्वरूपे नमोउस्तु ते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 27.17989)
- **Original**: क्षुत्तष्णेच्छा दया श्रद्धा निद्रा तन्द्रा स्मृति: क्षमा । एतास्तव कला: सर्वा नारायणि नमोस्तु ते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 27.17990)
- **Original**: लज्जामेधातुष्टिपुष्टिशान्तिसम्पत्तिवृद्धय: । एतास्तब कला: सर्वा: सर्वरूपे नमो5स्तु ते
- **Translation**: 

---

### Verse 5 (Vaivtpuran 27.17991)
- **Original**: वृष्टादृष्टस्वरूपे.. च तयोर्बीजफलप्रदे । सर्वानिर्वचचनीये चर महामाये नमोउस्तु ते
- **Translation**: 

---

### Verse 6 (Vaivtpuran 27.17992)
- **Original**: शिवे शंकरसौभाग्ययुक्ते सौभाग्यदायिनि । हरिं कान्ते च सौभाग्य देहि देवि नमोस्तु ते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 27.17993)
- **Original**: स्तोत्रेणानेन या: स्तुत्वा समाप्तेदिवसे शिवाम्‌ । नमन्ति परया भकक्‍त्या ता लभन्ति हरि पतिम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 27.17994)
- **Original**: इह कान्तसुखं भुक्‍त्या पतिं प्राप्य परात्यरम्‌ । दिव्य॑ स्वन्दनमारुहा यान्त्यन्ते कृष्णसंनिधिम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 27.17995)
- **Original**: इति औब्रह्मबैवर्ते जआनकौकुत पार्वतीस्तोजं सम्पूर्णम्‌। ( श्रोकृष्णजन्मखण्ड 27। 173--184) #ब*#र459700000
- **Translation**: 

---

### Verse 10 (Vaivtpuran 27.18825)
- **Original**: # श्रीकृष्णस्तोत्राणि * <23 55% $ $ $ ऊ $ # कफ $ # क 4 $ $ $ $ हक $ 5 4 कक कफ के 4 ऊ कफ 4 5 कफ कक फ 5545 कक $ कफ कक 55 कक क$ कड़क कक इत्येयमुक्त्वा सा देवी जले संन्यस्य विग्रहम्‌ । मनःप्राणांश्न श्रीकृष्णे तस्थौ स्थाणुसमा सत्ती
- **Translation**: 

---

### Verse 11 (Vaivtpuran 27.18826)
- **Original**: राधाकृतं हरे: स्तोत्र त्रिसंध्यं यः पठेन्नर: । हरिभक्तिं च दास्यं च लभेद्‌ राधागतिं धरुवम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 27.18827)
- **Original**: विपत्तौ यः पठेद्‌ भक्त्या सद्या: सप्पत्तिमाप्रुयात्‌ू । चिरकालगतं द्रव्यं हतं नष्ट च लभ्यते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 27.18828)
- **Original**: बन्धुवृद्धिर्भवेत्तस्प प्रसन्न मानस परम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 27.18829)
- **Original**: चिन्ताग्रस्त: पठेद भक्त्या परां निर्वुतिमाप्रुयात्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 27.18830)
- **Original**: पतिभेदे पुत्नभेदे मित्रभेदे च संकटे। मास भक्त्या यदि पतेत्सद्य: संदर्शन लभेत्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 27.18831)
- **Original**: भक्त्या कुमारी स्तोत्र च श्रृणुयाद्‌ वत्सरं यदि । श्रीकृष्णसदृ्शं कान्त॑ गुणवन्तं लभेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 27.18832)
- **Original**: इति श्रीब्रह्मवैवतें ए्ाकृत श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। (श्रीकृष्णजन्मखण्ड 27। 100--114) #+> >किस ची952202000 अष्टावक्रकृतं श्रीकृष्णस्तोत्रम्‌ अष्टावक्र उवाच गुणातीत गुणाधार गुणबीज गुणात्मक । गुणीश गुणिनां बीज गुणायन नमोउस्तु ते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 27.18833)
- **Original**: सिद्धिस्वरूप सिदध्यंश सिद्धिबीज परात्पर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 27.18834)
- **Original**: सिद्धसिद्धशणाधीश सिद्धानां गुरबे नमः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 27.18835)
- **Original**: है बेदबीज बेदज्ञ बेदिन्‌ बेदविदां बर । बेदाज्ञातोईओसि रूपेश बेदज्ञेश नमोउस्तु ते
- **Translation**: 

---

