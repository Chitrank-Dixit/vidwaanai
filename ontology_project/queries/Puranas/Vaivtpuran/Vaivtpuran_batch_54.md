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

### Verse 1 (Vaivtpuran 4.18358)
- **Original**: किशोरवयसं शान्त॑ राधाकान्तमनन्तकम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.18359)
- **Original**: कुत्रचिद्‌ रासमध्यस्थं॑ राधया परिसेवितम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.18360)
- **Original**: शतश्ृड्भाचलोत्कृष्ट. रप्ये बुन्दावने. बने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.18361)
- **Original**: गोलोके विरजातीरे पारिजातबने. बने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.18362)
- **Original**: निरामये चर बैकुण्ठे कुत्रचिच्य चतुर्भुजम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.18363)
- **Original**: कुत्रचित्‌ स्वांशरूपेण जगतां पालनाय च
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.18364)
- **Original**: कुत्रचित्‌ स्वांशकलया ब्रह्माण्डे ब्रहारूपिणम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.18365)
- **Original**: स्वात्मनः: षोडशांशेन सर्वाधार॑ परात्परम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.18366)
- **Original**: लीलया स्वांशकलया जगतां पालनाय च
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.18367)
- **Original**: वसन्ते कुत्रचित्‌ सन्त योगिनां हृदये सताम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.18368)
- **Original**: त॑ च॒ स्तोतुमशक्ताहमबला निर्गु्णं विभुम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.18369)
- **Original**: य॑ स्तोतुमक्षमोउइनन्त: सहस्त्रवदनेन च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.18370)
- **Original**: य॑ स्तोतुं न क्षमा माया मोहिता यस्य मायया
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.18371)
- **Original**: बेदा न शक्ता य॑ स्तोतुं को वा विद्वांश्न वेदवित्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 5.2347)
- **Original**: 108 + संक्षिम ग्रह्मवैवर्तपुराण « $$#££$#£ 5 #& ##%$ ## 4 $ 4 $####% #%##£$ 45444 4 ## 66% # 6 6 #ऋ 4 #& 5 4 # # # 8 # 5 % कर सकता है। कोई महान्‌ मूर्ख अथवा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 5.2348)
- **Original**: निश्रय हो पण्डित, परम बुद्धिमानू एवं दुर्बुद्धि ही क्‍यों न हो, यदि वह एक वर्षतक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 5.2349)
- **Original**: सुकवि हो जाता है।* नियमपूर्वक इस स्तोत्रका पाठ करता है तो वह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 5.2350)
- **Original**: (अध्याय 5) *याज्ञवल्क्य उवाच कृपा कुक जगन्सातमांपेव हततेजसम्‌ । गशुरुशापात्‌ स्थृतिभ्रष्ट विद्याहोन॑ च दुःखितम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 5.2351)
- **Original**: ज्ञन॑ देहि स्मृति देहि विद्यां विद्याधिदेवते । प्रतिष्ठा कवितां देहि शक्ति शिष्यप्रबोधिनीम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 5.2352)
- **Original**: ग्रन्थकर्तृुतरशक्ति.. च सुशिष्यं सुप्रतिष्ठितम्‌ । प्रतिभां सत्सभायां च विचारक्षमतां शुभाम्‌
- **Translation**: 

---

