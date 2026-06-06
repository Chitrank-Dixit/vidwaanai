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

### Verse 1 (Vaivtpuran 12.6514)
- **Original**: कीजिये। प्रभो! हमारा मायाशक्तिके साथ विवाद न मैं ही कर सकता हूँ। न चारों वेदोंकी ही शक्ति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6515)
- **Original**: हों गया है; अतः उस विप्नके प्रशमनके लिये है, फिर उन वेदवादियोंकी क्या गणना? मैं उस कवचको धारण करूँगा। इस प्रकार देवसभामें देवताऑंके साथ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6516)
- **Original**: । तदनन्तर भगवान्‌ विष्णुने कबचकी सुरेश्वर गणेशकी स्तुति करके सुराधीश रमापति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6517)
- **Original**: गोपनीयता और महिमा बतलाते हुए मौन हो गये। मुने! जो मनुष्य एकाग्रचित्त हो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6518)
- **Original**: कहा--सूर्यनन्दन! दस लाख जप करनेसे कवच भक्तिभावसे प्रातः, मध्याह और सायंकाल इस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6519)
- **Original**: सिद्ध हो जाता है। जो मनुष्य कवच सिद्ध कर विष्णुकृत गणेशस्तोत्रका सतत पाठ करता है,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6520)
- **Original**: लेता है, वह मृत्युको जीतनेमें समर्थ हो जाता है। विध्रेश्वर उसके समस्त विप्लॉंका विनाश कर देते
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6521)
- **Original**: सिद्ध-कबचवाला मनुष्य उसके ग्रहणमात्रसे भूतलपर हैं, सदा उसके सब कल्याणोंकी वृद्धि होती है
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6522)
- **Original**: वाग्मी, चिरचीवी, सर्वत्र विजयी और पूज्य हो और वह स्वयं कल्याणजनक हो जाता है। जो
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6523)
- **Original**: जाता है। इस मालामन्त्रकों तथा इस पुण्यकवचकों यात्राकालमें भक्तिपूर्बवक इसका पाठ करके यात्रा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6524)
- **Original**: धारण करनेवाले मनुष्योंके सारे पाप निश्चय ही करता है, निस्संदेह उसकी सभी अभीष्सित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6525)
- **Original**: नष्ट हो जाते हैं। भूत, प्रेत, पिशाच, कृष्माण्ड, कामनाएँ सिद्ध हो जाती हैं। उसके द्वारा देखा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6526)
- **Original**: ब्रह्मराक्षस, डाकिनी, योगिनी, बेताल आदि, बालग्रह, गया दुःस्वप्र सुस्वप्रमें परिणत हो जाता है। उसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6527)
- **Original**: ग्रह तथा क्षेत्रपाल आदि कवचके शब्दमात्रके कभी दारुण ग्रहपीड़ा नहीं भोगनी पड़ती। उसके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6528)
- **Original**: श्रवणसे भयभीत होकर भाग खड़े होते हैं। जैसे शत्रुओंका विनाश और बन्धुओंका विशेष उत्कर्ष
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6529)
- **Original**: गरुड़के निकट सर्प नहीं जाते, उसी तरह होता है। निरन्तर विप्लोंका क्षय और सदा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6530)
- **Original**: कवचधारी पुरुषोंक संनिकट आधि (मानसिक सम्पत्तिकी वृद्धि होती रहती है। उसके घरमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6531)
- **Original**: रोग), व्याधि (शारीरिक रोग) और भयदायक पुत्र-पौत्रकों बढ़ानेवाली लक्ष्मी स्थिररूपसे वास
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.6532)
- **Original**: शोक नहीं फटकते। इसे अपने सरल स्वभाववाले करती हैं। वह इस लोकमें सम्पूर्ण ऐश्वर्योंका भागी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.6533)
- **Original**: गुरुभक्त शिष्यको ही बतलाना चाहिये। होकर अन्‍्तमें विष्णु-पदको प्राप्त हो जाता है। शनैश्वर! इस 'संसारमोहन' नामक कवचके तीर्थों, यज्ञों और सम्पूर्ण महादानोंसे जो फल
- **Translation**: 

---

