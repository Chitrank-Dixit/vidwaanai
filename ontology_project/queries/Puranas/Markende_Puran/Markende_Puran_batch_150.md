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

### Verse 1 (Markende Puran 0.2981)
- **Original**: अथ मुण्डो5्ध्यथावत्तां दूृष्ठा चण्ज निषातितम्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2982)
- **Original**: तमप्यपातयद्धूमी सा खड्गाभिहतं रूघां
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2983)
- **Original**: हतशेष॑ तत्तः सैन्य दृष्टवा त्षण्ड निपातितम्‌। मुण्ड च सुमहावीर्य दिशो भेजे भ्यातुरम्‌
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2984)
- **Original**: शिरक्षण्डस्थ काली च गुहीत्वा मुण्डपेत्र च। प्राह् प्रचण्डाइड्रासपिअ्रम भ्येत्य चणिडिकाम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2985)
- **Original**: स्श्6् * संक्षिप्त मार्कण्डेअपुराण * $:33304.&#6#& # 7 4 व 56 & 00 लक्ध:उक 64 » + 545464606% 9 0 24:2.6.86 #45 05 2 ऋ 55624 %% 0 3 54:62 2007 , 25324 + फ मया तात्रोपहती चण्डमुण्डों भहापशू।
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2986)
- **Original**: चण्छ मुण्ड नामक महादैत्वोंको देखकर कल्याणमयी चुद्धयज़े स्वयं शुध्भ॑ निशुम्भ च हनिष्यसि
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2987)
- **Original**: चण्डीने कालोसे मधुर वाणीमें कहा-
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2988)
- **Original**: चण्डको मारा गया देख्थ मुण्ड भी देख्ोकी देवि ! तुम चण्ड और पुण्डको लेकर मेरे पास ओर दौड़ा। ज़ब देवोने रोष्में भश्कर उसे भो
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2989)
- **Original**: आयी हो, इसलिये संसारमें चामुण्डाके नामसे तलबारसे घायल करके ध्रसतोपर सुला दिया
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2990)
- **Original**: तुम्हारी ख्याति होगी
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2991)
- **Original**: महापराक्रमो चण्छ और मुण्डकों मारा गया देख्व ना मरनेसे बची हुई बाकी सेना घयसे व्याकुल हो चारों ओर भाग गयी
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2992)
- **Original**: तंदनन्तर कालीने, चण्ड और मुण्डका मस्तक हाथमें ले चण्डिकाके पास जाकर प्रचण्ड अट्ठहास्त करते हुए कहा--
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2993)
- **Original**: 'देवि! मैंने चण्ड और मुण्ड छामक इन दो महापशुओंको तुम्हें भेंट किया है। व युद्धवज्ञमें
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2994)
- **Original**: तुप शुप्ध और रिशुम्भका स्वर हो वध करता
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2995)
- **Original**: व्वानीत ततो दुष्ठी अण्डमुण्डी महाखुरौ। उबाच काली कल्याणी ललितेच्ण्डिका वच्न;
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2996)
- **Original**: यस्माच्यण्ड चर मुण्ड श्र गृहीत्वा त्वमुपागता।
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2997)
- **Original**: चापुण्डेति ततो लोके ख्याता देघि भविष्यसि
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2998)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2999)
- **Original**: 25 # वहाँ लाये हुए उन
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3000)
- **Original**: हाते ऑमार्कण्डेबएुएणें सावर्षिके अब्यकरे वेवीयाहात्पे कण्डयुग्डव्धों कम ग़समोउथ्काय:
- **Translation**: 

---

