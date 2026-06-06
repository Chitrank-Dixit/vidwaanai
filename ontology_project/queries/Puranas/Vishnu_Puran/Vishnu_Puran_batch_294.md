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

### Verse 1 (Vishnu Puran 0.5861)
- **Original**: 33 पिता पितामहशैव तथैब प्रपितामह: । तृप्तिं प्रयान्तु पिण्डेन मया दत्तेन भूतले
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5862)
- **Original**: 34 पिता पितामहक्षेव तथैव प्रफ्तिमह: । मृप्ति प्रयान्तु मे भक्‍त्या मयैतत्समुदाह्तम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5863)
- **Original**: 35 मातामहस्तृप्तिपुपतु..:$> तस्य तथा पिता तस्य पिता ततोउनन्‍्य: । विश्वे च देवा: परमां प्रयान्तु तृप्ति प्रणश्यन्तु च यातुधाना:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5864)
- **Original**: 36 यज्ञेधोरों हव्यसमस्तकव्य- भोक्ताव्ययात्मा हरिरीश्वरोउत्र । + *3% अ पहता असुरा रक्षा* सि वेदिषद' इस्यादि । रूपसे आ जाय तो निमन्लित ब्राह्मणोंकी आज्ञासे उसे भी यथेच्छ भोजन कराबे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5865)
- **Original**: अनेक अज्ञात-स्वरूप योगिगण मनुष्योंके कल्याणकी क्यममनासे नाना रूप धारणकर पृथिबीतलपर विचरते रहते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5866)
- **Original**: अतः विज्ञ पुरुष श्राद्धकारूमें आये हुए अतिथिका अवश्य सत्कार करे। हे नरेन्द्र ! उस समय अतिधिका सत्कार न करनेसे वह श्राद्ध-क्रियाके सम्पूर्ण फ़लूको नष्ट कर देता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5867)
- **Original**: हे पुरुषश्रेष्त ! तदनत्तर उन ब्राह्मणोंकी आज्ञासे दाक और लवणहीन अन्नसे अप्रिमें तीन बार आहुति दे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5868)
- **Original**: हे राजन्‌ ! उममेंसे 'अम्रये कख्यजाइनाय स्वाहा' इससे दूसरी और “वैवस्व॒ताय स्वाहा' इस मन्नसे तीसरी आहति दे । तदनन्तर आहततियोंसे बचे हुए अन्नको थोड़ा- थोड़ा सब त्राह्मणोंके पात्रोंमें परोस दे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5869)
- **Original**: फिर रुचिके अनुकूल अति संस्कारयुक्त मधुर अन्न सबफो परोसे और अति मृदुल वाणीसे कहे कि "आप भोजन कीजिये'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5870)
- **Original**: ब्राह्मणोंको भी तद्तचित्त और मौन होकर प्रसन्नमुस्तसे सुखपूर्वक भोजन करना चाहिये तथा यजमानको क्रोध और उताबलेपनको छोड़कर भक्तिपूर्वक. परोसते रहना चाहिये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5871)
- **Original**: फिर 'रक्षोघ्र'* मन्ज़का पाठ कर श्राद्धभूमिपर तिल छिड़के, तथा अपने पितृरूपसे उन टद्विजश्रेष्ठोकत्र ही चिन्तन करें
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5872)
- **Original**: ( और कहे कि ] 'इन ब्राक्मणोके शरीरोंमें स्थित मेरे पिता, पितामह और प्रपितामह आदि आज तृप्ति स््रभ करें
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5873)
- **Original**: होमद्वारा सबल होकर मेरे पिता, पितामह् और प्रपितामह आज तृप्ति ल्मरभ करें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5874)
- **Original**: मैने जो पृथिवीपर पिण्डदान किया है उससे मेरे पिता, पितामद्द और प्रपितामह तृप्ति लव करें
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5875)
- **Original**: श्राद्धलूपसे कुछ भी निवेदन न कर सकनेके कारण ] पैंने भक्तिपूर्वकक जो कुछ कहा है उस मेरे भक्ति- भावसे हो मेरे पिता, पितामह और अपितामह तृप्ति लाभ करें
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5876)
- **Original**: मेरे मातामह (नाना), उनके पिता और उनके भी पिता तथा विश्वेदेवगण परम तृप्ति ल्थाभ करें तथा समस्त राक्षसगण नष्ट हों
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5877)
- **Original**: यहाँ समस्त हव्यकव्यके भोक्ता यज्ञेशर भगवान्‌ हरि विराजमान हैं,
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5878)
- **Original**: 212 तत्सप्निधानादपयान्तु. सद्यो रक्षांस्यशेषाण्यसुराक्ष. सर्वे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5879)
- **Original**: 37 सृप्तेष्नेतेषु विकिरेदन्न॑ विप्रेषु भूतले । दष्यादाचमनार्थाय तेभ्यो वारि सकृत्सकृत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5880)
- **Original**: 38 सुतृप्तैस्तैरनुज्ञातस्सर्वेणान्नेन भूतले । सतिलेन तत: पिण्डान्सम्यग्द्यात्समाहित:
- **Translation**: 

---

