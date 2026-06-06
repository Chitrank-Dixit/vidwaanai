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

### Verse 1 (Mahabharat 0.4621)
- **Original**: युधिष्टिककों आहत कस्के जोरसे गर्जना की । फिर तो पाण्डव- महान्‌ पुरुवार्थ प्रकट कर।' यह कहकर युधिश्विस्ते कर्णको
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4621)
- **Original**: युधिष्टिककों आहत कस्के जोरसे गर्जना की । फिर तो पाण्डव- महान्‌ पुरुवार्थ प्रकट कर।' यह कहकर युधिश्विस्ते कर्णको
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4622)
- **Original**: पक्षके योद्धा बड़े अमर्षमें भरकर दौड़े और युधिष्ठिस्की रक्षाके दस बाणोंसे बींध डाला । सूतपुत्र कर्णने भी हैंसते-हैसते उन्हें लिये कर्णको बाणोंसे पीड़ित करने छगे । सात्यकि, चेकितान, दस बाणोंसे घायल करके तुरंत बदला चुकाया। तब
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4622)
- **Original**: पक्षके योद्धा बड़े अमर्षमें भरकर दौड़े और युधिष्ठिस्की रक्षाके दस बाणोंसे बींध डाला । सूतपुत्र कर्णने भी हैंसते-हैसते उन्हें लिये कर्णको बाणोंसे पीड़ित करने छगे । सात्यकि, चेकितान, दस बाणोंसे घायल करके तुरंत बदला चुकाया। तब
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4623)
- **Original**: युयुत्सु पाण्ड्य, धृष्टश॒प्न, झिखण्डी, ड्रोपदीके पुत्र, प्रभव्वक, युथिष्ठिरने पर्वतोंको भी बिदीर्ण करनेवाला यमदण्डके समान
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4623)
- **Original**: युयुत्सु पाण्ड्य, धृष्टश॒प्न, झिखण्डी, ड्रोपदीके पुत्र, प्रभव्वक, युथिष्ठिरने पर्वतोंको भी बिदीर्ण करनेवाला यमदण्डके समान
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4624)
- **Original**: नकुल-सहदेव, भीमसेन, धृष्टकेतु तथा करूष, मल्य, केकय, भपंकर बाण धनुषपर चढ़ाया और सूतपुत्रका वध करनेकी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4624)
- **Original**: नकुल-सहदेव, भीमसेन, धृष्टकेतु तथा करूष, मल्य, केकय, भपंकर बाण धनुषपर चढ़ाया और सूतपुत्रका वध करनेकी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4625)
- **Original**: काशी और कोसल देशके योद्धा--ये सब-के-सब कर्णपर इच्छासे उसे छोड़ दिया। वह वेगपूर्वक छोड़ा हुआ आाण
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4625)
- **Original**: काशी और कोसल देशके योद्धा--ये सब-के-सब कर्णपर इच्छासे उसे छोड़ दिया। वह वेगपूर्वक छोड़ा हुआ आाण
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4626)
- **Original**: बाणोंका प्रहार करने लगे। पाज्ञालदेशीय जनमेजय भी उसे बिजलीके समान कड़ककर महारथी कर्णकी बायीं कोखमें
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4626)
- **Original**: बाणोंका प्रहार करने लगे। पाज्ञालदेशीय जनमेजय भी उसे बिजलीके समान कड़ककर महारथी कर्णकी बायीं कोखमें
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4627)
- **Original**: सायकोसे बींधने लगगा। पाण्डबंीर कर्णपर सब ओरसे बैस गया। उसकी चोटसे कर्णको मूर्छां आ गयी। उसका
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4627)
- **Original**: सायकोसे बींधने लगगा। पाण्डबंीर कर्णपर सब ओरसे बैस गया। उसकी चोटसे कर्णको मूर्छां आ गयी। उसका
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4628)
- **Original**: बाराहकर्ण, नाराच, नालीक, बाण, वत्प्दन्‍्त, विपाट तथा सारा झरीर झिथिल हो गया, धनुष हाथसे छूटकर रथपर जा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4628)
- **Original**: बाराहकर्ण, नाराच, नालीक, बाण, वत्प्दन्‍्त, विपाट तथा सारा झरीर झिथिल हो गया, धनुष हाथसे छूटकर रथपर जा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4629)
- **Original**: क्षुत्र आदि नाना प्रकारके अख्न-झख्तोंकी वर्षा करने लगे । यह
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4629)
- **Original**: क्षुत्र आदि नाना प्रकारके अख्न-झख्तोंकी वर्षा करने लगे । यह
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4630)
- **Original**: कर्णपर्व ] देख कर्णने ब्रह्माख्र प्रकट किया, उसके बाणोंसे सम्पूर्ण
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4630)
- **Original**: कर्णपर्व ] देख कर्णने ब्रह्माख्र प्रकट किया, उसके बाणोंसे सम्पूर्ण
- **Translation**: 

---

