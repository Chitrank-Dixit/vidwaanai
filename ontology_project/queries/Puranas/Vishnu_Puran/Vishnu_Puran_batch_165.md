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

### Verse 1 (Vishnu Puran 0.3281)
- **Original**: 52 पुष्करा: पुष्कला धन्यास्तिष्यास्याश्ष महामुने । ब्राह्मणा: क्षत्रिया वैश्या: शुद्राश्चानुक्रमोदिता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3282)
- **Original**: 53 नदीमैत्रेय ते तत्र या: पिबन्ति शृणुत्न ताः । सप्तप्रधानाः शतझस्तत्नान्या: क्षुद्रनिश्नगा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3283)
- **Original**: 54 गौरी कुमुद्ती चैत्र सन्ध्या रात्रिमनोजबा । क्षान्तिश्ष पुण्डीका च सप्तैता वर्षनिम्नगा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3284)
- **Original**: 55 ततन्नापि विष्णुर्भगवान्युष्कराद्यैर्जनार्दन: । यागै रुत्स्वरूपश्च॒इज्यते यज्ञसब्निधो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3285)
- **Original**: 56 क्रोकद्वीप: समुद्रेण दधिमण्डोदकेन च। आवृत: सर्वतः क्रोझलद्वीपतुल्येन मानत:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3286)
- **Original**: 57 द्धिमण्डोदकआपि शाकट्ठीपेन संयृतः । द्वितीय अंश 117 हरनेवाल्मी हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3287)
- **Original**: बहाँ और भी सहस्नों छोटी-छोटी नदियाँ और पर्वत हैं। कुझद्रीपमें एक कुशका झाड़ है । उसीके कारण इसका यह नाम पड़ा है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3288)
- **Original**: यह द्वीप अपने ही बराबर विस्तारवाले घीके समुद्रसे घिरा हुआ है और वह घृत-समुद्र क्रौद्वीपसे परिवेष्टित है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3289)
- **Original**: है महाभाग ! अब इसके अगले क्रौशनामक महाद्वीपके विषयमें सुनो, जिसका विस्तार कुदाद्वीपसे दूना है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3290)
- **Original**: क्रौक्तद्वीपमें महात्मा चुतिमानके जो पुत्र थे; उनके नामानुसार ही महाराज चुतिमानने उनके वर्षकि नाम रखे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3291)
- **Original**: है मुने ! उसके कुशल, मन्दग, उष्ण, पोजर अन्धकारक, मुनि और दुलदुभि--ये सात पुत्र थे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3292)
- **Original**: वह्चाँ भी देवता और गन्श्रवॉसे सेलित अति मनोहर स्रात वर्षपर्वत हैं। हे महाबुद्धे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3293)
- **Original**: उनके नाम सुनो--
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3294)
- **Original**: डनमें पहल्त्र ऋैज्ञ, दूसरा वामन, तीसरा आन्चकास्क, चौथा घोड़ीके मुख्के समान रल्मय स्वाहिनी पर्वत पाँचवाँ दिवावृतू, उठा पुण्डरीकयान्‌ू और सातबाँ महापर्वत दुन्दुभि है। ये द्वीप परस्पर एक-दूसरेसे दूने हैं; और उन्‍्होंकी भाँति उनके पर्वत भी [उत्तरोत्तर द्विगुण] हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3295)
- **Original**: इन सुरम्य बर्षों और पर्जतश्रेष्ठों में देवगणोंके सहित सम्पूर्ण प्रजा निर्भय होकर रहती है।। 52
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3296)
- **Original**: है महामुने ! यहाँके ब्राह्मण, क्षत्रिय, खैइय और श॒द्र क्रमसे पुष्कर, पुष्कछ, धन्य और तिष्य कहल्लाते है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3297)
- **Original**: है चैत्रेय ! वहाँ जिनका जल पान किया जाता है उन नदियोंका खिवरण सुनो । उस ड्रीपमें सात प्रधान तथा अन्य सैकड़ों क्षुद्र नदियाँ हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3298)
- **Original**: बे सात बर्षनदियाँ गौरी, कुमुद्गबती, सम्ध्या, रात्रि, मनोजवा, क्षान्ति और पुण्डरीका हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3299)
- **Original**: वहाँ भी रुद्ररूपी जनार्दन भगवान्‌ विष्णुकी पुष्करादि वर्णाद्गारा यज्नादिसि पूजा की जाती है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3300)
- **Original**: यह क्रौकृद्वीप चारों ओरसे अपने तुल्य परिमाणवाले दर्घिमण्ड (मट्ठे) के समुद्रसे घिरा हुआ है
- **Translation**: 

---

