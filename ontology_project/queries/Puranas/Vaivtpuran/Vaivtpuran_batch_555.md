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

### Verse 1 (Vaivtpuran 39.8119)
- **Original**: खड़े हुए। उस समय उनके सारे अड्र घायल लेकर बैकुण्ठको चले गये, तब भूगुनन्दन हो गये थे। राजाके बाणसमूहसे आच्छादित परशुरामने पुत्रसहित राजा *सहस्ताक्षपर प्रहार
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8120)
- **Original**: होनेके कारण शस्त्रधारियोंमें श्रेष्ठ परशुरामको किया। यद्यपि राजा कबचहीन था तथापि वह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8121)
- **Original**: अपनी तथा राजाकी सेना ही नहीं दीख रही प्रयत्नपूर्वक ब्रह्मास्त्रद्वारा एक सप्ताहतक युद्ध करता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8122)
- **Original**: थी। फिर तो परस्पर घोर दिव्यास्त्रोंका प्रयोग रहा। अन्ततोगत्वा पुत्रसहित धराशायी हो गया।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8123)
- **Original**: होने लगा। अन्तमें राजाने दत्तात्रेयके दिये हुए सहस्लाक्षेके गिर जानेपर महाबली कार्तवीर्यार्जुन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8124)
- **Original**: अमोघ शूलकों यथाविधि मन्त्रोंका पाठ करके दो लाख अक्षौहिणी सेनाके साथ स्वयं युद्ध
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8125)
- **Original**: परशुरामपर छोड़ दिया। उस सैकड़ों सूर्योंके करनेके लिये आया। वह रल्ननिर्मित खोलसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8126)
- **Original**: समान प्रभाशाली एवं प्रलयाग्रिकी शिखाके सदृश आच्छादित स्वर्णमय रथपर सवार हो अपने चारों शूलके लगते ही परशुराम धराशायी हो गये। ओर नाना प्रकारके अस्त्रोंको सुसज्जित करके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8127)
- **Original**: तदनन्तर भगवान्‌ शिवने वहाँ आकर परशुरामको रणके मुहानेपर डटकर खड़ा हो गया। परशुरामने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8128)
- **Original**: पुनर्जीवन दान दिया। इसी समय वहाँ युद्धस्थलमें राजरजेश्वर कार्तवीर्यको समरभूमिमें उपस्थित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8129)
- **Original**: भक्तवत्सल कृपालु भगवान्‌ दत्तात्रेय शिष्यकी रक्षा देखा। वह रज्ननिर्मित आभूषणोंसे सुशोभित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8130)
- **Original**: करनेके लिये आ पहुँचे। फिर परशुरामने क्रुद्ध करोड़ों राजाओंसे घिरा हुआ था। रत्ननिर्मित छत्र
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8131)
- **Original**: होकर पाशुपतास्त्र हाथमें लिया; परंतु दत्तात्रेयकी उसकी शोभा बढ़ा रहा था। वह रत्नोंके गहनोंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8132)
- **Original**: दृष्टि पड़नेसे वे रणभूमिमें स्तम्भित हो गये। तब विभूषित था। उसके सर्वाज्गञमें चन्दनकी खौर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8133)
- **Original**: रणके मुहानेपर स्तम्भित हुए परशुरामने देखा कि लगी हुई थी। उसका रूप अत्यन्त मनोहर था
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8134)
- **Original**: जिनके शरीरकी कान्ति नूतन जलधरके सदृश और वह मन्द-मन्द मुस्करा रहा था। राजा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8135)
- **Original**: है; जो हाथमें वंशी लिये बजा रहे हैं; सैकड़ों मुनिवर परशुरामको देखकर रथसे उतर पड़ा और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8136)
- **Original**: गोप जिनके साथ हैं; जो मुस्कराते हुए प्रज्वलित उन्हें प्रणाम करके पुनः रथपर सवार हो राज-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8137)
- **Original**: सुदर्शन चक्रको निरन्तर घुमा रहे हैं और अनेकों समुदायके साथ सामने खड़ा हुआ। तब परशुरामने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8138)
- **Original**: पार्षदोंसे घिरे हुए हैं एवं ब्रह्मा, विष्णु और महे श्वर राजाको समयोचित शुभाशीर्वाद दिया और पुन:
- **Translation**: 

---

