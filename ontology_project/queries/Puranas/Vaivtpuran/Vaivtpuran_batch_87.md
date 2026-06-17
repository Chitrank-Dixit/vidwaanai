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

### Verse 1 (Vaivtpuran 6.19405)
- **Original**: 3» सर्ववर्णात्मिकाय पादयुग्म॑ सदावतु । 3» रागाधिष्टातृदेव्ये सर्वाडूं; मे सदावतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.19406)
- **Original**: 37 सर्वकण्ठवासिन्य स्वाहा प्राच्यां सदावतु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.19407)
- **Original**: 4 ह्डीं जिह्लाग्रवासिन्ये स्वाहाग्रिदिशि रक्षतु
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.19408)
- **Original**: 30 ऐं हीं श्रीं सरस्वत्ये बुधजनन्ये स्वाहा । सततं मन्त्रराजोड्यं दक्षिण मां सदाबतु
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.19409)
- **Original**: 37 हीं श्रीं व्यक्षरों मन्त्रो नैर्क़त्यां मे सदावतु । कविजिड्लाग्रवासिन्ये स्वाहा मां वारुणेउबतु
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.6170)
- **Original**: 310 + संक्षिप्त ब्रह्मवैवर्तपुराण ] पार्वतीकी स्तुतिसे प्रसन्न हुए श्रीकृष्णका पार्वतीको अपने रूपके दर्शन कराना, बर प्रदान करना और बालकरूपसे उनकी शय्यापर खेलना श्रीनारायण कहते हैं--नारद! पार्वतीद्वारा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.6171)
- **Original**: मुखपर मनोहर मुस्कान खेल रही थी। वह किये गये उस स्तवनकों सुनकर करुणानिधि
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.6172)
- **Original**: वन्दनीय स्वरूप शरदऋतुके चन्द्रमाका उपहासक श्रीकृष्णने पार्ववीकों अपने उस स्वरूपके, जो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.6173)
- **Original**: तथा मालतीकी मालाओंसे युक्त था। उसके सबके लिये अदृश्य और परम दुर्लभ है, दर्शन मस्तकपर मयूरपिच्छकी अनोखी छवि थी। कराये। उस समय पार्वतीदेवी स्तुति करके अपने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.6174)
- **Original**: गोपाड़नाएँ उसे घेरे हुए थीं। वह राधाके मनको एकमात्र श्रीकृष्णमें लगाकर ध्यानमें संलग्न
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.6175)
- **Original**: वक्ष:स्थलको उद्धासित कर रहा था, उसकी थीं। उन्होंने उस तेजोराशिके मध्य सबको मोहित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.6176)
- **Original**: लावण्यता करोड़ों कामदेवोंकों मात कर रही थी, करनेवाले श्रीकृष्णके स्वरूपका दर्शन किया। वह
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.6177)
- **Original**: वही लीलाका धाम, मनोहर, अत्यन्त प्रसन्न, एक र्रपूर्ण मनोर्म आसनपर, जो बहुमूल्य
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.6178)
- **Original**: सबका प्रेमपात्र और भक्तोंपर अनुग्रह करनेवाला रत्ोंका बना हुआ था, जिसमें हीरे जड़े हुए थे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.6179)
- **Original**: था। ऐसे उस रूपकों देखकर सुन्दरी पार्वतीने और जो मणियोंकी मालाओंसे शोभित था,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.6180)
- **Original**: मन-ही-मन उसीके अनुरूप पुत्रकौ कामना की विराजमान था। उसके शरीरपर पीताम्बर सुशोभित
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.6181)
- **Original**: और उसी क्षण उन्हें वह वर प्राप्त भी हो गया। था, हाथमें वंशी शोभा दे रही थी। गलेमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.6182)
- **Original**: इस प्रकार वरदानी परमात्माने पार्वतीके मनमें वनमालाकी निराली छटा थी। शरीरका रंग श्याम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.6183)
- **Original**: जिस-जिस वस्तुकी कामना थी, उसे पूर्ण करके था। रत्ञोंके आभूषण उसकी शोभा बढ़ा रहे थे।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.6184)
- **Original**: देवताओंका भी अभीष्ट सिद्ध किया। तत्पश्चात्‌ उसकी किशोर-अवस्था तथा वेश-भूषा विचित्र
- **Translation**: 

---

