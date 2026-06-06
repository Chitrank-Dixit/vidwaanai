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

### Verse 1 (Bramha 0.5361)
- **Original**: उनका प्रभाव अत्यन्त महान्‌ है। नारद! किसमें गौतमेश्वरके नामसे विख्यात हैं। लक्ष्मीसहित भगवान्‌
- **Translation**: 

---

### Verse 2 (Bramha 0.5362)
- **Original**: इतनी शक्ति है, जो गोदावरीकी महिमाका पूरा- विष्णु भी वहाँ नित्य निवास करते हैं। मैंने जो
- **Translation**: 

---

### Verse 3 (Bramha 0.5363)
- **Original**: पूरा बर्णन कर सके। जो भक्तिपूर्वक उनके वहाँ शिवकी स्थापना की है, वह शिवलिड़
- **Translation**: 

---

### Verse 4 (Bramha 0.5364)
- **Original**: गुणगानमें प्रवृत हो यथाकर्थंचित्‌ उनकी महिमाका ब्रह्मेश्वके नामसे प्रसिद्ध है। देबताओंसहित मैंने
- **Translation**: 

---

### Verse 5 (Bramha 0.5365)
- **Original**: दिग्दर्शन कराता है, उसके ऐसा करनेमें निःसंदेह अपने लिये कारण उपस्थित होनेपर सम्पूर्ण कोई अपराध नहीं है; इसलिये मैंने भी लोक- लोकोंके उपकारके लिये भगवान्‌ विष्णुका भी
- **Translation**: 

---

### Verse 6 (Bramha 0.5366)
- **Original**: कल्याणके उद्देश्यसे अत्यन्त प्रयास करके गज्जाके स्तवन किया था। वे विष्णु वहाँ चक्रपाणिके
- **Translation**: 

---

### Verse 7 (Bramha 0.5367)
- **Original**: माहात्म्यको संक्षेपसे सूचित किया है। कौन गोदाबरीके नामसे विख्यात हैं। वहीं ऐन्द्रतीर्थ भी है और
- **Translation**: 

---

### Verse 8 (Bramha 0.5368)
- **Original**: प्रत्येक तीर्थका प्रभाव बता सकता है। कहीं, उसीको हयग्रीवतीर्थ भी कहते हैं। वहाँ सोमतीर्थ
- **Translation**: 

---

### Verse 9 (Bramha 0.5369)
- **Original**: किसी स्थानपर, किसी विशेष समयमें कोई उत्तम भी है, जहाँ भगवान्‌ शिव सोमेश्वरके नामसे
- **Translation**: 

---

### Verse 10 (Bramha 0.5370)
- **Original**: तीर्थ प्रकट होते हैं; परंतु गौतमीमें सर्वत्र और प्रसिद्ध हैं। एक समय इन्द्रने बड़े-बड़े यज्ञोंद्वारा
- **Translation**: 

---

### Verse 11 (Bramha 0.5371)
- **Original**: सदा ही तीर्थोंका वास है। वे मनुष्योंके लिये सब मेरी आराधना करके मेरे प्रसादसे अपना मनोरथ
- **Translation**: 

---

### Verse 12 (Bramha 0.5372)
- **Original**: जगह और सब समय पवित्र हैं। उनके गुणोंका सिद्ध किया था। तबसे मैं भी वहाँ सब लोगोंका
- **Translation**: 

---

### Verse 13 (Bramha 0.5373)
- **Original**: वर्णन कौन कर सकता है। उनके लिये तो केबल उपकार करनेके लिये रहता हूँ, विष्णु और शिव
- **Translation**: 

---

### Verse 14 (Bramha 0.5374)
- **Original**: नमस्कार करना ही उचित जान पड़ता है। तो वहाँ हैं ही। अग्निने जहाँ यज्ञ किया, वह स्थान
- **Translation**: 

---

### Verse 15 (Bramha 0.5375)
- **Original**: . नारदजीने कहा--सुरेश्वर! आप गज्जाकों तीनों आग्नेयतीर्थक नामसे प्रसिद्ध है। तदनन्तर
- **Translation**: 

---

### Verse 16 (Bramha 0.5376)
- **Original**: देवताओंसे सम्बन्ध रखनेवाली बताते हैं। ब्रह्मर्षि आदित्यतीर्थ है, जहाँ वेदमय आदित्य प्रतिदिन
- **Translation**: 

---

### Verse 17 (Bramha 0.5377)
- **Original**: गौतमद्गार लायी हुई लोकपावनी गड्भा परम पतित्र मध्याहकालमें दूसरा रूप धारण करके मेरा,
- **Translation**: 

---

### Verse 18 (Bramha 0.5378)
- **Original**: और कल्याणमयी हैं। उनके आदि, मध्य और शिवका तथा विष्णुका दर्शन एवं ठपासना करनेके
- **Translation**: 

---

### Verse 19 (Bramha 0.5379)
- **Original**: अन्तमें दोनों तटोंपर भगवान्‌ विष्णु, शिव तथा आप लिये आते हैं। वहाँ मध्याह्कालमें सब लोग
- **Translation**: 

---

### Verse 20 (Bramha 0.5380)
- **Original**: व्याप्त हैं। उनकी महिमा सुननेसे मुझे तृप्ति नहीं बन्दनीय हैं, क्योंकि न मालूम सूर्य वहाँ किस
- **Translation**: 

---

