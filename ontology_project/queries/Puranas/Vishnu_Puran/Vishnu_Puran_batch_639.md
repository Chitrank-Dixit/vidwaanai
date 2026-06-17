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

### Verse 1 (Vishnu Puran 0.12761)
- **Original**: 60 ( आ* 7 स्वाण्डिक्य बोले--है महयभाग ! यह बतल्तइये कि जिसका आश्रय करनेसे चितके सम्पूर्ण दोष नए हो जाते हैं बह बितका शुभाश्रय क्या है ?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12762)
- **Original**: केशिध्बज बोले-- हे राजन ! चित्तका आश्रय ब्रह्म है जो कि पूर्त डब्चैर अमूर्त अथवा अपर और पर-रूपसे स्वभावसे ही दो फ्रकारका है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12763)
- **Original**: हे मूप ! इस जगतमें बह्म, कर्म और उभयात्मक नामसे तीन प्रकारकी मावनाएँ हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12764)
- **Original**: इनमें पहल्ये कर्मभावना, दूसरी बह्मभावना और तीसरी उभयात्मिकाभावना कहलातो है। इस प्रकार ये त़िलिध भावनाएँ हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12765)
- **Original**: सनन्‍्दनादे मुनिजन ज्ह्मभावनासे युक्त हैं और देवताओंसे छेकर रथानर- जंगमपर्वन्त समस्त प्राणी कर्मभावनायुक्त हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12766)
- **Original**: तथा [स्वरूपविघयक
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12767)
- **Original**: नोध और [स्वर्गादिविषयक] अधिकारसे युक्त हिरण्यगर्भादिपें.. अ्रह्मकर्ममयी डरभयात्मिकाभावना है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12768)
- **Original**: है राजन्‌ ! जबतक चिदोष्ठ ज्ञानके हेतु कर्म क्षीण नहीं होते तमीतक अहंकारादि भेदके झ्ारण भिन्न दृष्टि स्खनेजाले मनुष्योंफों त्रह्म और ज़गत्‌की भिन्नता प्रतीत होती नै
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12769)
- **Original**: जिसमें सम्पूर्ण भेद शान हो जाते ऐं, जो सत्तामात्र और जाणीका अनिषय हे तथा स्वर्य हो अनुभव करनेयोग्य हैं, वही ब्रह्मज्ञान कहल्मता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12770)
- **Original**: यहां परयात्पा चिष्णुका अरूप नामक परम रूप है, जो उनके खिश्वरूपसे विल्कक्षण है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12771)
- **Original**: है गजन्‌ ! योगाभ्यासी जन पहले-पहल उस रूपका चित्तन नहों कर सकते, इसल्ख्यि उन्हें श्रीहरिके विध्वमय स्थूल रूपका ही चित्तम करना चाहिये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12772)
- **Original**: सिसण्यार्भ, भगवान बासुदेन, प्रजापति, मरूत, ससु. रुद्र, सूर्य, तारे, ग्रहगण, गन्धर्व, यक्ष और दैत्य आदि समस्त देखयोजियाँ तथा मनुष्य, पहु, पर्वत, समुद्र, नदो, लुश्ष. सम्पूर्ण भूत एवं प्रधानसे लेकर विोष (पप्मतन्मात्रा) पर्यन्त उनके कारण तथा चेतन, अचेतन, एक्र, दो अथन्ना अनेक चरणोंबाले प्राणी और बिना चरणोंवाले जीव--ये सब भगवान्‌ हृरिकि भाजनाजयात्मक मूर्तरूम हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12773)
- **Original**: 5760-94
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12774)
- **Original**: यह सघ्यूर्ण क्तराचर जगत्‌, परव्रहास्वकूप भगवान्‌ सिणष्णुका, उनकी दक्तिसे सम्पन्न 'जिश्व' नामक रूप हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12775)
- **Original**: अआः7छ ] विष्णुशक्ति: परा प्रोक्ता क्षेत्रज्ञाख्या तथाउपरा । अविद्या कर्मसंज्ञान्या तृतीया झक्तिरिष्यते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12776)
- **Original**: 61 यया क्षेत्रज्ञशक्तिस्सा वेष्टिता नृप सर्वंगा। संसारतापानखिलानवाश्रोत्यतिसन्ततानू
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12777)
- **Original**: 62 तया तिरोहितत्वाद्य शक्तिः क्षेत्रज्ञसंज्ञिता सर्वभूतेषु भूषाल तारतम्येन लक्ष्यते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12778)
- **Original**: 63 अप्राणबत्सु स्वल्पा सा स्थावरेषु ततो5धिका । सरीसृपेषु तेभ्योडपि ह्ातिझाकत्या पतत्त्रिषु
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12779)
- **Original**: 6ंड पतत््रभ्यो मृगास्तेभ्यस्तच्छवत्या पशवो5धिका: । पशुभ्यो मनुजाश्चातिशक्त्या पुंसः प्रभाविता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12780)
- **Original**: 65 तेभ्यो5षपि नागगश्धर्वयक्षाद्या देवता नूप
- **Translation**: 

---

