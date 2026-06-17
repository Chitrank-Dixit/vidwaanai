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

### Verse 1 (Vishnu Puran 0.3401)
- **Original**: 15 मदाघूर्णितनेत्रोससौ यः सदैवैककुण्डल: । किरीटी ख्रग्धरों भाति साप्रि: श्वेत इवाचल:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3402)
- **Original**: 16 नीलबासा मदोत्सिक्त: श्वेतहारोपशोभित: । साभ्रगड्जरपप्रबाहोइसो कैलासाद्रिरिवापरः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3403)
- **Original**: 17 लाडुलासक्तहस्ताओ बिश्रन्पुसलमुत्तमम्‌ । उपास्यते स्वयं कान्त्या यो वारुण्या च मूर्तया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3404)
- **Original**: 18 कल्पान्ते यस्य वक्त्रेभ्यो विधानलशिखोज्ज्वल: । स्डूर्षणात्मको रुद्गो निष्क्रम्यात्ति जगल्नयम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3405)
- **Original**: 19 स बिप्रच्छेखरीभूतमशेषं क्षितिमण्डलम्‌। आस्ते पातालमूलस्थ: झेषो5शेषसुराचित:ः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3406)
- **Original**: 20 तस्य वीर्य प्रभावश्च स्वरूप रूपमेव च। न हि वर्णवितु शक्य॑ ज्ञातुं च त्रिदशैरपि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3407)
- **Original**: 21 यस्यैषा सकल पृथ्वी फणामणिशिखारुणा । आस्ते कुसुममालेव कस्तद्वीय॑ बदिष्यति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3408)
- **Original**: 22 द्वितीय अंश 121 उस पातालकों किसके समान कहें ?
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3409)
- **Original**: जहाँ-तहाँ दैत्य और दानबोंक्त्रे कन्वाओंसे सुशोभित पाताललोकमें किस मुक्त पुरुषकी भी प्रीति न होगी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3410)
- **Original**: जहाँ दिनमें सूर्यकी किरणें केखल प्रकाद ही करती हैं, घाम नहीं करतीं; तथा यातमें चन्द्रमाकी किरणोंसे शीत नहीं होता, केवल चाँदनी ही फैलती है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3411)
- **Original**: जहाँ भक्ष्य, भोज्य और महापानादिके भोगॉसे आनन्दित सर्पों तथा दानवादिकोंको समय जाता हुआ भी प्रतीत नहीं होता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3412)
- **Original**: जहाँ सुन्दर वन, नदियाँ, रमणीय सरोखर और कमलोंके वन हैं, जहाँ नरकोकिस्मेंकी सुमधुर कूक गूँजती है एवं आकादा मनोहारी है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3413)
- **Original**: और हे द्विज ! जहाँ पातालनिवासो दैत्य, दानत्र एजे नागगणद्वारा अति स्वच्छ आधूषण, सुगन्धमय अनुल्ेपन, वीणा, वेणु और पृदंगादिके स्वर तथा तूर्य--ये सब एवं भाग्यशालियोंके भोगनेयोग्य और श्री अनेक भोग भोगे जाते है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3414)
- **Original**: पातालॉंके नीचे लिष्णुभगवानका कोष नामक जो तमोमय विप्रह है उसके गुणोंका दैत्य अधत्रा दानवगण भी वर्णन गहीं कर सकते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3415)
- **Original**: जिन देयर्चिपुजित देखका सिद्धगण “अनन्त' कहकर बखान करते हैं ते अति निर्मल, स्पष्ट स्वस्तिक चिह्लोंसि विधुषित तथा सहस्तर सिस्वाले हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3416)
- **Original**: जओ अपने फर्णोकी सहस्तर मणियॉसे सम्पूर्ण दिज्ञाओंको देदीप्यमान करते हुए संसारके कल्याणफे लिये समस्त असुरोंको वोयंहोन करते रहते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3417)
- **Original**: सदके कारण अरुणनयन, सदैव एक ही कुण्डल पहने हुए तथा मुकुट और माल्
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3418)
- **Original**: आदि धारण किये जो अग्रियुक्त श्वेत पर्वतके समान सुशोधित हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3419)
- **Original**: मदसे उन्मत्त हुए जो नीलाम्बर तथा श्वेत हारोसे सुशोभित होकर मेघ्रमाला और ग॑गाप्रवाहसे युक्त दूसरे कैलास-पर्यतके समान विराजमान हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3420)
- **Original**: जो अपने हाथोंमें हल और उत्तम मूसल धारण किये हैं तथा जिनकी उपासना शोभा और वारुणी देवी स्वये मूर्तिमती होकर करती हैं
- **Translation**: 

---

