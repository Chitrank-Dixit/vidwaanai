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

### Verse 1 (Bramha 0.681)
- **Original**: पुत्र तथा चित्रा नामकी कन्या हुई। इस प्रकार उनके समान रूपवान्‌ दूसरा कोई नहीं था। नरश्रेष्ठ
- **Translation**: 

---

### Verse 2 (Bramha 0.682)
- **Original**: रोहिणीकी नौ संतानें थीं। चित्रा ही आगे चलकर
- **Translation**: 

---

### Verse 3 (Bramha 0.683)
- **Original**: केड * संक्षिप्त यह्मपुराण * सुभद्राके नामसे विख्यात हुई। बसुदेवके देवकीके
- **Translation**: 

---

### Verse 4 (Bramha 0.684)
- **Original**: पत्नीके भयसे दूसरी स्त्रीसे विवाह नहीं किया। गर्भसे महायशस्त्री भगवान्‌ श्रीकृष्ण अवतीर्ण हुए।
- **Translation**: 

---

### Verse 5 (Bramha 0.685)
- **Original**: एक बार किसी युद्धमें विजयी होनेपर उन्हें एक बलरामके रेवतीके गर्भसे निशठ उत्पन्न हुए, जो
- **Translation**: 

---

### Verse 6 (Bramha 0.686)
- **Original**: कन्या मिली। उसे रथपर बैठी देख स्त्रीने पूछा--' यह माता-पिताके बड़े लाड़ले थे। सुभद्राके अर्जुनके
- **Translation**: 

---

### Verse 7 (Bramha 0.687)
- **Original**: कौन है?' तब वे डरकर योले-'यह तुम्हारा सम्बन्धसे महार्थी अभिमन्यु उत्पन्न हुआ।
- **Translation**: 

---

### Verse 8 (Bramha 0.688)
- **Original**: पुत्रवंधू है।!' यह सुनकर रानी बोली--'मेरे तो वसुदेवजीकी परम सौभाग्यशालिनी सात पत्रियोंसे
- **Translation**: 

---

### Verse 9 (Bramha 0.689)
- **Original**: [एन ज्र जो पुत्र उत्पन्त हुए, उनके नाम बतलाता हूँ; सुनो। शान्तिदेवाके भोज और विजय, सुनामाके वृकदेव और गद तथा त्रिगर्तराजकन्या वृकदेवीके महात्मा अगावह नामक पुत्र हुए। क्रोष्टुके एक और पुत्र महायशस्वी वृजिनवान्‌
- **Translation**: 

---

### Verse 10 (Bramha 0.690)
- **Original**: 4 हुए। उनके पुत्र स्वाहि थे। स्वाहिके पुत्र राजा उषदूु हुए, जिन्होंने प्रचुर दक्षिणावाले अनेक महायज्ञोंका अनुष्ठान किया था। उपदुक़े पुत्र
- **Translation**: 

---

### Verse 11 (Bramha 0.691)
- **Original**: हि चित्ररथ हुए, चित्ररथके शशबिन्दु, शशबिन्दुके
- **Translation**: 

---

### Verse 12 (Bramha 0.692)
- **Original**: पृथुश्रवा, पृथुश्रवाके अन्तर, अन्तरके सुयज्ञ तथा सुयज्ञके उषत्‌ हुए। उषतूका अपने धर्मके प्रति बड़ा आदर था। उपषत्‌के पुत्र शिनेयु, शिनेयुके मरुत्‌, मरुतके कम्बलबर्हिषू, कम्बलबर्टिष॒के 2-58. 5 रुकक्‍्मकवच, रुक्मकवचके परजित्‌ तथा परजित्‌्के
- **Translation**: 

---

### Verse 13 (Bramha 0.693)
- **Original**: कोई पुत्र नहीं, फिर यह किसकी पत्नी होनेसे पाँच पुत्र हुए--रुक्मेषु, पृथुरुक्म, ज्यामघ,
- **Translation**: 

---

### Verse 14 (Bramha 0.694)
- **Original**: पुत्रवधू हुई?” यह सुनकर ज्यामघने कहा--' तुम्हें पालित तथा हरि। पालित और हरिको पिताने
- **Translation**: 

---

### Verse 15 (Bramha 0.695)
- **Original**: जो पुत्र उत्पन्न होगा, उसके लिये यह पत्नी प्रस्तुत विदेह प्रान्तकी रक्षामें नियुक्त कर दिया। रुक्मेषु
- **Translation**: 

---

### Verse 16 (Bramha 0.696)
- **Original**: को गयी है।' तत्पश्चात्‌ रानी शैब्याने कठोर पृथुरुकक्‍्मकी सहायतासे राजा हुए। इन दोनों भाइयोंने
- **Translation**: 

---

### Verse 17 (Bramha 0.697)
- **Original**: तपस्या करके एक विदर्भ नामक पुत्र उत्पन्न राजा ज्यामघको घरसे निकाल दिया। तब वे बनमें
- **Translation**: 

---

### Verse 18 (Bramha 0.698)
- **Original**: किया। उसका विवाह उक्त राजकन्यासे हुआ। आश्रम बनाकर रहने लगे। उस समय शान्तिपरायण
- **Translation**: 

---

### Verse 19 (Bramha 0.699)
- **Original**: उसके गर्भसे क्रथ और कौशिक नामक पुत्र राजाको ब्राह्मणोंने बहुत कुछ समझाया। तब जे
- **Translation**: 

---

### Verse 20 (Bramha 0.700)
- **Original**: उत्पन हुए। वे दोनों बड़े ही शूर तथा युद्धविशारद धनुष लेकर रथपर आरूढ़ हो दूसरे देशमें गये।
- **Translation**: 

---

