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

### Verse 1 (Vishnu Puran 0.8121)
- **Original**: आनकदुन्दुधि चसुदेवजीके पौरवो, येहिणी, मदिरा, भद्रा और देवकी आदि बहुत-सी ख्त्रियाँ थीं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8122)
- **Original**: उनमें रोहिणीसे वसुदेखजीने अलूभद्द, झाठ, सारण और दुर्मद आदि कई पुत्र उत्पन्न किये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8123)
- **Original**: तथा बलूभद्रजीके रेबतीसे विश्ुठ और उल्मुक नामक दो पुत्र हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8124)
- **Original**: साप्टि, मार्टि, सत्य और धृति आदि सारणके पुत्र थे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8125)
- **Original**: इनके अतिरिक्त भद्राश्व, सद्नबाहु, दुर्दम और भूत आदि भी रोहिणोहीकी सनन्‍्तानमें थे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8126)
- **Original**: ननन्‍्द, उपनन्‍्द और क़तक आदि मदिराके तथा उपनिधि और गद आदि भद्राके पुत्र थे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8127)
- **Original**: बैज्ञालीके गर्भसे कोशिक नामक केनल एक ही पुत्र हुआ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8128)
- **Original**: आनकदुनदुभिके देवकीसे कीर्तिमान, सुषेण, उदायु, भद्गसेन, ऋजुदास तथा भद्भदेज नामक छः पुत्र हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8129)
- **Original**: इन सबको कँसने मार डाल्म था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8130)
- **Original**: पीछे भगवानकी प्रेरणासे योगमायाने देखवकीके सातवें गर्भको आधी रातके समय खींचकर ग्रेहिणीकी कुक्षिमें स्थापित कर दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8131)
- **Original**: आकर्षण करनेसे इस गर्भका नाम संकर्षण हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8132)
- **Original**: तदनन्तर सम्पूर्ण संसाररूप महावक्षके मूलस्वरूप भूत, भविष्यत्‌ और बर्तमान- कालीन सम्पूर्ण देव, असुर और मुनिजनकों बुद्धिके अगम्य तथा ब्रह्मा और अग्नि आदि देवताओंद्वारा प्रणाम करके भूधारहरणके लिये प्रसन्न किये गये आदि, मध्य और अन्तहीन भगवान्‌ वासूदेवने देवकीके गर्भसे अवतार लिया तथा उन्होंकी कृपासे बढ़ी हुई महिमावाल्ली योगनिद्रा भी नन्‍्दगोपकोी पत्नी बशोदाके गर्भमें स्थित हुई
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8133)
- **Original**: उन कमलनयन भगवानके प्रकट होनेपर यह सम्पूर्ण जगत्‌ प्रसन्न हुए सूर्य, चन्द्र आदि ग्रहोँसे सम्पन्न सर्पादिके भयसे शुन्य, अभर्मादिसे रहित तथा स्वस्थचित्त हो गया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8134)
- **Original**: उन्होंने प्रकट होकर इस सम्पूर्ण संसारको सन्मार्गावल्म्बी कर दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8135)
- **Original**: इस मर्त्यलोकमें अवतोर्ण हु"णु भगवानूकी सोलह हजार एक सौ एक रानियाँ थीं। 34
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8136)
- **Original**: उनमें रुक्मिणी, सत्यभामा, जाम्बबती और चारुहासिनी आदि आठ मुख्य थीं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8137)
- **Original**: अगादि भगवान्‌ अखिलमूर्तिने उनसे एक
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8138)
- **Original**: 84 छः €ऊऋ अकखकभ्रीविष्णुपरण
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8139)
- **Original**: 0 आ* 15 85 भगवानखिलपूर्तिरनादिमानजनयत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8140)
- **Original**: तेषां च॒ प्रद्मु्नचारुदेष्णसाम्बादयस्रयोदश प्रधाना:
- **Translation**: 

---

