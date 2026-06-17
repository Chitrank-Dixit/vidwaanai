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

### Verse 1 (Sama Ved 0.4321)
- **Original**: 1696. क ईं वेद सुते सचा पिबन्तं कद्‌ बयो दधे । अय॑ यः पुरो विभिनत्त्योजसा मन्दानः शिफ्र्यन्धसः
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4322)
- **Original**: यज्ञ में सबके बीच बैठकर सोमरस पीने वाले इद्धदेव को एवं उनकी आयु को भला कौन जान सकता है? सिर पर रक्षा कबच धारण करके सोमपान से आनन्दित हे इन्द्रदेव ! शत्रु के नगरों को अपने पराक्रम से ध्वस्त करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4323)
- **Original**: 1697, दाना मृगो न वारणः पुरुत्रा च रथं दथे । न किष्ट्वा नि यमदा सुते गमो महाँश्षरस्योजसा
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4324)
- **Original**: अपने ओज से विचरण करने वाले, हमारे लिए सम्माननीय हे इन्द्रदेव ! इस सोमयज्ञ में पधारें । शत्रु की खोज में घूमने वाले मतवाले हाथी के समान, आपको रथ लेकर यज्ञ में जाने से कोई रोक नहीं सकता
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4325)
- **Original**: 1698. य उग्र: सनन्‍ननिष्ट्ठत: स्थिरो रणाय संस्कृत: । यदि स्तोतुर्मघवा श्रृणवद्धवं नेन्द्रो योषत्या गमत्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4326)
- **Original**: जो शख्रों से सुसज्जित युद्ध भूमि में स्थिर रहने वाले हैं, ऐसे अपराजेय, पराक्रमी, वैभवशाली इन्द्रदेव हमारी स्तुतियों को सुनकर दूसरी जगह न जाकर इस यज्ञ में ही उपस्थित होंगे
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4327)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4328)
- **Original**: चतुर्थ खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4329)
- **Original**: 1699. पवमाना असृक्षत सोमा: शुक्रास इन्दव: । अभि विश्वानि काव्या
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4330)
- **Original**: शुभ ज्योतिर्मय पवित्रता को प्राप्त होने वाला सोमरस, वेदमत्नों की स्तुतियों के साथ याजकों द्वारा शोधित किया जाता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4331)
- **Original**: 9700, पवमाना दिवस्पर्यन्तरिक्षादसृक्षत। पृथिव्या अधि सानवि
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4332)
- **Original**: संस्कारित होने वाला दिव्य साम अन्तरिक्ष से धरती के ऊँचे भाग पर्वत शिखरों में प्रवाहित होता है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4333)
- **Original**: 17019. पवमानास आशव:ः शुभ्रा असुग्रमिन्दव:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4334)
- **Original**: घ्नन्तो विश्वा अप द्विघ:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4335)
- **Original**: पवित्रता को प्राप्त होने वाला, उज्ज्वल सोमरस, विकारों का शमन करते हुए तीव्र गति से सुपात्र में स्थिर हो रहा है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4336)
- **Original**: 170 2. तोशा वृत्रहणा हुवे सजित्वानापराजिता। इन्द्राग्गी वाजसातमा
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4337)
- **Original**: दुष्ट-दुराचारियों, शत्रुओं का हनन कर, हमेशा युद्ध में विजय प्राप्त करने वाले, अपराजेय, साथकों को अपार वैभव प्रदान करने वाले, इन्द्र और अग्निदेव की हम वन्दना करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4338)
- **Original**: उत्तरा्चिके अषप्टादशो5थ्याय: 18.7 1703. प्र वामर्चनत्युक्थिनो नीथाविदो जरितार: । इन्द्राग्गी इष आ वृणे
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4339)
- **Original**: हे इन्द्र और अग्निदेव ! बैदिक मत्रों का पाठ करने वाले एवं सामगान करने वाले याजकगण आपकी वन्दना करते हैं। हम भी धन- धान्य की कामना से आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4340)
- **Original**: 1704.इन्द्राग्नी नवर्ति पुरो दासपलीरधूनुतम्‌ । साकमेकेन कर्मणा
- **Translation**: 

---

