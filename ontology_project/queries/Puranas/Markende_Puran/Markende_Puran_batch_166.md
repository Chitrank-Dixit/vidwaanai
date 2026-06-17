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

### Verse 1 (Markende Puran 0.3301)
- **Original**: चिच्छेदापततस्तस्य मुदगरं निशितैः शरै:। तथापि सो भ्यधावत्तां मुप्टिमुद्यम्य वेगबानू
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3302)
- **Original**: स॒मुष्टिं पातयामास हृदये द्वैत्यपुड्रव:। देव्यास्तं चापि सा देवी तलेनोरस्थताडयतू
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3303)
- **Original**: तलप्रहाराभिहतों.. निपषात महीतले। स दैत्यरयाज: सहसा पुनरेव तथोत्थित:
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3304)
- **Original**: उत्पत्थ च॒ प्रगृद्मोच्चैदेंवीं गगनमास्थित:। तब्रापि सा निराधारा युयुधे लेन चणिडका
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3305)
- **Original**: नियुद्धं खे तदा दैत्यश्वण्डिका चर परस्परम्‌। अक्रतु: प्रथम॑ सिद्धमुनिविस्मथकारकम्‌
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3306)
- **Original**: ततों नियुर्द्ध सुचिर॑ कृत्वा तेनाम्बिका सह। उत्पात्य भ्रामयामास चिक्षेप धरणीतले
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3307)
- **Original**: स क्षिप्तो धरणों प्राप्य मुष्टिमु्यम्य वेगित: ' । अभ्यधावत दुष्टात्मा चण्डिकानिधनेच्छया
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3308)
- **Original**: तमायान्त॑ ततों देवी सर्वदैत्यजनेश्वरम्‌। जगत्यां पातयामास भित्त्वा शूलेन वक्षसि
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3309)
- **Original**: स गतासुः पपात्तोव्याँ देवीशूलाग्रविक्षत:। चालयन्‌ सकलां पृथ्वी साब्धिद्वीपां सपर्वताम्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3310)
- **Original**: ततः प्रसन्नमख्थिल हते तस्मिन्‌ दुरात्मनि। जगत्स्वास्थ्यमतीवाप निर्मल चाभवन्नभ:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3311)
- **Original**: उत्पातमेघा: सोल्का ये प्रागासंस्ते शर्म ययु:। सरितो मार्मवाहिन्यस्तथासंस्तश्र॒पातिते
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3312)
- **Original**: ततो देवगणा: सर्वे हर्षनिर्भरमानसा:। अधूवुर्निहते तस्मिन्‌ गन्धर्वा ललितं जगुः
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3313)
- **Original**: अबादयंस्तवैवान्ये. ननृतुआ्लप्सरोगणा:।
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3314)
- **Original**: बबु: पुण्यास्तथा बाता: सुप्रभो5भूद्विबाकर:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3315)
- **Original**: जन्चलुश्चाग्रय: शान्ता: शान्ता दिग्जनितस्वना:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3316)
- **Original**: . ऋषि कहते हैं--
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3317)
- **Original**: तदनन्तर देवी और शुम्भ दोनोंमें सब देवताओं तथा दानवोंके देखते- देखते भयद्भूर युद्ध छिड़ गया
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3318)
- **Original**: बाणोंकी वर्षा तथा तीखे शस्त्रों एवं दारुण अस्त्रोंके प्रहारके कारण उन दोनोंका युद्ध सब लोगोंके लिये बड़ा भयानक प्रतोत हुआ
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3319)
- **Original**: उस समय अम्बिका
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3320)
- **Original**: देवीने जो सैकड़ों दिव्य अस्त्र छोड़े, उन्हें दैत्यराज शुम्भने उनके निवारक अस्त्रोंद्रारा काट डाला
- **Translation**: 

---

