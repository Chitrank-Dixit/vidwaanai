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

### Verse 1 (Vishnu Puran 0.661)
- **Original**: उसका अति प्रचण्ड शरीर आधा नर और आधा तारीरूप था। तब कऋक्काजी 'अपने शरेरका विभाग कर' ऐसा कहकर अन्तर्घान हो गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.662)
- **Original**: ऐसा कहे जानेपर ठस रुद्रने अपने शरीरस्थ स््री और पुरुष दोनो भागोंकों अलग-अलग कर दिया और फिर पुरुष-भागक्तो स्यारह भागोंमें विभक्त किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.663)
- **Original**: तथा ख्वी-भागक्तरे भी सौम्य, क्रूर, शान्त-अद्वान्‍त और ह्याम-गौर आदि कई रूपों विभक्त कर दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.664)
- **Original**: तदनत्तर, हे द्विज ! अपनेसे उत्पन्न अपने ही स्वरूप स्वायम्भुबको ब्रह्माजीने प्रजा-पालनके लिये प्रथम पमर्नुँ खनाया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.665)
- **Original**: उन स्वायस्पुव मनुने' [अपने ही साथ उत्पन्न हुई] तपके कारण निष्पाप शतरूपा नामको ख्रीको अपनो पत्नीरूपसे ग्रहण किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.666)
- **Original**: हे धर्मज्ञ ! उन स्वायप्थुव. मनुसे झतरूपा देलीने प्रियत्रत और उत्तानपादनामक दो पुत्र तथा उदार, रूप और गुणोंसे सम्पन्न प्रसूति और आकृति नामकी दो कन्याएँ उत्पन्न की
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.667)
- **Original**: उनमेंसे प्रसृतिको दक्षके साथ तथा आकूतिको रूचि अजापतिके साथ विवाह दिया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.668)
- **Original**: है महाभाग ! रूचि प्रजापतिने उसे ग्रहण कर लिया । तर उन दम्पतीके यज्ञ और दक्षिणा--ये युगल (जुड़वाँ) सन्तान उत्पन्न हुई
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.669)
- **Original**: यज्ञके दक्षिणासे बारह पूत्र- हुए, जो स्वायग्भुव मन्वन्तरमें याम नामके देवता कहल्लाये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.670)
- **Original**: तथा दक्षने प्रसुतिसे चौबीस कन्याएँ उत्पन्न कीं। मुझसे उनके शुभ नाम सुनो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.671)
- **Original**: श्रद्धा, लद्ष्मी, घृति, तुष्टि, मेघा, पुष्टि, क्रिया, बुद्धि, झाूज्णा, वपु, शान्ति, सिद्धि और तेरहवों कीर्ति---इन दक्ष-कन्याओंका धर्मने पत्रौरूपसे पहण किया। इनसे छोटी श्ोष स्थारह कन्याएँ, ख्याति, सती, सम्मूति, स्मृति, प्रीति, क्षमा, सन्तति, अनसूया, ऊर्जा, स्वाहा और स्वधा थीं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.672)
- **Original**: 23--25
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.673)
- **Original**: हे मुनिसत्तम ! इन ख्याति आदि कन्याओंको क्रमशः भृगु, शिव, मरीचि, अगिय, पुलस्त्य,
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.674)
- **Original**: अ07 ] अभश्रिर्वसिष्ठो वहिश्न पितरश्न यथाक्रमम्‌। ख्यात्याद्या जगृहु: कन्या मुनयो मुनिसत्तम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.675)
- **Original**: 27 श्रद्धा कार्म चला दर्प नियर्म ध्रूतिरात्मजम्‌ । सन्‍्तोष॑ च्र॒ तथा तुष्टिलॉर्भ पुष्टिससूयत
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.676)
- **Original**: 28 मेथा श्रुर्त क्रिया दण्ड नयं विनयमेव थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.677)
- **Original**: 29 बोध बुद्धिस्तथा रूज़जा विनय वपुरात्मजम्‌ व्यवसाय प्रजज्ञे वै क्षेम॑ शान्तिरसूयत
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.678)
- **Original**: 30 कामाद्रति: सुते हर्ष धर्मपौज्रमसूयत
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.679)
- **Original**: 31 हिंसा भार्या त्वधर्मस्य ततो जज्ञे तथानृतम्‌ । कन्या च्ञ निकृतिस्ताभ्यां भय नरकमेव च॑
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.680)
- **Original**: 32 माया च॒ लेदना चैव मिथुन त्विदमेतयो: । तयोर्जज्ञे5थ सै माया मृत्युं भूतापहारिणम्‌
- **Translation**: 

---

