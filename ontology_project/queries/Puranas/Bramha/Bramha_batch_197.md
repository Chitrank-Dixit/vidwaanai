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

### Verse 1 (Bramha 0.3921)
- **Original**: होगा। उनके सिवा दूसरा कोई तीनों लोकॉमें
- **Translation**: 

---

### Verse 2 (Bramha 0.3922)
- **Original**: » अश्वत्थ-पिष्पलतोीर्थ, शनैक्षरतीर्थ, सोमतीर्थ और थान्यतीर्थकी पहिमा * 193 ऐसा नहीं है, जो सबके मनोरथ सिद्ध कर सके।
- **Translation**: 

---

### Verse 3 (Bramha 0.3923)
- **Original**: फिर भगवान्‌ शेषेश्वरका दर्शन करनेके लिये बे मेरे कहनेसे शेषनाग वहाँ गये और गज्जामें स्तान
- **Translation**: 

---

### Verse 4 (Bramha 0.3924)
- **Original**: गौतमी-तटपर लौट आये। नागराज जिस मार्गसे करके हाथ जोड़कर देवेश्वर महादेवकी स्तुति
- **Translation**: 

---

### Verse 5 (Bramha 0.3925)
- **Original**: आये थे, उसमें रसातलसे बहाँतक छेद हो गया करने लगे--“ तीनों लोकोंके स्वामी भगवान्‌ शंकरको
- **Translation**: 

---

### Verse 6 (Bramha 0.3926)
- **Original**: था। उस बिलसे गौतमी गड्जाका अत्यन्त पुण्यदायक नमस्कार है। जो दक्षयज्ञके विध्वंसक, जगत्‌के
- **Translation**: 

---

### Verse 7 (Bramha 0.3927)
- **Original**: जल॑ पातालगद्भामें जा मिला। इस प्रकार उन आदि विधाता तथा त्रिभुवनरूप हैं, उन भगवान्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.3928)
- **Original**: दोनोंका संगम हुआ। भगवान्‌ शेषेश्वरके सामने शिवको नमस्कार है। जिनके सहस्रों मस्तक हैं,
- **Translation**: 

---

### Verse 9 (Bramha 0.3929)
- **Original**: एक विशाल कुण्ड बनाकर शेषनागने उसमें उन भगवान्‌ सदाशिवकों नमस्कार है। सबका
- **Translation**: 

---

### Verse 10 (Bramha 0.3930)
- **Original**: हवन किया। उस कुण्डमें सदा अग्निदेव स्थित संहार करनेवाले रुद्रदेवको नमस्कार है। भगवन्‌!
- **Translation**: 

---

### Verse 11 (Bramha 0.3931)
- **Original**: रहते हैं। उसमें गज्जाके जलका संगम होनेसे आप सोम, सूर्य, अग्नि और जलरूप हैं; आपको
- **Translation**: 

---

### Verse 12 (Bramha 0.3932)
- **Original**: वह जल गरम हो गया। महायशस्वी शेषनाग नमस्कार है। जो सर्वदा सर्वस्बरूप और कालरूप
- **Translation**: 

---

### Verse 13 (Bramha 0.3933)
- **Original**: महादेवजीकी आराधना करके पुनः अपने अभीष्ट हैं, उन भगवान्‌ शिवकों नमस्कार है। सर्वेश्वर
- **Translation**: 

---

### Verse 14 (Bramha 0.3934)
- **Original**: स्थान रसातलमें चले गये। तबसे बह तीर्थ शंकर ! मेरी रक्षा कीजिये। सर्वव्यापी सोमेश्वर !
- **Translation**: 

---

### Verse 15 (Bramha 0.3935)
- **Original**: नागतीर्थ एबं शेषतीर्थके नामसे प्रसिद्ध हुआ। मेरी रक्षा कौजिये। जगन्नाथ ! आपको नमस्कार
- **Translation**: 

---

### Verse 16 (Bramha 0.3936)
- **Original**: वह सम्पूर्ण अभीष्ट बस्तुओंको देनेवाला, पवित्र है। मेरा मनोरथ पूर्ण कीजिये।' तथा रोग और दरिद्रताका नाशक है। उससे इस स्तुतिसे प्रसन्न होकर महेश्वरने नागराजको
- **Translation**: 

---

### Verse 17 (Bramha 0.3937)
- **Original**: आयु एवं लक्ष्मीकी भी प्राप्ति होती है। वह मनोवाज्छित वर दिया, जो देवताओंसे शत्रुता
- **Translation**: 

---

### Verse 18 (Bramha 0.3938)
- **Original**: पवित्र तीर्थ स्नान और दानसे मोक्ष देनेवाला है। रखनेवाले दैत्य, दानव तथा राक्षसोंके विनाशमें
- **Translation**: 

---

### Verse 19 (Bramha 0.3939)
- **Original**: जो मनुष्य इस प्रसज्ञका भक्तिपूर्वक श्रवण, पाठ सहायक था। भगवानने शेषनागको शूल देकर
- **Translation**: 

---

### Verse 20 (Bramha 0.3940)
- **Original**: अथवा मनन करता है, उसकी सब कामनाएँ कहा--' इससे अपने शत्रुओंका संहार करो।'
- **Translation**: 

---

