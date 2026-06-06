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

### Verse 1 (Garuda1 0.221)
- **Original**: शह्डरक्षेक सर्वश्ष क्षान्तिद: .. क्षान्तिकृलरः।
- **Translation**: 

---

### Verse 2 (Garuda1 0.222)
- **Original**: डे8 * पुराणं गारुड वक्ष्ये सारं विष्णुकथाशअयम्‌ * [ संक्षिप्त गरुडपुराणाडु 440200000000 0 003030024//05000024]44400 03033 44]4]4 05050 0802800802080808 8 9 या] ]]]]घ]ॉ] भक्तप्रियस्तथा भरत्ता भक्तिमानू भक्तिवर्धन:
- **Translation**: 

---

### Verse 3 (Garuda1 0.223)
- **Original**: भक्तस्तुतो. भक्तपरः कीर्तिदः . कीर्तिवर्धन:। कीर्शिदीएिः . क्षमाकान्तिर्धक्तझैव दया. परा
- **Translation**: 

---

### Verse 4 (Garuda1 0.224)
- **Original**: दान॑ दाता च॑ करता चर देवदेवप्रिय: शुक्तिः
- **Translation**: 

---

### Verse 5 (Garuda1 0.225)
- **Original**: शुत्तिमान्‌ू सुखदों मोक्ष: कामआर्थ: सहखपात्‌
- **Translation**: 

---

### Verse 6 (Garuda1 0.226)
- **Original**: सहस्वशीर्षा वैद्य्ष मोक्षद्वारं तथेय च। प्रजाद्ररां सहखाक्ष: सहख्ककर एव... चा
- **Translation**: 

---

### Verse 7 (Garuda1 0.227)
- **Original**: शुक्रश्न ( सुधु: ) सुकिरीटी च॒ सुग्रीव: कौस्तुभस्तथा। प्रदुप्नशानिरुद्धशव हयगशीवक्ष सूकर:
- **Translation**: 

---

### Verse 8 (Garuda1 0.228)
- **Original**: मत्स्य: परशुरामश्ष प्रह्वादा बलिरेव च। शगण्यश्वैव नित्यश्न॒बुद्धों मुक्त: शरीरधृत्‌
- **Translation**: 

---

### Verse 9 (Garuda1 0.229)
- **Original**: खरदूषणहन्ता उच रावणस्थप प्रमर्दत:। सीतापतिश्ष. यर्थिष्णुभंरतश्च॒ तशैव च्ा
- **Translation**: 

---

### Verse 10 (Garuda1 0.230)
- **Original**: कुम्भेदजिनिहन्ता.. चर कुख्थकर्णप्रमर्दन:। तरासकासकश्षैय देवान्तकविनाशन:
- **Translation**: 

---

### Verse 11 (Garuda1 0.231)
- **Original**: दुष्टासुरनिहतता था शब्बरारिस्तथैय च। नरकस्प निहन्ता च॑ तिशीर्षस्प विनाशन:
- **Translation**: 

---

### Verse 12 (Garuda1 0.232)
- **Original**: यमलारजुनभेत्ता है तपोहितकरस्तथा। वादिष्न चैंव याहां च॒ बुद्धक्लैव वरप्रदः
- **Translation**: 

---

### Verse 13 (Garuda1 0.233)
- **Original**: सार: सारप्रियः सौरः कालहन्तृनिकृत्तन:। अगस्त्वो. देवलक्षव गारदो. तारदप्रियः
- **Translation**: 

---

### Verse 14 (Garuda1 0.234)
- **Original**: प्राणोउपानस्तथ्वा व्यानों रज: सत्ततं तमः शारत्‌। उदानक्ष समानक्ष भेषज॑ थ॑ भिषक्‌ तंथा
- **Translation**: 

---

### Verse 15 (Garuda1 0.235)
- **Original**: कूटस्थः स्वच्छरूपञ सर्वदेहविवर्जित:। अश्षुरिन्द्रियहीनक्ष खागिन्द्रियविवर्खित:
- **Translation**: 

---

### Verse 16 (Garuda1 0.236)
- **Original**: इस्तेन्द्रिपविहीनश्ल॒ पादाभ्यां चर विवर्जितः। पायूपस्थविही नश्व म्रहातापविवर्जित:
- **Translation**: 

---

### Verse 17 (Garuda1 0.237)
- **Original**: प्रवोधेन विहीनश्च॒युदध्या चैव विवर्जित:। चेतसा सिगतझ्ैव प्राणेक जल वियर्जित:
- **Translation**: 

---

### Verse 18 (Garuda1 0.238)
- **Original**: अपातेन विहीनश्च॒ व्यानेन च्॒ विवर्जितः:। उदानेन विहीनक्ष॒ समातेत विवर्जित:
- **Translation**: 

---

### Verse 19 (Garuda1 0.239)
- **Original**: आकाशेत विहीनक्ष॒ बायुना परिवर्जित:। अग्निना च विहीनश्॒ उदकेन विवर्जित:
- **Translation**: 

---

### Verse 20 (Garuda1 0.240)
- **Original**: पृथिव्या खा विहीनक्ष शब्देन चथ॑ विधर्जित:। स्पफ्शेंव च॑ विहीतक्ष सर्वरूपविवर्जित:
- **Translation**: 

---

