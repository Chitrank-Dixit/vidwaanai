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

### Verse 1 (Vaivtpuran 13.11442)
- **Original**: दर्शनमात्रसे सुलभ हो जाता है। मनुष्यकों चाहिये देवताओंकी पूजा सम्पन्न कर ली। देवताको नैवेद्य [कि वह पुण्यके लिये समस्त जीवोंको अन्न दे; देकर जो ब्राह्मणकों नहीं देता है, उसका वह
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11443)
- **Original**: परंतु विशिष्ट जीवोंको अन्न-दान करनेसे विशिष्ट नैवेद्य भस्मीभूत होता है और पूजन निष्फल हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11444)
- **Original**: फलकी प्राप्ति होती है। भगवान्‌ विष्णु ब्राह्मणोंके जाता है। देवताका नैवेद्य यदि ब्राह्मणकों दिया
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11445)
- **Original**: भक्त हैं। उन्हें उत्तम वस्तुका दान करनेसे दाताको जाय तो उस दानसे वह निश्चय ही अक्षय हो जाता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11446)
- **Original**: जो फल मिलता है, वह निश्चय ही भक्त है और उस अवस्थामें देवता संतुष्ट होकर दाताको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11447)
- **Original**: ब्राह्मणणो भोजन करानेमात्रसे मिल जाता है। अभीष्ट वरदान दे अपने धामको जाते हैं। जो मूढ़
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11448)
- **Original**: भक्तके संतुष्ट होनेपर श्रीहरि संतुष्ट होते हैं और देवताको नैवेद्य अर्पित करके ब्राह्मणके दिये बिना
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11449)
- **Original**: श्रीहरिके संतुष्ट होनेपर सब देवता सिद्ध हो जाते स्वयं खा लेता है, वह दत्तापहारी (देकर छीन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11450)
- **Original**: हैं। ठीक उसी तरह जैसे वृक्षकी जड़ सींचनेसे लेनेवाला) है और देवताकी वस्तु खाकर नरकमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11451)
- **Original**: उसकी शाखाएँ भी पुष्ट होती हैं। यदि ये सब पड़ता है। जो भगवान्‌ विष्णुको अर्पित न किया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11452)
- **Original**: संचित द्रव्य आप किसी एक देवताको देते हैं तो गया हो, वह अन्न विष्ठा और जल मूत्रके समान
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11453)
- **Original**: अन्य सब देवता रुष्ट हो जायँगे। उस दशामें एक है। यह क्रम सभीके लिये है; परंतु ब्राह्मणोंके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11454)
- **Original**: देवता क्या करेगा? मेरी सम्मति तो यह है कि लिये विशेषरूपसे इसपर ध्यान देना उचित है।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11455)
- **Original**: यहाँ जितनी वस्तुएँ प्रस्तुत हैं, उनका आधा भाग यदि नैवेद्य अथवा भोज्य वस्तु देवताको न देकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11456)
- **Original**: आप श्रीगोवर्धनदेवको दे दीजिये। वे गौओंकी ब्राह्मणको दे दी गयी तो देवता ब्राह्मणके मुखमें सदा वृद्धि करते हैं; इसलिये उनका नाम “गोवर्धन ही उसे खाकर संतुष्ट हो स्वर्गलोकको लौट जाते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11457)
- **Original**: हुआ है। पिताजी ! इस भूतलपर गोवर्धनके समान हैं; अत: पिताजी! आप सारी शक्ति लगाकर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11458)
- **Original**: पुण्यवान्‌ दूसरा कोई नहीं है; क्योंकि वे नित्यप्रति ब्राह्मणॉंका पूजन कीजिये; क्योंकि वे इहलोक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11459)
- **Original**: गौओंकों नयी-नयी घास देते हैं। तीर्थस्थानोंमें और परलोकमें भी उत्तम फलके दाता हैं। जो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11460)
- **Original**: जाकर स्लान-दानसे जो पुण्य प्राप्त होता है; श्रीहरिकी आराधना करनेवाले ब्राह्मण हैं, वे उन्हें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11461)
- **Original**: ब्राह्मणॉंको भोजन करानेसे जिस पुण्यको प्राप्ति प्राणोंसे भी अधिक प्रिय हैं। हरिभक्त ब्राह्मणोंका
- **Translation**: 

---

