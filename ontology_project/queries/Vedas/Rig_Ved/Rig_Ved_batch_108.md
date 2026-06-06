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

### Verse 1 (Rig Ved 0.2141)
- **Original**: [ सूक्त - 90
- **Translation**: 

---

### Verse 2 (Rig Ved 0.2142)
- **Original**: [ ऋषि - गोतम राहुगण । देवता - विश्वेदेवा । छन्द - गायत्रों, 9 अनुष्टप्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.2143)
- **Original**: ] 979, ऋजुनीती नो वरुणो मित्रो नयतु विद्वान्‌। अर्यमा देव: सजोषा:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.2144)
- **Original**: ज्ञानी देव मित्र और वरुण हमें सरल नीति पथ पर बढ़ाते हैं । देवों के सहचर अर्यमा हमें सरल मार्ग से उनतिशील बनायें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.2145)
- **Original**: 980, ते हि वस्वों बसवानास्ते अप्रमूरा महोभि:। ब्रता रक्षन्ते विश्वाहा
- **Translation**: 

---

### Verse 6 (Rig Ved 0.2146)
- **Original**: वे धनों के धारणकर्ता ध्र्पात, प्रकृ्ट बुद्धि सम्पन्न महान्‌ सामरथ्यों से सम्पूर्ण शत्रुओं के नाशक नियमों में अटल हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.2147)
- **Original**: 981. ते अस्मध्यं शर्म यंसन्नमृता मर्त्येभ्यः। बाधमाना अप द्विषः
- **Translation**: 

---

### Verse 8 (Rig Ved 0.2148)
- **Original**: वे अविनाशी देवगण हमारे शत्रुओं का नाश करके हम मनुष्यों को सब भाँति सुख देते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.2149)
- **Original**: श्स्द् ऋग्वेद संहिता धाग-9 982. वि न: पथ: सुविताय चियन्त्विन्द्रो मरूत:। पूषा भगो वन्द्यासः
- **Translation**: 

---

### Verse 10 (Rig Ved 0.2150)
- **Original**: ये वन्दनीय टेवगण इन्द्र, मरुत्‌ , पृषा और भग हमें कल्याणकारी पथ पर प्रेरित करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.2151)
- **Original**: 983. उत नो धियो गोअग्रा: पूषन्विष्णवेवयाव:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.2152)
- **Original**: कर्ता नः स्वस्तिमत:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.2153)
- **Original**: हे पूषन्‌ ! है विष्णो ! हे गतिशोल मरुतो ! आप हमारी बुद्धि को गो सदृश (पोषक विचार स्नरवित करने वाली) बनायें । (इस प्रकार) हमारा कल्याण करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.2154)
- **Original**: 984. मधु बाता ऋतायते मधु क्षरन्ति सिन्धव:। माध्वीर्न: सन्त्वोषधी:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.2155)
- **Original**: । यज्ञ कर्म करने वालों के लिये बायु एवं नदियाँ मधुर प्रवाह पैदा करें । सभी ओषधियाँ मधुर रस से सम्पन्न हों
- **Translation**: 

---

### Verse 16 (Rig Ved 0.2156)
- **Original**: 985. मधु नक्तमुतोषसो मधुमत्पार्थिवं रज:। मथु दयौरस्तु न: पिता
- **Translation**: 

---

### Verse 17 (Rig Ved 0.2157)
- **Original**: पिता की तरह पोषणकर्ता दिव्यलोक हमारे लिए माधुर्य युक्त हो । मातृवत्‌ रक्षक पृथ्वी की रज भी मधु के समान आननन्‍्दप्रद हो । रात्रि और देवी उषा भी हमारे लिये माधुर्ययुक्त हों
- **Translation**: 

---

### Verse 18 (Rig Ved 0.2158)
- **Original**: 986. मथुपाननो वनस्पतिर्मधुमाँ अस्तु सूर्य:। माध्वीर्गावों भवन्तु न:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.2159)
- **Original**: सम्पूर्ण वनस्पतियाँ हमारे लिये मधुर सुख प्रदायक हों । सूर्यदेव हमें अपने माधुर्य (तेजस्वी किरणों) से परिपृष्ट करें तथा गौएँ भी हमारे लिये अमृत स्वरूप मधुर दुग्ध रस प्रदान करने में सक्षम हों
- **Translation**: 

---

### Verse 20 (Rig Ved 0.2160)
- **Original**: 987 हं नो मित्र: शं वरुण: शं नो भवत्वर्यमा। शं न इन्द्रो बृहस्पति: शं नो विष्णुरुरुक्रमः
- **Translation**: 

---

