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

### Verse 1 (Vaivtpuran 67.6075)
- **Original**: तपकी फलस्वरूपा मायाको मैंने उन्हें प्रदान किया हर्षपूर्वक्क उस सभामें आये। फिर तो सुरेश्वरोंने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.6076)
- **Original**: है। मायारूपा पार्वतीका यह ब्रत लोकशिक्षाके उनकी स्तुति करना आरम्भ किया। तदनन्तर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.6077)
- **Original**: लिये ही है, अपने लिये नहीं है; क्योंकि जिनके चार भुजाएँ थीं; जो शक्ल, चक्र, गदा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.6078)
- **Original**: त्रिलोकौमें ब्रतों और तपस्याओंका फल देनेवाली और पद्म धारण किये हुए थे; जो लक्ष्मी और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.6079)
- **Original**: तो ये स्वयं ही हैं। इनकी मायासे सभी प्राणी सरस्वतीके स्वामी, शान्तस्वरूप, परम मनोहर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.6080)
- **Original**: मोहित हैं। फिर प्रत्येक कल्पमें पुन-पुनः इनके और सुखपूर्वक दर्शन करने योग्य थे, परंतु
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.6081)
- **Original**: स्तवन, न्रत और ब्रत-फलकी साधनासे क्‍या भक्तिहीनोंके लिये जिनका दर्शन करोड़ों जन्मोंमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.6082)
- **Original**: लाभ? देवताओंमें श्रेष्ठ जो ब्रह्मा, विष्णु और भी नहीं हो सकता; जिनके नील रंगकी आभा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.6083)
- **Original**: महेश्वर हैं, वे मेरे ही अंश हैं तथा जीवधारी प्राणी करोड़ों कामदेबोंकों मात कर रही थी; जिनका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.6084)
- **Original**: और देवता आदि मेरी ही कलाएँ तथा कलांशरूप प्रकाश करोड़ों चन्द्रमाओंके समान था; जो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.6085)
- **Original**: हैं। जैसे कुम्हार मिट्टीके बिना घटका निर्माण नहीं अमूल्य र्रोंद्वारा निर्मित सुन्दर भूषणोंसे विभूषित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.6086)
- **Original**: कर सकता तथा सोनार स्वर्णके बिना कुण्डल थे, जो ब्रह्मा आदि देवताओंद्वारा सेवनीय हैं,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.6087)
- **Original**: बनानेमें असमर्थ है, उसी तरह मैं भी शक्तिके भक्तगण सदा जिनका स्तबन करते हैं; जो अपने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.6088)
- **Original**: बिना अपनी सृष्टिकी रचना करनेमें असमर्थ हूँ। प्रकाशसे आच्छादित देवर्षियोंद्वारा घिरे हुए अतः सृष्टिके सृजनमें शक्तिकी ही प्रधानता थे--उन परमेश्वरको ब्रह्मा, विष्णु और शिव आदि
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.6089)
- **Original**: है--यह सभी दर्शनशास्त्रोंको मान्य है। मैं समस्त देवताओंने एक श्रेष्ठ रल्सिंहासनपर बैठाया और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.6090)
- **Original**: देहधारियोंका आत्मा, निर्लेप, अदृश्य और साक्षी सिर झुकाकर उन्हें प्रणाम किया। उस समय उन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.6091)
- **Original**: हूँ। प्रकृतिसे उत्पन्न सभी पाक्रभौतिक शरीर नश्वर सबकी अज्जलियाँ बँधी हुई थीं, शरीर रोमाश्चित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.6092)
- **Original**: हैं, परंतु सूर्यके समान प्रकाशमान शरीरवाला मैं थे और आँखोंमें आँसू छलक आये थे। तब
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.6093)
- **Original**: नित्य हूँ। जगत्‌में प्रकृति सबको आधारस्वरूपा परम बुद्धिमान्‌ भगवानने मुस्कराते हुए मधुर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.6094)
- **Original**: है और मैं सबका आत्मा हूँ। वेदमें ऐसा निरूपण बाणीद्वारा उनसे सारा वृत्तान्त पूछा और उनके
- **Translation**: 

---

