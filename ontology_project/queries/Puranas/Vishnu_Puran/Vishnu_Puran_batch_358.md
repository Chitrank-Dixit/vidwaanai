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

### Verse 1 (Vishnu Puran 0.7141)
- **Original**: 28--30
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7142)
- **Original**: त्तदनन्तर पितामह श्रीज्रह्माजीने उस बालककों गेककर तारासे स्वये हो पूछा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7143)
- **Original**: “बेटी ! ठीक-ठीक बता यह पुत्र किसका है--बृहस्पतिका या चन्द्रमाका ?'' इसपर उसने लज्जापूर्वक कहा, 'चन्द्रमाक्रा''
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7144)
- **Original**: तब्न तो नक्षत्रपति भगवान्‌ चन्द्रने उस बालकको हृदयसे लगाकर कहा--''बहुत ठीक, बहुत ठीक, बेटा ! ठुम बड़े बुद्धिमान हो;'” और उनका नाम “बुध' रख दिया । इस समय उनके निर्मल कपोल्त्रेंकी कान्ति ठच्छूवसित और देदीप्यमान हो रही थी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7145)
- **Original**: 256 श्रीविष्णुपुराण ([ अ0 6 तदाख्यातमेबेतत्‌ स॒ च यथेलायामात्मजं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7146)
- **Original**: _ बुधने जिस प्रकार इत््रसे अपने पुत्र पुरूसवाकों उत्पन्न पुरूरवसमुत्पादयामास
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7147)
- **Original**: पुरूरवास्त्वति- दानझीलो5तियज्वातितेजस्वी । ये सत्यवादिन- मतिरूपवन्ते मनस्विन॑ सित्रावरुणशापान्मानुषे लोके मया वस्तव्यमिति कृतमतिरुवशी ददर्श
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7148)
- **Original**: भूत्वा तमेबोपतस्थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7149)
- **Original**: सो5उपि च तामति- शयितसकलल्लेकस्त्रीकान्तिसोकुमार्यलावण्य- गतिबिलासहासादिगुणामवल्लोक्य तदायत्त- चित्तवृत्तिबभूव
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7150)
- **Original**: उभयमपि तन्यनस्क- मनन्यवृष्टि परित्यक्तसमस्तान्यप्रयोजन- मभूत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7151)
- **Original**: राजा तु प्रागल्क्यात्तामाह
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7152)
- **Original**: सुध्ु स्वामहमभिकामोउस्मि रूजावखण्खडितमुर्वशी ते प्राह
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7153)
- **Original**: भवत्वेवं यदि मे समयपरिपालनं भवान्‌ करोतीत्याख्याते पुनरपि तामाह
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7154)
- **Original**: आख्याहि मे समयमितति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7155)
- **Original**: अथ पृष्ठटा पुनरष्यब्रवीत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7156)
- **Original**: झयनसमीपे ममोरणकद्धय॑ पुत्रभूत॑ नापनेयम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7157)
- **Original**: भरवांश्व मया न नझनो ड्रष्टव्य:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7158)
- **Original**: घृतपाज्न च्न मम्राहार इति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7159)
- **Original**: एजमेवेति भरूषतिरप्याह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7160)
- **Original**: तथा सह स चावनिपतिरलकायां चैत्ररथादि- येषु रममाणः पष्टिवर्षसहस्नाण्यनुदिनप्रवर्द्मान- प्रमोदोइनयत्‌
- **Translation**: 

---

