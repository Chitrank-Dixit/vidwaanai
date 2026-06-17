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

### Verse 1 (Vaivtpuran 16.3414)
- **Original**: रथियोंमें श्रेष्ठ हो। राजा शद्बचूड़ने उस महारथीको एवं हीरे भी अपने गुरुदेव ब्राह्मणकी सेवामें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3415)
- **Original**: अगणित अक्षौहिणी सेनापर अधिकार प्रदान कर समर्पित किये। वह अपने कल्याणार्थ श्रेष्ठ हाथी,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3416)
- **Original**: दिया। उस सेनाध्यक्षमें ऐसी योग्यता थी कि स्वयं घोड़े और सर्वोत्तम सुन्दर धन दरिद्र ब्राह्मणोंकों
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3417)
- **Original**: तीस अक्षौहिणी सेनासे अपनी सेनाको बचा खुले हाथों बाँटने लगा। उस समय हजारों [सकता था। तत्पश्चात्‌ शब्बुचूड़ मन-ही-मन बस्तुपूर्ण भवन, लाखों नगर तथा असंख्य गाँव
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3418)
- **Original**: भगवान्‌ श्रीकृष्णका स्मरण करता हुआ बाहर शह्लुचूड़ने दानरूपमें ब्राह्मणोंको दिये। इसके बाद
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3419)
- **Original**: निकला। उत्तम रत्रोंसे बने हुए विमानपर सवार उसने अपने पुत्रकों सम्पूर्ण दानवोंका राजा हुआ और गुरुबरोंकों आगे करके भगवान्‌ बनाकर उसे अपनी प्रेयसी पत्नी, राज्य, सम्पूर्ण शंकरकों सेवामें चल दिया।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3420)
- **Original**: *प्रकृतिखण्ड « 155 3555%$55 54 $%%4% $$$ 54 $ 4 $ 45 5 % 4555 # 4 $4 $5$$ 555 45 4 4 54% $ 5 4 85% ## 5544 44854 4 £ 5554 5 & नारद! पुष्पभद्रा (या चन्द्रभागा) नदीके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3421)
- **Original**: शीघ्र प्रसन्न होते हैं। उनके मुखपर कभी उदासी तटपर एक सुन्दर अक्षयवर है। वहीं सिद्धोंक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3422)
- **Original**: नहीं आती। वे भक्तोंपर अनुग्रह करनेवाले हैं। बहुत-से आश्रम हैं। उस स्थानको सिद्धक्षेत्र कहा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3423)
- **Original**: उन्हें विश्वनाथ, विश्वबीज, विश्वरूप, विश्वज, गया है। यह पवित्र स्थान भारतवर्षमें है। इसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3424)
- **Original**: विश्वम्भर, विश्ववर और विश्वसंहारक कहा जाता कपिलमुनिकी तपोभूमि कहते हैं। यह पश्चिमी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3425)
- **Original**: है। वे कारणोंके कारण तथा नरकसे उद्धार समुद्रसे पूर्व तथा मलयपर्वतसे पश्चिममें है,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3426)
- **Original**: करनेमें परम कुशल हैं। वे सनातन प्रभु ज्ञान श्रीशैलपर्वतसे उत्तर तथा गन्धमादनसे दक्षिण
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3427)
- **Original**: प्रदान करनेवाले, ज्ञानके बीज तथा ज्ञानानन्द हैं। भागमें है। इसकी चौड़ाई पाँच योजन है और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3428)
- **Original**: दानवराज शह्लुचूड़ने विमानसे उतरकर उनके लम्बाई पाँच सौ योजन। वहाँ भारतवर्षमें एक पुण्यप्रदा नदी बहती है। उसका जल स्वच्छ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3429)
- **Original**: 5 स्फटिकमणिके समान उद्धासित होता है। वह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3430)
- **Original**: 3 जलसे कभी खाली नहीं होती। उसे पुष्पभद्रा [54 4) 4 कहते हैं। बह नदी समुद्रकी पत्नीरूपसे विराजमान होकर सदा सौभाग्यवती बनी रहती है। बह शुद्ध स्फटिकके समान निर्मल जलसे पूर्ण है। उसका उद्म-स्थान हिमालय है। कुछ दूर आगे आनेपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3431)
- **Original**: ---- - 5 शरावती नामकी नदी उसमें मिल गयी है। वह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3432)
- **Original**: दर्शन किये और सबके साथ सिर झुकाकर उन गोमन्तपर्वतको बायें करके बहती हुई पश्चिम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3433)
- **Original**: भगवान्‌ शंकरेकों भक्तिपूर्वक प्रणाम किया। उस समुद्रकी ओर प्रस्थान करती है। वहाँ पहुँचकर
- **Translation**: 

---

