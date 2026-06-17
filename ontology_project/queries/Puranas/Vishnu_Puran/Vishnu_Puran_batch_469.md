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

### Verse 1 (Vishnu Puran 0.9361)
- **Original**: 38 मनुष्यलीलां भगवन्‌ भजता भवता सुरा: । विडम्बयन्तस्त्वल्लीलां सर्व एवं सहासते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9362)
- **Original**: 39 अबतार्य भबान्पूर्व गोकुले तु सुराड्रनाः । क्रीडार्थमात्मन: पश्चादवतीणोसि शाश्वत
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9363)
- **Original**: 40 अत्रावतीर्णयो: कृष्ण गोपा एवं हि बान्धवाः । गोप्यक्ष सीदत: कस्मादेतान्बन्धूनुपेक्षसे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9364)
- **Original**: 49 दर्शितो मानुषो भावों दर्शितं बालचापलम । तदयं दम्यतां कृष्ण दुष्टात्मा दशानायुथ:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9365)
- **Original**: 42 पञश्चम अंश झ्र7 कुष्णके बिना साथ किये अब हम गोकुल नहीं जायैंगी; क्योंकि इनके बिना वह जरूहीन सरोवरके समान अत्यत्त अभव्य और असेब्य है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9366)
- **Original**: जहाँ नीककमलदलकी सी आधभावाछे ये दयामसुन्दर हरि नहीं हैं उस मात-मन्दिर्से भी प्रीति होना अत्यन्त आश्चर्य ही है। 29
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9367)
- **Original**: अरी! खिले हुए कमलदलके सदृद कान्तियुक्त नेत्रॉवाले श्रीहरिको देखे बिना अत्यन्त 74 तुम किस प्रकार वजमें रह सकग्रेगी ?
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9368)
- **Original**: जिन्हें अपनी अत्यच्त मनोहर बोलीसे हमारे सम्पूर्ण मनोरघोंको अपने वशीभूत कर लिया है उन कमलनयन कृष्णचन्द्रके बिना हम नन्‍्दरजीके गोकुल्ठकों नहीं जायैंगी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9369)
- **Original**: अरी गोपियों ! देखो, सर्पराजके फणसे आबृत होकर भी श्रीकष्णका मुख हमें देखकर मधुर मुसकानसे सुशोभित जो रहा है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9370)
- **Original**: श्रीपराशरजी खोले-- गोपियोंके ऐसे वचन सुनकर तथा आसविह्लऊ चकितमनेत्र गोपोक, पुत्रके मुखपर दुष्टि लगाये अत्यन्त दीन नन्‍दजीको और मूर्च्छाकुल यज्ञोदाको देखकर महाबली ग्रेहिणीनन्दन बलरामजोने अपने सड्े तमें कृष्णजीसे कहा--
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9371)
- **Original**: “हे देवदेवेश्वर ! क्या आप अपनेकों अनन्त नहीं जानते ? फिर किसलिये यह अत्यन्त मानव-भाव व्यक्त कर रहे हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9372)
- **Original**: पहियोंकी नाभि जिस प्रकार अशेंका आश्रय होती है उसी प्रकार आप ही जगतके आश्रय, कर्ता, हर्ता और रक्षक हैं तथा आप ही अल्प्रेक्यस्थवरूप और वेदत्रयीमय हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9373)
- **Original**: हे अचिन्त्यात्मन्‌ ! इन्द्र, रुद्ष, भप्रि, बसु, आदित्य, मरुद्रण ओ और अश्विनीकुमार तथा समस्त योगिजन आफहीका चित्तन करते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9374)
- **Original**: हे जगन्नाथ ! संसारके हितके लिये पृथिवीका भार उतारनेकी इच्छसे ही आपने सर्त्वलोकमें अवतार लिया है; आपका अग्रज मैं भी आपह्दीका अंझ हूँ। 38
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9375)
- **Original**: हे भगबन्‌ ! आपके मनुष्य- लील्म करनेपर ये गोपवेषधारी समस्त देवगण भी आपकी लोल्ाओंका अनुकरण करते हुए आपहीके साथ रहते हैं। 39
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9376)
- **Original**: हे शाश्वत! पहले अपने विहारार्थ देवाड्रगाओंको गोपीरूपसे गोकुलमें अवतीर्णकर पीछे आपने अबतार लिया है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9377)
- **Original**: हे कृष्ण ! यहाँ अवतीर्ण होनेपर हम दोनोकि तो ये गोप और गोपियाँ ही बान्धव हैं; फिर अपने इन दु:खी बान्धवोकी आप क्यों उपेक्षा करते हैं ।41
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9378)
- **Original**: है कृष्ण
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9379)
- **Original**: यह मनुष्यभाव और बालचापल्य तो आप बहुत दिख्वा चुके, अब तो ीघ्र ही इस दुष्टात्पाका जिसके दास्त्र दाँत ही हैं, दपन कीजिये”
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9380)
- **Original**: श्रोपराशर उवाच इति संस्मारित: कृष्ण: स्मितभिन्नोष्ठ सम्पुट: । आस्फोट्य मोचयामास स्वढेह भोगिबनधनात्‌
- **Translation**: 

---

