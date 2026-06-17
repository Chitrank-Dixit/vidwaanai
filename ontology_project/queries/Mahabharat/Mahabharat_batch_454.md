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

### Verse 1 (Mahabharat 0.4531)
- **Original**: और शूरसेननिवासी यज्ञ करनेवाले होते हैं। पूस्थके स्ेग कहने लगा। वह बोला, “मंद्रराज ! मैं जो बात कहता हूँ उसे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4531)
- **Original**: और शूरसेननिवासी यज्ञ करनेवाले होते हैं। पूस्थके स्ेग कहने लगा। वह बोला, “मंद्रराज ! मैं जो बात कहता हूँ उसे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4532)
- **Original**: दासवृत्ति कस्ते हैं, दक्षिणी ल्लोगोंका बर्ताव झुद्"ेंके समान जरा ध्यान देकर सुनों। इस बातकी चर्चा यैंने महाराज
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4532)
- **Original**: दासवृत्ति कस्ते हैं, दक्षिणी ल्लोगोंका बर्ताव झुद्"ेंके समान जरा ध्यान देकर सुनों। इस बातकी चर्चा यैंने महाराज
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4533)
- **Original**: होता है। वाहीक लोग चोर तथा सौराष्ट्र निवासी वर्णसंकर घृतराष्ट्रके पास सुनी थी। एक बार उनके महलमें कई ब्राह्मण
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4533)
- **Original**: होता है। वाहीक लोग चोर तथा सौराष्ट्र निवासी वर्णसंकर घृतराष्ट्रके पास सुनी थी। एक बार उनके महलमें कई ब्राह्मण
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4534)
- **Original**: होते हैं। मगध देशके मनुष्य इझारेसे ही बात- समझ लेते अनेकों अद्भुत देशों और प्राचीन वृत्तान्तोंका वर्णन कर रहे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4534)
- **Original**: होते हैं। मगध देशके मनुष्य इझारेसे ही बात- समझ लेते अनेकों अद्भुत देशों और प्राचीन वृत्तान्तोंका वर्णन कर रहे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4535)
- **Original**: हैं, कोसलकी प्रजा दृष्टिके संकेतको समझती है, -कुरु थे। वहाँ एक बूढ़े ब्राह्मणने बाहीक और मद्रदेशकी निन्‍दा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4535)
- **Original**: हैं, कोसलकी प्रजा दृष्टिके संकेतको समझती है, -कुरु थे। वहाँ एक बूढ़े ब्राह्मणने बाहीक और मद्रदेशकी निन्‍दा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4536)
- **Original**: और पाम्चालके लोग: आधी बात कह देनेपर पूरी बात समझ करते हुए कहा था--“जो हिमालय, गड्ल, सरस्वती, यमुना
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4536)
- **Original**: और पाम्चालके लोग: आधी बात कह देनेपर पूरी बात समझ करते हुए कहा था--“जो हिमालय, गड्ल, सरस्वती, यमुना
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4537)
- **Original**: पाते हैं तथा झाल्ज देशके निवासी पूरी बात कहनेसे और कुरुक्षेत्रसे बाहर तथा सिश्धु और उसकी पाँच सहायक
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4537)
- **Original**: पाते हैं तथा झाल्ज देशके निवासी पूरी बात कहनेसे और कुरुक्षेत्रसे बाहर तथा सिश्धु और उसकी पाँच सहायक
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4538)
- **Original**: ही उसे हृदयज्ञस करते हैं।- क्षिविदेझकी प्रजा।-पहाड़ी नदियोंके बीचमें स्थित है वह बाहीक देश धर्मबाह्म और
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4538)
- **Original**: ही उसे हृदयज्ञस करते हैं।- क्षिविदेझकी प्रजा।-पहाड़ी नदियोंके बीचमें स्थित है वह बाहीक देश धर्मबाह्म और
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4539)
- **Original**: ल्तेगोंकी तरह मूर्ख होती है। यबन स्थरेग सब बातोंको अपवित्र है। उससे सर्वंदा दूर रहना चाहिये। मैं एक गुप्त
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4539)
- **Original**: ल्तेगोंकी तरह मूर्ख होती है। यबन स्थरेग सब बातोंको अपवित्र है। उससे सर्वंदा दूर रहना चाहिये। मैं एक गुप्त
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4540)
- **Original**: अनायास ही समझ लेते और विशेषत: शूरवीर होते: हैं। कार्यवज्ञ कुछ दिन बाहीक देझमें रहा था। उस समय मैंने
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4540)
- **Original**: अनायास ही समझ लेते और विशेषत: शूरवीर होते: हैं। कार्यवज्ञ कुछ दिन बाहीक देझमें रहा था। उस समय मैंने
- **Translation**: 

---

