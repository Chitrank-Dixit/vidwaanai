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

### Verse 1 (Vishnu Puran 0.9081)
- **Original**: 24 कंसस्तूर्णमुपेत्यैनां ततो जग्राह बालिकाम्‌ । मुझ मुझ्लेति देवक्या सन्नकण्ठ्या निवारित:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9082)
- **Original**: 25 चिक्षेप चर शिलापृष्े सा क्षिप्ता वियति स्थिता । अबाप रूप सुमहत्सायुधाष्टमहाभुजम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9083)
- **Original**: 26 प्रजहास तथैवोच्चै: कंसं च रुषिताब्र॒जीत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9084)
- **Original**: किं मया क्षिप्तया कंस जातो यस्त्वां वधिष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9085)
- **Original**: 27 सर्वस्व॒भूतो देवानामासीन्मृत्यु: पुरा स ते । तदेतत्सम्प्रधार्याशु क्रियतां हितमात्मन:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9086)
- **Original**: 28 इत्युक्त्वा प्रययौ देवी दिव्यस्रमान्थभूषणा । पश्यतो भोजराजस्य स्तुता सिद्धैर्थिहायसा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9087)
- **Original**: 29 फश्तम अंश 3517 प्रभावसे अचेत हो गये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9088)
- **Original**: उस साजिके समय लर्पा करते हुए मेघोंकी जल्राशिकों अपने फर्णोंस रोककर श्रीशेषजी आनकदुन्दुभिके पीछे-पीछे चले
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9089)
- **Original**: भगवान्‌ विष्णुकों ले जाते हुए वसुदेवजी नाना भ्रकारके सैकड़ों भैंवरोंसे भरी हुई अत्यन्त गम्भीर यमुगाजीकों शुटनॉतक स्ख़कर हो पार कर गये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9090)
- **Original**: उन्होंने वहाँ यपुनाजीके तटपर ही कैसको कर देनेके लिये आये हुए नन्‍्द आदि बृद्ध गोपोंकों भी देखा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9091)
- **Original**: हे मैत्रेय ! इसी समय योगनिद्राके प्रभावसे सब मनुष्योंके मोहित हो जानेपर मोहित हुई यशोदाने भी उसी कन्याको जन्म दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9092)
- **Original**: तब अतिशय कान्तिमान्‌ वसुदेक्जी भी उस बालकको सुल्त्रकर और कन्याको लेकर तुरन्त यश्ञोदाके शयन-गृहसे चले आये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9093)
- **Original**: जब यदोदाने जागनेपर देखा कि ठसके एक नीलकमलदलके समान इ्यामलर्ण पुत्र उत्पन्न हुआ है तो उसे अत्यन्त प्रसन्नता हुई
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9094)
- **Original**: इधर, वसुदेवजीने कन्याकों ले जाकर अपने महलमें देक्कीके शायन-गृहपें सुल्त्र दिया और पूर्वबत्‌ स्थित हो गये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9095)
- **Original**: हे द्विज ! तदनन्तर बालकके रोमेका शब्द सुनकर कारागृह-रक्षक सहसा उठ खड़े हुए और देववीके सत्तान उत्पन्न होनेका बृत्तात्त कंसकों सुना दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9096)
- **Original**: यह सुनते ही कंसने त्रन्त जाकर देवकीके रुँघे हुए कण्ठसे 'छोड़, छोड़ -- ऐसा कहकर गेकनेपर भी उस बाल्िकाकों पकड़ लिया और उसे एक शिलापर पटक दिया । उसके पटकते ही बह आकाशाँं स्थित हो गयी और उसने शख्रयुक्त एक महागू्‌ अष्टभुजरूप धारण कर लिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9097)
- **Original**: तब उसने ऊँचे स्वस्से अट्टहास किया और कंससे शणोषपूर्वक कहा--“अरे कंस ! मुझे पटकनेसे तेरा क्या तप्रयोजन सिद्ध हुआ 2 जो तेरा वध करेगा उसने तो [ पहले ही ] जन्म ले लिया हैं; देवताओंके सर्वस्व वे हरि हो तुम्हारे [ कालनेमिरूप
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9098)
- **Original**: पूर्वजन्ममें भी का थे। अतः ऐसा जानकर तू शीघ ही अपने हितका उपाय कर'
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9099)
- **Original**: ऐसा कह, वह दिव्य माल्ता और चन्दनादिसे विभूषिता तथा सिद्धगणद्वारा स्तुति को जाती हुई देवी भोजराज कंसके देखते-देखते आकाझमार्गसे चलो गयी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9100)
- **Original**: +++++ हे न इति श्रीविष्णुपुराणे पश्चमेंठशी तुतोयोउध्यायः
- **Translation**: 

---

