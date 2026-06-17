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

### Verse 1 (Bavishya Puran 0.41)
- **Original**: कदाथ्िद॒पि ये पुण्यां न शण्यन्ति कथा नराः।ते भुकक्‍त्वा नस्‍्कान्‌ घोरान्‌ भवन्ति वनसूकराः
- **Translation**: 

---

### Verse 2 (Bavishya Puran 0.42)
- **Original**: ये कथामनुमोदले कौीर्यमानों नशेत्तमा:
- **Translation**: 

---

### Verse 3 (Bavishya Puran 0.43)
- **Original**: अधृण्वन्तोषपि ते यात्ति शाश्र॒ते परम पदम
- **Translation**: 

---

### Verse 4 (Bavishya Puran 0.44)
- **Original**: कथायां कीरच्यपघानायां लिप कुर्वत्ति ये शठाः
- **Translation**: 

---

### Verse 5 (Bavishya Puran 0.45)
- **Original**: कोट्यब्द नरकान्‌ भुक्त्वा भवन्ति आमसूकरां:
- **Translation**: 

---

### Verse 6 (Bavishya Puran 0.46)
- **Original**: ये आवयब्ति मनुजान्‌ पुण्यां पौराणिकी कथाम्‌। कल्पकोटिशते साग्र॑ तिए्ठन्ति ब्रह्मण: पढे
- **Translation**: 

---

### Verse 7 (Bavishya Puran 0.47)
- **Original**: आसतनार्थ प्रयच्छन्ति पुराणज्ञस्थय ये नराः
- **Translation**: 

---

### Verse 8 (Bavishya Puran 0.48)
- **Original**: कम्बलाजिनसासांसि मछे फल्कपेव छ
- **Translation**: 

---

### Verse 9 (Bavishya Puran 0.49)
- **Original**: स्वर्गलोक॑ समासाह्य भुवल्वा भोगान्‌ यथेप्सितान्‌
- **Translation**: 

---

### Verse 10 (Bavishya Puran 0.50)
- **Original**: स्थित्वा ब्रह्मादिस्लोकेषु प्॑यान्ति निरामयम्‌
- **Translation**: 

---

### Verse 11 (Bavishya Puran 0.51)
- **Original**: इसी प्रकार ज़ो वक्ताके समान आसनपर बैठकर कथा सुनता है, बह गुरू-शय्या-गमनके समान पापका भागी होकर नस्कगामी होता है। जो मनुष्य पुराणोंके ज्ञाता (व्यास) और पापोंको हरण करनेवाली कथाकी निन्‍दा करते हैं, ये सौ जन्मोतक सूकर-योनिमें उत्पन्न होते हैं। जो मनुष्य इस पुण्य कथाकों कभी भी नहीं सुनते, ये घोर नरकॉका भोग करके वनैले सूअर होते हैं। जो नरश्रेष
- **Translation**: 

---

### Verse 12 (Bavishya Puran 0.52)
- **Original**: ्ठ कही जाती हुई कथाका अनुमोदन करते हैं, वे कथा न सुननेपर भी अविनाझ्ञी परम पदको प्राप्त होते हैं। जो दुष्ट कही जाती हुई कथामें विन्न पैदा करते हैं, ये करोड़ों वर्षोंतक नस्वो्रेंका भोग करके अन्तपें ग्रामीण सूअर होते हैं। जो ल्त्रेग साधारण मनुष्योंको पुराणसम्बन्धी पुण्य कथा सुनाते हैं, वे सौ करोड़ कल्पोंसे भी अधिक समयतक ब्रह्मस्म्रेकमें निवास
- **Translation**: 

---

### Verse 13 (Bavishya Puran 0.53)
- **Original**: + पुराण- महिमा « 5 करते है। जो मनुष्य पुराणके ज्ञाता वक्ताको आसनके लिये कम्बल, मृगचर्म, वस्र, सिंहसन और चौकी प्रदान करते हैं, वे खर्गस्थ्रेकमें जाकर अभीष्ठ भोगोंका उपभोग करनेके बाद बह आदिके ल्तेकॉरमें निवास कर अन्तमें निरामय पदको प्राप्त होते हैं। पुराणस्थ प्रयर्कन्ति ये यरासनमुत्तमम्‌ । भोगिनो ज्ञानसम्पन्ना भवन्ति त् भवे भले
- **Translation**: 

---

### Verse 14 (Bavishya Puran 0.54)
- **Original**: ये महापातकैर्युक्ता उपपातकिनश्ष ये
- **Translation**: 

---

### Verse 15 (Bavishya Puran 0.55)
- **Original**: पुराणभ्रवणादेव ते प्रयान्ति पर॑ पदम्‌
- **Translation**: 

---

### Verse 16 (Bavishya Puran 0.56)
- **Original**: एवंविधविधानेन पुराण श्ृणुयान्नरः । भुक्त्वा भोगान्‌ यथाकार्म किष्णुल्मेक॑ प्रयाति सः
- **Translation**: 

---

### Verse 17 (Bavishya Puran 0.57)
- **Original**: पुस्तक पूजयेत्‌ पश्चाद्‌. वख्चारंकरणादिभिः । वाचयक॑. विप्रसंयुक्ते. पूजयीत ग्रयत्रवान्‌
- **Translation**: 

---

### Verse 18 (Bavishya Puran 0.58)
- **Original**: गोभूमिहेमवज्लाणि._ वाचकाय निवेदयेत्‌
- **Translation**: 

---

### Verse 19 (Bavishya Puran 0.59)
- **Original**: ग्राहमणान्‌.. भोजयेत्‌. पश्चान्पप्डलडडुकपायसै:
- **Translation**: 

---

### Verse 20 (Bavishya Puran 0.60)
- **Original**: त॑व॑व्यासरपी भगवन्‌ बुद्धघा चाड्मिससोपमः
- **Translation**: 

---

