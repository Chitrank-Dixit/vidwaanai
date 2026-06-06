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

### Verse 1 (Shiv Puran 0.2821)
- **Original**: नमः परमकल्याणगुणसंचयमूर्तथे । स्वत्तः खल़ु समुस्पन्ने जगत्वव्येव लीयते
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2822)
- **Original**: परम कल्याणमय गुणोंकी आप मूर्ति हैं, आपको नमस्कार हैं। सम्पूर्ण जगत्‌ आपसे ही उत्पन्न हुआ है, अतः आपमें ही छीन होगा
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2823)
- **Original**: । त्वद्विकात: फल दातुमोश्रणेषपि न शकुयात्‌। जन्पप्रपृति देवेशि जनोउ्ये त्यदुपाक्षितः
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2824)
- **Original**: अठोउस्प तय भक्तस्य निर्वर्तव मनोरघम्‌। देवेश्वारे ! अत: आपके खिना ईश्वर भी फल देनेमें समर्थ नहीं हो सकते। यह जन जष्यकाछसे ही आपकी झरणमें आया हुआ है। अतः देवि ! आप अपने इस भक्तका मनोरश्र सिद्ध कीजिये
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2825)
- **Original**: 0 यायतीपर्सद्िता + 375 क्रमम्ल 22.2 0020 04 कं छ 3. 2. # आ7औ आ##ऋ ली #
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2826)
- **Original**: 17000 आई 00 # ## # # ##' 4 (444 है000 00 631/0###+# #233994780007074# 01/47/4777 # कक 2. #+## # 6 #ऑो पछलकतें दशाघृज: शुरूस्फटिकसंनिभः 4 20
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2827)
- **Original**: सम्पूर्ण स्प्रेकॉकी रक्षा करनेके लिये उद्यत रहते हैं ओर अपने विभिन्न अंज्ञॉड्रारा अनेक े यार अजतार थारण करते हैं। वे भकत्या मयार्थिले मह्ी ऋर्थित शे प्रवष्छत
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2828)
- **Original**: 214 ही ये दोनों बन्धु शिव और प्ियाके श्रभो ! आपके पाँच मुख और दस्त पार्श्रभागमें मेरे द्वारा इस प्रकार पूजित हो उन भुजाएँ हैं। आपकी अजज्गभकान्ति झुद दोनॉकी आज्ञा ले प्रतिदिन मुझे प्रार्थित वस्तु स्फटिकमणिके समान निर्मल है। वर्ण, ब्रह्म प्रदान करें
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2829)
- **Original**: 23--26
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2830)
- **Original**: खसदासिवम्‌ । आप मुझे प्रार्धित कल्याण करें
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2831)
- **Original**: सदाहियाहुमारूदा अक्तिरिष्ज शिवाहुया। मनोजाजिछित वस्तु प्रदान करें
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2832)
- **Original**: । शिक्षोर्टवितों पुत्री देवों टेस्प्यप्म्पुलौ। दिश्षानुभावों. सर्वज्ञी विसज्ञानामृताशिनौ
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2833)
- **Original**: कृत परस्परे त्िग्भौ दिजाध्यों नित्यसल्कृती
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2834)
- **Original**: सह्कृती था सदा देसी अद्यार्टीखिददौरापि
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2835)
- **Original**: सर्वस्लेकपशिशिने.. कर्सुपण्युदिते. सूदा। स्वेज्छायतार॑ कुर्चन्ती. स्वोद्ापेदेस्नेकक्षः
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2836)
- **Original**: जाविमौ शिवयोः पार्ख नित्यमित्य॑ म्यार्थेंटो
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2837)
- **Original**: लवोशज्ञा पुसस्‍्कृत्य प्रार्थित से अ्यच्छताम्‌
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2838)
- **Original**: झिय और पार्बतीके प्रिय पुत्र, शिवके समान प्रभावशाली सर्वज्ञ तथा हिव- ज्ञानापृतका पान करके तृप्त रहनेबाले देवता जणेज्ञ और कार्तिकेय परस्पर स्तरेह रखते हैं । शिया और शिव दोनॉसे सत्कृत हैं तथा तद्मा आदि देखता भी इन दोनों देवॉका सर्वधा सत्कार करते हैं। ये दोनों भाई निरन्तर को
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2839)
- **Original**: 270--29
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2840)
- **Original**: पुरूणरू्ये. पुणतनम्‌। पूर्वकक्ताभिमाने थे वदितस्व॒पस्मेश्चित:
- **Translation**: 

---

