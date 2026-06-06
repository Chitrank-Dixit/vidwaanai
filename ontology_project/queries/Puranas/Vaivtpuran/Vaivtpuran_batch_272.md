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

### Verse 1 (Vaivtpuran 13.11582)
- **Original**: लिये नाना रूप धारण करते हैं; युगके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11583)
- **Original**: ण्र्ड * संक्षिप्त ब्रह्मवैवर्तपुराण « अनुसार जिनके श्वेत, रक्त, पीत और श्याम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11584)
- **Original**: स्थलपर विराजमान होते हैं, कहीं राधाके साथ वर्ण हैं; सत्ययुगमें जिनका स्वरूप शुक्ल
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11585)
- **Original**: जलक्रीड़ा करते हैं, कहीं वनमें राधिकाके तेजोमय है तथा उस युगमें जो सत्यस्वरूप हैं;
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11586)
- **Original**: केश-कलापोंकी चोटी गूँथते हैं, कहीं राधिकाके त्रेतामें जिनकी अद्भकान्ति कुंकुमके समान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11587)
- **Original**: चरणोंमें महाबर लगाते हैं, कहीं राधिकाके चबाये लाल है और जो ब्रह्मतेजसे जाज्वल्यमान रहते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11588)
- **Original**: हुए ताम्बूलको सानन्द ग्रहण करते हैं, कहीं बाँके 'ऋ कुकर]
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11589)
- **Original**: “त्रोंसे देखती हुई राधाको स्वयं निहारते हैं, > ै
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11590)
- **Original**: कहीं फूलोंकी माला तैयार करके राधिकाको 280)
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11591)
- **Original**: अर्पित करते हैं, कहीं राधाके साथ रासमण्डलमें जाते हैं, कहीं राधाकी दी हुई मालाकों अपने कण्ठमें धारण करते हैं, कहीं गोपाड्रनाओंके साथ विहार करते हैं, कहीं राधाको साथ लेकर चल 7
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11592)
- **Original**: देते हैं और कहीं उन्हें भी छोड़कर चले जाते £24
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11593)
- **Original**: हैं। जिन्होंने कहीं ब्राह्मणपत्रियोंक दिये हुए 2
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11594)
- **Original**: अन्नका भोजन किया है और कहीं बालकोंके साथ ताड़का फल खाया है; जो कहीं आनन्दपूर्वक 7 भ 2 गोप-किशोरियोंके चित्त चुराते हैं, कहीं ग्वालबालोंके 2 के
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11595)
- **Original**: साथ दूर गयी हुई गौओंको आवाज देकर बुलाते
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11596)
- **Original**: हैं, जिन्होंने कहीं कालियनागके मस्तकपर +
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11597)
- **Original**: अपने चरणकमलोंको रखा है और जो कहां हैं, द्वापरमें जो पीत कान्ति धारण करके पीताम्बरसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11598)
- **Original**: मौजमें आकर आनन्‍्द- विनोदके लिये मुरलीकी सुशोभित होते हैं; कलियुगमें कृष्णवर्ण होकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11599)
- **Original**: तान छेड़ते हैं तथा कहीं ग्वालबालॉके साथ *कृष्ण' नाम धारण करते हैं; इन सब रूपोंमें मधुर गीत गाते हैं; उन परमात्मा श्रीकृष्णको जो एक ही परिपूर्णतम परमात्मा हैं; जिनका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11600)
- **Original**: मैं प्रणाम करता हूँ। श्रीविग्रह नूतन जलधरके समान अत्यन्त श्याम इस स्तवराजसे स्तुति करके इन्द्रने श्रीहरिको एवं सुन्दर है; उन नन्दनन्दन यशोदाकुमार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11601)
- **Original**: भयसे प्रणाम किया। पूर्वकालमें वृत्रासुरके साथ भगवान्‌ गोविन्दकी मैं वन्दना करता हूँ। जो
- **Translation**: 

---

