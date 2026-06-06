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

### Verse 1 (Vishnu Puran 0.11461)
- **Original**: देख, यह मैंने चक्र छोड़ दिया, यह तेरे ऊपर गदा भी छोड़ दी और सह गरुड भी छोड़े देता हूँ, यह तेरी ध्वजापर आरूढ़ हों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11462)
- **Original**: श्रीपराशरजी खोल्ले-- ऐसा कहकर झोड़े हुए चक्रने पौण्डुकम्त्रे लिटीर्ण कर डाल्त्र, गदाने नीचे गिरा दिया और गरुड़ने उसकी ध्यजा तोड़ डाल्जी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11463)
- **Original**: तदनन्तर सम्पूर्ण सेनामें हाहाकार मच जानेपर अपने मित्रका बदला चुकानेके लिये खड़ा हुआ काशीनरेश श्रीबासुदेवसे लड़ने लूगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11464)
- **Original**: तब भगवानने शार्ई- धनुषसे छोड़े हुए एक बाणसे उसका सिर काटकर सम्पूर्ण त्लेगोंको विस्मित करते हुए काशीपुरीमें फेंक दिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11465)
- **Original**: इस प्रकार पौण्ड्क और काशौनरेशको अनुचरोंसहित मारकर भगवान्‌ फिर द्वारकाको ल्त्रैट आये और बहाँ स्वर्ग-सदूश सुख्तका अनुभव करते हुए रमण करने छगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11466)
- **Original**: इधर काशीपुरीमें काश्चिगजका सिर गिय देख सम्पूर्ण नगरनिवासी बिस्मयपूर्वक कहने छगे--“यह क्‍या हुआ ? इसे किसने काट डाला ?"
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11467)
- **Original**: ड04ड ज्ञात्वा ते बासुदेवेन हत॑ तस्य सुतस्तत: । पुरोहितेन सहितस्तोषयामास शह्भूरम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11468)
- **Original**: 29 वर॑ वृणीष्लेति तदा त॑ प्रोवाच नृपात्मजम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11469)
- **Original**: 30 स बच्रे भगवन्कृत्या पितृहन्तुर्वधाय मे । समुत्तिष्ठत्‌ कृष्णस्थ त्वत्मसादान्महेश्वर
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11470)
- **Original**: 31 अ्रीपताज्र उवाच एवं भविष्यतीत्युक्ते दक्षिणाग्रेरनन्तरम्‌। बे छझ ल्‍जशभ्रीविष्यपुराण ऑऑऑऑऑ##आ रेट _[ आ» कटे जब उसके पुत्रव्त्रे मालूम हुआ कि उसे श्रीवासुदेवने मारा है तो उसने अपने पुरोहितके साथ मिलन्कर भगवान्‌ आकरको सन्तुष्ट किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11471)
- **Original**: अविमुक्त महाक्षेत्रमें उस राजकुमारसे सन्तुष्ट होकर श्रीशंकरने कहा--'वर माँग'
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11472)
- **Original**: वह बोला--''हे भगवन्‌ ! हे महेश्वर !! आपकी कृपासे मेंरे पिताका यध करनेवाले कृष्णका नाश करनेके लिये (अग्निसे) कृत्या उत्पन्न हो”*
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11473)
- **Original**: श्रीपराहरजी बोले--भगवान्‌ शक्लूरने कहा, 'ऐसा ही होगा।' उनके ऐसा कहनेपर दक्षिणाभ्रिका चयन करतेके अनन्तर उससे उस अम्निका ही विनाश करनेवाली महाकृत्या समुत्तस्थौ तस्वैवाभरेविनाशिनी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11474)
- **Original**: कुत्या उत्पन्न हुई
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11475)
- **Original**: उसका करा मुख ततो ज्वालाकरालास्था ज्वलल्केशकपालिका । कृष्ण कृष्णेति कुपिता कृत्या द्वारबर्ती ययो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11476)
- **Original**: 33 तामवेक्ष्य जनस्त्रासादिचिलल्लोचनो सुने । ययौ हारण्यं जगतां शरणं मधुसूदनम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11477)
- **Original**: 34 काशिराजसुतेनेबमाराध्य.. वृषभध्वजम्‌ । उत्पादिता महाकृत्येत्यवगम्याथ चक्रिणा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11478)
- **Original**: 35 तदभ्रिमालाजटिलज्वालो द़्रातिभीषणाम्‌_। कृत्यामनुजगामाश विष्णुचक्र सुदर्शनम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11479)
- **Original**: 37 चक्रप्रतापनिर्दग्धा कृत्या माहेश्वरी तदा। ननाझ बेणिनी वेगात्तदप्यनुजगाम ताम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11480)
- **Original**: 38 कृत्या वाराणसीमेब प्रविवेज्ञ त्वरान्विता । विष्णुचक्रप्रतिहतप्रभावा मुनिसत्तम
- **Translation**: 

---

