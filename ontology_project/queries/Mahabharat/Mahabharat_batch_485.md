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

### Verse 1 (Mahabharat 0.4841)
- **Original**: कुरक्रे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4841)
- **Original**: कुरक्रे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4842)
- **Original**: ्ठ युधिष्ठिरको ही प्रसन्न करो, जब वे प्रसन्न हो
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4842)
- **Original**: ्ठ युधिष्ठिरको ही प्रसन्न करो, जब वे प्रसन्न हो
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4843)
- **Original**: . उतके ऐसा कहनेपर अरजुनने कहा--'राजन्‌! मैं जायें तो हमलछोग शीघ्र ही सूतपुत्र कर्णसे लड़नेके
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4843)
- **Original**: . उतके ऐसा कहनेपर अरजुनने कहा--'राजन्‌! मैं जायें तो हमलछोग शीघ्र ही सूतपुत्र कर्णसे लड़नेके
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4844)
- **Original**: 'कैल-सहदेव तथा भीमसेनकी सोगंध खाता हूँ और अपने लिये चलें।'
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4844)
- **Original**: 'कैल-सहदेव तथा भीमसेनकी सोगंध खाता हूँ और अपने लिये चलें।'
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4845)
- **Original**: इधियारोंको छूकर सत्यकी झपथ करके कहता हूँ कि आज गये और बोले “राजन्‌ ! धर्मपालनकी कामनासे भयभीत
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4845)
- **Original**: इधियारोंको छूकर सत्यकी झपथ करके कहता हूँ कि आज गये और बोले “राजन्‌ ! धर्मपालनकी कामनासे भयभीत
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4846)
- **Original**: रणभूमिमें शयन करूँगा।' राजासे यों कहकर अर्जुन होकर मैंने जो कुछ कह डाला है, उसे क्षपा कीजिये और श्रीकृष्णसे बोले---'माधव ! आज युद्धमें मैं अवश्य कर्णको मुझपर प्रमत्न होडये । धर्मगऊने देखा अत परोपा पड़े हा. 8 ऑफ आपकी बुद्धिके बलसे ही उस दुरात्माका वध शषे रहे हैं, तो उन्होंने अपने प्यारे भाईंकों उठाकर बड़े ख्रेहके साथ गले छगाया और स्वर्य भी फूट-फूटकर रोने लगे।
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4846)
- **Original**: रणभूमिमें शयन करूँगा।' राजासे यों कहकर अर्जुन होकर मैंने जो कुछ कह डाला है, उसे क्षपा कीजिये और श्रीकृष्णसे बोले---'माधव ! आज युद्धमें मैं अवश्य कर्णको मुझपर प्रमत्न होडये । धर्मगऊने देखा अत परोपा पड़े हा. 8 ऑफ आपकी बुद्धिके बलसे ही उस दुरात्माका वध शषे रहे हैं, तो उन्होंने अपने प्यारे भाईंकों उठाकर बड़े ख्रेहके साथ गले छगाया और स्वर्य भी फूट-फूटकर रोने लगे।
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4847)
- **Original**: आह छाप कोल" चुन । हु प्रदर््ाक5 धाम जद बाद के पक केज के के और
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4847)
- **Original**: आह छाप कोल" चुन । हु प्रदर््ाक5 धाम जद बाद के पक केज के के और
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4848)
- **Original**: इच्छा तुम किसी तरह मारते।' अर्जुनसे ही: के शुद्ध ही । यह आदह आह धर्मराज युधिष्ठिससे बोले--'राजन्‌ ! ह
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4848)
- **Original**: इच्छा तुम किसी तरह मारते।' अर्जुनसे ही: के शुद्ध ही । यह आदह आह धर्मराज युधिष्ठिससे बोले--'राजन्‌ ! ह
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4849)
- **Original**: आप पीड़ित हो गये हैं--यह तदनन्तर, युचिहिरने पुनः अर्जुनकों बड़े प्रेमसे गले।
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4849)
- **Original**: आप पीड़ित हो गये हैं--यह तदनन्तर, युचिहिरने पुनः अर्जुनकों बड़े प्रेमसे गले।
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4850)
- **Original**: और आपके डे लैब कद थे । सौधालाओो रूगाया और उनका मस्तक सुूँघकर अत्पत्त प्रसन्नताके साथ इक “कब को अंक लक बात है कि आप न तो मारे गये और न उसकी कैदमें ही 6-30 है “0 00 “अर यु 2020-08 4
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4850)
- **Original**: और आपके डे लैब कद थे । सौधालाओो रूगाया और उनका मस्तक सुूँघकर अत्पत्त प्रसन्नताके साथ इक “कब को अंक लक बात है कि आप न तो मारे गये और न उसकी कैदमें ही 6-30 है “0 00 “अर यु 2020-08 4
- **Translation**: 

---

