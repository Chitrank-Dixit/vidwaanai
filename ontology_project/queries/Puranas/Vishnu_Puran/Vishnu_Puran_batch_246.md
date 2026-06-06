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

### Verse 1 (Vishnu Puran 0.4901)
- **Original**: 7 श्रीपराइरजी बोले--हे महामुने ! व्यासजीके शिष्य चैज्ञम्पायनने यजुर्वेदरूपी वृक्षकी सत्ताईस शाख्लाओंको रचना क्यी; और उन्हें अपने शिष्योंको पढ़या तथा हदिष्योंने श्री क्रमश: ग्रहण किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4902)
- **Original**: है द्विज ! उनका एक परम घार्सिक और सदैव गुरुसेवामें तत्पर रटनेवाला शिष्य ब्रह्मरातकर पुत्र याज्ञवल्क्य था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4903)
- **Original**: [एक समय समस्त ऋषिगणने मिलकर यह नियम किया कि) जो कोई महामेरुपर स्थित हमारे इस समाजमें सम्मिलित न होगा उसको सात यात्रियोंके भीतर ही अद्यहत्या लगेगी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4904)
- **Original**: है ट्विज ! इस प्रकार मुनियॉने पहले जिस समयको नियत किया था उसका केवल एक वैद्ञाग्पायनने ही अतिक्रमण कर दिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4905)
- **Original**: इसके पश्चात्‌ उन्होंने [प्रमादबह्ग] पैरसे छूए हुए अपने भानजेकी दृत्या कर डाली; तब उन्होने अपने दिष्योंसे कहा--'हे शिष्यगण ! तुम सब लोग किसी प्रकारका विचार न करके मेरे लिये अह्यह॒त्याको दुर करनेवास्म व्रत करो'
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4906)
- **Original**: आप ] तृतीय अंझ 1757 अथाह याज्ञवल्क्यस्तु किमेभिर्भगवन्द्दिजैः । क्लेशितैरल्पतेजोभिश्वरिष्येडहमिर्द॑ ब्रतम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4907)
- **Original**: 8 ततः क्ुद्धों गुरु: प्राह याज्ञवल्क्य महामुनिम्‌ । मुच्यतां यक्त्ययाधीतं मत्तो विप्रावमानक
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4908)
- **Original**: 9 निस्तेजसो वदस्थेनान्यरत्त्व ब्राह्मणपुड्रजान । तेन शिष्येण नाथों5स्ति ममाज्ञाभड्कारिणा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4909)
- **Original**: 10 याज्ञवल्क्यस्तत: प्राह भक्त्यैतत्ते मयोदितम्‌ । ममाप्यलं त्वयाथीतं यन्मया तदिदे द्विज
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4910)
- **Original**: 11 अफ्रशर उवाच इत्युक्तो रुधिराक्तानि सरूपाणि यंजूषि सः । छर्दयित्वा ददौ तस्मै ययो स स्वेच्छया मुनि:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4911)
- **Original**: 12 यजूंष्यध विसुष्टानि याज्ञवल्क्येन वे द्विज । जगृहस्तित्तिरा भूत्वा तैत्तिरीयास्तु ते ततः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4912)
- **Original**: 13 ब्रह्महत्याव्रतं चीर्ण गुरुणा चोदितैस्तु ये: । चरकाध्वर्यवस्ते तु चरणान्पुनिसत्तम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4913)
- **Original**: 14 याज्ञवल्क्यो5पि मैत्रेब प्राणायामपरायण: । तुष्टाव प्रयतस्सूर्य बजूंष्यभिलपंस्तत:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4914)
- **Original**: 157 याहूत्रल्कव उन्नान नमस्सविश्रे द्वाराय मुक्तेरमिततेजसे । ऋण्यजुस्सामभूताब त्रयीधाम्ने च ते नमः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4915)
- **Original**: 16 नमो5प्रीषोमभूताय जगत: कारणात्मने । भास्कराय पर॑ तेजस्सौषुप्ररूुचिविभ्रते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4916)
- **Original**: 17 कलाकाष्टानिमेषादिकालज्ञानात्मस्पपिणे । ध्येयाय विष्णुरूपाय परमाक्षररूपिणे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4917)
- **Original**: 18 बिभरत्ति यस्पुरगणानाप्यायेन्दु स्वरहिमिभि: । स्वधामृतेन व पितृस्तस्मै तृप्ययात्मने नमः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4918)
- **Original**: 19 हिमाम्बुघर्मबृष्टीनां कर्ता भर्ता च्ञ यः प्रभु: । तस्मै त्रिकालरूपाय नमस्सूर्याय बेधसे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4919)
- **Original**: 20 अपहन्ति तमो यश्व जगतोउस्य जगत्पति: । सत्त्वधामधरों देवों नमस्तस्मै बिवस्वते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4920)
- **Original**: 21 सल्कर्मयोग्यो न जनो नेबाप: शुद्धिकारणम्‌ । तब याज्ञवल्क्य बोले" भगवन्‌ ! ये सब त्राह्मण अत्यन्त निस्तेज हैं, इन्हें कष्ट देनेकी क्या आवश्यकता है? मैं अकेला ही इस अतका अनुष्ठान करूँगा''
- **Translation**: 

---

