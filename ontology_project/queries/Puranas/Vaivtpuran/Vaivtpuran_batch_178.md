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

### Verse 1 (Vaivtpuran 13.2929)
- **Original**: स्वभाव ही बन गया था। वह केवल भगवान्‌ परम तपस्विनी देवी कैसे असुरके चंगुलमें फैंस शिवमें ही श्रद्धा रखता था। ऐसे स्वभाववाले गयी ? सम्पूर्ण संदेहोंको दूर करनेवाले प्रभो! आप
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.2930)
- **Original**: राजा वृषध्वजको देखकर सूर्यने उसे शाप दे मेरे इस संशयको मिटानेकी कृपा करें। दिया--' राजन! तेरी श्री नष्ट हो जाय!' भगवान्‌ नारायण कहते हैं--नारद! भक्तपर संकट देख आशुतोष भोलेनाथ दक्षसावर्णि नामसे प्रसिद्ध एक पुण्यात्मा मनु हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.2931)
- **Original**: भगवान्‌ शंकर हाथमें त्रिशूल उठाकर सूर्यपर टूट गये हैं। भगवान्‌ विष्णुके अंशसे प्रकट ये मनु
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.2932)
- **Original**: पड़े। तब सूर्य अपने पिता कश्यपजीके साथ परम पवित्र, यशस्ती, विशद कीर्तिसे सम्पन्न तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.2933)
- **Original**: ब्रह्माजीकी शरणमें गये। शंकर त्रिशूल लिये श्रीहरिके प्रति अटूट श्रद्धा रखनेवाले थे। इनके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.2934)
- **Original**: ब्रह्मतोककों चल दिये। ब्रह्माकों भी शंकरजीका पुत्रका नाम था ब्रह्मसावर्णि। उनका भी अन्तः-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.2935)
- **Original**: भय था, अतएव उन्होंने सूर्यको आगे करके करण स्वच्छ था। उनके मनमें धार्मिक भावना
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.2936)
- **Original**: बैकुण्ठकी यात्रा की। उस समय ब्रह्मा, कश्यप थी और भगवान्‌ श्रीहरिपर वे श्रद्धा रखते थे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.2937)
- **Original**: और सूर्य तीनों भयभीत थे। उन तीनों महानुभावोंने ब्रह्मसावर्णिके पुत्र धर्मसावर्णि नामसे प्रसिद्ध हुए,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.2938)
- **Original**: सर्वेश भगवान्‌ नारायणकी शरण ग्रहण की। जिनकी इन्द्रियाँ सदा वशमें रहती थीं और मन
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.2939)
- **Original**: तीनोंने मस्तक झुकाकर भगवान्‌ श्रीहरिको प्रणाम श्रीहरिकी उपासनामें निरत रहता था। धर्मसावर्णिसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.2940)
- **Original**: किया, बारंबार प्रार्थाा की और उनके सामने इन्द्रियनिग्रही एवं परम भक्त रुद्रसावर्णि पुत्ररूपमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.2941)
- **Original**: अपने भयका सम्पूर्ण कारण कह सुनाया। तब प्रकट हुए। इन रुद्रसाबर्णिके पुत्रका नाम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.2942)
- **Original**: भगवान्‌ नारायणने कृपापूर्वक उन सबको अभव देवसावर्णि हुआ। ये भी परम वैष्णव थे।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.2943)
- **Original**: प्रदाव किया और कहा--' भयभीत देबताओ! देवसावर्णिके पुत्रका नाम इन्द्रसार्णि था। फिर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.2944)
- **Original**: स्थिर हो जाओ। मेरे रहते तुम्हें कोई भय नहीं। भगवान्‌ विष्णुके अनन्य उपासक इन इन्द्रसावर्णिसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.2945)
- **Original**: विपत्तिक अवसरपर डरे हुए जो भी व्यक्ति जहाँ- वृषध्वजका जन्म हुआ। भगवान्‌ शंकरमें इस
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.2946)
- **Original**: कहाँ भी मुझे याद करते हैं, मैं हाथमें चक्र वृषध्वजकी असौम श्रद्धा थी। स्वयं भगवान्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.2947)
- **Original**: लिये तुरंत बहीं पहुँचकर उनकी रक्षा करता हूँ*। शंकर इसके यहाँ बहुत कालतक ठहरे थे। इसके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.2948)
- **Original**: देवो! मैं अखिल जगत्‌का कर्ता-भर्ता हूँ। मैं प्रति भगवान्‌ शंकरका स्लेह पुत्रसे भी बढ़कर
- **Translation**: 

---

