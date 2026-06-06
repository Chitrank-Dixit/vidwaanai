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

### Verse 1 (Agni Puran 0.6241)
- **Original**: परवित्रमधिक शुभोदर्य व्यासवक्त्रकधित॑ प्रवृत्तकम्‌
- **Translation**: 

---

### Verse 2 (Agni Puran 0.6242)
- **Original**: मनाक्य्सृतदन्तदोधिति स्मरोल्लप्ितगण्डमण्डला । कटाक्षललिता तु कामिनी मनो हरति चारुहासिनी
- **Translation**: 

---

### Verse 3 (Agni Puran 0.6243)
- **Original**: है. स्थिरजिलासनतमौक्तिकायली कमलकोमलाडी मृरेक्षणा। हरति कस्य हृदय न कामित: सुरतकेलिकुशलापरान्तिका
- **Translation**: 

---

### Verse 4 (Agni Puran 0.6244)
- **Original**: अश्मश्र॒ुपुणो.. विराैर्दनीर्गम्भीराक्षो. मितवासाप्र: । तिर्मासातु: स्फुटित: केशैर्मात्रासम्क लभते दुःखम्‌
- **Translation**: 

---

### Verse 5 (Agni Puran 0.6245)
- **Original**: 5. मन्पथचापध्वनिरमणीय: : । वनवासस्त्रीस्वनितविशेष: कस्य न चिर्त्त स्मयति पुंस:
- **Translation**: 

---

### Verse 6 (Agni Puran 0.6246)
- **Original**: 6. भ्रातर्गुणरहित विश्लोक॑ । जात॑ महितकुले5प्यविनीतं मित्र परिहर साधुविशोतम्‌
- **Translation**: 

---

### Verse 7 (Agni Puran 0.6247)
- **Original**: 7. यदि याज्ठसि परपदमारोदुं मैत्रीं परिहर सह वनिताभि: । सुझति मुनिरपि विषयासज़ाच्चित्रा भकति हि सनप्ो वृत्ति: # 8. यज्यित गुह्सरूपुदारं॑ विश्याध्यासमहास्यसन॑ च॑। पृथ्वी तस्य गुणैहपतचित्रा चन्रमरीचिनिभेर्भवतीयम्‌#
- **Translation**: 

---

### Verse 8 (Agni Puran 0.6248)
- **Original**: 9. अलिवाचालितविकसितबूते काले मदनसमागमदूते । स्मृत्वा कान्तां परिहवतसार्थ: पादाकुलकं धावति पान्य: # (इसमें झाजसमक, विश्लोक, वातवासिका और उपचित्राके चरण हैं।) म्रदकलखगकुलकलरवमुखरिणि विकसितसरसतिजपरिमलसुरभिणि
- **Translation**: 

---

### Verse 9 (Agni Puran 0.6249)
- **Original**: गिरिवरपरिसरसरस्तसि सहति खलु रतिरतिशयमिह सस इृदि खिलसति #
- **Translation**: 

---

### Verse 10 (Agni Puran 0.6250)
- **Original**: होता है। छन्दकी मात्राओंसे उसके अक्षरोंपें
- **Translation**: 

---

### Verse 11 (Agni Puran 0.6251)
- **Original**: ले, फिर अक्षरोंकी संख्या लिख ले। मात्राके जितनी. कमी हो, उतनी गुरुकी संख्या और
- **Translation**: 

---

### Verse 12 (Agni Puran 0.6252)
- **Original**: अझ्टोमेंसे अक्षरोंके अड्डू घटा दे; जितना बचे, अक्षरोंसे जितनी कमी गुरुकी संख्यामें हो, उतनी
- **Translation**: 

---

### Verse 13 (Agni Puran 0.6253)
- **Original**: वह गुरुकी संख्या हुईं। इसी प्रकार अक्षरसंख्यामें लघुकी संख्या मानी गयी है। तात्पर्य यह है' कि
- **Translation**: 

---

### Verse 14 (Agni Puran 0.6254)
- **Original**: गुरुकी संख्या घटा देनेपर जो बचे, वह लघु यदि कोई पूछे, इस आर्यामें कितने लघु और
- **Translation**: 

---

### Verse 15 (Agni Puran 0.6255)
- **Original**: अक्षरोंकी संख्या होगी'। इस प्रकार बर्ण आदिके कितने गुरु हैं तो उस आर्याकों लिखकर उसकी
- **Translation**: 

---

### Verse 16 (Agni Puran 0.6256)
- **Original**: अन्तरसे गुरु-लघु आदिका ज्ञान प्राप्त करना सभी मात्राओंकी गणना करके कहीं लिख
- **Translation**: 

---

### Verse 17 (Agni Puran 0.6257)
- **Original**: चाहिये
- **Translation**: 

---

### Verse 18 (Agni Puran 0.6258)
- **Original**: 13--18
- **Translation**: 

---

### Verse 19 (Agni Puran 0.6259)
- **Original**: इस प्रकार आदि आग्रेय महापुराणयें 'छन्दोजातिका निरूपण” नामक तीन साँ इकतीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 20 (Agni Puran 0.6260)
- **Original**: >>ढ>#व्वपड020 050 तीन सौ बत्तीसवाँ अध्याय विषमवृत्तका वर्णन अग्निदेव कहते हैं--[छन्द या पद्य दो
- **Translation**: 

---

