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

### Verse 1 (Vishnu Puran 0.5621)
- **Original**: प्राज्ञ पुरुष कलह न बढ़ाये तथा व्यर्थ वैरका भी त्याग करे। थोड़ी-सी हानि सह ले, किन्तु बैरसे कुछ लाभ होता हो तो उसे भी छोड़ दे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5622)
- **Original**: स्नान करनेके अनन्तर स्रानसे भीगी हुई धोती अथवा हाथोंसे शरीरकों न पोंछे तथा खड़े-खड़े केशोंकों न झाड़े और आचमन भो न करे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5623)
- **Original**: पैरके ऊपर पैर न रखे, गुरुजनॉके सामने पैर न फैलाले और धृष्टतापूर्वक उनके सामने कभी उच्चासनपर न बैठे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5624)
- **Original**: देवारुय, चौराहय, माज़ल्कि द्रव्य और पूज्य व्यक्ति---इन सबको बायीं ओर रखकर न निकले तथा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5625)
- **Original**: 202 सोमाक्काम्न्यम्युवायूनां पूज्यानां च न सम्पुखम्‌ । कुर्याश्रिष्टीवविण्पूत्रसमुत्सुग च पण्डित:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5626)
- **Original**: 27 तिष्ठन्न मूत्रयेत्तदत्पथ्िष्नपि न॒मूत्रयेत्‌ । इल्लेष्मविण्मून्ररक्तानि सर्वदेव न लक्बयेत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5627)
- **Original**: 28 इलेष्मशिद्लाणिकोत्सगों नान्नकाले प्रशस्थते । बलिपडुलजप्यादी न होमे न महाजने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5628)
- **Original**: 29 योषितो नावमन्येत न चासां विश्वसेद बुध: । न चैवेष्ष्या भवेत्तासु न घिक्क॒र्यात्कदाचन
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5629)
- **Original**: 30 मडन्‍ल्यपुष्परलाज्यपूज्याननभिवाद्य.. च। न निष्क्रमेद गृहात्माज्ञस्सदाचारपरों नर:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5630)
- **Original**: 39 चअतुष्पथान्नमस्कुर्यात्काले होमपरो भवेत्‌। दीनानभ्युद्धरेत्साधूनुपासीत. बहुभ्रुतान्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5631)
- **Original**: 32 देवर्षिपूजकस्सम्यक्पितृपिण्डोदकप्रदः_। सत्कर्ता चानिथीना यः स लोकानुत्तमान्जेत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5632)
- **Original**: 33 स याति ल्मेकानाहादहेतुभूतान्पाक्षयान्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5633)
- **Original**: 34 धीपान्हीमान्क्षमायुक्तो हास्तिको विनयान्वितः । विद्याभिजनवृद्धानां याति लोकाननुत्तमान्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5634)
- **Original**: 35 अकालगर्जितादौ च्न पर्वस्वाशौचकादिषु । अनध्यायं बुध: कुर्यादुपरागादिके तथा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5635)
- **Original**: 36 वर्षातपादिषु ऋत्नी दण्डी राज्यटवीपु च
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5636)
- **Original**: आरीरत्राणकामों वै सोपानत्कस्सदा व्रजेत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5637)
- **Original**: 38 नो्ध्व॑ न तिर्यग्दूरं जा न पह्यन्पर्यटेद्‌ बुध: । युगमात्र॑ महीपृष्ठ नरो गच्छेद्गिलोकयन्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5638)
- **Original**: 39 दोषहेतूनशेषांश वश्यात्मा यो निरस्थति। तस्य धर्मार्थकामानां हानिनल्पापि जायते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5639)
- **Original**: 40 पापे5प्यपाप: परुषे हाभिधत्ते प्रियाणि यः । मेन्रीद्रबान्त:करणस्तस्य मुक्ति: करे स्थिता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5640)
- **Original**: 49 श्रीविष्णुपुराण [ अ* 12 इनके विपरीत वस्तुओऑको दायों ओर रखकर न जाय
- **Translation**: 

---

