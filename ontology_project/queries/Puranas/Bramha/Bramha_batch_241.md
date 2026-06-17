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

### Verse 1 (Bramha 0.4801)
- **Original**: पवित्र भावसे गौतमीके तटपर गया और वहाँ स्नान दुःखसे कहा--मैं शुनःशेपका पिता हूँ। भारी ' करके भगवान्‌ दिष्णु और शिवका स्मरण करते हे 8 ' पण्यः श7]
- **Translation**: 

---

### Verse 2 (Bramha 0.4802)
- **Original**: हुए उसने प्रेतरूपी दुःखी पिताको जल दिया। 24/25/7744
- **Translation**: 

---

### Verse 3 (Bramha 0.4803)
- **Original**: जलाञलि देते ही अजीगर्तिने पत्रित्र होकर परम 003// (66-78 पुण्यमय दिव्य शरीर धारण कर लिया और 58 222 कह बे ः तेजस्वी रूप धारण करके बैकुण्ठधाममें रहते 84645 हे, *
- **Translation**: 

---

### Verse 4 (Bramha 0.4804)
- **Original**: लगे। तबसे यह स्थान पैशाचनाशनतीर्थके नामसे
- **Translation**: 

---

### Verse 5 (Bramha 0.4805)
- **Original**: प्रसिद्ध हुआ। उसके स्मरणमात्रसे मनुष्योंके बड़े- मे
- **Translation**: 

---

### Verse 6 (Bramha 0.4806)
- **Original**: बड़े पाप नष्ट हो जाते हैं। नारद! इस प्रकार मैंने
- **Translation**: 

---

### Verse 7 (Bramha 0.4807)
- **Original**: तुमसे इस तोर्थका माहात्म्य सुनाया। यहाँ और भी तीन सौ तोर्थ हैं, जो भोग और मोक्ष प्रदान >> 208 आप 3
- **Translation**: 

---

### Verse 8 (Bramha 0.4808)
- **Original**: . निम्नभेद नामक तीर्थ सब पापोंका नाश करनेवाला पापकर्म करके भयानक प्रेतयोनिमें पड़ा हूँ। पहले
- **Translation**: 

---

### Verse 9 (Bramha 0.4809)
- **Original**: है। बह गड्भाके उत्त-तटपर है। उसकी प्रसिद्धि तो यारंबार नरकोंमें यातनाएँ सहता रहा और अब । तीनों लोकोंमें है। उसके स्मरणमात्रसे सम्पूर्ण प्रेठयोनिको प्रात हुआ हूँ। जो-जो पापकर्म करनेवाले
- **Translation**: 

---

### Verse 10 (Bramha 0.4810)
- **Original**: पापोंका क्षय हो जाता है। वहीं बेदद्वीप है। उसके हैं, उन सबकी यही गति होती है।' यह सुनकर
- **Translation**: 

---

### Verse 11 (Bramha 0.4811)
- **Original**: दर्शनसे मनुष्य वेदोंका विद्वान होता है। एक अजीगर्तिके पुत्रकों बड़ा दुःख हुआ। उसने
- **Translation**: 

---

### Verse 12 (Bramha 0.4812)
- **Original**: समयकी बात है-परम धर्मात्मा राजा पुरूरवाने कहा--' पिताजी ! मैं हो आपका पुत्र शुनःशेप हूँ।
- **Translation**: 

---

### Verse 13 (Bramha 0.4813)
- **Original**: उर्वशी नामक अप्सराकी कामना की। मादक दस आम आपको पा डकार गररकआ
- **Translation**: 

---

### Verse 14 (Bramha 0.4814)
- **Original**: जय मजा ही सबक पका डक सकी कारण प्रकार आना डुता। उर्व स्थानपर गयी। पड़ा है। अब मैं आपको स्वर्गमें पहुँचाऊँगा।'
- **Translation**: 

---

### Verse 15 (Bramha 0.4815)
- **Original**: राजासे यह शर्त की कि मैं जबतक आपको नग्न ऐसी प्रतिज्ञा करके उसने गड्भजाजीका चिन्तन किया
- **Translation**: 

---

### Verse 16 (Bramha 0.4816)
- **Original**: न देखूँ, तभीतक आपके पास रह सकती हूँ। और पिताकों उत्तम लोक प्राप्त कग़नेकी चेष्टामें । उसके रहनेकी यह अवधि स्वीकार करके राजाने
- **Translation**: 

---

### Verse 17 (Bramha 0.4817)
- **Original**: » परुष्णीतीर्थ, नारसिंहतीर्थ, पैशाचताज्नतीर्थ और शद्भुहद तीर्थकी महिमा * 235 उस रमणीया अप्सराकों ग्रहण किया। एक दिन
- **Translation**: 

---

### Verse 18 (Bramha 0.4818)
- **Original**: आराधना करने लगे । जो बिपत्तिमें पड़नेपर तीर्थों जब यह पलंगपर सोयी हुई थी, राजा पुरूरवा
- **Translation**: 

---

### Verse 19 (Bramha 0.4819)
- **Original**: और देवताओंका सेवन नहीं करता, बह कालके उठे। उसी समय उन्हें नग्र देखकर उर्वशी बहाँसे
- **Translation**: 

---

### Verse 20 (Bramha 0.4820)
- **Original**: बशमें पड़ा हुआ जीव किस दशाको प्राप्त होगा। चली गयी। उसके जानेसे राजाको बड़ा दुःख
- **Translation**: 

---

