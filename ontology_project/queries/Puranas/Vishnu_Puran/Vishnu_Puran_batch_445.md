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

### Verse 1 (Vishnu Puran 0.8881)
- **Original**: 33 श्रीपराझर उताच इत्युक्त्वा प्रययो तत्र सह देव: पितामह: । सम्राहितमनाशञ्ैव॑ तुष्टाव गरूडध्वजम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8882)
- **Original**: 34 क्रह्मोगाच दे विद्ये स्वमनाप्नाय परा चैबापरा तथा। त॑ एवं भवतो रूपे मूर्तामृ्तात्पिके प्रभो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8883)
- **Original**: 35 द्वे ब्रह्मणी त्वणीयो5तिस्थूलात्मन्सर्न सर्ववित्‌ । जब्दब्रह्म पर चेव ब्रह्म ब्रह्ममयस्थ यत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8884)
- **Original**: 36 ज्लिक्षा कल्पो निरूक्ते च च्छन्दो ज्योतिषमेव॒ च
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8885)
- **Original**: 37 इतिहासपुराणे नि न- व्याकरणं प्रभो। मीर्मासा न्यायशास्त्रं च क्षज
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8886)
- **Original**: 38 आत्पात्मदेहगुणवद्धिचाराचारि. यद्गच: । तदप्याद्यपते. नान्यदध्यात्मात्मस्वरूपवत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8887)
- **Original**: 39 पश्चम अंझ आअ्श] च तक छ2&ःख झ पममअंश #झझ#झयञयञऑयथऑ»>रऱर्‌<़आ आस अर 309 है दिव्यमूर्तिघारी देवशण ! इस समय मेरे ऊपर महाबल्तयान्‌ और गवींले दैत्यगजोंकी अनेक अक्षौहिणी सेनाएँ हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8888)
- **Original**: है अमरेधरो ! मैं आपत्मेगोंको यह बतलाये देती हूँ कि अन मैं उनके अत्यन्त भारसे पीडित होकर अपनेकों धारण करनेमें सर्वथा असमर्थ हूँ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8889)
- **Original**: अतः है महाभागगण ! आपल्ोग मेंरे भार उतारनेक्ा अब कोई ऐसा उपाय कीजिये जिससे मैं अत्यन्त व्याकुल होकर रसातलऊूको न चली जाऊकँ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8890)
- **Original**: पृथिवीके इन वाक्योंको सुनकर उसके भार उतारनेके कविषयमें समस्त देवताओंकी प्रेरणासे भगवान ब्रह्मजीने कहना आरम्भ किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8891)
- **Original**: ब्रह्माजी बोले--हे देवगण ! पृथिवीने जो कुछ कहा है बह सर्वथा सत्य ही है, वास्तबमें मैं, दौकर और आप सब लोग नारायणस्वरूप ही हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8892)
- **Original**: उनकी जो-जों विभूतियाँ हैं, उनकी परस्पर न्यूनता और अधिकता हो खाध्य तथा बाधकरूयसे रहा करती है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8893)
- **Original**: इसलिये आओ, अब हमस्मरेग क्षीरसागरके पवित्र तटपर चलें, वहाँ श्रीहस्किी आराधना कर यह सम्पूर्ण वृत्तान्त उनरो निवेदन कर दें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8894)
- **Original**: ये विध्ररूप सर्वात्मा सर्वथा संसारके हितके लिये ही अपने शुद्ध सत््योदासे अबतोर्ण होकर पृथिवीमें घर्मकी स्थापना करते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8895)
- **Original**: 33 । श्रीपराशरजी ओले--ऐसा कहकर देवताओके सहित पितामह ब्रह्माजी वहाँ गये और एकाग्रचित्तसे अीगरुडध्वज भगवान्‌की इस प्रकार स्तुति करने छगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8896)
- **Original**: ब्रह्माजी बोले--हे वेदवाणीके अगोचर प्रभो ! परा और अपरा--वे दोनों विद्याएँ आप ही हैं। हे नाथ ! थे दोनों आपहीके मूर्त और अमूर्त रूप हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8897)
- **Original**: हे अत्यन्त सूक्ष्म ! हे घिराट्स्वरूप ! हे सर्व ! हे सर्वज्ञ ! शबप्यद्ा और परज्ह्म -ये दोनों आप ग्रह्ममयके ही रूप हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8898)
- **Original**: आप हो ऋग्वेद, यजुबेंद, सामयेद और अधर्ववेद हैं तथा आप ही शिक्षा, कल्प, निरुक्त, छन्‍्द और ज्योतिष्‌-शास्त्र हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8899)
- **Original**: हे प्रभो ! हे अधोक्षज ! इतिहास, पुराण, व्याकरण, मीौमांसा, न्याय और चर्मशाख--ये सब भी आप हो हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8900)
- **Original**: है आध्यपते ! जीबाह्मा, परमात्मा, स्थृुलन-सूक्ष्म-देह तथा उनका कारण अव्यक्त--इन सबके विचारसे युक्त जो अन्तयत्मा और परमात्पाके स्वरूपक्र बोधक [ तत््वमसि ] लाक्य है, बह भी आपसे भिन्न नहीं है
- **Translation**: 

---

