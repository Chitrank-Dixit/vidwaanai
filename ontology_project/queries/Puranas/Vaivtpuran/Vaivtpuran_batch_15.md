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

### Verse 1 (Vaivtpuran 3.165)
- **Original**: रूप, जय देनेबाले, जय देनेमें समर्थ, जयकी श्रवण करनेसे रोगी अपने रोगसे छुटकारा पा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.166)
- **Original**: ग्राप्तिक कारण तथा विजयदाताओंमें सर्वश्रेष्ठ हैं, जाता है। उन अपराजित देवता भगवान्‌ श्रीकृष्णकी मैं सौति कहते हैं--शौनकजी ! तत्पश्चात्‌ परमात्मा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.167)
- **Original**: वन्‍्दना करता हूँ। सम्पूर्ण विश्व जिनका रूप श्रीकृष्णके वामपार्श्बसे भगवान्‌ शिव प्रकट हुए।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.168)
- **Original**: है, जो विश्वके ईश्वरोंक भी ईश्वर हैं, विश्वेश्वर, मय मय अप अज्जकान्ति शुद्ध स्फटिकमणिके समान
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.169)
- **Original**: विश्वकारण, विश्वाधार, विश्वके विश्वासभाजन निर्मल एवं उज्ज्वल थी। उनके पाँच मुख थे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.170)
- **Original**: तथा विश्वके कारणोंक भी कारण हैं, उन और दिशाएँ ही उनके लिये बस्त्र थीं। उन्होंने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.171)
- **Original**: भगवान्‌ श्रीकृष्णकी मैं बन्दना करता हूँ। जो मस्तकपर तपाये हुए सुबर्णके समान पीले रंगकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.172)
- **Original**: जगत्‌की रक्षाके कारण, जगत्‌के संहारक तथा जटाओंका भार धारण कर रखा था। उनका मुख
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.173)
- **Original**: जगत्‌की सृष्टि करनेवाले परमेश्वर हैं; फलके मन्द-मन्द मुसकानसे प्रसन्न दिखायी देता था।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.174)
- **Original**: बीज, फलके आधार, फलरूप और फलदाता * यर॑ वरेण्यं बरदं॑ वराहँ वरकारणप्‌ । कारण कारणातां च कर्म तत्कर्मकारकम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.175)
- **Original**: तपस्तत्फलदं शश्वत्‌ तपस्विनां च तापसम्‌ । वन्दे नवघनश्याम॑ स्वात्मारामं॑ मनोहरम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.176)
- **Original**: निष्काम॑ कापरूपं च कामध्न कामकारणम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.177)
- **Original**: सर्व॑ सर्वेश्व सर्वबीजरूपमनुत्तमम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.178)
- **Original**: # वेदरूप॑ वेदबीज॑ बेदोक्तफलद॑ फलम्‌ । वेदज्ञ तद्विधानं च. सर्ववेदबिदां वरम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.179)
- **Original**: (चब्रह्मखण्ड 3। 10-13)
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.180)
- **Original**: + ब्रह्ाखण्ड + 9 हैं; उन भगवान्‌ श्रीकृष्णको मैं प्रणाम करता
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.181)
- **Original**: उनके सम्पूर्ण अज्भोंमें रोमाझ हो आया था तथा हूँ। जो तेज:स्वरूप, तेजके दाता और सम्पूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.182)
- **Original**: उनकी ग्रीवा भगबान्‌के सामने भक्तिभावसे झुकी तेजस्थियोंमें श्रेष्ठ हैं, उन भगवान्‌ गोविन्दकी मैं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.183)
- **Original**: हुई थी। वन्दना करता हूँ।* ब्रह्माजी बोले--जो तीनों गुणोंसे अतीत ऐसा कहकर महादेवजीने भगवान्‌ श्रीकृष्णको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.184)
- **Original**: और एकमात्र अविनाशी परमेश्वर हैं, जिनमें मस्तक झुकाया और उनकी आज्ञासे श्रेष्ठ रत्नमय
- **Translation**: 

---

