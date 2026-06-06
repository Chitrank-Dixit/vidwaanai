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

### Verse 1 (Vaivtpuran 9.2276)
- **Original**: 3*-स्वरूपिणी ग्रन्थवीजस्वरूपा देवीके लिये वक्षःस्थलकी रक्षा करें। 3» हीं विद्यास्वरूपा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 9.2277)
- **Original**: श्रद्धाको आहुति दी जाती है, वे सब ओरसे मेरी देवीके लिये श्रद्धाकी आहुति दी जाती है, वे मेरी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 9.2278)
- **Original**: रक्षा करें। नाभिकी रक्षा करें। 5» हॉँ- क्लीं-स्वरूपिणी देवी विप्र ! यह सरस्वती-कवच तुम्हें सुना दिया। वाणीके लिये श्रद्धाकी आहुति दी जाती है, वे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 9.2279)
- **Original**: असंख्य ब्रह्ममन्त्रोंका यह मूर्तिमान्‌ विग्रह है। सदा मेरे हाथोंकी रक्षा करें। 3»-स्वरूपिणी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 9.2280)
- **Original**: ब्रह्मस्वरूप इस कबचको 'विश्वजय' कहते हैं। भगवती सर्ववर्णात्मिकाके लिये श्रद्धाकी आहुति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 9.2281)
- **Original**: प्राचीन समयकी बात है-गन्धमादन पर्वतपर दी जाती है, वे दोनों पैरोंकों सुरक्षित रखें। 3»
- **Translation**: 

---

### Verse 7 (Vaivtpuran 9.2282)
- **Original**: पिता धर्मदेवके मुखसे मुझे इसे सुननेका सुअवसर बागकी अधिष्ठात्री देवीके लिये श्रद्धाकी आहुति
- **Translation**: 

---

### Verse 8 (Vaivtpuran 9.2283)
- **Original**: प्राप्त हुआ था। तुम मेरे परम प्रिय हो। अतएव दी जाती है, वे मेरे सर्वस्वकी रक्षा करें। सबके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 9.2284)
- **Original**: तुमसे मैंने कहा है। तुम्हें अन्य किसीके सामने कण्ठमें निवास करनेवाली 3“स्वरूपा देवीके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 9.2285)
- **Original**: इसकी चर्चा नहीं करनी चाहिये। विद्वान्‌ पुरुषको लिये श्रद्धाकी आहुति दी जाती है, बे पूर्व दिशामें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 9.2286)
- **Original**: चाहिये कि बस्त्र, चन्दन और अलंकार आदि सदा मेरी रक्षा करें। जीभके अग्रभागपर विराजनेवालो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 9.2287)
- **Original**: सामानोंसे विधिपूर्वक गुरुकी पूजा करके दण्डकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 9.2288)
- **Original**: भांति जमीनपर पड़कर उन्हें प्रणाम करे। तत्पथ्चात्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 9.2289)
- **Original**: पुरुष भाषण करनेमें परम चतुर, कवियोंका सम्राट्‌ उनसे इस कवबचका अध्ययन करके इसे हृदयमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 9.2290)
- **Original**: और त्रैलोक्यविजयी हो सकता हैं। वह सबको धारण करे। पाँच लाख जप करनेके पश्चात्‌ यह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 9.2291)
- **Original**: जीतनेमें समर्थ होता है।* मुने! यह कवंच कवच सिद्ध हो जाता है। इस कवचके सिद्ध
- **Translation**: 

---

### Verse 17 (Vaivtpuran 9.2292)
- **Original**: कण्व-शाखाके अन्तर्गत है। अब स्तोत्र, ध्यान, हो जानेपर पुरुषकों बृहस्पतिके समान पूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 9.2293)
- **Original**: वन्दव और पूजाका विधान बताता हूँ, सुनो। योग्यता प्राप्त हो सकती है। इस कबचके प्रसादसे (अध्याय 4) 30000 करियर 9क्‍8200000 * ब्रह्मोचाच शूणु वत्स प्रवक्ष्याभि कबचं सर्वकामदम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 9.2294)
- **Original**: श्रुतिसारं श्रुतिसुखं श्रुत्युक्त॑ ब्रुतिपूजितम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 9.2295)
- **Original**: उक्त कृष्णेन गोलोके महां वन्दावने बने
- **Translation**: 

---

