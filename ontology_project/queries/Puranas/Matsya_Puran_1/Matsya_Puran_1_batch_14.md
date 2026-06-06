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

### Verse 1 (Matsya Puran 1 0.261)
- **Original**: चतुदंश से उत्तर अन्य इसका बैसा ही विश्वुत हुआ था ।27। मेरु के दक्षिण भाग में जो भी राजा लोग कीतितं किये गये हैं उनमें ज्येष्ठ काकुत्स्थ हुआ था
- **Translation**: 

---

### Verse 2 (Matsya Puran 1 0.262)
- **Original**: उसका पूत्र सुयोधन नाम वाला था ।
- **Translation**: 

---

### Verse 3 (Matsya Puran 1 0.263)
- **Original**: 28। तस्य पुत्र: पृथुर्नाम विश्वगश्च पृथो: सुत: । इन्दुस्तस्यचपुत्रो5भूद्युवनाश्वस्ततो 5भवत्‌ ।
- **Translation**: 

---

### Verse 4 (Matsya Puran 1 0.264)
- **Original**: 26 श्रावस्तश्चमहातेजावत्सकस्तत्सुतो5भवतु । निर्मिता येन श्रावस्ती गौडदेशेद्विजोत्तमा:
- **Translation**: 

---

### Verse 5 (Matsya Puran 1 0.265)
- **Original**: 30 श्रावस्तादु बृहृदश्वो5भूतु कुचलाश्वस्ततो 5भवत््‌ ।
- **Translation**: 

---

### Verse 6 (Matsya Puran 1 0.266)
- **Original**: 100 ] [ मत्स्यपुराण धुन्धूमारत्वमगमद्‌ धुन्धु ना ना हत: पुरा
- **Translation**: 

---

### Verse 7 (Matsya Puran 1 0.267)
- **Original**: 31 तस्य पुत्रास्त्रयो जाता हढ़ाश्वो दण्ड एब च -। कपिलाश्वश्च विख्यातों धौन्धुमारि: प्रतापवान्‌
- **Translation**: 

---

### Verse 8 (Matsya Puran 1 0.268)
- **Original**: 32 हृढ़ाश्वस्य प्रमादश्चहयश्वस्तस्यचात्मज: । हयेश्वस्यनिकुम्भोज्भूत्संहताश्वस्तताउभवत्‌
- **Translation**: 

---

### Verse 9 (Matsya Puran 1 0.269)
- **Original**: 33 अकृताश्वो रणाश्बश्च संहताश्वसुतावुभौ । युवनाश्वो रणाश्वस्य मान्धाताचततो5भत्‌
- **Translation**: 

---

### Verse 10 (Matsya Puran 1 0.270)
- **Original**: 34 मान्धातु: पुरुकृत्सो5दम्मसेनश्च पार्थिव: । मुचकुन्दश्च विख्यात: शत्रजिच्चः प्रतापवात्‌
- **Translation**: 

---

### Verse 11 (Matsya Puran 1 0.271)
- **Original**: 35 सुयोधन के पुत्र का नाम पृथु और पृथु का आत्मज विश्वग नाम- धारी था । इसके पुत्र का नाभ इन्दु था और इन्दु का सुत युवनाश्व हुआ था ।26। भ्रावस्त महान तेज वाला था। इसके पुत्र का नाम वत्सक था । हे द्विजगणों ! इसी ने गौड़ देश में श्रीवस्ती नाम वाली पुरी का निर्माण किया था
- **Translation**: 

---

### Verse 12 (Matsya Puran 1 0.272)
- **Original**: 30। श्रीवस्त से वृहृदश्व ने जन्म प्राप्त किया था और इसके पुत्र का नाम कुबलाश्व हुआ था । यह ॒धुन्धुन्मारता को प्राप्त हो गया था क्‍योंकि पहले घुन्धु नामधारी का हनन किया था 131। इसके तीन सुतों ने जन्म ग्रहण क्रिया था । उनके नाम हृढ़ाश्व और दड़ थे तथा तीसरा कपिलाश्व था जो प्रताप वाला घौन्धुमारिं नाम से थबिख्यात हुआ था । 32
- **Translation**: 

---

### Verse 13 (Matsya Puran 1 0.273)
- **Original**: हेढ़ाश्व का श्रमोद और प्रमोद का हर्यश्व पुत्र हुआ था
- **Translation**: 

---

### Verse 14 (Matsya Puran 1 0.274)
- **Original**: हयेश्व का निकुम्भ सुत उत्पन्न हुआ था फिर इसका पुत्र संहताश्ब पैदा हुआ था ।33। संहताश्व के अकृताव और उरणाश्व ये दो सुत हुये थे । उरणाश्व का पुत्र युवनाश्व हुआ तथा फिर इसके भान्धाता नाम वाले ने जन्म ग्रहण किया था ।
- **Translation**: 

---

### Verse 15 (Matsya Puran 1 0.275)
- **Original**: 34। मान्धाता के पुन्न का नाम पुरुकुत्स था अधरंसेन पाथिव भी हुआ था एवं मुचुकुन्द परम विख्यात हुआ ओर प्रतापधारी शत्रुजित्‌ भी हुआ था ! ऐसे ये चार धुत्र हुये थे ।351
- **Translation**: 

---

### Verse 16 (Matsya Puran 1 0.276)
- **Original**: सूयंबंश वर्णन] 101 पुरुकुत्सस्य पुत्रो5भूद्वसुदो नम्मंदापति: । सम्भूतिस्तस्यपुतो5मू त्त्रिध॑न्चा चततो5भवतु
- **Translation**: 

---

### Verse 17 (Matsya Puran 1 0.277)
- **Original**: 36 जत्रिघन्बन: सुतोजातस्त्रय्यारुण इति स्मृतः । तस्मात्सत्यब्रतोनामतस्मात्सत्य रथ: स्मृत:
- **Translation**: 

---

### Verse 18 (Matsya Puran 1 0.278)
- **Original**: 37 तस्य पुत्रों हरिश्चन्द्रों हरिश्चन्द्राज्व रोहित: । रोहितोच्च बृको जातो वृकाद्वायहुरजायत:
- **Translation**: 

---

### Verse 19 (Matsya Puran 1 0.279)
- **Original**: 38 सगरस्तस्य पुत्रो5भूद्राजा पस्मधासिक: । द्व भाय्यं सगरस्यापि प्रभाभानुमती तथा
- **Translation**: 

---

### Verse 20 (Matsya Puran 1 0.280)
- **Original**: 36 ताभ्यामाराधितः पूर्वमौर्वोजरग्नि: पुत्र॒काम्यया । औवस्तुष्टस्तयो: प्रादाचयथेष्टं वर्मुत्तमस्‌ ।
- **Translation**: 

---

