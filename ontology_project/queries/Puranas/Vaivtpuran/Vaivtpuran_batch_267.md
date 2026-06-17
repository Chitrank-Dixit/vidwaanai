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

### Verse 1 (Vaivtpuran 13.11482)
- **Original**: जीवननिर्वाह करते हैं। सूर्य अपनी किरणोंद्वारा करता है; निःसंदेह उसे ब्रह्महत्यांकं समान पाप
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11483)
- **Original**: जो धरतीका जल सोख लेते हैं, वर्षाकालमें उसी लगता है। जो नारायणके अंशभूत ब्राह्मणों तथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11484)
- **Original**: जलका उनसे प्रादुर्भाव होता है। सूर्य और मेघ गौओंका बध करते हैं, वे मनुष्य जबतक चन्द्रमा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11485)
- **Original**: आदि सबका विधाताद्वारा निरूपण होता है। और सूर्यकी सत्ता है, तबतकके लिये कालसूत्र
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11486)
- **Original**: पशञ्चाज्ोंके अनुसार जिस वर्षमें जो मेघ गज और नामक नरकमें जाते हैं*। समुद्र माने गये हैं, जो शस्याधिपति राजा और नारद! ऐसा कहकर श्रीकृष्ण चुप हो गये। मन्त्री निश्चित किये गये हैं; उन सबका तब आनन्दयुक्त ननन्‍्दने मुस्कराते हुए उनसे कहा।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11487)
- **Original**: विधाताद्वारा ही निरूपण हुआ है। प्रत्येक वर्षमें नन्द बोले--बेटा! यह महात्मा महेन्द्रकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11488)
- **Original**: जल, शस्य तथा तृणोंकी आढक-संख्या निश्चित पूजा है, जो पूर्वपरम्परासे चली आ रही है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11489)
- **Original**: की जाती है, उस निश्चयके अनुसार वर्ष-वर्षमें, यह सुवृष्टिका साधन है और इससे सब प्रकारके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11490)
- **Original**: युग-युगमें और कल्प-कल्पमें वे सारी बातें मनोहर शरस्योंकी उत्पत्ति ही साध्य है। शस्य ही
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11491)
- **Original**: घटित होती हैं। ईश्वरकी इच्छासे ही जल आदिका प्राणियोंके प्राण हैं। शस्यसे ही जीवधारी जीवन-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11492)
- **Original**: आविर्भाव होता है। उसमें कोई बाधा नहीं पड़ती। निर्वाह करते हैं। इसलिये ब्रजवासी लोग पूर्व
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11493)
- **Original**: तात! भूत, वर्तमान और भविष्य तथा महान्‌, पीढ़ियोंके क्रमसे महेन्द्रकी पूजा करते चले आ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11494)
- **Original**: ्षुद्र और मध्यम--जिस कर्मका विधाताने निरूपण रहे हैं। यह महान्‌ उत्सव वर्षके अन्तमें होता
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11495)
- **Original**: किया है, उसका कौन निवारण कर सकता है? है। विप्न-बाधाओंकी निवृत्ति और कल्याणकी [ईश्वरकी आज्ञासे ही ब्रह्माजीने सम्पूर्ण चराचर प्राप्ति ही इसका उद्देश्य है। जगतू्‌का निर्माण किया है। पहले भोजनकी *भुक्तवन्तीं तृणं यश्च गां वार्यति कामत: । ब्रह्महत्या भवेत्‌ तस्य प्रायश्वित्ताद्‌ विशुध्यति
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11496)
- **Original**: सर्वे देवा गवामज़ें तीर्थानि तत्पदेषु च । तदगुद्योपु स्वयं लक्ष्मीस्तिपरत्येवः सदा पित:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11497)
- **Original**: गोष्पदाक्तत्‌ृदा यो हि तिलक॑ कुस्ते नर: । तीर्थल्नातो भवेत्‌ सद्यो जयस्तस्थ पदे पदे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11498)
- **Original**: गावस्तिझ्न्ति. यत्रैेव _तत्तीथ॑ परिकोीर्तितम्‌ । प्राणांस्त्यक्त्वा नरस्ततन्न सद्यो मुक्तों भवेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11499)
- **Original**: ब्राह्मणानां गवामड्रं यो हन्ति मानवाधम: । ब्रह्महत्यासम॑ पाप॑ भवेत्‌ तस्थ न संशयः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11500)
- **Original**: नारायणांशानू विप्रांक्ष गाश्ष ये प्नन्ति मानवा:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11501)
- **Original**: कालसूत्र च ते यान्ति यावच्चन्द्रदिवाकरौ
- **Translation**: 

---

