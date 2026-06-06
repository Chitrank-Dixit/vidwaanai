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

### Verse 1 (Vaivtpuran 543.17674)
- **Original**: मीज्यालयतबुप भोज ब स्तोत्र-कवच-संग्रह कुछ प्रेमी तथा श्रद्धालु सजनोंका अनुरोध है कि ब्रह्मनैवर्तपुराणमें आये हुए महत्त्वपूर्ण स्तोत्रों तथा कवचोंका संग्रह पाठ करनेवालोंकी सुविधाके लिये एक स्थानपर अवश्य छाप दिया जाय। उसीके अनुसार यह छापा जा रहा है। श्रद्धा रखनेवालोंके लिये ये स्तोत्र-कबचादि बस्तुतः बड़े ही महत्त्वपूर्ण और लाभप्रद हैं। --सम्पादक [
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17675)
- **Original**: अल हमार गणेशस्तोत्रम्‌ नारायण उवाच अथ विष्णु: सभामध्ये सम्पूज्य ते गणेश्वरम्‌ । तुष्टाव परया भकत्या सर्वविधश्नविनाशकम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17676)
- **Original**: श्रीविष्णुरुवाच ईश त्वां स्तोतुमिच्छामि ब्रह्मग्योति: सनातनम्‌ । निरूपितुमशक्तो5हमनुरूपमनीहकम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17677)
- **Original**: प्रवर॑ सर्वदेवानां सिद्धानां योगिनां गुरुम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17678)
- **Original**: सर्वस्वरूप सर्वेशं ज्ञानराशिस्वरूपिणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17679)
- **Original**: अव्यक्तमक्षर॑ नित्य सत्यपम्रात्मस्वरूपिणम्‌ । वायुतुल्यातिनिरलिपं चाक्षतं सर्वसाक्षिणम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17680)
- **Original**: संसाराणबपारे च॒ मायापोते सुदुर्लभे । कर्णधारस्वरूप॑ च॒ भक्तानुग्रहकारकम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17681)
- **Original**: खरे वरेण्यं यरदं॑ बरदानामपीश्वरम्‌ । सिद्ध सिद्धिस्वरूपं च सिद्धिदं सिद्धिसाधनम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17682)
- **Original**: ध्यानातिरिक्त ध्येयं च ध्यानासाध्यं च धार्मिकम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17683)
- **Original**: धर्मस्वरूप॑ धर्मज्ञ धर्माथर्मफलप्रदम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17684)
- **Original**: बीज॑ संसारवृक्षाणामादडरं च॒ तदाश्रयम्‌ । स््रीपुन्नपुंकानां च॒ रूपमेतदतीन्द्रियम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17685)
- **Original**: सर्वदह्यमग्रपूज्य॑ च. सर्वपूण्य गुणार्णवम्‌ । स्वेच्छया सगुणं ब्रह्म निर्गुणं चापि स्वेच्छया
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17686)
- **Original**: स्वयं प्रकृतिरूपं च्र॒ प्राकृतं प्रकृते: परम्‌। त्वां स्तोतुमक्षमो उनन्त: सहस्त्रवदनेन च
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17687)
- **Original**: न क्षम: पश्रवक्रश्न॒ न क्षमअ्तुरानन: । सरस्वती न शक्ता च न शक्तो5हं तब स्तुतौ। न शक्ताश्व चतुर्वेदा: के वा ते वेदवादिन:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 675.5660)
- **Original**: लेकर कीटपर्यन्त सारा जगत्‌ नश्वर ही है, केवल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 675.5661)
- **Original**: तपस्याओं, देवताओं और पुण्योंका जो सारतत्त्व निर्गुण परब्रह्म श्रीकृष्ण ही नित्य सत्य हैं। ब्रह्मा,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 675.5662)
- **Original**: है, वह श्रीकृष्ण है। श्रीकृष्ण-भक्तिसे हीन जो विष्णु और शिव आदिकी आदिजननी परात्परा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 675.5663)
- **Original**: मूढ़ मनुष्य है, वह निश्चय ही जीते-जी मृतकके प्रकृति मैं ही हूँ। मैं सगुणा, निर्गुणा, श्रेष्ठ, सदा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 675.5664)
- **Original**: समान है। श्रीकृष्ण-भक्तोंको छूकर बहनेवाली स्वेच्छामयी, नित्यानित्या, सर्वरूपा, सर्वकारणकारणा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 675.5665)
- **Original**: वायुका स्पर्श पाकर सारे तीर्थ पवित्र हो गये और सबको बीजरूपा मूलप्रकृति ईश्वरी हूँ।
- **Translation**: 

---

