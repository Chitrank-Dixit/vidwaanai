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

### Verse 1 (Vaivtpuran 13.11982)
- **Original**: काल हैं। मैं संकटके समुद्रमें पड़ा हूँ। मेरी रक्षा मेरे आशीर्वादसे इसका महान्‌ भय दूर हो जाय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11983)
- **Original**: कीजिये। आप संहारकर्ताके भी संहारक, सर्वे श्वर और यह शीघ्र ही संतापसे छूट जाय। और सर्वकारण हैं। महाविष्णुरूपी वृक्षके बीज कृपापूर्वक ऐसा कहकर पार्वती और शिव
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11984)
- **Original**: हैं। प्रभो! इस भवसागरसे मेरी रक्षा कीजिये। चुप हो गये। मुनिने उन्हें प्रणाम करके देवेश्वर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11985)
- **Original**: शरणागत एवं शोकाकुल जनोंका भय दूर करके वैकुण्ठनाथकी शरण ली। मनके समान तीक्र
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11986)
- **Original**: उनकी रक्षामें लगे रहनेवाले भगबन्‌! मुझ भयभीतका गतिसे चलनेवाले मुनीश्वर दुर्वासा बैकुण्ठभवनमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11987)
- **Original**: उद्धार कौजिये। नारायण! आपको नमस्कार है। जाकर सुदर्शनकों अपने पीछे-पीछे आते देख
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11988)
- **Original**: वेदोंमें जिन्हें आदिसत्ता कहा गया है, वेद भी श्रीहरिके अन्तःपुरमें घुस गये। वहाँ ब्राह्मणने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11989)
- **Original**: जिनकी स्तुति नहीं कर सकते और सरस्वती भी श्रीनारायणदेवके दर्शन किये। वे रत्नमय सिंहासनपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11990)
- **Original**: जिनके स्तवनमें जडवत्‌ हो जाती हैं; उन्हीं विराजमान थे। उनके हाथोंमें शह्भु, चक्र, गदा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11991)
- **Original**: प्रभुकी दूसरे विद्वान्‌ क्या स्तुति कर सकते हैं? और पद्म शोभा पाते थे। उन परम प्रभुने पीताम्बर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11992)
- **Original**: शेष सहस्र मुखोंसे जिनकी स्तुति करनेमें जडभावकों धारण कर रखा था। उनके चार भुजाएँ थीं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11993)
- **Original**: प्राप्त होते हैं, पक्ममुख महादेव और चतुर्मुख ब्रह्मा अज्जकान्ति श्याम थी। वे शान्त-स्वरूप लक्ष्मी-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11994)
- **Original**: भी जडीभूत हो जाते हैं, श्रुतियाँ, स्मृतिकार और कान्त अपने दिव्य सौन्दर्यसे मनको मोह लेते
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11995)
- **Original**: वाणी भी जिनकी स्तुतिमें अपनेको असमर्थ पाती थे। रत्रमय अलंकारोंकी शोभा उन्हें और भी श्री-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11996)
- **Original**: हैं; उन्हींका स्तवन मुझ-जैसा ब्राह्मण कैसे कर सम्पन्न बना रही थी। गलेमें रत्मयी मालासे वे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11997)
- **Original**: सकता है? मानद! मैं बेदोंका ज्ञाता कया हूँ, विभूषित थे। उनके प्रसन्न मुखपर मन्द हास्यकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11998)
- **Original**: वेदवेत्ता विद्वानोंका शिष्य हूँ। मुझमें आपकी स्तुति छटा छा रही थी। वे भक्तोंपर अनुग्रह करनेके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11999)
- **Original**: करनेकी कया योग्यता है? अट्टाईसवें मनु और लिये कातर दिखायी देते थे। उत्तम रत्रोंके सार-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12000)
- **Original**: महेन्द्रके समाप्त हो जानेपर जिनका एक दिन- तत्त्वसे निर्मित मुकुट धारण करके उनका मस्तक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12001)
- **Original**: रातका समय पूरा होता है, वे विधाता अपने वर्षसे अनुपम ज्योतिसे जगमगा रहा था। श्रेष्ठ पार्षदगण
- **Translation**: 

---

