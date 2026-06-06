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

### Verse 1 (Bramha 0.6081)
- **Original**: श्रीहरिका यह वचन सुनकर गोप मौन हो गये। वे यह सोचकर कि कन्हैया हमारी बातें सुनकर रूठ गया है, वहाँसे चुपचाप चले गये।
- **Translation**: 

---

### Verse 2 (Bramha 0.6082)
- **Original**: तदनन्तर एक दिन निशाकालमें श्रीकृष्णने देखा--आकाश स्वच्छ है, शरच्चन्द्रको मनोरम चाँदनी चारों ओर फैली है, कुमुदिनी खिली है,
- **Translation**: 

---

### Verse 3 (Bramha 0.6083)
- **Original**: जिसकी आमोदमय सुगन्धसे सम्पूर्ण दिशाएँ महक 5 कटा 02 रही हैं। बनमें सब ओर भौरे गूँज रहे हैं, जिससे
- **Translation**: 

---

### Verse 4 (Bramha 0.6084)
- **Original**: शरत्कालीन चन्द्रमाकी ज्योत्स्नासे अत्यन्त मनोरम वह वनश्रेणी अत्यन्त मनोहारिणी जान पड़ती है।
- **Translation**: 

---

### Verse 5 (Bramha 0.6085)
- **Original**: प्रतीत होनेवाली उस रजनीका सम्मान किया--रास प्रकृतिकों यह नैसर्गिक शोभा देखकर उन्होंने
- **Translation**: 

---

### Verse 6 (Bramha 0.6086)
- **Original**: आरम्भ करके उसे गौरव प्रदान किया। गोपियोंके साथ रास करनेका बिचार किया।
- **Translation**: 

---

### Verse 7 (Bramha 0.6087)
- **Original**: इसी बीचमें श्रीकृष्ण गायब होकर कहीं श्रीकृष्णने अत्यन्त मधुर स्वरमें संगीतकी मधुर
- **Translation**: 

---

### Verse 8 (Bramha 0.6088)
- **Original**: अन्यत्र चले गये। गोपियोंका शरीर श्रीकृष्णकी तान छेड़ दी, जो बनिताओंको बहुत ही प्रिय थी।
- **Translation**: 

---

### Verse 9 (Bramha 0.6089)
- **Original**: चेश्ठओंके अधीन था। वे झुंड-की-झुंड अपने गीतकी मनोरम ध्यनि सुनकर गोपियाँ घर छोड़कर
- **Translation**: 

---

### Verse 10 (Bramha 0.6090)
- **Original**: प्रियतमकी खोजके लिये बृन्दावनमें विचरने लगीं। निकल पड़ीं और बड़ी उताबलीके साथ उस
- **Translation**: 

---

### Verse 11 (Bramha 0.6091)
- **Original**: उनके मनमें केवल श्रीकृष्णके दर्शनकी लालसा स्थानपर आ पहुँचीं, जहाँ मधुसूदन मुरली यजा
- **Translation**: 

---

### Verse 12 (Bramha 0.6092)
- **Original**: थी। वे बृन्दावनकी भूमिपर रात्रिमें श्रीकृष्णके रहे थे। वहाँ आकर कोई गोपी तो उनके स्वरमें
- **Translation**: 

---

### Verse 13 (Bramha 0.6093)
- **Original**: चरण-चिह् देखकर उन्हें चारों ओर ढूँढ़ रही थीं। स्वर मिलाकर धीरे-धीरे गाने लगी। कोई ध्यान
- **Translation**: 

---

### Verse 14 (Bramha 0.6094)
- **Original**: श्रीकृष्णकी विभिन्न लीलाओंका अनुकरण करती देकर सुनती हुई मन-ही-मन भगवान्‌का स्मरण
- **Translation**: 

---

### Verse 15 (Bramha 0.6095)
- **Original**: हुई उन्होंमें व्यग्र हो सब गोपियाँ एक ही साथ करने लगी। कोई “कृष्ण-कृष्ण' कहकर लजा
- **Translation**: 

---

### Verse 16 (Bramha 0.6096)
- **Original**: वृन्दायनमें विचरने लगीं। बहुत खोजनेपर भी जब गयी। कोई प्रेमान्ध होकर लज्जाकों तिलाजलि दे श्रीकृष्ण नहीं मिले, तब उनके दर्शनसे निराश हो उनके बगलमें खड़ी हो गयी। कोई गोपी बाहर
- **Translation**: 

---

### Verse 17 (Bramha 0.6097)
- **Original**: वे सब-की-सब लौटकर यमुनाके तटपर आयी गुरुजनॉंको खड़ा देख घरके भीतर ही रह गयी
- **Translation**: 

---

### Verse 18 (Bramha 0.6098)
- **Original**: और उनके मनोहर चरित्नोंका गान करने लगीं। और नेत्र बंद करके तन्‍्मय हो गोविन्दका ध्यान
- **Translation**: 

---

### Verse 19 (Bramha 0.6099)
- **Original**: इतनेमें ही श्रीकृष्ण उन्हें आते दिखायी दिये। करने लगी। गोपियोंसे घिरे हुए श्रीकृष्ण रासलीलाका
- **Translation**: 

---

### Verse 20 (Bramha 0.6100)
- **Original**: उनका मुखकमल खिला था। त्रिभुवनके रक्षक रसास्वादन करनेको उत्सुक थे। अतः उन्होंने
- **Translation**: 

---

