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

### Verse 1 (Vaivtpuran 24.7109)
- **Original**: होकर सो गया। तब राजाको निद्रित देखकर मुनिने कपिलाद्वारा दी गयी शक्ति और शस्त्रके मुनिने उसी क्षण अर्धचन्द्रद्मामा उस भूपालके बलसे राजाको शस्त्रहीन करके मूर्च्छित कर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 24.7110)
- **Original**: सारथि, रथ और धनुषबाणको छिल्न-भिन्न कर दिया। तब कमललोचन राजा कार्तवीर्य पुनः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 24.7111)
- **Original**: दिया। क्षुरप्रसे मुकुट, छत्र और कवच काट डाला होशमें आकर क्रोधपूर्वक मुनिके साथ लोहा लेने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 24.7112)
- **Original**: तथा भाँति-भाँतिके अस्त्र-प्रयोगसे उसके अस्त्र, लगा। उस नृपश्रेष्ठने समरभूमिमें आग्रेयास्त्रका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 24.7113)
- **Original**: तरकस और घोड़ोंकी ध्ज्जियाँ उड़ा दीं। फिर प्रयोग किया, तब मुनिने वारुणास्त्रद्वारा उसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 24.7114)
- **Original**: युद्धस्थलमें हँसते हुए मुनिने खेल-ही-खेलमें हँसते-हँसते शान्त कर दिया। फिर राजाने रणभूमिमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 24.7115)
- **Original**: नागास्त्रद्वारा राजाके सभी मन्त्रियोंकों बाँधकर कैद मुनिके ऊपर वारुणास्त्र फेंका, तब मुनिने लीलापूर्वक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 24.7116)
- **Original**: कर लिया; फिर लीलापूर्वक उत्तम मन्त्रका प्रयोग वायव्यास्त्रद्वारा उसे शान्त कर दिया। तब राजाने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 24.7117)
- **Original**: करके उस राजाको जगाया और उन बंधे हुए युद्धस्थलमें वायव्यास्त्र चलाया; मुनिने उसे उसी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 24.7118)
- **Original**: सभी मन्त्रियोंको उसे दिखाया। राजाको दिखाकर क्षण गान्धर्वास्त्रद्वारा निवारण कर दिया। फिर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 24.7119)
- **Original**: मुनिने तत्काल ही उन्हें बन्धन-मुक्त कर दिया नरेशने रणके मुहानेपर नागास्त्र छोड़ा, मुनिवरने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 24.7120)
- **Original**: और नरेशको आशीर्वाद देकर कहा--'राजन्‌! उसे हर्षपूर्वक तत्काल ही गारुड़ास्त्रद्वारा प्रतिहत
- **Translation**: 

---

### Verse 13 (Vaivtpuran 24.7121)
- **Original**: अब अपने घर जाओ ।' परंतु राजा क्रोधसे भरा कर दिया। तब नृपवरने, जो सैकड़ों सूर्योके हुआ था। उसने उठकर त्रिशूल उठा लिया और समान कान्तिमान्‌ एवं दसों दिशाओंको उद्दीप्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 24.7122)
- **Original**: यत्रपूर्वक उसे मुनिवर जमदग्रिपर चला दिया। तब करनेवाला था, उस माहे श्रर नामक महान्‌ अस्त्रका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 24.7123)
- **Original**: मुनिने उसपर शक्तिसे प्रहार किया। इसी बीच उस प्रयोग किया। नारद! तब मुनिने बड़े यत्रके साथ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 24.7124)
- **Original**: युद्धस्थलमें ब्रह्माने आकर उत्तम नीतिद्वारा उन त्रिलोकव्यापी दिव्य वैष्णवास्त्रद्ारा उसका निवारण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 24.7125)
- **Original**: दोनोंमें परस्पर प्रेम स्थापित करा दिया। तब मुनिने कर दिया और फिर यत्रपूर्वक नारायणास्त्र चलाया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 24.7126)
- **Original**: संतुष्ट होकर रणक्षेत्रमें ब्रह्माके चरणोंमें प्रणिपात उस अस्त्रकों देखकर महाराज कार्तवीर्य उसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 24.7127)
- **Original**: किया और राजा ब्रह्मा तथा मुनिको नमस्कार नमस्कार करके शरणागत हो गया। तब प्रलयाग्रिके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 24.7128)
- **Original**: करके अपने घरको प्रस्थान कर गया। फिर मुनि समान वह अस्त्र वहाँ ऊपर-ही-ऊपर घूमकर
- **Translation**: 

---

