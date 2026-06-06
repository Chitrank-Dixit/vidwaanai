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

### Verse 1 (Vaivtpuran 66.5706)
- **Original**: दुरत्यया में माया त्व॑ं यया सम्मोहितं जगत्‌। यया मुग्धो हि विद्वांश्व॒ मोक्षमार्ग न पश्यति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 66.5707)
- **Original**: इत्यात्मना कृतं स्तोत्र दुर्गाया दुर्गनाशनम्‌। पूजाकाले पठेद्यो हि सिद्धिर्भवति वाउिछता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 66.5708)
- **Original**: (प्रकृतिखण्ड 66। 7-26)
- **Translation**: 

---

### Verse 4 (Vaivtpuran 66.5709)
- **Original**: श्रीकृष्ण बोले--देवि ! तुम्हीं सबकी जननी,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 66.5710)
- **Original**: तुम्हीं हो। तुम्हीं समस्त लोकोंके लिये भय उत्पन्न मूलप्रकृति ईश्वरी हो। तुम्हीं सृष्टिकार्यमें आद्याशक्ति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 66.5711)
- **Original**: करती हो। गाँव-गाँवमें ग्रामदेवी और घर-घरमें हो। तुम अपनी इच्छासे त्रिगुणमयी बनी हुई हो।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 66.5712)
- **Original**: गृहदेवी भी तुम्हीं हो। तुम्हीं सत्पुरुषोंकी कीर्ति कार्यवश सगुण रूप धारण करती हो। वास्तवमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 66.5713)
- **Original**: और प्रतिष्ठा हो। दुष्टोंकी होनेवाली सदा निन्‍्दा स्वयं निर्गुणा हो। सत्या, नित्या, सनातनी एवं
- **Translation**: 

---

### Verse 9 (Vaivtpuran 66.5714)
- **Original**: भी तुम्हारा ही स्वरूप है। तुम महायुद्धमें परब्रह्मस्वरूपा हो, परमा तेज:स्वरूपा हो। भक्तोंपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 66.5715)
- **Original**: दुष्टसंहाररूपिणी महामारी हो और शिष्ट पुरुषोंके कृपा करनेके लिये दिव्य शरोर धारण करती हो।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 66.5716)
- **Original**: लिये माताकी भाँति हितकारिणी एवं रक्षारूपिणी तुम सर्वस्वरूपा, सर्वेश्वरी, सर्वाधारा, परात्परा,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 66.5717)
- **Original**: हो। ब्रह्मा आदि देवताओंने सदा तुम्हारी बन्दना, सर्वबीजस्वरूपा, सर्वपूज्या, निराश्रया, सर्वज्ञा,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 66.5718)
- **Original**: पूजा एवं स्तुति की है। ब्राह्मणोंकी ब्राह्मणता और सर्वतोभद्रा (सब ओरसे मज़जलमयी),
- **Translation**: 

---

### Verse 14 (Vaivtpuran 66.5719)
- **Original**: तपस्वीजनोंकी तपस्या भी तुम्हीं हो, विद्वानोंकी सर्वमड्गलमड़ला, सर्वबुद्धिस्वरूपा, सर्वशक्तिरूपिणी,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 66.5720)
- **Original**: विद्या, बुद्धिमानोंकी बुद्धि, सत्पुरुषोंकी मेधा और सर्वज्ञानप्रदा देवी, सब कुछ जाननेवाली और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 66.5721)
- **Original**: स्मृति तथा प्रतिभाशाली पुरुषोंकी प्रतिभा भी सबको उत्पन्न करनेवाली हो। देवताओंके लिये
- **Translation**: 

---

### Verse 17 (Vaivtpuran 66.5722)
- **Original**: तुम्हाशा ही स्वरूप है। राजाओंका प्रताप और ह॒विष्य दान करनेके निमित्त तुम्हीं स्वाहा हो,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 66.5723)
- **Original**: वैश्योंका वाणिज्य भी तुम्हीं हो। विश्वपूजिते! पितरोंके लिये श्राद्ध अर्पण करनेके निमित्त तुम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 66.5724)
- **Original**: सृष्टिकालमें सृष्टिरूपिणी, पालनकालमें रक्षारूपिणी स्वयं ही स्वधा हो, सब प्रकारके दानयज्ञमें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 66.5725)
- **Original**: तथा संहारकालमें विश्वका विनाश करनेवाली दक्षिणा हो तथा सम्पूर्ण शक्तियाँ तुम्हारा ही
- **Translation**: 

---

