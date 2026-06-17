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

### Verse 1 (Vishnu Puran 0.11821)
- **Original**: 19 अवज्ञाय वचस्तस्य जगृहुस्ते तदा धनम्‌। सत्रीधन॑ चैब मैत्रेय विध्क्सेनपरिग्रहम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11822)
- **Original**: 20 ततोर्जुनो धननुर्दिव्यं गाण्डीवमजरं युधि। आगेपयितुमारेभे न झश्ाक च वीर्यवान्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11823)
- **Original**: 21 चकार सज्यं कृच्छाध तथधाभूच्छिधिलं पुन: । न सस्मार ततो5स्राणि चिन्तयन्नपि पाण्डव:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11824)
- **Original**: 22 त्वग्भेदं ते परं चक्कुरस्ता गाण्डीवधन्विना
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11825)
- **Original**: 23 वह्लिना येउक्षया दत्ताइशरास्ते5पि क्षय ययु: । युद्धयतस्सह गोपालैरजुनस्थ भवक्षये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11826)
- **Original**: 24 अचिन्तयच्च कौन्तेय: कृष्णस्यैव हि तद॒लम्‌ । यन्मया शरसझतैस्सकला भूभृतो हता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11827)
- **Original**: 25 मिघत: पाण्डुपुन्नस्थ ततस्ता: प्रमदोत्तमा: । आभीरैरपकृष्यन्त काम चान्या: प्रतुद्युवु:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11828)
- **Original**: 26 यह भगददैश्वर्यसम्पन्न स्थान अति पवित्र और समस्त पापोक्ये नष्ट करनेवात्त्र है; उसके दर्शनमात्रसे मनुष्य सम्पूर्ण पापोंसे छूट जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11829)
- **Original**: हे मुनिश्रेश्ष! अर्जुनने उन समस्त द्वारकावासियोंको अत्यन्त घन-धान्य-सम्पन्न पक्चनद (पक्काब) देझमें बसाया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11830)
- **Original**: उस समय अनाथा स्त्रियॉकों अकेसे घनुर्धारी अर्जुनको ले जाते देख कूटेरोंकों ल्लोभ उत्पन्न हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11831)
- **Original**: तब उन अत्यन्त दुर्मद, पापकर्मा और छुब्घहदय आभीर दस्युओने परस्पर मिलकर सम्मत्ति की--
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11832)
- **Original**: “देखो, यह धनुर्धारी अर्जुन अकेस्त्र ही हमारा अतिक्रमण करके इन अनाथा स्तरियोंको लिये जाता है; हमारे ऐसे बल-पुरुषार्थकों चिकार है !
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11833)
- **Original**: यह भीष्म, ड्रोण, जयद्रथ और कर्ण आदि [नगर-निजासियों] को मारकर ही इतना अभिमानी हो गया है, अभी हम आमीणेकि बलूकों यह नहीं जानता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11834)
- **Original**: हमारे हाथोंमें ल्जठी देखकर यह दुर्मति धनुष लेकर हम सबकी अवज्ञा करता है फिर हमारी इन ऊँची-ऊँची भुजाओँसे क्या लाभ है ?'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11835)
- **Original**: * ऐसी सम्मतिकर वे सहस्रों लुटेरे छाठी और ढेले लेकर उन अनाथ द्वास्कावासियोंपर टूट पड़े
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11836)
- **Original**: तब अर्जुनने उन लुटेरॉक्त्रे झिड़ककर हँसते हुए कहा---' ओरे पापियो ! यदि तुम्हें मरनेकी इच्छा न हो तो अभी ल्त्रैट जाओ"
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11837)
- **Original**: किन्तु हे मैत्रेय ! लुटेरोंने उनके कथनपर कुछ भी ध्यान न दिया और भगवान्‌ कृष्णके सम्पूर्ण धन और स्रीधनको अपने अधीन कर लिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11838)
- **Original**: तब बीरवर अर्जुनने युद्धमें अक्षीण अपने गाण्डीय धनुषको चढ़ाना चाहा; किन्तु वे ऐसा न कर सके
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11839)
- **Original**: उन्होंने जैसे-तैसे अति कठिनतासे उसपर प्रत्यज्ञा (डोरी) चढ़ा भी ली तो फिर बे शिधिल हो गये और बहुत कुछ सोचनेपर भी उन्हें अपने अखोंक्ा स्मरण न हुआ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11840)
- **Original**: तब वे क्रुद्ध होकर अपने शन्नुओपर वाण बरसाने लगे; किन्तु गाष्डीबधारी अर्जुनके छोड़े हुए उन वाणोंने केवल उनकी त्वचाकों हो बीँचा
- **Translation**: 

---

