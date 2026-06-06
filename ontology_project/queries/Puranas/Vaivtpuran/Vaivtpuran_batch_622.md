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

### Verse 1 (Vaivtpuran 56.5352)
- **Original**: 35 रां राधेति चतुर्ध्यनन॑ वहिजायान्तमेक च॑ । सर्वसिद्धिप्रद: पातु कपोल॑ नासिकां मुखम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.5353)
- **Original**: क्लीं श्रीं कृष्णप्रिया डेउन्त॑ कण्ठं पातु नमोउन्तकम्‌ । 3* रां रासेश्वरी डेउन्त॑ स्कन्ध॑ पातु नमो$न्तकम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.5354)
- **Original**: 3» रां रासविलासिन्ये स्वाहा पृष्ठ॑ सदावतु । वृन्दावनविलासिन्ये स्वाहा वक्ष: सदावतु
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.5355)
- **Original**: तुलसीवनवासिन्ये॑ स्वाहा पातु नितम्बकम्‌ । कृष्णप्राणाधिका डेउन्त॑ स्वाहान्त॑ प्रणवादिकम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.5356)
- **Original**: पादयुप्म॑ च. सर्वाड्र संतत पातु सर्वतः: । राधा रक्षतु प्राच्यां च वहौ कृष्णप्रियावतु
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.5357)
- **Original**: दक्ष रासेश्री पातु गोपीशा नैऊऋतेउवतु । पश्चिमे निर्गुणा पातु वायब्ये कृष्णपूजिता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.5358)
- **Original**: उत्तरे संतर्त॑ पातु मूलप्रकृतिरी भ्वरी । सर्वेश्वी सदैशान्यां पातु मां सर्वपूजिता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.5359)
- **Original**: जले स्थले चान्तरिक्षे स्वप्रे जागरणे तथा । महाविष्णोश्चव॒ जननी सर्वतः पातु संततम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.5360)
- **Original**: कवच कथित दुर्गे श्रीजगन्मड्रगल॑ परम्‌ । यस्मै कस्मै न दातव्यं गूढाद्‌ गूढ़तरं परम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.5361)
- **Original**: तब ख्ेहान्मया55ख्यातं॑ प्रवक्तत्य॑ न कस्यचित्‌ । गुरुमभ्यर्च्य विधिवद्ठस्त्रालंकारचन्दनै:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.5362)
- **Original**: कण्ठे वा दक्षिणे बाहौँ धृत्वा विष्णुसमो भवेत्‌ । शतलक्षजपेनैव सिद्ध च_ कवच भवेतू
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.5363)
- **Original**: यदि स्थात्‌ सिद्धकवचों न दग्धो वहिना भवेत्‌ । एतस्मात्‌ कवचाद दुर्गे राजा दुर्योधन: पुरा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.5364)
- **Original**: विशारदोी जलस्तम्भे वहिस्तम्पे च. निश्चिमम्‌ । मया सनत्कुमाराय पुरा दत्त च पुष्करे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.5365)
- **Original**: सूर्यपषणि मेरी च स॒ सान्दीपनये ददौ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.5366)
- **Original**: बलाय तेन दत्त च॒ ददौ दुर्योधनाय सः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.5367)
- **Original**: कवचस्यथ प्रसादेत जीवन्मुक्तो. भवेन्नर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.5368)
- **Original**: (प्रकृतिखण्ड 56। 32--49) *यथा कृष्णस्तथा शम्भुर्न॑ भेदों माधवेशयो:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.5369)
- **Original**: (प्रकृतिखण्ड 56। 62)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.5370)
- **Original**: + प्रकृतिखण्ड + 279 39548 484 446 #%## 44816 65644 88444 48% 44444 44 684 # 6 #% #% 4 46% # 4544 46 4444 68544 486 868 और-ब' कारका अर्थ है दाता। जो मड्गलदाता है,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.5371)
- **Original**: मूलप्रकृति ईश्वरीको महती देवी कहा गया है। वही शिव कहा गया है। जो विश्वके मनुष्योंका
- **Translation**: 

---

