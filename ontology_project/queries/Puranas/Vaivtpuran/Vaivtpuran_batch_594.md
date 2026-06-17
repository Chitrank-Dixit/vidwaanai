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

### Verse 1 (Vaivtpuran 49.4714)
- **Original**: राधाके पूजनीय हैं। वे दोनों एक-दूसरेके इष्ट दुर्गें! इस प्रकार मैंने श्रीराधाका उत्तम देवता हैं। उनमें भेदभाव करनेवाला पुरुष नरकमें उपाख्यान सुनाया। यह सम्पत्ति प्रदान करनेवाला,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 49.4715)
- **Original**: पड़ता है।* श्रीकृष्णके बाद धर्मने, ब्रह्माजीने, पापहारी तथा पुत्र और पौत्रोंकी वृद्धि करनेवाला
- **Translation**: 

---

### Verse 3 (Vaivtpuran 49.4716)
- **Original**: मैंने, अनन्तने, बासुकिने तथा सूर्य और चन्द्रमाने है। श्रीकृष्ण दो रूपोंमें प्रकट हैं-द्विभुज और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 49.4717)
- **Original**: श्रीराधाका पूजन किया। तत्पश्चात्‌ देवराज इन्द्र, चतुर्भुज। चतुर्भुजरूपसे वे बैकुण्ठधाममें निवास
- **Translation**: 

---

### Verse 5 (Vaivtpuran 49.4718)
- **Original**: रुद्रगण, मनु, मनुपुत्र, देबेन्द्रणण, मुनीन्द्रणण तथा करते हैं और स्वयं द्विभुज श्रीकृष्ण गोलोकधाममें।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 49.4719)
- **Original**: सम्पूर्ण विश्वके लोगोंने श्रीशधाकी पूजा कौ। ये अतुर्भुजकी पत्नी महालक्ष्मी, सरस्वती, गड्भा और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 49.4720)
- **Original**: सब द्वितीय आवरणके पूजक हैं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 49.4721)
- **Original**: तृतीय आवरणमें तुलसी हैं। ये चारों देवियाँ चतुर्भुत नारायणदेवकौ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 49.4722)
- **Original**: सातों द्वीपोंके सम्राट्‌ सुयज्ञने तथा उनके पुत्र-पौत्रों प्रिया हैं। श्रोकृष्णकी पत्नी श्रोराधा हैं, जो उनके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 49.4723)
- **Original**: एवं मित्रोंने भारतवर्षमें प्रसन्नतापूर्वक श्रीराधिकाका अर्धाज्रसे प्रकट हुई हैं। वे तेज, अवस्था, रूप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 49.4724)
- **Original**: पूजन किया। उन महाराजकों दैववश किसी तथा गुण सभी दृष्टियोंसे उनके अनुरूप हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 49.4725)
- **Original**: ब्राह्मणने शाप दे दिया था, जिससे उनका हाथ विद्वान्‌ पुरुषको पहले 'राधा' नामका उच्चारण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 49.4726)
- **Original**: रोगग्रस्त हो गया था। इस कारण वे मन-ही-मन करके पश्चात्‌ “कृष्ण” नामका उच्चारण करना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 49.4727)
- **Original**: बहुत दुःखी रहते थे। उनकी राज्यलक्ष्मी छिन चाहिये। इस क्रमसे उलट-फेर करनेपर वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 49.4728)
- **Original**: गयी थी; परंतु श्रीराधाके वरसे उन्होंने अपना पापका भागी होता है, इसमें संशय नहीं है।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 49.4729)
- **Original**: राज्य प्राप्त कर लिया। ब्रह्माजीके दिये हुए स्तोत्रसे कार्तिककी पूर्णिमाको गोलोकके रासमण्डलमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 49.4730)
- **Original**: परमेश्वरी श्रीराधाकी स्तुति करके राजाने उनके श्रीकृष्णने श्रीराधाका पूजन किया और तत्सम्बन्धी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 49.4731)
- **Original**: अभेद्य कबचको कण्ठ और बाँहमें धारण किया महोत्सव रचाया। उत्तम रत्नोंकी गुटिकामें राधा-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 49.4732)
- **Original**: तथा पुष्करतीर्थमें सौ वर्षोतक ध्यानपूर्वक उनकी कवच रखकर गोपोंसहित श्रीहरिने उसे अपने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 49.4733)
- **Original**: पूजा कौ। अन्तमें वे महाराज रत्रमय विमानपर कण्ठ और दाहिनी बाँहमें धारण किया। भक्तिभावसे
- **Translation**: 

---

