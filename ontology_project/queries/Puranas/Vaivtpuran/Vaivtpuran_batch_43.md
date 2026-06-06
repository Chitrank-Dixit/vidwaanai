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

### Verse 1 (Vaivtpuran 4.8907)
- **Original**: वायुके आधारपर स्थित था। श्रीराधिकाकी आज्ञाका वर्णन नहीं कर सके हैं। वह मनोहर आश्रम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8908)
- **Original**: अनुसरण करते हुए परमेश्वर श्रीकृष्णकी इच्छासे गोलाकार बना है तथा उसका विस्तार बारह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8909)
- **Original**: उसका निर्माण हुआ है। वह केवल मद्जलका कोसका है। उसमें सौ मन्दिर बने हुए हैं। वह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8910)
- **Original**: धाम है और सहस्नों सरोवरोंसे सुशोभित है। अद्भुत आश्रम दिव्य रत्रोंके तेजसे जगमगाता रहता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8911)
- **Original**: . मुने! देवताओंने वहाँ अत्यन्त मनोहर नृत्य है। बहुमूल्य रत्नोंक सार-समूहसे उसकी रचना
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8912)
- **Original**: तथा सुन्दर तालसे युक्त रमणीय संगीत देखा, हुई है। वह दुर्लद्वथ एवं गहरी खाइयोंसे सुशोभित जहाँ श्रीराधा-कृष्णके गुणोंका अनुवाद हो रहा है। कल्पवृक्ष उस आश्रमको सब ओरसे घेरे हुए
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8913)
- **Original**: था। उस अमृतोपम गीतको सुनते ही वे देवता हैं। उसके भीतर सैकड़ों पुष्पोद्यान शोभा पाते
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8914)
- **Original**: मूरच्छित हो गये। फिर क्षणभरमें सचेत हो मन-
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8915)
- **Original**: क्र श्रीकृष्णजन्मखण्ड * 409 44428: 8 : 2 22
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8916)
- **Original**: ] । 20 0 2 00। 3 ऋऋऋऋऋब। ही-मन श्रीकृष्णका चिन्तन करते हुए उन्होंने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8917)
- **Original**: उनके नाम सुनो-सुशीला, शशिकला, यमुना, स्थान-स्थानपर परम आश्चर्यमय मनोहर दृश्ण
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8918)
- **Original**: माधवी, रति, कदम्बमाला, कुन्ती, जाहवी, देखे। नाना प्रकारके वेश धारण किये समस्त
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8919)
- **Original**: स्वयंप्रभा, चन्द्रमुखी, पद्ममुखी, सावित्री, सुधामुखी, गोपिकाएँ उनके दृष्टिपथमें आयीं। कोई अपने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8920)
- **Original**: शुभा, पद्मा, पारिजाता, गौरी, सर्वमड्भगला, कालिका, हाथोंसे मृदंग बजा रही थीं तो किन्हींके हाथोंसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8921)
- **Original**: कमला, दुर्गा, भारती, सरस्वती, गड्जा, अम्बिका, बीणा-वादन हो रहा था। किन्हींके हाथमें चैंबर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8922)
- **Original**: मधुमती, चम्पा, अपर्णा, सुन्दरी, कृष्णप्रिया, सती, थे तो किन्हींक करताल। किन्हींके हाथोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8923)
- **Original**: नन्दिनी और ननन्‍्दना-ये सब-कौ-सब समान यन्त्रवाद्य शोभा पा रहे थे। कितनी ही रत्नमय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8924)
- **Original**: रूपवाली हैं। इनके शुभ्र आश्रम रत्नों और . नूपुरोंकी झनकार फैला रही थीं। बहुतोंकौ रत्रमयी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8925)
- **Original**: धातुओंसे चित्रित हैं। नाना प्रकारके चित्रोंसे काझ्ी बज रही थी, जिसमें क्षुद्रघंटिकाओंके शब्द
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8926)
- **Original**: चित्रित होनेके कारण वे अत्यन्त मनोहर प्रतीत गूँज रहे थे। किन्हींके माथेपर जलसे भरे घड़े
- **Translation**: 

---

