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

### Verse 1 (Brahamandp 0.2121)
- **Original**: ... शक्‍तेरावारतां प्राप्ते: स्त्रीपू लिगने नो भयम्‌
- **Translation**: 

---

### Verse 2 (Brahamandp 0.2122)
- **Original**: 56 जक्तिस्तु सर्वतो भाति.संसारस्य स्वभावत:
- **Translation**: 

---

### Verse 3 (Brahamandp 0.2123)
- **Original**: तहिं तस्या दुराणाया: प्रवृत्तिज्ञायतां त्वया
- **Translation**: 

---

### Verse 4 (Brahamandp 0.2124)
- **Original**: 60 केयं कस्मात्समुत्पन्ना किमाचारा किमाश्रया
- **Translation**: 

---

### Verse 5 (Brahamandp 0.2125)
- **Original**: 5... किकला किसहाया वा देव॑-तत्प्रविच्नायंताम्‌
- **Translation**: 

---

### Verse 6 (Brahamandp 0.2126)
- **Original**: 61 .. ।। इत्युक्त: स.विष गेण .को, विद्या से -महीजसाय्‌
- **Translation**: 

---

### Verse 7 (Brahamandp 0.2127)
- **Original**: अस्मद्बले महासत्त्वा अक्षोौहिण्यधिपा: शेतख्‌
- **Translation**: 

---

### Verse 8 (Brahamandp 0.2128)
- **Original**: 642 / पातु क्षमास्त जैलधीनल दर॑धु त्रिविष्टपम्‌। अरे पापसभ्राज्ञार कि वृथा शथड्ढसे स्व्ियंः,4
- **Translation**: 

---

### Verse 9 (Brahamandp 0.2129)
- **Original**: 6 3 प्राचीन समय में-भी चणष्डिका नाम ववाली- एक नारी ही तो थी जिसते रण! में निशुम्भ-शुम्भ और महिष को ' मार:डाला
- **Translation**: 

---

### Verse 10 (Brahamandp 0.2130)
- **Original**: थाः।47
- **Translation**: 

---

### Verse 11 (Brahamandp 0.2131)
- **Original**: उसी के प्रसंग/स्े उसने बहुत से देत्यों का विन्लार्श -करः।दिया ल्‍थ्राः ।इसी/पकॉरणं से 'मैं।यही बतलाता है कि यह संमझ करके केवल सन्नी ही तो: है. कर भी भी अबन्नव नहीं करनी चाहिए ।58। शक्ति'ही सर्वत्र विजय-की श्री।काजकारण. हुआ करत्तो है। शक्तिके आधार को प्राप्त हैं उतःस्त्री भर: पुरुषों से हम को भ्य नहीं हैं ।56। इस संसार की स्वभाव से- ही शक्ति ही सर्व ओर ब्रिभात हुआ।करतती है। सो उम्र घुरे आशय बाली क्री क्या प्रवृत्ति है++आप्र- को; समझ लेना चाहिए ।60। हैः देव !! आपको :इतत- सभी “्वात्ों. का विकर): कर लेत्ता । चाहिए कि बह। कौन है++किससे यह समुल्यन्न हुई है-- इसके ओ।च्नार/क्यो। हैं: इसका भोश्रे यक्पा. है--- इसके बल कसा ओर कितत्ता है-- इसकी पतदायता
- **Translation**: 

---

### Verse 12 (Brahamandp 0.2132)
- **Original**: भंडासुर अहंकार वर्णन] [ 281 करने वाले कौन-कौन हैं ।66। उस विषंग छोटे भाई के द्वारा जब इस रीति से भंडासुर से कहा गया था तो उसने कहा था कि जो महांत्र्‌॒ ओज वाले हैं उनके लिए विचार का करने की क्‍या आवश्यकता है। हमारी सेता में महान्र्‌ सत्वधारी हैं और सैकड़ों तो अक्षौहिणी सेना के अधिप हैं। वे इतने समर्थ हैं कि जलधि के जल का भी पान कर सकते हैं और स्व को भी दग्ध कर सकते हैं। अरे ! पापसमाचार ! व्य्थे ही स्त्रियों के विषय में तू क्या ऐसी शझ्भुत कर रहा है ।62-63
- **Translation**: 

---

### Verse 13 (Brahamandp 0.2133)
- **Original**: । तत्सव॑ हि मया पूर्व चारद्वारावलोकितम्‌ । अग्रे समुदिता काचिलललितानामधारिणी
- **Translation**: 

---

### Verse 14 (Brahamandp 0.2134)
- **Original**: 64 यथार्थना मवत्येषा पुष्पवत्पेशलाकृति: । न सत्त्वं न च॒ वीय॑ वा न संग्रामेषु वा गति:
- **Translation**: 

---

### Verse 15 (Brahamandp 0.2135)
- **Original**: 65 सा चाविचारनिवहा किंतु मायापरायणा
- **Translation**: 

---

### Verse 16 (Brahamandp 0.2136)
- **Original**: तत्सत्त्वेनाविद्यमान स्त्रीकदम्बकमात्मन:
- **Translation**: 

---

### Verse 17 (Brahamandp 0.2137)
- **Original**: 66 उत्पादितवती कि ते न च्षेवं तु विचेश्ते । अथ वा भवदुक्तेन न्यायेनास्तु महदंबलम्‌
- **Translation**: 

---

### Verse 18 (Brahamandp 0.2138)
- **Original**: 67 त्रेलोक्यल्लंघिमहिमा भण्ड: केन विजीयते
- **Translation**: 

---

### Verse 19 (Brahamandp 0.2139)
- **Original**: 68 इदानीमपि मद्वाहुबलसंमद मूच्छिता: । श्वसितु चापि पटवो न कदाचन नाकिन:
- **Translation**: 

---

### Verse 20 (Brahamandp 0.2140)
- **Original**: 66& केचित्पातालगर्भेबु केचिदम्बुधिवारिषु । केचिट्विंगंतकोणेषु केचित्कुज्जेषु भुभूताम्‌
- **Translation**: 

---

