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

### Verse 1 (Sama Ved 0.1041)
- **Original**: 392. यस्य त्यच्छम्बरं मदे दिवोदासाय रन्थयन्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1042)
- **Original**: अय॑ स सोम इन्द्र ते सुतः पिब
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1043)
- **Original**: हे इद्धदेव ! जिस सोमरस को पी करके मदोन्मत्त आपने, दिवोदास के कल्याण के लिए शम्बरासुर का हनन किया, उस शोधित सोमरस का आप सेवन करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1044)
- **Original**: 393. एन्द्र नो गथि प्रिय सत्राजिदगोह्मा । गिरिरन विश्वत: पृथु: पतिर्दिव:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1045)
- **Original**: हे सर्वप्रिय ! सभी शत्रुओं को जीतने वाले, अपराजेय इन्द्रदेव॒ पर्वत के सदृश सुविशाल द्युलोक के अधिपति, आप (अनुदान देने हेतु) हमारे पास आएँ
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1046)
- **Original**: 394. य इन्द्र सोमपातमों मदः शविष्ठ चेतति। येना हंसि न्‍्या3त्रिणं तमीमहे
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1047)
- **Original**: 4 अत्यधिक सोमपान करने वाले बलशाली इन्धदेव आपका उत्साह प्रशंसनीय है । जिससे आप ( अद्वितकारी) घातक असुरों (आसुरी वृत्तियों) को नष्ट करते हैं, ऐसे आपकी हम स्तुति करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1048)
- **Original**: 395. तुचे तुनाय तत्सु नो द्राधीय आयुर्जीवसे । आदित्यास: समहसः कृणोतन
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1049)
- **Original**: है महान्‌ आदित्यो ! हमारे पुत्र और पात्रों को दीर्घायुष्य प्रदान करने की आप कृपा करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1050)
- **Original**: 396. वेत्था हि निर्क्रतीनां वज्रहस्त परिवृजम्‌। अहरहः शुन्ध्यु: परिपदामिव । ।6
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1051)
- **Original**: हे बद्रधारी इन्द्रदेव ! आप विघष्मकारक तत्वों को दूर करने के मार्ग को जानते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1052)
- **Original**: पवित्रता से आपत्तियों (रोगों) को दूर करने वाले मानव के समान, आप भी विपत्तियों को दूर करने में समर्थ हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1053)
- **Original**: 397. अपामीवामप स्रिधमप सेधत दुर्मतिम्‌। आदित्यासो युयोतना नो अंहसः
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1054)
- **Original**: है आदित्यो !( आप हमें) रोगों, शत्रुओं, पापों एवं दुष्ट बुद्धि के दुष्प्रभावों से दूर रखें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1055)
- **Original**: [यहाँ सूर्य रफ्पियों से शारीरिक एवं मानसिक चिकित्सा के सूत्र-संकेत विद्यमान हैं ।] 398. पिबा सोममिन्द्र मन्दतु त्या यं ते सुषाव हर्यश्नाद्रि: । सोतुर्बाहुभ्यां सुयतो नार्वां
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1056)
- **Original**: है अश्वयुक्त इन्द्रदेव ! आप आनन्ददायक सोमरस का पान करें । रस्सी से बँघे हुए, स्थिर घोड़े के समान (यज्ञशाला पें) सुरक्षित रखे गये पत्थर से सोमरस आपके लिए निकाला जाता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1057)
- **Original**: इति एकोनरत्रिंश: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1058)
- **Original**: पूर्कार्चिक ऐ-द्रपर्वणि चनुर्ों5ध्याय: ड7
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1059)
- **Original**: त्रिंश: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1060)
- **Original**: 399. अभ्नातृव्यो अना त्वमनापिरिन्द्र जनुषा सनादसि। युथेदापित्वमिच्छसे
- **Translation**: 

---

