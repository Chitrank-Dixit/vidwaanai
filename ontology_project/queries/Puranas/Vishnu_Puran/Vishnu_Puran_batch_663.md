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

### Verse 1 (Vishnu Puran 0.13241)
- **Original**: ततल्ामस्तसैन्येन -« 5 प्ररेक॑:हर1 त्तस्तत्पदानादवज्ञातम्‌ 4 “37 ए्6
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13242)
- **Original**: सवस्ु केसनोद्ोगम ++.. 5 उडी 7 फंड परतैक्षासावानक्ुत्टुभिर 4. 14 “₹9-
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13243)
- **Original**: ततरखई पर्ुर्पुफिः 0... छा बैंड ता रह सततश्ष तत्कारप्तत्ानाप्‌ » 7 ह85- 12
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13244)
- **Original**: ततसद्चर् शुल्वा 5. 3670411 चतछतमे के रोषु हे ह
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13245)
- **Original**: 5-- 14- । जतस्तु कोस्कत्सास्थात्‌ 5 3थ77 बट ठदश सझलजान्पहमतरए हु 5678 30-
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13246)
- **Original**: ततस्स वानरोज्थ्येत्य 5. पवध्द 5719 त्तश्व पौरव दुष्पत्तम 4. 16 87 7
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13247)
- **Original**: ततले यौवनोसत्ताः ला ततब्ित्रस्थः 4 5श18 8 श6
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13248)
- **Original**: जाए यादवात्सवें 97737 7538 राज्य यपश्षम्पास्‌ 3. 184 “270
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13249)
- **Original**: ततक्षान्योन्यमम्येत्य 75 इु7- 443 ततश् हर्यश्ष: 4 16 748-
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13250)
- **Original**: ततम्लर्णपरध्येन छुए डृछ- हें कओ्लोपरिषरों ससु: 4 59-80
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13251)
- **Original**: सत्र ददशेतत्र 70 37 5732 कतभ्ाशेफाशविसाइाम्‌ डे 0230 178 .
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13252)
- **Original**: कार्श भाजनाह का उतश्ष तमृपुक्रहाणाः डे 207 5168
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13253)
- **Original**: ठतस्ते पापकर्माण: 6505 रे8 8 7 14 रास्ते खदाणाः डे 408 27...
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13254)
- **Original**: ततएश्रेपु क्ीणेपु 5-7सरे85रू27 ततश्ष मृहद्ाजः 4 71208 6
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13255)
- **Original**: ततस्थुदु:खिते जिष्णुः 50436 “529 ततब्न श्ुद्रकततश् इनक रेरेलीकट कक
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13256)
- **Original**: 6 #59:441536 जतथ्ध सेनजित्तत& 4 7723 77 57
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13257)
- **Original**: ततस्मम्फूज्यते व्याप्म्‌ हक दराकरेतप्मारे8 उठ विधासपूपः 4 7 2441 8 4
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13258)
- **Original**: कस्स मगवान्किणु: श74 8 73 कांग रै7 वह शिवानाभः हैं शहे 8-9.
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13259)
- **Original**: उतस्तस्पातुभाबेग द 3 क 020 लतश्ाजावस्तु: डे 5 24 24
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13260)
- **Original**: ततत्तापफौतातु 6 प*3ततमीरिंट ततड नव चैताक्नदात्‌ डे जब पेय च्तक्षापो इतसा: हह/#:%8243& खाद कृष्णनामा ड:रड डंडे ततस्तु मूलमासाप द्॑गऋंडः -->26 गतआरिश्कर्मा डे रह ड6।
- **Translation**: 

---

