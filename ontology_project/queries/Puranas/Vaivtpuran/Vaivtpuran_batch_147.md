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

### Verse 1 (Vaivtpuran 9.2296)
- **Original**: रासेधेण विधभुना रासे ये रासफमण्डले
- **Translation**: 

---

### Verse 2 (Vaivtpuran 9.2297)
- **Original**: अतीव गोपनीय॑ च कल्पवृक्षमम॑ परम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 9.2298)
- **Original**: अश्रुताद्धतमत्राणां. समूहैश्ध समन्वितम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 9.2299)
- **Original**: यद्‌ धृत्वा भगवाज्छुक्र: सर्वदैत्येषू. पूजित:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 9.2300)
- **Original**: यद धृत्वा पठनाद ब्रह्मन्‌ बुद्धिमांक्ष बृहस्पति:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 9.2301)
- **Original**: पठनाद्धारणाद्वाग्मी कवीदओ वाल्मिकों मुनि:। स्थायम्भुवों मनुश्चैद यद्‌ धृत्वा सर्वपूजित:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 9.2302)
- **Original**: कणादो गौतम: कण्व: पाणिनि: शाकटायन:। ग्रन्ध॑ चकार यद्‌ धृत्वा दक्ष: कात्यायन: स्वयम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 9.2303)
- **Original**: धृत्वा वेदविभाग॑ च पुराणान्यछिलानि च। चकार लीलामातप्रेण कृष्ण्रैपायन: स्वयप्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 9.2304)
- **Original**: शातातपञ्च॑ संवर्तोि.. वसिष्ठश्ष॒ पराशर: । यद्‌ घृत्वा पठनाद्‌ ग्रन्थं याज्ञवल्क्यश्चकार स;
- **Translation**: 

---

### Verse 10 (Vaivtpuran 9.2305)
- **Original**: ऋष्यश्ृद्रो भरद्वाजश्वास्तीकों.. देवलस्तथा । जैगौषव्योड्थ जाबालिय॑द धृत्वा सर्वपूजिता:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 9.2306)
- **Original**: कवचस्यास्थ विप्रेद्ध ऋषिरेव प्रजापति: । स्वयं हछन्दशध॒यहती देवता शारदाम्बिका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 9.2307)
- **Original**: सर्वतत्त्वपरिज्ञाने सर्वार्थसाधनेषु चञ। कवितासु च सर्वासु विनियोग: प्रकीर्तित:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 9.2308)
- **Original**: शी हीं सरस्वत्ये स्वाहा शिरों में पातु सबंत:। अ्नं वाग्देवताये स्वाहा भाल में सर्वदावतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 9.2309)
- **Original**: सरस्वत्य॑स्वाहेति श्रोत्रे पातु निरन्तरम्‌ । 35 श्रीं हों भारत्यै स्वाहा नेत्रयुग्म॑ सदाबतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 9.2310)
- **Original**: वाग्वादिन्यै स्वाहा नासां मे सर्वतोउवतु ! 3» हाँ विद्याधिष्ठातृदेव्ये स्वाहा ओएछ्ं सदावतु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 9.2311)
- **Original**: हीं ब्राह्मण स्वाहेति दन्तपडूक्ति सदावतु। ऐमित्येकाक्षोो मनत्रों मम कष्ठ सदावतु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 9.2312)
- **Original**: श्रीं हीं पातु मे ग्रीवां स्कन्धौ मे श्रीं सदावतु। 3» श्रीं विद्याधिष्ठातृदेव्यै स्वाहा वक्ष: सदावतु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 9.2313)
- **Original**: हीं विद्यास्वरूपायै स्वाहा में पातु नाभिकाम्‌ू । 3» हुं क्लीं वाण्यै स्वाहेति मम हस्तौ सदावतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 9.2314)
- **Original**: सर्ववर्णात्मिकाये॑ पादयुग्म॑ सदावतु । यागधिष्ठातृदेव्ये॑े स्वाहा सर्व॑ सदायतु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 9.2315)
- **Original**: सर्वकण्ठवासिन्ये॑ स्वाहा प्रार््यां सदावतु
- **Translation**: 

---

