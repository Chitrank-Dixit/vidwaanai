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

### Verse 1 (Vaivtpuran 12.706)
- **Original**: चले गये और उपबर्हण गन्धर्बने तत्काल उस समयानुसार बड़े होनेपर उपबर्हणने वसिष्ठजीके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.707)
- **Original**: शरीरको इस प्रकारसे त्याग दिया-मूलाधार, द्वारा परम दुर्लभ हरि-मन्त्रकी दीक्षा पाकर दुष्कर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.708)
- **Original**: स्वाधिष्ठान, मणिपूर, अनाहत, विशुद्ध और आज्ञा तपस्या प्रारम्भ की। एक समयको बात है, बे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.709)
- **Original**: नामवाले छ: चक्रोंका क्रमश: भेदन करके उन्होंने गण्डकीके तटपर विराजमान थे। उन्हें युवावस्था
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.710)
- **Original**: इडा आदि नाड़ियोंका भेदन आरम्भ किया। इडा, प्राप्त हो चुकी थी। उस समय पचास गन्धर्वकन्याओंने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.711)
- **Original**: सुषुम्णा, मेधा, पिड्ला, प्राणहारिणी, सर्वज्ञानप्रदा, उन्हें देखा। देखते ही वे सब-कौ-सब मोहित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.712)
- **Original**: मनःसंयमनी, विशुद्धा, निरुद्धा, वायुसंचारिणी, तेज:- हो गयीं। उन सबने उपबर्हणको पतिरूपमें प्राप्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.713)
- **Original**: शुष्ककरी, बलपुष्टिकरी, बुद्धिसंचारिणो, ज्ञानजुम्भन- करनेका संकल्प ले योगशक्तिसे प्राणोंकों त्याग
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.714)
- **Original**: कारिणी, सर्वप्राणहरा तथा पुनर्जीवनकारिणी-इन दिया और चित्ररथ गन्धर्वके घर जन्म लेकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.715)
- **Original**: सोलह नाड़ियोंका भेदन करके मनसहित पिताकी आज्ञासे उनके साथ बिबाह कर लिया।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.716)
- **Original**: जीवात्माको ब्रह्मरन्श्रमें लाकर वे योगासनसे बैठ उपबर्हणने दीर्घकालतक उन सबके साथ विहार
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.717)
- **Original**: गये और दो घड़ीतक उन्होंने आत्माको आत्मामें किया। चिर्कालतक निरन्तर उनके साथ राज्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.718)
- **Original**: ही लगाया। तत्पश्चात्‌ वे जातिस्मर (पूर्वजन्मकी करके एक दिन वे ब्रह्माजीके स्थानपर गये और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.719)
- **Original**: बातोंको याद रखनेबाले) योगिराज उपबर्हण वहाँ श्रीहरिका यशोगान करने लगे। वहीं रम्भाको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.720)
- **Original**: ब्रह्मभावको प्राप्त हो गये। तीन तारवाली दुर्लभ नृत्य करते देख उपबर्हणके मनमें वासना जाग
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.721)
- **Original**: बीणाको बायें कंधेपर रखकर दाहिने हाथमें शुद्ध उठी और उनका वीर्य स्खलित हो गया। इससे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.722)
- **Original**: स्फटिककी माला लिये वे बेदके सारतत्त्व तथा उनकी बड़ी हँसी हुई और ब्रह्माजीने उन्हें शाप
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.723)
- **Original**: उद्धारके उत्तम बीजरूप परात्पर परब्रह्ममय (कृष्ण) देते हुए कहा--'तुम गन्धर्व-शरीरको त्याग दो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.724)
- **Original**: इन दो अक्षरोंका जप करने लगे। उन्होंने कुशको और शुद्रयोनिको प्राप्त हो जाओ। फिर समयानुसार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.725)
- **Original**: चटाईपर पूर्वकी ओर सिरहाना करके पश्चिम वैष्णबोंका संसर्ग प्राप्त कर तुम पुनः मेरे पुत्रके
- **Translation**: 

---

