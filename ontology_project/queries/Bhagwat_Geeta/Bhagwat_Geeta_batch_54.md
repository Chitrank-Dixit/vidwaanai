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

### Verse 1 (Bhagwat_Geeta 14.1244)
- **Original**: रजो रागात्मकं विदिद्वि तृष्णासड्भगसमुद्धवम्‌। तन्निबध्नाति कौन्तेय कर्मसड्रेन देहिनम्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 14.1245)
- **Original**: हे अर्जुन! रागरूप रजोगुणको कामना और आससक्तिसे उत्पन्न जान । वह इस जीवात्माको कर्मोके और उनके फलके सम्बन्धसे बाँधता है
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 14.1246)
- **Original**: तमस्त्वज्ञानजं विद्द्धि मोहनं सर्वदेहिनाम्‌। प्रमादालस्यनिद्राभिस्तन्निबध्नाति भारत
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 14.1247)
- **Original**: हे अर्जुन! सब देहाभिमानियोंको मोहित करनेवाले
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 14.1248)
- **Original**: * अध्याय 14* 183 तमोगुणको तो अज्ञानसे उत्पन्न जान। वह इस जीवात्माको प्रमाद', आलस्य' और निद्राके द्वारा बाँधता है
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 14.1249)
- **Original**: सत्त्वं सुखे सञ्लयति रज: कर्मणि भारत। ज्ञानमावृत्य तु तमः प्रमादे सम्जयत्युत
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 14.1250)
- **Original**: हे अर्जुन! सत्त्वगगुण सुखमें लगाता है और रजोगुण कर्ममें तथा तमोगुण तो ज्ञानको ढककर प्रमादमें भी लगाता है
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 14.1251)
- **Original**: रजस्तमश्लाभिभूय सत्त्वं भवति भारत। रजः सत्त्वं तमश्लेव तमः सत्त्वं रजस्तथा
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 14.1252)
- **Original**: हे अर्जुन! रजोगुण और तमोगुणको दबाकर सत्त्वगुण, सत्तगगुण और तमोगुणको दबाकर रजोगुण, वैसे ही सत्त्तगुण और रजोगुणको दबाकर तमोगुण होता है अर्थात्‌ बढ़ता है
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 14.1253)
- **Original**: सर्वद्वारेषु देहेउस्मिन्प्रकाश उपजायते। ज्ञानं यदा तदा विद्याद्विवृद्धं सत्त्वमित्युत
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 14.1254)
- **Original**: जिस समय इस देहमें तथा अन्तःकरण और इद्द्रियोमें चेतनता और विवेकशक्ति उत्पन्न होती है, उस समय 1. इन्द्रियों और अन्त:करणकी व्यर्थ चेष्टाओंका नाम 'प्रमाद' है। 2. कर्तव्य-कर्ममें अप्रवृत्तिरूप निरुद्यमताका नाम 'आलस्य' है।
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 14.1255)
- **Original**: 184 * श्रीमद्धगवद्रीता * ऐसा जानना चाहिये कि सत्त्वगुण बढ़ा है
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 14.1256)
- **Original**: लोभ: प्रवृत्तिरारम्भ: कर्मणामशम: स्पृहा। रजस्येतानि जायन्ते विवृद्धे भरतर्षभ
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 14.1257)
- **Original**: हे अर्जुन! रजोगुणके बढ़नेपर लोभ, प्रवृत्ति, स्वार्थबुद्धिसि कर्मोका सकामभावसे आरम्भ, अशान्ति और विषयभोगोंकी लालसा-ये सब उत्पन्न होते हैं
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 14.1258)
- **Original**: अप्रकाशो5प्रवृत्तिश्च॒ प्रमादो मोह एव च। तमस्थेतानि जायन्ते विवृद्धे कुरुनन्दन
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 14.1259)
- **Original**: हे अर्जुन! तमोगुणके बढ़नेपर अन्त:करण और इन्द्रियोंमें अप्रकाश, कर्तव्य-कर्मोमें अप्रवृत्ति और प्रमाद अर्थात्‌ व्यर्थ चेष्टा और निद्रादि अन्त:करणकी मोहिनी वृत्तियाँ--ये सब ही उत्पन्न होते हैं
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 14.1260)
- **Original**: यदा सत्त्वे प्रवृद्धे तु प्रलयं याति देहभूत्‌ । तदोत्तमविदां लोकानमलान्प्रतिपद्यते
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 14.1261)
- **Original**: जब यह मनुष्य सत्त्वगुणकी वृद्धिमें मृत्युको प्राप्त होता है, तब तो उत्तम कर्म करनेवालोंके निर्मल दिव्य स्वर्गादि लोकोंको प्राप्त होता है
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 14.1262)
- **Original**: रजसि प्रलयं गत्वा कर्मसड्रिषु जायते। तथा प्रलीनस्तमसि मूढयोनिषु जायते
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 14.1263)
- **Original**: * अध्याय 14* 185 रजोगुणके बढ़नेपर मृत्युको प्राप्त होकर कर्मोंकी आसक्तिवाले मनुष्योंमें उत्पन्न होता है; तथा तमोगुणके बढ़नेपर मरा हुआ मनुष्य कीट, पशु आदि मूढ़योनियोंमें उत्पन्न होता है
- **Translation**: 

---

