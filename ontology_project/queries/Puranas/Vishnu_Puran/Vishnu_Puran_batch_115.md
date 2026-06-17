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

### Verse 1 (Vishnu Puran 0.2281)
- **Original**: इसलिये विवेकी पुरुषकों चाहिये कि देहकी बाल्य, यौवन और वृद्ध आदि अनस्थाओंकी अपेक्षा न करके बाल्यावस्थामें हो अपने कल्याणका यत्न करे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2282)
- **Original**: मैंने तुम ल्तेगोंसे ओ कुछ कहा है उसे यदि तुम मिथ्या नहीं समझते तो मेरी प्रसन्नताके लिये ही बनन्‍्धनको छुटानेवाले श्रीविष्णुभगवानका स्मरण करो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2283)
- **Original**: उनका स्मरण करनलेमें परिश्रम भी क्‍या है? और स्मरणमात्रसे ही खे अति शुभ फल देते हैं तथा रात-दिन उच्कींका स्मरण करनेजाल्म्रेंका पाप भी नष्ट हो जाता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2284)
- **Original**: उन सर्वभूतस्थ प्रभूमें तुम्हारी बुद्धि अहर्निस छगी रहे और उनमें निरन्तर तुम्हारा प्रेम बढ़े; इस प्रकार तुम्हारे समस्त फ्लेद्दा दूर हो जायैंगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2285)
- **Original**: जब कि यह सभी संसार तापत्रयसे दग्घ हो रहा है तो इन बेचारे शोचनीय जीवॉसे कौन बुद्धिमान्‌ द्वेष करेगा 2
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2286)
- **Original**: यदि [ ऐसा दिखायो दे कि ] 'और
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2287)
- **Original**: रे अ्ीविष्णुपुराण [ अ0 17
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2288)
- **Original**: 82 एते भिन्नदुशां दैत्या विकल्पा: कथिता मया । कृत्वाभ्युपगर्म॑ तत्र सल्लेप: श्रूयतां मम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2289)
- **Original**: 883 विस्तार: सर्वभूतस्य बिष्णो: सर्वमिर्दं जगत्‌ । द्व्यमात्यवत्तस्मादभेदेन.. विच्क्षण:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2290)
- **Original**: 84 समुत्सुज्यासुरं भाव॑ तस्माद्यूयं तथा बयम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2291)
- **Original**: तथा यत्रं करिष्यामो यथा प्राप्स्याम निर्वृतिम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2292)
- **Original**: 85 या नाग्निना न चार्केण नेन्दुना ज न बायुना । पर्जन्यवरुणाभ्यां वा न सिद्धैर्न च राक्षसैः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2293)
- **Original**: 86 न यक्षैर्न च दैत्येज्रैनोरिगर्न च किन्नरैः । न म्नुष्यर्न पशुभिदेषिर्नैवात्मसम्भवै:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2294)
- **Original**: 87 ज्वराक्षिरोगातीसारप्रीहगुल्मादिकैस्तथा । द्ेषेष्यापत्सराद्येर्वा रागछोभादिभि: क्षयम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2295)
- **Original**: 88 न चान्यैर्नीयते कैश्निन्नित्या यात्यन्तनिर्मला। तामाप्रोत्यमले न्यस्थ केशवे हुदय॑ नरः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2296)
- **Original**: 89 असारसंसारविवर्तनेषु .. आ यात तोष॑ प्रसर्भ ब्रवीमि । सर्वत्र दैत्यास्समतायुपेत समत्वमाराधनमच्युतस्य तस्मिशससक्ने किमिहास्यलभ्यं ___ प्रर्मार्थकार्मेरलूमल्पकास्ते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2297)
- **Original**: 90 जीव तो आनन्दमें हैं, मैं ही परम शक्तिहीन हूँ” तब भी प्रसन्न ही होना चाहिये, क्योंकि ट्रेषका फल तो टु:खरूप ही है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2298)
- **Original**: यदि कोई प्राणी वैरभावसे द्रेष भी करें. तो विचारवानोंके लिये तो वे 'अहो ! ये महामोहसे व्याप्त हैं!” इस प्रकार अत्यन्त शोचनीय ही हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2299)
- **Original**: हे दैत्यगण ! ये मैंने भिन्न-भिन्न दृष्टिवाल्त्रेंके किकल्प (भिन्न-भिन्न उपाय) कहे। अजब उनका समन्ययपूर्वक संक्षिप्त विचार सुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2300)
- **Original**: यह सम्पूर्ण जगत्‌ सर्वभूतमय भगवान्‌ विष्णुका विस्तार है, अतः विचक्षण पुरुषोंकोी इसे आत्माके समान अभेदरूपसे देखना चाहिये
- **Translation**: 

---

