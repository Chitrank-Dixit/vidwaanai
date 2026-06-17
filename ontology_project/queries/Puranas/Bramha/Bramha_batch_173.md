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

### Verse 1 (Bramha 0.3441)
- **Original**: देवताओंकी प्रीति बढ़ानेवाला हैं। मुनिश्रेष्ठ ! नन्दिकेश्वके पास जाकर बोले-'हमें जगत्‌का वहाँ किया हुआ केवल स्नान भी सहस््न गो- उपकार करनेबाली गौएँ दीजिये।' नन्‍्दी
- **Translation**: 

---

### Verse 2 (Bramha 0.3442)
- **Original**: दानोंका फल देनेवाला है। #>>>#स्फपथ 9700 श्वेततीर्थ, शुक्रतीर्थ और इन्द्रतीर्थका माहात्म्य ब्रह्माजी कहते हैं-नारद! श्वेततीर्थ तीनों लोकोंमें विख्यात है। उसके श्रवणमात्रसे मनुष्य
- **Translation**: 

---

### Verse 3 (Bramha 0.3443)
- **Original**: सकते। जिनके ऊपर भगवान्‌ शंकर प्रसन्न हो सब पापोंसे छुटकारा था जाता है। पूर्वकालमें
- **Translation**: 

---

### Verse 4 (Bramha 0.3444)
- **Original**: जाय, उन्हें भय कैसा।' श्वेत नामके एक ब्राह्मण थे, जो महर्षि गौतमके
- **Translation**: 

---

### Verse 5 (Bramha 0.3445)
- **Original**: . तब मृत्युने अपना फंदा हाथमें लेकर स्वयं ही प्रिय सखा थे। वे गोदाबरीके तटपर रहकर
- **Translation**: 

---

### Verse 6 (Bramha 0.3446)
- **Original**: ब्राह्मणके घरमें प्रवेश किया। ब्राह्मण तो भक्तिपूर्वक अतिथियोंके स्वागत-सत्कारमें लगे रहते और
- **Translation**: 

---

### Verse 7 (Bramha 0.3447)
- **Original**: भगवान्‌ शिवकी पूजा कर रहे थे। उन्हें न तो मन-वाणी तथा क्रियाद्वारा भगवान्‌ शिवका भजन
- **Translation**: 

---

### Verse 8 (Bramha 0.3448)
- **Original**: मृत्युके आनेका पता था और न यमदूतोंके। करते थे। वे सदा भगवान्‌ सदाशिवकी पूजा और
- **Translation**: 

---

### Verse 9 (Bramha 0.3449)
- **Original**: श्वेतके समीप पाशधारी मृत्युकों खड़ा देख ध्यान करते रहते थे। शिवक्े भजनमें ही उनकी
- **Translation**: 

---

### Verse 10 (Bramha 0.3450)
- **Original**: दण्डधारी भैरबने विस्मित होकर पूछा-- मृत्युदेव ! आयु पूरी हो गयी। तब यमराजके दूत उन्हें ले
- **Translation**: 

---

### Verse 11 (Bramha 0.3451)
- **Original**: यहाँ क्या देखते हो ?' मृत्युने उत्तर दिया--'मैं जानेके लिये आये, परंतु नारदजी ! वे ब्राह्मण-
- **Translation**: 

---

### Verse 12 (Bramha 0.3452)
- **Original**: श्वेतको ले जानेके लिये यहाँ आया हूँ, अतः देवताके घरमें प्रवेश न कर सके। जब ब्राह्मणकी
- **Translation**: 

---

### Verse 13 (Bramha 0.3453)
- **Original**: इन्हींको देखता हूँ।' भैरवने कहा--/लौट जाओ।' मृत्युका समय व्यतीत हो गया, तब चित्रकने पृत्युने श्वेतपर अपना फंदा फेंका। यह देखकर मृत्युसे पूछा--' मृत्यो ! श्वेतका जीवन समाप्त हो
- **Translation**: 

---

### Verse 14 (Bramha 0.3454)
- **Original**: भैरव कुपित हो उठे। उन्होंने शिबके दिये हुए चुका है, वह अबतक क्‍यों नहीं आवा? तुम्हारे
- **Translation**: 

---

### Verse 15 (Bramha 0.3455)
- **Original**: दण्डसे मृत्युपर गहरी चोट की। मृत्युदेवता पाश दूत भी अभीतक नहीं लौटे। ऐसा होना उचित
- **Translation**: 

---

### Verse 16 (Bramha 0.3456)
- **Original**: हाथमें लिये हुए ही धरतीपर गिर पड़े। मृत्युको नहीं।' यह सुनकर मृत्युकों बड़ा क्रोध हुआ और
- **Translation**: 

---

### Verse 17 (Bramha 0.3457)
- **Original**: मारा गया देख यमदूत भाग गये। उन्होंने मृत्युके ये स्वयं ही श्वेतके घरपर पधारे। उनके दूत
- **Translation**: 

---

### Verse 18 (Bramha 0.3458)
- **Original**: वधका समाचार यमराजसे कहा। यह सुनकर भयभीत होकर बाहर ही खड़े थे। उन्हें देखकर
- **Translation**: 

---

### Verse 19 (Bramha 0.3459)
- **Original**: महिषबाहन यमराजकों बड़ा क्रोध हुआ। उन्होंने मृत्युने पूछा-'दूतों ! यह क्‍या बात है?' दूत
- **Translation**: 

---

### Verse 20 (Bramha 0.3460)
- **Original**: अधिक बलवान चित्रगुप्त, अपनी रक्षा करनेवाले ब्रोले--' श्वेत भगवान्‌ शिवके द्वारा सुरक्षित हैं।
- **Translation**: 

---

