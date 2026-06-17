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

### Verse 1 (Vaivtpuran 31.7491)
- **Original**: राज्य॑ देय॑ शिरों देय॑ प्राणा देयाक्ष पुत्रक। एवंभूत॑ च कवच न॒ देय॑ प्राणसंकटे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7492)
- **Original**: (गणपतिखण्ड 31
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.7493)
- **Original**: + गणपतिखए्ड + 359 अंक $ $ % # ऊ # $ 5 $ हक 5 $ $ $ $ ऊ$ कक 5 $ # कड़क $$# 85 कह # # # # है # $ 8 5 कक ##$ 8 56 54% # कु ## 6. सम्यक्‌-रूपसे पूजा करे। तत्पश्चात्‌ इसी क्रमसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.7494)
- **Original**: धारण करते हैं तथा जो देव स्वयं माया और श्रीकृष्णका पूजन करे। फिर गणेश, सूर्य, अग्रि,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.7495)
- **Original**: स्वयं मायेश्वर हैं; उन्हें मेरा प्रणाम है। जो सम्पूर्ण विष्णु, शिव और पार्वती-इन छ: देवोंकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.7496)
- **Original**: दुःखोंसे उबारनेवाले, सभी कारणोंके कारण और भलीभाँति अर्चना करके इष्टदेवकी पूजा करे।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.7497)
- **Original**: समस्त विश्वोंको धारण करनेवाले हैं, सबके विघ्ननाशके लिये गणेशका, व्याधिनाशके लिये
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7498)
- **Original**: कारणस्वरूप हैं; उन परमेश्वरको मैं प्रणाम करता सूर्यका, आत्मशुद्धिके लिये अग्रिका, मुक्तिके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7499)
- **Original**: हूँ। जो तेजस्वियोंमें सूर्य, सम्पूर्ण जातियोंमें लिये श्रीविष्णुका, ज्ञानेक लिये शंकरका और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7500)
- **Original**: ब्राह्मण और नक्षत्रोंमें चन्द्रमा हैं; उन जगदी श्वरको परमैश्चर्यकी प्राप्तिके लिये दुर्गाका पूजन करनेपर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7501)
- **Original**: मेरा अभिवादन है। जो रुद्रों, वैष्णवों और यह फल मिलता है। यदि इनका पूजन न किया
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7502)
- **Original**: ज्ञानियोंमें शंकर हैं तथा जो नागोंमें शेषनाग हैं; जाय तो विपरीत फल प्राप्त होता है। तदनन्तर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7503)
- **Original**: उन जगत्पतिकों मैं मस्तक झुकाता हूँ। जो भक्तिभावसहित इष्टदेवका परिहार करके भक्तिपूर्वक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7504)
- **Original**: प्रजापतियोंमें ब्रह्मा, सिद्धोंमें स्‍्व्य॑ कपिल और सामवेदोक्त स्तोत्रका पाठ करना चाहिये। (वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7505)
- **Original**: मुनियोंमें सनत्कुमार हैं; उन जगदगुरुकों मेरा स्तोत्र बतलाता हूँ) उसे श्रवण करो। प्रणाम स्वीकार हो। जो देवताओंमें विष्णु, महादेवजीने कहा--जो परखब्रह्म, परम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7506)
- **Original**: देवियोंमें स्वयं प्रकृति, मनुओंमें स्वायम्भुव मनु, धाम, परम ज्योति, सनातन, निर्लिप्त और सबके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7507)
- **Original**: मनुष्योंमें वैष्णण और नारियोंमें शतरूपा हैं; उन कारण हैं, उन परमात्माकों मैं नमस्कार करता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7508)
- **Original**: बहुरूपियेको मैं नमस्कार करता हूँ। जो ऋतुओंमं हूँ। जो स्थूलसे स्थूलतम, सूक्ष्मसे सृक्ष्मतम, वसन्त, महीनोंमें मार्गशीर्ष और तिथियोंमें एकादशी सबके देखनेयोग्य, अदृश्य और स्वेच्छाचारी हैं,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7509)
- **Original**: हैं; उन सर्वरूपको मैं प्रणाम करता हूँ। जो उन उत्कृष्ट देवको मैं प्रणाम करता हूँ। जो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7510)
- **Original**: सरिताओंमें सागर, पर्वतोंमें हिमालय और सहनशीलॉमें साकार, निराकार, सगुण, निर्णुण, सबके आधार,
- **Translation**: 

---

