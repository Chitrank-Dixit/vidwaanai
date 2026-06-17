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

### Verse 1 (Bramha 0.4381)
- **Original**: तथा पुत्र-पौत्रोंका विस्तार करनेवाला होगा। इस ही उनके लिये जो विधान रच दिया है, वह कभी
- **Translation**: 

---

### Verse 2 (Bramha 0.4382)
- **Original**: तीर्थमें पिण्ड आदि देनेसे पितरोंकी मुक्ति हो बदल नहीं सकता। अतः जीब व्यर्थ ही क्लेश
- **Translation**: 

---

### Verse 3 (Bramha 0.4383)
- **Original**: जायगी। कोई भी मनुष्य इसमें स्नान करनेसे मन, उठाते हैं।* इसलिये हम जगत्‌के कल्याणके लिये
- **Translation**: 

---

### Verse 4 (Bramha 0.4384)
- **Original**: वाणी तथा शरीरजन्य पापसे मुक्त हो जायगा। ही कुछ याचना करते हैं। हमारी यह याचना सबके
- **Translation**: 

---

### Verse 5 (Bramha 0.4385)
- **Original**: अग्निदेवने कहा--जो लोग नियमपूर्वक रहते लिये गुणदायक है। आप दोनों इसका अनुमोदन
- **Translation**: 

---

### Verse 6 (Bramha 0.4386)
- **Original**: हुए दक्षिण-तटपर मेरे स्तोत्रका पाठ करेंगे, उन्हें मैं करें। गड्ाके दोनों तटोंपर जो हमारे आश्रम हैं, वे
- **Translation**: 

---

### Verse 7 (Bramha 0.4387)
- **Original**: आयु, आरोग्य, ऐश्वर्य, लक्ष्मी तथा रूप प्रदान करूँगा। तीर्थरूपमें परिणत हो जायेँ। वहाँ कोई पापी या
- **Translation**: 

---

### Verse 8 (Bramha 0.4388)
- **Original**: जो कोई मानव कहीं भी इस स्तोत्रका पाठ करेगा पुण्यात्मा जिस किसी तरह जो कुछ भी स्नान, दान,
- **Translation**: 

---

### Verse 9 (Bramha 0.4389)
- **Original**: अथवा लिखकर भी इसे घरमें रख देगा, उसको तथा जप, होम और पितरोंका पूजन आदि करें, बह सब
- **Translation**: 

---

### Verse 10 (Bramha 0.4390)
- **Original**: उसके घरको कभी भी अग्निसे भय न होगा। जो अक्षय पुण्य देनेवाला हो। मनुष्य पवित्र होकर अग्रितीर्थमें स्नान और दान यमराज बोले--जो लोग गौतमीके उत्तर-
- **Translation**: 

---

### Verse 11 (Bramha 0.4391)
- **Original**: करेगा, ठसे निश्चय ही अग्नि्टोम-यज्ञका फल मिलेगा। तटपर यमस्तोत्रका पाठ करेंगे, उनके वंशमें सात
- **Translation**: 

---

### Verse 12 (Bramha 0.4392)
- **Original**: तबसे वह तीर्थ याम्यतीर्थ, आग्रेयतीर्थ, कपोततीर्थ, पीढ़ियोंतक किसीकी अकालमृत्यु नहीं होगी। वे
- **Translation**: 

---

### Verse 13 (Bramha 0.4393)
- **Original**: उलूकतीर्थ और हेत्युलूकतीर्थके नामसे विद्वानोंमें पुरुष सदा सब प्रकारकी सम्पत्तियोंके भागी होंगे।
- **Translation**: 

---

### Verse 14 (Bramha 0.4394)
- **Original**: प्रसिद्ध हुआ। वहाँ तीन हजार तीन सौ नब्बे तीर्थ जो जितात्मा पुरुष प्रतिदिन इस स्तोत्रका पाठ
- **Translation**: 

---

### Verse 15 (Bramha 0.4395)
- **Original**: हैं और उनमेंसे प्रत्येक तीर्थ मोक्ष देनेबाला है। करेगा, वह अट्टासी हजार व्याधियोंसे कभी
- **Translation**: 

---

### Verse 16 (Bramha 0.4396)
- **Original**: उन तीथ्थोंमें स्नान करनेसे मनुष्य पवित्र होते, पुत्र पीड़ित न होगा। इस तीर्थमें तीन मासतक स्नान
- **Translation**: 

---

### Verse 17 (Bramha 0.4397)
- **Original**: और धन पाते तथा अन्तमें स्वर्गलोकको जाते हैं। 8 >> कवव4/000 तपस्तीर्थ, इन्द्रतीर्थ और वृषाकपषि एवं अब्जकतीर्थकी महिमा 07::7% 8 कहते हैं--तपस्तीर्थ बहुत बड़ा तीर्थ
- **Translation**: 

---

### Verse 18 (Bramha 0.4398)
- **Original**: प्रसन्नताको बढ़ानेवाला है। उस तीर्थमें जो पापनाशक है। बह तपस्याकी वृद्धि करनेवाला, समस्त
- **Translation**: 

---

### Verse 19 (Bramha 0.4399)
- **Original**: घटना घटी है, उसे बतलाता हूँ; सुनो। ऋषियोंमें अभिलषित वस्तुओंका दाता, पवित्र तथा पितरोंकी
- **Translation**: 

---

### Verse 20 (Bramha 0.4400)
- **Original**: अग्नि और जलकी श्रेष्ठताको लेकर परस्पर संवाद + आत्मार्थ यस्तु याचेत स शोच्यो हि सुरेश्वरो। जीवितं सफल तस्य यः परार्थोद्यत: सदा
- **Translation**: 

---

