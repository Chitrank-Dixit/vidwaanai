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

### Verse 1 (Vaivtpuran 23.2082)
- **Original**: [6 भी संतानका मुख नहीं देख सकेंगी।' इतनेमें उस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2083)
- **Original**: " देवीकी जीभके अग्रभागसे सहसा एक परम [%4£ मनोहर कन्या प्रकट हो गयी। उसके शरौरका वर्ण शुक्ल था। वह श्वेतवर्णका ही वस्त्र धारण किये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2084)
- **Original**: , 5 हुए थी। उसके दोनों हाथ बीणा और पुस्तकसे ह / हर सुशोभित थे। सम्पूर्ण शास्त्रोंकी वह अधिष्ठात्री
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2085)
- **Original**: हो गये। अवस्था, तेज, रूप, गुण, बल और देवी रत्रमय आभूषणोंसे विभूषित थी। पराक्रममें बे सभी श्रीकृष्णके समान ही प्रतीत तदनन्तर कुछ समय व्यतीत हो जानेके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2086)
- **Original**: होते थे। प्राणके समान प्रेमभाजन उन गोपोंको पश्चात्‌ वह मूल प्रकृतिदेवी दो रूपोंमें प्रकट हुई।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.2087)
- **Original**: परम प्रभु श्रीकृष्णने अपना पार्षद बना लिया। ऐसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.2088)
- **Original**: 96 ह « संक्षिप्त ्रह्मवैग्व्तपुराण « %%%%%%#%#%%%%%#6 #### 56665 66% 6 66% ######## ##$%$%%%$%#$%#% 66% #%$$$%#%#$$%%#$ ### # ## कलासे उत्पन्न हैं। इनकी माया जगत्‌के समस्त प्राणियोंको मोहित करनेमें समर्थ है। सकामभावसे उपासना . करनेवाले गृहस्थोंकों ये सम्पूर्ण ऐश्वर्य 7 6, हि
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.2089)
- **Original**: प्रदान करती हैं। इनकी कृपासे भगवान्‌ श्रीकृष्णमें 32098
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.2090)
- **Original**: भक्ति उत्पन्न होती है। विष्णुके उपासकोंके लिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.2091)
- **Original**: ये भगवती वैष्णवी (लक्ष्मी) हैं। मुमुक्षुजनोंको हक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.2092)
- **Original**: मुक्ति प्रदान करना और सुख चाहनेवालोंकों सुखी $5$
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.2093)
- **Original**: बनाना इनका स्वभाव है। स्वर्गमें 'स्वर्गलक्ष्मी' 54)
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.2094)
- **Original**: और गृहस्थोंके घर “गृहलक्ष्मी' के रूपमें ये विराजती हैं। तपस्वियोंके पास तपस्यारूपसे उन मधुरभाषिणी कन्याओंको राधाने अपनी दासी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.2095)
- **Original**: राजाओंके यहाँ श्रीरूपसे, अग्रिमें दाहिकारूपसे, बना लिया। वे रत्रमय भूषणोंसे विभूषित थीं।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.2096)
- **Original**: सूर्यमें प्रभारूपसे तथा चन्द्रमा एवं कमलमें उनका नया तारुण्य सदा बना रहता था। परम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.2097)
- **Original**: शोभारूपसे इन्हींकी शक्ति शोभा पा रही है। पुरुषके शापसे वे भी सदाके लिये सन्तानहीना
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.2098)
- **Original**: सर्वशक्तिस्वरूपा ये देबी परमात्मा श्रीकृष्णमें हो गयी थीं। विराजमान रहती हैं। इनका सहयोग पाकर विप्र! इतनेमें श्रीकृष्णेः शरीरसे देवी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.2099)
- **Original**: आत्मामें कुछ करनेकी योग्यता प्राप्त होती है। दुर्गाका सहसा आविर्भाव हुआ। ये दुर्गा सनातनी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2100)
- **Original**: इन्हींसे जगत्‌ शक्तिमान्‌ माना जाता है। इनके एवं भगवान्‌ विष्णुकी माया हैं। इन्हें नारायणी. । बिना प्राणी जीते हुए भी मृतकके समान हैं। ईशानी और सर्वशक्तिस्वरूपिणी कहा जाता है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2101)
- **Original**: [छ पे / (2 ] ये परमात्मा श्रीकृष्णकी बुद्धिकी अधिष्ठात्री देवी
- **Translation**: 

---

