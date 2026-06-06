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

### Verse 1 (Vishnu Puran 0.8221)
- **Original**: सत्यकर्मणस्त्वतिरथ:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8222)
- **Original**: यो गड्ढाड़तो मझ्नूषागतं पृथापविद्धं कर्ण पुत्रमबाप
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8223)
- **Original**: कर्णादवृषसेनः इत्येतदन्ता अड्डब॑ंइ्या:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8224)
- **Original**: अतश्च पुरुबंश श्रोतुमहसि
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8225)
- **Original**: तथा तितिक्षु नामक दो पुत्र हूए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8226)
- **Original**: उश्ञोनरके शिबि, नृग, नर, कृमि और वर्म नामक पाँच पुत्र हुए्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8227)
- **Original**: उनमेंसे शिक्रिकि पृषदर्थ, सुबीर, केकय और मद्रक--ये चार पुत्र थे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8228)
- **Original**: तितिक्षुका पुत्र रुदाद्रध हुआ। उसके हेम, हेमके सुतपा तथा सुतपाके बलि नामक पुत्र हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8229)
- **Original**: इस बलिके क्षेत्र (रानी) में दीर्घतमा नामक मुनिने अद्भ, वह, कर्ज, सुह्ा और पौण्डु नामक पाँच वाक्ेय क्षत्रिय उत्पन्न किये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8230)
- **Original**: इन बलिपुत्रोंकी सन्ततिके नामानुसार पाँच देशोंके भी ये ही नाम पढ़े
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8231)
- **Original**: इनमेंसे अज्गसे अनपान, अनपानसे दिविरथ, दिविरथसे घर्मरथ और धर्मरथसे चित्ररथका जन्म हुआ जिसका दूसरा नाम रोमपाद था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8232)
- **Original**: इस रोमपादके मित्र दशरथजो थे, अजके पुत्र दशरथजीने ग्रेमपादकों सन्तानहीन देखकर उन्हें पुत्रीरूपसे अपनी शाक्ता नामकी कन्या गोद दे दी थी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8233)
- **Original**: 15-- 18
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8234)
- **Original**: गेमपादका पूत्र चतुरेग था। चतुरंगके पृथुलाक्ष तथा पृथुल्क्षके चग्प नामक पुत्र हुआ जिसने चम्पा नामकी पुरी बसायी थी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8235)
- **Original**: अम्पके हर्यड्र नामक पुत्र हुआ, हर्यज़से भद्गरथ, भद्दरथसे बहद्गथ, बृहद्रथसे बृहत्कर्मा बृहत्कर्मासे बृहद्धानु, युहद्धानुसे खहत्पना, बृहन्मनासे जयद्रथका जन्म हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8236)
- **Original**: जबद्रथको ब्राह्मण और क्षत्रियके संसर्गसे उत्पन्न हुई पत्रीके गर्भसे विजय नामक पुत्रका जन्म हुआ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8237)
- **Original**: विजयके धृति नामक पुत्र हुआ, धृतिके धृतब्रत, घृतब्रतके सत्यकर्मा और सत्यकर्मके अतिरथका जप्म हुआ जिसने कि [ स्नानके लिये ] गड्जाजीमें जानेरर पिटारीमें रखकर पृथाद्वारा यहाये हुए कर्णको पुत्ररूपसे पाया था। इस कर्णका पुत्र वृषसेन था। बस, अज़्वंद्ा इतना हो है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8238)
- **Original**: 24--29
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8239)
- **Original**: इसके आगे पुरुबेशका जर्णन सुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8240)
- **Original**: जा अ 0 जि +--- इति श्रीविष्णुपुराणे चतुर्थेडशे अष्टादशोडध्यायः
- **Translation**: 

---

