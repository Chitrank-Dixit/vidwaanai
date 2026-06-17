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

### Verse 1 (Vaivtpuran 17.974)
- **Original**: पूर्णत: पवित्र हो जाता है*। ब्रह्मन्‌! कर्मके + अपवित्र: पविष्रों वा सर्वावस्थां गतो5पि वा । यः स्मरेत्‌ पुण्डरीकाक्ष स बाह्याभ्यन्तर: शुचि:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.975)
- **Original**: (ब्रह्मखण्ड 17
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.976)
- **Original**: » खह्यस्वण्ड ड9 62424 82 4 ] 6 4 6 6
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.977)
- **Original**: 000 ]4]]00 0 (04
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.978)
- **Original**: 0 040।0440/।/4!4
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.979)
- **Original**: आरम्भ, मध्य और अन्तमें जो श्रीविष्णुका स्मरण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.980)
- **Original**: ईश्वरकी स्थिति है, तभीतक देहधारी जीव सब करता है, उसका वैदिक कर्म साज्जोपाड़ु पूर्ण हो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.981)
- **Original**: प्रकारके कर्म करनेमें समर्थ होता है। उन ईश्वर जाता है*। जगत्‌की सृष्टि करनेबाला मैं विधाता,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.982)
- **Original**: (या उनके अंशभूत जीव)-के निकल जानेपर संहारकारी हर तथा कर्मोके साक्षी धर्म-ये सब
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.983)
- **Original**: शरीर शब होकर अस्पृश्य एवं त्याज्य हो जाता जिनकी आज्ञाके परिपालक हैं, जिनके भय और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.984)
- **Original**: है। ऐसे सर्वेश्वर शिवकों कौन देहधारी नहीं आज्ञासे काल समस्त लोकोंका संहार करता है,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.985)
- **Original**: मानता? सबकी सृष्टि करनेवाले साक्षात्‌ जगत्‌- यम पापियोंको दण्ड देता है और मृत्यु सबको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.986)
- **Original**: विधाता ब्रह्मा निरन्तर उन भगवान्‌के चरणारविन्दोंका अपने अधिकारमें कर लेती है। सर्वेश्वरी, सर्वाद्या
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.987)
- **Original**: चिन्तन करते हैं, परंतु उनका दर्शन नहीं कर और सर्व॑जननी प्रकृति भी जिनके सामने भयभीत
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.988)
- **Original**: पाते। ब्रह्माजीने श्रीकृष्णकी प्रसन्नताके लिये जब रहती तथा जिनकी आज्ञाका पालन करती है। वे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.989)
- **Original**: एक लाख युगोंतक तप किया, तब इन्हें ज्ञान भगवान्‌ विष्णु ही सबके आत्मा और सर्वेश्वर हैं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.990)
- **Original**: प्रात हुआ और ये संसारकी सृष्टि करनेमें समर्थ मरहेश्वर बोले--ब्रह्मन्‌! ब्रह्माजीके जो सुप्रसिद्ध हुए। मैंने भी श्रीहरिकी आराधना करते हुए सुदीर्घ पुत्र हैं, उनमेंसे किसके वंशमें तुम्हारा जन्म हुआ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.991)
- **Original**: कालतक, जिसकी कोई गणना नहीं है, तप है? वेदोंका अध्ययन करके तुमने कौन-सा सार
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.992)
- **Original**: किया; परंतु मेरा मन नहीं भरा। भला, मड्गलकी तत्त्व जाना है? विप्रवर! तुम किस मुनीन्‍्द्रके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.993)
- **Original**: प्राप्तिति कौन तृत्त होता है? अब मैं समस्त कर्मोंसे शिष्य हो? और तुम्हारा नाम क्या है? तुम अभी
- **Translation**: 

---

