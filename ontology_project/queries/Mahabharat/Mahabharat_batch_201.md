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

### Verse 1 (Mahabharat 0.2001)
- **Original**: सिरपर ल्लात मारी और उसकी छातीपर घुटने टेककर उसके जो हर समय कानतक धनुष चढ़ाये दिखायी देता था, वह
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2001)
- **Original**: सिरपर ल्लात मारी और उसकी छातीपर घुटने टेककर उसके जो हर समय कानतक धनुष चढ़ाये दिखायी देता था, वह
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2002)
- **Original**: ऐसा घूँसा मारा कि यह अचेत हो गया। महारथी सुझपकि गेस भाई तो पहले ही मर गया।' फिर यह भीमसेनपर
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2002)
- **Original**: ऐसा घूँसा मारा कि यह अचेत हो गया। महारथी सुझपकि गेस भाई तो पहले ही मर गया।' फिर यह भीमसेनपर
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2003)
- **Original**: पकड़ लिये जानेपर ज़िगत्तोंकी सारी सेना भयभीत होकर आर-आर तीखे बाण छोड़ने लगा। यह देखकर सभी पाण्डव
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2003)
- **Original**: पकड़ लिये जानेपर ज़िगत्तोंकी सारी सेना भयभीत होकर आर-आर तीखे बाण छोड़ने लगा। यह देखकर सभी पाण्डव
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2004)
- **Original**: भागने लूमी। तब महारथी पाण्डबॉने समस्त गौओंको फेर क्रोधमें भर गये और घोड़ोंको त्रिगत्तॉंकी ओर मोड़कर उनपर
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2004)
- **Original**: भागने लूमी। तब महारथी पाण्डबॉने समस्त गौओंको फेर क्रोधमें भर गये और घोड़ोंको त्रिगत्तॉंकी ओर मोड़कर उनपर
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2005)
- **Original**: लिया तथा सुझमाँको परास्त करके उसका सारा घन दिव्य अख्नोंकी वर्षा करने लगे। राजा युधिष्ठिस्ते बात-की-
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2005)
- **Original**: लिया तथा सुझमाँको परास्त करके उसका सारा घन दिव्य अख्नोंकी वर्षा करने लगे। राजा युधिष्ठिस्ते बात-की-
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2006)
- **Original**: छीन लिया। बातमें एक हजार योद्धाओंकों मार डाल्का, भीमसेनने सात
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2006)
- **Original**: छीन लिया। बातमें एक हजार योद्धाओंकों मार डाल्का, भीमसेनने सात
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2007)
- **Original**: भीमसेनके नीचे पड़ा हुआ सुझर्मा अपने प्राण बचानेके हजार त्रिगत्तॉंको घराझायी कर दिया तथा नकुलने सात सौ
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2007)
- **Original**: भीमसेनके नीचे पड़ा हुआ सुझर्मा अपने प्राण बचानेके हजार त्रिगत्तॉंको घराझायी कर दिया तथा नकुलने सात सौ
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2008)
- **Original**: लिये छठपटा रहा था। उसका सारा अंग धूलसे भर गया था और सहदेवने तीन सौ बीरोंकों नष्ट कर डाल्ा। और चेतना लुप्त-सी हो गयी थी। भीमसेनने उसे बाँधकर अन्तमें भीमसेन सुझमकि पास आये और अपने पैने
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2008)
- **Original**: लिये छठपटा रहा था। उसका सारा अंग धूलसे भर गया था और सहदेवने तीन सौ बीरोंकों नष्ट कर डाल्ा। और चेतना लुप्त-सी हो गयी थी। भीमसेनने उसे बाँधकर अन्तमें भीमसेन सुझमकि पास आये और अपने पैने
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2009)
- **Original**: अपने रथपर रख लिया और महाराज युथिप्ठिस्के पास ले बाणोंसे उसके घोड़ोंको तथा अड्भरक्षकोंकों मार झाल्म । फिर
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2009)
- **Original**: अपने रथपर रख लिया और महाराज युथिप्ठिस्के पास ले बाणोंसे उसके घोड़ोंको तथा अड्भरक्षकोंकों मार झाल्म । फिर
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2010)
- **Original**: जाकर उन्हें दिखाया। युध्िष्ठिर उसे देखकर हैसे और
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2010)
- **Original**: जाकर उन्हें दिखाया। युध्िष्ठिर उसे देखकर हैसे और
- **Translation**: 

---

