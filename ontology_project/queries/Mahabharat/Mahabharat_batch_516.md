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

### Verse 1 (Mahabharat 0.5151)
- **Original**: सूचना देते हुए कहा 'अब पृथ्वी तुप्हारे पहियेको निगलना ही उसे बड़ी बेदना होने लगी । उसके मस्तकपर एक सुन्दर मुकुट
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5151)
- **Original**: सूचना देते हुए कहा 'अब पृथ्वी तुप्हारे पहियेको निगलना ही उसे बड़ी बेदना होने लगी । उसके मस्तकपर एक सुन्दर मुकुट
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5152)
- **Original**: चाइती है।' इसी समय परशुरामजीके द्वारा मिले हुए ब्राह्म कानोमें सुन्दर कुण्डल झोभा पा रहे थे। अर्जुनके बाणोंकी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5152)
- **Original**: चाइती है।' इसी समय परशुरामजीके द्वारा मिले हुए ब्राह्म कानोमें सुन्दर कुण्डल झोभा पा रहे थे। अर्जुनके बाणोंकी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5153)
- **Original**: चोट:खाकर कर्णका वह मुकुट कुष्डलॉके साथ ही जमीनपर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5153)
- **Original**: चोट:खाकर कर्णका वह मुकुट कुष्डलॉके साथ ही जमीनपर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5154)
- **Original**: जा पढ़ा। उसने जो कबक्‍च पहन रखा था, वह भी बड़ा
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5154)
- **Original**: जा पढ़ा। उसने जो कबक्‍च पहन रखा था, वह भी बड़ा
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5155)
- **Original**: था जिसमें उत्तम-उत्तम मणि, हीरे और सुवर्ण जड़े हुए थे।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5155)
- **Original**: था जिसमें उत्तम-उत्तम मणि, हीरे और सुवर्ण जड़े हुए थे।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5156)
- **Original**: अखकी याद उसके मनसे जाती रही । उधर, पृथ्वी ब्राह्मणके दिनोंमें बनाया था, परंतु अजुनने एक ही क्षणमें बाण मारकर
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5156)
- **Original**: अखकी याद उसके मनसे जाती रही । उधर, पृथ्वी ब्राह्मणके दिनोंमें बनाया था, परंतु अजुनने एक ही क्षणमें बाण मारकर
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5157)
- **Original**: उसके दुकडे-दुकड़े कर डाले। इसके बाद तेज किये हुए चार _ बाण मास्कर उन्होंने उसे और भी घायल कर दिया। जैसे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5157)
- **Original**: उसके दुकडे-दुकड़े कर डाले। इसके बाद तेज किये हुए चार _ बाण मास्कर उन्होंने उसे और भी घायल कर दिया। जैसे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5158)
- **Original**: बात; पित्त और कफके ग्कोपसे होनेवाले सक्निपात-ज्वरमें
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5158)
- **Original**: बात; पित्त और कफके ग्कोपसे होनेवाले सक्निपात-ज्वरमें
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5159)
- **Original**: रोगीको विशेष व्यथा होती है, वैसे ही वाज्रुका बारंबार प्रहार
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5159)
- **Original**: रोगीको विशेष व्यथा होती है, वैसे ही वाज्रुका बारंबार प्रहार
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5160)
- **Original**: है होनेसे कर्णको बड़ी पीड़ा हुई। अर्जुनमें कार्य-कुशलता,
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5160)
- **Original**: है होनेसे कर्णको बड़ी पीड़ा हुई। अर्जुनमें कार्य-कुशलता,
- **Translation**: 

---

