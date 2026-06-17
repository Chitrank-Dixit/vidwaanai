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

### Verse 1 (Bramha 0.7561)
- **Original**: रहनेवाला), परिवेत्ता (बड़े भाईके ब्याहसे पहले धन, विद्या, स्वर्ग, मोक्ष, सुख तथा राज्य भी देते
- **Translation**: 

---

### Verse 2 (Bramha 0.7562)
- **Original**: ही विवाह कर लेनेबाला), परिवेदनिका (बड़ी हैं। पितरोंको पूर्वाह्की अपेक्षा अपराह्न अधिक प्रिय
- **Translation**: 

---

### Verse 3 (Bramha 0.7563)
- **Original**: बहिनके विवाहके पहले ही ब्याह करनेवाली है। घरपर आये हुए ब्राह्मणोंका स्वागतपूर्वक पूजन
- **Translation**: 

---

### Verse 4 (Bramha 0.7564)
- **Original**: स्त्री)-का पुत्र, शुद्रजातीय स्त्रीका स्वामी और करके उन्हें पवित्रयुक्त हाथसे आचमन करानेके
- **Translation**: 

---

### Verse 5 (Bramha 0.7565)
- **Original**: उसका पुत्र-ऐसे ब्राह्मण श्राद्ध-भोजनके अधिकारी पश्चात्‌ आसनोंपर बरिठाये; फिर विधिपूर्वक श्राद्ध
- **Translation**: 

---

### Verse 6 (Bramha 0.7566)
- **Original**: नहीं हैं। शूद्रीके पुत्नका संस्कार करानेवाला, करके उन श्रेष्ठ ब्राह्मणॉंकों भोजन करानेके पश्चात्‌
- **Translation**: 

---

### Verse 7 (Bramha 0.7567)
- **Original**: अविवाहित, जो दूसरेकी पत्नी रह चुकी हो, ऐसी भक्तिपूर्वक प्रणाम करे और प्रिय वचन कहकर
- **Translation**: 

---

### Verse 8 (Bramha 0.7568)
- **Original**: स्त्रीका पति, वेतन लेकर पढ़ानेवाला, वैसे गुरुसे विदा करे। दरवाजेतक उन्हें पहुँचानेके लिये पीछे-
- **Translation**: 

---

### Verse 9 (Bramha 0.7569)
- **Original**: पढ़नेवाला, सूतकके अन्नपर जीविका-निर्वाह पोछे जाय और उनकी आज्ञा लेकर लौंटे। तदनन्तर
- **Translation**: 

---

### Verse 10 (Bramha 0.7570)
- **Original**: करनेवाला, सोमरसका विक्रय करनेवाला, चोर, नित्य-क्रिया करे और अतिथियोंको भोजन कराये।
- **Translation**: 

---

### Verse 11 (Bramha 0.7571)
- **Original**: पतित, ब्याज लेकर खानेबाला, शठ, चुगलखोर, किन्हीं-किन्हीं श्रेष्ठ पुरुषोंका विचार है कि यह
- **Translation**: 

---

### Verse 12 (Bramha 0.7572)
- **Original**: बेदोंका त्याग करनेवाला, अग्निहोत्रका त्यागी, नित्यकर्म भी पितरोंके ही उद्देश्यसे होता है। दूसरे
- **Translation**: 

---

### Verse 13 (Bramha 0.7573)
- **Original**: राजाका पुरोहित, सेवक, विद्याहीन, ट्वेष रखनेवाला, लोगोंका कहना है कि इससे पितरॉका कोई सम्बन्ध
- **Translation**: 

---

### Verse 14 (Bramha 0.7574)
- **Original**: वृद्ध पुरुषोंसे शत्रुता रखनेवाला, दुर्धर्ष, क्रूर, मूढ़, नहीं है। शेष कार्य सदाकी भाँति करें। किन्हीं-
- **Translation**: 

---

### Verse 15 (Bramha 0.7575)
- **Original**: मन्दिरकी आयपर जीनेवाला, नक्षत्र बतानेवाला, किन्हींका मत है कि पितरोंके लिये पृथक्‌ पाक
- **Translation**: 

---

### Verse 16 (Bramha 0.7576)
- **Original**: बाण बनानेवाला और यज्ञके अनधिकारी पुरुषोंसे बनाकर श्राद्ध करना चाहिये। कुछ लोगोंका विचार
- **Translation**: 

---

### Verse 17 (Bramha 0.7577)
- **Original**: यज्ञ करानेवाला-ये तथा अन्य जितने भी निन्दित है कि ऐसा न करके पहले बने हुए पाकसे ही अन्न
- **Translation**: 

---

### Verse 18 (Bramha 0.7578)
- **Original**: और अधम ब्राह्मण हैं, उन्हें श्राद्धमें सम्मिलित न लेकर सब कार्य पूर्ववत्‌ करना चाहिये। करे; क्‍योंकि वे पंक्तिको दूषित करनेवाले हैं। तदनन्तर श्राद्धकर्ता मनुष्य अपने भृत्य आदिके
- **Translation**: 

---

### Verse 19 (Bramha 0.7579)
- **Original**: जहाँ दुष्ट पुरुषोंका आदर और साधु पुरुषोंकी साथ अवशिष्ट अन्न भोजन करे। धर्मज्ञ पुरुषको
- **Translation**: 

---

### Verse 20 (Bramha 0.7580)
- **Original**: अवहेलना होती हो, वहाँ देवताओंका दिया हुआ इसी प्रकार एकाग्रचित्त होकर पितरोंका श्राद्ध
- **Translation**: 

---

