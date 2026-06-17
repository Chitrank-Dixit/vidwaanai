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

### Verse 1 (Agni Puran 0.3141)
- **Original**: 11--13
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3142)
- **Original**: बभधके: योग्य: प्राणियोंका वध करना-यह चाण्डालका कर्म बताया गया है। स्त्रियोंके उपयोगमें आनेवाली वस्तुओंके निर्माणसे जीविका चलाना तथा स्त्रियोंकी रक्षा करना-यह “वैदेहक' का कार्य है। सूतोंका कार्य है--घोड़ॉंका सारथिपना, *पुक्कस ' व्याध-वृत्तिसे रहते हैं तथा 'मागध' का कार्य है--स्तुति करना, प्रशंसाके गीत गाना। *अयोगव'का कर्म है-रम्जभूमिमें उतरना और शिल्पके द्वारा जीविका चलाना। 'चाण्डाल 'कों गाँवके बाहर रहना और मुर्देसे उतारे हुए बस्त्रको धारण करना चाहिये। चाण्डालकों दूसरे वर्णके लोगोंका स्पर्श नहीं करना चाहिये। ब्राह्मणों तथा गौओंकी रक्षाके लिये प्राण त्यागना अथवा स्त्रियों
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3143)
- **Original**: एवं बालकोंकी रक्षाके लिये देह-त्याग करना
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3144)
- **Original**: गया है। व्रर्णलंकर व्यक्तियोकी जाति उनके बर्ण-बाह्य चाण्डाल आदि जातियोंकी सिद्धिका
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3145)
- **Original**: पिता-माता तथा जातिसिद्ध कर्मोंस जाननी (उनकी आध्यात्मिक उम्नति)-का कारण माना
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3146)
- **Original**: चाहिये
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3147)
- **Original**: 14--18
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3148)
- **Original**: इस प्रकार आदि आस्तेय महापुराणमें 'वर्णानतर-धर्मोका वर्णन” नामक एक साौँ इक्यावनवाँ अभ्याय यूरा हुआ
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3149)
- **Original**: 1514 पुष्कर कहते हैं--परशुरामजी ! ब्राह्मण अपने
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3150)
- **Original**: द्वारा जो पौधोंको नष्ट कर डालते हैं, उससे यज्ञ शास्त्रोक्त कर्मसे ही जीविका चलावे; क्षत्रिय, वैश्य
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3151)
- **Original**: और देवपूजा करके मुक्त होते हैं
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3152)
- **Original**: तथा शुद्रके धर्मसे जीवन-निर्वाह न करें। आपत्तिकालमें
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3153)
- **Original**: आठ बैलॉका हल धर्मानुकूल माना गया है। क्षत्रिय और वैश्यकीं वृत्ति ग्रहण कर ले; किंतु
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3154)
- **Original**: जीविका चलानेवालोंका हल छ: बैलॉंका, निर्दयी शृद्र-वृत्तिसे कभी गुजारा न करे। द्विज खेती,
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3155)
- **Original**: हत्यारोंका हल चार बैलोंका तथा धर्मका नाश व्यापार, गोपालन तथा कुसीद (सूद लेना)--इन
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3156)
- **Original**: करनेवाले मनुष्योॉंका हल दो बैलोंका माना युत्तियोंका अनुष्ठान करे; परंतु वह गोरस, गुड़,
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3157)
- **Original**: गया है। ब्राह्मण ऋत' और अमृतसे' अथवा मृत नमक, लाक्षा और मांस न बेचे। किसान लोग
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3158)
- **Original**: और प्रमृतसे”ं या सत्यानृत॑' वृत्तिसे जीविका धरतीको कोड़ने-जोतनेके द्वारा जो कीड़े और
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3159)
- **Original**: चलाबे। श्वान-वृत्तिसें' कभी जीवन-निर्वाह न चौींटी आदिकी हत्या कर डालते हैं और सोहनीके
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3160)
- **Original**: इस ग्रकार आदि आग्नेय महाएुराणमें 'गृहस्थ-जीविकाका वर्णन” नामक एक साँ बावत्रवाँ अध्याय पूरा हुआ
- **Translation**: 

---

