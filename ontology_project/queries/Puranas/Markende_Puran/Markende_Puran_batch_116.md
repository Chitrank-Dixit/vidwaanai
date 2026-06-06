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

### Verse 1 (Markende Puran 0.2301)
- **Original**: ज्ञी(समुद्रने उज्वल हार तथा कभी अप्लानपद्जञुजां मालां शिरस्थुरसि चापराम्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2302)
- **Original**: जीर्ण न होनेबाले दो दिव्य बस्तर भेंट किये। साथ 9. कई प्रतियोंगें उसके जद 'ततो देवा दरदुस्तस्थै स्थानि स्वान्यादुधानि च। ऊच्चुजंसण्येत्युन्तर्जयर्तों ते ज॑यैधिणः ।' इतना पाठ आंध्र है। 2. पा7-रम
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2303)
- **Original**: 3. पा0-ट्य। 4. पा7-तस्ये चा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2304)
- **Original**: । 5, पा0--बाहगान्‌!
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2305)
- **Original**: +देवताओंके तेजसे देश्वीकत प्रादर्भान और महिषासुरकों सेनाका ्ष्र * श्थ्रु 74 क-ऋ 7 + 44-44 54446 45:54 4 5:2:22:20205 02757 + #47177 # # # अत; 546:4 5: 7 22 20220 57 # 7+ % + ++74 + अत 65: 72: 5 ही उन्होंने दिव्य चुड़ा्मणे, दो कुण्डल, कड़े. उज्यल अर्धचन्द्र, सब ब्राहओऑक लिये केयर, दोनों चरणोंके लिये सिमिल नूपुर, गलेकों सुद्धर इँसली और सब अगुलियोंमें पहननेक्े लिये रत्नोंकी बनी अँगूटियाँ भी दों। विश्वकर्माने उन्हें अत्वत्त निर्मल फरसा भेंट कियां
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2306)
- **Original**: 25--27
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2307)
- **Original**: साथ हो अनेकछ्त प्रकारके अस्त और अभेद्य कवच दिये; इनके सिवा मस्तक और वक्ष:स्थलपर धारण करतेके लिये भी न कुम्हलानेठाले कपलोंकी मालाएँ दों
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2308)
- **Original**: जलधिये उन्हें लुन्दः कपमलका फूल भेंट किया। हिमालयने सवार्के लिये सिंह तथा भाँति भातिके रत्न समर्पित 'किये
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2309)
- **Original**: धनाभ्यक्ष कुबेस्ने मधुसे भरा पावपात्र दिया तथा सम्पूर्ण सागोंके राजा शेधने, जो इस पृथ्वीको धारण करते हैं, उन्हें बहुमूल्य मणियोंसे विभूषित नागहार भेंट दिया। इसी प्रकार ओन्‍्य देवताओंते भी आभूषण और अस्त्र-शस्त्र देकर देवीका सम्पान क्िसा। तल्पक्षात्‌ उन्होंने बारैबार अट्टहासपूर्वक उन्चस्वस्से गर्जना की। उनके फयंकर नादसे सम्पूर्ण आकाश ग्रूँज उठा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2310)
- **Original**: देवीका वह अत्यन्त उच्नस्दरसे किया हुआ मिंहनाद कहीं समा तन राका, आकाश उसके सामने रूघु प्रतोत होने लगा। उससे वड़े जोरको प्रत्रिध्वनि हुई, जिससे सम्पूर्ण निश्वपें हलचल पंच गयी और समुद्र काँप उठे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2311)
- **Original**: (थली डॉोलने ल्गों और समस्त पर्वत हिलने लगे। उस समय देवताओंने अत्पन्त प्रसालताक्रे राथ सिंहवाहिनी भवानीसे कहा--' दे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2312)
- **Original**: तुम्हारी झत्र हों'
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2313)
- **Original**: साथ हो महर्षियोंने भक्तिभावसे विनर होकर उनका स्तवन किया। दृष्टवा समस्त सेक्षुब्ध अलोक्यमसरास्थ:
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2314)
- **Original**: मुमोतच्ासुरदेहेपु शस्ब्राण्थस्त्राणिण चेश्वरी। संनद्धाखिलसैन्यास्ते समुत्तस्थुरुदायुधा:। आः किमेतदिति क्रोधादाभाष्य पहिषासुर:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2315)
- **Original**: 38 # अभ्यधायत ते जब्दमशेषभैरसरेर्चृत:। स॒ द॒दर्श ततो देवों व्यामलोकत्रयाँ त्विषा
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2316)
- **Original**: पादाक्रान्त्यां नतभुर्व किरीटोलिखिताप्जराम्‌। क्षोभिताशंषपातालां धनुज्यानि:स्वनेन ताम्‌
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2317)
- **Original**: दिश्ञों भुजसहस्त्रेण सपत्ताद व्याप्य संस्थिताम्‌। तत: प्रवब॒ते युद्ध तम्ा देव्या सुरद्विघाम्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2318)
- **Original**: शस्प्रास्त्रैर्जहुधा. मुक्तैरादीपितदिगन्तरम्‌। महिषासुरसेनानीश्षिक्षुराख्थ्ों.. सहाखुर:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2319)
- **Original**: युयुथे. चामरश्चान्यैश्चतुरड्रयलान्वित: स्थानामयूर्त: घड्भिरुद्ग्राख्यो पहासुर:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2320)
- **Original**: अयुध्यतायुतानां च॑ सहख्लेण महाहनु:
- **Translation**: 

---

