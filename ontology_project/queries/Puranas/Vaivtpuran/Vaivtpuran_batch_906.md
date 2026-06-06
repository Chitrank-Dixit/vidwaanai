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

### Verse 1 (Vaivtpuran 543.16434)
- **Original**: आँगनोंका विस्तार कितना होना चाहिये? किस उज्वल, परिष्कृत, श्रेत चम्पकके सदृश कान्तिमती,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16435)
- **Original**: दिशामें पुष्पोद्यान मद्गलप्रद होता है? सुरेधर! तपाये हुए स्वर्णकी-सी चमकौली, स्वर्णके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16436)
- **Original**: परको्ों, खाइयों, दरवाजों, गृहों और चहारदीबारियोंका मूल्यसे सौगुनी अधिक मूल्यवाली, थोड़ी-थोड़ी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16437)
- **Original**: क्या प्रमाण है? प्रभो! शिविर-निर्माणमें किस- लाल, परम सुन्दर, वजनदार, सर्वोत्तम और पूजनीय
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16438)
- **Original**: किस वृक्षकी लकड़ी प्रशस्त मानी गयी है और उत्तम मणियोंद्वारा वास्तु-शास्त्रके विधानानुसार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16439)
- **Original**: किन वृशक्षोंके कापष्ठ अमज्जलजनक होते हैं? यह यथायोग्य घटा-बढ़ाकर एक ऐसे मनोवाउ्छित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16440)
- **Original**: सब मुझे बतलानेकी कृपा कीजिये। परम मनोहर नगरकी रचना करो, जो सौ योजनके श्रीभगवानने कहा--देवशिल्पिन्‌! गृहस्थोंके विस्तारवाला हो। जबतक तुम नगरका निर्माण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16441)
- **Original**: आश्रममें नारियलका वृक्ष धन प्रदान करनेवाला करोगे, तबतक यक्षणण हिमालयसे रात-दिन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16442)
- **Original**: होता है। वही वृक्ष यदि शिविरके ईशानकोण मणियोंको लाते रहेंगे। कुबेरकी प्रेरणासे आये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16443)
- **Original**: अथवा पूर्व दिशामें हो तो पुत्रप्रद होता है। बह हुए सात लाख यक्ष, शंकरद्वारा भेजे हुए एक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16444)
- **Original**: मनोहर वृक्षराज सर्वत्र मड्गलका दाता होता है। लाख बेताल और एक लाख कृष्माण्ड तथा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16445)
- **Original**: यदि पूर्व दिशामें आमका वृक्ष हो तो वह गिरिराजनन्दिनीद्वारा नियुक्त किये हुए दानब और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16446)
- **Original**: मनुष्योंको सम्पत्ति प्रदान करता है और सर्वत्र ब्रह्मराक्षस तुम्हारे सहायक बने रहेंगे। मेरी सोलह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16447)
- **Original**: शुभदायक होता है। बेल, कटहल, जम्बीरी नीबू हजार एक सौं आठ पत्नियोंके लिये ऐसे दिव्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16448)
- **Original**: तथा बेरके वृक्ष पूर्व दिशामें संतानदायक, दक्षिणमें शिविर तैयार करो, जो खाइयोंसे युक्त तथा ऊँची- धनदाता तथा सर्वत्र सम्पत्तिप्रद होते हैं। इनसे ऊँचो चहारदीवारियोंसे परिवेष्टित हों। जिनमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16449)
- **Original**: गृहस्थकी उन्नति होती है। जामुन, अनार, केला प्रत्येकमें बारह कमरे और सिंहद्वार लगे हों, जो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16450)
- **Original**: तथा आमलाके वृक्ष पूर्वमें बन्धुप्रद तथा दक्षिणमें चित्र-बिचित्र कृत्रिम किवाड़ोंसे युक्त हों; निषिद्ध
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16451)
- **Original**: मित्रकी वृद्धि करनेवाले होते हैं और सर्वत्र वृक्षोंसे रहित और प्रसिद्ध वृक्षोंसे सम्पन्न हों और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16452)
- **Original**: शुभदायक होते हैं। सुवाक दक्षिणमें धन-पुत्र- जिनके आँगन शुभ लक्षणयुक्त और चन्द्रबेध हों।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16453)
- **Original**: शुभप्रद, पश्चिममें हर्षदायक और ईशानकोणमें इसी प्रकार यदुवंशियों और नौकरोंके लिये भी
- **Translation**: 

---

