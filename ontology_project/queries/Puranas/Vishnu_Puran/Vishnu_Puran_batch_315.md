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

### Verse 1 (Vishnu Puran 0.6281)
- **Original**: तझाथा सकलजगतापमादिरनादिभूतस्स ऋग्य- जुस्सामादिमयों भगवान्‌ विष्णुस्तस्य ब्रह्मणो पूर्त्त रूप॑ हिरण्यग्ों ब्रह्माण्डभूतो ब्रहा भगवान्‌ प्राग्वभूव
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6282)
- **Original**: 02494 %5729 58:27 दक्षप्रजापति: 02494 %5729 58:27 विवस्वतो मनुः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6283)
- **Original**: मनोरिक्ष्वाकुनृगधृष्ट- अर्यातिनरिष्यन्तप्रांशुनाभागदिष्टकरूषपृषध्राख्या दहव पुत्रा नभूबु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6284)
- **Original**: इृष्टिं च्ष मिनत्नावरुणयोर्मनु: पुत्र॒कामअकार
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6285)
- **Original**: तत्र ताबदपहुते होतुरफ्जारादिला नाम कन्या बभूव
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6286)
- **Original**: सैत ज्ञ मित्रावरुणयो: असादात्सुम्युश्नों नाम मनोः पुत्रो मैत्रेय आसीत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6287)
- **Original**: पुनश्षेश्वरकोपात्खी सती सा तु सोमसूनोर्चुधस्याश्रमसमीपे बश्राम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6288)
- **Original**: श्रीमैत्रेयजी जोले--हे भगवन्‌ ! सत्कर्ममें प्रवुत्त रहनेवाले पुरुषोंको जो करने चाहिये उन सम्पूर्ण नित्य- नैमित्तिक कर्मोंका आपने वर्णन कर दिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6289)
- **Original**: हे गुगे ! आपने वर्ण-घर्म और आश्रम-घर्मोंकी व्याख्या भी कर दी। अब मुझे राजयंशॉक्म विवरण सुननेकी इच्छा है, अतः डक्‍का वर्णन कीजिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6290)
- **Original**: श्रीपराइरजी जोले--हे मैत्रेय ! अब तुप्त अनेकों यज्ञकर्ता, ्युरवीर और चैर्यश्ञात्त्र भुपालॉंसे सुशोभित इस मनुवंधाका वर्णन सुनो जिसके आदिपुरुष श्रीग्रह्माजी हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6291)
- **Original**: हे मैत्रेय! अपने वंझके सम्पूर्ण पापोको नष्ट करनेके लिये इस वंश-परम्पणकी कथाका क्रमश: श्रवण करो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6292)
- **Original**: डसका विवरण इस प्रकार है--सकल सं॑सारके आदिकारण भगकान्‌ विष्णु हैं। वे अनादि तथा ऋक्‌- साम-यजु:स्वरूप हैं। उन ज्हास्वरूप भगवान्‌ विष्णुके मूर्चरूप त्रह्माप्डसय हिरण्यगर्भ भगवान्‌ ब्रह्माजी सबसे पहले प्रकट हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6293)
- **Original**: अ्ह्माजीके दायें औगूठेसे दक्षप्रजापति हुए, दक्षसे अदिति हुई तथा अदितिसे विजस्वान्‌ और बिवस्वानूसे मनुका जन्म हुआ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6294)
- **Original**: मनुके इश्च्वाकु, नृग, धृष्ट, शर्याति, नरिष्यन्त, प्रोशु, नाभाग, दिष्ट, करूष और पृषन्त॒ नामक दस पुत्र हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6295)
- **Original**: मनुते पुत्रकी इच्छासे मिनश्नावरुण नामक दो देवताओंके यज्ञका अनुष्ठान किया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6296)
- **Original**: किन्तु होताके विपरीत सहूल्पसे यज्ञ्में विपर्यय हो जानेसे उनके 'इला' नामकी कन्या हुई
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6297)
- **Original**: हे मैत्रेय ! मित्रावरणकी कृपासे वह इत्म हो मनुका '“सुझुम्र' नामक पूत्र हुईं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6298)
- **Original**: फिर महादेक्जीके कोप (कोपप्रयुक्त शाप) से वह स्तरों होकर चन्द्रमाके पुत्र बुधफे आश्रपके निकट घूमने छूगी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6299)
- **Original**: 228 श्रीविष्णुपुराण [अश 1 सानुरागश्च तस्यां बुध: पुरूरवसमात्मजमुत्पा- दयामास
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6300)
- **Original**: जातेउपि तस्मिन्नमिततेजोधि: परमर्पिभिरिष्टिमय. ऋछमयों यजुर्मयस्साथ- मयो<थर्वणमयस्सर्ववेदमयो मनोमबो ज्ञानमयो न किज्षित्मयो5न्नमयो भगवान्‌ यज्ञपुरुषस्वरूपी सुधुप्नस्य पुंस्तवमभिलषद्धिर्यथावदिष्टस्तत्पसादा- दिला पुनरपि सुद्ुप्लो$भवत्‌
- **Translation**: 

---

