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

### Verse 1 (Vishnu Puran 0.4401)
- **Original**: 27 तस्माच्छेयांस्यशेषाणि नृपैतानि न संशय: । परमार्थस्तु भूषाल सद्ठलेपाच्छुयतां मम
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4402)
- **Original**: 28 एको व्यापी समः शुद्धो निर्गुणः प्रकृतेः पर: । जन्मवद्धयादिरहित आत्मा सर्वगतोउव्यय:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4403)
- **Original**: 29 परज्ञानमयो5सद्धिर्नामजात्यादिभि्विभु: । न योगवात्न युक्तो5भून्नेव पार्थिव योक्ष्यते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4404)
- **Original**: 30 तस्यात्मपरदेहेषु सतो5प्येकमर्य हि यत्‌। खिज्ञान परमार्थोड्सो बैतिनोज्तथ्यदर्शिनः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4405)
- **Original**: 31 बेणुरम्रप्रभेदेन भेद: पडजादिसंज्ञितः । अभेदव्यापिनो वायोस्तथास्य परमात्मन:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4406)
- **Original**: 32 एकस्वरूपभेदश बाह्ाकर्मप्रवृत्तिज: । देवादि भरेदेपध्वस्ते नास्त्येवावरणे हि सः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4407)
- **Original**: 33 तो उसके किषयमें मेरा ऐसा विचार है---
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4408)
- **Original**: हे तृप ! जो यस्तु कारणरूपा मृत्तिकाका क्यर्य होतों है वह कारणको अनुगामिनी होनेसे मृत्तिकारूप ही जानी जाती है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4409)
- **Original**: अतः जो क्रिया समिध, घृत और कुशा आदि नाशवान्‌ द्रव्योंसे सम्पन्न होतो है वह भी नादावान्‌ ही होगी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4410)
- **Original**: किक्तु परमार्थक्रो तो प्राज्ञ पुरुष अविनाशी बतत्ते हैं और नाशचान्‌ द्रव्योंसे निष्पन्न होनेके कारण कर्म [अथवा उनसे निष्पन्न होनेवाले स्वर्गादि] नाशवान्‌ हो हैं-- इसमें सन्देह नहीं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4411)
- **Original**: यदि फलाशासे रहित निष्कामकर्मकों परमार्थ माउते हो तो वह तो मुक्तिरूप फलका साधन होनेसे साधन ही है, परमार्थ नहों
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4412)
- **Original**: यदि देहादिसे आत्माव्य पार्थक्य विचारकर उसके ध्याय करमेको परमार्थ कहा जाय तो बह तो अनाम्मासे आत्माका भेद करनेवात्म है और परमार्थमें भेद है नहीं [ अतः वह भी परमार्थ नहीं हो सकता]
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4413)
- **Original**: यदि परमात्मा और जीवात्माके संयोगको परमार्थ कहें तो ऐसा कहना सर्व था मिध्या है, क्योंकि अन्य बद्रव्यसे अन्य दरव्यकी एकता कभी नहीं हो सकती*
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4414)
- **Original**: अतः हे राजन्‌ ! विःसन्देत ये सब श्रेय ही हैं,
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4415)
- **Original**: परमार्थ नहीं] अब जो परमार्थ है वह मैं संक्षेपसे सुनाता हूँ, श्रवण ऊरो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4416)
- **Original**: आत्मा एक, व्यापक, सम, शुद्ध, निर्गुण और प्रकृतिसे परे है; वह जन्म-वृद्धि आदिसे रहित, सर्वव्यापी और अच्यय है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4417)
- **Original**: हे राजन्‌ ! वह परम ज्ञानमय है, असत्‌ नाम और जाति आदिसे उस सर्वव्यापकका संयोग न कभी हुआ, न है और न होगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4418)
- **Original**: 'वह, अपने और अन्य प्राणियोंकि शरीरमें विद्यमान रहते हुए भी, एक ही है '---इस प्रकारका जो विशेष ज्ञान है वहाँ परमार्थ है; दंत धववनाबाले पुरुष तो अपरमार्धदःञों हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4419)
- **Original**: जिसप्त प्रकार अभिम्न भावसे व्याप्त एक हो वायुके बाँसरीके छिट्टेंकि भेदसे पदज आदि भेद होते हैं उसी प्रकार [ शरीरादि उपाधियोंके कारण ] एक ही परमात्माके [ देवता- मनुष्यादि ] अनेक भेद प्रतीत होते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4420)
- **Original**: एकरूप आत्माके जो नाना भेद हैं वे बाद्दा देहादिकी कर्मप्रवृत्तिके कारण हो हुए है । देवादि शरौगेंक्रे भेदका निराकरण झे जानेपर बह नहीं रहता । उसकी स्थिति तो अविद्याके आवरणतक ही है
- **Translation**: 

---

