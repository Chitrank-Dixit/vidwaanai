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

### Verse 1 (Vaivtpuran 35.7842)
- **Original**: जिसे धारण करके वामदेव, देवल, स्वयं च्यवन,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7843)
- **Original**: 372 + संक्षिप्त-ब्रह्मलैवर्तपुराण 4004 0 42020 । 2 0 20
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7844)
- **Original**: 0।0/ 4 /4/। ओह अगस्त्य और पुलस्त्य विश्ववन्द्य हो गये। '3&
- **Translation**: 

---

### Verse 4 (Vaivtpuran 35.7845)
- **Original**: 'भूतेश' मेरी रक्षा करें। अग्निकोणमें 'शंकर' रक्षा नम्त: शिवाय' यह सदा मेरे मस्तककी रक्षा करे।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 35.7846)
- **Original**: करें। दक्षिणमें 'रुद्र' तथा नैऋत्यकोणमें स्थाणु * 30 नमः शिवाय स्वाहा' यह सदा ललाटकी रक्षा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 35.7847)
- **Original**: मेरी रक्षा करें। पश्चिममें 'खण्डपरशु', वायव्यकोणमें करे। '30 हीं श्रीं क्लीं शिवाय स्वाहा' सदा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 35.7848)
- **Original**: 'चन्द्रशेखर', उत्तरमें 'गिरिश' और ईशानकोणमें नेत्रोंकी रक्षा करे। 3» हीं क्लीं हूं शिवाय नमः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 35.7849)
- **Original**: स्वयं “ईश्वर' रक्षा करें। ऊर्ध्वभागमें 'मृड़' और / मेरी नासिकाकी रक्षा करे। '47 नमः शिवाय
- **Translation**: 

---

### Verse 9 (Vaivtpuran 35.7850)
- **Original**: अधोभागमें स्वयं 'मृत्युझ्य' सदा रक्षा करें। शान्ताय स्वाहा' सदा कण्ठकी रक्षा करे। '3» हीं
- **Translation**: 

---

### Verse 10 (Vaivtpuran 35.7851)
- **Original**: जलमें, स्थलमें, आकाशमें, सोते समय अथवा श्रीं हूं संहारकत्रें स्वाहा ' सदा कानोंको रक्षा करे।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 35.7852)
- **Original**: जागते रहनेपर भक्तवत्सल 'पिनाकी' सदा मुझ * 3 हीं श्रीं पश्चवक्त्राय स्वाहा ' सदा दाँतकौ रक्षा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 35.7853)
- **Original**: भक्तकी स्रेहपूर्वक रक्षा करें। करे। ' 3» हीं महेशाय स्वाहा' सदा मेरे ओठकी वत्स! इस प्रकार मैंने तुमसे इस परम अद्भुत रक्षा करे। ' 30 हीं श्रीं क्लीं त्रिनेत्राय स्वाहा' सदा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 35.7854)
- **Original**: ककचका वर्णन कर दिया। इसके दस लाख केशोंकी रक्षा करे। “30 हीं ऐं महादेवाय स्वाहा' जपसे ही सिद्धि हो जाती है, यह निश्चित है। यदि सदा छातीकी रक्षा करे। '3» हीं श्रीं क्लीं ऐं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7855)
- **Original**: यह कवच सिद्ध हो जाय तो वह निश्चय ही रुद्र- रुद्राय स्वाहा' सदा नाभिकौ रक्षा करे। '3& हीं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7856)
- **Original**: तुल्य हो जाता है। वत्स! तुम्हारे स्रेहेके कारण ऐँ श्री ईश्वराय स्वाहा' सदा पृष्ठभागकी रक्षा करे।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7857)
- **Original**: मैंने वर्णन कर दिया है, तुम्हें इसे किसीको नहीं 7 हीं क्लीं मृत्युक्रयाय स्वाहा' सदा भौंहोंकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7858)
- **Original**: बतलाना चाहिये; क्योंकि यह काण्वशाखोक्त रक्षा करे। 50 हीं श्रीं क्‍्लीं ईशानाय स्वाहा' सदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7859)
- **Original**: कवच अत्यन्त गोपनीय तथा परम दुर्लभ है। पार््भागकी रक्षा करे। “3 हीं ईश्वराय स्वाहा' [सहस्नों अश्वमेध और सैकड़ों राजसूय-ये सभी सदा मेरे उदरकी रक्षा करे। '5» श्रीं क्लीं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7860)
- **Original**: इस कवचको सोलहवीं कलाकी समानता नहीं मृत्युझ्रयाय स्वाहा' सदा भुजाओंकी रक्षा करे।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7861)
- **Original**: कर सकते। इस कबचकी कृपासे मनुष्य निश्चय '30 हीं श्री क्लीं ईश्वराय स्वाहा' मेरे हाथोंकी
- **Translation**: 

---

