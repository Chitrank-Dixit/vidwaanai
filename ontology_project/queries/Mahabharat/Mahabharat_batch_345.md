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

### Verse 1 (Mahabharat 0.3441)
- **Original**: लिये कर्ण खड़ा था तथा इृदप-स्थानमें जयद्रथ, सम्पाति, सेनाकी व्यूहत्वना कर युधिश्विरको पकड़नेके विचारसे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.3441)
- **Original**: लिये कर्ण खड़ा था तथा इृदप-स्थानमें जयद्रथ, सम्पाति, सेनाकी व्यूहत्वना कर युधिश्विरको पकड़नेके विचारसे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.3442)
- **Original**: ऋषभ, जय, धूमिक्षय, वृष, क्राथ और निषधराज बहुत बड़ी युद्धेक्षेत्रती ओर चले। महाराज युधिष्ठिस्से आचार्यकी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.3442)
- **Original**: ऋषभ, जय, धूमिक्षय, वृष, क्राथ और निषधराज बहुत बड़ी युद्धेक्षेत्रती ओर चले। महाराज युधिष्ठिस्से आचार्यकी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.3443)
- **Original**: सेनाके साथ खड़े थे। इस प्रकार पदाति, अश्वागेही, गजारोही मण्डलार्थव्यूह
- **Translation**: 

---

### Verse 6 (Mahabharat 0.3443)
- **Original**: सेनाके साथ खड़े थे। इस प्रकार पदाति, अश्वागेही, गजारोही मण्डलार्थव्यूह
- **Translation**: 

---

### Verse 7 (Mahabharat 0.3444)
- **Original**: और रघीसेनासे आचार्य ग्रेणका बनाया हुआ वह गसडव्यूह ऋरतोंके गरुडव्यूहके मुखस्थानपर महारथी द्रोण
- **Translation**: 

---

### Verse 8 (Mahabharat 0.3444)
- **Original**: और रघीसेनासे आचार्य ग्रेणका बनाया हुआ वह गसडव्यूह ऋरतोंके गरुडव्यूहके मुखस्थानपर महारथी द्रोण
- **Translation**: 

---

### Verse 9 (Mahabharat 0.3445)
- **Original**: वायुके झकोरंसे उछलते हुए समुद्रके समान जान पड़ता था। भाइयोंके दुर्षोधन था,
- **Translation**: 

---

### Verse 10 (Mahabharat 0.3445)
- **Original**: वायुके झकोरंसे उछलते हुए समुद्रके समान जान पड़ता था। भाइयोंके दुर्षोधन था,
- **Translation**: 

---

### Verse 11 (Mahabharat 0.3446)
- **Original**: इसके मध्यभागमें हाथीपर चढ़े हुए महाराज भगठत्त अवास्थानमें
- **Translation**: 

---

### Verse 12 (Mahabharat 0.3446)
- **Original**: इसके मध्यभागमें हाथीपर चढ़े हुए महाराज भगठत्त अवास्थानमें
- **Translation**: 

---

### Verse 13 (Mahabharat 0.3447)
- **Original**: बालसूर्यके समान सुझोभित हो रहे थे। “8 इस अजेय और अतिमानुष व्यूहको देखकर राजा चूरं, आभीर, दश्चेश्क, झक, यबन, काम्बोज, हंसपथ,
- **Translation**: 

---

### Verse 14 (Mahabharat 0.3447)
- **Original**: बालसूर्यके समान सुझोभित हो रहे थे। “8 इस अजेय और अतिमानुष व्यूहको देखकर राजा चूरं, आभीर, दश्चेश्क, झक, यबन, काम्बोज, हंसपथ,
- **Translation**: 

---

### Verse 15 (Mahabharat 0.3448)
- **Original**: युधिष्ठिरने धृष्ट्युम़्से कहा, 'वीर ! आज तुप ऐसा प्रयत्र झर्सेन, दरद, मद्र और केकथ आदि देशोंके वीर हथियारोसे जे, कि, ट्रेन हम (स लैस होकर हाथी, घोड़े, रथ और पदातिसेनाके रूपमें खड़े
- **Translation**: 

---

### Verse 16 (Mahabharat 0.3448)
- **Original**: युधिष्ठिरने धृष्ट्युम़्से कहा, 'वीर ! आज तुप ऐसा प्रयत्र झर्सेन, दरद, मद्र और केकथ आदि देशोंके वीर हथियारोसे जे, कि, ट्रेन हम (स लैस होकर हाथी, घोड़े, रथ और पदातिसेनाके रूपमें खड़े
- **Translation**: 

---

### Verse 17 (Mahabharat 0.3449)
- **Original**: . पृष्टदुप़े कहा--महाराज ! कितना ही प्रयत्न थे। दायीं ओर अक्षौहिणी सेनाके सहित भूरिश्रवा, झल्य,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.3449)
- **Original**: . पृष्टदुप़े कहा--महाराज ! कितना ही प्रयत्न थे। दायीं ओर अक्षौहिणी सेनाके सहित भूरिश्रवा, झल्य,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.3450)
- **Original**: करें, वे आपको अपने कायूमें नहीं कर सकेंगे। आज उन्हें सौमदत्त और बाद्ीक थे। बायीं ओर अवच्तिनरेश विन्द और
- **Translation**: 

---

### Verse 20 (Mahabharat 0.3450)
- **Original**: करें, वे आपको अपने कायूमें नहीं कर सकेंगे। आज उन्हें सौमदत्त और बाद्ीक थे। बायीं ओर अवच्तिनरेश विन्द और
- **Translation**: 

---

