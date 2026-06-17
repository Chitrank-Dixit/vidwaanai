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

### Verse 1 (Mahabharat 0.781)
- **Original**: स्वजन-सम्बन्धी आपस्प्रेगोंके पास धरोहरके रूपमें रखे हुए हैं, चलेंगे। जबसे हमें यह बात मालूम हुईं है कि दुर्योधन आदिने
- **Translation**: 

---

### Verse 2 (Mahabharat 0.781)
- **Original**: स्वजन-सम्बन्धी आपस्प्रेगोंके पास धरोहरके रूपमें रखे हुए हैं, चलेंगे। जबसे हमें यह बात मालूम हुईं है कि दुर्योधन आदिने
- **Translation**: 

---

### Verse 3 (Mahabharat 0.782)
- **Original**: उनके साथ श्रेमका व्यवहार करें। मैं आपल्ोगोंसे अपने बड़ी निर्दयतासे कपट-दयूतमें हराकर आपलोगोंको वनवासी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.782)
- **Original**: उनके साथ श्रेमका व्यवहार करें। मैं आपल्ोगोंसे अपने बड़ी निर्दयतासे कपट-दयूतमें हराकर आपलोगोंको वनवासी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.783)
- **Original**: हृदयकी सच्ची बात कह रहा हूँ। उन्र ल्लोगोंकी रक्षा ही सेरा बना दिया है, तबसे हमल्पेग बहुत भयभीत हो गये हैं। हमें
- **Translation**: 

---

### Verse 6 (Mahabharat 0.783)
- **Original**: हृदयकी सच्ची बात कह रहा हूँ। उन्र ल्लोगोंकी रक्षा ही सेरा बना दिया है, तबसे हमल्पेग बहुत भयभीत हो गये हैं। हमें
- **Translation**: 

---

### Verse 7 (Mahabharat 0.784)
- **Original**: सबसे बड़ा काम है। आपलोगोंके वैसा करनेसे मुझे बड़ा ऐसी अवस्थामें छोड़कर जाना उचित नहीं है। हम आपके
- **Translation**: 

---

### Verse 8 (Mahabharat 0.784)
- **Original**: सबसे बड़ा काम है। आपलोगोंके वैसा करनेसे मुझे बड़ा ऐसी अवस्थामें छोड़कर जाना उचित नहीं है। हम आपके
- **Translation**: 

---

### Verse 9 (Mahabharat 0.785)
- **Original**: सन्तोष होगा और मैं उसे अपना ही सत्कार समझुगा। सेबक, प्रेमी और हितैषी हैं। कहीं दुरात्मा दुर्योधनके कुराज्यमें
- **Translation**: 

---

### Verse 10 (Mahabharat 0.785)
- **Original**: सन्तोष होगा और मैं उसे अपना ही सत्कार समझुगा। सेबक, प्रेमी और हितैषी हैं। कहीं दुरात्मा दुर्योधनके कुराज्यमें
- **Translation**: 

---

### Verse 11 (Mahabharat 0.786)
- **Original**: जिस समय श्र्मराज युथ्िष्ठिरने अपनी प्रजासे यह बात हमारा सर्वनाश् न हो जाय। आप जानते ही हैं कि दुष्ट
- **Translation**: 

---

### Verse 12 (Mahabharat 0.786)
- **Original**: जिस समय श्र्मराज युथ्िष्ठिरने अपनी प्रजासे यह बात हमारा सर्वनाश् न हो जाय। आप जानते ही हैं कि दुष्ट
- **Translation**: 

---

### Verse 13 (Mahabharat 0.787)
- **Original**: कही, उस्त समय सब लोग बड़े आर्तस्वरसे 'हाय ! हाय !!' पुरुषोंके साथ रहनेमें क्या-क्या हानियाँ हैं और सत्पुस्णोके
- **Translation**: 

---

### Verse 14 (Mahabharat 0.787)
- **Original**: कही, उस्त समय सब लोग बड़े आर्तस्वरसे 'हाय ! हाय !!' पुरुषोंके साथ रहनेमें क्या-क्या हानियाँ हैं और सत्पुस्णोके
- **Translation**: 

---

### Verse 15 (Mahabharat 0.788)
- **Original**: पुकार उठे। पाण्डबोंके गुण, स्वभाव आदिका स्परण करके साथ रहनेमें क्या-क्या त्मभ हैं। जैसे सुगन्थित पुष्पोंके
- **Translation**: 

---

### Verse 16 (Mahabharat 0.788)
- **Original**: पुकार उठे। पाण्डबोंके गुण, स्वभाव आदिका स्परण करके साथ रहनेमें क्या-क्या त्मभ हैं। जैसे सुगन्थित पुष्पोंके
- **Translation**: 

---

### Verse 17 (Mahabharat 0.789)
- **Original**: उनकी आकुलूताकी सीमा न रही और वे इच्छा न रहतेपर भी संसर्गसे जल, तिरू और स्थान सुगन्धित हो जाते हैं वैसे ही
- **Translation**: 

---

### Verse 18 (Mahabharat 0.789)
- **Original**: उनकी आकुलूताकी सीमा न रही और वे इच्छा न रहतेपर भी संसर्गसे जल, तिरू और स्थान सुगन्धित हो जाते हैं वैसे ही
- **Translation**: 

---

### Verse 19 (Mahabharat 0.790)
- **Original**: पाण्डवोंके आप्रहसे लौट आये । ज़ब पुस्मन ल्हौट गये, तब मनुष्य भी धले-बुरेके संगके अनुसार भल्का-घुरा हो जाता है। दुष्टोंके संगसे मोहकी वृद्धि होती है और सत्पुरुषोके साथसे धर्मकी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.790)
- **Original**: पाण्डवोंके आप्रहसे लौट आये । ज़ब पुस्मन ल्हौट गये, तब मनुष्य भी धले-बुरेके संगके अनुसार भल्का-घुरा हो जाता है। दुष्टोंके संगसे मोहकी वृद्धि होती है और सत्पुरुषोके साथसे धर्मकी
- **Translation**: 

---

