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

### Verse 1 (Vaivtpuran 17.1014)
- **Original**: स्थान मदिरापात्रकी भाँति अपवित्र माना जाता होता है, तब परमात्मा विष्णुके नेत्रकी एक पलक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.1015)
- **Original**: है। वहाँ जाकर यदि भगवज्निन्दा सुनी गयी तो गिरती है। मैं परमात्मा श्रीकृष्णकी एक श्रेष्ठ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.1016)
- **Original**: सुननेवाला प्राणी निश्चय ही नरकमें पड़ता है। कलामात्र हूँ। अत: उनकी महिमाका पार कौन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.1017)
- **Original**: ब्रह्माजीने पूर्वकालमें विष्णु-निन्दाके तीन भेद पा सकता है? मैं तो कुछ भी नहीं जानता।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.1018)
- **Original**: बताये थे। एक तो वह जो परोक्षमें निन्दा करता शौनक! ऐसा कहकर भगवान्‌ शंकर वहाँ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.1019)
- **Original**: है, दूसरा वह जो श्रीहरिको मानता ही नहीं है चुप हो गये। तब समस्त कर्मोंके साक्षी धर्मने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.1020)
- **Original**: तथा तीसरी कोटिका निन्दक वह ज्ञानहीन नराधम अपना प्रवचन आरम्भ किया। है, जो दूसरे देवताओंके साथ उनकी तुलना करता धर्म बोले--जिनके हाथ-पैर तथा सबको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.1021)
- **Original**: है। सौ ब्रह्माओंकी आयुपर्यन्त उस निन्‍्दकका देखनेवाले नेत्र सर्वत्र विद्यमान हैं; जो सबके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.1022)
- **Original**: नरकसे उद्धार नहीं होता। जो नराधम गुरु एवं अन्तरात्मारूपसे प्रत्यक्ष हैं, तथापि दुरात्मा पुरुष
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.1023)
- **Original**: पिताकी निन्‍दा करता है, वह चन्द्रमा और सूर्यकी जिन्हें नहीं देख या समझ पाते; उन सर्वव्यापी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.1024)
- **Original**: स्थितिपर्यन्त कालसूत्र नरकमें पड़ा रहता है। प्रभुके सब देशकाल और बस्तुओंमें विद्यमान
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.1025)
- **Original**: भगवान्‌ विष्णु तीनों लोकॉमें सबके गुरु, पिता, होनेपर भी जो तुमने यह कहा कि 'अभीतक
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.1026)
- **Original**: ज्ञानदाता, पोषक, पालक, भयसे रक्षक तथा भगवान्‌ विष्णु इस सभामें नहीं आये', ऐसा किस
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.1027)
- **Original**: वरदाता हैं। बुद्धिसे निश्चय किया? तुम्हारी बात सुनकर इन तीनोंकी बात सुनकर बे ब्राह्मणशिरोमणि मुनियोंकों भी मतिभ्रम हो सकता है। जहाँ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.1028)
- **Original**: हँसने लगे। फिर उन देवताओंसे मधुर वाणीमें महापुरुषकी निन्‍दा होती हो, वहाँ साधु पुरुष
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.1029)
- **Original**: बोले। उस निन्दाकों नहीं सुनते; क्योंकि निन्दक ब्राह्मणने कहा--हे धर्मशाली देवताओं! श्रोताओंके साथ ही कुम्भीपाक नरकमें जाता है
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.1030)
- **Original**: मैंने भगवान्‌ विष्णुकी क्‍या निन्‍्दा की है? श्रीहरि और वहाँ एक युगतक कष्ट भोगता रहता है। यहाँ नहीं आये इसलिये आकाशवाणीकी बात यदि दैवबश महापुरुषोंकी निन्‍दा सुनायी पड़ जाय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.1031)
- **Original**: व्यर्थ हो गयी, यही तो मैंने कहा है। देवेश्वरो! तो दिद्वानू पुरुष श्रीविष्णुका स्मरण करनेपर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.1032)
- **Original**: धर्मके लिये सच बोलो। जो सभामें बैठकर समस्त पापोंसे मुक्त होता और दुर्लभ पुण्य पाता
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.1033)
- **Original**: पक्षपात करते हैं वे अपनी सौ पीढ़ियोंका नाश है। जो इच्छा या अनिच्छासे भी भगवान्‌ विष्णुकी
- **Translation**: 

---

