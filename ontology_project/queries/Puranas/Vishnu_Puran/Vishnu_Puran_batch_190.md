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

### Verse 1 (Vishnu Puran 0.3781)
- **Original**: 75 किन ज्युक कु पकमाकप्ण यदा भास्वांस्तदा शाशी । विशाखानां
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3782)
- **Original**: 76 व जद विजन कातन तल स्थन 'यदा तृतीयकम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3783)
- **Original**: तदा चर
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3784)
- **Original**: 77 कर िनुयासथोरल का प्ले मल ये काल:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3785)
- **Original**: तदा दानानि :;
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3786)
- **Original**: 78 सन्त लिए उकपसमन न दानजम्‌ । दत्तदानस्तु क्र कक मस्त
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3787)
- **Original**: 79 अह्लेरात्रार्उ॑मासास्तु कला: काष्ठा: क्षणास्तथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3788)
- **Original**: पौर्णमासी तथा ज्ञेया अमाबास्या तथैव थे । सिनीबाली कुहूक्षेब राका चानुमतिस्तथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3789)
- **Original**: 80 तपस्तपस्थो मधुमाथवों ऋ शुक्र: शुचिश्षायनमुत्तरं स्थात्‌। नभोनभस्या॑ च्॒ इषस्तथोर्ज- प्रकारके वर्ष 'युग' कहलाते हैं यह युग ही [मरूमासादि] सत्र प्रकारके काल-निर्णकका कारण कहा जाता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3790)
- **Original**: उनमें पहला संवत्सर, दूसरा परिवत्सर, तीसरा इद्वत्सर, चौथा अनुवत्सर और पाँचवाँ वत्सर है । यह काल “युग' नामसे बिख्यात है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3791)
- **Original**: श्वेतयर्षके उत्तरमें जो शृड़्वान्‌ नामसे विख्यात पर्वत है उसके तीन भंग हैं, जिनके कारण यह धृड्जजान्‌ कहा जाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3792)
- **Original**: उनमेंसे एक श्रृक्ष उत्तरमें, एक दक्षिणमें तथा एक मध्यमें है। मध्यशृड़ ही 'सैषुबत' है। शरत्‌ और वसनन्‍्तऋतुके मध्यमें सूर्य इस खैषुजतःधृद्भपर आते हैं; अतः हे मैत्रेय ! मेष अथवा तुलाराशिके आरम्भमें तिमिरापहारी सूर्यदेव दिषुवतपर स्थित होकर दिन और रात्रिको समान- परिमाण कर देते हैं। उस समय ये दोनों पत्वह-पन्द्रह मुहूर्तके होते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3793)
- **Original**: '44-75
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3794)
- **Original**: हे मुने ! जिस समय सूर्य कृत्तिकानक्षत्रके प्रथम भाग अर्थात्‌ मेषरादरिके अन्तमें तथा अन्द्रमा निश्चय ही विशास्ताके चतुर्थॉश [ अर्थात्‌ वृश्चिकके आरम्भ ) में हों; अथवा जिस समय सूर्य विशाखाके तृतीय भाग अर्थात्‌ तुछाके अन्तिमौध्ाका भोग करते हों और चन्द्रमा कृत्तिकाके प्रथम भाग अर्धात्‌ मेषान्तमें स्थित जान पड़ें तभी यह 'बिषुब' नामक अति पवित्र काल कहा जाता है; इस समय देवता, ब्राह्मण और पितृगणके उद्देश्यसे संयतचित्त होकर दानादि देने चाहिये। यह समय दानग्रहणके लिये मानो देवताओंके खुले हुए मुखके समान है। अतः 'विषुव' कालमें दान करनेवाला मनुष्य कृतकृत्य हो जाता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3795)
- **Original**: 76---79
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3796)
- **Original**: गरागादिके काल-निर्णयके लिये दिन, रात्रि, पक्ष, कला, काप्ठा और क्षण आदिका विषय भली प्रकार जानना चाहिये। राका और अनुमति डो प्रकारकी पूर्णमासी* तथा सिनीवाली और कुह्दू दो प्रकारकी अमावास्या + होती हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3797)
- **Original**: माघ-फाल्गुन, चैत्र-वैज्ञास्तर तथा ज्येष्ठ-आषाढ़--ये छः मास उत्तरायण होते हैं और श्रावण-भाद, आश्विन-कार्तिक तथा अगहन- स्सहःसहस्याविति दक्षिणं तत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3798)
- **Original**: पौष--ये छः दक्षिणायन कहलाते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3799)
- **Original**: *+ जिस पूर्णिमामें पूर्णचद्ध विराजमान होता है वह 'राका' कहलाती है तथा जिसमें एक कलाहीन होती हैं वह 'अनुमति' कही जाती है + दृष्टचन्द्रा अमावास्थाका नाम 'सिनीयाली' है और नष्टचनद्राका नाम 'कुहू' है।
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3800)
- **Original**: आ08 ] लोकालोकश्न यहदैलः प्रागुक्तो भवतो मया । लोकपालास्तु चत्वारस्तत्न तिष्ठन्ति सुश्रता:
- **Translation**: 

---

