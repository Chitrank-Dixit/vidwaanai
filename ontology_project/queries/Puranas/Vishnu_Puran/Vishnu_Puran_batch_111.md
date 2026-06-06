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

### Verse 1 (Vishnu Puran 0.2201)
- **Original**: हिरण्यकशियु बोत्ला--अरे स्पों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2202)
- **Original**: इस अत्यन्त दुर्बुद्ध और दराचारीकों अपने तिषाप्रि-सन्तप्त मुजोंसे ऋटकर शीघ्र हो नष्ट कर दो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2203)
- **Original**: श्रीपरा्यरजी बोले--ऐसी आज्ञा होनेपर अतिक्ूर और जविषधचर तक्षक आदि स्पोनि. उनके समस्त अगोंमें काटा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2204)
- **Original**: किन्तु उन्हें तो श्रीकृष्णचन्द्रमें आसक्त- डन महासपोके काटनेपर भी अपने दारोरकी कोई सुधि नहीं हुई
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2205)
- **Original**: सर्प खोले--डे टैत्यगाज ! देखो, हमारी दाठें टूट गयीं, मणियाँ खटखने लगीं, फणो्में पीड़ा होने छगी और हृदय कँपने लगा, तथापि इसको त्वचा तो जरा भी नहीं कटी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2206)
- **Original**: इसलिये अब आप हमें कोई और कार्य बताइये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2207)
- **Original**: हिरण्यकहिपु खोलला--हे दिगजो ! तुम सब अपने संकीर्ण दाँतोंकों मिलाकर मेरे दात्रु-पक्षद्वार [ बहकाकर ] मुझसे विमुख किये हुए इस बआालकको मार डालते । देखो, जैसे अरणीसे उत्पन्न हुआ अप्रि उसीको जला डालता है उसी प्रकार कोई-कोई जिससे उत्पन्न होते हैं ठसीके नाश करनेवाले हो जाते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2208)
- **Original**: श्रीपराह्रजी बोले--तब पर्वत-शिखरके समान विशालकाय दिग्गजोनि उस बालूककों पृथिवीपर पटककर अपने दाँतोंसे खूब रौंदा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2209)
- **Original**: किन्तु श्रीगोविन्दका स्मरण करते रहनेसे हाथियोंकि हजारों दाँत उनके यक्षःस्थलसे टकराकर टूट गये; तब उन्होंने पिता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2210)
- **Original**: आ 17 ] प्रधम अंदा 39 जि से न बलें ममैतत्‌। ऑष्कर्षलिकोम ..... जनारनानुस्परणानुभावः हिरण्यकलिपुरुवाच ज्वाल्यतामसुरा वह्िरपसर्पत दिगाजा:। वायो समेथयाप्नि त्वं दह्मतामेष पापकृत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2211)
- **Original**: 45 औपरादर उवाच महाकाष्डचयस्थ॑ तमसुरेन्रसुतं॑. ततः । अ्रज्वाल्य दानवा वह्ठिं ददहुः स्वामिनोदिता:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2212)
- **Original**: 46 अह्लाद उताच तातैष यहि: पवनेरितोउपि न माँ दहत्यत्न समन्ततो5हम्‌। पश्यामि पद्मास्तरणास्तृतानि शीतानि सर्वाणि दिद्याम्मुखानि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2213)
- **Original**: 47 अ्रीपयदार उवाच अथ दैव्येश्वरं प्रोचुर्भा्गवस्थात्मजा द्विजा: । पुरोहिता महात्मानः साप्ना संस्तूय बराम्मिन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2214)
- **Original**: 48 राजन्नियम्यतां कोपो बालेउपि तनये निजे । कोपो देवनिकायेषु तेषु ते सफलो यतः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2215)
- **Original**: 49 तथातथैनं बालं ते शासितारों खयं नृप । यथा विपक्षनाशाय विनीतस्ते भविष्यति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2216)
- **Original**: 70 बालत्व॑ सर्वदोषाणां दैत्यराजास्पदं यतः । ततोउत्र कोपमत्यर्थ योक्तुमरहसि नार्भके
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2217)
- **Original**: 51 न त्यक्ष्यति हरेः पक्षमस्माकं वचनाछयदि। तत:ः कृत्यां वधायास्य करिष्यामोउनिवर्त्तिनीम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2218)
- **Original**: 52 श्रीपराजर उवाच एवमभ्यर्थितस्तैस्तु दैत्ययाज: पुरोहितेः । दैत्यैर्निष्कासयाघास पुत्र पावकसज्लयात्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2219)
- **Original**: 53 ततो गुरुगृहे बाल: स वसनन्‍्जालदानवान्‌ ।
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2220)
- **Original**: हिरण्यकशिपुसे कहा--
- **Translation**: 

---

