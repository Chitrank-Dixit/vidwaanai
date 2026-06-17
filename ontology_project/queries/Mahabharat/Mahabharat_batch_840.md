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

### Verse 1 (Mahabharat 941.8391)
- **Original**: स्वर्गलोकमें पहुँचे हुए हैं। महान्‌ धनुर्धर तथा झख्धारियोंमें युथिष्ठिस्को सान्वना देते हुए कहा--'महाबाहो ! अबतक
- **Translation**: 

---

### Verse 2 (Mahabharat 941.8391)
- **Original**: स्वर्गलोकमें पहुँचे हुए हैं। महान्‌ धनुर्धर तथा झख्धारियोंमें युथिष्ठिस्को सान्वना देते हुए कहा--'महाबाहो ! अबतक
- **Translation**: 

---

### Verse 3 (Mahabharat 941.8392)
- **Original**: श्रेष्ठ कर्ण भी, जिनके लिये तुम सदा दुःखी रहते हो, उत्तम जो हुआ सो हुआ, अब इससे अधिक कष्ट उठानेकी
- **Translation**: 

---

### Verse 4 (Mahabharat 941.8392)
- **Original**: श्रेष्ठ कर्ण भी, जिनके लिये तुम सदा दुःखी रहते हो, उत्तम जो हुआ सो हुआ, अब इससे अधिक कष्ट उठानेकी
- **Translation**: 

---

### Verse 5 (Mahabharat 941.8393)
- **Original**: सिद्धिको प्राप्त हुए हैं। तुम्हारे दूसरे भाई तथा पाण्डव-पक्षके आवश्यकता नहीं है। आओ; हमारे साथ चल्छो । तुम्हें बहुत
- **Translation**: 

---

### Verse 6 (Mahabharat 941.8393)
- **Original**: सिद्धिको प्राप्त हुए हैं। तुम्हारे दूसरे भाई तथा पाण्डव-पक्षके आवश्यकता नहीं है। आओ; हमारे साथ चल्छो । तुम्हें बहुत
- **Translation**: 

---

### Verse 7 (Mahabharat 941.8394)
- **Original**: अत्य राजा भी अपने-अपने योग्य स्थानको प्राप्त हुए हैं। उन बड़ी /सिद्धि मिली है, साथ ही अक्षयलोकोकी ग्राप्ति भी हुई
- **Translation**: 

---

### Verse 8 (Mahabharat 941.8394)
- **Original**: अत्य राजा भी अपने-अपने योग्य स्थानको प्राप्त हुए हैं। उन बड़ी /सिद्धि मिली है, साथ ही अक्षयलोकोकी ग्राप्ति भी हुई
- **Translation**: 

---

### Verse 9 (Mahabharat 941.8395)
- **Original**: सबको चलकर देखो और अपनी मानसिक चिन्ताका त्याग है। तुम्हें जो नसक देखना पड़ा है, इसके लिये क्रोध न करना ।
- **Translation**: 

---

### Verse 10 (Mahabharat 941.8395)
- **Original**: सबको चलकर देखो और अपनी मानसिक चिन्ताका त्याग है। तुम्हें जो नसक देखना पड़ा है, इसके लिये क्रोध न करना ।
- **Translation**: 

---

### Verse 11 (Mahabharat 941.8396)
- **Original**: कर मेरे साथ स्वर्गमें बिहार करो । अपने किये हुए पुण्यकर्म, मनुष्य अपने जीवनमें झुभ और अश्युभ--दो प्रकारके
- **Translation**: 

---

### Verse 12 (Mahabharat 941.8396)
- **Original**: कर मेरे साथ स्वर्गमें बिहार करो । अपने किये हुए पुण्यकर्म, मनुष्य अपने जीवनमें झुभ और अश्युभ--दो प्रकारके
- **Translation**: 

---

### Verse 13 (Mahabharat 941.8397)
- **Original**: तप और दानके फल भोगो। राजसूध-यज्ञद्ारा जीते हुए कमोंकी राज्मि संचित करता है। जो पहले झुभ कमोंका फल
- **Translation**: 

---

### Verse 14 (Mahabharat 941.8397)
- **Original**: तप और दानके फल भोगो। राजसूध-यज्ञद्ारा जीते हुए कमोंकी राज्मि संचित करता है। जो पहले झुभ कमोंका फल
- **Translation**: 

---

### Verse 15 (Mahabharat 941.8398)
- **Original**: समृद्धिशाली स्थेकॉंक्रो स्वीकार करो और अपनी तपस्थाका आोगता है, उसे पीछेसे नस्‍क भोगना-पड़ता है और जो पहले
- **Translation**: 

---

### Verse 16 (Mahabharat 941.8398)
- **Original**: समृद्धिशाली स्थेकॉंक्रो स्वीकार करो और अपनी तपस्थाका आोगता है, उसे पीछेसे नस्‍क भोगना-पड़ता है और जो पहले
- **Translation**: 

---

### Verse 17 (Mahabharat 941.8399)
- **Original**: महान्‌ फल भोगो। युधिष्ठिर ! तुम्हें प्राप्त हुए सम्पूर्ण लोक ही नरकका कष्ट भोग लेता है, वह पीछे स्वर्गीय सुखका
- **Translation**: 

---

### Verse 18 (Mahabharat 941.8399)
- **Original**: महान्‌ फल भोगो। युधिष्ठिर ! तुम्हें प्राप्त हुए सम्पूर्ण लोक ही नरकका कष्ट भोग लेता है, वह पीछे स्वर्गीय सुखका
- **Translation**: 

---

### Verse 19 (Mahabharat 941.8400)
- **Original**: राजा हरिक्षद्रके स्प्रेकोंकी भाँति सब राजाओंके ल्लेकोंसे
- **Translation**: 

---

### Verse 20 (Mahabharat 941.8400)
- **Original**: राजा हरिक्षद्रके स्प्रेकोंकी भाँति सब राजाओंके ल्लेकोंसे
- **Translation**: 

---

