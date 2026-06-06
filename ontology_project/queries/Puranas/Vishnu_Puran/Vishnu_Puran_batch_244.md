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

### Verse 1 (Vishnu Puran 0.4861)
- **Original**: 18 इन्द्रप्रमितिरिकां तु संहितां स्वसुतं ततः:। माण्डकेय॑ महात्माने मैत्रेयाध्यापयत्तदा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4862)
- **Original**: 19 तस्य झिष्यप्रज्ञिष्येभ्य: पुत्नश्िष्यक्रमाहयौ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4863)
- **Original**: 20 भगवान्‌ कृष्णद्रैपायनको तुम साश्नात्‌ नाशयण हो समझो, क्योंकि हे मैत्रेथ ! संसारों नारायणके अतिस्क्ति और कौन महाभारतका सचयिता हो सकता हे 2?
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4864)
- **Original**: हे मैत्रेय ! द्वापरयुगर्मे मेरे पुत्र महात्मा कृष्णहैपायनने जिस प्रकार लेदोँका विभाग किया था यह यथायत सुनो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4865)
- **Original**: जब अह्माजीकी प्रेरणासे व्यासजीने बेदोंका विभाग करनेका उपक्रम फिया, तो उन्होंने येदका अन्ततक अध्यचन करनेगें समर्थ चार ऋषियोंको शिष्व बनाया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4866)
- **Original**: उनमेंसे उन महामुनिने पैलकों ऋग्ेद, खैद्वाम्मायनकों यजुर्वेद और जैमिनिकों सामत्रेद पढ़ाया तथा तन मसतिसान्‌ व्यासजीका सूमत्त्‌ु नामक शिक्य अथर्वशेदका ज्ञाता हुआ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4867)
- **Original**: इनके सिला सूतजातीय महाबुद्धिमान्‌ रोमहर्षणक्तो महामुनि व्यासजोने अपने इतिहास और पुयणके विद्यार्थरूपसे ग्रहण किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4868)
- **Original**: पूर्तकाल्में यजुर्वेद एक ही था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4869)
- **Original**: उसके उन्होंने चार विभाग किये, अनः उसमें चातुहत्रिकी प्रवति हुई और इस चातुर्हश्र-खिघिसे हो उन्होंने यज्ञानुष्ठानको ल्यतस्था की
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4870)
- **Original**: व्यासजीने यजुःसे अध्वर्युके, ऋकसे होताके, सामसे उद्ाताक तथा अथर्वचेदसे ब्रह्माके कर्मकी स्थापना की
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4871)
- **Original**: तदनन्तर उन्होंने ऋकू तथा यजु:श्रुतिवोंका उद्धार करके ऋग्वेट एवं यजुर्वेदकी और सामश्रुतियोंसे सामवेदकी रचना की
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4872)
- **Original**: हे मैत्रेय ! अश्चर्वत्रेदके द्वारा भगवान्‌ व्यासजीने सम्पूर्ण राज-कर्म और बद्यत्ककी यथावत्‌ व्यवस्था कौ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4873)
- **Original**: इस प्रकार व्यासजीने खेटरूप एक वक्षके चप्र विभाग कर टिये फिर विभक्त हुए उन चारोंसे बेदरूपों वक्षोंका वन उत्पन्न हुआ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4874)
- **Original**: 15। हे ब्िप्र ! पहले पैलने अऋग्वेदरूप वृक्षके दो विभाग क्रिये और तन दोनों शास्त्राऑकफो अपने शिष्य इन्‍्द्रप्रसिति और ब्ाष्कलको पढ़ाया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4875)
- **Original**: फिर बाष्कलने भी अपनी शास्त्राके चार भाग किये और उन्हें बोध्य आदि अपने शिष्योंकों दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4876)
- **Original**: हे सुने ! खाष्कल्कों ज्ञाखाको उन चारों प्रतिशाखाओँको उनके दिष्य बोध्य, आप्रिमाढक, याज्ञवल्क्यथय और पयदारने ग्रहण किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4877)
- **Original**: हे मैत्रेयजी ! इन्द्रप्रमतिने अपनों प्रतिशाखाको अपने पुत्र महात्मा माण्डकेयकों पढ़ाया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4878)
- **Original**: इस प्रकार दिष्य-प्रशिष्य-क्रमसे उस शास्त्ाका डनके पुत्र और शअिष्योमें प्रचार हुआ । इस
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4879)
- **Original**: 1्छढ बेदमित्रस्तु शाकल्य: संहितां तामधीतवान्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4880)
- **Original**: चकार संहिता: पञ्च शिष्येभ्य: प्रददौ च ता:
- **Translation**: 

---

