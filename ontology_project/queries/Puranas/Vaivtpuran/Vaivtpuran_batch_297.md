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

### Verse 1 (Vaivtpuran 13.12082)
- **Original**: साधनभूता मुरलीको उन्होंने अपने हाथमें ले रखा हैं--गणेश, सूर्य, अग्नि, विष्णु, शिव तथा पार्वती।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12083)
- **Original**: है। देवता और असुर सभी उनकी पूजा करते हैं। इन सबकी पूजा और वन्दना करके श्रीहरिका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12084)
- **Original**: वे ध्यानके द्वारा भी किसीके वशमें आनेवाले नहीं स्मरण करते हुए व्रत करे। ज्रती पुरुष यदि इन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12085)
- **Original**: हैं। उन्हें आराधनाद्वारा रिझ्ना लेना भी बहुत कठिन छ: देवताओंकी आराधना किये बिना नित्य और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12086)
- **Original**: है। ब्रह्मा आदि देवता भी उनकी वन्दना करते हैं नैमित्तिक कर्मका अनुष्ठान करता है तो उसका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12087)
- **Original**: और वे समस्त कारणोंके भी कारण हैं; उन बह सारा कर्म निष्फल हो जाता है। इस प्रकार
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12088)
- **Original**: परमेश्वर श्रीकृष्णका मैं भजन करता हूँ। ब्रतकी अड्भभूत सारी आवश्यक विधि बतायी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12089)
- **Original**: । इस विधिसे ध्यान और आवाहन करके गयी। इसका काण्वशाखामें वर्णन है। महामुने!
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12090)
- **Original**: पूर्वोक्त सोलह प्रकारकी उपहार-सामग्री अर्पित अब तुम अभीष्ट ब्रतके विषयमें सुनो। करते हुए भक्तिभावसे उनका पूजन करे। नारद! सामवेदमें बताये हुए ध्यानके अनुसार परात्पर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12091)
- **Original**: निम्नाद्धित मन्त्रोंसे उन्हें पूजनोपचार अर्पित करने भगवान्‌ श्रीकृष्णका ध्यान करके मस्तकपर फूल
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12092)
- **Original**: चाहिये। रखकर फिर ध्यान करे। नारद! मैं गूढ़ ध्यान बता आसन रहा हूँ, जो सबके लिये वाज्छनीय है। इसे अभक्त। परमेश्वर! यह रत्नसारजटित सुवर्णनिर्मित पुरुषके सामने नहीं प्रकाशित करना चाहिये।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12093)
- **Original**: सिंहासन भाँति-भाँतिके विचित्र चित्रोंसे अलंकृत भक्तोंके लिये तो यह ध्यान प्राणोंसे भी अधिक
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12094)
- **Original**: है। इसे ग्रहण कीजिये। प्रिय है। भगवान्‌ श्रीकृष्णका शरीर-विग्रह नवीन वस्त्र मेघमालाके समान श्याम तथा सुन्दर है। उनका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12095)
- **Original**: . राधावल्लभ ! विश्वकर्मद्वारा निर्मित इस दिव्य मुख शरत्पूर्णिमाके चन्द्रमाकी आभाको तिरस्कृत
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12096)
- **Original**: बस्त्रकों प्रज्बलित आगमें धोकर शुद्ध किया गया
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12097)
- **Original**: 534 » संक्षिप्त ख्रह्मवैवर्तपुराण + 882 3 7) )2])0।)]0]।।0। 2 । 03333] है। इसका मूल्य वर्णनातीत है। इसे धारण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12098)
- **Original**: शिल्पीद्वारा रचित यज्ञोपवीत ग्रहण कीजिये। कीजिये। भूषण पाद्य नन्दनन्दन! बहुमूल्य रत्नोंद्ारा रचित दिव्य करुणानिधान! आपके चरणोंकों पखारनेके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12099)
- **Original**: प्रभासे प्रकाशमान तथा समस्त अवयबोंको लिये सुवर्णमय पात्रमें रखा हुआ यह सुवासित
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12100)
- **Original**: विभूषित करनेवाला यह भूषण स्वीकार कीजिये। शीतल जल स्वीकार कीजिये। गन्ध अर्घ्य दीनबन्धो! समस्त मड्भल-कर्ममें वर्णनीय भक्तवत्सल! शब्बु-पात्रमें रखे गये जल,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12101)
- **Original**: तथा मज्जलदायक यह प्रमुख गन्ध सेवामें समर्पित पुष्प, दूर्वा तथा चन्दनसे युक्त यह पवित्र अर्ध्य
- **Translation**: 

---

