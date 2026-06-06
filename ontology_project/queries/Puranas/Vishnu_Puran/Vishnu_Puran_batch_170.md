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

### Verse 1 (Vishnu Puran 0.3381)
- **Original**: 97 । बचत और कततत इति श्रीविष्णुपुराणे द्वितीयेंउशें चतुर्थोड्ष्यायः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3382)
- **Original**: जज-+ और कतततन पाँचवाँ अध्याय सात पातालत्तेकॉका वर्णन अ्रीपराष्ार उवाच विस्तार एच कथित: पृथिव्या भवतो मया । सप्ततिस्तु सहस्लाणि ट्विजोच्छुयो4पि कथ्यते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3383)
- **Original**: 1 दह्शसाहस्नमेकैके पाताल मुनिसत्तम । अतलं वितले चैव नितलं चर गभस्तिमत्‌। महाख्यं सुतलं चाप्यं पातारूंचापि सप्तमम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3384)
- **Original**: 2 चुक्ककृष्णारुणा: पीता: शर्करा: शैलकाझना: । भूमयो यत्र मैत्रेय वरप्रासादमण्डिता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3385)
- **Original**: 3 तेषु दानवदैतेया यक्षाश्र शतशस्तथा। आह्वादकारिण: शुघ्रा मणयो यत्र सुप्रभा: । नागाभरणभूषासु पातालं केन तत्समम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3386)
- **Original**: 6 श्रीपराशरजी जोले--हे द्विज ! मैंने तुमसे यह पृथिवीका विस्तार कहा; इसको ऊँचाई भी सत्तर सहस्न योजन कही जाती है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3387)
- **Original**: हे मुनिसत्तम ! अतल, बितल, नितल, गभस्तिमान, महातल, सुतहू और पाताल इन सातोंमेंसे प्रत्येक दस-दस सहस्र योजनको दूरोपर है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3388)
- **Original**: है मैश्रेय ! सुन्दर महल्लॉंसे सुझोभित वहाँको भूमियाँ झुक, कृष्ण, अरुण और पीत चवर्णकी तथा शर्करामयी (केंकरीली), शैली (पत्थस्की) और सुबर्णमयी है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3389)
- **Original**: हे महामुने ! उनमें दानव, दैत्य, यक्ष और बढ़े-बढ़े नाग आदिकोंकी सैकड़ों जातियाँ निवास करती हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3390)
- **Original**: एक बार नास्दजीने पाताललोकसे स्वर्गमें आकर वहाँके निवासियोंसे कहा था कि 'पाताछ तो स्वर्गसे भी अधिक सुन्दर है'
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3391)
- **Original**: जहाँ नागगणके आधृषणोंमें सुन्दर प्रभायुक्त आह्वादकारिणी जुघ्र मणियाँ जड़ी हुई हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3392)
- **Original**: अ* 5 ) दैत्यदानवकन्याभिरितश्रेतश्न॒. शोभिते । पाताले कस्य न प्रीतिर्विमुक्तस्थापि जायते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3393)
- **Original**: 7 दिवार्करइमयो यत्र प्रभां तन्‍्वन्ति नातपम्‌। शहशिरश्मिर्न शीताय निशि द्योताय केवल्म्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3394)
- **Original**: 8 भोगिषधिः । यत्र न ज्ञायते कालो गतो5पि दनुजादिभि:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3395)
- **Original**: 9 खनानि नद्यो रम्याणि सरांसि कमलाकरा: । पुंस्कोकिलाभिलापाश्च मनोज्ञान्यम्बराणि च
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3396)
- **Original**: 10 भूषणान्यतिशुभ्राणि गन्धाक्यं चानुलेपनम्‌ । बीणाबेणुपृदड्ानां स्वनास्तूर्याण च द्विज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3397)
- **Original**: 11 एतान्यन्यानि चोदारभाग्यभोग्यानि दानवै: । दैत्योरगैश॒भुज्यन्ते पातालान्तरगोचरै:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3398)
- **Original**: 12 पातालानामथशश्चास्ते विष्णोर्या तामसी तनु: । शेषाख्या यद्रुणान्वक्तुं न शक्ता दैत्यदानवा:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3399)
- **Original**: 13 स सहस्लशिरा व्यक्तस्वस्तिकामछभूषण:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3400)
- **Original**: 14 फणापणिसहस्नेण य: स विद्योतयन्दिश: । सर्बान्करोति निर्वीर्यान्‌ हिताय जगतो5सुरान्‌
- **Translation**: 

---

