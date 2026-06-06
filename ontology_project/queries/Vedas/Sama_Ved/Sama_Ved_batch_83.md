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

### Verse 1 (Sama Ved 0.1641)
- **Original**: 638.उद्चचामेषि रज: पृथ्वहा मिमानो अक्तुभि: । पश्यज्जन्मानि सूर्य
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1642)
- **Original**: हे सूर्यदेव ! आप दिन को रात्रि से नापते हुए शरीरधारियों को प्रकाशित करते हैं और स्वर्ग तथा अन्तरिक्ष को भी प्रकाश से भर देते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1643)
- **Original**: 639.अयुक्त सप्त शुन्ध्युवः सूरो रथस्य नफ्य: । ताभिर्याति स्वयुक्तिभि:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1644)
- **Original**: सूर्यदेव शुद्ध करने वाले सात घोड़ों (सतरंगी किरणों) को अपने रथ में जोड़े हुए हैं। रथ चलाने वाली, घोड़े रूपी किरणों से अपनो शक्तियों के द्वारा सूर्यदेव सब जगह जाते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1645)
- **Original**: [ वैज्ञानिक स्दर्ध में सूर्य की सात किरणों को निष्प प्रकार बताया है “वैनीआहपीनाला” बैगनी, नीला, आसमानी, हरा, पीला, नारंगी, लाल
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1646)
- **Original**: मज में इसे ही सूर्य के सात घोड़े कहा गया है। ] 640,सप्त त्वा हरितो रथे वहन्ति देव सूर्य । शोचिष्केशं विचक्षण
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1647)
- **Original**: हे प्रकाशक सूर्यदेव ! शुद्ध करने वाली सात रंग की सात किरणें आपके रथ को ले जाती हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1648)
- **Original**: इति पञ्चम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1649)
- **Original**: कु के के
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1650)
- **Original**: इत्यारण्यपर्वीण षष्ठो5ध्याय:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1651)
- **Original**: पूर्वार्चिक: समाप्त:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1652)
- **Original**: जा ह* >कऋ-की प्लेन 3 _
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1653)
- **Original**: पूर्वार्चिकि आरण्पपर्वाण पष्ठो5प्याव
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1654)
- **Original**: अथ महानाम्नयार्चिक: ।। 641.विदा मघवन्‌ विदा गातुमनुशंसिषो दिशः । शिक्षा शचीनां पते पूर्वीणां पुरूवसो
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1655)
- **Original**: हे परमात्मन्‌ (सम्पत्तिशाली) इन्द्रदेव ! आप सब कुछ जानते हैं, अत: लक्ष्य तक पहुँचने का मार्ग दिखाएँ । है शक्तियों के स्वामी ! हे ऐश्वर्यवान्‌ प्रभो !आप हमें उपदेश दें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1656)
- **Original**: 1 1 642. आभिष्ट्वमभिष्टिमि: स्वा53नौशु: । प्रचेतन प्रचेतयेन्द्र गयुम्माय न इधे
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1657)
- **Original**: 2 !। हे प्रैलोक्यपते इन्द्रदेव ! सूर्यदेव के समान तेजस्वी आप तेजयुकत, पोषक अल प्राप्त करने की दिशा में प्रेरित करते हुए हमें संरक्षण प्रदान करें
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1658)
- **Original**: 643.एवा हि शक्रो राये वाजाय द्रव:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1659)
- **Original**: शविष्ठ वस्रिन्दृज्जसे मंहिष्ठ वच्रिन्नज्जस । आ याहि पिब मत्स्व
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1660)
- **Original**: हे महान्‌ वज्नधारी इन्द्रदेव ! आप शक्तिवान्‌ हैं। अत: है बलशाली इन्द्रदेव ! आप हमें धन और वल प्राप्त करने के लिए समर्थ बनाएँ । आप हमें सामर्थ्यवान्‌ बना" । आप हमारे पास आकर सोमरस के पान से आनन्दित हों
- **Translation**: 

---

