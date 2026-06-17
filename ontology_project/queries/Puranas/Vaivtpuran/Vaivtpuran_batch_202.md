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

### Verse 1 (Vaivtpuran 13.10182)
- **Original**: ड58 * संक्षिप्त ग्रह्मवैयर्तपुराण « भड़क ऋकऋ 45 अं कड कक क 4 कक #अ अर क कक कद अ 5 कद कक कक पक कक ऋ ऋ कक कक कक क ड़ 25 क अर 4484 8# 88 8 आपका दिया हुआ यह धन भी नहीं लूँगा। मुझ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10183)
- **Original**: मनसे अपने-अपने घरोंको गये। समस्त बन्दीजन अनुरागी सेवकको अपने चरणकमलॉंकी सेवामें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10184)
- **Original**: भी पूर्णमनोरथ होकर अपने घरको लौट गये। उन रख लीजिये।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10185)
- **Original**: सबको मीठे पदार्थ, वस्त्र, उत्तम श्रेणीके अश्व इस प्रकार स्तुति करके गर्गजी नेत्रॉसे आँसू तथा सोनेके आभूषण प्राप्त हुए थे। आकण्ठ बहाते हुए श्रोहरिके चरणोंमें गिर पड़े और जोर-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10186)
- **Original**: भोजन करके तृप्त हुए भिक्षुकगण बड़ी प्रसन्नताके जोरसे रोने लगे। उस समय भक्तिके उद्रेकसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10187)
- **Original**: साथ अपने घरको लौटे। वे सुवर्ण और वस्त्रोंके उनके शरीरमें रोमाझ्ष हो आया था। गर्गजीकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10188)
- **Original**: भारी भारसे धककर चलनेमें असमर्थ हो गये थे। बात सुनकर भक्तवत्सल श्रीकृष्ण हँस पड़े और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10189)
- **Original**: कोई धीरे-धीरे चलते, कोई विश्रामके लिये बोले--' मुझमें तुम्हारा अविचल भक्ति हो।'
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10190)
- **Original**: धरतीपर सो जाते और कुछ लोग मार्गमें उठते- जो मनुष्य गर्गजीद्वारा किये गये इस स्तोत्रका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10191)
- **Original**: बैठते जाते थे। कोई वहाँ सानन्द हँसते हुए टिक तीनों संध्याओंके समय पाठ करता है, वह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10192)
- **Original**: जाते थे। कपर्दकों तथा अन्य वस्तुओंके जो श्रीहरिकी सृदृढ़ भक्ति, दास्यभाव और उनकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10193)
- **Original**: बहुत-से शेष भाग बच गये थे, उन्हें कुछ लोग स्मृतिका सौभाग्य अवश्य प्राम्त कर लेता है। इतना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10194)
- **Original**: ले लेते थे। कुछ लोग खड़े हो दूसरोंको वे वस्तुएँ हो नहीं, वह श्रीकृष्णभक्तोंकी सेवामें तत्पर हो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10195)
- **Original**: दिखाते थे। कुछ लोग नृत्य करते थे और कितने जन्म, मृत्यु, जगा, रोग, शोक और मोह आदिके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10196)
- **Original**: ही लोग वहाँ गीत गाते थे। कोई नाना प्रकारकी संकटसे पार हो जाता है। श्रीकृष्णके साथ रहकर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10197)
- **Original**: प्राचीन गाथाएँ कहते थे। राजा मरुत्त, श्वेत, सगर, सदा आनन्द भोगता है और श्रीहरिसे कभी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10198)
- **Original**: मान्धाता, उत्तानपाद, नहुष और नल आदिकी जो उसका वियोग नहीं होता। कथाएँ हैं, उन्हें सुनाते थे। श्रीरामके अश्वमेधयज्ञकी भगवान्‌ नारायण कहते हैं--नारद ! श्रोहरिकी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10199)
- **Original**: तथा राजा रन्तिदेवके दान-कर्मकी भी गाथाएँ गाते इस प्रकार स्तुति करके गर्गमुनिने उन्हें नन्दजीको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10200)
- **Original**: थे। कोई ठहर-ठहरकर और कोई सो-सोकर दे दिया और प्रशंसापूर्वक कहा--'गोपराज ! अब
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10201)
- **Original**: यात्रा करते थे। इस प्रकार सब लोग प्रसन्नतापूर्वक मैं घर जाता हूँ, आज्ञा दो। अहो! कैसी विचित्र
- **Translation**: 

---

