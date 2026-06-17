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

### Verse 1 (Vaivtpuran 4.8476)
- **Original**: तुम्हीं शिवके समीप शिवा (पार्वती), मन्द मुस्कान थी। अहो ! तुम्हारी मूर्ति बड़ी सुन्दर नारायणके निकट लक्ष्मी और ब्रह्माकी प्रिया थी, उसका वर्णन करना कठिन है। तुम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8477)
- **Original**: वेदजननी सावित्री और सरस्वती हो। जो मुमुक्षुओंको मोक्ष प्रदान करनेवाली तथा स्वयं
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8478)
- **Original**: परिपूर्णतम एवं परमानन्दस्वरूप हैं, उन रासेश्वर महाविष्णुकी विधि हो। बाले ! तुम सबको मोहित
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8479)
- **Original**: श्रीकृष्णकी: तुम परमानन्दरूपिणी राधा हो। कर लेनेवाली हो। तुम्हें देखकर श्रीकृष्ण उसी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8480)
- **Original**: देवाज्ननाएँ भी तुम्हारे कलांशकी अंशकलासे क्षण मोहित हो गये। तब तुम उनसे सम्भावित
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8481)
- **Original**: प्रादुर्भूत हुई हैं। सारी नारियाँ तुम्हारी विद्यास्वरूपा होकर सहसा मुस्कराती हुई भाग चलीं। इसी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8482)
- **Original**: हैं और तुम सबकी कारणरूपा हो। अम्बिके ! कारण सत्पुरुष तुम्हें 'मूलप्रकृति' ईश्वरी राधा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8483)
- **Original**: सूर्यकी पत्नी छाया, चन्द्रमाकी भार्या सर्वमोहिनी कहते हैं। उस समय सहसा श्रीकृष्णने तुम्हें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8484)
- **Original**: रोहिणो, इन्द्रकी पत्नी शची, कामदेवकी पत्नी बुलाकर वीर्यका आधान किया। उससे एक महान्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8485)
- **Original**: ऐश्वर्यशशालिनी रति, वरुणकी पत्नी वरुणानी, डिम्ब उत्पन्न हुआ। उस डिम्बसे महाविराट्की
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8486)
- **Original**: वायुकी प्राणप्रिया स्त्री, अग्निकी प्रिया स्वाहा, उत्पत्ति हुई, जिसके रोमकूपोंमें समस्त ब्रह्माण्ड
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8487)
- **Original**: कुबेरकी सुन्दरी भार्या, यमकी पत्नी सुशौला, स्थित हैं। फिर राधाके श्रृड्रारक्रमसे तुम्हारा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8488)
- **Original**: नैक्रतकी जाया कैटभी, ईशानकी पत्नी शशिकला,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8489)
- **Original**: 3. « संक्षिप्त ्रह्मवैवर्तपुराण «» ऋ##&##% # कक ऊ कक ## # क़# # # कक ऋकऋकऋऋ# # 68 8 #% #ऋऋऋऊऋ कक # 6662 555555%####%#0# # मनुकी प्रिया शतरूपा, कर्दमकी भार्यां देवहूति,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8490)
- **Original**: वृषरूपधारी विष्णुद्वारा उठाये गये स्वयं शम्भुने वसिष्ठकी पत्नी अरुन्धती, देवमाता अदिति,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8491)
- **Original**: त्रिपुरका संहार किया था; उन दुर्गाकों मैं अभिवादन अगस्त्य मुनिकी प्रिया लोपामुद्रा, गौतमकी पत्नी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8492)
- **Original**: करता हूँ। जिनकी आज्ञासे निरन्तर वायु बहती है, अहल्या, सबकी आधाररूपा वसुन्धरा, गद्जा,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8493)
- **Original**: सूर्य तपते हैं, इन्द्र वर्षा करते हैं और अग्नि जलाती तुलसी तथा भूतलकी सारी श्रेष्ठ सरिताएँ--ये
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8494)
- **Original**: है; उन दुर्गाको मैं सिर झुकाता हूँ। जिनकी सभी तथा इनके अतिरिक्त जो अन्य स््रियाँ हैं, ,आज्ञासे काल सदा वेगपूर्वक चक्कर काटता रहता वे सभी तुम्हारी कलासे उत्पन्न हुई हैं। है और मृत्यु जीव-समुदायमें विचरती रहती है; तुम मनुष्योंके घरमें गृहलक्ष्मी, राजाओंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8495)
- **Original**: उन दुर्गको मैं नमस्कार करता हूँ। जिनके भवनोंमें राजलक्ष्मी, तपस्वियोंकी तपस्या और
- **Translation**: 

---

