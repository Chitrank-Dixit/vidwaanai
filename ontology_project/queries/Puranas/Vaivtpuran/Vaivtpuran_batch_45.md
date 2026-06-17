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

### Verse 1 (Vaivtpuran 4.8947)
- **Original**: डर0 + संक्षिप्त ब्रह्मवै््तैपुरोण « (]7]0727]4]4]./.7]]।।।04/।। । ।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8948)
- **Original**: किशोर थी। शरीरकी कान्ति सुन्दर एवं श्याम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8949)
- **Original**: थे। सम्राटोंके समान दस लाख प्रजा उनके साथ थी। वे सोनेका बेंत हाथमें लिये रत्नमय
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8950)
- **Original**: थी। हाथमें बेंत धारण करनेवाले द्वारपाल देवभानुसे आभूषणोंसे विभूषित हो रज्लमय सिंहासनपर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8951)
- **Original**: पूछकर देवतालोग प्रसन्नतापूर्वक आगे बढ़े। सामने विराजमान थे। पाँच लाख गोपोंका समूह उनकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8952)
- **Original**: छठा ट्वार था। उसकी विलक्षण शोभा थी। शोभा बढ़ा रहा था। उनसे पूछकर देवतालोग
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8953)
- **Original**: चित्रोंकी श्रेणियोंसे वह द्वार उद्धासित हो रहा था। तीसरे उत्तम द्वारपर गये, जो दूसरेसे भी अधिक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8954)
- **Original**: उसकी दोनों दीवारें वज़मणि (हीरे)- की बनी थीं सुन्दर, विचित्र तथा मणियोंके तेजसे प्रकाशित
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8955)
- **Original**: और फूलोंकी मालाओंसे सजाबी गयी थीं। उस था। नारद! वहाँ द्वारकी रक्षामें नियुक्त सूर्यभानु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8956)
- **Original**: द्वारपर व्रजराज शक्रभानु नियुक्त थे। देवतालोग नामक द्वारपाल दिखायी दिये, जो दो भुजाओंसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8957)
- **Original**: उनसे मिले। वे नाना प्रकारके अलंकारोंकी शोभासे युक्त, मुरलीधारी, किशोर, श्याम एवं सुन्दर थे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8958)
- **Original**: सम्पन्न थे। उनके साथ दस लाख प्रजाएँ थीं। उनके दोनों गालोंपर दो मणिमय कुण्डल
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8959)
- **Original**: चन्दन-पल्लवसे युक्त उनके कपोल कुण्डलोंकी झलमला रहे थे। रत्रकुण्डलधारी सूर्यभानु श्रीराधा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8960)
- **Original**: प्रभासे उद्धासित थे। उनसे आज्ञा लेकर देवतालोग और श्रीकृष्णके परम प्रिय एवं श्रेष्ठ सेवक थे।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8961)
- **Original**: तुरंत ही सातवें द्वारपर जा पहुँचे। उसमें नाना वे सम्राट्की भाँति नौ लाख गोपोंसे घिरे रहते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8962)
- **Original**: प्रकारके चित्र अद्धित थे। वह पिछले छहों द्वारोंसे थे। उनसे पूछकर देवतालोग चौथे द्वारपर गये,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8963)
- **Original**: अत्यन्त विलक्षण था। वहाँ द्वारपालके पदपर जो उन सभी द्वारोंसे विलक्षण, रमणीय तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8964)
- **Original**: श्रीहरिके परम प्रिय रत्नभानु नियुक्त थे, जिनका मणियोंकी दिव्य दीप्तिसे उद्दी्त दिखायी देता था।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8965)
- **Original**: सारा अद्भ चन्दनसे अभिषिक्त था। वे पुष्पोंकी अद्भुत एवं विचित्र रत्समूहसे जटित होनेके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8966)
- **Original**: मालासे विभूषित थे। मणि-रत्रनिर्मित मनोहर एवं कारण उस द्वारकी मनोहरता और बढ़ गयी थी।
- **Translation**: 

---

