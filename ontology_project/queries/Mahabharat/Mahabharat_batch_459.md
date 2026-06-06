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

### Verse 1 (Mahabharat 0.4581)
- **Original**: उन्होंने एक सायक अपने हाथमें लिया; परंतु कर्णने उसे काट ज्येष्ठ पुत्र वृषसेन स्वयं उसके पीछे रहकर पृष्ठभागकी रक्षा
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4581)
- **Original**: उन्होंने एक सायक अपने हाथमें लिया; परंतु कर्णने उसे काट ज्येष्ठ पुत्र वृषसेन स्वयं उसके पीछे रहकर पृष्ठभागकी रक्षा
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4582)
- **Original**: दिया और भीमको भी तीन बाणोंसे आहत किया। अब करता था। भीमने दूसरा बहुत तेज बाण हाथमें लिया और उसे सुषेणको तदलन्तर धृष्टसुप्र, सात्यकि, ब्रौपदीके पाँचों पुत्र, लक्ष्य करके छोड़ दिया; किंतु कर्णने उसके भी दुकड़े-दुकड़े भीमसेन, जनमेजय, शिखण्डी, प्रधान-प्रधान प्रभव्॒क, चेदि,
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4582)
- **Original**: दिया और भीमको भी तीन बाणोंसे आहत किया। अब करता था। भीमने दूसरा बहुत तेज बाण हाथमें लिया और उसे सुषेणको तदलन्तर धृष्टसुप्र, सात्यकि, ब्रौपदीके पाँचों पुत्र, लक्ष्य करके छोड़ दिया; किंतु कर्णने उसके भी दुकड़े-दुकड़े भीमसेन, जनमेजय, शिखण्डी, प्रधान-प्रधान प्रभव्॒क, चेदि,
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4583)
- **Original**: कर दिये और भीमसेनको मार डालनेकी इच्छासे उसने उनपर केकय, पश्ाल तथा मल्यदेशीय वीर और नकुल-सहदेव--
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4583)
- **Original**: कर दिये और भीमसेनको मार डालनेकी इच्छासे उसने उनपर केकय, पश्ाल तथा मल्यदेशीय वीर और नकुल-सहदेव--
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4584)
- **Original**: तिहत्तर आणोंका प्रहार किया। इधर, सुषेणने अपना धनुष ये कबच आदिसे सुसजित हो कर्णको मार डालनेकी इच्छासे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4584)
- **Original**: तिहत्तर आणोंका प्रहार किया। इधर, सुषेणने अपना धनुष ये कबच आदिसे सुसजित हो कर्णको मार डालनेकी इच्छासे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4585)
- **Original**: ऊैकर नकुलकी दोनों भुजाओं तथा उातौमें पाँच बाण मारे। उसकी ओर दौड़े। पास आते ही उन्होंने कर्णपर ब्राणोंकी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4585)
- **Original**: ऊैकर नकुलकी दोनों भुजाओं तथा उातौमें पाँच बाण मारे। उसकी ओर दौड़े। पास आते ही उन्होंने कर्णपर ब्राणोंकी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4586)
- **Original**: तब नकुलने भी बीस बाणोंसे सुषेणको घायल किया और झड़ी छग्रा दी। कर्णके पुत्रों तथा आपके पक्षके अन्य
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4586)
- **Original**: तब नकुलने भी बीस बाणोंसे सुषेणको घायल किया और झड़ी छग्रा दी। कर्णके पुत्रों तथा आपके पक्षके अन्य
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4587)
- **Original**: भीषण पिंहनाद करके कर्णको भी भयभीत कर डाला
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4587)
- **Original**: भीषण पिंहनाद करके कर्णको भी भयभीत कर डाला
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4588)
- **Original**: यह योद्धाओने - उस समय उन बीरोंको आगे बढ़नेसे गरेका।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4588)
- **Original**: यह योद्धाओने - उस समय उन बीरोंको आगे बढ़नेसे गरेका।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4589)
- **Original**: देख सुषेणके क्रोधको सीमा न रही, उसने नकुछूकों साठ सुषेणने. भल्छ मास्कर भीमसेनका धनुष काट डाला और
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4589)
- **Original**: देख सुषेणके क्रोधको सीमा न रही, उसने नकुछूकों साठ सुषेणने. भल्छ मास्कर भीमसेनका धनुष काट डाला और
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4590)
- **Original**: तथा सहदेवको सात बाणोंसे घायल कर दिया। दूसरी ओर सात नाराचोंसे उनके हृदयमें घाव करके बड़े जोरसे गर्जना
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4590)
- **Original**: तथा सहदेवको सात बाणोंसे घायल कर दिया। दूसरी ओर सात नाराचोंसे उनके हृदयमें घाव करके बड़े जोरसे गर्जना
- **Translation**: 

---

