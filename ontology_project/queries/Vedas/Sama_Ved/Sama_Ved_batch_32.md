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

### Verse 1 (Sama Ved 0.621)
- **Original**: स्तुति न करने वाले (आस्थाहीन) के इद्धदेव, शत्रु हैं। स्तोता द्वारा पठित स्तोत्रों को वे भली-भाँति जानते हैं। सामवेद के गायक (उदगाता) के गायन को भी वे सुनते और समझते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.622)
- **Original**: पूर्वार्चिकि ऐज्रपर्वणि द्वितीयोउध्याय: ह 2.13 226. इन्द्र उक्थेभिर्मन्दिष्ठो बाजान॑ च वाजपति:। हरिवांत्सुतानां सखा
- **Translation**: 

---

### Verse 3 (Sama Ved 0.623)
- **Original**: महाबलशाली, अश्वों से सुसज्जित इन्द्रदेव सोमयज्ञ में साधकों के स्तोत्रों से आनन्दित होकर उनके सहायक बनते हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.624)
- **Original**: 227. आ याद्युप नः सुतं वाजेभिर्मा हणीयथा: । महाँ इब युवजानि:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.625)
- **Original**: पलीवत धर्म का पालन करने वाले योर पुरुष की भांति हे इन्रदेव ! आप हमारे ही सोमयज्ञ में पधारकर हविष्यान्न ग्रहण करें । दूसरों के (हीनपुरुषों के) अन्न पर दृष्टि न डालें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.626)
- **Original**: 228. कदा बसो स्तोत्र हर्यत आ अब श्मशा रुधद्ठा: । दीर्घ सुतं वाताप्याय 6
- **Translation**: 

---

### Verse 7 (Sama Ved 0.627)
- **Original**: हे स्तुतियों से प्रसन्‍न होने वाले इद्रदेंव ! जैसे नहरें निकालने के लिए जल रोका जाता है, उसी प्रकार तैयार किया हुआ सोमरस प्रदान करने के लिए आपको कब रोकें ?
- **Translation**: 

---

### Verse 8 (Sama Ved 0.628)
- **Original**: 229. ब्राह्मणादिन्द्र राधस: पिबा सोममृतृँरनु
- **Translation**: 

---

### Verse 9 (Sama Ved 0.629)
- **Original**: तवेदं सख्यमस्तृतम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.630)
- **Original**: हे इन्द्रदेव ! ब्रह्म को जानने वाले साधक के पात्र से, मित्रवत्‌ ऋतुओं के अनुसार सोमरस का पान करें, क्योंकि आपकी मित्रता अदूट है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.631)
- **Original**: ; 230. बय॑ घा ते अपि स्मसि स्तोतार इन्द्र गिर्वण:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.632)
- **Original**: त्वं नो जिन्व सोमपा:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.633)
- **Original**: हे प्रशंसा के योग्य इन्धदेव ! हम आपके स्तोता हैं । हे सोमपायी इन्द्रदेव ! आप हमें तुष्टि प्रदान करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.634)
- **Original**: 231. एन्द्र पृक्षु कासु चित्नृम्णं तनूषु थेह्ि नः। सत्राजिदुग पौस्यम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.635)
- **Original**: हे इन्रदेव ! यज्ञीय कार्य में प्रयुक्त हमारे अंगों में बल प्रदान करें । हे बोर इद्धदेव.! एक साथ सभी शत्रुओं को पराजित करने की शक्ति हमें प्रदान करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.636)
- **Original**: 232. एवा ह्वासि वीरयुरेवा शूर उत स्थिर:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.637)
- **Original**: एवा ते राध्यं मन:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.638)
- **Original**: है बलवान्‌ इन्द्रदेव ! रणक्षेत्र में शत्रुओं को पराजित करने वाले, युद्ध में अडिग रहने वाले आप शूरवीर हैं ' आपका मन (संकल्पशोल) प्रशंसा के योग्य है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.639)
- **Original**: इति द्वादश: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.640)
- **Original**: औ औऑे और
- **Translation**: 

---

