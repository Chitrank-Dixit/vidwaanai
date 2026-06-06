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

### Verse 1 (Vishnu Puran 0.2421)
- **Original**: 9 श्रीपराझ्र उकाच इति श्रुत्वा स दैत्येन्द्र: प्रासादशिखरे स्थित: । क्रोधान्धकारितमुखः प्राह दैतेयकिड्डूरान्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2422)
- **Original**: 10 हिरण्यकशिपुरुवाच दुरात्पा क्षिप्यतामस्मात्मासादाच्छतयोजनात्‌ । गिरिपृष्ठे पतत्वस्मिन्‌ शिलाभिन्नाड्संहति:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2423)
- **Original**: 11 ततस्ते चिक्षिपु: सर्वे बाल दैतेयदानवाः । पपात सोप्यध: क्षिप्तों हृदयेनोद्नहन्हरिम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2424)
- **Original**: 12 पतमान जगद्धात्री जगद्धातरि केझवे। भक्तियुक्ते दधारैनमुपसड्म्य मेदिनी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2425)
- **Original**: 13 ततो विस्मेक्य त॑ स्वस्थमविशीर्णास्थिपश्नरम्‌ । हिरण्यकहदिपु: प्राह शम्बरं मायिनां वरम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2426)
- **Original**: 14 हिरण्यकशिपुरुवाच नास्माभि: शक्‍्यते हन्तुमसो दुर्बुद्धबालक: । मायां वेत्ति भवांस्तस्मान्माययैन निषृदय
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2427)
- **Original**: 95 गअम्बर उवासच सूदयाम्येव दैत्वेच्र पश्य मायाव्ल्ल मम । सहस््रमत्र मायानां पश्य कोटिशतं तथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2428)
- **Original**: 16 औपयशर उकाच त्ततः स ससूजे मायां प्रह्मादे शम्बरोउसुरः । बिनाशमिचछन्दुर्बुद्धि: सर्वत्र समदर्शिनि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2429)
- **Original**: 27 प्रधम अंश 87 प्रकार कहा---
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2430)
- **Original**: “पिताजी ! मेरा यह प्रभाव न तो मन्त्रादिजनित है और न स्वाभात्रिक हो है, बल्कि जिस- जिसके इ्दयमें श्रोअच्युतभगवान्‌का निबास होता है उसके लिये यह सामान्य बात है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2431)
- **Original**: जो मनुष्य अपने समान दूसरोंका बुरा नहीं सोचता, हे तात ! कोई कारण न रहनेसे उसका भी कभी बुरा नहीं होता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2432)
- **Original**: जो मनुष्य सन, वचन या कर्मसे दूसरोंको कष्ट देता हैं उसके उस परपीडाकूप बीजसे ही उत्पन्न हुआ उसको अत्यन्त अशुभ फल मिलता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2433)
- **Original**: अपनेसहित समस्त प्राणियॉमें श्रीकशवको वर्तमान समझकर मैं न तो किसीका बुरा चाहता हूँ और न कहता या करता ही हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2434)
- **Original**: इस प्रकार सर्वत्र शुभचित्त होनेसे मुझको शारीरिक, मानसिक, दैविक अथना भौतिक दुःख किस प्रकार प्राप्त हो सकता है ?
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2435)
- **Original**: इसी प्रकार भगवानूकों सर्वभूतमय जानकर विद्वानोंको सभी प्राणियॉमें अविचल भक्ति (प्रेम) करनी चाहिये"
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2436)
- **Original**: श्रीपराशरजी बोले-- अपने महलकी अड्टाल्कापर जैठे हुए उस दैत्ययाजने यह सुनकर क्रोधान्ध हो अपने दैत्य-अनुचरोंसे कहा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2437)
- **Original**: हिरण्यकशिपु खोला--यह बड़ा दुरात्पा है, इसे इस सौ योजन ऊँचे महलसे गिरा दो, जिससे यह इस पर्वतके ऊपर गिरे और शिल्‍ल्लाओसे इसके अंग-ओग छिन्र-भिन्न हो जाये 11
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2438)
- **Original**: तब उन समस्त दैत्य और दानयोने उन्हें महललसे गिरा दिया और वे भी उनके ढकेल्नेसे हृदयमें श्रीतरिका स्मरण करते-करते नीचे गिर गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2439)
- **Original**: जगशत्कर्ता भगवान्‌ केशक्के परमभक्त प्रह्नदजीके गिरते समय उन्हें जगद्धात्री पृथिवीने निकट जाकर अपनी गोदमें ले ल्थ्या
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2440)
- **Original**: तब बिना किसी हड्डी-पसलीके टूटे उन्हें स्वस्थ देख देत्ययाज हिरण्यकदिपुने परमसायाबी हाम्बरासरसे कहा
- **Translation**: 

---

