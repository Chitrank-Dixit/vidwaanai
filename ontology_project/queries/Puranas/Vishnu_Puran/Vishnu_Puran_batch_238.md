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

### Verse 1 (Vishnu Puran 0.4741)
- **Original**: 49 चतुर्दश्मभिरेतैस्तु गतैर्मन्वन्तरैद्विज । सहस््रयुगपर्यन्तः कल्पो निइशेष उच्यते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4742)
- **Original**: 50 ताबत्ममाणा च निशा ततो भवति सत्तम । ब्रह्मरूपधरइहेते.. झेषाहावम्बुसम्पवे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4743)
- **Original**: 51 त्रैलोक्यमखिलं ग्रस्त्वा भगवानादिकृद्धिभुः । स्वमायासंस्थितो विप्र सर्वभूतो जनार्दन:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4744)
- **Original**: 52 तत:ः प्रबुद्धो भगवान्‌ यथा पूर्व तथा पुनः । सृष्टि करोत्यव्ययात्या कल्पे कल्पे रजोगुण:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4745)
- **Original**: 53 मनवो भूभुजस्सेद्रा देवास्सप्तर्षयस्तथा। सात्विकॉंशः स्थितिकरों जगतो द्विजसत्तम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4746)
- **Original**: 54 चतुर्युगेषप्यसौ विष्णु: स्थितिव्यापारलक्षण: । युगव्यवस्थां कुरुते यथा मैत्रेय तच्छूणु
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4747)
- **Original**: 55 कुते सुगे पर ज्ञान कपिलादिस्वरूपधृक्‌ । द्दाति सर्बभूतात्मा सर्वभूतहिते रत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4748)
- **Original**: 56 चक्रवर्त्तिस्वरूपेण त्रेतायामपि स्‌ प्रभु: । दुष्टानां निग्रह कुर्वन्परिपाति जगत्मयम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4749)
- **Original**: 57 तृतीय अंश 169 हे मैत्रेय ! चौटहवाँ मनु भौम छोगा। उस समय शुति नामक इन्द्र और पाँच देवगण होंगे; उनके नाम सुनो--वे चाश्षुषर, पचित्र, कनिष्ठ, भ्राजिक और वाचावृद्ध नामक देवता हैं। अब तत्काल्गन सप्मर्षियोंके नाम भी सुनो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4750)
- **Original**: उस समय अग्रित्राहु, शचि, शुक्र, मागध, अध्रिध, युक्त और जित--ये सार्षि होंगे। अब मनुपुत्रोंके बिषयमें सुनो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4751)
- **Original**: हे मुनिशार्द्ल ! कहते हैं, उस मनुके ऊर और गम्भीरबुद्धि आदि पुत्र होंगे जो राज्याधिकारी होकर पृथिवीका पालन करेंगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4752)
- **Original**: प्रत्येक यतुर्युगके अच्तपें वेदॉंका छोप हो जाता है, उस समय सप्तर्षिणण ही स्वर्गलोकसे पृथिवीमें अवरतीर्ण होकर उनकतर प्रचार करते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4753)
- **Original**: प्रत्येक सत्ययुगके आदियें [ मनुष्योंकी धर्म-मर्यादा स्थापित करनेके लिये ) स्पृति-शास्त्रके रचयिता मनुका प्रादुर्भाव होता है; और उस मन्वन्तरके अन्त-पर्यन्त तत्कालीन देवगण यज्ञ-भागोंको भोगते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4754)
- **Original**: तथा मनुके पुत्र और डनके जेशघर मन्वन्तरकफे अन्ततक पृथिवोका पालन करते रहते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4755)
- **Original**: इस प्रकार मनु सप्तर्षि, देवता, इन्द्र तथा मनु-पुत्र राजागण--ये प्रत्येक मन्वन्तरके अधिकारों होते है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4756)
- **Original**: हे द्विज ! इन चौदह मन्वन्तरोंके बौत जानेपर एक सहस््र युग रहनेवाल्ला कल्प समाप्त हुआ कहा जाता हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4757)
- **Original**: है साधुश्रेष् ! फिर इतने ही समयकोी रात्रि होती है। उस्र समय ब्रह्मरूपधारी श्रीविष्णुभगवान्‌ प्रल्यकालीन जलके ऊपर शेष-शब्यापर शयन करते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4758)
- **Original**: हे विष्र ! तब आदिकर्ता सर्वन्यापक सर्वभूत भगवान्‌ जनार्दन सम्पूर्ण त्रिलोकौीका आस कर अपनी मायामें स्थित रहते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4759)
- **Original**: फिर [प्रक्ृूय-रात्रिका अन्त होनेपर] प्रत्येक कल्पके आदिमें अव्ययात्पा भगवान्‌ जाग्रत्‌ होकर रजोगुणका आश्रय कर सृष्टिकी रचना करते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4760)
- **Original**: हे द्विजश्रेष्ठ )! मनु, मनु-पूत्र राजागण, इन्द्र देवता तथा सप्रर्ष--ये सब जगतूक़ा पालन करनेवाले भगवागके सात्विक औहदा हैं
- **Translation**: 

---

