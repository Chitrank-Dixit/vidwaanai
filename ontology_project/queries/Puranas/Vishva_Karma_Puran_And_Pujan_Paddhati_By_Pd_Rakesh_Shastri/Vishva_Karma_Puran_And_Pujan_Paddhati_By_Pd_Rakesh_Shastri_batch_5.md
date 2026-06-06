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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.81)
- **Original**: गणेशेनाघिका होता यज्ञे पूज्याश्च घोडश
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.82)
- **Original**: षोडशमातृका चक्र-गणेशजी प हक हक के) 4 पे 0 ही हे पे पे 0 767 88 0 गौ, पं. श. मे. सा. वि. ज. दे. स्व. सवा. मा. लो. है. पु. तु. कु. पूजा के बाद आचार्य आदि का वरण करके निम्नलिखित वैदिक या तांत्रिक मंत्रों द्वारा प्रधान कलश की स्थापना करे। उसी कलश पर विश्वकर्मा की मूर्ति” रखे । अथ . प्रधान कलश स्थापनम्‌ शुद्ध भूमि अधवा वेदी पंचरंग से सुन्दर अष्टदल कमल बनाकर नीचे के मन्त्र से भूमि स्पर्श करें- ः "सोने, चांदी, अष्टधातु, मृण्मयी मूर्ति पृथक वेदी या चौकी पर रखनी चाहिए। -
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.83)
- **Original**: ... श्री विश्वकर्मा पुराण एवं पूजन पद्धति... 73] विश्वकर्मा पुराण एवं पूजन पद्धति 3
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.84)
- **Original**: कँ भूरिस भूमिरस्यदितिरसि व्विश्वधाया व्विश्वस्य भुवनस्य धर्न्ी [वर पृथिवीं यच्छ पूथिवीं दू्शह पृथिवीं माहिधसी:
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.85)
- **Original**: इति मन्त्रेण भूमि स्पर्शनिं कृत्वा । अष्टदल कमल के ऊपर सप्तधान्य रखे- ऊँ घान्यमसि घिनुहि देवान्‌ प्राणायत्वोदानायत्वा व्यानायत्वा । दीघमिनुप्रसितिमायुषे थां देवो वः सविता हिरण्यपाणिः प्रतिगृम्णात्वच्छिद्रेण पाणिना चक्षुषे त्वा महीनाम्पयो5सिं
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.86)
- **Original**: . उसी पर सप्तधान्य बिखेर कर मिट्टी या तांबे का कलश स्थापित करे- ऊँ आजिप्न कलर्श मह्मात्वा विशञान्त्विन्दव: । पुनरूर्जा निवर्तस्वसानः सहसं धुक्ष्वोरुघारा पयस्वत्ती: पुनर्मा विशतांद्रयिः
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.87)
- **Original**: कलश में जल भरना- ऊँ व्वरुणस्योत्तम्मनमसि व्वरुणस्य स्कम्म सर्जनीस्थो व्वरुणस्यडऋत- सदनमसि वरुणस्य5ऋतसदनमासीद
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.88)
- **Original**: कलश में गन्धाक्षत छोड़े- ऊँ त्वां गन्धर्वाउअखनंस्त्वामिन्द्र स्त्वां बृहस्पत्तिस्त्वामौषधे सोमो राजा विदानूयक्ष्यादमुच्यत
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.89)
- **Original**: सर्वोषधि डालना- ऊँ या औषधी: पूर्वा जाता देवेम्यस्त्रियुगं पुरा । मुनै नु ब्रणामहथ्4 शत घामानि सप्त च
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.90)
- **Original**: दूर्वाकुर प्रश्नेपण- ः ऊँ काण्डात्‌ू काण्डातू प्रहारेन्ती परुष: परुषस्परि । एवानोदूर्वेप्रतनु- सहस्रेणशतेन च
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.91)
- **Original**: पंचपल्लव डालने का मन्त्र- ऊ अश्वत्थे वो निषदनं पर्णे वो वसतिष्कृता । गोभाजउइत्किला सथधयत्सनवधथपुरुषमू
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.92)
- **Original**: सप्तमृत्तिका डालना-- - .... ऊँ स्योना पृथिवीनो भवानृक्षरा निवेशनी । यच्छान: शर्म सप्रथा:
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.93)
- **Original**: कलश में कुश (दर्भाकुर) छोड़े- ऊँ पवित्रेस्थो वैष्णव्यी सवितुर्व: प्रसवर5उत्पुनाम्यच्छिद्रेण पविज्नेण सूर्यस्य रशिमभिः । तस्य ते पवित्रपते पवित्नपूतस्य यत्कामः पुने तच्छकेयमू
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.94)
- **Original**: पूंगीफल (सुपाड़ी) डालना- ऊँ या: फलिनीरयाँ अफला अपुष्यायाश्च पुष्यिणी: । वृहस्पतिप्रसूतास्ता नो मुन्नन्त्वश् हस:
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.95)
- **Original**: ! पंचरत्न अथवा द्रव्यदक्षिणा- ऊं हिरण्यगर्भ: समवर्तताय़े 'भूतस्य जातः पतिरेक5आसीत्‌ । स दाघार 4. श्री विज़वकर्मा पुराण एवं यूजर श्री विश्वकर्मा पुराण एवं पूजन पद्धति...) पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.96)
- **Original**: पृथिवीं चामुते मां कस्मै देवाय हविषा विधेम
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.97)
- **Original**: धोती एवं चादर से कलश आच्छादन करना- ऊँ सुजातो ज्योतिषासहशर्मव्वरूथमासदत्स्वः: । वासो5अग्ने विश्वरूपध9 संव्ययस्व विभावसो । ऊँ युवासुवासाः परिवीत आगात्स5उश्रेयान्‌ भवति जायमान: । तन्थीरास: कव्य5उचन्नयन्ति स्वाध्यो मनसा देवयन्तः
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.98)
- **Original**: चावल से भरा पूर्णपात्र स्थापित करे- पूर्णदर्वि परापत सुपूर्णा पुनरापत । व्वस्नेव्वविकी णावहा5इषमूर्ज&9 शत्रक्रतो
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.99)
- **Original**: न कलश के ऊपर नारिकेल फल तथा विश्वकर्मा की धातुमयी मूर्ति स्थापित ऊँ श्रीश्च ते लग्मीश्च पत्न्यावहोरोत्रे पार्शवे नक्षत्नाणि रूपमश्विनी व्यात्तम । इष्णनिषाणा मुम्मडइघाण सर्वलोकम्म5इघाण
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.100)
- **Original**: इसके बाद कलश में वरुण देवता का आह्वान करे- 3 तत्वायामि ब्रह्मणा व्वन्दमानस्तदाशास्ते यजमानों हविर्मिः । अहेडमानोवरुणेहबो ध्युरुश 8 समानऊआयुः प्रमोषीः । ऊ॑ अपाम्पत्ये वरुणाय नमः । तत्पश्चात्‌ पुनः कलश में गंगादि नदियों का आद्वान करके प्रार्थना करनी चाहिए कलशस्य मुखे विष्णु: कण्ठे रुद्र: समाश्ितः । मूले तस्य स्थितो ब्रह्मा मध्ये मातृगणा: स्पृता:
- **Translation**: 

---

