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

### Verse 1 (Vishnu Puran 0.11981)
- **Original**: उन सब पाण्डु-पुत्रोनि अर्जुनके मुखसे व्यासजीका सन्देश सुनकर राज्यपदपर परीक्षित॒को अभिषिक्त किया और स्वयं वनको चले गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11982)
- **Original**: हे मैत्रेय ! भगवान्‌ वासुदेखने यदुवंद्वामें जन्म केकर जो-जो स्वेल्मएँ की थीं वह सब मैंने विस्तारपूर्वक तुम्हें सुना दीं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11983)
- **Original**: जो पुरुष भगवान्‌ कृष्णके इस चरित्रको सर्वदा सुनता है बह सम्पूर्ण पापोंसे मुक्त होकर अन्तमें विष्णुल्त्रेककों जाता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11984)
- **Original**: ल्च कै ततततत कर इति श्रीविष्णुपराणे पञ्ममेंडशे अष्टात्रिशोउध्याय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11985)
- **Original**: ग्र्ाः, नी इति श्रीपराहशरमुनिविरचिते श्रीविष्णुपरत्वनिर्णायके श्रीमति विष्णुमहापुराणे फपश्षमोंडईश: समाप्तः । न है ---
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11986)
- **Original**: 35 आमन्नारायणाय नम: श्रीविष्णुपुराण घषष्ठ अंश पहला अध्याय कलिथर्मनिरूपण श्रीमेत्रेय उवाच व्याख्याता भवता सर्गवंशमन्वन्तरस्थिति: । बंशानुचरितं चैव विस्तरेण महामुने
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11987)
- **Original**: 1 श्रोतुमिच्छाम्यह॑त्कत्तो यथावदुपसंहतिम्‌। महाप्रलयसंज्ञां च कल्पान्ते च महामुने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11988)
- **Original**: 2 औपराशर उवाच मैत्रेय श्रूयतां मत्तो यथावदुपसंहति: । कल्पान्ते प्राकृते चैव प्ररये जायते यथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11989)
- **Original**: 3 अहोर िणी तु मासो5ब्द्खिदिवौकसाम्‌ । परम सही तु ब्रह्मणो वे द्विजोत्तम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11990)
- **Original**: 4 कृत त्रेता द्वापरं च कलिश्लेति चतुर्युगम्‌। तद्द्वादशभिरुच्यते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11991)
- **Original**: 5 चतुर्युगाण्यझेषाणि सदृशानि स्वरूपत: । आइ्य॑ कृतयुगं मुक्त्वा मैत्रेयान्त्यं तथा कलिम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11992)
- **Original**: 6 आह्ये कृतयुगे सर्गो ब्रह्मणा क्रियते यथा । क्रियते जोपसंहारस्तथान्ते च कल्मे युगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11993)
- **Original**: 7 कलेस्स्बरूप॑ मैत्रेय यद्भवाञ्कोतुमिच्छति । तब्निबोध समासेन वर्तते यन्पहामुने
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11994)
- **Original**: 9 वर्णाश्रमाचारवती प्रवृत्तिन कलौ नृणाम्‌। सामऋग्यजुर्धम॑विनिष्पादनहैतुकी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11995)
- **Original**: । 10 विवाहा न कलौ धर्म्या न शिष्यगुरुसंस्थिति: । न दाम्पत्यक्रमो नैव वहिदेवात्मक: क्रम:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11996)
- **Original**: 99 श्रीमैत्रेयजी बोले-- हे महासुने ! आपने सृष्टिरचना, वडा-परम्परा और मन्वन्तरोंकी स्थितिका तथा वंशोंकि चर्त्रोंका विस्तारसे वर्णन किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11997)
- **Original**: अब मैं आपसे कल्पान्तमें होनेवाले महाप्रकय नामक संसारके उपसंहास्का यथावत्‌ वर्णन सुनना चाहता हूँ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11998)
- **Original**: श्रीपराहरजी बोल्े--हे मैत्रेय
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11999)
- **Original**: कल्पात्तके समय प्राकृत प्रल्यमें जिस प्रकार जीवोका उपसंहार होता है, वह सुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12000)
- **Original**: हे द्विजोत्तम ! मनुष्योंका एक मास पितृगणका, एक वर्ष देवगणक्त्र और दो सहस्र चतुर्युग ब्रह्माका एक दिन-रात होता है
- **Translation**: 

---

