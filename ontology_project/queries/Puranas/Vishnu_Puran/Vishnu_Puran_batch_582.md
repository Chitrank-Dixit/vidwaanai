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

### Verse 1 (Vishnu Puran 0.11621)
- **Original**: 29 अनेन दुष्टकपिना दैत्यपक्षोपकारिणा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11622)
- **Original**: जगन्निराकृर्त वीर दिष्टया स क्षयमागतः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11623)
- **Original**: 22 इत्युकल्वा दिवमाजम्मुर्देवा हृष्टास्सगुद्यकाः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11624)
- **Original**: 23 औरीपराशर उवाच एवंविधान्यनेकानि बलदेवस्यथधीमत॑: । कर्माण्यपरिमेयानि शेषस्थ धरणीभृतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11625)
- **Original**: र4ढ पश्मम अंश 409 तब श्रीहलूधरने क्ुद्ध होकर उसे घमकाया तथापि बह उनकी अवज्जञा कस्के किलकारी मारने लगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11626)
- **Original**: तदनन्तर श्रीबलरामजीने मुसकाकर क्रोधसे अपना मूसछ उठा लिया तथा उस्र बानरने भी एक भारी चढद्ठान ले ली
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11627)
- **Original**: और उसे बलरामजीके ऊपर फेंकी किन्तु यदुबीर बलभद्रजीने मूसलसे उसके हजारों टुकड़े कर दिये; जिससे वह पृथिवीपर गिर पड़ी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11628)
- **Original**: तब उस वानरने बलगामजोके मूसलका बार बचाकर रोषपूर्वक अत्यन्त खेगसे उनकी खतोमें घूँसा मारा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11629)
- **Original**: तत्पश्चात्‌ बलभद्रजीने भी क्रुद्ध होकर द्विविदके सिरमें घूंसा मारा जिससे वह रुचिर वमन करता हुआ निर्जीव होकर पृथिवीपर गिर पट्टा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11630)
- **Original**: हे मैत्रेय ! उसके गिरते समय उसके शरीर्का आघात पाकर इन्द्र-वद्से विदीर्ण होनेके समान उस पर्वतके शिखस्के सैकड़ों टुकड़े हो गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11631)
- **Original**: उस समय देवतालोग बलरामजीके ऊपर फूल खरसाने छगे और कहां आकर “आपने यह बड़ा अच्छा किया” ऐसा कहकर उनकी प्रशंसा करने लगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11632)
- **Original**: “हे वीर! दैत्य-पक्षके उपकारक इस दुष्ट खानरने संसारकों बड़ा कष्ट दे रखा था; यह बड़े ही सौभाग्यका विषय है कि आज यह आपके हाथों मारा गया ।' ऐसा कहकर गुह्मकॉंके सहित देबगण अत्यन्त हर्पपूर्वक स्वरल्झोककों चले आये।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11633)
- **Original**: श्रीपराइरजी जोे--शेषावतार धरणीधर धीमान्‌ बलभद्रजीके ऐसे ही अनेकों कर्म हैं, जिनका कोई परिमाण (तुलना) नहीं बताया जा सकता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11634)
- **Original**: -कचत है अल मपन्‍मणथ इति श्रीविष्णुपुराणे पञ्षमेंउदों षद्त्रिज्ञोउ्ध्यायः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11635)
- **Original**: व जौ अयन-+++ सैंतीसवाँ अध्याय ऋषियोंका झाप, यदुरवंशविनाइ तथा भगवानका स्वधाम सिधारना श्रापराशर उताच एवं दैत्यवर्ध कृष्णो बलदेवसहायवान्‌। चक्रे दुष्टक्षितोशानां तथैव जगत: कृते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11636)
- **Original**: 91 क्षितेश्ष भार॑ भगवान्फाल्गुनेन समन्वितः । अवतारयामास विभुस्समस्ताक्षोहिणीवधात्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11637)
- **Original**: 2 कृत्वा भारावतरणं भुवो हत्वाखिलान्नपान्‌ । श्रीपराशस्जी बोले--हे मैत्रेय! इसी प्रक्तार संसारके उपकारके लिये बलभद्गजीके सहित श्रीकृष्णचद्रने दैत्यों और दुष्ट राजाओऑंका वध किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11638)
- **Original**: तथा अन्‍्तमें अर्जुनके साथ मिलकर भगवान्‌ कृष्णने अठारह अक्षौहिणी सेनाको मारकर पृथिवीका भार उतारा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11639)
- **Original**: इस प्रक्कार सम्पूर्ण राजाओंको मारकर पृथिवीका भारावतरण किया और फिर शापतव्याजेन विप्राणामुपसंहतवान्कुलम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11640)
- **Original**: ब्राह्मणोंके शञापके मिपसे अपने कुलका भी उपसंहार कर
- **Translation**: 

---

