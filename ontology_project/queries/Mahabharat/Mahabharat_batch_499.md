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

### Verse 1 (Mahabharat 0.4981)
- **Original**: बढ़ाया। थे रथ्षपर बैठे-ही-अैठे खारों ओर खड़ी हुई उसकी छातीमें नौ बाणोंका प्रहार किया। फिर क्रोधमें पाण्डव-सेनाको धीरज बैंधाते जाते थे। वीरबर अर्जुन भरकर भीमको भी तीस बाणोंसे घायक किया। एक
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4981)
- **Original**: बढ़ाया। थे रथ्षपर बैठे-ही-अैठे खारों ओर खड़ी हुई उसकी छातीमें नौ बाणोंका प्रहार किया। फिर क्रोधमें पाण्डव-सेनाको धीरज बैंधाते जाते थे। वीरबर अर्जुन भरकर भीमको भी तीस बाणोंसे घायक किया। एक
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4982)
- **Original**: आपकी सेनाको परास्त करते हुए आगे बढ़ रहे थे। श्वेत भललसे सहदेवकी ध्वजा काटकर तीन बाणोंसे उसके
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4982)
- **Original**: आपकी सेनाको परास्त करते हुए आगे बढ़ रहे थे। श्वेत भललसे सहदेवकी ध्वजा काटकर तीन बाणोंसे उसके
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4983)
- **Original**: घोड़ेवाले रथपर बैठकर अपने सारथि भगवान्‌ कृष्णके साथ सारथ्षिको भी मार डाला तथा ड्रौपदीके पुत्रोंको रथहीन
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4983)
- **Original**: घोड़ेवाले रथपर बैठकर अपने सारथि भगवान्‌ कृष्णके साथ सारथ्षिको भी मार डाला तथा ड्रौपदीके पुत्रोंको रथहीन
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4984)
- **Original**: अर्जुनको आते देख मद्रराज झल्यने कर्णसे कहा--'कर्ण ! कर दिया। यह सारा काम पलक मास्ते-मारते हो गया।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4984)
- **Original**: अर्जुनको आते देख मद्रराज झल्यने कर्णसे कहा--'कर्ण ! कर दिया। यह सारा काम पलक मास्ते-मारते हो गया।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4985)
- **Original**: तुम दूसरे ल्थोेगोंसे जिनका पता पूछते फिरते थे, ये कुन्तीनन्दन देखनेबालोंके लिये यह बड़े आक्षर्यकी बात हुई। महारथी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4985)
- **Original**: तुम दूसरे ल्थोेगोंसे जिनका पता पूछते फिरते थे, ये कुन्तीनन्दन देखनेबालोंके लिये यह बड़े आक्षर्यकी बात हुई। महारथी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4986)
- **Original**: अर्जुन अपना गाष्डीब धनुष लिये हुए सामने खड़े हैं, वह कर्णने चेदि तथा मल्य देझके योद्धाओको भी अपने
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4986)
- **Original**: अर्जुन अपना गाष्डीब धनुष लिये हुए सामने खड़े हैं, वह कर्णने चेदि तथा मल्य देझके योद्धाओको भी अपने
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4987)
- **Original**: उनका रथ आ रहा है। यदि आज उन्हें मार डाल्प्रेगे तो तीखे तीरोंका निञ्चाना बनाया। उसकी मार खाकर वे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4987)
- **Original**: उनका रथ आ रहा है। यदि आज उन्हें मार डाल्प्रेगे तो तीखे तीरोंका निञ्चाना बनाया। उसकी मार खाकर वे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4988)
- **Original**: हमत्झोगोंका भल्म होगा। अर्जुनके धनुषकी प्रत्यक्षामें चन्द्रमा भंयधीत होकर भाग चले । कर्णका यह अद्भुत पराक्रम मैंने
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4988)
- **Original**: हमत्झोगोंका भल्म होगा। अर्जुनके धनुषकी प्रत्यक्षामें चन्द्रमा भंयधीत होकर भाग चले । कर्णका यह अद्भुत पराक्रम मैंने
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4989)
- **Original**: एवं ताराओंके चिड्ढ हैं, उनकी ध्वजाके झिखरपर भयंकर अपनी आँखों देखा था। जैसे भेड़िया पशुओंको भयभीत
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4989)
- **Original**: एवं ताराओंके चिड्ढ हैं, उनकी ध्वजाके झिखरपर भयंकर अपनी आँखों देखा था। जैसे भेड़िया पशुओंको भयभीत
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4990)
- **Original**: वानर दिखायी पड़ता है, जो चारों ओर ताक-ताककर करके भगा देता है, उसी प्रकार कर्णने पाष्डव-योद्धाको
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4990)
- **Original**: वानर दिखायी पड़ता है, जो चारों ओर ताक-ताककर करके भगा देता है, उसी प्रकार कर्णने पाष्डव-योद्धाको
- **Translation**: 

---

