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

### Verse 1 (Vaivtpuran 39.8099)
- **Original**: 3 हीं मे पातु कपालं॑ च 3» हां श्रीमिति लोचने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8100)
- **Original**: पातु में कर्णयुस्मं॑ च 3& दुर्गाय॑ नमः सदा । 7+ हीं श्रोमिति नासां में सदा पातु च सर्वतः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8101)
- **Original**: हीं श्रों हृमिति दन्ताति पातु क्लैमोष्टयुग्मकम्‌ । क्रौं क्रो क्रीं पातु कण्ठं च दुर्गे रक्षतु गण्डकम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8102)
- **Original**: स्कन्ध॑ दुर्गविनाशिन्ये स्वाहा पातु निरन्तरम्‌ । वक्षो विपद्विनाशिन्यै स्वाहा में पातु सर्वतः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8103)
- **Original**: दुर्ग दुर्गे रक्षणीति स्वाहा नाभि सदाउवतु । दुर्गे दुर्गे रक्ष रक्ष पृष्ठे मे पातु सर्वतः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8104)
- **Original**: 3 हु दुर्गाय स्वाहा च हस्तौ पादौ सदाउवतु । 3» हां दुर्गाय॑ स्वाहा च सर्वाड्रं मे सदाउवतु
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8105)
- **Original**: प्राच्यां पातु महामाया आग्रेय्यां पातु कालिका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8106)
- **Original**: दक्षिणे दक्षकन्या च नैर्त्यां शिवसुन्दरों
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8107)
- **Original**: पश्चिमे पार्वती पातु वाराही वारुणे सदा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8108)
- **Original**: कुबेरमाता कौबेयपिशान्यामीधरी. सदा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8109)
- **Original**: ऊर्ध्वे नारायणी पातु अम्बिकाध: सदा5वतु । ज्ञाने ज्ञानप्रदा पातु स्वप्रे निद्रा सदाउवतु
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8110)
- **Original**: इति ते कथित वत्स सर्वमन्त्रौषविग्रहम्‌ । ब्रह्माण्डबिजयं नाम कवच परमाद्भधुतम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8111)
- **Original**: सुल्लात: सर्वतीर्थेषु. सर्वयज्ञेपु यतू. फलम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8112)
- **Original**: सर्वव्रतोपवासे च ततू फल लभते नरः#
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8113)
- **Original**: गुरुमभ्यर्च्य विधिवद्‌ू. वस्व्रालंकारचन्दनै: । कष्ठे या दक्षिणे बराहौँ कबचं धारयेतु यः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8114)
- **Original**: सच जैलोक्यविजयी सर्दशत्रुप्रमर्दक:। इंद॑ कवचमज्ञात्वा भजेद्‌. दुर्गतिनाशिनीम्‌ । ज्ञतलक्षप्रजप्तोतपि न मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8115)
- **Original**: कवच. काण्वशाखोक्तमुक्त॑ नारद सुन्दरम्‌। यस्मै कसम न दातव्य॑ गोपनीय सुदुर्लभम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8116)
- **Original**: (गणपतिखण्ड 39। 3--23)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8117)
- **Original**: + गणपतिखण्ड « 381 परशुरामद्वारा पुत्रसहित राजा सहस्तराक्षका बध, कार्तवीर्य-परशुराम-युद्ध, परशुरामकी मूर्च्छा, शिवद्वारा उन्हें पुनरज बन दान, काव्य, परशुराम -संवाद, आकाशवाणी सुनकर शिवका धारण करके कवच माँग लेना, परशुद्वारा कार्तवीर्य तथा अन्यान्य क्षत्रियोंका संहार, ब्रह्मका आगमन और परशुरामको गुरुस्वरूप शिवकी शरणमें जानेका उपदेश देकर स्वस्थानको लौट जाना श्रीनारायण कहते हैं--नारद ! जब भगवान्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8118)
- **Original**: महाबली भाई कार्तवीर्यसे पीड़ित होकर भाग विष्णु महालक्ष्मी-कवच तथा दुर्गा-कवचकों
- **Translation**: 

---

