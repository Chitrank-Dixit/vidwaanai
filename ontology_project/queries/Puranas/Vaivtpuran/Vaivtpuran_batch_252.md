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

### Verse 1 (Vaivtpuran 13.11182)
- **Original**: आपके चरणोंकी सेवाकों छोड़कर इन्द्रपद, जाओ। वत्स! तुमको और कौन-सा उत्तम बर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11183)
- **Original**: अमरत्व अथवा परम दुर्लभ ब्रह्मपदको भी पानेकी अभीष्ट है? उसे इस समय माँगो। मैं तुम्हारा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11184)
- **Original**: इच्छा नहीं होती। आपके भक्तजन सालोक्य आदि दुःख दूर करनेवाला हूँ; अत: भय छोड़कर मुझसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11185)
- **Original**: चार प्रकारकी मुक्तियोंकों अत्यन्त फटे पुराने मनकी बात कहो। वस्त्रके चिथड़ेके समान तुच्छ देखते हैं *। ब्रह्मन्‌! श्रीकृष्णकी बात सुनकर कालियनाग, जो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11186)
- **Original**: मैंने भगवान्‌ अनन्तके मुखसे ज्यों ही आपके भवसे काँप रहा था, दोनों हाथ जोड़कर उनसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11187)
- **Original**: मन्त्रका उपदेश प्राप्त किया, त्यों ही आपकी बोला। भावना करते-करते आपके अनुग्रहसे मैं आपके कालियने कहा--वरदायक प्रभो! दूसरे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11188)
- **Original**: समान वर्णवाला हों गया। मैं अपक्व भक्त था किसी वरके लिये मेरी इच्छा नहीं है। प्रत्येक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11189)
- **Original**: अर्थात्‌ मेरी भक्ति परिपक्व नहीं हुई थी। यह जन्ममें मेरी आपके चरणकमलोंमें भक्ति बनी रहे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11190)
- **Original**: जानकर ही स्वयं सुदृढ़ भक्ति धारण करनेवाले और मैं सदा आपके उन चरणारविन्दोंका चिन्तन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11191)
- **Original**: गरुड़ने मुझे देशसे दूर कर दिया और धिक्कारा करता रहूँ; यही वर मुझे दीजिये। जन्म ब्राह्मणके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11192)
- **Original**: था। परंतु वरदेश्वर! अब आपने मुझे अविचल कुलमें हो या पशु-पक्षियोंकी योनियोंमें, सब
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11193)
- **Original**: भक्ति दे दी है। गरुड़ भी भक्त हैं, मैं भी भक्त समान है। वही जन्म सफल है, जिसमें आपके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11194)
- **Original**: हो गया हूँ; अतः अब वे मेरा त्याग नहीं कर चरणकमलोंकी स्मृति बनी रहे। यदि आपके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11195)
- **Original**: सकते हैं। आपके चरणारविन्दोंके चिहसे अलंकृत चरणोंका स्मरण न हो तो देवता होकर स्वर्गमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11196)
- **Original**: मेरे श्रीयुत मस्तककों देखकर गरुड़ मुझे सदोष रहना भी निष्फल है। जो आपके चरणोंके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11197)
- **Original**: होनेपर भी गुणवान्‌ मानेंगे; अत: इस समय मेरा चिन्तनमें तत्पर है, उसे जो भी स्थान प्राप्त हो,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11198)
- **Original**: त्याग नहीं कर सकेंगे। अब तो वे यह मानकर वही सबसे उत्तम है। उस पुरुषकी आयु एक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11199)
- **Original**: कि नागेन्रगण हमारे आराध्य हैं, मुझे कष्ट नहीं क्षणकी हो या करोड़ों कल्पोंकी, अथवा उसकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11200)
- **Original**: देंगे। परमेश्वर! अब मैं उनका वध्य नहीं रहा। आयु तत्काल ही क्षीण होनेवाली क्‍यों न हो;
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11201)
- **Original**: उन गुरुदेव अनन्तके सिवा मुझे कहीं किसीसे यदि वह आपकी आराधनामें बीत रही है तो
- **Translation**: 

---

