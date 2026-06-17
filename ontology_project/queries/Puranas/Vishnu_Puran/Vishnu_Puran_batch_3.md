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

### Verse 1 (Vishnu Puran 0.41)
- **Original**: क्रोध तो मू्खोंको ही हुआ करता है, बिचारवानोंकों भला कैसे हो सकता है ? भैया ! भल्ण कौन किसीको मारता है ? पुरुष स्वय हो अपने कियेका फल भोगता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.42)
- **Original**: है प्रियवर ! यह क्रोध तो मनुष्यके अत्यन्त कष्टसे सद्चित यश और तपका भी प्रबल नाझक है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.43)
- **Original**: हे तात ! इस ल्त्रेक' और परस्णेक दोनॉक्य्रे बिगाड़नेवाझे इस क्रोधका महर्षिगण सर्वदा त्याग करते हैं, इसलिये तू इसके वशीभूत मत हो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.44)
- **Original**: अब इन बेचारे निरफााध राक्षसोंको दग्ध करनेसे कोई ल्मभ नहीं; अपने इस यज्ञको समाप्त करो । साधुओंका घन तो सदा क्षमा ही है”'
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.45)
- **Original**: महात्मा दादाजीके इस प्रकार समझानेपर उनकी बातोंके गौरबका बिचार करके मैंने यह यज्ञ समाप्त कर दिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.46)
- **Original**: इससे मुनिश्चे8न्‍्ठ भगवान्‌ बसिष्ठजी बहुत प्रसन्न हुए। उसी समय ब्रह्माजीके पुत्र पुलस्त्यजी वहाँ आये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.47)
- **Original**: है मैत्रेय ! पितागह [वसिप्ठजी] ने उन्हें अर्ध्य दिया, तब वे महर्षि पुलहके ज्येष्ठ भ्राता महाधाग पुलूस्यजी आसन गअहण करके मुझसे खोले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.48)
- **Original**: आ0 2 ] ज्रथप अंश लि] पुलस्त्य उवाच बैरे महति यद्दाक्यादगुरोरद्याश्रिता क्षमा। त्वया तस्मात्ससस्तानि भवाउ्च्छास्राणि वेत्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.49)
- **Original**: 28 त्वया तस्मान्महाभाग ददाम्यन्य महावरम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.50)
- **Original**: 257 पुराणसंहिताकर्ता भवरान्बत्स भविष्यति। देवतापारमार्थ्य चर बथाबद्वेल्यत्ें भवान्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.51)
- **Original**: 26 प्रवृत्ते न निवृत्ते चर कर्मण्यस्तमला मत्तिः । मत्पसादादसन्दिग्धा लब् वत्स भविष्यति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.52)
- **Original**: 27 ततश्व प्राह भगवान्वप्लिष्ठो मे पितामहः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.53)
- **Original**: पुलस्येन यदुक्त ते सर्वमेतद्धविष्यति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.54)
- **Original**: 28 इति पूर्व बसिष्ठेन पुलस्येन च॑ धीमता । यदुक्ते तत्स्पृर्ति याति त्वव्पश्नादरिलं मम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.55)
- **Original**: 29 सो$हई वदाम्यशेष ते मैत्रेय परिपृच्छते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.56)
- **Original**: पुराणसंहितां सम्यक्‌ तां निद्योध यथातथम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.57)
- **Original**: 30 विष्णोः सकाश दुख नं जगत्तत्रैव च स्थितम्‌ स्थितिस जगतो5स्प जगच्च सः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.58)
- **Original**: 319 पुलूस्त्यजी बोले--तगु्ने, चित्तर्में पड़ा बैरभाव रहतेपर भी अपने यड़े-यूदे यसिप्तजीके कहनेसे द्ामा स्वीकार सत्र है, इसलिये तुम सम्पूर्ण शास्त्रोंक ज्ञाता होगे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.59)
- **Original**: है महाभाग ! अत्यन्त क्रोधित होउे52 भी तुमने मेरी सन्तानका सर्वथा पृल्ल्रेच्छेद नहीं किया; अतः मै तुम्हें एक और उत्तम वर देता हूँ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.60)
- **Original**: है उत्स ! तुम पुराणसंहिताके बक्ता होंगे और देखताओंके यथार्थ स्वरूपकों जानोगे
- **Translation**: 

---

