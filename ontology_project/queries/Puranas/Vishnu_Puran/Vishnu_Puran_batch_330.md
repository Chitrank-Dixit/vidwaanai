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

### Verse 1 (Vishnu Puran 0.6581)
- **Original**: इस प्रकार जलमें स्थित सौभारे ऋषिने एकाग्रतारूप समाधिको छोड़कर यत-दिन ठस मत्स्यरजकी अपने पुत्र, पौत्र और दौहित्र आदिके साथ अति रमणीय क्रीडा ऑको देखकर विचार किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6582)
- **Original**: 'अह्ो ! यह अन्य है, जो ऐसी अनिष्ट योनिमें उत्पन्न होकर भी अपने इन पुत्र, पौत्र और दौहित्र आदिके साथ निरन्तर रमण करता हुआ हमारे हृदयमें डाह उत्पन्र करता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6583)
- **Original**: 238 श्रीविष्णुपुराण [ #0 2 वयमप्येव॑ पुत्रादिभिस्सह ललित रंस्थामहे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6584)
- **Original**: हम भी इसी प्रकार अपने पुत्रादिके साथ अति इत्येबमभिकाज्नन्‌ स॒ तस्मादन्तर्जलान्निष्क्रम्य
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6585)
- **Original**: ललित क्रीडाएँ करेंगे।' ऐसी अभिलत्रपा करतेहुए राजानमगच्छत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6586)
- **Original**: ये उस जलके भीतरसे निकल आये और सस्तानार्थ गहस्थाश्रममें प्रवेश कसनेकी कामनासे कन्या अहण आगमनश्रवणसमनतन्तर॑ चोत्थाय तेन राज्ञा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6587)
- **Original**: करेके लिये राजा मान्धाताके पास आये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6588)
- **Original**: सम्यगर्घ्यादिना सम्पूजित: कृतासनपरिग्रहः सौभरिरुवाच राजानम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6589)
- **Original**: कि ल्वर्थिनामर्थितदानदीक्षा कृतक्रत॑ इल्लाध्यमिदं कुलं ते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6590)
- **Original**: 78 अझतार्थसंख्यास्तव सन्ति कन्या- स्तासां ममैकां नृपते प्रयच्छ। यत्यार्थनाभड्रभयाद्विभेमि तस्मादर्ह॑ राजवरातिदुःखात्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6591)
- **Original**: 79 अ्रीपप्शर उवाच इति ऋषिवचनमाकर्ण्य स राजा जराजर्जरित- देहमृषिमास्थेक्य. प्रत्याख्यानकातरस्तस्माश्च शापभीतो बिभ्यत्किक्षिदधोमुखश्मिर॑ दक्यो चा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6592)
- **Original**: सौभरिरिवाच नरेन्द्र कस्मात्समुपैषि चिन्ता- कृतार्थता नो यदि कि न लब्धा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6593)
- **Original**: 81 औपरारार उसाच मुनिवक्का आगमन सुन राजने उठकर अर्ध्यदानादिसे उनका भली प्रकार पूजन किया। तदनन्तर सौभरे मुनिनें आसन ग्रहण करके गजासे कहा--
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6594)
- **Original**: सौभरिजी बोले--हे राजन्‌ ! मैं कन्या-परिग्रहका अभिल्मपी हूँ, अतः तुम मुझे एक कन्या दो; मेरा प्रणय भक्न मत करो। ककुत्स्थवैद्यमें कार्यवज्ष आया हुआ कोई भी प्रार्थी पुर्ष कभी खाली हाथ नहीं स्तैटता
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6595)
- **Original**: हे मान्धाता ! पृथिवीतलमें और भी अनेक याचक्लोंको माँगी हुई वस्तु दान देनेके नियममें दृढप्रतिज्ञ तो यह तुम्हारा प्रशोसनीय कुल ही है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6596)
- **Original**: हे ग़जन्‌ ! तुम्हारे पचास कनन्‍्याएँ हैं, उनमेंसे तुम मुझे केवल एक हो दे दो। हे नृपश्रेष्ठ ! मैं इस समय प्रार्थाभड्रकी आशफ्टुसे उत्पन्न अतिशय - दुःखसे भयभीत हो रहा हूँ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6597)
- **Original**: श्रीपरादारजी बोछे--ऋषिके ऐसे वचन सुनकर राजा उनके जराजीर्ण देहको देखकर शापके भयसे अस्वीकार करनेमें कातर हो उनसे डरते हुए कुछ नीचेको सुख करके मन-ही-मन चित्ता करने लगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6598)
- **Original**: सौभरिजी खोले--हे नरेन्द्र ! तुम चिन्तित क्यों होते हो ? मैंने इसमें कोई असहा आत तो कही नहीं है; जो कन्या एक दिन तुम्हें अवश्य देनो ही है उससे ही यदि हम कुतार्थ हो रूकें तो तुम क्या नहीं प्राप्त कर सकते हो ?
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6599)
- **Original**: श्रीपराशरजी बोले--तब भगवान्‌ सौभरिके अथ तस्य भगवतइशापभीतस्सप्रश्नयस्तमुवा-
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6600)
- **Original**: शापसे भयभीत हो राजा मान्खाताने नम्नतापूर्वक उनसे चासौ राजा
- **Translation**: 

---

