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

### Verse 1 (Vishnu Puran 0.3221)
- **Original**: 20 इत्येवे तव ॒मैत्रेय प्रक्षद्वीप उदाहतः । सद्लेपेण मया भूयः शाल्मलं मे निशामय
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3222)
- **Original**: 21 शाल्मल्स्येश्वरो वीरो वपुष्पांस्तत्सुताज्छृप्पु तेषां तु नामसंज्ञानि सप्तवर्षाणि तानि ये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3223)
- **Original**: 22 श्रेतो&थ हरितश्लैव जीमूतो रोहितस्तथा । बैद्यतो मानसऔब सुप्रभअ महामुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3224)
- **Original**: 23 'बिस्तारद्विगुणेनाथ सर्वतः संवृतः स्थित:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3225)
- **Original**: 24 तत्रापि पर्वता: सप्त विज्ञेया रत्नयोनय: । वर्षाभिव्यज्ञका ये तु तथा सप्त च निप्नगा:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3226)
- **Original**: 25 कुमुदश्नोन्नतक्षेव तृतीयश्च॒ बलाहक: । द्रोणो यत्र महौषध्यः स चतुर्थों महीधर:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3227)
- **Original**: 26 कड्डस्तु पश्चम: षष्ठो महिष: सप्तमस्तथा । ककुगान्पर्वतवर: सरित्रापानि में श्रुणु
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3228)
- **Original**: 27 यह मैंने तुमसे प्रधान-प्रधान पर्वत और नदियॉका वर्णन किया है; वहाँ छोटे-छोटे पर्वत और नदियाँ तो और भी सहसों हैं । उस टेहके हष्ट-पुष्ट व्लेग सदा उन नदियॉका जल पान करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3229)
- **Original**: हे द्विज ! उन ल्मेगोमें हास अधवा वृद्धि नहीं होती और न उन सात वर्षोिं युगको ही कोई अवस्था है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3230)
- **Original**: हे महामते! हे ब्रह्मन्‌! प्रक्षद्रीपसले लेकर दाकद्रीपपर्यन्त छहों द्वीपोमें सदा त्रेतायुगके समान समय रहता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3231)
- **Original**: इन द्वीपेकि मनुष्य सदा नीणोग रहकर पाँच हजार वर्षतक जीते हैं और इनमें वर्णाश्रम-विभागानुसार पाँचों धर्म (अहिंसा, सत्य, अस्तेय, ब्रह्मचर्य और अपरिप्रह) वर्तमान रहते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3232)
- **Original**: यहाँ जो चार वर्ण है वह मैं तुमको सुनाता हूँ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3233)
- **Original**: हे मुनिसत्तम ! उस द्वीपमें जो आर्यक, कुरर, लिदिइय और भावी नामक जातियाँ हैं; वे ही क्रमसे ब्राह्मण, क्षत्रिय, खैद्य और णूद्र हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3234)
- **Original**: हे ट्विजोत्तम ! उसीमें जम्बूवृक्षके हो परिमाणवाला एक प्नक्ष (पाकर) का वृक्ष है, जिसके नामसे उसकी संज्ञा हक्षद्वीप हुई है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3235)
- **Original**: यहाँ आर्यकादि वर्णोंद्रार जगत्ल्नष्टा, सर्वरूप, सर्वेश्वर भगवान्‌ हरिका सोमरूपसे यजन किया जाता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3236)
- **Original**: प्रक्षद्वीप अपने ही खराबर परिमाणवाले कत्ताकार इक्षुरसके समुद्रसे घिय हुआ है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3237)
- **Original**: हे मैत्रेथ ! इस प्रकार मैंने तुमसे संक्षेपमें प्रक्षद्वीपका जर्णन किया, अब तुम शाल्मकूद्वीपका विवरण सुनो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3238)
- **Original**: शाल्मलट्टीपके स्वामी वीरबर बपुष्मान्‌ थे । उनके पुत्रोंके नाम सुनो--हे महामुने ! वे श्वेत, हरित, जीमूत, रोहित, कैययुत, मानस और सुप्रभ थे। उनके सात वर्ष उन्हींके नामानुसार संज्ञावाले हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3239)
- **Original**: यह (प्नक्षद्रीपको चेरनेवाला) इश्षुरसका समुद्र अपनेसे दूने विस्तारवाले इस शाल्मलड्ीपसे चारों ओरसे घिरा हुआ है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3240)
- **Original**: वहाँ भी रल्रेकि उद्भवस्थानरूप सात पर्वत हैं, जो उसके सातों क्योकि विभाजक ऐ तथा सात नदियाँ है
- **Translation**: 

---

