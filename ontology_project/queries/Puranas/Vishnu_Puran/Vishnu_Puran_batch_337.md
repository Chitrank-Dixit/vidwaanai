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

### Verse 1 (Vishnu Puran 0.6721)
- **Original**: नागाधिपतिगण नागलोकमें स्त्रैट आये और पुल्कृत्सको स्तनेके लिये [अपनी बहिन एवम्‌ पुरुकुत्सकी भार्या] नर्मदाको प्रेरित किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6722)
- **Original**: तदनन्तर नर्मदा पुरुकृत्सको रसातलमें ले आयी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6723)
- **Original**: रसातकमें पहुँचनेपर पुरुकुत्सने भगवानके तेजसे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6724)
- **Original**: आ*3 ] वीर्यस्सकलगदश्धर्वान्निजघान
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6725)
- **Original**: पुनअ स्वपुरमाजगाम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6726)
- **Original**: सकलपन्नगाधि- पतयश्च नर्मदायै बर॑ ददुः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6727)
- **Original**: यस्तेडनुस्मरणसमवेतं नाम्ग्रहणं करिष्यति न तस्य सर्पविषभयय भविष्य- तीति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6728)
- **Original**: अन्न च इलोक:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6729)
- **Original**: नर्मदाये नमः प्रातर्नर्मदाये नमो निशि। नमोस्तु नर्मदे तुभ्यं त्राहि मां विषसर्पत:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6730)
- **Original**: 13 इत्युच्चार्याहर्निशमन्धकारप्रवेशे वा सर्पर्न दहयते न चापि कृतानुस्मरणभुजो विषमपि भुक्तमुपघाताय भवतति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6731)
- **Original**: पुरुकुत्साय सन्ततिविच्छेदो न भविष्यतीत्युरगपतयो वर ददुः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6732)
- **Original**: पुरुकृत्सो नर्मदायां त्रसहस्युमजीजनत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6733)
- **Original**: त्रसदस्युतस्सम्यूतो5नरण्यः, य॑ रावणो दिग्विजये जघान
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6734)
- **Original**: अनरण्यस्य पृषदश्चः पृषद्श्वस्थ हर्यश्च: पुत्रो>अमवत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6735)
- **Original**: तस्य चल हस्तः पुत्रो>भवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6736)
- **Original**: ततश्न सुमनास्तस्यापि ब्रिधन्जा त्रिधन्चनख्रय्यारुणि:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6737)
- **Original**: त्रय्यारुणे- स्सत्यव्रत:,यो5सौ त्रिशड्डुसंज्ञामनाप
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6738)
- **Original**: स॒चाण्डालतामुपगतश्च
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6739)
- **Original**: द्वादश वार्षिक्यामनावृष्टणं विशधामित्रकल्ञापत्य पोषणार्थ चाण्डालप्रतिग्रहपरिहरणाय च जाह्नवी तीरन्यग्रोथे मृगमांसमनुदिनं बबन्ध
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6740)
- **Original**: स॑ तु. परितुष्टेन विश्वामित्रेण सशरीरस्स्वर्ग- प्रारोपित:
- **Translation**: 

---

