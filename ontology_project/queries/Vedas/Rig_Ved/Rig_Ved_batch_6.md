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

### Verse 1 (Rig Ved 0.101)
- **Original**: 44. यस्य संस्थे न वृण्वते हरी समत्सु शत्रव:। तस्मा इन्द्राय गायत
- **Translation**: 

---

### Verse 2 (Rig Ved 0.102)
- **Original**: (है याजको !) संग्राम में जिनके अश्वों से युक्त रथों के सम्मुख शत्रु टिक नहीं सकते, उन इन्द्रदेव के गुणों का आप गान करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.103)
- **Original**: 45, सुतपान्ने सुता इमे शुच्तयो यन्ति बीतये । सोमासो दष््याशिर:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.104)
- **Original**: यह निचोड़ा और शुद्ध किया हुआ टी मिश्रित सोमरस, सोमपान को इच्छा करने वाले इन्द्रदेव के निमित्त प्राप्त हो
- **Translation**: 

---

### Verse 5 (Rig Ved 0.105)
- **Original**: 46. त्वं सुतस्य पीतये सद्यो वृद्धो अजायथा:। इन्द्र ज्यैष्ठद्याय सुक्रतो
- **Translation**: 

---

### Verse 6 (Rig Ved 0.106)
- **Original**: है उत्तम कर्मवाले इन्द्रदेव ! आप सोमरस पीने के लिये देवताओं में सर्वश्रेष्ठ होने के लिये तत्काल वृद्ध रूप हो जाते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.107)
- **Original**: 47 आ त्वा विशन्त्वाशव: सोमास इन्द्र गिर्वण:। शं ते सन्तु प्रचेतसे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.108)
- **Original**: हे इद्धदेव ! तीजों सबतों में व्याप्त रहने वाला यह सोम, आपके सम्मुख उपस्थित रहे एवं आपके ज्ञान को सुखपूर्वक सपृद्ध करे
- **Translation**: 

---

### Verse 9 (Rig Ved 0.109)
- **Original**: 48. त्वां स्तोमा अवीबृधन्‌ त्वामुक्था शत्क्रतो । त्वां वर्धन्तु नो गिर:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.110)
- **Original**: हे सैकड़ों यज्ञ करने वाले इन्द्रदेव ! स्तोत्र आपकी वृद्धि करें । यह उक्थ (स्तोत्र) वचन और हमारी वाणी आपकी महत्ता बढ़ायें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.111)
- **Original**: 49, अक्षितोति: सनेदिमं बाजमिन्द्र: सहर्त्रणम्‌। यस्मिन्‌ विश्वानि पौंस्था
- **Translation**: 

---

### Verse 12 (Rig Ved 0.112)
- **Original**: रक्षणीय की सर्वथा रक्षा करने वाले इन्द्रदेव बल-पराक्रम प्रदान करने वाले विविध रूपों में विद्यमान सोम रूप अन का सेवन करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.113)
- **Original**: 50, मा नो मर्ता अभि द्वुहन्‌ तनूनामिन्द्र गिर्वण:। ईशानो यवया वधम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.114)
- **Original**: हे स्तुत्य इद्धदेव ! हमारे शरीर को कोई भी शत्रु क्षति न पहुँचाये । हमें कोई भी हिंसित न करे, आप हमारे संरक्षक रहें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.115)
- **Original**: [ सूक्त - 6 ] [ऋषि - प्रधुच्ठन्दा वैश्वामित्र । देवता-1-3 इत्र ; 4, 6. 8, 9 मरुद्गण; 5-7 मरुद्गण और इन ; 10 इन्द्र । छन्द-गायत्री
- **Translation**: 

---

### Verse 16 (Rig Ved 0.116)
- **Original**: ] 51. युठजन्ति ब्रध्ममरुष चरन्तं परि तस्थुष:। रोचन्ते रोचना दिवि
- **Translation**: 

---

### Verse 17 (Rig Ved 0.117)
- **Original**: ( वे इद्धदेव) चुलोक में आदित्य रूप में,भूमि पर अहिंसक अग्नि रूप में, अन्तरिक्ष में सर्वत्र प्रसरणशील वायु रूप में उपस्थित हैं। उन्हें उक्त तीनों लोकों के श्राणी अपने कार्यों में देवत्वरूप से सम्बद्ध मानते हैं।
- **Translation**: 

---

### Verse 18 (Rig Ved 0.118)
- **Original**: मं0 1 सृ0 6 है चुलोक में प्रकाशित होने वाले नक्षत्र-ग्रह आदि उन्हों (इद्धदेव) के ही स्वरूपांश हैं। (अर्थात्‌ तीनों लोकों की प्रकाशमयौ- प्राणमयी शक्तियों के वे हो एक मात्र संगठक हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.119)
- **Original**: 52. युञ्जन्त्यस्थ काम्या हरी विपक्षसा रथे। शोणा धृष्णू नवाहसा
- **Translation**: 

---

### Verse 20 (Rig Ved 0.120)
- **Original**: इन्द्रदेव के रथ में दोनों ओर रक्‍तवर्ण, संघर्षशील, मनुष्यों को गति देने वाले दो घोड़े नियोजित रहते हैं
- **Translation**: 

---

