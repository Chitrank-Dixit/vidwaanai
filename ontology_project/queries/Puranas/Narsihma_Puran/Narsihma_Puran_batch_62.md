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

### Verse 1 (Narsihma Puran 0.1221)
- **Original**: 36 मनुः सप्तर्षयों देवा भूषालाश्ष मनोः सुताः। मन्वन्तरे भवन्‍त्येते शक्राश्नैवाधिकारिण:
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.1222)
- **Original**: 37 चतुर्दशभिरेतैस्तु गतैर्मन्वन्तद्विज। सहस्त्रयुगपर्यन्तः कालो गच्छति बासरः
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.1223)
- **Original**: 38 तावत्यमाणा चर निशा ततो भवति सत्तम। ब्रह्मरूपधर: शेते सर्वात्मा नृहरि: स्वयम्‌
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.1224)
- **Original**: 39 प्रैलोक्चमखिलं ग्रस्ता भगबानादिकृद्धिभु:। स्वमायामास्थितो विप्र सर्वरूपी जनार्दन
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.1225)
- **Original**: 40 अथ प्रबुद्धो भगवान्‌ यथा पूर्व तथा पुनः। युगव्यवस्थां कुरुते सुष्टिं चर पुरुषोत्तम:
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.1226)
- **Original**: 49 एते तबोक्ता मनवोउपराश्च पुत्राश् भूषा सुतयक्ष सर्वे। विभूतयस्तस्य स्थितौ स्थितस्य चौदह मन्वन्तरॉँका और उन-उन मनुके पुत्र तत्कालीत राजाओंका वर्णन किया, जिनके द्वारा इस वसुधाका पालन होता है।
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.1227)
- **Original**: # 17-36
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.1228)
- **Original**: प्रत्येक मन्वन्तरमें मनु, सप्तषिं, देवता और भूपाल मनुपुत्न तथा इन्द्र-ये अधिकारी होते हैं। ब्रह्मनू ! इन चौदह मन्वन्तरोंके व्यतीत हो जानेपर एक हजार चतुर्युगका समय बीत जाता है। यह ( ऋऋद्माजोका) एक दिन कहलाता हैं। साधुशिरोमणे! फिर उतने हो प्रमाणकी उनकी रात्रि होती है। उस समय सब भूतोंके आत्मा साक्षात्‌ भगवान्‌ नृसिंह ब्रह्मरूप धारण करके शयन करते हैं। विप्रवर! सर्वत्र व्यापक एवं आदिविधाता सर्वरूप भगवान्‌ जनार्दन उस समय समस्त त्रिभुवनकों अपनेमें लीन करके अपनो योगमायाका आश्रय ले शयन करते हैं। फिर जाग्रत्‌ होनेपर वे भगवान्‌ पुरुषोत्तम पूर्वकल्पके अनुसार पुनः युग-व्यवस्था तथा सृष्टि करते हैं। ब्रह्मन्‌! इस प्रकार मैंने मनु, देवगण , धूपाल, मनुपुत्र और ऋषि-इन सबका आपसे वर्णन किया। आप इन सबको पालनकर्ता भगवान्‌ तस्थैब॒ सर्व॑त्वमवेहि बिप्र
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.1229)
- **Original**: बिष्णुकी विभूतियाँ ही समझें
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.1230)
- **Original**: 37--42
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.1231)
- **Original**: इति ऑफासिंहएएणे अयोकिशो: ध्याय: #
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.1232)
- **Original**: 23 # इस प्रकार क#वक्सिएएएणमें चाँद सन्‍्वनारॉका कर्षात ' नायक तेईसर्जों अध्याय यूरो हुआ
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.1233)
- **Original**: #उ0+++ डे 4723-90
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.1234)
- **Original**: अध्याय 24]... सूर्य॑र्यश--राजा इक्ष्याकुका भगवल्येम; उनका भगयदर्शनके हेतु तपस्याके लिये प्रस्थान मना 3 3, 3 >> ऋ्‌[]छ]'णएणएाशाआए*<2<:22>2> रा भु;+8+& एन ्‌े् िअअइअइअकातए 73 सूर्यबंश--राजा इक्ष्वाकुका भगवत्प्रे; उनका भगबइर्शनके हेतु तपस्थाके लिये प्रस्थान #यूह उकाच अत: परं प्रवक्ष्यामि वंशानुचरितं शुभम्‌। श्रुण्वतामपि पापघ्न॑ सूर्यसोमनृपात्मकम्‌
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.1235)
- **Original**: 91 सूर्यबंशोद्धवो यो बै मनुपुत्रः पुरोदितः। इक्ष्वाकुर्नाम भूपालक्षरितं तस्य में श्रृणु
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.1236)
- **Original**: 2 आसीद्‌ भूमौ महाभाग पुरी दिव्या सुशोभना। सरयूतीरमासाद्य अयोध्या नाम नामत:
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.1237)
- **Original**: 3 अमराक्त्यतिशया.. त्रिंशद्योजनजालिनी। हस्त्यश्वरथपत्त्योपैर्ट्रमै: कल्पद्ुमप्रभे:
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.1238)
- **Original**: 4 प्राकाराइप्रतोलीभिस्तोरण:. काछनप्रभे:। विराजमाना सर्वत्र सुविभक्तचतुष्पथा
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.1239)
- **Original**: 5 अनेकभूमिप्रासादा बहुभाण्डसुविक्या। पद्मोत्पलशुभैस्तोयैवांपीभिरुपशोभिता_
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.1240)
- **Original**: 6 देवतायतनैर्दिन्यर्वेदघोषै श्र शोभिता। वीणावेणुमृदड्रैंआ. शब्दैरुत्कृष्कैर्युता
- **Translation**: 

---

