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

### Verse 1 (Vishnu Puran 0.9381)
- **Original**: 43 आनम्य चापि हस्ताभ्यामुभाभ्यां मध्यम शिर: । आस्द्वाभुअशझिरसः प्रणनत्तोरुविक्रम:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9382)
- **Original**: 4डड॑ ब्राणा: फणे5भवश्रास्य कृष्णस्पाह्मप्निनिकुड्ने: । यत्रोन्नति च कुरुते ननामास्थ ततहिशरः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9383)
- **Original**: 45 मूर्छछापुपाययो भ्रान््या नाग: कृष्णस्य रेचकै: । दण्डपातनिपातेन वबाम रुधिर॑ बहु
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9384)
- **Original**: 46 त॑ विभुम्रशिरोग्रीवमास्थेभ्यस्लुतशोणितम्‌ । विलोक्य करुणं जग्मुस्तत्पत्यों मधुसूदनम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9385)
- **Original**: 47 नागफ्ल्‍य ऊचु: ज्ञातोईसि देवदेवेश सर्वज्ञस्त्वमनुत्तम: । परं ज्योतिरचिन्यं यत्तदंशः परमेश्वर:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9386)
- **Original**: 48 न समर्था: सुरास्स्तोतुं यमनन्यभय्ं विभुम्‌ । स्वरूपवर्णनं तस्थ कर्थ योफ्त्किरिष्यति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9387)
- **Original**: 49 यस्थाखिलमहीव्योमजलाभिपवनात्यकम्‌ । ब्रह्माण्डमल्पकाल्पांश: स्तोष्यामस्त कथं वयम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9388)
- **Original**: 50 यतन्तो न दिदुर्नित्यं यत्स्वरूपं हि योगिन: । परमार्थमणोरल्पं स्थूलात्स्थूलं नता: सम तम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9389)
- **Original**: 51 न यस्य जन्मने धाता यस्प चान्ताव नान्तक: । स्थितिकर्त्ता न चान्योउस्ति यस्य तस्मै नमस्सदा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9390)
- **Original**: 52 कोप:ः स्वल्पो5पि ते नास्ति स्थितिपालनमेव ते । कारणं कालियस्थास्थ दमने श्रूयतां बच:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9391)
- **Original**: 53 खियो5नुकम्प्यास्साधूनां मूढ़ा दीनाझ्न जन्तव: । अतस्ततोउस्य दीनस्य क्षम्बतां क्षमताों वर
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9392)
- **Original**: 54 प्रीतिब्रेषो समोत्कृष्टगोचरौ भवतोउव्यय
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9393)
- **Original**: 56 अश्रीचिष्णुपुराण [ अच 7 श्रीपराशरजी बोले--इस प्रकार स्मरण कराये जानेपर, मधुर मुसकानसे अपने ओष्ठसप्पुटकों खोलते हुए श्रीकृष्णचद्धने उछलछकर अपने झरीस्को सर्पके बन्धनसे छुड़ा लिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9394)
- **Original**: और फिर अपने दोनों हाथोंसे उसका थ्ीचका फण झुकाकर उस नतमस्तक सर्पके ऊपर चढ़कर बड़े वेगसे नाचने सकगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9395)
- **Original**: कृष्णचन्द्रके चरणोंकी धमकसे उसके प्राण मुखमें आ गये, यह अपने जिस मस्तककों उठाता उसीपर कूदकर भगवान्‌ उसे झुका देते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9396)
- **Original**: श्रीकृष्णचन्द्रजीकी भ्रान्ति (भ्रम), रेचक तथा दण्ड॒पात नामकी [ नृत्यसम्बन्धिनी गतियोंके ताडनसे व महासर्प मूर्च्छत हो गया और उसने बहुत-सा रुधिर वमन किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9397)
- **Original**: इस प्रकार उसके सिर और ग्रीवाओंको झुके हुए तथा मुखोंसे रुधिर बहता देख उसकी पत्रियाँ करुणासे भरकर श्रीकृष्णचन्द्रक पास आयी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9398)
- **Original**: नागपत्नियाँ बोलीं--हे देवदेवेश्वर ! हमने आपको पहचान लिया; आप सर्वज्ञ और सर्वश्रेष्ठ हैं, जो अचिन्त्य और परम ज्योति है आप उसीके अंद् परमेश्वर हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9399)
- **Original**: जिन स्वयम्भू और व्यापक प्रभुको स्तुति करनेमें देवगण भी समर्थ नहों हैं उन्हीं आपके स्बरूपका हम स्त्रियाँ किस प्रकार वर्णन कर सकतो हैं ?
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9400)
- **Original**: पुथिवी, आकादा, जरू, अग्नि और वायुखरूग यह सम्पूर्ण ब्रह्माण्ड जिनका छोटे-से-छोटा अश्न है, उसकी स्तुति हम किस प्रकार कर सकेंगी
- **Translation**: 

---

