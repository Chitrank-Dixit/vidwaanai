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

### Verse 1 (Bramha 0.6041)
- **Original**: ' यों कहकर व्रजबासियोंने गिरियज्ञका चाहिये। वही उसके लिये उपकारक है। जो
- **Translation**: 

---

### Verse 2 (Bramha 0.6042)
- **Original**: अनुष्ठान किया। गिरिराज गोवर्धनको दही और मनुष्य एकका दिया हुआ फल भोगता और
- **Translation**: 

---

### Verse 3 (Bramha 0.6043)
- **Original**: खीर आदिकी बलि चढ़ायी। सैकड़ों-हजारों किसी दूसरेकी पूजा करता है, यह इस ज लोक वा 048 9 हु 5 गायों और साँडॉकी परलोकमें - कल्याणका भार पूजा र्‌ ड्वारा गिरिराजकी होता। हमारे इस स्रजकी जो प्रख्यात सोमाएँ हैं,
- **Translation**: 

---

### Verse 4 (Bramha 0.6044)
- **Original**: परिक्रमा करायी गयी। साँड जलसे भरे मेघकी उनका पूजन होना चाहिये। सीमाके भीतर बन
- **Translation**: 

---

### Verse 5 (Bramha 0.6045)
- **Original**: भाँति गर्जना करते थे। भगकान्‌ श्रीकृष्ण दूसरे है और वनके भीतर सम्पूर्ण पर्वत हैं, जो हमारे
- **Translation**: 

---

### Verse 6 (Bramha 0.6046)
- **Original**: रूपमें पर्वतके शिखरपर जा बैठे और मैं ही लिये परम आश्रय हैं। अत: हमें गिरियज्ञ और
- **Translation**: 

---

### Verse 7 (Bramha 0.6047)
- **Original**: मूर्तिमान्‌ गिरिराज हूँ--यों कहकर गोपोंद्वारा अर्पित गोयज्ञ आरम्भ करना चाहिये। इन्द्रसे हमारा क्या
- **Translation**: 

---

### Verse 8 (Bramha 0.6048)
- **Original**: किये हुए नाना प्रकारके अन्नॉका भोग लगाने लगे लाभ होता है। हमारे लिये तो गौएँ और
- **Translation**: 

---

### Verse 9 (Bramha 0.6049)
- **Original**: गिरिराज ही देवता हैं। ब्राह्मण मन्त्रयुक्त यज्ञको
- **Translation**: 

---

### Verse 10 (Bramha 0.6050)
- **Original**: . प्रधानता देते हैं। किसानोंके यहाँ सीरयज्ञ (हल-
- **Translation**: 

---

### Verse 11 (Bramha 0.6051)
- **Original**: ह पूजन) होता है और हम-जैसे बन एवं पर्वतॉमें
- **Translation**: 

---

### Verse 12 (Bramha 0.6052)
- **Original**: है रहनेवाले लोग गिरियज्ञ और गोयज्ञका अनुष्ठान । 8 करें तो उत्तम है। इसलिये मेरा विचार तो यह है कि आपलोग भाँति-भाँतिकी पूजा-सामग्रियोंसे
- **Translation**: 

---

### Verse 13 (Bramha 0.6053)
- **Original**: गिरिराज गोवर्धनकी पूजा करें। सम्पूर्ण ब्रजका
- **Translation**: 

---

### Verse 14 (Bramha 0.6054)
- **Original**: (7... दूध एकत्र किया जाय और उससे ब्राह्मणों तथा
- **Translation**: 

---

### Verse 15 (Bramha 0.6055)
- **Original**: * अन्य याचकोंकों भोजन कराया जाय। इस प्रकार गोवर्धनका पूजन, होम और ब्राह्मण-भोजन हो
- **Translation**: 

---

### Verse 16 (Bramha 0.6056)
- **Original**: 4505) 0 92 जानेपर गौओंका शरद्‌ ऋतुमें प्राप्त होनेवाले
- **Translation**: 

---

### Verse 17 (Bramha 0.6057)
- **Original**: --..... कप $ 6 47%: पुष्पोंद्वारा श्ृज्जार किया जाय और वे गिरिराजकी । श्र >अयबाह . 3
- **Translation**: 

---

### Verse 18 (Bramha 0.6058)
- **Original**: है परिक्रमा करें। गोपगण। यही भेरी सम्मति है।
- **Translation**: 

---

### Verse 19 (Bramha 0.6059)
- **Original**: 6404 /222/90/53. 20 2.7 यदि आपलोग प्रेमपूर्वक यह यज्ञ करेंगे तो 'तथा अपने कृष्णरूपसे ही गोपोंके साथ पर्वत- इसके द्वारा गौएँ और गिरिराज गोवर्धन प्रसत्र
- **Translation**: 

---

### Verse 20 (Bramha 0.6060)
- **Original**: शिख/पर चढ़कर उन्होंने अपने द्वितीय शरीर होंगे। साथ हो मुझे भी बड़ी प्रसन्नता होगी।'
- **Translation**: 

---

