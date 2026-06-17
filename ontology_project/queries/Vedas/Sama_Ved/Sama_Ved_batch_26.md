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

### Verse 1 (Sama Ved 0.501)
- **Original**: हे देवो ! वेद मज्रों के अनुसार आचरण करने वाले हम याजक, न कोई धर्म विरुद्ध कार्य करते हैं और न हो किसी को कोई हानि पहुँचाते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.502)
- **Original**: 177. दोषों आगाद्‌ बृहद्‌गाय द्युमद्गामननाथर्वण
- **Translation**: 

---

### Verse 3 (Sama Ved 0.503)
- **Original**: स्तुहि देव॑ सवितारम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.504)
- **Original**: हे प्रकाश मार्ग के पधिक अधर्ववेदीय ब्राह्मण ! हे बृहत्‌ नामक साम के स्तोता ! यज्ञ कार्य के दोषों को परिमार्जित करने के लिए सविता देवता का स्तवन्‌ करो
- **Translation**: 

---

### Verse 5 (Sama Ved 0.505)
- **Original**: 178. एघो उषा अपूर्व्या व्युच्छति प्रिया दिव: । स्तुषे वामश्विना बृहत्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.506)
- **Original**: यह प्रसन्नता देने वाली उषा अंतरिक्ष स्रे प्रकाशित होती है । हे (उषा के कार्य सहयोगी) अश्विनीकुमारो ! हम आपकी बृहद्‌ (विशेष) स्तुति करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.507)
- **Original**: 179, इन्द्रो दधीचो अस्थभिर्वत्राण्यप्रतिष्कुत: । जघान नवतीर्नव
- **Translation**: 

---

### Verse 8 (Sama Ved 0.508)
- **Original**: अपराजित इद्धदेव ने दधीचि की हड्डियों से ( बने हुए बज़ से) निन्‍्यानवे ( सैकड़ों-हजारों ) राक्षसों का संहार किया
- **Translation**: 

---

### Verse 9 (Sama Ved 0.509)
- **Original**: 180. इन्द्रेहि मत्स्यन्थसो विश्वेभि: सोपर्वभि: । महाँ अभिष्टिरोजसा
- **Translation**: 

---

### Verse 10 (Sama Ved 0.510)
- **Original**: हे इद्धदेव ! अन्नरूपी समस्त सोमरस से आप प्रफुल्लित होते हैं। आप आएँ और (सोमरस पान करके) अपनी शक्ति से दुर्दान्त शत्रुओं पर विजय प्राप्त करने को क्षमता प्राप्त करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.511)
- **Original**: 2.8 सामवेद-संहिता 181. आ तू न इन्द्र वृत्रहन्नस्माकमर्धमा गहि। महान्महीभिरूतिभि:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.512)
- **Original**: हे वृत्रहन्ता ! आप महान्‌ बनकर संरक्षण के विविध साधनों सहित हमारे पास आएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.513)
- **Original**: 182. ओजस्तदस्य तित्विष उभे यत्समवर्तयत्‌ । इन्द्रश्नमेंव रोदसी
- **Translation**: 

---

### Verse 14 (Sama Ved 0.514)
- **Original**: इन्द्रदेव का वह ओज प्रकाशित हो उठा है, जिसे वह द्युलोक से प्रथ्वीलोक तक (लपेटे हुए) चमड़े के समान फैला देता है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.515)
- **Original**: 183. अयमु ते समतसि कपोत इव गर्भधिम्‌। वचस्तच्चिन्न ओहसे
- **Translation**: 

---

### Verse 16 (Sama Ved 0.516)
- **Original**: हे इद्धदेव ! जैसे कबूतर, गर्मिणी कबूतरी के साथ बराबर बना रहता है, उसीप्रकार आपके लिए तैयार सोमरस के पास आप जाते हैं और हमारी स्तुति को ध्यानपूर्वक सुनते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.517)
- **Original**: 184. वात आ वातु भेषजं शम्भु मयोभु नो हृदे । प्र न आयूंषि तारिषत्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.518)
- **Original**: हमारे हृदय के लिए शान्तिदायक तथा सुखदायी ओषधियों को यह वायुदेव हमारे पास पहुँचाएँ। ये ओषधियोँ हमें दीर्घजीवी बनाएँ
- **Translation**: 

---

### Verse 19 (Sama Ved 0.519)
- **Original**: इति सप्तम: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.520)
- **Original**: जे में मे
- **Translation**: 

---

