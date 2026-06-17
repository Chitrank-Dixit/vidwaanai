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

### Verse 1 (Mahabharat 0.341)
- **Original**: बशमें हैं, शहु उसकी कुछ भी हानि नहीं कर सकते।' $ स्वीकार करता है, वह स्याहीके बिलमें पुसकर आगसे बच
- **Translation**: 

---

### Verse 2 (Mahabharat 0.341)
- **Original**: बशमें हैं, शहु उसकी कुछ भी हानि नहीं कर सकते।' $ स्वीकार करता है, वह स्याहीके बिलमें पुसकर आगसे बच
- **Translation**: 

---

### Verse 3 (Mahabharat 0.342)
- **Original**: विदुरका संकेत सुनकर युथिष्ठिरते कहा, “मैंने आपकी आात जाता है। घूमने-फिरनेसे रास्तेका ज्ञान हो जाता है।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.342)
- **Original**: विदुरका संकेत सुनकर युथिष्ठिरते कहा, “मैंने आपकी आात जाता है। घूमने-फिरनेसे रास्तेका ज्ञान हो जाता है।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.343)
- **Original**: भलीभाँति समझ लकी।' बिदुर हस्तिनापुर लौट आये यह नक्षत्रोंसे दिशाका पता छूण जाता है। जिसकी पाँचों इच्धियाँ
- **Translation**: 

---

### Verse 6 (Mahabharat 0.343)
- **Original**: भलीभाँति समझ लकी।' बिदुर हस्तिनापुर लौट आये यह नक्षत्रोंसे दिशाका पता छूण जाता है। जिसकी पाँचों इच्धियाँ
- **Translation**: 

---

### Verse 7 (Mahabharat 0.344)
- **Original**: घटना फाल्गुन झुक्क अष्टमी, रोहिणी नक्षत्रकी है। व पाण्डबोंका लाक्षागृहमें रहना, सुरड्रका खोदा जाना और आग छगाकर निकल-भाग़ना वैज्ण्पायमजी कहते. हैं--जनमेजय ! . पाण्डबोंके
- **Translation**: 

---

### Verse 8 (Mahabharat 0.344)
- **Original**: घटना फाल्गुन झुक्क अष्टमी, रोहिणी नक्षत्रकी है। व पाण्डबोंका लाक्षागृहमें रहना, सुरड्रका खोदा जाना और आग छगाकर निकल-भाग़ना वैज्ण्पायमजी कहते. हैं--जनमेजय ! . पाण्डबोंके
- **Translation**: 

---

### Verse 9 (Mahabharat 0.345)
- **Original**: लिये नियत वासस्थानपर आदंस्के साथ उन्हें ठहराया और आुुंधागमनका समाचार सुनकर वारणावतके नागरिक
- **Translation**: 

---

### Verse 10 (Mahabharat 0.345)
- **Original**: लिये नियत वासस्थानपर आदंस्के साथ उन्हें ठहराया और आुुंधागमनका समाचार सुनकर वारणावतके नागरिक
- **Translation**: 

---

### Verse 11 (Mahabharat 0.346)
- **Original**: भोजन, पलंग, आसन आदि सामग्रियोंसे उन्हें सन्तुष्ठ करनेकी झाख-विधिके अनुसार मड्डलूमयी वस्तुओंकी घेंट लेकर
- **Translation**: 

---

### Verse 12 (Mahabharat 0.346)
- **Original**: भोजन, पलंग, आसन आदि सामग्रियोंसे उन्हें सन्तुष्ठ करनेकी झाख-विधिके अनुसार मड्डलूमयी वस्तुओंकी घेंट लेकर
- **Translation**: 

---

### Verse 13 (Mahabharat 0.347)
- **Original**: चेश्ना को। पाण्छबलोग सुखपूर्वक वहाँ रहने रगे। प्रसन्नता और उत्साहके साथ सवारियोपर खढ़कर उनकी
- **Translation**: 

---

### Verse 14 (Mahabharat 0.347)
- **Original**: चेश्ना को। पाण्छबलोग सुखपूर्वक वहाँ रहने रगे। प्रसन्नता और उत्साहके साथ सवारियोपर खढ़कर उनकी
- **Translation**: 

---

### Verse 15 (Mahabharat 0.348)
- **Original**: युरवासियोंकी- भीड़ प्रायः लगी ही रहती। दस दिन बीत अंगवानीके लिये आये। उनके जय-जयकार और मड्ल-
- **Translation**: 

---

### Verse 16 (Mahabharat 0.348)
- **Original**: युरवासियोंकी- भीड़ प्रायः लगी ही रहती। दस दिन बीत अंगवानीके लिये आये। उनके जय-जयकार और मड्ल-
- **Translation**: 

---

### Verse 17 (Mahabharat 0.349)
- **Original**: जानेपर पुरोचनने पाण्डवॉले उस सुन्दर नामवाले किन्तु ध्वनिसे दिशाएँ गूँज उठीं। पुरवासियोंके बीचमें युथिष्ठिर ऐसे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.349)
- **Original**: जानेपर पुरोचनने पाण्डवॉले उस सुन्दर नामवाले किन्तु ध्वनिसे दिशाएँ गूँज उठीं। पुरवासियोंके बीचमें युथिष्ठिर ऐसे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.350)
- **Original**: अपड्डलल भवनकी चर्चा की। उसकी ग्रेरणासे पाण्डव जान पड़ते थे मानो स्वयं देवराज इत्र हों। स्वागत
- **Translation**: 

---

### Verse 20 (Mahabharat 0.350)
- **Original**: अपड्डलल भवनकी चर्चा की। उसकी ग्रेरणासे पाण्डव जान पड़ते थे मानो स्वयं देवराज इत्र हों। स्वागत
- **Translation**: 

---

