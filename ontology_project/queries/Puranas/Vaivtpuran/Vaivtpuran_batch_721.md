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

### Verse 1 (Vaivtpuran 543.12734)
- **Original**: विमानपर बैठे हुए निर्बाध गतिसे ऊपरके लोक थे, इसलिये यह “भागीरथी' नामसे प्रसिद्ध हुई।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12735)
- **Original**: (वैकुण्ठ)-में चले जाते हैं। यदि दैववश सुरधुनी अपने स्रोतके अंशसे पृथ्वीपर आयी थी;
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12736)
- **Original**: पूर्वकर्मके प्रभावसे पापी पुरुष गड्ढामें डूब जाये अत: *गां गता' इस व्युत्पत्तिक अनुसार उसका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12737)
- **Original**: तो वे शरीरमें जितने रोएँ हैं, उतने दिव्य वर्षोतक “गड्जा' नाम प्रसिद्ध हुआ। इसके जलपर क्रोध
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12738)
- **Original**: भगवद्धाममें सानन्द निवास करते हैं। तदनन्तर होनेके कारण महात्मा जहुने इस नदीको अपने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12739)
- **Original**: उन्हें निश्चय ही अपने पाप-पुण्यका फल भोगना जानुओं (घुटनों)-द्वारा ग्रहण कर लिया था।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12740)
- **Original**: पड़ता है। परंतु वह भोग स्वल्पकालमें ही पूरा फिर उनकौ कन्यारूपसे इसका प्राकट्य हुआ;
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12741)
- **Original**: हो जाता है; तत्पश्चात्‌ भारतवर्षमें घुण्यवानोंके अत: इसका दूसरा नाम “जाह्नवी' है। वसुके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12742)
- **Original**: घरमें जन्म ले निश्चल भक्ति पाकर वे भगवत्स्वरूप अवतार भीष्म इसके गर्भसे उत्पन्न हुए थे, इस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12743)
- **Original**: हो जाते हैं। जो शुद्धिके लिये यात्रा करके देवेश्वरी कारण यह “भीष्मसू' (भीष्मजननी) कहलाती
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12744)
- **Original**: गड़ामें नहानेके लिये जाता है, वह जितने पग है। गद्जा मेरी आज्ञासे तीन धाराओंद्वारा स्वर्ग, चलता है, उतने वर्षोंतक अवश्य हो बैकुण्ठधाममें पृथ्वी तथा पातालमें गयी है; अत: “त्रिपथगा'
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12745)
- **Original**: आनन्द भोगता है। यदि आनुषब्लिकरूपसे भी कही जाती है। इसकी प्रमुख धारा स्वर्गमें है। गद्भाको पाकर कोई पापयुक्त मनुष्य उसमें स्नान वहाँ इसे 'मन्दाकिनी' कहते हैं। स्वर्गमें इसका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12746)
- **Original**: करता है तो वह उस समय सब पापोंसे मुक्त पाट एक योजन चौड़ा है और यह दस हजार
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12747)
- **Original**: हो जाता है। यदि वह फिर पापमें लिप्त न हो योजनकी दूरीमें प्रवाहित होती है। इसका जल
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12748)
- **Original**: तो निष्पाप ही रहता है। कलियुगमें पाँच हजार दूधके समान स्वच्छ एवं स्वादिष्ट है तथा इसमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12749)
- **Original**: वर्षोतक भारतवर्षमें गड्भाकी साक्षात्‌ स्थिति है। सदा ऊँची-ऊँची लहरें उठती रहती हैं। वैकुण्ठसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12750)
- **Original**: उसके विध्वमान होते हुए कलिका क्‍या प्रभाव यह ब्रह्मलोकमें और वहाँसे स्वर्गमें आयी है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12751)
- **Original**: रह सकता है? कलिमें दस हजार बर्षोंतक मेरी स्वर्गसे चलकर हिमालयके शिखरपर होती हुईं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12752)
- **Original**: प्रतिमाएँ तथा पुराण रहते हैं। उनके होते हुए यह प्रसन्नतापूर्वक पृथ्वीपर उतरी है। इसकी उस
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12753)
- **Original**: वहाँ कलिका प्रभाव क्‍या हो सकता है?
- **Translation**: 

---

