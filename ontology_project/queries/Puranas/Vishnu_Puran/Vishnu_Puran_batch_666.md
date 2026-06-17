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

### Verse 1 (Vishnu Puran 0.13301)
- **Original**: उदेव क्षुलस्पो+यम 2 ए#ह48#/7 78 तदर्थमवनीओं उसी 5 38 60 । पदंश्गृतसकेंगम्‌ न... 457 7188-16 शा हि दफ़ते सर्वम्‌ 9 हे 23 ।हद्च्ठतनभीः कर्र्या $ 17 5 ड4ड तदाकरं जगगेदम्‌ श 69: - 7
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13302)
- **Original**: तदचछबछयावास्रम्‌ धुत 37070 18 छदाकर्ण्य तै य हे हर 28 । तद्क्क फांउजाप ला रद्माकर्म्प भगषते 3
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13303)
- **Original**: कद्च्छ ओयसे सर्वम्‌ 6 7 - 101 ढदा तुल्यमहोणफ्म्‌ "7 63 8 475
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13304)
- **Original**: शझदशनाहरास्याम्‌ 4 हल सफाई रादा प्रयूदक्ष कि: » 4. 24 107
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13305)
- **Original**: उद्जुस्तानिशरस्ाणि 7000 380 30 स्दाकर्ष्य रजा कम. 4 6 पड
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13306)
- **Original**: तु पर्स नित्यम्‌ बल है। 2 13 र्टाश्याट्मेवैत्‌ 4 8 5 इंद
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13307)
- **Original**: तड़प योगी 7. 3 220 छोई रुदार्तरवश्रवपानतश्प्‌ 13 8 45
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13308)
- **Original**: स्यष् तत्रों धाम न... 100 7 7788 रदाश्रममुपाताश्र 4. 20 रड
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13309)
- **Original**: सुझततर 45 75... हक हंपुछाजतदै8 स्वागच्छत गछ्छाम: 6-80 1 4:32
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13310)
- **Original**: द्छुद्य पर धाम 7... छह णई 7: हट टदा विष्काएक सर्वम्‌ 50 15-21.
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13311)
- **Original**: तद्भघानेव चारवितुभ्‌ 48-17: 109 ट्दाप्रोत्यलिस सम्पार 6 “«6। बेर.
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13312)
- **Original**: तद्वस्मस्र्ज्ञााभूत' 3] स्टिद ते मनो दिष्टया &6& 7 8:10
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13313)
- **Original**: तद्गवुत्थारसु 50 133 'छ1 रहिए स्पनचफरणम्‌ डे 613 रा;
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13314)
- **Original**: तंद्वायभावनापन्नः 6 7 97 रदिय खदीयापहसना डे: शूढ-. 738...
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13315)
- **Original**: तद्ूरिमारफीडार्ता 3] रादीसणाय राप्याय दिलॉसड दे 3.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13316)
- **Original**: क्यया समतकाजगतम्‌ इंहलबरे हु] स्थुफसेनों मुसल्य्‌ «& -जू7 12
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13317)
- **Original**: त्येणरस्लि. केडित्‌ धटक्उप्ेंगए 11 स्वुफ्पशिनिशात्‌ 4 -13 - 769
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13318)
- **Original**: दूत विश्ररूपसथ श 50 7क 73 ऋ्दुत्फास्सता रफ 4 3138 880
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13319)
- **Original**: ददूपपत्वया नैकर श 7 47 91 त्दुफ्फोफविशेदाय डे 6 ए0 “317.
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13320)
- **Original**: तदद्धरोतकेम्यश्र ई<6011:84 85 तदेउदबगायाहम्‌ 1-19 - 42.
- **Translation**: 

---

