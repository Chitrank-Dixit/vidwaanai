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

### Verse 1 (Vishnu Puran 0.12281)
- **Original**: 2 सर्वभूतमयो5क्न्तयो भगवान्भूतभावन: । अनादिरादिर्विश्वस्थ पीत्वा वायुमशेषत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12282)
- **Original**: 3 एकार्णवे ततस्तस्मिज्व्छेषशब्यागत: प्रभु: । ब्रह्मरूपधरइशेते. भगवानादिकृद्धरि:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12283)
- **Original**: 4 जनत्तोकगतैस्सिद्धैस्सनकाझैरभिष्टतः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12284)
- **Original**: ब्रहलोकगतैश्षैव चिन्त्यमानो मुमुक्षुभि:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12285)
- **Original**: 5 आत्ममायाम्रयी दिव्यां योगनिद्रां समास्थित: । आत्पानं बासुदेबाख्यं चिन्तयन्मधुसूदन:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12286)
- **Original**: 6 एप नैमित्तिको नाम मैत्रेय प्रतिसझ्जरः । निमित्त॑ तत्र यच्छेते ब्रह्मरूपधरों हरि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12287)
- **Original**: 7 यदा जागर्ति सर्वात्मा स॒ तदा चेष्टते जगत्‌ । निमीलत्येतद्खिलें मायाशय्यां गतेच्युते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12288)
- **Original**: 8 पद्मयोनेर्दिनं. यत्तु. चतुर्युगसहस्नरवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12289)
- **Original**: एकार्णवीकृते छोके ताबती रात्रिरिष्यते ।। 9 ब्रिलोकी एक महासमुद्रके समान हो जाती है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12290)
- **Original**: हे पैत्रेय ! तदनन्तर, भगवान्‌ विष्णुके मुख-नि:श्राससे प्रकट हुआ वायु उन मेषोंको नष्ट करके पुन: सौ वर्षतक चलता रहता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12291)
- **Original**: फिर जनलोकनिवासी सनकादि सिद्धनणसे स्तुत और ब्रह्मलोकको प्राप्त हुए मुमुक्षुओंसे ध्यान किये जाते हुए सर्वभूतमय, अचित्य, अनादि, जगत्‌के आदिकारण, आदिकर्ता, भूतभावन, मधुसूदन भगबान्‌ हरि विश्वके सम्पूर्ण यायुको पीकर अपनी दिव्य- मायारूपिणी योगनिद्राका आश्रय ले अपने वासुदेवात्पक स्वरूपक्या चिन्तन करते हुए उस महासमुद्रमें शेषशय्यापर शयन करते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12292)
- **Original**: हे मैत्रेय ! इस प्रकवयके होनेमें ब्रह्मारूपधारी भगवान्‌ हरिका दायन करना ही निमित्त है; इसलिये यह नैमित्तिक प्रछय कहत्मता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12293)
- **Original**: जिस समय सर्वात्मा भगवान्‌ विष्णु जागते रहते हैं उस समय सम्पूर्ण संसारकी चेष्टाएँ होती रहती हैं और जिस समय वे अच्युत मायारूपी शय्यापर सो जाते हैं उस समय सैसार भी ल्वीन हो जाता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12294)
- **Original**: जिस प्रकार ब्रह्माजीका दिन एक हजार चतुर्युगका होता है उसी प्रकार संसारके एकार्णवरूप हो जानेपर उनकी रात्रि भी उतनी ही बड़ी होती
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12295)
- **Original**: डइ3ढ आशरीविष्णुपुराण [ आः्4 ततः प्रबुद्धों राज्यन्ते पुनस्सुष्टि करोत्यज: । ब्रह्मस्वरूपधृम्विष्णुर्यथा ते कथित पुरा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12296)
- **Original**: 10 इत्येष कल्पसंहारो5वान्तरप्रयो ट्विज । नैमित्तिकस्ते कथ्चितः प्राकृतं श्रूण्वतः परम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12297)
- **Original**: 11 अनावृष्टबादिसम्पर्कात्कृते संक्षालने मुने। समस्तेष्चेच लोकेषु पातालेघ्ृखिलेषु च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12298)
- **Original**: 12 महदादेविंकारस्थ॒ विशेषान्तस्थ संक्षये । कृष्णेच्छाकारिते तस्मित्रवृत्ते प्रतिसज्ञरे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12299)
- **Original**: 13 आपो असन््ति बै पूर्व भूमेर्गन्‍धात्मक॑ गुणम्‌ । आत्तगश्धा ततो भूमि: प्रछयत्वाय कल्पते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12300)
- **Original**: 14 प्रणष्टे गन्धतन्मात्रे भवत्युवीं जलात्मिका
- **Translation**: 

---

