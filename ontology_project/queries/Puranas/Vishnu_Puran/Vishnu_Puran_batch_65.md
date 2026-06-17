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

### Verse 1 (Vishnu Puran 0.1281)
- **Original**: 14 श्रीपराशरजी बोले--हे मैत्रेय ! यह सब सुनकर राजपुत्र घुव उन ऋषियोंक्य्रे प्रणामकर उस बनसे चल दिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1282)
- **Original**: और हे द्विज! अपनेको कृतकृत्य-सा मानकर वह यमुनातटवत्तों अति पत्रित्र मघु नामक बनमें आया। आगे चलक़र उस कनमें मधु नामक टैत्य रहने लगा था, इसलिये वह इस पृथ्वीतलूमें मधुबन नामसे ब्रिख्यात हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1283)
- **Original**: यहीं मधुके पुत्र लवण नामक महानली राक्षसक्रों मारकर झत़ुप्नने मधुरा (मथुर) नामकी पुरी बसायी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1284)
- **Original**: जिस (मशुबन) में निरन्तर देवदेव श्रीहरिकी सत्रिधि रहती है उसी सर्वपापापहारी तीर्थमें घुबने तपस्या की
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1285)
- **Original**: मरीचि आदि मुनीश्चरोंने उसे जिस प्रकार उपदेश किया था उसने उसी प्रकार अपने इृदयमें विराजमान निखिलदेवेश्वर श्रीविष्णुभगवान्‌क्ा ध्यान करना आरम्भ किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1286)
- **Original**: इस प्रकार हे विप्न ! अनन्य-चित्त होकर ध्यान करते रहनेसे उसके हृदयमें सर्वभूतान्तर्यामी भगवान्‌ हरि. सर्वतोभानसे प्रकट हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1287)
- **Original**: है मैत्रेच! योगी धुक्‍्के चित्तमें भगवान्‌ विष्णुके स्थित हो जानेपर सर्वभूतोंकों धारण करनेबाली पृथियी उसका भार न सैभाल सकी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1288)
- **Original**: ठसके बायें चरणपर खड़े होनेसे पृथिवीका बायाँ आधा भाग झुक गया और फिर दाँयें चरणपर खड़े होनेसे दायाँ भाग झुक गया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1289)
- **Original**: और जिस समय कह पैरके अगूठेसे पृथिबीको (जीचसे) दबाकर खड़ा हुआ तो पर्वतोके सहित समस्त भूमष्डल बिचलित हो गया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1290)
- **Original**: हे महामुने ! उस समय नदी, नंद और समुद्र आदि सभी अत्यन्त क्षुब्ध हो गये और उनके क्षोभसे देवताओँमें भी बड़ी हलूचल मची
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1291)
- **Original**: है सैत्रेय ! तब याम नामप्रक देजताओने अत्यन्त व्याकुल हो डुन्द्रक्रे साथ परामर्श कर उसके ध्यानकों भजन करनेका आयोजन किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1292)
- **Original**: हे महामुने ! इन्द्रके साथ अति आतुएर कृष्माण्ड नामक उपदेवताओंने नानारूप धारणकर उसकी समाधि भज़ू करना आरम्भ किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1293)
- **Original**: उस समय मायाहीसे रची हुई उसकी माता सुनीति नेत्रोंमें आँसू भरे उसके सामने प्रकट हुई और 'हे पुत्र ! हे पुत्र !! ऐसा कहकर करुणायुक्त वचन बोलने लगी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1294)
- **Original**: 127) पुत्रकास्मात्रिवर्त्त्व शरीरात्ययदारुणात्‌ । निर्बन्धतो मया लव्धो बहुभिस्त्व॑ मनोरथै:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1295)
- **Original**: 95 दीनामेका परित्यक्तुमनाथां न त्वमर्हईसि । सपल्रीबचनाइत्स अगतेस्त्व॑ गतिर्मम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1296)
- **Original**: 16 क्ल चर त्वं पञ्चवर्षोयः क्र चेतहारुणं तपः । निवर्ततां मनः कष्टान्निर्बनधात्फलवर्जितात्‌ ।। 97 काल: क्रीडनकानान्ते तदन्तेउध्ययनस्थ ते । ततः समस्तभोगानां तदन्ते चेष्यते तप:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1297)
- **Original**: 18 काल: क्रीडनकानां यस्तव बालस्य पुत्रक । तस्मिस्त्वमिच्छसि तप: कि नाशायात्मनो रत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1298)
- **Original**: 19 मत्ीति: परमो धर्मो बयो5बस्थाक्रियाक्रमम्‌ । अनुकर्त्तस्व मा मोहान्निवर्तास्मादधर्मत:ः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1299)
- **Original**: 20 परित्यजति वत्साद्य यद्येत्न भवांस्तप:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1300)
- **Original**: त्यक्ष्याम्यहमिह प्राणांस्ततो बै पद्यतस्तव
- **Translation**: 

---

