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

### Verse 1 (Mahabharat 0.5521)
- **Original**: मद्धराजके ऊपर बड़े वेगसे चल्लाया; जोस्से फेंकनेके कारण उससे आगकी चिनगारियाँ छूटने लगीं। पाण्डबॉने चन्दन; माल्य और उत्तम आसन आदिके द्वारा सदा ही उस क्षक्तिकी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5521)
- **Original**: मद्धराजके ऊपर बड़े वेगसे चल्लाया; जोस्से फेंकनेके कारण उससे आगकी चिनगारियाँ छूटने लगीं। पाण्डबॉने चन्दन; माल्य और उत्तम आसन आदिके द्वारा सदा ही उस क्षक्तिकी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5522)
- **Original**: पूजा की थी, वह प्रथकालीन अभ्रिके समान प्रज्वलित तथा
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5522)
- **Original**: पूजा की थी, वह प्रथकालीन अभ्रिके समान प्रज्वलित तथा
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5523)
- **Original**: अ्र्बा अड्डिराद्वारा उत्पन्न की हुई कृत्याके समान भयंकर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5523)
- **Original**: अ्र्बा अड्डिराद्वारा उत्पन्न की हुई कृत्याके समान भयंकर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5524)
- **Original**: झल्यपर्व ] अल्यवध 107 आशजणख।:/:जाेअल्ल्ल्ल्लस्‍कस्‍कक मकत[्‌ाोतो)0मम+-+- कतक्‍ततन्‍-स्‍तत्चचब न्न्-पओ-नियय-.7तऑऑऑऑल_कक»0-»---.+#कऋह थ्री। उसमें जललर, धरखर तथा नभचर जीवॉंको भी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5524)
- **Original**: झल्यपर्व ] अल्यवध 107 आशजणख।:/:जाेअल्ल्ल्ल्लस्‍कस्‍कक मकत[्‌ाोतो)0मम+-+- कतक्‍ततन्‍-स्‍तत्चचब न्न्-पओ-नियय-.7तऑऑऑऑल_कक»0-»---.+#कऋह थ्री। उसमें जललर, धरखर तथा नभचर जीवॉंको भी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5525)
- **Original**: यह सभी गुणोंमें अपने भाईकी बराबरी करता था। झल्यके बलपूर्वक नष्ट करनेकी झक्ति थी। विश्वकर्माने ब्रह्मचयांदि
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5525)
- **Original**: यह सभी गुणोंमें अपने भाईकी बराबरी करता था। झल्यके बलपूर्वक नष्ट करनेकी झक्ति थी। विश्वकर्माने ब्रह्मचयांदि
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5526)
- **Original**: मारे जानेपर वह पाण्डुनन्दन युथिष्ठिरपर चढ़ आया और बड़ी नियमोंका पालन करके उसका निर्माण किया था, वह ब्रह्म . झीघताके साथ उन्हें नाराचोंका निझाना बनाने लूगा। तब द्रोहियोंका विनाप करनेवाल्ली और लक्ष्य बेघनेमें अचूक थी।
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5526)
- **Original**: मारे जानेपर वह पाण्डुनन्दन युथिष्ठिरपर चढ़ आया और बड़ी नियमोंका पालन करके उसका निर्माण किया था, वह ब्रह्म . झीघताके साथ उन्हें नाराचोंका निझाना बनाने लूगा। तब द्रोहियोंका विनाप करनेवाल्ली और लक्ष्य बेघनेमें अचूक थी।
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5527)
- **Original**: धर्मराजने उसे छः बाणोंसे बींध डाला और दो क्षुराकार बल और प्रयत्रके द्वारा उसका वेग बहुत बढ़ गया था।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5527)
- **Original**: धर्मराजने उसे छः बाणोंसे बींध डाला और दो क्षुराकार बल और प्रयत्रके द्वारा उसका वेग बहुत बढ़ गया था।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5528)
- **Original**: सायकोंसे उसके धनुष तथा ध्वजाको भी काट गिराया। युधिप्ठिरने उसे भयंकर मन्च्नोंसे अधिमन्खित करके बड़े यत्रके
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5528)
- **Original**: सायकोंसे उसके धनुष तथा ध्वजाको भी काट गिराया। युधिप्ठिरने उसे भयंकर मन्च्नोंसे अधिमन्खित करके बड़े यत्रके
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5529)
- **Original**: साथ अपने शत्रु मद्रराजपर छोड़ा था। एक तो वह पूरा बल
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5529)
- **Original**: साथ अपने शत्रु मद्रराजपर छोड़ा था। एक तो वह पूरा बल
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5530)
- **Original**: लरूगाकर छोड़ी गयी थी, दूसरे उसकी झक्तिको रोकना
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5530)
- **Original**: लरूगाकर छोड़ी गयी थी, दूसरे उसकी झक्तिको रोकना
- **Translation**: 

---

