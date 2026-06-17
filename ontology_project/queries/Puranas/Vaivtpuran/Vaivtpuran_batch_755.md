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

### Verse 1 (Vaivtpuran 543.13414)
- **Original**: पालन करने लगे; उन्होंने भृगुजीको पुरोहित चैत्रबंशी राजा सुरथके नामसे प्रसिद्ध थे। नवें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13415)
- **Original**: बनाकर सौ यज्ञोंका अनुष्ठान किया; परंतु इन्द्रपदको मनुका नाम दक्षसावर्णि और दसवेंका ब्रह्मसावर्णि
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13416)
- **Original**: नश्वर और अत्यन्त तुच्छ मानकर उन्होंने उसे ग्रहण है। ग्यारहवें श्रेष्ठ मनुको धर्मसावर्णि कहते हैं।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13417)
- **Original**: नहीं किया। उन शुद्धबुद्धिवाले नरेशने अपने तत्पश्चात्‌ रुद्रसावर्णिका मन्वन्तर आता है। रुद्रसावर्णि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13418)
- **Original**: प्रज्बलित तेजसे इन्द्र, बलि तथा समस्त दानवेन्द्रोंको भगवान्‌ शिवके भक्त और जितेन्द्रिय थे। उनके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13419)
- **Original**: लीलापूर्वक जीत लिया। बाद क्रमश: देवसावर्णि और इन्द्रसावर्णि तेरहवें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13420)
- **Original**: ।. हिमालय ! उन महाराजके सौ पुत्र और एक तथा चौदहवें मन्वन्तरोंके अधिकारी हुए हैं।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13421)
- **Original**: सुन्दरी कन्या हुई, जो लक्ष्मीके समान लावण्यमयी भैया! इस प्रकार मैंने तुम्हें चौदह मनुओंका थी। उसका नाम पद्मा रखा गया था। वह पिताके परिचय दिया। इन सबके व्यतीत हो जानेपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13422)
- **Original**: घरमें रहकर धीरे-धीरे युवावस्थामें प्रविष्ट हुई। ब्रह्माजीका एक दिन पूरा होता है। अब तुम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13423)
- **Original**: तब महाराजने वरकौ खोजके लिये दूत भेजा। इन्द्रसावर्णिका सारा वृत्तान्त मुझसे सुनों। एक दिन अपने आश्रमको जानेके लिये उत्सुक इन्द्रसावर्णि सब मनुओमें श्रेष्ठ, धर्मात्मा तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13424)
- **Original**: हुए पिप्पलाद मुनिने तपस्याके निर्जन स्थानमें एक गदाधारी भगवान्‌ विष्णुके अनन्य भक्त थे। उन्होंने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13425)
- **Original**: गन्धर्वको देखा, जो स्त्रियोंसे घिरा था। उसका इकहत्तर युगोंतक धर्मपूर्वक राज्य किया। इसके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13426)
- **Original**: चित्त श्रृड्राररसके समुद्रमें डूबा हुआ था। कामसे बाद वे अपने पुत्र सुरेन्द्रको राज्य देकर तपस्याके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13427)
- **Original**: अत्यन्त मतवाले हुए उस गन्धर्वको दिन-रातका लिये बनमें चले गये। सुरेन्द्रका पुत्र महाबली भान नहीं होता था। उसे देखकर मुनिवर श्रीमान्‌ श्रीनिकेत हुआ। उसका पुत्र महायोगी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13428)
- **Original**: पिप्पलादके मनमें कामभावका उदय हुआ। पुरीषतर और उसका पुत्र अत्यन्त तेजस्वी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13429)
- **Original**: उनका चित्त तपस्यासे विचलित हो गया और गोकामुख हुआ। गोकामुखके वृद्धश्रवा, वृद्धश्नवाके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13430)
- **Original**: वे पत्नी-प्राप्तिका उपाव सोचने लगे। एक दिन भानु, भानुके पुण्डरीक, पुण्डरीकके जिहल,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13431)
- **Original**: पुष्पभद्रा नदीमें स््नानके लिये जाते हुए मुनीश्चर जिहलके थ्रृज्जी, श्रृज्ीक भीम और भीमके पुत्र
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13432)
- **Original**: पिप्पलादने युवती पद्माकों देखा, जो पद्मा यशश्चन्द्र हुए; जिन्होंने अपने यशसे चन्द्रमाकों [(लक्ष्मी)-के समान मनोरम जान पड़ती थी। जीत लिया था। संतपुरुष तथा देवतालोग सदा ही
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13433)
- **Original**: मुनिने आसपास खड़े हुए लोगोंसे पूछा--'यह उनकी निर्मल कीर्तिका गान करते हैं। उनका पुत्र
- **Translation**: 

---

