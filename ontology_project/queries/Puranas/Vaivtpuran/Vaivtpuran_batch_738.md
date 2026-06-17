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

### Verse 1 (Vaivtpuran 543.13074)
- **Original**: रात उसे जलाये रखती और उसके बीचमें बैठकर संक्षेपसे सुना गया है और न विस्तारसे ही। परंतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13075)
- **Original**: निरन्तर मन्त्र जपती रहती थी। वर्षा-ऋ्तु आनेपर अब विस्तारसे ही सुननेकी इच्छा है; अत: आप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13076)
- **Original**: श्मशानभूमिमें शिवा सदा योगासन लगाकर बैठती विस्तारपूर्वक इस विषयका वर्णन कीजिये।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13077)
- **Original**: और शिलाकी ओर देखती हुई जलकी धारासे पार्वतीने स्वयं कौन-कौन-सा कठोर तप किया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13078)
- **Original**: भीगती रहती थी। शीतकाल आनेपर वह सदा था? और किस-किस वरकों पाकर किस तरह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13079)
- **Original**: जलके भीतर प्रवेश कर जाती तथा शर्तकी महे श्वरकों प्राप्त किया तथा रतिने फिर किस प्रकार
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13080)
- **Original**: भयंकर बर्फवाली रातोंमें भी निराहार रहकर कामदेवको जिलाया? प्यारे कृष्ण! आप पार्वती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13081)
- **Original**: भक्तिपूर्वक तपस्या करती थी। और शिवके' विवाहका वर्णन कीौजिये। इस प्रकार अनेक वर्षोंतक कठोर तप करके श्रीकृष्णने कहा--प्राणाधिके राधिके !
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13082)
- **Original**: भी जब सती-साध्वी पार्वती शंकरकों न पा सकी, प्राणवल्लभे ! सुनो। प्राणेश्वरि! तुम प्राणोंकी अधिष्ठात्री
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13083)
- **Original**: तब वह शोकसे संतप्त हो अग्निकुण्डका निर्माण देवी हो। प्राणाधारें! मनोहरे! जब रुद्रदेव
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13084)
- **Original**: करके उसमें प्रवेश करनेको उद्यत हो गयी। वटवृक्षेक नीचेसे चले गये, तब पार्वती माता-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13085)
- **Original**: तपस्यासे अत्यन्त कृशकाय हुई सती शैल-पुत्रीको पिताके बार-बार रोकनेपर भी तपस्याके लिये अग्निकुण्डमें प्रवेश करनेको उच्चत देख कृपासिन्धु चली गयी। गज़ाके तटपर जा तीनों काल स्त्रान
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13086)
- **Original**: शिव कृपा करके स्वयं उसके पास गये। अत्यन्त करके बह मेरे दिये हुए मन्त्रका प्रसन्नतापूर्वक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13087)
- **Original**: नाटे कदके बालक ब्राह्मणका रूप धारण करके जप करने लगी। उस जगदम्बाने पूरे एक वर्षतक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13088)
- **Original**: अपने तेजसे प्रकाशित होते हुए भगवान्‌ शिव
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13089)
- **Original**: + श्रीकृष्णजन्मखण्ड « 571 कक ऋक्4 49% ###%## #% %# 4 ### ## ##ऋऋ% 45% %$%%%%%## ####### मन-ही-मन बड़े हर्षका अनुभव कर रहे थे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13090)
- **Original**: पार्वतीने कहा--ब्रह्मन्‌ ! न तो मैं वेदजननी उनके सिरपर जटा थी। उन्होंने दण्ड और छत्र
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13091)
- **Original**: सावित्री हूँ, न लक्ष्मी हूँ और न वाणीकी भी ले रखे थे। श्वेत वस्त्र, श्वेत यज्ञोपवीत, श्वेत
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13092)
- **Original**: अधिष्ठात्री देवी सरस्वती ही हूँ। मेरा जन्म कमलके बीजोंकी माला एवं श्वेत तिलक धारण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13093)
- **Original**: भारतवर्षमें हुआ है। मैं इस समय गिरिराज किये वे मन्द-मन्द मुस्करा रहे थे। निर्जन स्थानमें
- **Translation**: 

---

