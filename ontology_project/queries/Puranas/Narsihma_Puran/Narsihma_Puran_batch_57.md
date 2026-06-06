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

### Verse 1 (Narsihma Puran 0.1121)
- **Original**: एवं मुने सृष्टिरियं तवेरिता देवासुराणां नरनागरक्षसाप्‌। वियन्मुखानामपि य पठेदिरद श्रृण्व॑श्न भवत्या हरिलोकमेति सः
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.1122)
- **Original**: 9 बाद इन्द्का दर्प चूर्ण करनेवाला पुत्र तुम्हारे गर्भरों उत्प्र होगा।' कश्यपजीके यों कहनेपर दितिने उस गर्भको धारण किया
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.1123)
- **Original**: 1--4 # इच्धकों भो जब यह समाचार शञात रहने लगे। जब सौ वर्ष पूर्ण होनेमें कुछ ही कमी रह गयी, तब एक दिन दिति (भोजनके पश्चात्‌) पैर धोये बिना ही शब्यापर आखूढ़ हो, सो गयी। इधर इद्धने भी अवसर प्राप्त हो जानेसे यज् हाथमें ले, दितिके उदरमें प्रकिष् हो, वज़ले उस गर्भके सात टुकड़े कर दिये। उनके द्वाय काटे जानेपर बह गर्भ रोने लगा। तब इन्द्रने “मा रोदी:' (मत शोओ)-यों कहते हुए पुनः: एक एकके सात सात॑ टुकड़े कर डाले। इस तरह सात-सात टुकड़ॉमें बेटे हुए ये सातों खण्ड ' मास्त' नामसे विख्यात हुए; क्योंकि जन्म होते हो इख्रने उन्हें 'मा रोदीः '-इस प्रकार कहा था। ये सभो इन्धके सहायक “मख्तू' नामक देवता हुए 47--8
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.1124)
- **Original**: भुने! इस प्रकार मैंने तुमसे देवता, असुर, नर, भाग, गाक्षसत और आकाश आदि भूतोंकी सृष्टिका वर्णन किया। जो इसका भक्तिपूबंक पाठ अधब्रा श्रषण करता हैं, वह विष्णुलोकको प्राप्त होता है
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.1125)
- **Original**: इवि वीशासिंहएुएणे (विंशवितयो: ध्कय:
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.1126)
- **Original**: 20 2 इस एकार औनरसिंहपराजम 'मतक़ोंकी उत्पत्ति कपक बीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.1127)
- **Original**: दि सूर्ययंशका बर्णन भंरदाज उप्राप अनुसर्गश्च सर्गक्ष त्वया चित्रा कथेरिता। भ्रद्वाजजी बोले--सूतजों! आपने 'सर्ग' और *अनुसग्ग' का वर्णन किया, विचित्र कथाएँ सुनायों; अर मुझसे राजाओंके यंश., मन्वन्तर तथा खंशानुचरितिफा वर्णन बंशमन्वन्तरे ब्रूहि वंशानुचरितं तर में
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.1128)
- **Original**: युत उकाच राज्ञां वंश: पुराणेषु विस्तरेण प्रकोर्तित:। सूतजी बोले-- पुराणोंमें राजओंके त्रंशका चिस्तार- चूर्वक वर्णन किया गया है; यहाँ मैं राजाओंके वंश. तथा संशानुचश्तिका संश्षेपसे. वर्णन संक्षेपात्‌ कथयिष्यामि बंशमन्वन्तराणि ते
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.1129)
- **Original**: 2 करूँगा। महामतें विप्रवर! इसे आप तथा अन्य वंशानुचरित चैव श्रृणु बिप्र महामते। मुनि भी, जो कथाश्रवणके लिये यहाँ आकर ठहरे श्रृण्वन्तु मुनयश्षेमे श्रोतुपागत्य ये स्थिता:
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.1130)
- **Original**: हुए हैं, सु्ें
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.1131)
- **Original**: चिद कश्यपादादित्य:
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.1132)
- **Original**: आदित्यान्मनु;। मनो- रिक्ष्वाकु:, इडक्ष्वाकोर्विकुक्षि:। विकुक्षेद्योति:, चोतादेनो वेनात्पयूथु: पृथो: पृथाश्च:
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.1133)
- **Original**: पृथाश्चादसंख्याताश्व: । असंख्याताश्वा- न्मान्धाता
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.1134)
- **Original**: माश्धातु: पुरुकृत्स: पुरुकुत्साददपदो दृषदादभिशम्भु:
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.1135)
- **Original**: अभिशम्भोर्दारुणो दारुणात्‌ सगरः
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.1136)
- **Original**: सगराद्धर्वश्वो हर्यश्चाद्धारीत:
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.1137)
- **Original**: हारीताद्रोहिताश्वो रोहिताश्वादंशुमान्‌। अंशुमतो भगीरथः
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.1138)
- **Original**: भगीरथात्‌ सौदास: सौंदासा- च्छब्नुंदम:
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.1139)
- **Original**: शत्रुंदमादनरण्य:। अनरण्याद्दीर्धबाहु:। दीर्घबाहोरज:
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.1140)
- **Original**: अजाइशरथ:,. दशरथाद्राम:,.._ रामाह्नव:, लबात्‌ पड़ा:
- **Translation**: 

---

