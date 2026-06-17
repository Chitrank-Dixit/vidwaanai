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

### Verse 1 (Vaivtpuran 37.18116)
- **Original**: ऊर्थ्व॑ नारायणी पातु अम्बिकाध: सदावतु । ज्ञाने ज्ञानप्रदा पातु स्थप्रे निद्रा सदावतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 37.18117)
- **Original**: इति ते कथित वत्स सर्वमन्त्रौधविग्रहम्‌ । ब्रह्माण्डविजयं नाम कञवचं परमाद्भधुतम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 38.8049)
- **Original**: «'गंणपतिखण्ड « 379 $)
- **Translation**: 

---

### Verse 4 (Vaivtpuran 38.8050)
- **Original**: 88 888 दुर्गा-कवचका वर्णन नारदजीने कहा--प्रभो! महालक्ष्मीके मनोहर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 38.8051)
- **Original**: . “** हीं दुर्गतिनाशिन्यै स्वाहा ' मेरे मस्तककी कबचका बर्णन तो आपने कर दिया। ब्रह्मन्‌!
- **Translation**: 

---

### Verse 6 (Vaivtpuran 38.8052)
- **Original**: रक्षा करे। '3» ह्लीं' मेरे कपालकी और “3 अब दुर्गतिनाशिनी दुगकि उस उत्तम कवचको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 38.8053)
- **Original**: हीं श्रीं' नेत्रोंकी रक्षा करे। '3» दुर्गाय नमः बतलाइये, जो पद्माक्षके प्राणतुल्य, जीवनदाता,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 38.8054)
- **Original**: सदा मेरे दोनों कानोंकी रक्षा करे। '30 हीं श्रीं' बलका हेतु, कवचोंका सार-तत्त्व और दुर्गाकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 38.8055)
- **Original**: सदा सब ओरसे मेरी नासिकाकी रक्षा करे। “हीं सेवाका मूल कारण है। श्रीं हूं' दाँतोंकी और 'क्लीं' दोनों ओष्टोंकी रक्षा श्रीनारायण बोले--नारद! प्राचीन कालमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 38.8056)
- **Original**: करे। “क्रो क्रीं क्रीं' कण्ठकी रक्षा करे। 'दुर्गे' श्रीकृष्णने गोलोकमें ब्रह्माकों दुर्गाका जो शुभप्रद
- **Translation**: 

---

### Verse 11 (Vaivtpuran 38.8057)
- **Original**: कपोलोंकी रक्षा करे। 'दुर्गविनाशिन्यै स्वाहा' कवच दिया था, उसका वर्णन करता हूँ; सुनो।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 38.8058)
- **Original**: निरन्तर कंधोंकी रक्षा करे। 'विपद्विनाशिन्यै पूर्वकालमें त्रिपुर-संग्रामके अवसरपर ब्रह्माजीने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 38.8059)
- **Original**: स्वाहा' सब ओरसे मेरे वक्षःस्थलकी रक्षा करे। इसे शंकरको दिया, जिसे भक्तिपूर्वक धारण करके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 38.8060)
- **Original**: ['दुर्गें दुर्गे रक्षणीति स्वाहा' सदा नाभिकी रक्षा रुद्रने त्रिपुरका संहार किया था। फिर शंकरने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 38.8061)
- **Original**: करे। 'दुर्गे दुर्गे रक्ष रक्ष" सब ओरसे मेरी पीठकी सा गौतमको और गौतमने पद्माक्षको दिया,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 38.8062)
- **Original**: रक्षा करे। '3» ह्डीं दुर्गाय॑ स्वाहा' सदा हाथ- जिसके प्रभावसे विजयी पद्माक्ष सातों द्वीपोंका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 38.8063)
- **Original**: पैरोंकी रक्षा करें। '3 हीं दुर्गाय॑ स्वाहा' सदा अधिपति हो गया। जिसके पढ़ने एवं धारण मेरे सर्वाद्गकी रक्षा करे। पूर्वमें 'महामाया' रक्षा करनेसे ब्रह्मा भूतलपर ज्ञानवान्‌ और शक्तिसम्पन्न
- **Translation**: 

---

### Verse 18 (Vaivtpuran 38.8064)
- **Original**: करे। अग्निकोणमें 'कालिका', दक्षिणमें 'दक्षकन्या' हो गये। जिसके प्रभावसे शिव सर्वज्ञ और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 38.8065)
- **Original**: और नै्त्यकोणमें 'शिवसुन्दरी' रक्षा करे। योगियोंके गुरु हुए और मुनिश्रेष्ठ गौतम शिव-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 38.8066)
- **Original**: पश्चिममें 'पार्वती ', वायव्यकोणमें 'बाराही ', उत्तरमें तुल्य माने गये। इस “त्रह्माण्डविजय' नामक
- **Translation**: 

---

