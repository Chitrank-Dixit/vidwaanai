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

### Verse 1 (Vishnu Puran 0.9501)
- **Original**: 10 तयोहिद्द्रान्तरप्रेप्सुरविषह्ञामसन्यत । कृष्ण ततो रौहिणेयं हन्तुं चक्रे मनोरधम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9502)
- **Original**: 11 हरिणाक्रीडर॑ नाम बालक्रीडनक ततः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9503)
- **Original**: प्रकुर्वन्तो हि ते सर्वे द्वो द्वो युगपदुत्थितो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9504)
- **Original**: 12 श्रीपराशरजी बोले--अपने अनुचरोंसहित उस गर्दभासुस्के मारे जानेपर बड़ सुरम्य ताल्वन गोप और गोपियोंके लिये सुखदायक हो गया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9505)
- **Original**: तदनच्तर घेनुकासुरकों मारकर ले दोनों वसुदेवपुत्र प्रसन्न-मनसे भाष्डीर नामक वरटदृक्षके तले आये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9506)
- **Original**: कन्धेपर गौ बाँधनेकी रस्सी डाले और वनमालासे विभूषित हुए बे दोनों महात्मा बालक सिंहनाद करते, गाते, वुक्षोंपर चढ़ते, दूरतक गौएऐँ चराते तथा उनका नाम ले-लेकर पुकारते हुए नये सींगोंबाले बछड़ोंके समान सुशोभित हो रहे थे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9507)
- **Original**: उन दोनोंके वस्न [क्रमशः ] सुनहरी और श्याम रंगसे रँगे हुए थे अतः वे इन्द्रघनुषयुक्त बैल और दयाम मेघके समान जान पड़ते थे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9508)
- **Original**: वे समस्त लोकपालॉके प्रभु पृथियीपर अबतीर्ण होकर नाना प्रकारकी त्लेकिक लीलाओंसे परस्पर खेल रहे थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9509)
- **Original**: मनुष्य-धर्ममें तत्पर रहकर मनुष्यताका सम्मान करते हुए थे मनुष्यजातिके गुणोंकी क्रीडाएँ करते हूए वनमें विचर रहे थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9510)
- **Original**: थे दोनों महाचल्ती बालक कभी झूल्ममें झूछकर, कभी परस्पर मल्लयुद्धकर और कभों पत्थर फेंकक्तर नाना प्रकारसे व्यायाम कर रहे ये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9511)
- **Original**: इसौ समय उन दोनों खेलते हुए बाल्कॉकों उठा ले जानेकी इच्छासे प्रलम्य नामक दैत्य गोपवेषमें अपनेक्ो छिपाकर वहाँ आया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9512)
- **Original**: दानवल्नेष्ठ प्ररुम्न मनुष्य न होनेपर भो मनुष्यरूप धारणकर निदषक्भावसे उन बालकोंके बीच घुस गया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9513)
- **Original**: उन दोनोंको असावधानताका अवसर देखनेवाले उस दैत्यने कृष्णको तो सर्वथा अजेय समझा; अतः उसने बलरामजीको मारनेका निश्चय किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9514)
- **Original**: तदनन्तर ये समस्त ग्वाल्याल हरिणाक्रौडन* नामक खेल खेलते हुए आपसमें एक साथ दो-दो +# एक निश्चित रूक्ष्यके पास दो-दो बालक एक-एक साथ हिसनकों भाँति उछलते हुए जाते हैं। जो दोनॉमें पहले पहुँच आता है बत्त विजयी होता है, हारा हुआ बालक जीते हुएको अपनी पोठपर चढ़ाकर पुख्य सथानतक के आंता है। यही हरिणाक्रीदन है।
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9515)
- **Original**: श्रीदाम्ना सह गोविन्द: प्रलम्बेन तथा बल: । गोपालैरपरैश्वान्ये गोपाला: पुप्नुवुस्ततः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9516)
- **Original**: 13 श्रीदामान ततः कृष्ण: प्रलम्बं रोहिणीसुतः । जितवान्कृष्णपक्षीयैगोंपैरन्ये. पराजिता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9517)
- **Original**: 14 ते बाहवन्तस्त्वन्योन्ये भाण्डीरं वटपमेत्य वै। पुनर्निववृतुस्सर्वे ये ये ततन्र पराजिता:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9518)
- **Original**: 15 सड्ूर्षणं तु स्कन्धेन शीप्रपुत्क्षिप्प दानव: । नभस्सस्‍थलं जगामाशु सचन्द्र इव वारिदः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9519)
- **Original**: 16 असहन्नौहिणेयस्य स॒भार॑ दानवोत्तमः। ववृधे स महाकाय: प्रावृषीव बलाहकः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9520)
- **Original**: 17 सड्डर्षणस्तु त॑ दृष्ठा दःधदौल्ोपमाकृतिम्‌ । ख्रग्दामलम्बाभर्ण मुकुटाटोपमस्तकम्‌
- **Translation**: 

---

