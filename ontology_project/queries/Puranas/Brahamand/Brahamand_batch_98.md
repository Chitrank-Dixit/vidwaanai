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

### Verse 1 (Brahamand 0.1941)
- **Original**: 46 यसिष्ठ उवाच-- इति तद्वचन श्रुत्वा' धृत्तिमालंब्य रेणुका । तद्वाक्यगो रवाद्धव मवापुस्तनयाश्र ते'
- **Translation**: 

---

### Verse 2 (Brahamand 0.1942)
- **Original**: 47 _ततो नीत्वा पितुर्देहमाश्रमाभ्यंतरं सुने: । शाययित्वा निवांते तु परितः समुपाविशन्‌
- **Translation**: 

---

### Verse 3 (Brahamand 0.1943)
- **Original**: 48 : तैषां तक्रोपविष्टानामग्रहशत्मचेतसाम्‌-। निमत्ताति शुभान्यासन्ननेकानि महांतिः व
- **Translation**: 

---

### Verse 4 (Brahamand 0.1944)
- **Original**: 4& - है रेणुके
- **Translation**: 

---

### Verse 5 (Brahamand 0.1945)
- **Original**: परम सावधान होकर अपने पुत्रों के सहित मेरी वाणी का श्रवण करो । है भव्रे
- **Translation**: 

---

### Verse 6 (Brahamand 0.1946)
- **Original**: तुम साहस मंत करो । मैं आपका प्रिंयः वचन कहूँगो ।43
- **Translation**: 

---

### Verse 7 (Brahamand 0.1947)
- **Original**: अपनी आत्मा के हित की अभिलाषों रखने-वाले' किसी को भी साहस कभी नहीं करना चाहिए'। आपको नहीं “मरना चाहिए क्योंकि जो प्राणी जीवित रहता: है वह्‌:शुभ कर्मों को देखा करता है
- **Translation**: 

---

### Verse 8 (Brahamand 0.1948)
- **Original**: 44 इसलिए आप घेंये' के घन बाली होकर काल की प्रतीक्षा की आकाडूक्षा वाली होओ । - है शुशिःस्मित वाली: ! भले ही कुछ ही तिमित्त को अन्तरित बनाकर ऐसा करो-345
- **Translation**: 

---

### Verse 9 (Brahamand 0.1949)
- **Original**: :बहुत ही स्वल्प समय में आपके भत्ता सचेतन हो जाँय॑ंगे अर्थात्त जीवित: हो जैयमे पर हे!शोभने
- **Translation**: 

---

### Verse 10 (Brahamand 0.1950)
- **Original**: ःजक उनमें जीवन सपत्पनाहो: जायग्रेएलो' आपकी/कांमना पूर्णतया प्रपप्त
- **Translation**: 

---

### Verse 11 (Brahamand 0.1951)
- **Original**: हो जायमी आर फिर विशेष अधिककाल परयंग्तः अनेक॑ कल्याणों की-भाजन होने! वाली? होंगी. ।46। वर्सिष्ठा जी ने केहेः3 इस प्रकार के उसःअन्तरिकवाणी
- **Translation**: 

---

### Verse 12 (Brahamand 0.1952)
- **Original**: के वर्सत का। अंवणः केस्केः रेणुका:ने धैयेः
- **Translation**: 

---

### Verse 13 (Brahamand 0.1953)
- **Original**: परशुराम,की-प्रतिज्ञा
- **Translation**: 

---

### Verse 14 (Brahamand 0.1954)
- **Original**: & [ 233 का आलम्बन ग्रहण किया था । और उसके जो पुत्र थे उन्होंने. भी उसके बचनों के गौरव से परम प्रसन्नता प्राप्त की थी ।47। इसके पश्चात्‌ उन्होंने उस मुनि अपने पिता के मृत शरीर को आश्रम को भीतर ले जाकर रख दिया था और -उसको बहाँ लिटाकर..निवात में वे उसके चारों ओर बैठ गये थे
- **Translation**: 

---

### Verse 15 (Brahamand 0.1955)
- **Original**: 48।:जिस समय में थे वहाँ पर बहुत ही खिन्‍न आत्मा और - मंचों वाले बठे हुए थे-तो उस बेला में उनको बहुत से परम शुभ एवं-महान्‌ निर्मित्त हुए थे । अच्छे शकुन दिखाई -दिये थे
- **Translation**: 

---

### Verse 16 (Brahamand 0.1956)
- **Original**: तेनःतेर्शकचिदाश्वस्तचेतसो सुनिपु गंवा: । निर्षेदुः सहिता भाँत्रा कांक्षंतों जीवित पिंतु:
- **Translation**: 

---

### Verse 17 (Brahamand 0.1957)
- **Original**: 50 एतंस्मिन्तंतरे राजस्भृग्रुवंशधरो सुनि: । - विश्लेबलेन मलिमांस्तत्रागछछहरुछया
- **Translation**: 

---

### Verse 18 (Brahamand 0.1958)
- **Original**: 5 1 अथवेणां विधिः साक्षाह्वेदवेदांगरपा रग: । सर्वंशास्त्रा्थ वित्प्राज्न: सकलासुरवंदित:
- **Translation**: 

---

### Verse 19 (Brahamand 0.1959)
- **Original**: ।52 मृतसंजीविनी विद्या यो वेद मुनिदुर्लेभास्‌ । यथाहतान्मृतान्देब रुस्थापयति दानवाच्‌
- **Translation**: 

---

### Verse 20 (Brahamand 0.1960)
- **Original**: 53 शास्त्रमौशनस येन रोज्ञों राज्यफलप्रदम्‌ । प्रणीतमनुजीवंति सर्वेब्यापीह 'पाथिवा: 4454 स तदाश्नममासाद प्रविष्टोंउतमेहामुनि: । ददर्श 'तंदवस्थांस्तान्सर्वान्दु:खंप्ररिप्लुतात्‌
- **Translation**: 

---

