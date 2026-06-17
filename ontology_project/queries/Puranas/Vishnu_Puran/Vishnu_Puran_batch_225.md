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

### Verse 1 (Vishnu Puran 0.4481)
- **Original**: 29 यवगोधूममुद्गादि घृते तैले पयो दधि। गुड फलादीनि तथा पार्थरिवा: परमाणवः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4482)
- **Original**: 30 तदेतद्धबता ज्ञात्वा मृष्टामृष्टविच्वारि यत्‌। तन्मनस्समतालम्बि कार्य साम्ये हि मुक्तये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4483)
- **Original**: 31 ब्राह्मण उदय इत्याकर्ण्य बचस्तस्य परमार्थाश्रित नूप । प्रणिपत्य महाभागो निदाघो बाक्यमत्नवीत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4484)
- **Original**: 32 प्रसीद मद्धितार्थाय कथ्यतां यक्त्तमागतः । नष्टो मोहस्तवाकर्ण्य वचांस्येतानि में द्विज
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4485)
- **Original**: 33 ऋषुत्वाच ऋभुरस्मि तवाचार्य: प्रज्ञादानाय ते द्विज । डुहागतो5हं यास्थामि परमार्थस्तवोदितः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4486)
- **Original**: 34 एयमेकमिदं विद्धि न भेदि सकलं जगत्‌। वासुदेवाभिधेयस्य स्वरूप परमात्मन:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4487)
- **Original**: 35 ब्राह्मण उवाच तथेत्युक्वा निदाघेन ग्रणिपातपुर:सरम्‌ । पूजित: परया भकक्‍त्या इच्छात: प्रययावृभु:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4488)
- **Original**: 36 इसी प्रकार कभी अरुचिकर पदार्थ रुचिकर हो जाते हैं ओर रुचिकर पदा्ोंसे मनुष्यको उद्बेग हो जाता है । ऐसा अन्न भला कौन-सा है जो आदि, मध्य और आत्त तीगों काल्‍ूमें रचिकर ही हो 2
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4489)
- **Original**: जिस प्रकार मिट्टीका घर पिंड्टीसे लीपने-पोतमेंसे दृढ़ होता है, उसों प्रकार यह पार्धिन देह पार्थिय अन्नके परमाणुओंसे पुष्ट हो जाता हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4490)
- **Original**: जौ, गेहूँ, मूँग, घृत, तेल, दूध, दही, गुड़ और फल आदि सभी पदार्थ पार्थिब परमाणु हो तो हैं । [ इनमेंसे किसको स्वाटु कहें और किसको अश्नाद्‌ ?]
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4491)
- **Original**: अत; ऐसा जानकर मुर्म्हे इस स्वादु-अस्थारुफा छिचार करनेवाले चित्तको समदर्शी बनाना चाहिये, क्योंकि मोक्षका एकमात्र ठपाय समता ही है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4492)
- **Original**: ब्राह्मण खोले--हे राजन्‌ ! तनके ऐसे परमार्थमय खचन सुनकर महाभाग निदाघने उन्हें प्रणाम करके कहा--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4493)
- **Original**: “प्रभो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4494)
- **Original**: आप पसन्न होइये ! कृपया बतल्खइये, मेरे कल्याणक्त्रे कामनासे आये हूए आप कौन हैं ? हे ट्विज ! आपके इन बचनोंकों सुनकर मेरा सम्पूर्ण मोह नष्ट हो गया है'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4495)
- **Original**: ऋषभु बोले--हे द्विज ! मैं तेरा गुरु क्रभु हूँ; तुझकों सदसड्विवेकिनी युद्धि प्रदान करनेके ल्त्ये मैं यहाँ आया था
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4496)
- **Original**: अब मैं जाता हूँ, जो कुछ परमार्थ है चह मैने तुझसे कह हीं दिया है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4497)
- **Original**: इस परमार्थतत्त्कका विचार करते हुए तू इस सम्पूर्ण जगत॒को एक बासुदेव परमात्माठीका स्वरूप जान; इसमें भेद-भाव बिलकुल नहीं है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4498)
- **Original**: बाह्मण बोले--तदनत्तर निदाघने “बहुत अच्छा कह उजें प्रणाम किया और फिर उससे परम भक्तिपूर्वक पूजित हो ऋभु स्तेच्छानुसार चले गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4499)
- **Original**: इति श्रीविष्णुपुराणे द्वितीयेंडशे प्ददशोडथ्यायः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4500)
- **Original**: सोलहवाँ अध्याय ऋभुकी आज्ञासे निदाघका अपने घरको त्ह्रैंटना आह्यण उवाच ऋशुर्वर्धसहस्ने तु समतीते नरेश्वर । निदाघज्ञानदानाय. तदेव नगरं ययौ
- **Translation**: 

---

