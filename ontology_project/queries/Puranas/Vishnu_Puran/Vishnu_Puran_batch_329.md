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

### Verse 1 (Vishnu Puran 0.6561)
- **Original**: पश्चाशइ- हितरस्तस्थामेव तस्य नृपतेर्ब भूखु:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6562)
- **Original**: तस्मिन्ननतते बहवृच्रक्ष सौभरिनाम महर्षि- रन्तर्जले द्वादशाब्द॑ कालमुबास
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6563)
- **Original**: तत्र चान्तर्जले सम्मदो मीनाधिपतिरासीत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6564)
- **Original**: तस्थ च॒ पुत्रपौत्र- चोपरि भ्रमन्तस्तेनेष सदाहर्निशमतिनिर्व॒ता रेपिरे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6565)
- **Original**: स चापत्यस्पशॉफ्लीयमानप्रहर्ष प्रकर्षो बहुप्रकार॑ तस्थ ऋषे: पश्यतस्तैरात्मजपुत्र पोत्रदौह्ित्रादिभि: सहानुदिनं सुतरां रेमे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6566)
- **Original**: अथान्तर्जलावस्थितस्सौभरिरेकाग्रतस्समाधि- धन्योउयमीदृशमनभिमतत रमवाप्यैभिरात्मजपुत्रपौत्रदौहित्रादिभिस्सह रममाणो5तीवास्मार्क स्पृहामुत्पादयति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6567)
- **Original**: कोख फाड़कर निकल आया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6568)
- **Original**: कितु इससे राजाकी मृत्यु नहीं हुई
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6569)
- **Original**: उसके जन्म लेनेपर मुनियोनि कह्ा--““यह बालक क्या पान करके जीवित रहेगा ?'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6570)
- **Original**: उसी समय देवराज इद्धने आकर कहा--“यह मेरे आश्रय-जीवित रहेगा"
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6571)
- **Original**: अत: उसका नाम मान्धाता हुआ । देवेच्रने उसके मुखमें अपनी तर्जनी (अँगूठेके पासकी) अंगुली दे दी और यह उसे पोने लगा। उस अमृतमयी अंगुलीका आस्वादन करनेसे यह एक ही दिनमें बढ गया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6572)
- **Original**: तभीसे चक्रवर्ती मान्धाता साप्तद्वोपा पृधिवीका राज्य भोगने छगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6573)
- **Original**: इसके विषयमें यह इल्जेक कहा जाता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6574)
- **Original**: 'जहाँसे सूर्य उदय होता है और जहाँ अस्त होता है जह सभी क्षेत्र युवनाश्वके पुत्र मान्धाताका है'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6575)
- **Original**: माच्धाताने शतबिन्दुकी पुत्री बिन्दुमतीसे विवाह किया और उससे प्रुकुत्स, अम्बरीष और मुचुकुन्द नामक तोन पुत्र उत्पन्न किये तथा उसी (बिन्दुमती) से उनके पचास कन्याएँ हुईं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6576)
- **Original**: 66--68
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6577)
- **Original**: उसी समय बहूवृत्त सौभरि नामक महर्षिने बारह वर्षतक जलमें निवास किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6578)
- **Original**: उस जलमें सम्मद्‌ नामक एक बहुत-सी सत्तानोंबाला और अति दीर्घकाय मत्स्यशाज था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6579)
- **Original**: उसके पुत्र, पौष और दौहित्र आदि उसके आगे-पीछे तथा इधर-उधर पक्ष, पुच्छ और शिरके ऊपर घूमते हुए अति आनन्दित होकर रात-दिन' उसीके साथ क्रीडा करते रहते थे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6580)
- **Original**: तथा वह भी अपनी सन्‍्तानक्रे सुकोमल स्पर्श़से अत्यन्त हर्षयुक्त होकर उन मुनिश्वरके देखते-देखते अपने पुत्र, पौत्र और दौतित्र आदिके साथ अहर्निश क्रीडा करता रहता था
- **Translation**: 

---

