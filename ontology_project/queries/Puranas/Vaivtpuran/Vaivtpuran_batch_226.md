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

### Verse 1 (Vaivtpuran 13.10662)
- **Original**: सब-के-सब संगीतकी तानमें तत्पर थे। राधिकाकी मुने! श्रीराधाकी जो सुशीला आदि सहेली
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10663)
- **Original**: दूसरी-दूसरी दासियाँ बहुत बड़ी संख्यामें यात्रा गोषियाँ थीं, वे नाना प्रकारके अलंकारोंसे विभूषित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10664)
- **Original**: कर रही थीं, उनके मनमें बड़ा उल्लास था। मुखपर हो बड़ी भव्य दिखायी देती थीं। दिव्य वस्त्र धारण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10665)
- **Original**: मन्द मुस्कानकी छटा छा रही थी और वे सब- कर हर्षसे मुस्कराती हुई वे सव-की-सब वृन्दावनकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10666)
- **Original**: की-सब सोनेके गहनोंसे सजी थीं। उनमेंसे ओर चलीं। कोई शिबिकापर सवार थीं तो कोई
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10667)
- **Original**: कितनोंके हाथमें सिन्दूर थे, कितनी ही काजल रथपर। राधिकादेवी रलमय अलंकारोंसे विभूषित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10668)
- **Original**: लेकर चल रही थीं। किन्हींके हाथोंमें कन्दुक थे हो सुवर्णमय उपकरणोंसे युक्त रथपर बैठकर उन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10669)
- **Original**: तो किन्हींके पुतलियाँ। कुछ सुन्दरी दासियाँ अपने सब सहेलियोंके साथ यात्रा कर रही थीं। यशोदा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10670)
- **Original**: हाथोंमें भोग-द्रव्य और क्रीड़ा-द्रव्य लेकर चल और रोहिणीजी भी रत्नमय अलंकारोंसे अलंकृत
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10671)
- **Original**: रही थीं। किन्हींके हाथोंमें वेघरचनाकी सामग्री थी हो सुवर्णमय उपकरणोंसे सुसज्जित रथपर चढ़कर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10672)
- **Original**: तो किन्हींके हाथोंमें फूलोंकी मालाएँ। कुछ जा रही थीं। नन्‍्द, सुननन्‍्द, श्रीदामा, गिरिभानु,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10673)
- **Original**: गोपियाँ हाथोंमें वीणा आदि बाच्य लिये सानन्द विभाकर, वीरभानु और चन्द्रभानु-ये प्रमुख
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10674)
- **Original**: यात्रा कर रही थीं। कुछ अपने साथ अग्रिशुद्ध गोपगण हाथीपर बैठकर सानन्द यात्रा कर रहे थे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10675)
- **Original**: दिव्य बस्त्रोंका भार लिये चल रही थीं। कितनी ही श्रीकृष्ण और बलदेब दोनों भाई रत्ननिर्मित आभूषणोंसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10676)
- **Original**: चन्दन, अगुरु, कस्तूरी और केसरका द्रव ले जा विभूषित हो सुवर्णमय रथपर बैठकर बड़े हर्षके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10677)
- **Original**: रही थीं। कोई संगीतमें मग्न थीं तो कोई विचित्र साथ वृन्दावनकी ओर जा रहे थे। कोटि-कोटि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10678)
- **Original**: कथाएँ कह रही थीं। उस समय कोटि-कोटि शिबिकाएँ, रथ, घोड़े, गाड़ियाँ, बैल और लाखों हाथी आदि चल रहे थे। मुने ! वृन्दावनमें पहुँचकर कक 4744 24
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10679)
- **Original**: सबने उसे गृहशून्य देखा। तब वे सभी लोग वृक्षोंके नीचे यथास्थान ठहर गये। उस समय &6ं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10680)
- **Original**: श्रीकृष्णे गोपोंको अभीष्ट गृह और गौओंके उहरनेके स्थान बताते हुए कहा--' आज इसी तरह 5 38005:2
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10681)
- **Original**: ठहरो। कल सब व्यवस्था हो जायगी ।' श्रीकृष्णकी
- **Translation**: 

---

