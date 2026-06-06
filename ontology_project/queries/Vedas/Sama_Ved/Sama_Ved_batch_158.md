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

### Verse 1 (Sama Ved 0.3141)
- **Original**: [पवित्र करने वाला सोम अंतरिक्ष (चतुर्व लोक) वासी दिव्य सोम है तथा पवित्र होने वाला सोम वनस्पतियों से प्राप्त सोष है, जो पवित्र होकर अपनी दिव्य क्षपताएँ प्रकट कर सकता है।] 1217. अयुक्त सूर एतशं पवमानों मनावधि । अन्तरिक्षेण यातवे
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3142)
- **Original**: यह पवित्र सोम, अभीष्ट ऊर्ध्व गति पाने के लिए संकल्पित याजकों को सूर्य के अश्वों (किरणों ) जैसा वेग प्रदान करने में समर्थ है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3143)
- **Original**: 1218. उत त्या हरितो रथे सूरो अयुक्त यातवे । इन्दुरिन्द्र इति ब्रुवन्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3144)
- **Original**: इन्द्रदेव सोम को पुकारते हुए, हरितवर्ण वाले अश्वों को सूर्य के रथ में जाने के लिए युक्त करते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3145)
- **Original**: इति पञ्ञम: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3146)
- **Original**: के के के
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3147)
- **Original**: पषष्ठ: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3148)
- **Original**: 1219. अर्ग्नि वो देवमग्निभि: सजोषा यजिष्ठं दूतमध्वरे कृणुध्वम्‌ । यो मत्येंषु निश्वुविर्रुतावा तपुर्मूर्धा घृतान्‍न: पावक:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3149)
- **Original**: है देवताओ ! अनेक अग्नियों में पूज्य, उस यज्ञाग्नि को दूत बनाकर प्रयुक्त करो, जो अग्नि, देवता होकर भी मनुष्य का साथी है, घृत जिसका आहार है और जिसका तेज विकारनाशक एवं पवित्रता प्रदान करने चाला है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3150)
- **Original**: 1220, प्रोथदश्वो न यवसे5विष्यन्यदा मह: संवरणाद््यस्थात्‌ । आदस्य वातो अनु वाति शोचिरध स्म ते ब्रजनं कृष्णमस्ति
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3151)
- **Original**: हिन- हिनाते घोड़े जिस प्रकार घास को चरते चले जाते हैं, उसी प्रकार दावानल वृक्षों को उद्रस्थ क<7 चलता है । उस अवस्था में वायु के प्रभाव से जिस ओर काला धुआँ जाता है, वही मार्ग अग्नि का होता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3152)
- **Original**: रद सामवेद- संहिता 1221. उद्यस्य ते नवजातस्य वृष्णो5ग्ने चरन्त्यजरा इधाना: । अच्छा द्यापरुषो धूम एपि सं दूतो अग्न ईयसे हि देवान्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3153)
- **Original**: हे यज्ञाग्ति ! आपकी नवौन ज्वालाएँ वृष्टि करने में समर्थ हैं । हे प्रकाशित यज्ञाग्नि ! आप नष्ट न होने वाली अपनी ऊर्जा सहित द्युलोक में पहुँचकर देवों को तुष्ट करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3154)
- **Original**: 1222. तमिन्द्रं वाजयामसि महे वृत्राय हन्तवे ।स वृषा वृषभो भुवत्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3155)
- **Original**: इद्धदेव स्वयं हो बलशालोी है । बृत्रासुर (राक्षसी वृत्तियों) के विनाश के लिए उन्हें हम और अधिक बललान्‌ बनाते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3156)
- **Original**: 1223. इन्द्र: स दामने कृत ओजिष्ठ: स बले हितः । झुम्नी श्लोकी स सोम्यः
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3157)
- **Original**: दान देने के लिए ही पैदा हुए इन्द्रदेव बलवान्‌ बनने के लिए सोमपान करते हैं । प्रशंसनीय कार्य करने वाले इन्द्रदे सोम पिलाये जाने योग्य हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3158)
- **Original**: 1224. गिरा वच्रो न सम्भृत: सबलो अनपच्युत: । बवक्ष उग्रो अस्तृत:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3159)
- **Original**: वज्रपाणि, स्तुतियों से प्रशंसित, बलवान्‌, तेजस्वी, वीर और अपराजेय इन्द्रदेव, साधकों को ऐश्वर्य देने की इच्छा रखते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3160)
- **Original**: इति षष्ठ: खण्ड:
- **Translation**: 

---

