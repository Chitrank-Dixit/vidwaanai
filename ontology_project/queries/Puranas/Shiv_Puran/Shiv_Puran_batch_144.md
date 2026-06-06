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

### Verse 1 (Shiv Puran 0.2861)
- **Original**: झिख और शझिवाकी हृदयरूपी सूर्तियाँ दिबभावसे भावित हो उन्हीं दोनोंकी आज्ञा शिगेधार्य करके मेरा मनोरश् पूर्ण करें
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2862)
- **Original**: । शिवस्थ च शिवायाश्व सिसायूत्ती सिवाश्रिते। सल्कुत्य शिवयोशज्ञां ते मे काम प्रयच्छताम्‌
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2863)
- **Original**: 'दिव और शिवाकी झिरवारूपा मूर्तियाँ आज्ञाका आदर करके मुझे मेरी अभीष्ट घस्तु अदान करें
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2864)
- **Original**: 15004 440 35474#ऋ ऑजैआऋ# 4 + #+ + 333 लय /+/0+0/0+##4 कैंट कै 47 # 4 है (7 # कु #0##ऋ7
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2865)
- **Original**: 4+4;+45400 00010 कह सियस्य च शिवायागर वर्मणा शिवभाविते
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2866)
- **Original**: सत्कृत्प तिवगोराज्च ते मे कार्र प्रयच्छताम्‌
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2867)
- **Original**: जझिल और शिवाकी कव्चचरूपा मूर्तियाँ श्रीकण्ठ शिवभावसे भावित हो शिख-पार्वतीकी आज्ञाका सत्कार करके मेरी कामना सफत्क करें
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2868)
- **Original**: खिवस्थ थ शिवायाक्ष नेज्रमूर्ती सिंलाश्रिते। सत्कृत्य विवयोगज्ञ॑ ते से काम प्रयच्छताम्‌
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2869)
- **Original**: शिष और शिषघाकी नेप्ररूपा मूर्तियाँ हिवके आश्वित रह उन्हीं दोनोंकी आज्ञा शिरोथार्थ करके मुझे मेरा भनोरण प्रदान करें
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2870)
- **Original**: । अख्यपूर्ती का दिखयोर्नित्यमर्चनतत्परे । सत्कृत्य शिवयोराज् ते ये काम प्रयच्छताप्‌
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2871)
- **Original**: जिव और क्षिवाकी अस्यरूपा मूर्तियाँ नित्य उन्हीं दोनोंके अर्थनमें तत्पर रह उनकी आज्ञाका सत्कार करती हुईं मुझे मेरी अभीष्ट अस्तु अदान करें
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2872)
- **Original**: वामो प्येप््तथा रुद्र: काल्मे विक्रणस्तथा
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2873)
- **Original**: बल चिकरणकैस अलप्रमथनः: परः
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2874)
- **Original**: सर्वभूतस्य दमनस्तादृशकश्चाष्टदाक्तय: । त्रार्थित॑ में प्रसच्छन्तु शिवर्थोरेत दासनात्‌
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2875)
- **Original**: दमन--ये आठ शियपूर्तियाँ तथा इनकी वैसी ही आठ डाक्तियाँ--बामा, ज्येष्टा, रुद्राणी, काली, विकरणी, खलविकरणी, बल्लप्रमथनी तथा सर्वभूतदमनी--ये सख जझ्िब और शिवाके ही शासनसे मुझे प्रार्थित यस्तु प्रदान करें
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2876)
- **Original**: अधानत्तथ्य॒सूक्ष्मस दिवश्ञाप्येफनेत्कः
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2877)
- **Original**: पकरुटस्मिमूर्तित श्रीफण्ठक्ष शि्नण्डिक:
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2878)
- **Original**: तथाएँ शक्तयछोषा द्वितीयाबरणेअर्चिता: । ते में काम प्रथकछत्तु शिवयोरेव शासनात्‌
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2879)
- **Original**: अनन्त, सूक्ष्म, दिव (अथवा शिवोत्तम), एकनेत्र, एकरुूछ, त"रिमूर्ति, और शिखण्डी--ये. आठ विश्येश्वर तथा इनकी जैसी ही आठ शक्तियाँ--अनत्ता, सुक्ष्मा, शिला (अथवा शिवोत्तमा), एकनेन्रा, एकरुद्रा, तिमूर्ति, श्रीकण्ठी और खझिखण्डिनी, जिनकी द्वितीय आवरणमें पूजा हुई है, शिजा और जिवके ही झासनसे मेरी मनःकासना पूर्ण करें
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2880)
- **Original**: भचाद्या मूर्तयक्षाप्टौ तासामपि था वाक्तयः। सहादेवादयक्षान्ये तथैकादशमूर्तय:
- **Translation**: 

---

