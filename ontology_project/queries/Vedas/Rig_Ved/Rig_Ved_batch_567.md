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

### Verse 1 (Rig Ved 0.11321)
- **Original**: आप समस्त देवगण सत्य (यज्ञीय) मार्ग को बढ़ाते हैं। आप ऋतुओं के अनुसार हवन करने के लिए सर्वविदित हैं । आप योग्य दुग्ध को स्वीकार करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11322)
- **Original**: 4928. स्तोत्रमिद्धों मरुद्रणस्त्वष्ड्मान्‌ मित्रो अर्यमा
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11323)
- **Original**: इमा हव्या जुषन्त न:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11324)
- **Original**: मैं0 6 सू0 53 77 मरुदगण के साथ इ्धदेव त्वष्टादेव, मित्र, अर्यमा आदि सब देव हमारी आहुतियों को एवं स्तोत्रों को स्वीकार करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11325)
- **Original**: 4929. इमं नो अग्ने अध्वरं होतर्वयुनशो यज । चिकित्वान्दैव्यं जनम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11326)
- **Original**: है होता अग्निदेव ! आप हमारे इस यज्ञ में प्रमुख देवताओं के लिए उनके अनुरूप यजन क़रें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11327)
- **Original**: 4930. विश्वे देवा: शृणुतेम॑ हर्व मे ये अन्तरिक्षे य उप द्यावि ष्ठ। ये अग्निजिद्वा उत वा यजत्रा आसपद्यास्मिन्बर्हिंधि मादयध्वम्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11328)
- **Original**: हे विश्वेदेवणणो ! आप अन्तरिक्ष में अधवा द्ुलोक में (जहाँ भी) हैं, हमारी प्रार्थना सुनकर आएँ और इन कुशाओं पर बैठकर सोम का पान करके आनन्दित हों
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11329)
- **Original**: 4931. विश्वे देवा मम शृण्वन्तु यज्ञिया उभे रोदसी अपां नपाच्च मन्म
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11330)
- **Original**: मा वो वचांसि परिचक्ष्याणि बोचं सुम्नेष्विद्वो अन्तमा मदेम
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11331)
- **Original**: पृथ्वी, अन्तरिक्ष एवं अग्नि सहित समस्त देवशक्तियाँ हमारे द्वाग प्रस्तुत, श्रेष्ठ स्तोत्रों का श्रवण करें । हम कभी भी देवों को अप्रिय लगने वाले बचन न बोलें एवं देवों द्वारा प्रदत्त अनुदानों से हो ज़मुदित हों
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11332)
- **Original**: 4932. ये के च ज्मा महिनो अहिमाया दिवो जज्ञिरे अपां सथस्थे। ते अस्मभ्यमिषये विश्वमायु: क्षप उञ्चा वरिवस्यन्तु देवा:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11333)
- **Original**: चुलोक, पृथ्वोलोक और अन्तरिक्ष में अपने महान्‌ कर्मकौशल से युक्त देव प्रकट हों और हमारे पुत्रादि को अन्न एवं पूर्ण आयुष्य प्रदान करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11334)
- **Original**: 4933. अग्नीपर्जन्याववतं धियं मेउस्मिन्हवे सुहवा सुष्ठुततिं नः । इब्छामन्यो जनयद्‌ गर्भमन्य: प्रजावतीरिष आ धत्तमस्मे
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11335)
- **Original**: है अग्निदेव और पर्जन्य ! आप हमारी बुद्धि की सुरक्षा करें । है आवाहन करने योग्य ! आप स्तुति सहित हमारा आवाहन सुनें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11336)
- **Original**: आप में से एक अन्नदाता और दूसरे सन्तानदाता हैं। आप प्रसन्न होकर हमें अज्न सहित सत्तान प्रदान करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11337)
- **Original**: 4934. स्तीएें बर्हिधि समिधाने अग्नौ सूक्तेन महा नमसा विवासे । अस्मिन्नो अद्य विदथे यजत्रा विश्वे देवा हविषि मादयध्वम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11338)
- **Original**: है देवताओ !हम कुश के आसन बिऊते हैं और अग्नि प्रदीप्त करते हैं । जब हम मनोयोगपूर्वक मंत्र पाठ करें , तब आप सब देव हमारी आहुतियों एवं नमस्कारों से तृप्त हों
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11339)
- **Original**: [ सूक्त - 53 ] [ ऋषि - भरद्वाज बा्हस्पत्य । देवता.-पूषा । छन्द - गायत्री; 8 - अनुष्टप्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11340)
- **Original**: ] 4935. वयमु त्वा पथस्पते रथ न वाजसातये
- **Translation**: 

---

