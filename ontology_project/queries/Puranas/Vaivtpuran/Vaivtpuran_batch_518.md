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

### Verse 1 (Vaivtpuran 31.7531)
- **Original**: मुरली सुशोभित है, किशोर-अवस्था है, जो परमेश्वरको मैं मस्तक झुकाता हूँ। जो शिल्पियोंमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7532)
- **Original**: आनन्दपूर्वक मुस्करा रहे हैं, गोपाड्ननाएँ निरन्तर विश्वकर्मा, रूपवानोंमें कामदेव और पत्नियोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.7533)
- **Original**: जिनकी ओर निहारा करती हैं; उन्हें मेरा प्रणाम पतिब्रता हैं; उन नमनीय प्रभुको मेरा अभिवादन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.7534)
- **Original**: स्वीकार हो। जो रत्ननिर्मित सिंहासनपर विराजमान है। जो प्रिय प्राणियॉमें पुत्ररूप, मनुष्योंमें नरेश्वर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.7535)
- **Original**: हैं और राधाद्वारा दिये गये पानको चबा रहे हैं; और यत्त्रोंमें शालग्राम हैं; उन विशिष्टकों मैं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.7536)
- **Original**: ठन मनोहर रूपधारी ईश्वरको मैं प्रणाम करता नमस्कार करता हूँ। जो कल्याणबीजोमें धर्म,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.7537)
- **Original**: हूँ। जो रत्नोंक आभूषणोंसे भलीभाँति सुसज्जित वेदोंमें सामबेद और धर्माँमें सत्यरूप हैं; उन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7538)
- **Original**: हैं तथा जिनपर पार्षदप्रवर गोपकुमार श्वेत चँवर विशिष्टको मैं प्रणाम करता हूँ। जो जलमें डुला रहे हैं; उन्हें मैं नमस्कार करता हूँ। जो शीतलता, पृथ्बीमें गन्‍ध और आकाशमें शब्दरूपसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7539)
- **Original**: रमणीय वृन्दावनके भीतर रासमण्डलके मध्य विद्यमान हैं; उन वन्दनीयको मैं अभिवादन करता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7540)
- **Original**: स्थित होकर रासक्रीडाके उल्लाससे समुत्सुक हैं; हूँ। जो यज्ञॉमें राजसूययज्ञ और छन्दोंमें गायत्री
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7541)
- **Original**: उन रसिकेश्वरको मेरा प्रणाम है। जो शतशथ्ृड्गकी छन्द हैं तथा जो गन्धर्वोर्में चित्ररथ हैं; उन परम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7542)
- **Original**: चोटियोंपर, महाशैलपर, गोलोकमें र्नपर्वतपर महनीयको मैं सिर झुकाता हूँ। जो गव्य पदार्थोंमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7543)
- **Original**: तथा विरजा नदीके रमणीय तटपर विहार दूधस्वरूप, पतित्रोंमें अग्रि और पुण्य प्रदान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7544)
- **Original**: करनेवाले हैं; उन्हें मेरा नमस्कार है। जो करनेवालॉमें स्तोत्र हैं; उन शुभदायकको मैं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7545)
- **Original**: परिपूर्णतम, शान्त, राधाके प्रियतम, मनको हरण प्रणिपात करता हूँ। जो तृणोंमें कुशरूप और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7546)
- **Original**: करनेवाले, सत्यरूप और न्रह्मस्वरूप हैं, उन शत्रुओंमें रोगरूप हैं तथा जो गुणोंमें शान्तरूप
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7547)
- **Original**: अविनाशी श्रीकृष्णनों मैं अभिवादन करता हूँ। हैं; उन विचित्र रूपधारीकों मैं नमन करता हूँ।। जो मनुष्य भारतवर्षमें श्रीकृष्णके इस स्तोत्रका जो तेजोरूप, ज्ञानरूप, सर्वरूप और महान्‌ हैं; तीनों काल पाठ करता है, वह धर्म, अर्थ, काम, उन सबके द्वारा अनिर्वचनीय सर्वव्यापी स्वयं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7548)
- **Original**: मोक्षका दाता हो जाता है। इस स्तोत्रकी कृपासे प्रभुको मेरा नमस्कार है। जो सर्वाधारस्वरूपोंमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7549)
- **Original**: श्रीहरिमें उसकी भक्ति सुदृढ़ हो जाती है। उसे वायु और नित्यरूपधारियोंमें आत्माके समान हैं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7550)
- **Original**: श्रीहरिकी दासता मिल जाती है और वह इस तथा जो आकाशकी भाँति व्याप्त हैं; उन लोकमें निश्चय ही विष्णु-तुल्य जगत्पूज्य हो जाता सर्वव्यापकको मेरा प्रणाम है। जो वेदोंद्वारा
- **Translation**: 

---

