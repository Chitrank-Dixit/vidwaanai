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

### Verse 1 (Vaivtpuran 543.17234)
- **Original**: राधे! सौ वर्षके बाद तुम श्रीदामाके शापसे मुक्त * ये त्वां निन्दन्ति मद्धक्तास्त्वदूभकाश्रापि मामपि। कुम्भीपके च पच्यन्ते यावच्द्धदिवाकरौ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17235)
- **Original**: राधामाधवयोर्भेदं ये कुर्वन्ति. नराधमा: । वंशहानिर्धवेत्रेषां. पच्यन्ते नरके. चिरम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17236)
- **Original**: 44-45)
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17237)
- **Original**: + श्रीकृष्णजन्मखण्ड + 763 कक अं अं 44554 59548 95556 % 48% 95% 85% ### ####%##% ## 55% कक हुई हो; अत: आज मेरे वरदानसे तुम श्रीकृष्णके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17238)
- **Original**: चम्पावतीने चम्पाके सुन्दर पुष्पको चन्दनसे साथ मिलो। सुन्दरि! मेरी दुर्लभ आज्ञा मानकर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17239)
- **Original**: अनुलिप्त करके श्रीकृष्णके लिये दोनेमें सजाकर तुम अपना उत्तम श्रृड्ञार करो। रखा। फिर उसने श्रीकृष्णकी प्रसन्नताके लिये तब पार्वतीकी आज्ञासे प्यारा सखियाँ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17240)
- **Original**: केलि-कदम्बोंका पुष्प, मनोहर स्तवक (गुलदस्ता) राधाका श्रृड्ार करनेमें जुट गयीं। उन्होंने ईश्वरी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17241)
- **Original**: और कदम्ब-पुष्पोंकी माला तैयार की। कृष्णप्रियाने राधाको रमणीय रत्लसिंहासनपर बैठाया। फिर तो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17242)
- **Original**: श्रीकृष्णके लिये कपूर आदिसे सुवासित श्रेष्ठ एवं सखी रत्नमालाने सामनेसे आकर राधाके गलेमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17243)
- **Original**: रुचिर पान तथा सुगन्धित जल उपस्थित किया। रलोंकी माला पहना दी और उनके दाहिने हाथमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17244)
- **Original**: इसी समय देवताओं तथा मुनियोंने देखा कि जल- मनोहर क्रीड़ा-कमल रख दिया। पद्ममुखीने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17245)
- **Original**: स्थलसहित सारा आश्रम गोरोचनके समान उद्भासित उनके दोनों चरणकमलोंको महावरसे सुशोभित
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17246)
- **Original**: हो रहा है। उस समय तीनों लोकोंमें वास किया। सुन्दरी गोपीने चन्दनयुक्त सिन्दूरकी परम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17247)
- **Original**: करनेवाले सभी लोगोंने राधिकाके दर्शन किये। रुचिर बेंदीसे सीमन्तके अधोभाग--ललाटकों जिनके शरीरकी कान्ति श्वेत चम्पकके सुशोभित किया। सती मालतीने मालतीकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17248)
- **Original**: समान परम मनोहर एवं अनुपम है; जो ऊर्ध्वरिता मालाओंसे विभूषित करके ऐसी मनभावनी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17249)
- **Original**: मुनियोंके भी मनोंको मोहमें डाल देती हैं; जो रमणीय कवरी गूँथकर तैयार की जो मुनियोंके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17250)
- **Original**: सुन्दर केशोंवाली, सुन्दरी, षोडशवर्षीया और भी मनको मोहे लेती थी। फिर कपोलोंपर कस्तूरी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17251)
- **Original**: बटवृक्षेके नीचे मण्डलमें वास करनेवाली हैं; और कुंकुममिश्रित चन्दनसे सुन्दर पत्रभड्ीकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17252)
- **Original**: जिनका मुख करोड़ों चन्द्रमाओंकी छबिको छीने रचना कौ। मालाबतीने राधाको सुन्दर चम्पाके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17253)
- **Original**: लेता है; जो सदा मुस्कराती रहती हैं, जिनके दाँत पुष्पोंकी मनोहर गन्धवाली माला और खिली हुई
- **Translation**: 

---

