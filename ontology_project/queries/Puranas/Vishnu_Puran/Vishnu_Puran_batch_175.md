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

### Verse 1 (Vishnu Puran 0.3481)
- **Original**: 25 असिपत्रवनं याति बनच्छेदी वृथैव यः। औरभ्रिको मृगव्याधो बह्विज्वाले पतन्ति वै
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3482)
- **Original**: 26 यान्त्येते द्विज तत्रेज ये चापाकेषु वहिदा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3483)
- **Original**: 27 ज्रतानां लोपको यश् स्वाश्रमाद्विव्युतश्न य: । सन्दंशयातनामध्ये.. पततस्तावुभावषि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3484)
- **Original**: 28 दिवा स्वप्ने च स्कत्दन्ते ये नरा ब्रह्मचारिण: । पुत्रैरध्यापिता ये चर ते पतन्ति श्रभोजने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3485)
- **Original**: 29 एते चान्ये चर नरका: झतझो5थ सहस्नद्य: । येषु दुष्कृतकर्माण: पच्यन्ते यातनागता:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3486)
- **Original**: 30 यथैव पापान्येतानि तथान्यानि सहस्नद्ञः । भुज्यन्ते तानि पुरुषैर्नरकान्तरगोच्रै:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3487)
- **Original**: 31 बर्णाश्रपविरुद्धे च कर्म कुर्बन्ति ये नरा: । कर्मणा मनसा वाच्या निरयेषु पतन्ति ते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3488)
- **Original**: 32 अधःशिरोभिदृश्यन्ते नारकैर्दिय देवता: । देबाश्चाधोमुखान्सर्वानध: पह्यन्ति नारकान्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3489)
- **Original**: 33 स्थाबरा: कृमयोउब्जाश्व पक्षिण: पशवो नरा: । धार्मिकाखिदशास्तदून्पोक्षिणश्ष॒यथाक्रमम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3490)
- **Original**: 34 सहस्तभागप्रथ्मा. द्वितीयानुक्रमास्तथा । सर्बे छोते महाभाग यावन्पुक्तिसमाञअ्रया:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3491)
- **Original**: 35 यावन्तो जन्तव: स्वर्गे तावन्तो नरकौकस: । पापकृद्याति नरक॑ प्रायश्चित्तपराहमुख:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3492)
- **Original**: 36 पापानामनुरूपाणि प्रायश्ित्तानि यद्यथा। तथा तथैव संस्मृत्य प्रोक्तानि परमर्षिभि:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3493)
- **Original**: 37 पापे गुरूणि गुरुणि स्वल्पान्यल्पे च तद्ठिदः । प्रायक्षित्तानि प्रैत्रेय जगु: स्वायाभुवादय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3494)
- **Original**: 38 आयश्चित्तान्यहोषाणि तपःकर्मात्मकानि वे । यानि तेषामशेषाणां कृष्णानुस्मरणं परम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3495)
- **Original**: 39 आदि पर्वदिनोंका कार्य करानेवाल्त्र द्विज, घरमें आग रूगानेबात्म, मित्रकी हत्या करनेवाला, शकुन आदि जतानेबाल्ग, आमका पुरोहित तथा सोम (मदिरा) बेचने- यवाला--ये सब रुधिरान्यनर्कमें गिरते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3496)
- **Original**: यज्ञ अथवा ग्रामको नष्ट करनेवाल्प्र पुरुष जाता है, तथा जो लोग चीर्यपातादि करनेवाले, स्वेतॉक्त बाड़ तोड़नेवाले, अपवित्र और छलवयुतिके आश्रय रहनेवाले होते हैं वे कृष्णनस्कमें गिरते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3497)
- **Original**: जो बृथा ही वनोंको काटता है बह असिपत्रवननरकमें जाता है। मेषोपजीवी (गड़रिये) और व्याधगण बह्विज्वालनस्कमें गिरते हैं तथा हे ट्विज ! जो कच्चे घड़ों अथवा ईंट आदिको फ्कानेके लिये उनमें अप्रि डालते हैं, ये भी उस (वहिज्वालनस्क) में ही जाते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3498)
- **Original**: ब्रतोंकों स्जेप करनेवाले तथा अपने आश्रमसे पत्ित दोनों ही प्रकारके पुरुष सन्देश नामक नरकमें गिरते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3499)
- **Original**: जिन ब्रह्मचारियोंका दिनमें तथा सोते समय [जुरी भावनासे] वीर्यपात हो जाता है, अथवा जो अपने ही पुत्रॉंसे पढ़ते है ये त्लेग श्रभोजननरकमें गिरते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3500)
- **Original**: इस प्रकार, ये तथा अन्य सैकड़ों-हजारों नरक हैं, जिनमें द्ृष्कर्मी ल्लोग नाना प्रकास्की यातनाएँ भोगा करते है
- **Translation**: 

---

