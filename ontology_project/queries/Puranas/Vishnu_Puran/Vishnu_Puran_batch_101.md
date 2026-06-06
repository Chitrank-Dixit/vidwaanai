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

### Verse 1 (Vishnu Puran 0.2001)
- **Original**: 125 मुनि पूर्वमन्वन्तरे भ्रेष्ठा द्वादशासन्सुरोत्तमा: । तुषिता नाम तेउन्योउन्यमूजुवैंबस्वतेउन्तरे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2002)
- **Original**: 126 उपस्थितेठतियझसश्चाक्षूपस्थान्तरे मनो:। समवायीकृताः सर्वे समागम्य परस्परम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2003)
- **Original**: 127 अनिरूकी पत्नी शिवा थी; उससे अनिलके मनोजब और अखिज्ञातगति--ये दो पुत्र हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2004)
- **Original**: अग्निके पुत्र कुमार शरस्तम्ब (सरकण्डे)से उत्पन्न हुए थे, ये कृत्तिकाओंके पुत्र होनेसे कार्तिकेय कहलाये। झास, विशञाख और नैगमेय इनके छोटे भाई थे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2005)
- **Original**: 115-116
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2006)
- **Original**: देवलक नामक ऋषिको प्रत्यूषकत्र पुत्र कहा जाता है। इन देवलके भी दो क्षमाशील और मनीषी पुत्र हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2007)
- **Original**: बृहस्पतिजीकी बहिन वरस्त्री, जो ब्रह्मचारिणी और सिद्ध योगिनी थी तथा अनासक्त-भावसे समस्त भूमण्डलमें विचरती थी, आठवें यसु प्रभासको भार्या हुई
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2008)
- **Original**: उससे सहस्रों शिल्पों (क्रशैगरियों) के कर्ता और देवताओंके शिल्पी महाभाग प्रजापति विश्वकर्माका जच्म हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2009)
- **Original**: जो समस्त शिल्पकारोंमें श्रेष्ठ और सब प्रकारके आभूषण बनानेवाले हुए तथा जिन्होंने देवताओके सम्पूर्ण विमानॉकी रचना की और जिन महात्माकी [ आकिष्कृता ] शिल्प- लिद्याके आश्रयसे बहुत-से मनुष्य जीवन-निर्वाह करते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2010)
- **Original**: उन विश्वकर्मकि चार पुत्र थे; उनके नाम सुनो । वे अजैकपाद, अहिर्बुध्न्य, त्वष्टा और परमपुरुषार्थी स् थे। उममेंसे त्वाशके पुत्र मह्मतंपस्वी विश्वरूप
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2011)
- **Original**: हे महामुते ! हर, बहुरूप, ज्यम्बक,
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2012)
- **Original**: अपराजित, बुषाकपि, दाम्भु, कपदीं, रैवत, मृगव्याध,
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2013)
- **Original**: शर्व और कपाली--ये ब्रिल्लोकीके अधीश्वर ग्यारह रुद्र कहे गये हैं। ऐसे सैकड़ों महातेजस्वी एकाददा रुद्र
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2014)
- **Original**: असिद्ध हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2015)
- **Original**: 122-123
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2016)
- **Original**: जो [ दक्षकन्याएँ ] कश्यपजीकी स्त्रियाँ हुई उनके नाम सुनों--वे अदिति, दिति, दनु, अरिप्टा, सुरसा, खसा, सुर्राभ, जिनता, ताम्रा, क्रोधवज्ञा, इरा, कद्भु और मुनि थीं। हे धर्मज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2017)
- **Original**: अब तुम उनकी सन्तानका विवरण श्रवण करो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2018)
- **Original**: 124-1257
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2019)
- **Original**: पूर्व (चाक्षुष) मन्वन्तरमें तुषित नामक बारह श्रेष्ठ देवगण थे । ये यदास्वी सुरश्रेष्ठ चाक्षुष मन्‍्वन्तरके पश्चात्‌ सैवस्वत-मन्वन्तरके उपस्थित होनेपर एक-दूसरेके पास जाकर मिले और परस्पर कहते रूगे---
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2020)
- **Original**: 126-127
- **Translation**: 

---

