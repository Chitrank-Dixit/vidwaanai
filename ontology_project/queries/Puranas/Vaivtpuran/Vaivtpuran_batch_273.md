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

### Verse 1 (Vaivtpuran 13.11602)
- **Original**: युद्धेके समय गुरु बृहस्पतिने इन्द्रको यह स्तोत्र गोपियोंका चित्त चुराते हैं तथा राधाके लिये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11603)
- **Original**: दिया था। सबसे पहले श्रीकृष्णने तपस्वी ब्रह्माको प्राणोंसे भी अधिक प्रिय हैं, जो कौतूहलवश
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11604)
- **Original**: कृपापूर्वक एकादशाक्षर-मन्त्र, सब लक्षणोंसे युक्त विनोदके लिये मुरलीकी ध्वनिका विस्तार
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11605)
- **Original**: कवच और यह स्तोत्र दिया था। फिर ब्रह्माने करते रहते हैं, जिनके रूपकी कहीँ तुलना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11606)
- **Original**: पुष्करमें कुमारको, कुमारने अड्विराको और अड्विराने नहीं है, जो रत्रमय आभूषणोंसे विभूषित हो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11607)
- **Original**: बृहस्पतिको इसका उपेदश दिया था। इन्द्रद्वारा कोटि-कोटि कन्दर्पोंका सौन्दर्य धारण करते हैं;
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11608)
- **Original**: किये गये इस स्तोत्रका जो प्रतिदिन भक्तिपूर्वक उन शान्त-स्वरूप परमेश्वरको मैं प्रणाम करता पाठ करता है, वह इहलोकमें श्रीहरिकी सुदृढ़ हूँ। जो वृन्दावनमें कहीं राधाके पास क्रौड़ा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11609)
- **Original**: भक्ति और अन्तमें निश्चय ही उनका दास्य-सुख करते हैं, कहीं निर्जन स्थलमें राधाके वक्ष:-
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11610)
- **Original**: प्राप्त कर लेता है। जन्म, मृत्यु, जरा, व्याधि और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11611)
- **Original**: + भ्रीकृष्णजन्मखण्ड * 515 अऊक 5 55% ## #5# 8 #/ 45 ## 84 44 $ $ 5 % # ## 544 4 %5# 5 95 ## ### 6 #& #/ # # # 4 #$ डक डक ऊ कक 5 इक ड़ शोकसे छुटकारा पा जाता है और स्वप्रमें भी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11612)
- **Original**: चाहनेवाले हैं; उन सच्चिदानन्दमय गोविन्ददेवको कभी यमदूत तथा यमलोकको नहीँ देखता।*
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11613)
- **Original**: बारंबार नमस्कार है। प्रभो! आप ब्राह्मणोंका प्रिय भगवान्‌ नारायण कहते हैं--इन्द्रका वचन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11614)
- **Original**: करनेवाले देवता हैं; स्वयं ही ब्रह्म और परमात्मा सुनकर भगवान्‌ लक्ष्मीनिवास प्रसन्न हो गये और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11615)
- **Original**: हैं; आपको नमस्कार है। आप अनन्तकोटि उन्होंने प्रेमपूर्वक उन्हें वर देकर उस पर्वतको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11616)
- **Original**: ब्रह्माण्डधामोंके भी धाम हैं; आपको सादर नमस्कार वहाँ स्थापित कर दिया। श्रीहरिको प्रणाम करके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11617)
- **Original**: है। आप मत्स्य आदि रूपोंके जीवन तथा साक्षी इन्द्र अपने गणोंके साथ चले गये; तदनन्तर गुफामें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11618)
- **Original**: हैं; आप निर्लिप्त, निर्गुण और निराकार परमात्माको छिपे हुए लोग वहाँसे निकलकर अपने घरको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11619)
- **Original**: नमस्कार है। आपका स्वरूप अत्यन्त सूक्ष्म है। गये। उन सबने श्रीकृष्णको परिपूर्णतम परमात्मा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11620)
- **Original**: आप स्थूलसे भी अत्यन्त स्थूल हैं। सर्वेश्वर, माना। व्रजवासियोंको आगे करके श्रीकृष्ण अपने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11621)
- **Original**: सर्वरूप तथा तेजोमय हैं; आपको नमस्कार है। घरको गये। नन्दके सम्पूर्ण अद्जोंमें रोमाश्न हो
- **Translation**: 

---

