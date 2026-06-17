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

### Verse 1 (Vaivtpuran 32.7637)
- **Original**: कर रहे थे तथा “जय हो' ऐसा उच्चारण कर हूँ। फिर देखा कि मैं नदीतटपर बड़े-बड़े कमल-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.7638)
- **Original**: रहे थे। फिर परशुरामने स्वप्रमें सुधावृष्टि, पत्तोंकी पत्रोंपर रखकर दही, घी और मधु-मिश्रित खीर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.7639)
- **Original**: वर्षा, फलोंकी वृष्टि, लगातार होती हुई पुष्प और खा रहा हूँ। पुनः देखा कि मैं पान चबा रहा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.7640)
- **Original**: चन्दनकी वर्षा, तुरंतका काटा हुआ मांस, जीवित हूँ। मेरे सामने फल, पुष्प और दीपक रखे हुए
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.7641)
- **Original**: मछली, मोर, श्वेत खंजन, सरोवर, तीर्थ, कबूतर, हैं तथा ब्राह्मण मुझे आशीर्वाद दे रहे हैं। फिर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.7642)
- **Original**: शुक, नीलकण्ठ, सफेद चीौल, चातक, बाघ, अपनेको बारंबार पके हुए फल, दूध, शक्करमिश्रित सिंह, सुरभी, गोरोचन, हल्दी, सफेद धानका गरमा-गरम अन्न, स्वस्तिकके आकारकी बनी हुई
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.7643)
- **Original**: विशाल पर्वत, प्रज्वलित अग्नि, दूब, समूह-के- मिठाई खाते देखा। पुनः उन्होंने देखा कि मुझे [समूह देव-मन्दिर, पूजित शिवलिड्र और पूजा जल-जन्तु, बिच्छू, मछली तथा सर्प काट रहे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.7644)
- **Original**: की हुई शिवकी मृण्मयी मूर्तिकों देखा। परशुरामने हैं और मैं भयभीत होकर भाग रहा हूँ। फिर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.7645)
- **Original**: स्वप्रमें जौ और गेहूँके आटेकी पूड़ी और लड्डू देखा कि मैं चन्द्रमा और सूर्यका मण्डल, पति
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.7646)
- **Original**: देखा और उन्हें बारंबार खाया। फिर अकस्मात्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.7647)
- **Original**: + गणपंतिसाण्ड * 365 अभड 8 बछ श 9 9 8 88 88% 88 # 8 888 98 8884 ##4 4888 5 8 8 5 ## 444 44 #/44 484 4 8 6 58% 44 4 8 5 8 8 8 88 8 88. अपनेको शस्त्रसे घायल और जंजीरसे बंधा हुआ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.7648)
- **Original**: प्रातःकालिक नित्य कर्म सम्पन्न किया और देखकर उनकी नींद टूट गयी और बे प्रात:काल
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.7649)
- **Original**: मनमें ऐसा समझ लिया कि निश्चय ही सारे श्रीहरिका स्मरण करते हुए उठ बैठे। इस स्वप्रसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.7650)
- **Original**: शत्रुओंको जीत लूँगा। उन्हें अत्यन्त हर्ष हुआ। तत्पश्चात्‌ उन्होंने अपना (अध्याय 33) 0 परशुरामका कार्तवीर्यके पास दूत भेजना, दूतकी बात सुनकर राजाका युद्धके लिये उद्यत होना और रानी मनोरमासे स्वप्रदृष्ट अपशकुनका वर्णन करना, रानीका उन्हें परशुरामकी शरण ग्रहण करनेको कहना, परंतु राजाका मनोरमाको समझाकर युद्धयात्राके लिये उद्यत होना श्रीनारायण कहते हैं--नारद! तदनन्तर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.7651)
- **Original**: देना चाहते हैं। इस समाचारसे मेरे प्राण काँप भृगुवंशी परशुरामने प्रातःकालिक नित्यकर्म समाप्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.7652)
- **Original**: उठे हैं, मन बारंबार श्षुब्ध हो रहा है और मेरा करके भाई-बन्धुओंके साथ परामर्श किया और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7653)
- **Original**: बायाँ अद्भ निरन्तर फड़क रहा है। प्रिये! मैंने कार्तवीर्यके आश्रमपर दूत भेजा। उस दूतने शीघ्र ही
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7654)
- **Original**: एक स्वप्र भी देखा है, सुनो। जाकर राजाधिराज कार्तवीर्यसे कहा। उस समय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7655)
- **Original**: मैंने देखा है-मैं तेलसे सराबोर हूँ, लाल राजा मन्त्रियोंसे घिरे हुए राजसभामें बैठे थे। ।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7656)
- **Original**: वस्त्र धारण किये हुए हूँ, शरीरपर लाल चन्दन परशुरामका दूत बोला--महाग़ज ! नर्मदातटके
- **Translation**: 

---

