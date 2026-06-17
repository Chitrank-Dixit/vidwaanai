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

### Verse 1 (Rig Ved 0.8741)
- **Original**: [ सूक्त - 22
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8742)
- **Original**: [ऋषि - विश्वसामा आत्रेय । देवता - अग्नि
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8743)
- **Original**: छन्द - अनुष्टप्‌: 4 पंक्ति
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8744)
- **Original**: ] 3798. प्र विश्वसामन्नत्रिवर्द्या पावकशोचिषे । यो अध्वरेष्वीड्यों होता मन्द्रतमो विशि
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8745)
- **Original**: हे विश्वसामा उग़ते ! आप पत्रित्र दीप्ति युक्त उन अग्निदेव का अग्रि त्रग्रष के समान पूजन करें । ये अग्निटेव सब ऋषियों द्वारा स्तुत्य है । ये देवों के आवाहक और अत्यन्त पूजनोय है
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8746)
- **Original**: 3799. न्‍्य1ग्निं जातवेदसं दाता देवप्रृत्विजम्‌ । प्र यज्ञ एत्वानुषगद्या देवव्यचस्तम:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8747)
- **Original**: हे यजमानों ! सब प्राणियों को जानने वाले, दिव्य यज्ञकर्ता अग्निदेव को आप स्थापित करें; जिससे देवों के लिए प्रीतिकर और यज्ञ के साधन रूप हवि-पदार्थ हम अग्निदेव के निमित्त प्रदान करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8748)
- **Original**: 3800, चिकित्विन्मनसं त्वा देवं पर्तास ऊतये
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8749)
- **Original**: वरेण्यस्य तेडवस इयानासो अमन्महि
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8750)
- **Original**: है अग्निदेव ! आप ज्ञान से सम्पन्न और मन से दीप्तिमान्‌ हैं। अपनी रक्षा के तिमित हम सब मनुष्य आपके सम्मुख उपस्थित होते हैं और आपको श्रेष्ठ हवियों से सन्तुष्ट करते हुए स्तुति करते हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8751)
- **Original**: 3801, अग्ने चिकिद्धयश्स्थ न इद बच: सहस्य। तं त्वा सुशिप्र दप्पते स्तोमैर्वर्धन्त्यत्रयो गीर्मि: शुप्भन्त्यत्रय:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8752)
- **Original**: है बलपुत्र अभ्ददेव ! आप हमारे इन उत्तम वचनों को जानें । हे सुन्दर हनु (ठोड़ी) और नासिका वाले गृहपालक अभ्निदेव ! अब्रि वंशज आपको उत्तम स्तोत्रों द्वारा प्रवृद्ध करते हैं और उत्तम वाणियों द्वारा सुशोभित लरते हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8753)
- **Original**: श्ष्ट ऋग्वेद संहिता भागे - 2 [ सूक्त - 23 ] [ ऋषि - दुम्न विश्वरर्षणि आत्रिय । देवता - अग्नि
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8754)
- **Original**: छन्द - अनुष्ट॒पु: 4 पंक्ति ।] 3802. अग्ने सहन्तमा भर द्युम्नस्य प्रासहा रयिम्‌। विद्या यश्चर्षणीरभ्या3सा वाजेषु सासहत्‌
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8755)
- **Original**: है अभ्नदेव ! 'दुम्म' ऋषि के लिए शत्रुओं का ऐश्वर्य जीतकर लाने वाला एक वीर पुत्र प्रदान करें; जो स्तोत्रों से युक्त होकर युद्धों में सम्पूर्ण शत्रुओं को पराभूत कर सके
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8756)
- **Original**: 3803. तमग्ने पृतनाषहं रयिं सहस्व आ भर । त्व॑ हि सत्यो अद्भुतो दाता वाजस्थ गोमतः
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8757)
- **Original**: है बलशाली अग्निदेव ! आप सत्यस्वरूप, अद्भुत और गवादियुक्त अन्नों को देने वाले है। आप हमारे निमित्त शत्रुओं की सेना का ऐश्वर्य जीतकर हमें प्रदान करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8758)
- **Original**: 3804, विश्वे हि त्वा सजोषसो जनासो वृक्तबर्हिष:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8759)
- **Original**: होतारं सद्यसु प्रियं व्यन्ति वार्या पुरु
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8760)
- **Original**: हे अम्निदेव ! आप देवों का आड्वान करने वाले 'होता' रूप और सबके हितकारी हैं । ये सम्यक्‌ प्रीति रखने बाले और यज्ञार्थ कुश लाने वाले ऋ्विग्गण आपसे वरणीय धनों की याचना करते हैं
- **Translation**: 

---

