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

### Verse 1 (Vaivtpuran 27.4083)
- **Original**: मनुष्य ब्राह्मणको फलयुक्त वृक्ष प्रदान करता है, ब्राह्मणको दो पादुकाएँ प्रदान करता है, उसे दस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 27.4084)
- **Original**: वह फलके बराबर वर्षोतक इन्द्रलोकमें सम्मान हजार वर्षतक वायुलोकमें प्रतिष्ठा प्राप्त होती है।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 27.4085)
- **Original**: पाता है। फिर उत्तम योनिमें जन्म पाकर वह मनोहर दिव्य शब्या ब्राह्मणको देनेसे दीर्घकालतक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 27.4086)
- **Original**: सुयोग्य पुत्र प्राप्त करता है। फलवाले वृक्षोंके चन्द्रलोकमें प्रतिष्ठा होती है। जो देवताओं अथवा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 27.4087)
- **Original**: दानकी महिमा इससे हजारगुना अधिक बतायी *अन्नदानातू पर॑ दान॑ न भूत॑ न भविष्यति । नात्र पात्रपरीक्षा स्यात्न कालनियम: क़्चित्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 27.4088)
- **Original**: (प्रकृतिखण्ड 27। 3)
- **Translation**: 

---

### Verse 7 (Vaivtpuran 27.4089)
- **Original**: गयी है। अथवा ब्राह्मणको केवल फलका भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 27.4090)
- **Original**: पतिक्रते! जो पुरुष ब्राह्मणको जम्बूद्वीपका दान दान करनेवाला पुरुष दीर्घकालतक स्वर्गमें वास
- **Translation**: 

---

### Verse 9 (Vaivtpuran 27.4091)
- **Original**: करता है, उसे निश्चितरूपसे सौगुने फल प्राप्त करके पुनः भारतवर्षमें जन्म पाता है। होते हैं। जो सातों द्वीपोंकी पृथ्वीका दान भारतवर्षमें रहनेवाला जो पुरुष अनेक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 27.4092)
- **Original**: करनेवाले, सम्पूर्ण तीर्थोमें निवास करनेवाले, द्रव्योंसे सम्पन्न तथा भाँति-भाँतिके धान्योंसे भरे-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 27.4093)
- **Original**: समस्त तपस्याओंमें संलग्न, सम्पूर्ण उपवास-ब्रतके पूरे विशाल भवन ब्राह्मणको दान करता है, वह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 27.4094)
- **Original**: पालक, सर्वस्व दान करनेवाले तथा सस्पूर्ण उसके फलस्वरूप दीर्घकालतक कुबेरके लोकमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 27.4095)
- **Original**: सिद्धियोंके पारड्भरत तथा श्रीहरिके भक्त हैं, उन्हें वास पाता है। तत्पश्चात्‌ उत्तम योनिमें जन्म पाकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 27.4096)
- **Original**: पुनः जगत्‌में जन्म धारण करना नहीं पड़ता। वह महान्‌ धनवान्‌ होता है। साध्वि! हरी-भरी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 27.4097)
- **Original**: उनके सामने असंख्य ब्रह्माओंका पतन हो जाता खेतीसे युक्त सुन्दर भूमि भक्तिपूर्वक ब्राह्मणको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 27.4098)
- **Original**: है, परंतु वे श्रीहरिक गोलोक या बैकुण्ठधाममें अर्पण करनेवाला पुरुष निश्चयपूर्वक बैकुण्ठधाममें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 27.4099)
- **Original**: निवास करते रहते हैं। विष्णु-मन्त्रकी उपासना प्रतिष्ठित होता है। जो मानव उत्तम गोशाला तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 27.4100)
- **Original**: करनेवाले पुरुष अपने मानवशरीरका त्याग गाँव ब्राह्मणको दान करता है, उसकी बैकुण्ठलोकमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 27.4101)
- **Original**: करनेके पश्चात्‌ जन्म, मृत्यु एवं जरासे रहित दिव्य प्रतिष्ठा होती है। फिर, जहाँकी उत्तम प्रजाएँ हों,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 27.4102)
- **Original**: रूप धारण करके श्रीहरिका सारूप्य पाकर उनकी जहाँकी भूमि पकी हुई खेतियोंसे लहलहा रही
- **Translation**: 

---

