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

### Verse 1 (Vishnu Puran 0.401)
- **Original**: उस महात्मासे प्रथम तम (अज्ञान), मोह, सहामोह (भोगेच्छा), तासिस्र (क्रोध) और अन्भतासिस्त (अभिनित्रेदठ) नामक पतञ्मपर्वा (पाँच प्रकास्की) विद्या उत्पन्न हुई
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.402)
- **Original**: उसके ध्यान करनेपर ज्ञानशुन्य, आहर-भीतरसे तमोमय और जड् नगादि (वक्ष-गुल्म-छता-वोरुत्‌-तृण) रूप पाँच प्रकास्का सर्ग हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.403)
- **Original**: [वराहजीद्वारा सर्वप्रथम स्थापित होनेके ऋरषण]) नगादिकों मुख्य कहा गया है, इसछिये यह सर्ग भी सुख्य सर्म कहस्मता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.404)
- **Original**: उस सृष्टिको पुरुषार्थजी असाधिका देखकर उन्होंने फिर अन्य सर्गके लिये ध्यान किया तो तिर्यकु-स्रोत-सूृष्टि उत्पन्न हुई। यह सर्ग
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.405)
- **Original**: चायुके समान] तिरछा चलनेवाला है इसलिये तियंक-स्नरोत कहर्वता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.406)
- **Original**: ये पशु, पश्षी आदि नामसे प्रसिद्ध हैं--और भ्रायः तमोमय (अज्ञानी), विग्ेकरहित अनुचित सार्गका अवला्यन करनेवाले और विपरीत ज्ञानकों हो यथार्थ ज्ञान माननेवाले होते हैं। ये सब अहंकारोी, अभिपानो. अद्राईस व्घोंसे युक्त* आन्तरिक सुख आदिको ही पूर्णतथा समझनेवाले और परस्पर एक- अन्त: प्रकाशास्ते सर्वे आबृताश्च परस्परम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.407)
- **Original**: 19 दूसरेकी अवृत्िकों न जाननेवाले होते है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.408)
- **Original**: # सांख्य-कारिकामें अद्ठाइंस बध्षोंका वर्णन इस प्रकार किया हं-- एकादअन्द्रिववधा सर अध्यागिक्य धतस्त: ऊह।. शब्दोउध्यचने.. दुःखत्रिघातास्वयः बुद्धितफैशक्तिस्दिश । सप्दश प्रकायुपादानम्रालभाग्यास्या: । द्राह्या धिपयोपरमातु पशे॒ च नव तुष्टयोअभिमताः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.409)
- **Original**: सुहरभाप्ति: । दानक्ष स़्ध्ा नुद्धेर्तिपर्ययार्त्शिसि द्वीताम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.410)
- **Original**: सिद्धयोकी सिद्धे:. पूर्वोश्कुखिविधा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.411)
- **Original**: (49--51) प्यारह इद्रियव्ष और लुष्टि तथा सिद्धिफे विष्यंय्स सत्रह बुद्ध-पध--ये कुल अद्राईस वघ अज्क्ति कहलाते है। प्रकृति, उपाडान, काल और भाग्य नामक चार अ'्यात्पिक और पाँधों आऋनेद्धियेंके बाह्य विषयोकि तिवृत हो जनेसे पाँच शाह्म-- इस प्रकार
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.412)
- **Original**: तम्रप्यसाधकं प्रत्वा ध्यायतोःधन्यस्ततो5भवत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.413)
- **Original**: ऊर्ध्बत्नोतास्तृतीयस्तु सात््विकोर्ध्वमवर्त्तत
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.414)
- **Original**: 12 ते सुखप्रीतिबहुला बहिरन्तस्त्वनावृता: प्रकाशा बहिरन्तश्न ऊर्ध्वश्नोतोद्धवा: स्मृता:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.415)
- **Original**: 13 तुष्टात्मनस्तृतीयस्तु देवसर्गस्तु स स्पृतः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.416)
- **Original**: तस्मिन्सगेंभवलद्मीतिर्निष्पन्ने ब्रह्मणस्तदा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.417)
- **Original**: 14 ततो&न्यं स तदा दश्यो साथकं सर्गमुत्तमम्‌ । असाथकांस्तु ताउ़ात्या मुख्यसर्गादिसम्भवान्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.418)
- **Original**: 15 तथाभिध्यायतस्तस्य सत्याभिध्यायिनस्तत: । प्रादुर्बभूब चाव्यक्तादर्बाक्छ्रोतास्तु साधक:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.419)
- **Original**: चस्मादर्वाग्व्यवर्त्तन्त ततो5वाॉक्स्नोतसस्तु ते । ते च प्रकाशबहुलास्तमोद्रिक्ता रजोउधिका:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.420)
- **Original**: तस्पात्ते दुःखबहुला भूयोभूयश्व कारिण: । प्रकाशा बहिरन्तश्न मनुष्या: साधकास्तु ते
- **Translation**: 

---

