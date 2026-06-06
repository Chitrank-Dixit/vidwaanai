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

### Verse 1 (Vishnu Puran 0.3241)
- **Original**: पर्वतोंमें पहल्म कुमुद, दूसरा उन्नत और तौसरा बलाहक है तथा चौथा ड्रोणाचल है, जिसमें नाना प्रकारकी महौषधियाँ हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3242)
- **Original**: पाँचवाँ कहक्कू, छठ महिष और सातवाँ गिरिवर ककुंदान्‌ है। अब नदियोंके नाम सुनो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3243)
- **Original**: 116 श्रीविष्णुपुराण [ आ0 4 योनिस्तोया वितृष्णा च॒ चन्द्रा मुक्ता विमोचनी । निवृत्ति: सप्तमी तासां स्मृतास्ता: पापशान्तिदा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3244)
- **Original**: 28 श्रेतज्ष हरित चैव बैद्युत॑ मानसं तथा। जीपूते रोहितं चैब सुप्रभं चापि झोभनम्‌। सप्तैतानि तु वर्षाणि चातुर्वर्ण्ययुतानि वै
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3245)
- **Original**: 29 शाल्यले ये तु वर्णाश्॒ वसन्‍्त्येते महामुने । कपिलाओआरुणा: पीता: कृष्णाशैब पृथक्‌ पृथक्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3246)
- **Original**: 30 वायुभूत॑ मखश्रेन्नैर्यज्वानो यज्ञसंस्थितिम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3247)
- **Original**: 31 देवानाम्त्र सान्निध्यमतीव सुमनोहरे । झाल्मलि: सुमहान्वृक्षो नाम्ना निर्वतिकारक:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3248)
- **Original**: 32 एष द्वीप: समुद्रेण सुरोदेन समावृतः। विस्ताराच्छाल्मलस्यैव समेन तु समन्तत:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3249)
- **Original**: 33 शाल्मलप् तु विस्ताराद द्विगुणेन समन्तत: ।। 34 ज्योतिष्मत: कुशद्वीपे सप्त पुत्राउन्कृणुष्न तान्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3250)
- **Original**: 35 उद्धिदो वेणुमांश्रैव बैरथो लम्बनो धृति: । प्रभाकरो5थ कपिलस्तज्नामा बर्षपद्धतिः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3251)
- **Original**: 36 तस्मिन्वसन्ति मनुजाः सह दैतेयदानवेः। तथैव देवगश्चर्वयक्षकिम्पुरुषादय:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3252)
- **Original**: 37 बर्णास्तत्रापि चत्वारों निजानुष्ठानतत्परा: । दमरिनः शुष्पिण: स्त्रेहा मन्देहाक्ष महामुने
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3253)
- **Original**: 38 व्राह्मणा: क्षत्रिया वैश्या: शुद्राक्षानुक़मोदिता:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3254)
- **Original**: 39 यथोक्तकर्मकर्तृत्वात्खाधिकारक्षयाय ते । तत्रैव त॑ कुशद्वीपे ब्रह्मरूपं जनार्दनम्‌। यजन्त: क्षपयन्त्युग्रमधिकारफलप्रदम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3255)
- **Original**: 40 विद्दपों हेमवौल्ष झ्युतिमान्‌ पुष्पवांस्तथा । कुशेशयो हरिश्वैव सप्तमो मन्दराचल:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3256)
- **Original**: 491 वर्षाचलास्तु सप्तैते तत्र द्वीपे महामुने। नद्यश्न सप्त तासां तु श्रृूणु नामान्यनुक्रमात्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3257)
- **Original**: 42 धृतपापा झिवा चैव पवित्रा सम्मतिस्तथा । विद्युदम्भा मही चान्या सर्वपापहरास्त्विपा:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3258)
- **Original**: 43 वे योनि, तोया, वितृष्णा, चन्द्रा, मुक्ता, विमोचनी और निवृत्ति हैं तथा स्मरणमात्से ही सारे पापोक्रो शात्त कर देनेवाली हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3259)
- **Original**: श्रेत, हरित, बैद्युत, मानस, जीमूत, रोहित और अति शोभायमान सुप्रम--ये उसके चारों वर्णोंसे युक्त सात वर्ष हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3260)
- **Original**: हे महामुने
- **Translation**: 

---

