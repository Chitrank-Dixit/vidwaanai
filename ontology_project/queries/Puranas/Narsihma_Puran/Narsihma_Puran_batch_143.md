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

### Verse 1 (Narsihma Puran 0.2841)
- **Original**: इस प्रकार यह चक्रवर्तो राजा कार्तवीर्य श्रोभगवान्‌ विष्णुके हाथसे बधको प्राप्त होकर दिव्यरूप धारण करके, श्रीसम्पन्न एवं दिव्य चन्दनोंसे अनुशित्त होकर, दिव्य विमानपर आह हो, विष्णुधामको प्राप्त हुआ। फिर महात्‌ जल और पराक्रमवाले परशुराणमजीने भी इस पृथ्वीके क्षत्रियोंका इक्तोस जार संहार किया। इस प्रकार क्षत्रियोंका वध करके उन्होंने भूमिका भार उतारा और सम्पूर्ण पृथ्यो महात्मा कश्यपजीको दान कर दी
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.2842)
- **Original**: 38--40/,
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.2843)
- **Original**: इस प्रकार मैंने तुमसे सह 'जामदग्न्य' (परशुराम) नामक अबतारका बर्णन किया। जो भक्तिपूर्वक इसका श्रयण करता है, बह सब पापॉसे मुक्त हो जाता हैं। राजन्‌! इस तरह पृथ्यीपर अबतीर्ण होनेके बाद ये साक्षात्‌ भगवान्‌ विष्णुस्वरूप परशुरामजी इक्कोस बार क्षत्रियोंको मारकर, क्षत्रियतेजकों छित्न-भिन्न करके आज रामः स्थितोउच्यापि गिरौ महेन्द्रे
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.2844)
- **Original**: भी झहेन्द्र पर्वतपर विराजमान हैं
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.2845)
- **Original**: 41--43
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.2846)
- **Original**: परजुशमणदर्भाकों तम फ्ट्चत्वारिशोंठ ध्याय:
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.2847)
- **Original**: 46 4 इस प्रकार क्ीतरस्तिहयुरायमों ' परजुरमावतार नापक छियालीसकाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.2848)
- **Original**: जव # दा श्रीरापमावतारकी कथा-- श्रीरामके जन्मसे लेकर सिवाहतकके चरित्र औीयार्कण्डैय उदाए श्रृणु राजन्‌ प्रवक्ष्यामि प्रादुर्भावं हरे: शुभम्‌। ओमार्कण्डेमजी बोले--राजन्‌! अग्र मैं भगवान्‌ किण्णुके उस शुभ अवतारका वर्णन करूँगा, जिसके द्वारा देवताओंके लिये कण्टकस्वरूप रावण अपने गणोंसहित निहतो राबणो येन सगणो देवकण्टक:
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.2849)
- **Original**: मारा गया। तुम [ ध्यात देकर ] सुनो
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.2850)
- **Original**: 166 ख्रह्मणो मानसः पुत्रः पुलस्त्यो5भून्महामुनि:। तस्य वै विश्रवा नाम पुत्रो5भूत्तस्य राक्षस:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.2851)
- **Original**: 2 तस्माज्जातो महाबीरों रावणो लोकरावण:। त़्पसा महता युक्त: स तु लोकानुपाद्र॒यत्‌
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.2852)
- **Original**: 3 सेन्द्रा देवा जितास्तेन गन्धर्वा: किंनरास्तथा। यक्षाएच दानवाडऔव तेन राजन्‌ बिनिर्जिता:
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.2853)
- **Original**: 4 स्त्रियश्लैल सुरूपिण्यो हतास्तेन दुरात्मना। देवादीनां नृपश्रेष्ठ रत्नानि विविधानि च
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.2854)
- **Original**: 5 रणे कुबेरं निर्जित्य रावणो बलदर्पित:। तत्पुरीं जगृहे लड्ढां विमान चापि पुष्पकम्‌
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.2855)
- **Original**: 6 तस्वां पुर्या दशग्रीवो रक्षसामधिपो5भवत्‌। पुत्राश्न॒ जहवस्तस्थ बभूवुरमितौजस:
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.2856)
- **Original**: 7 राक्षसाक्ष तमाथ्ित्य महाबलपराक़मा:। अनेककोटयों राजन्‌ लक्कायां नित्रसन्ति ये
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.2857)
- **Original**: 8 देवान्‌ पितृन्‌ मनुष्यांश्र विद्याधरगणानपि। यक्षांश्षैव ततः सर्वे घातयन्ति दिवानिशम्‌
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.2858)
- **Original**: 9 संत्र॒स्त॑ तद्धयादेव जगदासीच्चराचरम्‌। दुःखाभिभूतमत्वर्थ सम्बभूज नराधिप
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.2859)
- **Original**: 10 एतस्मिन्रेव काले तु देवा: सेन्द्रा महर्षय:। सिद्धा विद्याधराश्षैतर गन्धर्ता: किंनरास्तथा
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.2860)
- **Original**: 11 गुहाका भुजगा यक्षा ये चानये स्वर्गंवासिन:। ब्रह्माणमग्रत: कृत्वा शद्धूरं च्र नराधिष
- **Translation**: 

---

