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

### Verse 1 (Vishnu Puran 0.5441)
- **Original**: 71 तुतीय अंश 1957 आँगनमें रहे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5442)
- **Original**: यदि अतिथि आ जाय तो उसका स्वागतादिसे तथा आसन देकर और चरण धोकर सत्कार करें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5443)
- **Original**: फिर श्रद्धापूर्वक भोजन कराकर मधुर वाणीसे प्रश्रोत्तर करके तथा उसके जानेके समय पीछे-पीछे जाकर उसको प्रसन्न करे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5444)
- **Original**: जिसके कुल और नामका कोई पता न हो तथा अन्य देशसे आया हो उसी अतिथिका सत्कार करे, अपने हो गाँवमें रहनेवाले पुरुषकी अतिधिरूपसे पूजा करनी उचित नहीं है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5445)
- **Original**: जिसके पास कोई सामग्री न हो, जिससे कोई सम्बन्ध न हो, जिसके कुल-शीसूका कोई पता न हो और जो भोजन करना चाहता हो उस अतिधिका सल्कार किये बिना भोजन करनेसे मनुष्य अधोगतिक्ओ प्राप्त होता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5446)
- **Original**: गृहस्थ पुरुषको चाहिये कि आये हुए अतिधिके अध्ययन, गोत्र, आचरण और कुछ आदिके विषयमें कुछ भी न पूछकर हिरण्यगर्थ-बुद्धिसे उसकी पूजा करे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5447)
- **Original**: हे नृप ! अतिथि-सत्कारके अयन्तर अपने ही देशके एक और पास्यज्षिक ब्राहणको जिस्रके आचार और कुछ आदिका ज्ञान हो पितृणणके लिये भोजन करावे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5448)
- **Original**: है भूपाछ ! [ मनुष्ययज्ञकी विधिसे “मनुष्पेभ्यो हन्त' इत्यादि मन्‍्लोचारणपूर्वक ] पहले ही निकालकर अलग रखे हुए हन्तकार नामक अन्नसे उस श्रोत्रिय ब्राह्मणको भोजन कराये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5449)
- **Original**: इस प्रकार [देवता, अतिथि और ब्राह्मणको] ये तीन भिक्षाएँ, देकर, यदि सामर्थ्य हो तो परित्राजक और बह्यचारियोंको भो बिना ल्कैराये हुए इच्छानुसार भिक्षा दे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5450)
- **Original**: तीन पहले तथा धिक्षुगण--ये चारों अतिथि कहलाते हैं। हे राजन्‌ ! इन चार्णोका पूजन करनेसे मनुष्य समस्त पापोंसे मुक्त हो जाता है।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5451)
- **Original**: जिसके घरसे अतिथि निराश होकर लौट जाता है उसे वह अपने पाप देकर उसके झुभक्मोंकों छे जाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5452)
- **Original**: हे नरेश्र ! धाता, प्रजापति, इच्ध, अग्नि, बसुगण और अर्यमा--ये समस्त देवगण अतिथियमें प्रविष्ट होकर अन्न भोजन करते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5453)
- **Original**: अतः मनुष्यको अतिथि-पूजाके लिये निरन्तर प्रयत्न करना चाहिये। जो पुरुष अतिथिके बिना भोजन करता है वह तो केवल पाप ही भोग करता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5454)
- **Original**: तदनन्तर गृहरुथ पुरुष पितृगृहमें रहुनेवाल्णी विवाहिता सरीसूपा यानगक्ष॒पद्ावों मृगपक्षिण: । तिर्यक् इति कध्यन्ते पह्षैताः प्राणिजातयः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5455)
- **Original**: अर्थ--स्रिद्ध, गृछाक, गय्धर्थ. यक्ष, ग्क्षस, सर्प, विद्याधर और पिशाय--ये आठ देखयोनियाँ मानों गयी हैं तथा सरीसृप, वानर, पशु, मृग, (जालों प्राणों) और पश्षौ--ये पाँच तिर्यग्‌ योनियाँ कही गयी हैं।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5456)
- **Original**: 196 श्ीविष्णुपुराण [ आ* 11 अभुक्तवत्सु चैतेपु भुझन्पुद्क्ते स दुष्कृतम्‌। मृतञ्ञ गत्वा नरक॑ इलेष्मभुग्जायते नर:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5457)
- **Original**: 72 अज्लाताशी पलं भुड्कक्ते हाजपी पूयशोणितम्‌। असंस्कृतात्रभुड्मृत्र॑ बालादिप्रथर्म शकृत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5458)
- **Original**: 73 अहोमी च कृमीन्भुड्क्ते अदत्त्वा विषमश्चुते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5459)
- **Original**: 74 तस्माच्छृणुष्न॒ राजेन्र यथा भुझ्लीत वे गृही । भुक्लतशक्ष यथा पुंस: पापबन्धो न जायते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5460)
- **Original**: 75 इह चारोग्यविपु्लं बलबुद्धिस्तथा नृप। भवत्यरिष्टशान्तिश्र॒ वैरिपक्षाभिचारिका
- **Translation**: 

---

