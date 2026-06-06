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

### Verse 1 (Vaivtpuran 21.18439)
- **Original**: देव्यक्ष मुनयः सर्वे पार्वती स्तोतुमुद्यता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.18440)
- **Original**: धौतवस्त्रा जटाभारं॑ बिश्रती सुत्रता बनते । प्रेरिता परमात्मान ब्रताराध्य॑े शिवेन च
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.18441)
- **Original**: ज्वलदग्रिशिखारूपा . तेजोमूर्तितती सती । तपसां फलदा माता जगतां सर्वकर्मणाम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.18442)
- **Original**: पार्वत्युवाच कृष्ण जानासि मां भद्र नाहं त्वां ज्ञातुमीश्री । के वा जानन्ति वेदज़ा वेदा वा बेदकारका:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.18443)
- **Original**: त्वदंशास्त्यां न जानन्ति कथ॑ ज्ञास्यन्ति त्वत्कला: । त्व॑ चापि तत्ब॑ जानासि किमन्ये ज्ञातुमीश्चरा:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.18444)
- **Original**: सूक्ष्मात्‌ सूक्ष्मतमो व्यक्त: स्थूलात्‌ स्थूलतमो महान्‌ । विश्वस्त॑ विश्वरूपश्ष॒विश्वजीज॑ सनातनः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.18445)
- **Original**: कार्य त्व॑ कारण त्वंच्त कारणानां च॒ कारणम्‌ । तेजःस्वरूपो भगवान्‌ निराकारों निराश्रय:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.18446)
- **Original**: निर्लिप्तो निर्गुण: साक्षी स्वात्माराम: परात्पर: । प्रकृतीशों विराडबीज॑ विराड्रूपस्त्वमेव च। सगुणस्त्व॑ प्राकृतिक: कलया सृष्टिहेत॒वे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.18730)
- **Original**: 820 + संक्षिम ख्रह्मवैयर्तपुराण + #%%&#%4%%%%%$%$%%#### ## ## ##%##### ##############क्र# 4 4446 ####क## 44 कं #
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.18731)
- **Original**: # 4 ## #&##
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.18732)
- **Original**: # # ## # क्रीडन्तं राथया सार्थ वृन्दारण्ये च॒ कुत्रचित्‌ । कुत्रचित्रिर्जने5रण्ये राधावक्ष:स्थलस्थितम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.18733)
- **Original**: जलक़ीडां प्रकुर्वन्त॑ राधया सह कुत्रचित्‌ । राधिकाकबरीभार॑ कुर्बन्त॑ कुत्रचिद बने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.18734)
- **Original**: कुत्रचिद राधिकापादे._ दत्तवन्तमलक्तकम्‌ । राधाचर्चितताम्बूलं॑ गृहन्त॑ कुज़चिन्मुदा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.18735)
- **Original**: पश्यन्त॑ कुत्रचिद्‌ गधां पश्यन्ती बक़्चक्षुषा। दत्तवन्तं चर राधाये कृत्वा मालां च्व कुत्रचित्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.18736)
- **Original**: कुत्रच्चिद्‌ राथया सार्थ गच्छन्तं रासमण्डलम्‌। राधादत्तां गले मालां धृतबन्त॑ चर कुत्रचितू
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.18737)
- **Original**: सार्थ गोपालिकाभिश्च विहरन्तं च कुत्रचित्‌। राधां गृहीत्वा गच्छन्तं विहाय तां क्र कुत्रचित्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.18738)
- **Original**: विप्रपलीदत्तमन्न भुक्तवन्त॑ उच्॒कुत्रचित्‌ । भुक्तबन्त॑ तालफलं बालकै: सह कुत्रचित्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.18739)
- **Original**: वस्त्र गोपालिकानां च हरन्तं कुत्रचिन्मुदा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.18740)
- **Original**: गवां -गणं व्याहरन्तं॑ कुत्रचिद्‌ बालक: सह
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.18741)
- **Original**: कालीयपूर्श्ध पादाब्ज॑ दत्तवन्तं च कुत्रचित्‌
- **Translation**: 

---

