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

### Verse 1 (Vishnu Puran 0.1601)
- **Original**: तब उन पृथिवीपतिने पृथिंयीका पालन करते हुए बड़ी-बड़ो दक्षिणाओंवाले अनेकों महान्‌ यज्ञ किये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1602)
- **Original**: अराजकताके समय ओषधियोंके नष्ट हो जानेसे भूखसे व्याकुल हुई प्रजा पृथिवीनाथ पृथुके पास आयी और डनके पूछनेपर प्रणाम कस्के उनसे अपने आनेका कारण निवेदन किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1603)
- **Original**: फ्रजाने कहा--हे प्रजापति नृपश्रेष्ट ! अराजकताके समय पृथिवोने समस्त ओषचियाँ अपनेमें लीन कर ली है, अतः आपकी सप्पूर्ण प्रजा क्षीण हो रही है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1604)
- **Original**: विधाताने आपको हमारा जीवनदायक प्रजापति बनाया है; अत: क्षुधारूप महारोगसे पीड़ित हम प्रजाजनॉको आप जीवनरूप ओषधि दीजिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1605)
- **Original**: श्रीपराशरजी बोले--यह स़ुज्कर महाण्ज पृथु अपना आजगव नामक दिव्य घनुष और दिव्य बाण स्कर अत्यन्त क्रोधपूर्वक पृथिवीके पीछे दौड़े
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1606)
- **Original**: तब भयसे अत्यन्त य्याकुल हुई पृथिवी गौका रूप धारणकर भागी और ब्रह्मल्लेक आदि सभी ल्तेकोंमें गयी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1607)
- **Original**: समस्त भूतोंकों धारण करनेवाए्में पृथिवरी जहाँ-जहाँ भी गयी' बहीं-बहीं उसने बेनपुत्र पृथुको गाख-सन्धान किये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1608)
- **Original**: आ0 13 ] ततस्त॑ प्राह बसुधा पृथ्ुं पृथुपराक्रमप्‌। प्रवेषमाना तद्बाणपरित्राणपरावणा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1609)
- **Original**: 72 परथिष्युवाच खीवधे त्वे महापाप॑ कि नरेन्द्र न पश्यसि । थेन माँ हन्तुमत्यर्थ प्रकरोषि नृषोद्यमम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1610)
- **Original**: 73 पृथुरुूवाच एकस्मिन्‌ यत्र निथन प्रापिते दुष्टकारिणि । बहूनां भवति क्षेमं तस्य पुण्यप्रदों वध:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1611)
- **Original**: 74 पृथिच्दुवाच प्रजानामुपकाराय यदि मां त्वं हनिष्यसि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1612)
- **Original**: आधारः कः प्रजानां ते नृषश्रेष्ठ भविष्यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1613)
- **Original**: 75 प्थुस्याच त्वा हत्वा वसुथे बाणैर्मच्छासनपराज्सुखीम्‌ । आत्मयोगबलेनेमा धारबिष्याम्यहं प्रजा:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1614)
- **Original**: 76 औपणशर उवाच तत:ः प्रणम्य वसुधा ते भूय: प्राह पार्थिवम्‌ । प्रवेषिताड्डी परम साध्वर्स समुपागता
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1615)
- **Original**: 77 पृथिव्युकाच उपायत: समारब्धा: सर्वे सिद्धचन्त्युपक्रमा: । तस्माद्दाम्युपायं ते ते कुरुच्च यदीचछछसि
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1616)
- **Original**: 78 समस्ता या मया जीर्णा नरनाथ महोषधीः । यदीच्छसि प्रदास्यामि ता: क्षीरपरिणामिनी:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1617)
- **Original**: 79 तस्माठाजाहितार्थाय मम धर्मभृतां बर। त॑ तु वत्सं कुरुच्च त्व॑ क्षरेय बेन बत्सला
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1618)
- **Original**: 80 समां च कुरु सर्वत्र येन क्षीर॑ समनन्‍्तत: । वरौषथीबीजभूत॑ बीज सर्वत्र भावये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1619)
- **Original**: 819 श्रीपराशर उकाच तत उत्सार्यामास हैलान्‌ दहातसहस्रश्ः । धनुष्कोट्या तदा वैन्यस्तेन चैला विनर्द्धिता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1620)
- **Original**: 82 न हि पूर्वविसगें बे विषमे पृथिवीतले। प्रविभाग: पुराणां वा ग्रामाणां वा पुराउभवत्‌
- **Translation**: 

---

