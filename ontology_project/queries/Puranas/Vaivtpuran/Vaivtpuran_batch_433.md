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

### Verse 1 (Vaivtpuran 23.1622)
- **Original**: हैं। पाद्य, अर्घ्य, आचमनीय, पुष्प और नैवेद्य-ये सम्पन्न हो वेदोक्त विधिसे इष्टदेवकी पूजा करे।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1623)
- **Original**: पाँच उपचार हैं। श्रेष्ठटटपत साधक मूलमन्त्रका शालग्राम-शिलामें, मणिमें, मन्त्रमें, प्रतिमामें, जलमें,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1624)
- **Original**: उच्चारण करके ये सभी उपचार अर्पित करें। थलमें, गायकी पीठपर अथवा गुरु एवं ब्राह्मणमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1625)
- **Original**: गुरुके उपदेशसे प्राप्त हुआ मूलमन्त्र समस्त कर्माँमें श्रीहरिकी पूजा कौ जाय तो वह उत्तम मानी जाती
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1626)
- **Original**: उत्तम माना गया है। पहले भूतशुद्धि करके फिर है। जो अपने सिरपर शालग्रामका चरणोदक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1627)
- **Original**: प्राणायाम करे। तत्पश्चात्‌ अड्जभन्यास, प्रत्यड्रन्यास, छिड़कता है, उसने मानो सम्पूर्ण तीथाँमें स्नान कर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1628)
- **Original**: मन्त्रन्यास तथा वर्णन्यासका सम्पादन करके अर्ध्यपात्र लिया और सम्पूर्ण यज्ञोंकी दीक्षा ग्रहण कर ली।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1629)
- **Original**: प्रस्तुत करे। पहले त्रिकोणाकार मण्डल बनाकर जो मनुष्य प्रतिदिन भक्तिभावसे शालग्राम-शिलाका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1630)
- **Original**: उसके भीतर भगवान्‌ कूर्म (कच्छप)-की पूजा जल (चरणामृत) पान करता है, वह जौीवन्मुक्त
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1631)
- **Original**: करें। इसके बाद द्विज शट्डुमें जल भरकर उसे होता है और अन्तमें श्रोकृष्णधामको जाता है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1632)
- **Original**: वहीं स्थापित करें। फिर उस जलकी बिधिवत्‌ नारद! जहाँ शालग्राम-शिलाचक्र विद्यमान है,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1633)
- **Original**: पूजा करके उसमें ती्थॉंका आवाहन करे। तदनन्तर वहाँ निश्चय ही चक्रसहित भगवान्‌ विष्णु तथा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1634)
- **Original**: उस जलसे पूजाके सभी उपचारोंका प्रक्षालन सम्पूर्ण तीर्थ विराजमान हैं। वहाँ जो देहधारी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1635)
- **Original**: करे। इसके बाद फूल लेकर पवित्र साधक जानकर, अनजानमें अथवा भाग्यवश मर जाता है,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1636)
- **Original**: योगासनसे बैठे और गुरुके बताये हुए ध्यानके वह दिव्य रज्रोंद्वारा निर्मित विमानपर बैठकर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1637)
- **Original**: अनुसार अनन्यभावसे भगवान्‌ श्रीकृष्णका चिन्तन श्रीहरिके धामको जाता है। कौन ऐसा साधुपुरुष
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1638)
- **Original**: करे। इस तरह ध्यान करके साधक मूलमन्त्रका है, जो शालग्राम-शिलाके सिवा और कहीं श्रीहरिका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1639)
- **Original**: उच्चारण करते हुए पाद्य आदि सब उपचार बारी- पूजन करेगा; क्योंकि शालग्राम-शिलामें श्रीहरिकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1640)
- **Original**: बारीसे आराध्यदेवको अर्पित करें। तन्त्रशास्त्रमे पूजा करनेपर परिपूर्ण फलकी प्राप्ति होती है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1641)
- **Original**: बताये हुए अड्भग-प्रत्यज्ञ देवताओंके साथ श्रीहरिकी पूजाके आधार (प्रतीक)-का वर्णन किया
- **Translation**: 

---

