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

### Verse 1 (Vaivtpuran 45.4501)
- **Original**: भगवान्‌ श्रीहरिकी उपासनाके अतिरिक्त सब भाँति साथ छोड़ देता है।' कुछ केवल विडम्बनामात्र है। मैंने तुम्हें यथार्थ नारद! ब्रह्माजीकी बात सुनकर मुनिवर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4502)
- **Original**: ज्ञानोपदेश कर दिया; क्‍योंकि स्वामी भी वही जरत्कारुने मन्त्र पढ़कर योगबलका सहारा ले
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4503)
- **Original**: कहलाता है, जो ज्ञान प्रदान कर दे। ज्ञानके देवी मनसाकी नाभिका स्पर्श कर दिया और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4504)
- **Original**: द्वारा बन्धनसे मुक्त करनेवाला *स्वामी' माना उससे कहा। जाता है और वही यदि बन्धनमें डालता है मुनिवर जरत्कारुने कहा--मनसे! इस
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4505)
- **Original**: तो “शत्रु' है। जो गुरु भगवान्‌ श्रीहरिमें भक्ति गर्भसे तुम्हें पुत्र होगा। वह पुत्र जितेन्द्रिय पुरुषोंमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4506)
- **Original**: उत्पन्न करनेवाला ज्ञान नहीं देता, उसे 'शिष्यघाती' श्रेष्ठ, धार्मिक, ब्रह्मज्ञानी, तेजस्वी, तपस्वी, यशस्वी,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4507)
- **Original**: कहते हैं; क्योंकि वह शिष्यकों बन्धनमुक्त नहीं गुणी, वेदबेत्ताओं, ज्ञानियों और योगियोंमें प्रमुख, कर सका। जो जननीके गर्भमें रहनेके क्लेशसे विष्णुधक्त तथा अपने कुलका उद्धारक होगा।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4508)
- **Original**: तथा यमयातनासे मुक्त नहीं कर सकता, उसे ऐसे सुयोग्य पुत्रके उत्पन्न होनेमात्रसे पितर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4509)
- **Original**: गुरु, तात और बान्धव कैसे कहा जाय ? भगवान्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.4510)
- **Original**: ] प्रकृतिखण्ड ] 243 अडहक कह 854 5 85 58 555 4 4 ह 5 5 5 हक 4 4 5 88 8 8 $ हर 5 85884 89999 88898 /6 882 44 4885 88489 8 88 8, श्रीकृष्णणा सनातन मार्ग परमानन्द-स्वरूप है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.4511)
- **Original**: इस प्रकार कहकर मनसादेवी अपने स्वामीके जो निरन्तर ऐसे मार्गका प्रदर्शन नहीं कराता,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.4512)
- **Original**: चरणोंमें पड़ गयी। वह मनुष्योंके लिये कैसा बान्धव है? अतः मुनिवर जरत्कारु कृपाके समुद्र थे। उन्होंने साध्वि! तुम निर्गुण एवं अच्युत ब्रह्म भगवान्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.4513)
- **Original**: कृपाके वशीभूत होकर क्षणभरके लिये उसे श्रीकृष्णी उपासना करो; इनकी उपासनासे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.4514)
- **Original**: अपनी गोदमें ले लिया। मुनिके नेत्रोंसे जलकी पुरुषोंके सारे कर्ममूल कट जाते हैं। प्रिये! मैंने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.4515)
- **Original**: ऐसी धारा गिरी कि वह साध्वी मनसा नहा उठी जो तुम्हारा त्याग कर दिया है, इस अपराधको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.4516)
- **Original**: तथा वियोग-भयसे कातर हुई मनसाने भी अपने क्षमा करो। साध्वी स्त्रियाँ क्षमापरायण होती हैं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4517)
- **Original**: आँसुओंसे मुनिके वक्ष:स्थलको भिगो दिया। सत्त्वगुणके प्रभावसे उनमें क्रोध नहीं रहता।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4518)
- **Original**: तत्पश्चात्‌ वे दोनों पति-पत्नी ज्ञानद्वारा शोकसे देवि! मैं तपस्या करनेके लिये पुष्करक्षेत्रमें जा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4519)
- **Original**: मुक्त हुए। रहा हूँ। तुम भी सुखपूर्वक यहाँसे जा सकती
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4520)
- **Original**: . तदनन्तर मुनिवर जरत्कारु परमात्मा भगवान्‌ हो; क्‍योंकि निःस्पृह पुरुषोंके लिये एकमात्र
- **Translation**: 

---

