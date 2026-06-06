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

### Verse 1 (Vishnu Puran 0.9121)
- **Original**: अतः पृथिवीमें जो कोई यहास्वी और यज्ञकर्ता हों उनका देवताओंके अपकारके लिये सर्वधा बघ कर देना चाहिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9122)
- **Original**: अः5 ] पञ्चम अंझ 319 उत्पन्नश्रापि मे मृत्युर्भूतपूर्वस्स ले किल्‍ल । देवकीके गर्भसे उत्पनत्र हुई बालिकाने यह भी कहा है इत्येतद्वारिका प्राह देवकीगर्भसम्भवा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9123)
- **Original**: कि, वह मेरा भृतपूर्ण (प्रथम जन्पवत्र) काल निध्वय हो तस्माद्वलेषु चर परो यत्रः कार्यो महीतले । यत्नोद्धिक्ते बल्ले बाले स हन्तव्यः प्रयक्नतः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9124)
- **Original**: 13 इत्पज्ञाप्यासुरानकंस: प्रविश्याशु गृह तत: । मुमोत्त बसुदेज॑ ज्र देवकीं चर निरोधतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9125)
- **Original**: 14 कस उवाच युवयो्घातिता गर्भा वृथैवैत्ते मयाधुना । को5प्यन्य एवं नाशाय बालो मम समुद्गतः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9126)
- **Original**: 17 तदल॑ परितापेन नून॑ तद्भधाविनो हि ते। अर्भका युवयोदेषधाश्वायुषो यद्वियोजिताः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9127)
- **Original**: 16 ग्रीपराज्र उवाच इत्याश्चास्प विमुक्त्वा च कंसस्तो परिशक्नित: । उत्पन्न हो चुका है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9128)
- **Original**: अतः आजकल पृथित्रीपर उत्पन्न हुए बाछकॉके विषयमें विशेष सावधानी रख्तनो चाहिये और जिस बालकर्म विशेष बलका उद्रेक हो उसे यलपूर्वक मार डालना चाहिये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9129)
- **Original**: असुरोंको इस प्रकार आज्ञा दे कंसने कारागृहमें जाकर तुरत्त ही वसूदेल और देवकीको बन्धनसे मुक्त कर दिया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9130)
- **Original**: कंस बोला--मैंने अबतक आप दोनोंके बालकॉकी तो व॒था ही हत्या की; मेरा नाश करनेके लिये तो कोई और ही बालक उत्पन्न हों गया है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9131)
- **Original**: परन्तु आपलोग इसक्य कुछ दुःस्त्र न मानें क्योंकि उस बालकॉंकी होनहार ऐसी हीं थी। आपत्मेगोंके प्रार्व्ध-दडोषसे हो उन बालकोंको अपने जीजनसे हाथ धोना पड़ा है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9132)
- **Original**: श्रीपराशरजी बोले--हे द्विजश्रेष्ठ ! उन्हें इस प्रकार छाँढ़स बैंधा और बन्धनसते मुक्तकर कैसने शड्डित चित्तसे अन्तर्गुह द्विजश्रेष्ठ प्रविवेश तत: स्वक्रम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9133)
- **Original**: अपने अच्तःपुरमें प्रवेश किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9134)
- **Original**: इति श्रीविष्णुपुराणे पम्रमें$शे चतुर्थोउध्याय:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9135)
- **Original**: श्र पाँचवाँ अध्याय पूतना-वध अपराशर उवाच विपुक्तो वसुदेवोउपि नन्‍्दस्य शक गतः। अबृष्ट दृष्टवान्नन्दं पुत्रों जातों ममेति लै
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9136)
- **Original**: 9 वसुदेवो5पि त॑ प्राह दिष्टया दिष्टयेति सादरम्‌ । यार्दधकेपि समुत्यन्नस्तनयो5य॑ तबाधुना
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9137)
- **Original**: 2 द्तो हि वार्षिकस्सर्वों भवद्धि्॑पते: कर: । यदर्थमागतास्तस्मान्नात्र स्थेये: महाधनैः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9138)
- **Original**: 3 यदर्थमागता: कार्य तजन्निष्पन्न॑ किमास्यते । भवद्धिर्गम्यतां नन्‍द तच्छीघ्रं निजगोकुलम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9139)
- **Original**: 4 ममापषि बालकस्तत्न रोहिणीप्रभवों हि यः। स रक्षणीयो भवता यथाय॑ तनयो निजञ्ञ:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9140)
- **Original**: 5 इत्युक्ताः भ्रययुगोपा नन्दगोपपुरोगमा: । झकटारोपितैर्भाण्डै: कर॑ दत्त्वा महाब॒त्का:
- **Translation**: 

---

