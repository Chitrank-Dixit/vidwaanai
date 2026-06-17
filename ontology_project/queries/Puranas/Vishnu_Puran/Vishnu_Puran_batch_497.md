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

### Verse 1 (Vishnu Puran 0.9921)
- **Original**: %एऋषण >ज उदग्रककुदाभोगप्रमाणो.. दुरतिक्रमः । विष्मूत्रस्विप्रपृष्ठाड़ो.. गवामुद्रेगकारक:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9922)
- **Original**: 4 प्रलृम्बकण्ठो5तिमुखस्तरुखाताड्लिताननः । पातयन्स गबां गर्न्दित्यो वृषभरूपधृक्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9923)
- **Original**: 5 सूदयंस्तापसानुग्रों वनानटति वस्सदा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9924)
- **Original**: 6 ततस्तमतिघोराक्षमवेक्ष्यातिभयातुरा:..। गोपा गोपस्तरियश्चैव कृष्ण कृष्णेति चुक्कुशु:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9925)
- **Original**: 7 सिंहनादं ततश्चक्रे तलशब्द च केशव: । तच्छब्दभ्रवणाश्यासो. दामोदरमुपाययो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9926)
- **Original**: 8 अग्नन्यस्तविषाणाग्र: कृष्णकुक्षिकृतेक्षण: । अभ्यधावत दुष्टात्मा कृष्णं वृषभदानव:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9927)
- **Original**: 9 आयानत दैत्यवृषभं दृष्ठा कृष्णो महाबल: । न चच्चाल तदा स्थानादवज्ञास्मितलीलया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9928)
- **Original**: 10 आसन्न॑ चैव जग्राह ग्राहवन्मधुसूदन: । जघान जानुना कुक्षौ विषाणग्रहणाचलम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9929)
- **Original**: 11 तस्य दर्पबलं भड्वत्वा गृहीतस्थ विषाणयो: । अपीडयदरिष्टस्थ कणठे क्लिन्नमिबाम्बरम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9930)
- **Original**: 12 उत्पाट्य श्रूडमेके तु तेनैबाताडयत्तत: । ममार स महादैत्यो मुखाच्छोणितमुद्रमन्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9931)
- **Original**: 13 तुष्ठवुर्निहते तस्मिन्दैत्ये गोपा जनार्दनम्‌। श्रीविष्णुपुराण ___ ( अ* एड रखी थी तथा उसके स्कन्धबन्भन कठोर थे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9932)
- **Original**: उसके ककूद (कुहान) और दारीरका प्रमाण अत्यन्त ऊँचा एवं दुर्लड्घ्य था, पृष्ठणभाग गोबर और मूत्रसे लिधड़ा हुआ था तथा बह समस्त गौओको भयभीत कर रहा था
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9933)
- **Original**: उसकी ग्रीवा अत्यन्त लम्बी और मुख वक्षके स्वॉसख्बलेके समान अति गम्भीर था। वह वृषभरूपथारी दैत्य गौओंके गर्भॉको गियता हुआ और तपस्वियोंक्ों मारता हुआ सदा खनमें खिचरा करता था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9934)
- **Original**: तब उस अति भयानक नेत्रोंवाले दैत्यकों देखकर गोप आऔर गोपाडुनाएँ, भयभीत होकर “कृष्ण, कृष्ण' पुकारने लगीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9935)
- **Original**: उनका शब्द सुनकर श्रीकेशयने घोर सिंहनाद किया और ताली बजायी । उसे सुनते ही वह श्रोदामोदरको ओर फिरा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9936)
- **Original**: दुरात्मा वृषभासुर आगेक्ये सींग कस्के तथा कृष्णचन्द्रकी कुक्षिमें दृष्टि छगाकर उनको ओर दौड़ा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9937)
- **Original**: किन्तु महायली कृष्ण वृषभासुस्को अपनी ओर आता देख अबहेलनासे लील्मपूर्वक मुसकराते हुए. उस स्थानसे विचलित न हुए.
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9938)
- **Original**: निकट आनेपर श्रीमधुसूदनने उसे इस प्रकार पकड़ लिया जैसे याह किसी क्षुद्र जीक्को पकड़ लेता है; तथा सींग पकड़नेसे अचल हुए उस दैत्यकी क्प्रेखमें घुटनेसे प्रहार किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9939)
- **Original**: इस प्रकार सींग पकड़े हुए उस दैत्यकता दर्प भंगकर भगनानने अरिष्टासुस्कों ग्रोवाकों गौले बस््रके सम्नात मरोड़ दिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9940)
- **Original**: तदनत्तर उसका एक सींग उखाइकर उसोसे उसपर आघात किया जिससे वह महादैत्य मुखसे रक्त बमन करता हुआ मर गया
- **Translation**: 

---

