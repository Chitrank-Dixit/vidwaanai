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

### Verse 1 (Vaivtpuran 18.1159)
- **Original**: ग्राणरूपं प्राषण्नां च परमात्मानमीश्वम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1160)
- **Original**: त॑ च॒ स्तोतुमशक्ताहमबला निर्गुणं विभुम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1161)
- **Original**: निर्लक्ष्यं च निरीह च सार॑ वाइमनसो: परम्‌ । य॑ स्तोतुमक्षमोउनन्त: सहस्नवदनेन च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1162)
- **Original**: पञ्चयक्त्रक्षतुर्वकत्रों.. गजवक्त; घड़ानन: । य॑ स्तोतुं न क्षमा माया मोहिता यस्य मायया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1163)
- **Original**: य॑ं स्तोतुं न क्षमा श्रीक्ष जडीभूता सरस्वतों। वेदा न शक्ता य॑ स्तोतुं को वा विद्वांख वेदवित्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1164)
- **Original**: कि स्तौमि तमनीहँ च शोकार्ता स्त्री परात्परम्‌ू। (त्रह्मखण्ड 18
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1165)
- **Original**: 9-343)
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1166)
- **Original**: + खह्यास्त्रणड + 55 अ5%$%ऋ%$%%$%$%%क%%$%$%%$%$%$%%$%$%%ऋ%ऋऋ%कऋ$%ऋ%$ऋ%ऋकऋऋ%कऋ%$%%कऊऋकऋऋ%ऋऋऋऊऋ%कऋ$%ऋऊऋऊऋ%%$%ऊऋऋऋ%ऋऋ%%#%%%%$%%%$%क%%$%%%%%$ 95 %$ जाता है। भयभीत पुरुष भयसे छुटकारा पा जाता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1167)
- **Original**: होनेकी स्थितिमें आ गया है अथवा जलके है। जिसका धन नष्ट हो गया है, उसे धनकी प्राप्ति समुद्रमें डूब रहा है, वह भी इस स्तोत्रका पाठ होती है। जो विशाल वनमें डाकुओं अथवा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1168)
- **Original**: करके विपत्तिसे छुटकारा पा जाता है। हिंसक जन्तुओंसे घिर गया है, दावानलसे दग्ध
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1169)
- **Original**: (अध्याय 18) #40/500/50 सक46225..052+ 0 ब्रह्माण्डपावन नामक कृष्णकबच, संसारपावन नामक शिवकवच और शिवस्तवराजका वर्णन तथा इन सबकी महिमा सौति कहते हैं--मालावती ब्राह्मणोंकों धन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1170)
- **Original**: इस प्रकार बोधसम्पन्न हो परमानन्दमय गन्‍्धर्वने देकर बहुत प्रसन्न हुई। उसने स्वामीकी सेवाके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1171)
- **Original**: अपने कुबेरभवनसदृश आश्रममें रहकर बन्धु- लिये नाना प्रकारसे अपना श्रृड्गार किया। बह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1172)
- **Original**: बान्धवोंके साथ राज्य किया। उपबर्हणकी अन्य प्रतिदिन पतिकी सेवा-शुश्रूषा और समयोचित
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1173)
- **Original**: स्त्रियाँ भी जैसे-तैसे वहाँ आयी और आकर पूजा करने लगी। उत्तम ब्रतका पालन करनेवाली
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1174)
- **Original**: उन्होंने बड़े आनन्दके साथ पुन: अपने स्वामीको उस पतित्नताने स्वयं एकान्तमें पतिको भूले हुए
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1175)
- **Original**: प्रात किया। महापुरुषके स्तोत्र, पूजन, कबच और मन्त्रक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1176)
- **Original**: शौनकने पूछा--सूतनन्दन! पूर्वकालमें बोध कराया। पूर्वकालमें वसिष्ठजीने पुष्करतीर्थमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1177)
- **Original**: बसिष्ठजीने उन दोनों दम्पतिकों भगवान्‌ विष्णुके गन्धर्व और मालाबतीकों इस श्रीहरिके स्तोत्र,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1178)
- **Original**: किस स्तोत्र, कवच, मन्त्र और पूजा-विधिका पूजन आदिका तथा एक मन्त्रका उपदेश दिया
- **Translation**: 

---

