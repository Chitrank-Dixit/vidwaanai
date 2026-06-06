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

### Verse 1 (Bramha 0.5601)
- **Original**: (178 । 123--125)
- **Translation**: 

---

### Verse 2 (Bramha 0.5602)
- **Original**: 270 हि * संक्षिप्त ब्रह्मपुराण « भगवान्‌की झाँकी देखकर कण्डुमुनिके शरीरमें
- **Translation**: 

---

### Verse 3 (Bramha 0.5603)
- **Original**: गर्मी करनेवाले हैं। आपका पार पाना कठिन है। रोमाञझ्न हो आया। उन्होंने दण्डकी भाँति पृथ्वीपर
- **Translation**: 

---

### Verse 4 (Bramha 0.5604)
- **Original**: आप बड़ी कठिनाईसे प्राप्त होते हैं। दुःख और गिरकर साष्टाड़ प्रणाम किया और कहा-'आज
- **Translation**: 

---

### Verse 5 (Bramha 0.5605)
- **Original**: पीड़ाओंका नाश करनेवाले हरे! जलमें शयन मेरा जन्म सफल हुआ, आज मेरी तपस्याका फल
- **Translation**: 

---

### Verse 6 (Bramha 0.5606)
- **Original**: करनेवाले नारायण! आपको नमस्कार है। अव्यक्त मिल गया।' यों कहकर मुनिने भगवान्‌की स्तुति
- **Translation**: 

---

### Verse 7 (Bramha 0.5607)
- **Original**: परमेश्वर! आप सम्पूर्ण भूतोंके पालक और ईश्वर आरम्भ की। हैं। भौतिक तत्त्वोंसे आप कभी क्षुब्ध होनेवाले नहीं
- **Translation**: 

---

### Verse 8 (Bramha 0.5608)
- **Original**: ज़्ण्ब्यू प्रा उूफात्नचआ
- **Translation**: 

---

### Verse 9 (Bramha 0.5609)
- **Original**: हैं। सम्पूर्ण प्राणी आपमें ही निवास करते हैं। आप न ; ।
- **Translation**: 

---

### Verse 10 (Bramha 0.5610)
- **Original**: सब भूतोंके आत्मा हैं। सम्पूर्ण भूत आपके गर्भमें स्थित हैं। आपको नमस्कार है। आप यज्ञ, यज्वा, यज्ञधर, यज्ञधाता और अभय देनेवाले हैं। यज्ञ आपके गर्भमें स्थित है। आपका श्रीअड्ढ सुवर्णके समान कान्तिमान्‌ है। पृश्चिगर्भ! आपको नमस्कार है। आप क्षेत्रज्ञ, क्षेत्रपालक, क्षेत्री, क्षेत्रहन्ता, क्षेत्रकर्ता, जितेन्द्रिय, क्षेत्रात्मा, क्षेत्रहित और क्षेत्रके स्रष्टा हैं। आपको नमस्कार है। गुणालय, “
- **Translation**: 

---

### Verse 11 (Bramha 0.5611)
- **Original**: गुणावास, गुणाश्रय, गुणावह, गुणभोक्ता, गुणाराम प्‌ गुणत्यागी--ये सब आपके ही नाम हैं। आपको नमस्कार है। आप ही श्रीविष्णु हैं। आप हो श्रोहरि और चक्री कहलाते हैं। आप ही 3 श्रीविष्यु और आप ही जनार्दन हैं। आप ही कण्डु बोले--नारायण! हरे! श्रीकृष्ण!
- **Translation**: 

---

### Verse 12 (Bramha 0.5612)
- **Original**: बषट्कार कहे गये हैं। भूत, भविष्य और वर्तमानके श्रीवत्साडू! जगत्पते! जगद्बीज! जगद्धाम!
- **Translation**: 

---

### Verse 13 (Bramha 0.5613)
- **Original**: प्रभु भी आप ही हैं। आप भूतोंके उत्पादक और जगत्साक्षिन्‌! आपको नमस्कार है। अव्यक्त विष्णो!
- **Translation**: 

---

### Verse 14 (Bramha 0.5614)
- **Original**: अव्यक्त हैं। सबकी उत्पत्तिक कारण होनेसे आप आप ही सबकी उत्पत्तिके कारण हैं। प्रकृति और
- **Translation**: 

---

### Verse 15 (Bramha 0.5615)
- **Original**: 'भव' कहलाते हैं। आप सम्पूर्ण प्राणियोंके भरण- पुरुष दोनोंसे उत्तम होनेके कारण आपको पुरुषोत्तम
- **Translation**: 

---

### Verse 16 (Bramha 0.5616)
- **Original**: पोषण करनेवाले हैं। आप ही भूतभावन देवता हैं। कहते हैं। कमलनबन गोविन्द! जगन्नाथ! आपको
- **Translation**: 

---

### Verse 17 (Bramha 0.5617)
- **Original**: आपको अजन्मा और ईश्वर कहते हैं। नमस्कार है। आप हिरण्यगर्भ, लक्ष्मीपति, पद्मनाभ
- **Translation**: 

---

### Verse 18 (Bramha 0.5618)
- **Original**: आप विश्वकर्मा हैं, श्रीविष्णु हैं, शम्भु हैं और और सनातन पुरुष हैं। यह पृथ्वी आपके गर्भमें
- **Translation**: 

---

### Verse 19 (Bramha 0.5619)
- **Original**: वृषभकी आकृति धारण करनेवाले हैं। आप ही है। आप ध्रुव और ईश्वर हैं। हृषीकेश! आपको
- **Translation**: 

---

### Verse 20 (Bramha 0.5620)
- **Original**: शंकर, आप ही शुक्राचार्य, आप ही सत्य, आप नमस्कार है। आप अनादि, अनन्त और अजेय हैं।
- **Translation**: 

---

