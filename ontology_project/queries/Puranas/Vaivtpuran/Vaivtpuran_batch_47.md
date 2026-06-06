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

### Verse 1 (Vaivtpuran 4.8987)
- **Original**: अश्रुत था। वज़्मयी भीतोंपर अक्वित चित्रोंके तथा मालाओंकी जालीसे विभूषित था। वहाँ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8988)
- **Original**: कारण उस द्वारकी सुन्दरता और मनोहरता बहुत सुन्दर आकारवाले सुबल नामक द्वारपाल दृष्टिगोचर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8989)
- **Original**: बढ़ गयी थी। देवताओंने देखा बारहवें द्वारकी हुए, जो भाँति-भौतिके आभूषणोंसे भूषित, भूषणके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8990)
- **Original**: रक्षामें सुन्दरी गोपाड़नाएँ नियुक्त हुई हैं। वे सब- योग्य तथा मनोहर थे। उनके साथ बारह लाख
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8991)
- **Original**: कौ-सब रूप-यौवनसे सम्पन्न, रत्नाभरणोंसे विभूषित, ब्रजवासी थे। दण्डधारी सुबलसे पूछकर देवताओंने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8992)
- **Original**: पीताम्बरधारिणी तथा बँधे हुए केश-कलापके तत्काल दूसरे द्वारको प्रस्थान किया। उस विलक्षण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8993)
- **Original**: भारसे सुशोभित थीं। उनके सारे अद्गभ सुस्तरिग्ध दसवें द्वारको देखकर देवताओंको बड़ा विस्मय
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8994)
- **Original**: मालतीकी मालाओंसे अलंकृत थे। रत्रोंके बने हुए हुआ। मुने ! वहाँका सब कुछ अनिर्वचनीय, अदृष्ट
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8995)
- **Original**: कंगन, बाजूबंद तथा नूपुर उन-उन अम्ञॉकी शोभा और अश्रुत था-वैसा दृश्य कभी देखने और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8996)
- **Original**: बढ़ाते थे। उनके दोनों कपोल दिव्य रत्रमय सुननेमें भी नहीं आया था। वहाँ सुन्दर सुदामा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8997)
- **Original**: कुण्डलॉसे उद्भासित हो रहे थे। वे चन्दन, अगुरु, नामक गोप द्वारपालके- पदपर प्रतिष्ठित थे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8998)
- **Original**: कस्तूरी और कुंकुमके द्रवसे अपना श्रृज्ञार किये सुदामाका रूप श्रीकृष्णके समान ही मनोहर तथा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8999)
- **Original**: हुए थीं। वहाँ सौ कोटि गोपियोंमें एक श्रेष्ठ गोपी अवर्णनीय था। उनके साथ बीस लाख गोपोंका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.9000)
- **Original**: थी, जो श्रीहरिको भी परम प्रिय थी। उन करोड़ों समूह रहता था। दण्डधारी सुदामाका दर्शनमात्र
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.9001)
- **Original**: गोपिकाओंको देखकर देवताओंको बड़ा विस्मय करके देवतालोग दूसरे ट्वारपर चले गये। हुआ। मुने! उन सब गोपियोंसे अनुमति ले वे वह ग्यारहबाँ द्वार अत्यन्त विचित्र और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.9002)
- **Original**: देवता प्रसन्नतापूर्वक दूसरे द्वारपर गये। इस तरह अद्भुत था। वहाँ सुन्दर चित्र अद्भित थे। वहाँके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.9003)
- **Original**: क्रमशः तीन द्वारोंपर उन्होंने देखा--श्रेष्ठ और द्वारपाल ब्रजराज श्रीदामा थे, जिन्हें राधिकाजी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.9004)
- **Original**: अत्यन्त मनोहर गोपाड्नाएँ उनकी रक्षा कर रही अपने पुत्रके समान मानती थीं। वे पीताम्बरसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.9005)
- **Original**: हैं। वे सुन्दरियोंमें भी सुन्दरी, रमणीया, धन्या, विभूषित थे, बहुमूल्य रज्नोंद्ार रचित रम्य सिंहासनपर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.9006)
- **Original**: मान्या और शोभाशालिनी हैं। सब-की-सब सौभाग्यमें आसीन थे और अमूल्य रत्राभरण उनकी शोभा
- **Translation**: 

---

