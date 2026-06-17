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

### Verse 1 (Bramha 0.7741)
- **Original**: प्रतिवर्ष अपने घर आये हुए ब्राह्मणोंका वैभवके पूर्व या उत्ततकी ओर मुँह करके क्षौर कराये। उत्तम
- **Translation**: 

---

### Verse 2 (Bramha 0.7742)
- **Original**: अनुसार स्वागत-सत्कार करे। कुलमें उत्पन्न होनेपर भी जो कन्या किसी अड्से अपने घरमें यथाल्थान देवताओंका भलीभाँति होन या रोगिणी हो, उसके साथ विवाह न करे।
- **Translation**: 

---

### Verse 3 (Bramha 0.7743)
- **Original**: पूजन करके क्रमश: अग्रिमें आहुति दे। पहली ईर्ष्याका परित्याग करे। दिनमें शबन अथवा मैथुन
- **Translation**: 

---

### Verse 4 (Bramha 0.7744)
- **Original**: आहुति ब्रह्माको, दूसरी प्रजापतिको, तीसरी गृह्याओंको, न करे। दूसरोंको कष्ट देनेवाला कार्य न करें। कभी
- **Translation**: 

---

### Verse 5 (Bramha 0.7745)
- **Original**: चौथी कश्यपको तथा पाँचवीं अनुमतिको दे। किसी भी जीवको पीड़ा न दे। रजस्वला स्त्री चार
- **Translation**: 

---

### Verse 6 (Bramha 0.7746)
- **Original**: तत्पश्चात्‌ बलिवैश्वदेव करे। देवताओंकि लिये पृथक्‌- रातोतक सभी वर्णके पुरुषोंके लिये त्याज्य है। यदि
- **Translation**: 

---

### Verse 7 (Bramha 0.7747)
- **Original**: धृथक्‌ स्थानका विभाग करके उनके लिये बलि कन्याका जन्म अभीष्ट न हो तो उसे ग्रेकनेके लिये
- **Translation**: 

---

### Verse 8 (Bramha 0.7748)
- **Original**: अर्पण करे। उसका क्रम इस प्रकार है। एक पात्रमें पाँक्‍वीं रातमें भी स्त्रीसहवास न करें। छठी रात
- **Translation**: 

---

### Verse 9 (Bramha 0.7749)
- **Original**: पहले पर्जन्य, जल और पृथ्वीको तीन बलियाँ दे; आनेपर स्त्रीके पास जाय, क्योंकि युग्म रात्रियाँ हो
- **Translation**: 

---

### Verse 10 (Bramha 0.7750)
- **Original**: फिर पूर्व आदि प्रत्येक दिशामें वायुको बलि देकर इसके लिये श्रेष्ठ हैं। युग्म रात्रियॉमें स्त्रीसहवास
- **Translation**: 

---

### Verse 11 (Bramha 0.7751)
- **Original**: क्रमश: उन-उन दिशाओँके नामसे भी बलि समर्पित करनेसे पुत्र होता है और अयुग्म रात्रियोंमें गर्भाधान
- **Translation**: 

---

### Verse 12 (Bramha 0.7752)
- **Original**: करे। तत्पश्चात्‌ मध्यमें क्रमश: ब्रह्मा, अन्तरिक्ष और करनेसे कन्या उत्पन्न होती है। पर्व आदिके
- **Translation**: 

---

### Verse 13 (Bramha 0.7753)
- **Original**: सूर्यको बलि दे। उनके उत्तरभागमें विश्वेदेवों और अवसरपर मैथुन करनेसे विधर्मी संतान होती है
- **Translation**: 

---

### Verse 14 (Bramha 0.7754)
- **Original**: विश्वभूतॉंकों बलि दे फिर उनके भी उत्तरभागमें और संध्याकालमें गर्भाधान करनेसे नपुंसक उत्पन्न
- **Translation**: 

---

### Verse 15 (Bramha 0.7755)
- **Original**: उपा और भूतपतिको बलि समर्पित करें। तदनन्तर होते हैं। विद्वान्‌ पुरुष क्षौरकर्ममें रिक्ना (चतुर्थी,
- **Translation**: 

---

### Verse 16 (Bramha 0.7756)
- **Original**: 'पितृभ्यः स्वधा नमः” यों कहकर दक्षिण दिशामें नवमी और चतुर्दशी) तिथियोंका परित्याग कर अपसब्य होकर पितरोंके लिये बलि दे और वायब्य विनयरहित उद्दण्ड पुरुषोंकी बात क्रभी न सुने। जो
- **Translation**: 

---

### Verse 17 (Bramha 0.7757)
- **Original**: दिशामें अन्नका शेष भाग तथा जल लेकर 'यश्ष्मैत्ते अपनेसे नीचा हो, उसे आदरपूर्वक ऊँचा आसन न
- **Translation**: 

---

### Verse 18 (Bramha 0.7758)
- **Original**: निर्णेजनम्‌” यह मन्त्र पढ़कर उसे विधिपूर्वक छोड़ दे। हजामत बनवाने, बमन होने, स्त्री-प्रसद्भ करने
- **Translation**: 

---

### Verse 19 (Bramha 0.7759)
- **Original**: दे। फिर देवताओं और ब्राह्मणोंकों नमस्कार करे। तथा श्मशानभूमिमें जानेपर वस्त्रसहित स्नान करें।
- **Translation**: 

---

### Verse 20 (Bramha 0.7760)
- **Original**: दाहिने हाथमें अँगूठेके उत्तर ओर जो एक रेखा देवता, वेद, द्विज, साधु, सच्चे महात्मा, गुरु,
- **Translation**: 

---

