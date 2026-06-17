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

### Verse 1 (Bramha 0.561)
- **Original**: जन्तु था, जिसके सौ पुत्र हुए। उन सबसमें छोटे उन्होंने चार पुत्र उत्पन्न किये-दुष्यन्त, सुष्मन्त,
- **Translation**: 

---

### Verse 2 (Bramha 0.562)
- **Original**: पृषत्‌ थे, जिनके पुत्र द्रपद हुए। ये सभी आजमीढ प्रवीर और अनाथ। दुष्यन्तके पुत्र पराक्रमी भरत! तथा सोमक क्षत्रिय कहलाते हैं। अजमीढके एक हुए, जो सर्बदमनके नामसे विख्यात थे। उनमें
- **Translation**: 

---

### Verse 3 (Bramha 0.563)
- **Original**: और पत्नी थीं, जिनका नाम था--धूमिनी। रानी दस हजार हाथियोंका बल था। वे शकुन्तलाके
- **Translation**: 

---

### Verse 4 (Bramha 0.564)
- **Original**: धूमिनी बड़ी पतित्रता थीं। ये पुत्रकी कामनासे गर्भसे उत्पन्न चक्रवर्ती राजा थे। उन्हींके नामपर
- **Translation**: 

---

### Verse 5 (Bramha 0.565)
- **Original**: व्रत करने लगीं। दस हजार वर्षोंतक अत्यन्त इस देशको भारतवर्ष कहते हैं। अन्विरानन्दन
- **Translation**: 

---

### Verse 6 (Bramha 0.566)
- **Original**: दुष्कर तपस्या करके उन्होंने विधिपूर्वक अग्रिमें बृहस्पतिजीके पुत्र महामुनि भरद्वाजने भरतसे
- **Translation**: 

---

### Verse 7 (Bramha 0.567)
- **Original**: हवन किया तथा पविश्नतापूर्वक नियमित भोजन पुत्रोत्पत्तिक लिये बड़े-बड़े यज्ञोंका अनुष्ठान कराया।
- **Translation**: 

---

### Verse 8 (Bramha 0.568)
- **Original**: करके वे अग्निहोत्रके कुशोंपर ही लेट गयीं। उसी इसके पहले पुत्र-जन्मका सारा प्रयास व्यर्थ हो
- **Translation**: 

---

### Verse 9 (Bramha 0.569)
- **Original**: अवस्थामें राजा अजमीढने धूमिनीदेवीके साथ चुका था। अत: भरद्वाजके प्रयत्रसे जो पुत्र उत्पन्न
- **Translation**: 

---

### Verse 10 (Bramha 0.570)
- **Original**: समागम किया। इससे ऋक्ष नामक पुत्रकी उत्पत्ति हुआ, उसका नाम वितथ हुआ। वितथके जन्मके हुई। ऋक्ष धूप्रके समान वर्णवाले एवं दर्शनीय बाद राजा भरत स्वर्गवासी हो गये, तब भरद्वाजजी
- **Translation**: 

---

### Verse 11 (Bramha 0.571)
- **Original**: पुरुष थे। ऋक्षसे संवरण और संबरणसे कुरु बितथको राज्यपर अभिषिक्त करके बनमें चले
- **Translation**: 

---

### Verse 12 (Bramha 0.572)
- **Original**: उत्पन्न हुए, जिन्होंने प्रयागसे जाकर कुरुक्षेत्रको गये। वितथने पाँच पुत्र उत्पन्न किये--सुहोत्र,
- **Translation**: 

---

### Verse 13 (Bramha 0.573)
- **Original**: स्थापना की
- **Translation**: 

---

### Verse 14 (Bramha 0.574)
- **Original**: बह बड़ा ही पवित्र एवं रमणीय क्षेत्र सुहोता, गय, गर्ग तथा महात्मा कपिल। सुहोत्रके ' है। कितने ही पुण्यात्मा पुरुष उसका सेवन करते दो पुत्र थे-महासत्यवादी काशिक तथा राजा
- **Translation**: 

---

### Verse 15 (Bramha 0.575)
- **Original**: हैं। कुरुका महान्‌ वंश उन्हींके नामपर कौरब गृत्समति। गृत्समतिके पुत्र ब्राह्मण, क्षत्रिय और
- **Translation**: 

---

### Verse 16 (Bramha 0.576)
- **Original**: कहलाया। कुरुके चार पुत्र हुए--सुधन्वा, सुभनु, वैश्य--तीनों बर्णोंक लोग हुए। परीक्षित्‌ और अरिमेजय। परीक्षित्‌के पुत्र जनमेजय, मुनिवरो! अब आजमीढ नामक दूसरे बंशका
- **Translation**: 

---

### Verse 17 (Bramha 0.577)
- **Original**: श्रुतसेन, अग्रसेन और भीमसेन हुए। ये सभी वर्णन सुनो। सुहोत्रका एक पुत्र था-बृहत्‌।
- **Translation**: 

---

### Verse 18 (Bramha 0.578)
- **Original**: बलशाली और पराक्रमी थे। जनमेजयके पुत्र उसके तौन पुत्र हुए--अजमीढ, द्विमीढ और
- **Translation**: 

---

### Verse 19 (Bramha 0.579)
- **Original**: सुरथ हुए, सुरथके विदूरथ, बिदूरथके महारथी पुरुमीढ। अजमीढसे नीलीके गर्भसे सुशान्ति नामक
- **Translation**: 

---

### Verse 20 (Bramha 0.580)
- **Original**: ऋक्ष हुए। ये दूसरे ऋक्ष थे। इस सोमबंशमें दो पुत्र उत्पन्न हुआ। सुशान्तिसे पुरुजाति और पुरुजातिसे
- **Translation**: 

---

