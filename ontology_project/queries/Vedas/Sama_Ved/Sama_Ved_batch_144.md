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

### Verse 1 (Sama Ved 0.2861)
- **Original**: हे श्रेष्ठ अग्निदेव ! आप हमारे पास रहते हुए हमारी रक्षा करें तथा हमारे कल्याण के निमित् बनें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2862)
- **Original**: 1108. वसुरग्निर्वसुश्रवा अच्छा नक्षि द्युमत्तमों रविं दा:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2863)
- **Original**: सभी को आश्रय देने वाले, धनवानों में अग्रगण्य, हे अग्निदिव ! आप हमारे पास सहजता से आएँ और तेजस्वितायुक्त होकर हमें धन प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2864)
- **Original**: 1109.त॑ त्वा शोचिष्ठ दीदिव: सुम्नाय नूनमीमहे सखिभ्य:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2865)
- **Original**: हे तेजवान्‌ और प्रकाशवान्‌ अग्निदेव ! मित्र आदि स्नेहों परिजनों के लिए सुख की कामना करते हुए निश्चित ही हम आपकी प्रार्थना करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2866)
- **Original**: 1110.इमा नु क॑ भुवना सीषधेमेन्द्रश्न विश्वे च देवा:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2867)
- **Original**: ये सभी लोक हमारे आनन्द के साधन हों । इन्द्र सहित सभी देवता हमारे लिए सुखकर हों
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2868)
- **Original**: छ.10 सामवेद-संहिता 1111. यज्ञ च नस्तन्वं च प्रजां चादित्यैरिन्द्र: सह सीषधातु
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2869)
- **Original**: आदित्यों सहित हे इन्द्र ! हमारे यज्ञकर्म, शरीर और सन्तानादि को आप श्रेष्ठ सफलता से युक्त करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2870)
- **Original**: 1112.आदित्यैरिन्द्र: सगणो मरुद्धिरस्मभ्यं भेषजा करत्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2871)
- **Original**: आद्रित्यों, मरूद्गणों एवं अपनी अन्य सहायक शक्तियों के साथ इन्द्र (सूर्य) देव हमारे लिए ओषधि (सूर्य-चिकित्सा से आरोग्व कारक स्थिति ) तैयार करें
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2872)
- **Original**: 1113.-प्र व इन्द्राय वृत्रहन्तमाय विप्राय गाथं गायत य॑ं जुजोषते
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2873)
- **Original**: हे मनुष्यो ! शत्रुहन्ता, विद्वान्‌ इन्द्रदेव के लिए स्तवनों का गान करो, जिन्हें वे प्रसन्‍नता से सुनते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2874)
- **Original**: 1114.अर्चन्त्यर्क मरुतः स्वर्का आ स्तोभति श्रुतो युवा स इन्द्र:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2875)
- **Original**: आदरणीय, प्रशंसनीय इन्द्रदेव की साधकगण स्तुति करते हैं। बलवान्‌ एवं यशस्वी इन्द्रदेव उनकी हर प्रकार से रक्षा करतें हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2876)
- **Original**: 1115.उप प्रक्षे मधुमति क्षियन्तः पुष्येम रखिं धीमहे त इन्द्र
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2877)
- **Original**: हे इन्द्रदेव !आपके संरक्षण में निवास करने वाले हम याजक बलवान्‌ हों और धन-सम्पदा धारण करें
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2878)
- **Original**: इति सप्तम: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2879)
- **Original**: की ही हऋऔऑ ऋषि, देवता, छन्‍्द-विवरण ऋषि- (अकृष्टा माषादि) तीन क्रप्रष 1031-1033 । कश्यप मारीच 1034-1036, 1076-1078 । मेधातिथि काण्व 1037-1046 । हिरण्यस्तृप आद्विसस 1047-1056 । अवत्सार काश्यप 1056-1060 । जमदम्नि भार्गव 1061-1063। कुत्स आद्विस्स 1064-1066, 1104-1106। वस्सिष्ठ मैत्रावरुणि 1067-1069
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2880)
- **Original**: व्रिशोक काण्व 1070-1072। श्यावाश्च आत्रेय 1073-1075। सप्तर्षिगण 1079-1080 । अमहीयु आइ्रिसस 1081-1083 । शुकःशेप आजीगर्ति 1084-1086
- **Translation**: 

---

