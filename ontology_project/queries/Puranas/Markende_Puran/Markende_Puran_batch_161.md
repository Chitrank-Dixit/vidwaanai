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

### Verse 1 (Markende Puran 0.3201)
- **Original**: शुम्भमुक्ताज्छान्देती शुम्भस्तत्प्रहिताजछरान्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3202)
- **Original**: चिच्छेद स्वशॉररूग्रैं! श़तशो5थ स्रहस्त्रश)
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3203)
- **Original**: ज्ञतः सा चणिडका क़ुद्धा शूलेनाभिजधान तम्‌। सत्र त्दाधिहृतों भूझो मूर्किछतों निपपात ह
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3204)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3205)
- **Original**: राजन्‌ ! युद्धमें रक्तबौज तथा अन्य दैत्वोंक्ते मारे जानेपर शुम्भ और निशुम्भके क्रोधकी सीमा न रहीं
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3206)
- **Original**: अपनी विशाल सेना इस प्रछार मारी जातो देख निशुम्भ अमर्पमें भरकर देवोकी ओर दौड़ा। उसके साथ असुरोंकी प्रधान सेना थी
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3207)
- **Original**: उसके आगे, पीछे तथा याश्चभागर्मे बड़े-बड़े असुर थे, जो क्रोधले ओंठ चबाते हुए देवीको पार डालनेके लिये आये
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3208)
- **Original**: महापराक्रमी शुम्भ भी अपनी सेनाके साथ मात्ताणोंसे बुद्ध करके क्रोधवश चश्डिकाकों मारनेके लिये आ पहुँचा
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3209)
- **Original**: तब देवीके साथ शुम्भ और
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3210)
- **Original**: निशुल्भका घोर संग्राम छिड़ गया। जे दोतों दैत्य मेघोंकों भाँति बाणोंकी भयंकर चरृष्ठि कर रहे थ्रे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3211)
- **Original**: ठन दोनोंके चलाये हुए बाणोंको चण्डिकाने अपने बाणोंके समूहसे तुरंत काट डाला और शस्त्रसमृहोंकों वर्षा कूस्के उन दोनों दैत्यपतियोंकि अश्लोंगें भी चोर पहुँचायी
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3212)
- **Original**: निशुप्थने तीखों तलवार और बमकतों हुई ढाल लेकर देबीके श्रेष्ठ बहन सिंहके मम्तकपर प्रहार किया
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3213)
- **Original**: बाणसे निशुम्भक्ी श्रेष्ठ तलवार तुरंत ही काट डाली और उसकी ढालकों भी, जिसमें आठ चाँद जड़े थे, खण्ड-खण्ड कर दिवा
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3214)
- **Original**: ढाल और तलवारके कट जानेपर उस असुरने शक्ति चलायी, किंतु सामने आनेपर देवीने चक्रसे उसके भी दो दडुकड़े कर दिये
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3215)
- **Original**: अब तो निशुम्ध क्रोधसे जल उठा और उस दानबने देवीको मारनेके लिये शूल उठाया; किंतु चैज्ोने समीप आनेपर उसे भी मुक्केसे मारकर चूर्ण कर दिया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3216)
- **Original**: तब उसने गदा श्रुपाकर चण्डीके ऊपर चलायी, परंतु बह भा देवीके त्रिशुलसे क्रटकर भस््स हो गयी
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3217)
- **Original**: तदनन्तर दँत्यगाज निशुम्भकों फरसा हाथमें लेकर आते देख देखीने बाणसमूहोंसे ध्रॉयलकर धरतीपर डुला दिया
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3218)
- **Original**: डस भयंकर पराक्रमी भाई निशुम्भके धराशायी हो जानेपर शुघ्पक्तों बड़ा क्रोध हुआ और अम्बिकाका बध करनेके लिये बह आगे बला
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3219)
- **Original**: रथपर बले-बैठे ही 3त्तम
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3220)
- **Original**: # निशुष्ष-चथध * आवुधोंसे सुशोभित अपनी बड़ी-बड़ी आठ अनुपप भुजाओंसे समूचे आकाशको ठककर नह अद्भुत शोभा पाने लगा
- **Translation**: 

---

