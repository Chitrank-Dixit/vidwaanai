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

### Verse 1 (Markende Puran 0.2321)
- **Original**: पज्ञाशद्भिश्ध॒ नियुतैरसिलोपा महासुरः
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2322)
- **Original**: अयुतानां शत: पड्भिर्बाप्कलों युयुभे रणे। गजवाजिसहस्त्रौद्यरनैके!.. प्रिवारितः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2323)
- **Original**: बृतो स्थानां कोठ्या व युद्धे तस्मिन्नयुध्यत। बिडालाख्योउयुतानां च पद्माशद्भिरथायुत्री:
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2324)
- **Original**: युयुधे संयुगे तत्र रथाना प्रिवारित-। अन्ये ञ्ञ तबायुतशों रथनागहयैदृता:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2325)
- **Original**: युयुधु: संयुगे देव्या सह तत्र महासुरा:। कोटिकोटिसहलैस्तु रधानां दन्तिनां तथा
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2326)
- **Original**: 48 हयानां चर बृतो युद्धे तत्राभूम्महिपासुर:। तोमरैसिन्दिपालैश शक्तिभिर्पुसलैस्तंथा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2327)
- **Original**: बुयुधु: संयुगे देव्या खड्गै: परशुपट्विशैः। क्रेचिच्च चिक्षिपु: शक्तीो: केचित्पाशास्तथापरे
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2328)
- **Original**: देवी खड़गप्रहरिस्तु ते तां हन्तुं प्रचक्रमुः। साप्रि देवी ततस्तानि शस्त्राण्यस्लाणि चणिड़का
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2329)
- **Original**: लीलयैब प्रचिच्छेट मिजशस्त्रास्त्रवर्षिणी। अवनायस्तानना देंजो स्तृथमाना सुरर्धिभि:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2330)
- **Original**: 3. ण॒र-कैरूडदर्शन:। 5. खिल्री-किलली प्रनिनें इसके जाट 'युतः वकयालो रध्षज उ रणे गहासवायुत।। दुयुे संदूरे तू ववडेि: पररिदारिह:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2331)
- **Original**: इतत अबिक कर है!
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2332)
- **Original**: 190 सम्पूर्ण त्रिलोकौकों क्षोभग्रस्त देख दैत्यगण अपनी समस्त सेनाकों कवच आदिसे सुसज्जित कर, हाथोंपें हथियार ले सहसा ठठकर खड़े ड्ो गयये। ठस्त समय महिषासुरने बड़े क्रोधमें आकर कहा- “आ:! यह क्‍या हो रहा हैं।' फिर वह सम्पूर्ण अमुरोंसे घिस्कर उस सिंहनादकों ओर लक्ष्य करके दौड़ा और आगे पहुँचकर उसने देवोकों देखा. जो अपनी प्रभासे प्ीनों लौकॉंको प्रकाशित कर रही थीं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2333)
- **Original**: 35--37
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2334)
- **Original**: उनके चरणोंकि धारसे पृथ्वी दबी जा रही थी। माथके मुक्ुटसे आकाश में रेखा-सी खिंच रही थी तथा ने अपने घनुषकों टछछशरसे स्ात्तों पातालोंकों क्षुब्ध किये देती थीं
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2335)
- **Original**: टेवी अपगी हजारों भुजाओंसे सम्पूर्ण दिशाओंकों आच्छादित करके खड़ी थों। तदनन्तर उनके साथ दैत्योंका युद्ध छिड़॒ गया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2336)
- **Original**: नाना प्रकारके अस्त्र-शस्त्रोंके प्रहारसे सम्पूर्ण ना 4 दिशाएँ उल्डारुत होने हार्गी 1. परितो तरदति श्यूरति च्युरत्पार!:। +#संक्षिक्ष प्ार्कण्डेखपुराण * &5&&5666&665#6##&#& & 4& & & 85648 65654 &55& अखसुर महिंषासुस्का सेनानावक था
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2337)
- **Original**: वह देवीके साथ बुद्ध करने ल्वगा। अन्य दैत्पोंकी चतुरक्किगों सेना साथ लेकर चामर भी लड़ने ल्गा। साठ हजार रथियोंके स्राथ आकर उद्ग्र नामक महादैत्यने लोहा लिया
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2338)
- **Original**: एक करोड़ रथ्ियोंको स्राथ लेकर महाइनु नामक दत्य बुद्ध करने लगा। जिम्रके रोएँ तलवारके समान तीखे थे, वह अम्निलोमा नामक! महादैत्य पाँच करोड़ रथी फैनिकोंसहित युद्धमें आ डटा
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2339)
- **Original**: साठ लाख रथियोंसे घिरा हुआ बाण्कल नामक दैत्य भी उम्र युद्धभूमिमें लड़ने लगा
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2340)
- **Original**: मरिवारित नामक राक्षस हाथीसणझार और घुड़रुवारोंके अनेक दलों तथा एक करोड़ रथियोका सेना लेकर युद्ध करने लगा। बिंडाल नामक द्ेत्य पाँच अरब ग्थियोंसे घिरकर लोहा लेने जगा
- **Translation**: 

---

