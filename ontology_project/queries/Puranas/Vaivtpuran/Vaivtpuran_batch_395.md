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

### Verse 1 (Vaivtpuran 19.18686)
- **Original**: स्तोतुं यमीशा नो जाड्घात्‌ सर्पस्तोष्यति तं कथम्‌। हे नाथ करुणासिन्धो दीनबन्धो क्षमाधमम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.18687)
- **Original**: खलस्वभावादज़ानात्‌ कृष्ण त्वं चर्वितो मया। नास्वलक्ष्यो यथाकाशो न दृश्यान्तो न लद्घ्यक:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.18688)
- **Original**: न स्पृश्यो हि न चावर्यस्तथा तेजस्त्वमेव च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.18689)
- **Original**: इत्येवमुक्वा नागेनद्र: पपात चरणाम्बुजे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.18690)
- **Original**: इति श्रीब्रह्मवैवर्ते कालियकुर्त श्रीकृष्णस्तवन सम्पूर्णम्‌। श्रीकृष्णजन्मखण्ड
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.19094)
- **Original**: <83$2 '.. » संक्षिप्त बहचैवर्तपुराण « %5%%%%%%$%%%5%%% 55 55% % 5 55% #% 5 % 85% 8 ऋ% 6 4 86 55 # 8 59 645 85 # 5 # 58 65 88 # 6 # 65% 5 # 5 संतत॑ सर्वतः पातु परो नारायण: स्वयम्‌ । इ्ति ते कथितं ब्रह्मनू कबचं परमाद्भुतम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.19095)
- **Original**: मम जीवनतुल्यं च युधष्मभ्य॑ दत्तमेव च
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.19096)
- **Original**: अश्वमेधसहस्राणि_ वाजपेयशतानि_ च। कलां नाईन्ति तान्येव कबचस्यैत धारणात्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.19097)
- **Original**: गुरुमभ्यर््यय विधिवद्‌ वस्व्रालंकारचन्दनै: । स्त्रात्वा त॑ चर नपस्कृत्य कवच धारयेत्‌ सुधीः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.19098)
- **Original**: कवचस्यथ प्रसादेन जीवन्मुक्तो भवेतन्नर: । यदि स्थात्‌ सिद्धकवचों विष्णुरेव भवेद्‌ द्विज
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.19099)
- **Original**: इति श्रीब्रह्मवैवते ब्रह्माण्डपावन श्रीकृष्णकवर्च सम्पूर्णस्‌। (ब्रह्मखण्ड 19। 8-38) #00//00004 कस 24200/0..050050 तऔत्रैलोक्यविजयं नाम श्रीकृष्णकवचम्‌ महादेव उवाच ब्रैलोक्यविजयस्यास्थ कवचस्य॒ प्रजापति: । ऋषिएउन्दश्ल गायत्री देवो राधेश्वरः स्वयम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.19100)
- **Original**: ब्रैलोक्यविजयप्राम्मा विनियोग: प्रकीर्तित: । परात्पं च कवचं त्रिषु लोकेषु दुर्लभम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.19101)
- **Original**: प्रणबों मे शिरः पातु श्रीकृष्णाय नम्रः सदा । पायात्‌ कपालं कृष्णाय स्वाहा पश्नाक्षरः स्मृतः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.19102)
- **Original**: कृष्णेति पातु नेत्रे च्र कृष्णस्वाहेति तारकम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.19103)
- **Original**: हरये नम इत्येबं॑ भ्रूलतां पातु मे सदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.19104)
- **Original**: 3» गोविन्दाय स्वाहेति नासिकां पातु संततम्‌ । गोपालाय नमो गण्डौ पातु में सर्वतः सदा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.19105)
- **Original**: 30 नमो गोपाड़्ुनेशाय कर्णों पातु सदा मम। 3» कृष्णाय नमः शश्चत्‌ पातु मे5धरयुग्मकम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.19106)
- **Original**: 30 गोविन्दाय स्वाहेति दन्तालीं में सदावतु । 3» कृष्णाय दन्तरन्श्रं दन्तोघ्च॑क्लीं सदायतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.19107)
- **Original**: 3 श्रीकृष्णाय स्वाहेति जिद्लिकां पातु मे सदा । राधेश्वराय स्वाहेति तालुक॑ पातु मे स॒दा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.19108)
- **Original**: राधिकेशाय स्वाहेति कण्ठं पातु सदा मम । नमो गोपाड्ुनेशाय वक्ष: पातु सदा मम
- **Translation**: 

---

