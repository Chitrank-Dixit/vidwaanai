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

### Verse 1 (Vaivtpuran 56.19354)
- **Original**: राधा रक्षतु प्राच्यां च बह्लौ कृष्णप्रियाबतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.19355)
- **Original**: दक्षे रासेश्वरी पातु गोपीशा नैऋतेडलतु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.19356)
- **Original**: पश्चिमे निर्गुणा पातु बायव्ये कृष्णपूजिता। उत्ते . संततं पातु मूलप्रकृतिरीश्वरी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.19357)
- **Original**: सर्वेश्वरी सदैशान्यां पातु मां सर्वपूजिता । जले स्थले चान्तरिक्षे स्वप्रे जागरणे तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.19358)
- **Original**: महाविष्णोश्न जननी सर्वतः पातु संततम्‌ । कब्च॑ कधथित॑ दुर्ग श्रीजगन्मड्रल॑ परम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.19359)
- **Original**: यअस्मै कस्मे न दातव्यं गूढाद्‌ गृढ़तरं परम्‌ । तब स्लेहान्मयाख्यातं प्रवक्तव्य॑ न कस्यचित्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.19360)
- **Original**: गुरुभभ्यर््यय विधिवद्‌._ वस्त्रालंकारचन्दनै; । कण्ठे वा दक्षिणे बाहौ धृत्वा विष्णुसमों भवेत्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.19361)
- **Original**: शतलक्षजपेनैव सिद्ध॑ च कवच भवेत्‌ । यदि स्यथात्‌ सिद्धकवचों न दग्धो वह्िना भवेत्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.19362)
- **Original**: एतस्मात्‌ कवचाद्‌ दुर्ग राजा दुर्योधन: पुरा । विशारदों जलस्तम्भे वहिस्तम्भे च निश्चितम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.19363)
- **Original**: मया सनत्कुमाराय पुरा दत्त चर पुष्करे। सूर्यपर्वण मेरा च स॒सान्दीपनये ददौ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.19364)
- **Original**: खलाय तेन दत्त तर ददौ दुर्योधनाय सः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.19365)
- **Original**: कवचस्य॒ प्रसादेन जीवन्मुक्तो भवेन्नर:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.19366)
- **Original**: नित्यं पठति भक्त्येदं॑ तन्मन्रोपासकश्न॒ यः। विष्णुतुल्यो भवेत्रित्य॑ राजसूयफल लभेतू
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.19367)
- **Original**: सस्‍्नानेन सर्वतीर्थानां सर्वदानेन यत्फलम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.19368)
- **Original**: सर्वव़तोपवासे च॒ पृथिव्याश्च॒ प्रदक्षिणे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.19369)
- **Original**: सर्वयज्ञेषु दीक्षायां नित्य च सत्यरक्षणे । नित्य श्रीकृष्णसेवायां. कृष्णनैवेह्यभक्षणे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.19370)
- **Original**: पाठे चतुर्णा बेदानां यत्फलं॑ च लभेन्नर: । तत्फलं॑ लभते नूनं पठनात्‌ कबचस्थ च
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.19371)
- **Original**: राजद्वारे श्मशाने च सिंहव्याप्रान्विति बने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.19372)
- **Original**: दाबाग्नौँ संकटे चैव दस्युचौरान्विति भवे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.19373)
- **Original**: कारागारे विपदग्रस्ते घोरे च॑ दृढबन्धने । व्याधियुक्तों भवेन्मुक्तो धारणात्‌ कबचस्यथ च
- **Translation**: 

---

