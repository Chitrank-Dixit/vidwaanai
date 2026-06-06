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

### Verse 1 (Vishnu Puran 0.7741)
- **Original**: किंतु जब इतने दिनोंतक वे उसमेंसे न निकले तो उन्होंने समझा कि 'अवदय हो श्रीमधुसूदन इस गुफामें मारे गये, नहीं तो जीवित रहनेपर जत्रुके जीतनेमें उन्हें इतने दिन क्‍यों लगते ?' ऐसा निश्चय कर वे द्रारका्गे चले आये और यहाँ. कष्ट दिया कि श्रीकृष्ण मारे गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7742)
- **Original**: उनके बन्धुओंने यह सुनकर समयोचित सम्पूर्ण औध्व॑दैहिक कर्म कर दिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7743)
- **Original**: इधर, अति श्रद्धापूर्वक दिये हुए विशिष्ट पात्रोंसहित इनके अन्न और जलसे युद्ध करते समय श्रीक्रष्णनन्द्रके बल और प्राणकी पुष्टि हो गयो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7744)
- **Original**: तथा अति महान्‌ पुरुषके द्वारा मार्दित होते हुए उनके अत्यन्त निष्ुर प्रह्ारोंकि आधघातसे पीडित शरीरवाले जाम्बवानूका बल नियाहार रनेसे क्षीण हो गया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7745)
- **Original**: अन्तमें भगवानसे पराजित होकर आम्बयानने उन्हें प्रणाम करके कहा--
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7746)
- **Original**: “भगवन्‌ ! आपको तो देवता, असुर, गन्धर्व, यक्ष, राक्षस आदि कोई भी नहों जीत सकते, फिर पृथिवीतलपर रहनेवाले अल्पवीर्य मनुष्य अथवा मनुष्योंके अलयवभूत हम-जैसे तिर्यकू-योनिगत जीवॉकी तो बात ही क्या है ? अवदय ही आप हमारे प्रभु श्रोगमचद्धजीके समान सकल लोक-प्रतिपाकुक भगवान्‌ नारायणके ही अंशसे प्रकट हुए हैं।' जाम्बवानके ऐसा कहनेपर भगवानने पृथिवीका भार उतारनेके ह्थियि अपने अवतार झेनेका सम्पूर्ण वतान्त उससे कह दिया और उसे प्रीतिपूर्वक अपने हाथसे छूकर युद्धके श्रमसे रहित कर दिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7747)
- **Original**: 2734 अश्रीविष्णुपराण [ अ» 13 सच प्रणिपत्य पुनरप्येन॑ प्रसाद्य जाम्नवर्ती नाम कन्यां गृहागतायार्ध्यभूतां ग्राहयामास
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7748)
- **Original**: स्थमन्तकमणिरत्रमपि प्रणिपत्य तस्मै प्रददो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7749)
- **Original**: अच्युतो5प्यतिप्रणतात्तस्मादग्राह्ममपि तन्मणिरत्रमात्मसंझोधनाय जग्माह
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7750)
- **Original**: सह जाम्बवत्या स द्वारकामाजगाम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7751)
- **Original**: भगवदागमनोद्धूतहर्षोत्कर्षस्थ द्वारकावासि- जनस्य कृष्णायलोकनात्तस्क्षणमेवातिपरिणत- वयसो5पि नवयौवनमिवाभवत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7752)
- **Original**: दिछ्टया दिष्व्वेति सकलयादवा:ः ख्रियश्ष सभाजयामासु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7753)
- **Original**: भगवानपि यथानुभूतमशेष॑ यादव- समाजे यथावदाचचक्षे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7754)
- **Original**: स्थमन्तकं॑ च सत्राजिते दत्त्वा मिथ्याभिशस्तिपरिशुद्धिमवाप
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7755)
- **Original**: जाम्बबती चान्तःपुरे निवेशया- मास
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7756)
- **Original**: सत्राजिदपि मयास्यथाभूतमलिनमारोपितमिति जातसन्तरासात्स्वसुर्ता सत्यभामां भगवते भार्यार्थ ददौ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7757)
- **Original**: ता चाक्रूरकृतवर्मशतधन्वप्रमुखा यादवा: प्राग्वर्याम्बभूवु:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7758)
- **Original**: ततस्त- त्यदानादबन्नातमेबात्मानं॑ मन्यमाना: सन्नाजिति बैरानुबन्ध चक्कु:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7759)
- **Original**: अक्रूरकृतवर्मप्रमुखाश्च॒_ शतधन्यानपूचु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7760)
- **Original**: अयमतीव दुरात्मा सत्राजिद्‌ योउस्माभि- भंवता च॒ प्रार्थितो5प्यात्मजामस्मान्‌. भवतन्ते चाविगणय्य. कृष्णाय.. दत्तवान्‌
- **Translation**: 

---

