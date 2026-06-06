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

### Verse 1 (Vaivtpuran 63.5560)
- **Original**: * प्रकृतिखप्ड + 287 कक कक ऋ्ऋ्ऋ्ऋ्ऋ्ऋ्ऋ्ऋऋ्ऋ ऋऋ्ऋऋऋऋऋऋऋ्#### बना रहता है। वैष्णवीदेवीकी पूजा करके विद्वान्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5561)
- **Original**: तदनन्‍्तर सोलह उपचार चढ़ाकर देवीकी पूजा पुरुष विष्णुलोकमें जाता है और माहेश्वरीकी पूजा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5562)
- **Original**: करे। सजल कुशसे त्रिकोण मण्डल बनाकर वहाँ करके वह शिवलोकको प्राप्त होता है। वेदोंमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5563)
- **Original**: धार्मिक पुरुष कच्छप, शेषनाग और पृथ्वीका सात्त्विकी, राजगसी और तामसीके भेदसे तीन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5564)
- **Original**: पूजन करे। मण्डलके भीतर ही तिपाई रखे और प्रकारकी देवीकी पूजा बतायी गयी है, जो क्रमश:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5565)
- **Original**: उसके ऊपर शद्भु। शट्गमें तीन भाग जल डालकर उत्तम, मध्यम और अधम है। सात्किकी पूजा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5566)
- **Original**: उसकी पूजा करे तथा उसमें गज्जा आदि तीर्थोका वैष्णबोंकी है, शाक्त आदि राजसी पूजा करते हैं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5567)
- **Original**: आवाहन करते हुए कहे-- और जो किसी मन्त्रकी दीक्षा नहीं ले सके हैं,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5568)
- **Original**: गड्ढे च यमुने चैव गोदावरि सरस्वति। ऐसे असत्‌ पुरुषोंकी पूजा तामसी कही गयी है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 63.5569)
- **Original**: नर्मदे सिन्धु काबेरि चद्भभागे च कौशिकि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 63.5570)
- **Original**: हक रे वजन गत गया है वजन पूजा जीवहत्यासे रहित और श्रेष्ठ है, वही
- **Translation**: 

---

### Verse 12 (Vaivtpuran 63.5571)
- **Original**: स्वर्णेखे कनखले पारिभद्रे च गण्डकि। सात्तविको एवं वैष्णवी मानी गयी है। श्वेतगड़े चत्धरेखे पम्पे चम्पे च गोमति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 63.5572)
- **Original**: बैष्णबीदेवोके बरदानसे गोलोकमें जाते हैं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 63.5573)
- **Original**: माहेश्वरी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 63.5574)
- **Original**: पद्माखति त्रिपर्णाशे विपाशे विरजे प्रभे। एबं राजसी पूजामें बलिदान होता है। शाक्त आदि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 63.5575)
- **Original**: शतहुदे चेलगड़े जलेउस्मिन्‌ संनिधिं कुरु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 63.5576)
- **Original**: राजस पुरुष उस पूजासे कैलासमें जाते हैं । किरात
- **Translation**: 

---

### Verse 18 (Vaivtpuran 63.5577)
- **Original**: - हे गड्जे! यमुने! गोदावरि! सरस्वति! नर्मदे! लोग तामसी पूजाद्वारा भूत-प्रेतोंकी आराधना
- **Translation**: 

---

### Verse 19 (Vaivtpuran 63.5578)
- **Original**: सिन्धु! काबेरि! चन्द्रभागे! कौशिकि! स्वर्णरेखे! करके नरकमें पड़ते हैं। माँ! तुम्हीं जगतके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 63.5579)
- **Original**: कनखले ! पारिभ्रे! गण्डकि! श्वेतगड़े ! चन्द्ररेखे! जीवॉको धर्म, अर्थ, काम और मोक्षरूप चारों
- **Translation**: 

---

