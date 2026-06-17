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

### Verse 1 (Bramha 0.1161)
- **Original**: स्तुतिजप्योपहारेण पूजयापि. विवस्वत: । उपवासेन भकत्या जै सर्वपापै: प्रमुच्यते
- **Translation**: 

---

### Verse 2 (Bramha 0.1162)
- **Original**: प्रणिधाय शिरों भ्रूप्यां नमस्कार कग्रेति यः । तत्क्षणात्सर्वपापेभ्यो मुच्यते नात्र संशय:
- **Translation**: 

---

### Verse 3 (Bramha 0.1163)
- **Original**: अक्तियुक्तों नरो योउसौं रखे: कुर्यात्मरदक्षिणाम्‌
- **Translation**: 

---

### Verse 4 (Bramha 0.1164)
- **Original**: प्रदक्षिणीकृताः तेन. सप्रद्वीपा. बसुंधरा
- **Translation**: 

---

### Verse 5 (Bramha 0.1165)
- **Original**: सूर्य मनसि य: कृत्वा कुर्याद्‌ व्योमप्रदक्षिणाम्‌। प्रदक्षिणोकृतास्तेन सर्पे देवा भवन्ति हि
- **Translation**: 

---

### Verse 6 (Bramha 0.1166)
- **Original**: (29। 17-21)
- **Translation**: 

---

### Verse 7 (Bramha 0.1167)
- **Original**: 60 # संक्षिस ब्रह्मपुराण ही] करके नियम और ब्रतका पालन करते हुए
- **Translation**: 

---

### Verse 8 (Bramha 0.1168)
- **Original**: है। वह कभी तिर्यग्योनिमें नहीं पड़ता। जलते हुए सूर्यदेवका भक्तिपूर्वक पूजन करता है, उसे , दीपकको न कभी चुराये, न नष्ट करे। दीपहर्ता अश्वमेष-यज्ञका फल मिलता है। जो षष्ठी अथवा
- **Translation**: 

---

### Verse 9 (Bramha 0.1169)
- **Original**: मनुष्य बन्धन, नाश, क्रोध एवं तमोमय नरकको ससमीको दिन-रात उपवास करके भगवान्‌ भास्करका
- **Translation**: 

---

### Verse 10 (Bramha 0.1170)
- **Original**: प्राप्त होता हैं। उदयकालमें प्रतिदिन सूर्यकों अर्घ्य पूजन करता है, बह परम गतिको प्राप्त होता है।
- **Translation**: 

---

### Verse 11 (Bramha 0.1171)
- **Original**: देनेसे एक हो वर्षमें सिद्धि प्राप्त होती है। सूर्यके जब शुक्लपक्षकी सप्तमीको रविवार हो, उस
- **Translation**: 

---

### Verse 12 (Bramha 0.1172)
- **Original**: उदयसे लेकर अस्ततक उनकी ओर मुँह करके दिन विजयासप्तमी होती है। उसमें दिया हुआ दान खड़ा हो किसी मन्त्र अथवा स्तोत्रका जप करना महान्‌ फल देनेवाला है। विजयासप्तमीको किया
- **Translation**: 

---

### Verse 13 (Bramha 0.1173)
- **Original**: आदित्यब्रत कहलाता है। यह बड़े-बड़े पातकोंका हुआ सत्रान, दान, तप, होम और उपवास-सब
- **Translation**: 

---

### Verse 14 (Bramha 0.1174)
- **Original**: नाश करनेवाला है। सूर्योदयके समय श्रद्धापूर्वक कुछ बड़े-बड़े पातकोंका नाश करनेवाला है। जो
- **Translation**: 

---

### Verse 15 (Bramha 0.1175)
- **Original**: अर्घ्य देकर सब कुछ साझ्जोपाज़ दान करे। इससे मनुष्य रविवारके दिन श्राद्ध करते और महातेजस्वी
- **Translation**: 

---

### Verse 16 (Bramha 0.1176)
- **Original**: सब पापोंसे छुटकारा मिल जाता है।* अग्नि, जल, सूर्यका यजन करते हैं, उन्हें अभीष्ट फलकी प्राप्ति ' आकाश, पवित्र भूमि, प्रतिमा तथा पिण्डी (प्रतिमाकी होती हैं। जिनके समस्त धार्मिक कार्य सदा
- **Translation**: 

---

### Verse 17 (Bramha 0.1177)
- **Original**: वेदी)-में यत्नपूर्वक सूर्यदेवकों अर्घ्य देना चाहिये+। भगवान्‌ सूर्यके उद्देश्यसे होते हैं, उनके कुलमें
- **Translation**: 

---

### Verse 18 (Bramha 0.1178)
- **Original**: उत्तरायण अथवा दक्षिणायनमें सूर्यदेवका विशेषरूपसे कोई दरिद्र अथवा रोगी नहीं होता। जो सफेद, , पूजन करके मनुष्य सब पापोंसे मुक्त हो जाता है। लाल अथवा पीली मिट्टीसे भगवान्‌ सूर्यके मन्दिरको
- **Translation**: 

---

### Verse 19 (Bramha 0.1179)
- **Original**: इस प्रकार जो मानव प्रत्येक बेलामें अथवा लीपता है, उसे मनोवाब्छित फलकी प्राप्ति होती
- **Translation**: 

---

### Verse 20 (Bramha 0.1180)
- **Original**: कुवेलामें भी भक्तिपूर्वक श्रीसूर्यदेबका पूजन करता है। जो निराहार रहकर भाँति-भाँतिके सुगन्धित
- **Translation**: 

---

