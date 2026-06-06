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

### Verse 1 (Sama Ved 0.2141)
- **Original**: है अनाधिपति, बलवान्‌ इन्द्रदेव ! गाय के दूध में मिलाये गये मधुर सोमरस का पान करके आप आनन्दित हों । आलसी ब्राह्मण की धाँति निष्क्रिय न रहें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2142)
- **Original**: 827.इनद्रं विश्वा अवीवृधन्त्समुद्रव्यचसं गिर: । रथीतमं रथीनां बाजानां सत्पर्ति पतिम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2143)
- **Original**: समुद्र के समान विशाल, महारथी, बलों के स्वामी, देवी शक्तियों के संरक्षक इद्धदेव की प्रशंसा सभी स्तुतियों द्वारा की जाती हैं जिनसे उनका यश बढ़ता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2144)
- **Original**: 828.सख्ये त इन्द्र वाजिनो मा भेम शवसस्पते
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2145)
- **Original**: त्वामभि प्र नोनुमो जेतारमपराजितम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2146)
- **Original**: हे बलरक्षक इन्द्रदेव ! आपकी मित्रता में हम बलशाली होकर किसी से न डरें। है अपराजित विजयी इन्द्रदेव ! हम साधकगण आपको प्रणाम करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2147)
- **Original**: 829.पूर्वीरिद्वस्थ रातयो न वि दस्वन्त्यूतय: । यदा वाजस्य गोमत स्तोतृभ्यो मंहते मघम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2148)
- **Original**: देवराज इद्ध की दानशीलता सनातन है । सूर्य रश्मियों के माध्यम से उत्पन्न अन्नादि पोषक तत्त्व, जब वह स्तोताओं को देते हैं, तब याजक का दान क्षीण नहीं होता
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2149)
- **Original**: इति षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2150)
- **Original**: के के के
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2151)
- **Original**: झ8 सामवेद-संहिता ऋषि, देवता, छन्‍्द-विवरण ऋषि- जमदरिन भार्गव 775-777 । अमहीयु आइ्रिरस 778-780, 787-789,815-817
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2152)
- **Original**: कश्यप मारीच 781-783 । भृगु वारुणि अथवा जमदग्नि भार्गव 784-786, 803-805
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2153)
- **Original**: मेधातिथि काण्व 790-995
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2154)
- **Original**: मधुच्छन्दावैश्वामित्र 796-799। वसिष्ठमैत्रावरण 800-802। उपमन्यु वासिष्ठ 806-808 । शंयु बार्हस्पत्य 809-810 । वालखिल्य प्रस्कण्व काण्व 811-812 । नृमेघ आइ्विरस 813, 814 । नहुष मानव 818-820 । सिकता निवावरी 821-822 । पृश्नियो5जा 823 । श्रुतकक्ष अथवा सुकक्ष आड्रिरस 824-826 । जेता माधुच्छन्दस 8 27-829
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2155)
- **Original**: देवता- पवमान सोम 775-789, 803-808, 815-829। अग्नि 790-792
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2156)
- **Original**: । भित्रांवरुण 793-795
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2157)
- **Original**: इन्द्र 796-799, 809-814 । इन्द्राग्गी 800-802। छन्द- गायत्री 775-805, 815-817, 824-829 । त्रिष्टप्‌ 806-808 । बार्हत प्रगाथ (विषमा बृहती, समा सतोबृहती) 809-814 । अनुष्टप्‌ 818-823 ।
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2158)
- **Original**: इति तृतीयोउ ध्याय:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2159)
- **Original**: गा मा ली
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2160)
- **Original**: अथ चतुर्थो5 ध्याय:
- **Translation**: 

---

