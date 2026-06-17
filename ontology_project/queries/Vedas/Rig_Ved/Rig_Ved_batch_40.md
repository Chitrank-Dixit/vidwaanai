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

### Verse 1 (Rig Ved 0.781)
- **Original**: 350. त्व॑ त्येभिरा गहि वाजेभिर्दृहितर्दिव:। अस्मे रयिं नि धारय
- **Translation**: 

---

### Verse 2 (Rig Ved 0.782)
- **Original**: हे द्युलोक की पुत्री उपे ! आप उन (दिव्य) बलों के साथ यहाँ आयें और हमें उत्तम ऐश्वर्य धारण करायें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.783)
- **Original**: [ सूक्त - 31 ] (ऋषि -हिरण्यस्तूप आद्रिरस
- **Translation**: 

---

### Verse 4 (Rig Ved 0.784)
- **Original**: देवता-अग्नि
- **Translation**: 

---

### Verse 5 (Rig Ved 0.785)
- **Original**: छत्द-जगती 8,16,18 त्रिष्टप्‌ ।] 351. त्वमन्ने प्रथमो अड्डिरा ऋषिदेवों देवानामभव: शिव: सखा। तब ब्रते कवयो विद्यनापसो5जायन्त मरुतो भ्राजदृष्टय:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.786)
- **Original**: है अग्निदिव ! आप सर्वप्रथम अंगिरा क्रषि के रूप में प्रकट हुए, तदनन्तर सर्वद्रष्ट, दिव्यतायुक्त, कल्याणकारी और देवों के सर्वश्रेष्ठ मित्र के रूप में प्रतिष्ठित हुए। आप के व्रतानुशासन से मरुद्गण क्रान्तदर्शों कर्मों के ज्ञाता और श्रेष्ठ तेज आयुधों से युक्त हुए है
- **Translation**: 

---

### Verse 7 (Rig Ved 0.787)
- **Original**: 352. त्वमग्ने प्रथमो अड्विरस्तम: कविर्देवानां परि भूषसि द्तम्‌। विभुर्विश्वस्मै भुवनाय मेधिरो द्विपाता शयु: कतिथा चिदायवे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.788)
- **Original**: है अम्निदेव ! आप अंगिराओं में आद्य और शिरोमणि हैं। आप देवताओं के नियमों को सुशोभित करते हैं। आप संसार में व्याप्त तथा दो माताओं वाले दो अरणियों से समुद्भूत होने से बुद्धिमान्‌ हैं। आप मनुष्यों के हितार्थ सर्वत्र विद्यमान रहते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.789)
- **Original**: 40 ऋग्वेद संहिता भाग-9 353. त्वमग्ने प्रथमो मातरिश्वन आविर्भव सुक्रतूया विवस्वते
- **Translation**: 

---

### Verse 10 (Rig Ved 0.790)
- **Original**: अरेजेतां रोदसी होतृवूयें3सध्मोर्भारमयजो महो बसो
- **Translation**: 

---

### Verse 11 (Rig Ved 0.791)
- **Original**: है अग्निदेव! आप ज्योतिर्मय सूर्यदेव के पूर्व और वायु के भी पूर्व आविर्भूत हुए । आपके बल से आकाश और पृथ्वी काँप गये । होता रूप में वरण किये जाने पर आपने यज्ञ के कार्य का सप्पादन किया । देवों का यजनकार्य पूर्ण करने के लिए आप यज्ञ वेदी पर स्थापित हुए
- **Translation**: 

---

### Verse 12 (Rig Ved 0.792)
- **Original**: 354 त्वमग्ने मनवे द्यामवाशय: पुरूरवसे सुकृते सुकृत्तर:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.793)
- **Original**: श्वात्रेण यत्पित्रोर्मुच्यसे पर्या त्वा पूर्वमनयन्नापरं पुनः
- **Translation**: 

---

### Verse 14 (Rig Ved 0.794)
- **Original**: है अग्निदिव! आप अत्यन्त श्रेष्ठ कर्म वाले हैं। आपने मनु और सुकर्मा-पुरूरवा को स्वर्ग के आशय से अबगत कराया । जब आप मातृ-पितृ रूप दो काष्ठों के मंथन से उत्पन हुए, तो सूर्यदेव की तरह पूर्व से पश्चिम तक व्याप्त हो गये
- **Translation**: 

---

### Verse 15 (Rig Ved 0.795)
- **Original**: 355. त्वमग्ने वृषभ: पुष्टिवर्धन उद्यतख्ुच्चे भवसि श्रवाय्य:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.796)
- **Original**: य आहुति परि वेदा वषट्कृतिमेकायुरये विश आविवाससि
- **Translation**: 

---

### Verse 17 (Rig Ved 0.797)
- **Original**: हे अग्निदेव! आप बड़े बलिष्ठ और पुष्टिवर्धक हैं
- **Translation**: 

---

### Verse 18 (Rig Ved 0.798)
- **Original**: हविदाता, खुया हाथ में लिये स्तुति को उद्यत हैं, जो वषदकार युक्त आहुति देता है, उस याजक को आप अग्रणी पुरुष के रूप में प्रतिष्ठित करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.799)
- **Original**: 356. त्वमग्ने वृजिनवर्तनि नरं सक्मन्पिपर्षि विदथे विचर्षणे
- **Translation**: 

---

### Verse 20 (Rig Ved 0.800)
- **Original**: यः शूरसाता परितक्म्ये घने दश्नेभिश्चित्समृता हंसि भूयस:
- **Translation**: 

---

