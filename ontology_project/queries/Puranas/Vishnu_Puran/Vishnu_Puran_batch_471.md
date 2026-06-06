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

### Verse 1 (Vishnu Puran 0.9401)
- **Original**: योगिजन जिनके नित्यस्वरूपकों यत्र करनेपर भी नहीं जान पाते तथा जो परमार्थरूप अणुसे भा अणु और स्थूछसे 'भो स्थूल है उसे हम नमस्कार करती हैं। 55
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9402)
- **Original**: जिनके जन्पमें विधाता और अन्तमें काछ हेतु नहीं हैं तथा जिनका स्थितिकर्ता भी कोई अन्य नहीं है उन्हें सर्वदा नमस्कार करतों हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9403)
- **Original**: इस कालियनागके दमनमें आपको थोड़ा-सा भी क्रोध नहों है, केबल लोकरक्षा ही इसका हेतु है; अतः हमारा निवेदन सुनिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9404)
- **Original**: हे क्षमाज्ञील्हॉमें श्रेष्ठ ! साधु प्रुषोंको स्त्रियों तथा मूह और दीन जन्तुऑपर सदा ही कृपा करनी चाहिये; अतः आप इस दीनका अपराध क्षमा कीजिये।
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9405)
- **Original**: प्रभो आप सम्पूर्ण संसार्के अधिष्ठान हैं और यर सर्प तो [ आपकी अपेक्षा ] अत्यन्त नलूटीन है । आपके चरणोंसे पीड़ित होकर तो यह आधे मुहूर्तमें ही अपने प्राण छोड़ देगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9406)
- **Original**: हे अच्यय ! प्रीति समानसे और द्वेष उत्कष्टसे देखे जाते हैं; फिर कहां तो यह अल्पवीर्य सर्प और कहाँ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9407)
- **Original**: अः7 ] ततः कुरू जगत्स्वामिग्नसादमबसीदत: । प्राणास्यजति नागो5य॑ भर्तृभिक्षा प्रदीयताम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9408)
- **Original**: 57 भुखनेश जगन्नाथ महापुरुष पूर्वज । प्रार्णास्यजति नागो5व॑ भर्तृभिक्षां प्रयच्छ न:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9409)
- **Original**: 58 वेदान्तवेष्ल. देवेश . वुष्टदैल्यनिबर्हण । प्रार्णासत्यजति नागो5यं॑ भर्तृभिक्षा प्रदीयताम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9410)
- **Original**: 59 अ्रीपराशर उवाच इत्युक्ते ताभिराश्चस्य झ्लान्तदेहोउपि पन्नग: । ज्रसीद देवदेवेति प्राह वाक्य शनेः शनैः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9411)
- **Original**: 60 कालिय उवाच तवाष्टगुणमैश्वर्य नाथ स्वाभाविक परम्‌। निरस्तातिशयं यस्य तस्य स्तोष्यामि किन्वहम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9412)
- **Original**: 69 त्व॑ परस्त्व॑ परस्याद्य: पर॑ त्वत्त: परात्मक । परस्मात्परमो यस्त्व॑ तस्य स्तोष्यापि किन्वहम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9413)
- **Original**: 62 यस्मादब़ह्मा च॒ रूद्धश्न चद्धेद्रमरुदख्चिन: । वसवश्न सहादित्यैस्तस्प स्तोष्यामि किन्वहम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9414)
- **Original**: 63 एकावयवसूक्ष्मांशें यस्पैतदखिलं.. जगत्‌ । कल्पनावयवस्यांशस्तस्य स्तोष्यामि किन्वहम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9415)
- **Original**: 64 सदसद्रूपिणो यस्य व्रह्माद्यास्त्रिदशेश्वरा: । परमार्थ न जानन्ति तस्य स्तोष्यामि किन्वहम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9416)
- **Original**: 65 ब्रह्मारचितो यस्तु गन्धपुष्पानुलेपन: । नन्‍्दनादिसमुद्धूतैस्सो5र्च्यते जा कर्थ मया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9417)
- **Original**: 66 यस्यावताररूपाणि. देवराजस्सदार्चति । न वेत्ति परमं रूप सोउर्च्यते जा क॒र्थ मया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9418)
- **Original**: 67 विषयेभ्यस्समावृत्य सर्वाक्षाणि ख योगिन: । यमर्चयन्ति ध्यानेन सो3र्च्यते वा कथ मया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9419)
- **Original**: 68 हृदि सड्ूल्प्य यद्गुपं ध्यानेनार्चीन्ति योगिनः । भावपुष्पादिना नाथ: सोर्च्यते वा कर्ध मया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9420)
- **Original**: 69 सो#हं ते देवदेवेश नार्चनादौ स्तुता न च। सामर्थ्यवान्‌ कृपापात्रमनोवृत्ति: प्रसीद मे
- **Translation**: 

---

