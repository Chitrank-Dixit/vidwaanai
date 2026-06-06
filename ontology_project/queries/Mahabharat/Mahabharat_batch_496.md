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

### Verse 1 (Mahabharat 0.4951)
- **Original**: अजुनके द्वारा खींचे जानेबाले गाष्डीव धनुषकी भरकर ठंकार गये हैं। किस-किस तरहके बाण बचे हैं और उनकी संख्या
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4951)
- **Original**: अजुनके द्वारा खींचे जानेबाले गाष्डीव धनुषकी भरकर ठंकार गये हैं। किस-किस तरहके बाण बचे हैं और उनकी संख्या
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4952)
- **Original**: क्‍या तुम्हें नहीं सुनायी देती ? पाष्डुलन्दन ! लो, तुम्हारी सारी कितनी है ? यह सब समझकर बता।' कामनाएँ पूरी हुई, उधर देखो, हाथियोंकी सेनामें अर्जुनके विज्ञोकतें कहा--औीरवर ! अब अपने पास साठ हजार
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4952)
- **Original**: क्‍या तुम्हें नहीं सुनायी देती ? पाष्डुलन्दन ! लो, तुम्हारी सारी कितनी है ? यह सब समझकर बता।' कामनाएँ पूरी हुई, उधर देखो, हाथियोंकी सेनामें अर्जुनके विज्ञोकतें कहा--औीरवर ! अब अपने पास साठ हजार
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4953)
- **Original**: रथकी ध्वजाका बानर दिखायी देता है। वह ध्वजाके ऊपर मार्गण हैं, दस-दस हजार क्षु और भल्ल हैं, दो हजार नाराच
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4953)
- **Original**: रथकी ध्वजाका बानर दिखायी देता है। वह ध्वजाके ऊपर मार्गण हैं, दस-दस हजार क्षु और भल्ल हैं, दो हजार नाराच
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4954)
- **Original**: चढ़कर झन्ुओंको भयभीत करता हुआ चारें ओर देख रहा है। बचे. हैं तथा तीन हजार प्रदर हैं। अभी इतने अख्न-झख्त्र
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4954)
- **Original**: चढ़कर झन्ुओंको भयभीत करता हुआ चारें ओर देख रहा है। बचे. हैं तथा तीन हजार प्रदर हैं। अभी इतने अख्न-झख्त्र
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4955)
- **Original**: मैं स्वयं भी उसे देखकर डर रहा हूँ। अर्जुनका जह विचित्र
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4955)
- **Original**: मैं स्वयं भी उसे देखकर डर रहा हूँ। अर्जुनका जह विचित्र
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4956)
- **Original**: दर संक्षिप्त महाभारत [ कर्णपर्व मुकुट, जिसमें सूर्यके समान खमकील्हीःमणि लगी हुई है,
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4956)
- **Original**: दर संक्षिप्त महाभारत [ कर्णपर्व मुकुट, जिसमें सूर्यके समान खमकील्हीःमणि लगी हुई है,
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4957)
- **Original**: सारथिसहित चार सौ रथ्षियोंको मार डाला, सात” सौ कितना सुन्दर है ? उनकी बगलमें देवदत्त नामवाल्त श्वेत झद्ब
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4957)
- **Original**: सारथिसहित चार सौ रथ्षियोंको मार डाला, सात” सौ कितना सुन्दर है ? उनकी बगलमें देवदत्त नामवाल्त श्वेत झद्ब
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4958)
- **Original**: हाथियोंका है। इसी प्रकार भगवान्‌ श्रीकृष्णके पाश्च॑में सूर्यके समान
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4958)
- **Original**: हाथियोंका है। इसी प्रकार भगवान्‌ श्रीकृष्णके पाश्च॑में सूर्यके समान
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4959)
- **Original**: पैदलॉको मौतके प्रकार कान्तिमान्‌ चक्र है, जो उनका यज्ञ बढ़ानेबाला है। यदुबंशी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4959)
- **Original**: पैदलॉको मौतके प्रकार कान्तिमान्‌ चक्र है, जो उनका यज्ञ बढ़ानेबाला है। यदुबंशी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4960)
- **Original**: कौरव-योद्धाओंका संहार करते हुए महाबल्ली अर्जुन सदा उसकी पूजा किया करते हैं। श्रकृष्णके पास उनका
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4960)
- **Original**: कौरव-योद्धाओंका संहार करते हुए महाबल्ली अर्जुन सदा उसकी पूजा किया करते हैं। श्रकृष्णके पास उनका
- **Translation**: 

---

