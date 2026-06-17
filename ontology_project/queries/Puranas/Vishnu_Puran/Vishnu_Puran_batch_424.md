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

### Verse 1 (Vishnu Puran 0.8461)
- **Original**: मणिपुरपतिपुत्र्यां पुत्रिका- धर्मेण बच्नुवाहन नाम पुत्रमर्जुनोइजनयत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8462)
- **Original**: सुभद्रायां चार्भकत्वेषपि योइसाबतिबलपराक्रम- स्समस्तारातिरथजेता सो5भिमन्युरजायत
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8463)
- **Original**: श्रीविष्णुपुराण [ अब 20 बाक्लीकके सोमदत्त मामक पुत्र हुआ तथा सोमदत्तके भूरि, भूरिश्रता और दाल्य नामक तीन पुत्र हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8464)
- **Original**: झान्तनुके गज्जाजीसे अतिशय कीर्तिमान तथा सम्पूर्ण शाख्रोंका जाननेबाला भीष्म नामक पूत्र हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8465)
- **Original**: शानन्‍्तनुने सत्यवतीसे चित्राड्नद और तिचित्रलीर्य नामक दो पुत्र और भी उत्पन्न किये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8466)
- **Original**: उनमेंसे घित्राक़ुदको तो बाल्यावस्थामें ही चित्राज़द नामक गन्बर्वने युद्धमें मार डाल्मथ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8467)
- **Original**: पिचित्रवीर्यने काशिराजकी पुत्री अम्बिका और अम्बालिकासे विवाह किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8468)
- **Original**: उनमें अत्यन्त भोगासक्त रहनेके कारण अतिदाय स्रिन्न रहनेसे वह यक्ष्माके बशीभूत होकर [ अकालटोमें ] मर गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8469)
- **Original**: तदनन्तर मेरे पुत्र कृष्णड्रैपायनने सत्यवतीके नियुक्त करनेसे माताक्य्र चचन टालना उचित न जान ब्रिचिजवीर्यक्ती पत्नियोंसे धृतराष्ट और पाष्डु नामक दो पुत्र उत्पन्न किये और उनकी भेजी हुई दासीसे लिदुर नामक एक पुत्र उत्पन्न किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8470)
- **Original**: घृतराष्ट्रने भी गान्धारीसे दुर्योधन और दुःशासन आदि सौ पुत्रोंको जन्म दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8471)
- **Original**: पाएडू वनमें आस्वेट करते समय ऋषिके शापसे सन्तानोत्यादनमें असमर्थ हो गये थे अतः उनको स्त्री कुन्तोसे धर्म, वायु और इन्द्रने क्रमद्ाः युघिप्ठिर, भीम और अर्जुन नामक तीन पुत्र तथा माद्रीसे दोनों अश्विनीकुमारोंने नकुल और सहदेव नामक दो पृत्र उत्पन्न किये। इस प्रकार उनके पाँच पुत्र हुए
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8472)
- **Original**: उन पांचोंके द्रौपदीसे पाँच हो पुत्र हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8473)
- **Original**: उनमेंसे युध्रिष्टिससे प्रतिविन्ध्य, भीमसेनसे श्रुतसेन, अर्जुनसे श्रुतकीर्ति, नक्ुलसे श्रुतानीक तथा सहदेवसे श्रुतकर्माका जन्म हुआ था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8474)
- **Original**: इनके अतिरिक्त पाष्डलोंके और भी बई पुत्र हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8475)
- **Original**: जैसे--युथिष्ठिस्से यौधेयीके देवक नामक पुत्र हुआ, भीमसेनसे हिडिम्बाके घटोत्कच और काशीसे सर्वग नामक पूत्र हुआ, सहदेवसे किजयाके सुहोत्रका जन्म हुआ, नकुलने रेणुमतीसे निरमित्रको उत्पन्न किया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8476)
- **Original**: 44---48
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8477)
- **Original**: अर्जुनके नागकन्या उल्मूपीसे इराबान्‌ नामक पुन हुआ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8478)
- **Original**: मणिपुर नरेश्की पुत्रीसे अर्जुनने पुत्रिका-घर्मानुसार बभुवाहन नामक एक पुत्र उत्पन्न किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8479)
- **Original**: तथा उसके सुभद्रासे अभिमन्युका जन्म हुआ जो कि बाल्यावस्थामें ही बड़ा बल-पराक्रम-सम्पत्र तथा अपने सम्पूर्ण झन्नुऑकी जीतनेवाला था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8480)
- **Original**: आ0 21 ] चअतुर्ण अंश 297 अभिमन्योरुत्तरायां परिक्षीणेषु कुरुप्ृश्नत्थाम- प्रयुक्तब्रह्मास्रेण गर्भ एबं भस्मीकृतों भगवत- स्सकलसुरासुरवन्दितचरणयुगलस्यात्मेच्छया कारणमानुषरूपधारिणोनुभावात्पुनर्जीबित - म्रवाष्य परीक्षिजज्ञे
- **Translation**: 

---

