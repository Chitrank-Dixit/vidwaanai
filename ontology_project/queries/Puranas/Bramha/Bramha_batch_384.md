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

### Verse 1 (Bramha 0.7661)
- **Original**: लिये विद्वान्‌ पुरुष धर्मका अनुष्ठान करे। वह इस मनुष्यकों न इस लोकमें सुख मिलता है न! लोकमें भी फल देनेवाला होता है। ब्राह्ममुहूर्तमें परलोकमें। जो सदाचारका उल्लद्डन करके मनमाना
- **Translation**: 

---

### Verse 2 (Bramha 0.7662)
- **Original**: जागे। जागकर धर्म और अर्थका चिन्तन करे। बर्ताव करता है, उस पुरुषका कल्याण यज्ञ, दान
- **Translation**: 

---

### Verse 3 (Bramha 0.7663)
- **Original**: इसके बाद शब्या त्याग कर नित्यकर्मसे निवृत्त और तपस्यासे भी नहीं होता। दुराचारी पुरुषकों
- **Translation**: 

---

### Verse 4 (Bramha 0.7664)
- **Original**: हो, स्नान आदिसे पवित्र होकर मनको संयममें इस लोकमें बड़ी आयु नहीं मिलती, अत: उत्तम
- **Translation**: 

---

### Verse 5 (Bramha 0.7665)
- **Original**: रखते हुए पूर्वाभिमुख बैठे और आचमन करके +* पितुः पिण्डं प्रदधाच्च भोजयेच्च पितामहम्‌ । प्रपितामहस्प पिण्डं वै छ्ायं शास्त्रेषु निर्णय:
- **Translation**: 

---

### Verse 6 (Bramha 0.7666)
- **Original**: मृतेघु पिण्ड दातव्यं जीवन्तं चापि भोजयेत्‌। सपिण्डीकरणं नास्ति न च पार्वणमिष्यते
- **Translation**: 

---

### Verse 7 (Bramha 0.7667)
- **Original**: (220। 208-209)
- **Translation**: 

---

### Verse 8 (Bramha 0.7668)
- **Original**: + गृहस्थोचित सदाचार तथा कर्तव्याकर्तव्यका वर्णन * 369 संध्योपासन करे। प्रातःकालकी संध्या उस समय
- **Translation**: 

---

### Verse 9 (Bramha 0.7669)
- **Original**: पृथक्‌ नमक लेकर न खाय। जूठा अन्न खाना आरम्भ करे, जब तारे दिखायी देते हों। इसी
- **Translation**: 

---

### Verse 10 (Bramha 0.7670)
- **Original**: वर्जित है। मनुष्यको चाहिये कि मनको वशमें रखे प्रकार सायंकालकी संध्योपासना सूर्यास्तसे पहले
- **Translation**: 

---

### Verse 11 (Bramha 0.7671)
- **Original**: ! और खड़े होकर या चलते-चलते मल-मूत्रका ही विधिपूर्वक आरम्भ करे। आपत्तिकालके सिवा
- **Translation**: 

---

### Verse 12 (Bramha 0.7672)
- **Original**: त्याग, आचमन तथा किसी बस्तुका भक्षण न करे। और किसी समय उसका त्याग न करे। द्विजो! मुँह वार्तालाप न करे तथा उस अवस्थामें बुरी-बुरी बातें बकना, झूठ बोलना, कठोर बचन
- **Translation**: 

---

### Verse 13 (Bramha 0.7673)
- **Original**: स्वाध्याय भी वर्जित है। जूठी अवस्थामें सूर्य, चद्धमा मुँहसे निकालना, असत्‌ शास्त्र पढ़ना, नास्तिकवादको
- **Translation**: 

---

### Verse 14 (Bramha 0.7674)
- **Original**: और तारॉंकी ओर जानबूझकर न देखे। दूसरेके अपनाना तथा दुष्ट पुरुषोंकी सेवा करना अवश्य
- **Translation**: 

---

### Verse 15 (Bramha 0.7675)
- **Original**: आसन, शब्या और बर्तनका भी स्पर्श न करे। छोड़ देना चाहिये।* मनको वशमें रखते हुए। गुरुजनॉंके आनेपर उन्हें बैठनेकों आसन दे। प्रतिदिन सायंकाल और प्रातःकाल हवन करे।
- **Translation**: 

---

### Verse 16 (Bramha 0.7676)
- **Original**: उठकर प्रणाम आदिके द्वारा उनका आदर-सत्कार उदय और अस्तके समय सूर्यमण्डलका दर्शन न
- **Translation**: 

---

### Verse 17 (Bramha 0.7677)
- **Original**: करे। उनके अनुकूल वार्तालाप करे। जाते समय करे। बाल सँवारना, दर्पण देखना, दाँतन करना,
- **Translation**: 

---

### Verse 18 (Bramha 0.7678)
- **Original**: उनके पीछे-पीछे कुछ दूर जाकर पहुँचाये। उनके आँजन लगाना और देवताओंका तर्पण करना--यह
- **Translation**: 

---

### Verse 19 (Bramha 0.7679)
- **Original**: प्रतिकूल कोई बर्ताव न करे। एक वस्त्र धारण सब 'कार्य पूर्वाह्ककालमें ही करना चाहिये। करके भोजन और देवपूजन न करे। बुद्धिमान्‌ ग्राम, निवासस्थान, तीर्थ और क्षेत्रोंके मार्गमें,
- **Translation**: 

---

### Verse 20 (Bramha 0.7680)
- **Original**: पुरुष ब्राह्मणोंसे बोझ न ढुलाये। आगमें मूत्र त्याग जोते हुए खेतमें तथा गोशालामें मल-मूत्र न करे।
- **Translation**: 

---

