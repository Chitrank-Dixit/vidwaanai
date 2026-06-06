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

### Verse 1 (Vaivtpuran 23.1542)
- **Original**: । 8 यतियों, वैष्णवों, ब्रह्मर्षियों एवं ब्रह्मचारियोंके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1543)
- **Original**: पालन करके मुँह धोये। पहले सोलह बार कुल्ला लिये गृहस्थोंको अपेक्षा चौगुने शौचका विधान
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1544)
- **Original**: करके मुख शुद्ध करनेके पश्चात्‌ दँतुवनसे दाँतकी किया गया है। उपनवनरहित द्विज, शूद्र तथा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1545)
- **Original**: सफाई करे। फिर सोलह बार कुछ्ला करके मुँह स्त्रीके लिये उतने ही शौचका विधान है, जितनेसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1546)
- **Original**: शुद्ध करे। नारद! दाँत माँजनेके लिये जो काठकी उन-उन अड्रोमें लगे हुए मलके लेप और दुर्गन्‍्ध
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1547)
- **Original**: लकड़ी ली जाती है, उसके विषयमें भी कुछ मिट जाय॑ं। क्षत्रिय और वैश्यके लिये भी गृहस्थ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1548)
- **Original**: नियम है, उसे सुनो। सामबेदमें श्रीहरिने आहिक ब्राह्मणोंक समान शौचका विधान है। वैष्णव
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1549)
- **Original**: प्रकरणमें इसका निरूपण किया है। अपामार्ग आदि मुनियोंके लिये दुगुना शौच कहा गया है।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1550)
- **Original**: (चिड़चिड़ा या ऊँगा), सिन्धुवार (सँभालू या शुद्धिकी इच्छा रखनेवाले मनुष्यको शौचके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1551)
- **Original**: निर्गुण्डी), आम, करबीर (कनेर), खैर, सिरस, उपर्युक्त नियममें न्यूनता या अधिकता नहीं करनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1552)
- **Original**: जाति (जायफल), पुन्नाग (नागकेसर या कायफल), चाहिये; क्योंकि विहित नियमका उल्लज्नन करनेपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1553)
- **Original**: शाल (साखू), अशोक, अर्जुन, दूधवाला वृक्ष, प्रायक्षित्तका भागी होना पड़ता है। कदम्ब, जामुन, मौलसिरी, उड़ (अढ़ठल) और नारद! अब तुम मुझसे शौच तथा उसके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1554)
- **Original**: पलाश--ये वृक्ष दँतुवनके लिये उत्तम माने गये नियमके विषयमें सावधान होकर सुनो! मिट्टरीसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1555)
- **Original**: हैं। बेर, देवदारु, मन्दार (आक), सेमर, कैंटीले शुद्धि करनेपर ही वास्तविक शुद्धि होती है। ब्राह्मण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1556)
- **Original**: वृक्ष तथा लता आदिको त्याग देना चाहिये। भी इस नियमका उल्लब्लन करे तो वह अशुद्ध ही
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1557)
- **Original**: पीपल, प्रियाल (पियाल), तिन्तिडीक (इमली), है। बाँबीकी मिट्टी, चूहोंकी खोदी हुई मिट्टी और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1558)
- **Original**: ताड़, खजूर और नारियल आदि वृक्ष दँतुवनके पानीके भीतरकौं मिट्टी भी शौचके उपयोगमें न
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1559)
- **Original**: उपयोगमें वर्जित हैं। जिसने दाँतोंकी शुद्धि नहीं लाये। शौचसे बची हुई मिट्टी, घरकी दीवारसे लो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1560)
- **Original**: की, बह सब प्रकार्के शौचसे रहित है। शौचहीन हुईं मिट्टी तथा लीपने-पोतनेके काममें लायी हुई
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1561)
- **Original**: पुरुष सदा अपवित्र होता है। वह समस्त कर्मोंके मिट्टी भी शौचके लिये त्याज्य है। जिसके भीतर
- **Translation**: 

---

