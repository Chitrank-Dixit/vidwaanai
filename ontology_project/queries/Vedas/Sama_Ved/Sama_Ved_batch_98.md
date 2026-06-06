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

### Verse 1 (Sama Ved 0.1941)
- **Original**: 748.तमु हुवे बाजसातय इन्द्र भराय शुष्मिणम्‌ ।भवा नः सुम्ने अन्तम: सखा वृधे
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1942)
- **Original**: हम उन बलवान्‌ इन्द्रदेव को अन को वृद्धि करने के लिए यज्ञ में युलाते हैं । हे इन्द्रदेव ! सुख एवं उन्नति के समय मार्गदर्शक के रूप में आप हमारे पास रहें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1943)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1944)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1945)
- **Original**: 749.एना वो अग्नि नमसोजजों नप्रातमा हुवे । प्रिय॑ चेतिष्ठमरतिं स्वध्वरं विश्वस्थ दूतममृतम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1946)
- **Original**: हे अपनी स्तुतियों से, ऋत्विजों के दूत रूप, बल क्षय न करने वाले, प्रगतिशील, अमर आफ्निदेव का तुम्हारे (यजमान के) लिए आवाहन करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1947)
- **Original**: उत्तरार्िके द्वितीयों5 ध्यायः 2.5 750.स योजते अरुषा विश्वभोजसा स दुद्गवत्स्वाहुत: । सुब्रह्मा यज्ञ: सुशमी वसूनां देव॑ राधो जनानाम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1948)
- **Original**: वे अग्निदेव विश्व के सभी पदार्थोंका सेवन करके समर्थ तेज को नियोजित करते हैं। तब वे उत्तम ज्ञानी, संयमी, पवित्र अग्निदेव श्रेष्ठ आहुतियों से प्रदीप्त होकर तेमान्‌ होते हैं । यह अग्नि विद्वानों का श्रेष्ठ धन है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1949)
- **Original**: 751.प्रत्यु अदर्श्यायत्यू3च्छन्ती दुहिता दिव: । अपो मही वृणुते चक्षुषा तमो ज्योतिष्कृणोति सूनरी
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1950)
- **Original**: देवलोक से आने वालो (उषादेवी ) की प्रकाशित किरणें, घने अन्धकार को पराजित करती हैं । नेतृत्व की क्षमता सम्पन्न चुलोक की यह पुत्री सम्पूर्ण जगत्‌ को प्रकाश से भर देती हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1951)
- **Original**: 3 । । 75 2,उदुस्लिया: सृजते पूर्य: सचा उद्यान्नक्षत्रमर्चिवत्‌ । तवेदुषो व्युषि सूर्भस्थ च सं भक्तेन गमेमहि
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1952)
- **Original**: 4 ।! ग्रह, नक्षत्र और सूर्य, आकाश को प्रकाशित करते हैं । सूर्यदेव सहसा अपनी किरणों को फैलते हैं । हे उपे ! आपके और सूर्य के प्रकाश को पाकर हम अन्नादे से परिपूर्ण हों
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1953)
- **Original**: 753.इमा उ वां दिविष्टय उस्रा हवन्ते अश्विना । अय॑ वामह्वे5वसे शचीवसू विशंविशं हि गच्छथ:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1954)
- **Original**: है अश्विनीकुमारों ! सब>ू आश्रयदाता, आपको स्वर्ग की कामना वाली प्रजा मदद के लिए बुलाती है । अपनी क्षमता से स्वर्ग में स्था+ 8 ने वाले हे देवो ! ये साधक आश्रय के लिए आपका आवाहन करते हैं; क्योंकि आप ही स्तुति करने वालों के दि 51 जाते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1955)
- **Original**: 754.युवं चित्र ददथुभोजन नरा चोदेथां सूनृतावते । अर्वाग्रथं॑ समनसा नि यच्छतं पिबतं सोम्य॑ मधु
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1956)
- **Original**: हे नेतृत्व प्रदान करने वाले अश्विनीकुमारो ! आप दिव्य आहार देने वाले हैं । स्तुति करने वालों के प्रेरक हे देव ! रथ रोककर मनोयोगपूर्वक यहाँ मधुर रस का पाज़ करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1957)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1958)
- **Original**: के के के
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1959)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1960)
- **Original**: 755. अस्य प्रत्लामनु चुत शुक्र दुदुल्ले अह्य:। पय: सहस्नसामृषिम्‌
- **Translation**: 

---

