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

### Verse 1 (Markende Puran 0.1961)
- **Original**: स्थान, सूर्यस्वरूप तथा प्रकाशात्परूप हैं। आपको शुध हो जाय।' सूर्की उसकी ज़पस्थाका उच्ेश्य नमस्कार हैं। प्रभाफा विस्तार करनेवाले आपको ज्ञात हो गया; अत: उन्होंने लिशवकर्मासे कहा-- आप
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1962)
- **Original**: नमस्कार है। दिगकों सृष्टि करनेवाले आपको मेरे तेजकों छौ8 डीजिये।” तब उन्होंने संत्रत्सररूप ' प्रणप है। रात्रिके हेतु भी आए ही हैं तथा संध्या , जकपाले सूर्चक॑ तेजकों छाँट दिया, उस समय
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1963)
- **Original**: और चाँदनोकी सृष्टि भी आप ही करते हैं; देखताओंने ठतकों बड़ी प्रशंसा को। तसदनन्तर। आपको नमस्कार है। देवताओं और ऋपैयोंने सम्पूर्ण त्रिधुवनके पूजनाय त््व॑ सर्वभेतद भगवन्‌ जगदुद्भ्रमता त्थया। भंगलान्‌ सूर्यकी स्तवर आरमंभ कियो--
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1964)
- **Original**: भ्रमत्याविद्धमखिलब्रह्मण्ड॑ सचराचरम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1965)
- **Original**: डक ऊ्ू: त्वदंशुभिरिद स्पृष्टं सर्व संजायते शु्ति
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1966)
- **Original**: जपस्ते प्रक्स्वरूपाय सामरूपाय ते चमः।
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1967)
- **Original**: क्रियते त्वत्करें: स्पर्शांज्जलादीतां पवित्रता
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1968)
- **Original**: भजुःस्वरूपरूपाय साप्तां धामवतें नम:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1969)
- **Original**: ' होमदानादिकों थ्रप्तों नोपक्राराब जायते। ज्ञानैकऋपभुताथ निर्धुततमसे नमः।
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1970)
- **Original**: तावद्‌ यावन्न संयोगि जगदेतत्‌ त्वदंशुभि:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1971)
- **Original**: शुक्धज्योतिःस्त्ररूपाय.. विशुद्धाचामलात्पने
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1972)
- **Original**: भ्रगव]! आप हो यह सम्पूर्ण जगत हैं। वरिष्ठाय वरश्याय परस्से परमात्मने। आपमें हो चराचर प्राणियोंसहित समस्त अह्यापण्ड नपो5खिलजगदल्वापिस्वरूपायात्मपूर्तये. #
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1973)
- **Original**: ओत्रप्रोत है; अतएब उम्र्थलोकमें जब आप जकारणभूताथ निष्ठाय._ ज्ञानचेतसाम्‌
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1974)
- **Original**: भ्रमण करते हैं तो आपके साथ पह बद्माग्ड भी नमः सूर्बस्वकृपाव प्रकाशात्मस्वरूपिणे
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1975)
- **Original**: घुमता है। आपको क्रिरणोंका स्पर्श पाकर डी भ्रास्कराय नमस्तुभ्य॑ तथा दिनकृत्ते नमः।
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1976)
- **Original**: सम्भूण बस्‍्तुएँ पॉवेज होती हैं। आपका किरणें हो शर्वरीहेतते चैव संथ्याज्योत्स्राकृते नमः
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1977)
- **Original**: अपने स्पर्शशे जल आदिकों गबित्र करती हैं। देवता बोले-- भगवन्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1978)
- **Original**: ऋषेदस्वरूप अ।पको। जबतक इस जगतूमें आपकों दिव्य रश्मिवॉका समस्कार हैं। स्ामवेदरूप आपको प्रणाम है।
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1979)
- **Original**: संयोग नहीं होता, तक्तरू होम-ठान आदि धर्म थजुर्तेदस्वरूप आपको नमस्कार है। आए हों सफल नहीं हो पाता। सँमम्त सामौके अधिष्ठान हैं, आपको प्रणाम है। । ऋचस्ते सकला होता यजुंष्येतानि चान्यत:। आप शानके एकमात्र आधार एवं अनछकारका! सकलानि ज्ञ साथानि निफ्तन्ति त्वदड्डतः
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1980)
- **Original**: नाश ऋरनेठाले हैं, आपको +भस्कार है। आपका. ऋद्सयस्त्थ जगन्नाथ त्वमेंव क्ञ चजुर्पयः। स्वरूप शुद्ध ज्योतिर्मव है। आप स्वभावसे ही
- **Translation**: 

---

