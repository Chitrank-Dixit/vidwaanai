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

### Verse 1 (Bramha 0.301)
- **Original**: और हरितके पुत्र चन्बु हुए। चुके पुत्र॒का नाम जब अनावृष्टिका भय दूर हो गया, तत्र विश्वामित्रने
- **Translation**: 

---

### Verse 2 (Bramha 0.302)
- **Original**: विजय था। वे सम्पूर्ण पृथ्यीपर विजय प्राप्त उसे पिताके राज्यपर अभिषिक्त करके उसके द्वारा
- **Translation**: 

---

### Verse 3 (Bramha 0.303)
- **Original**: करनेके कारण विजय कहलाये। विजयके पुत्र यज्ञ कराया। वे महातपस्वी थे, उन्होंने देवताओं
- **Translation**: 

---

### Verse 4 (Bramha 0.304)
- **Original**: राजा रुकक हुए, जो धर्म और अर्थके ज्ञाता थे। तथा वसिष्ठके देखते-देखते सत्यन्नरतकों शरीरसहित
- **Translation**: 

---

### Verse 5 (Bramha 0.305)
- **Original**: रुकुकके वृक, बृकके बाहु और बाहुके सगर हुए। हि कि जएकडडन
- **Translation**: 

---

### Verse 6 (Bramha 0.306)
- **Original**: वे गर अर्थात्‌ विषके साथ प्रकट हुए थे, इसलिये अ
- **Translation**: 

---

### Verse 7 (Bramha 0.307)
- **Original**: मुनिसे आग्नेय-अस्त्र प्रातषक्त तालजक्लू और हैहय 9
- **Translation**: 

---

### Verse 8 (Bramha 0.308)
- **Original**: पृथ्वीपर विजय प्राप्त की। फिर शक, पह़व तथा पारदोंके धर्मका निराकरण किया।
- **Translation**: 

---

### Verse 9 (Bramha 0.309)
- **Original**: मुनियोंने पूछा--सगरकी उत्पत्ति गरके साथ ऐल
- **Translation**: 

---

### Verse 10 (Bramha 0.310)
- **Original**: कैसे हुई? उन्होंने क्रोधभें आकर शक आदि
- **Translation**: 

---

### Verse 11 (Bramha 0.311)
- **Original**: महातेजस्वी क्षत्रियोंक कुलोचित धर्मांका निराकरण
- **Translation**: 

---

### Verse 12 (Bramha 0.312)
- **Original**: क्यों किया? यह सब विस्तारपूर्वक सुनाइये।
- **Translation**: 

---

### Verse 13 (Bramha 0.313)
- **Original**: लोमहर्षणजीने कहा--राजा याहु व्यसनी थे,
- **Translation**: 

---

### Verse 14 (Bramha 0.314)
- **Original**: अत: पहले हैहय नामक क्षत्रियोंने तालजड्डों और शकोंकी सहायतासे उनका राज्य छीन लिया। यवन, पारद, काम्बोज तथा पहुव नामके गणोंने
- **Translation**: 

---

### Verse 15 (Bramha 0.315)
- **Original**: + राजा सगरका चरित्र रथा इश्ष्याकुबवंशके मुख्य-मुख्य राजाओंका परिचय * 17 भी हैहयोंके लिये पराक्रम दिखाया। राज्य छिन
- **Translation**: 

---

### Verse 16 (Bramha 0.316)
- **Original**: पड़नेपर बे सभी महर्षि वसिष्ठकी शरणमें गये जानेपर राजा याहु दुःखी हो पत्नीके साथ वनमें चले
- **Translation**: 

---

### Verse 17 (Bramha 0.317)
- **Original**: और उनके चरणोंपर गिर पड़े। तब महातेजस्वी गये। वहीं उन्होंने अपने प्राण त्याग दिये। बाहुकी । बसिष्टने कुछ शर्तके साथ उन्हें अभय-दान दिया पत्नी यादवी गर्भवती थीं। वे भी राजाका सहगमन
- **Translation**: 

---

### Verse 18 (Bramha 0.318)
- **Original**: और राजा सगरकों रोका। सगरने अपनो प्रतिज्ञा करनेको प्रस्तुत हो गयीं। उन्हें उनकी सौतने
- **Translation**: 

---

### Verse 19 (Bramha 0.319)
- **Original**: तथा गुरुक वचनका विचार करके केवल उनके पहलेसे ही जहर दे रखा था। उन्होंने वनमें चिता ' धर्मका निराकरण किया और उनके वेष बदल बनाग्री और उसपर आरूढ़ हो पतिके साथ भस्म
- **Translation**: 

---

### Verse 20 (Bramha 0.320)
- **Original**: दिये। शकोके आधे मस्तकको मूँड़कर विदा कर हो जानेका विचार किया। भृगुबंशो और्वमुनिको (दिया। यवनों और काम्बोजोंका सारा सिर मुँड़ा उनकी दशापर बड़ी दया आयी। उन्होंने रानीको
- **Translation**: 

---

