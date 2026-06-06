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

### Verse 1 (Vishnu Puran 0.12101)
- **Original**: हे मुनिश्रेष्ठ ! कल्युगमें सास और ससुर ही व्लेगोंके गुरुजन होंगे और हृदयहारिणों भार्या तथा साले ही सुद्दद्‌ होंगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12102)
- **Original**: स्त्रेग अपने ससुरके अनुगामी होकर कहेंगे कि 'ज़्वैन किसका पिता है और कौन किसकी माता; सब पुरुष अपने कर्मानुसार जच्मते-मरते रहते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12103)
- **Original**: ] घए्ठ अंश 427 बाड्डनःकायजैदोपैरभिभूता: पुनः पुनः । उस समय अल्पबुद्धि पुरुष बारम्बार वाणी, मन और नराः पापान्यनुदिन॑ करिष्यन्त्यल्पमेधसः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12104)
- **Original**: शरीरादिके दोषोंके वज्ीभूत होकर प्रतिदिन पुनः-पुनः निस्सत्ततानामशौचानां निह्लीकाणां तथा नृणाम्‌। यद्यददुःखाय तत्सर्व कल्काले भविष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12105)
- **Original**: 58 निस्स्वाध्यायवषदकारे स्वधास्वाहाविवर्जिते । पापकर्म करेंगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12106)
- **Original**: शक्ति, शौच और लज्जाहीन पुरुषोंकों जो-जो दुःख हो सकते हैं कलियुगमें ते सभी दुःख उपस्थित होंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12107)
- **Original**: उस समय संसारके स्वाध्वाय और वषटकारसे होन तथा स्वधा और स्वाहमसे वर्जित हो जानेसे तदा प्रविरलो धर्म: क्चिल्लोके निवल्यति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12108)
- **Original**: *हो-करहीं कुछ-कुछ धर्म रहेगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12109)
- **Original**: किंतु कलियुगमे तत्राल्पेनेव यत्रेन पुण्यस्कन्थमनुत्तमम्‌ मनुष्य थोड़ा-सा प्रयत्न करनेसे ही जो अत्यन्त उत्तम पुण्यराशि प्राप्त करता है यहों सत्ययुगमें महान्‌ तपस्यासे करोति य॑ कृतयुगे क्रियते तपसा हि सः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12110)
- **Original**: प्राप्त किया जा सकता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12111)
- **Original**: ््् श्र इति श्रीविष्णुपुराणे पश्नेंडशे प्रथमोडध्याय
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12112)
- **Original**: विजन, है 4 «00, दूसरा अध्याय श्रीव्यासजीद्वारा कलियुग, झूद्र और स््रियोंका महत्त्व-वर्णन श्रीपराद्ार उवाच व्यासश्वाह महाबुद्धिर्यदत्रैव हि बस्तुनि। तच्छूयतां महाभाग गदतो मम तत्त्वतः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12113)
- **Original**: कस्मिन्कालेडल्पको धर्मो ददाति सुमहत्फलम्‌ । मुनीनां पुण्यवादो5भूल्कैश्नासौ क्रियते सुखम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12114)
- **Original**: सन्देहनिर्णयार्थाय बेद्व्यासं॑ महामुनिम्‌। ययुस्ते संझायं प्रष्ठुं मैत्रेथ मुनिपुड्ढता:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12115)
- **Original**: दद्शुस्ते मुर्नि तत्र जाह्वीसलिले द्विज । वेदव्यास॑ महाभागमर्दस्न्नात॑ सुत॑ मम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12116)
- **Original**: स््रानावसानं ते तस्य गतीक्षन्तो महर्षय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12117)
- **Original**: तस्थुस्तीरी महानद्यास्तरुषण्डमुपाश्रिता:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12118)
- **Original**: ममप्नो5थ जाह्नबीतोयादुत्थायाह सुतो मम । शुद्रस्साधु: कलिस्साधुरित्येव॑ थृण्वतां बच:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12119)
- **Original**: तेषां मुनीनां भूयश्ष ममज् स नदीजले। साधु साध्विति चोत्थाय शुद्र धन्योउसि चाब्रवीत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12120)
- **Original**: निमअश्च समुत्थाय पुनः प्राह महामुनिः । योषितः साथु धन्यास्तास्ताभ्यो धन्यतरो5स्ति कः
- **Translation**: 

---

