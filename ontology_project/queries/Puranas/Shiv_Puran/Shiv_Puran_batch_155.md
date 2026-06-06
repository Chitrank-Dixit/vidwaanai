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

### Verse 1 (Shiv Puran 0.3081)
- **Original**: 10427 लौकिक ब्राह्मण, क्षत्रिय, चैशय वेदबेदाड्रोंके तत्वज्ञ विद्वान, सर्वज्ञासत्रकुत्क, वैशेषिक, थोगजञाख्के आचार्य तैयायिक, सुर्योपासक, त्रह्मोपासक, दौव वैष्णव तथा अन्य सब शिष्ट और विज्रिष्ठ पुरुष शिवकी आज्ञाके अधीन हो मेरे इस कर्मको अधीष्ट-साधक मानें
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.3082)
- **Original**: 670--172
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.3083)
- **Original**: ज्ौवा: सिद्धाक्तपार्गस्था: रैया: पाञुपतालतथा । जीव महाय्तघरा: दौता: कापालिका: परे
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.3084)
- **Original**: 17झ्मा शिवाज्ञापालूकाः पूज्या ममापि दिव्द्यासयात्‌। सतें सामनृप्हृणतु झंससु सफलब्रिपाम्‌
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.3085)
- **Original**: 1छडा जीब--थे सब-के-सल शिवकी आज्ञाके पालक तथा मेरे भी पुज्य हैं। अतः जझिवकी आज्ञासे इन सबका मुझपर अनुग्रह हो और ये इस कार्यकों सफत्ड घोषित करें
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.3086)
- **Original**: 273-1574
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.3087)
- **Original**: - दक्षिणज्ञाननिष्ठाक्ष दक्षिणोत्तरमार्गगा: । अधिरोधेन वर्तत्तं घन्त्रे श्रेयो्थिनों मम
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.3088)
- **Original**: जो दक्षिणाचारके ज्ञानमें परिनिष्ठ तथा दक्षिणाचारके उत्कृष्ट पार्गपर चरूनेवाले हैं, वे परस्पर विरोध न रखते हुए मत्बनका जप करें और पेरे कल्याणकामी हों
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.3089)
- **Original**: # नास्तिकाश जशठधैव कृतप्राल्व तामसा:। पापण्टाक्नातिफफाश॒सर्तन्तों. टूरतो. मम
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.3090)
- **Original**: 176आ बहु: कि स्तुतैरत्र येठपि केउपि चिदास्तिकाः । सर्चें मामनुगृहणत्तु सब्तः इसत्तु मजजलम्‌
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.3091)
- **Original**: चास्तिक, द्राठ, कुतप्ा, तामस, पाखण्डी और अति पापी प्राणी मुझसे दूर ही रहें। यहाँ बहुतोंकी स्तुतिसे क्या छाभ ? जो आज्ञीर्वाद दें
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.3092)
- **Original**: ₹76-977
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.3093)
- **Original**: नमः शिवाय श्राम्याय ससुतायादिहेतरों। घ से
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.3094)
- **Original**: नमस्कार है
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.3095)
- **Original**: इत्युक्त्वा टण्डयद्‌ भूम्पी प्रशिपत्य शिव सियाम्‌ जपेत्पक दरों बिद्यागप्रोत्तशतावशप्‌
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.3096)
- **Original**: 6794 तथैय शाक्तिवियां व जपित्था तत्समर्पणम्‌। कृत्य ते क्षमयिस्वेद्दं पूजाशेष समापयेत्‌ #180
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.3097)
- **Original**: ऐसा कहकर झिलव और शज्िवाके उद्देश्यसे भूधिषर दण्डकी भाँति गिरकर अ्रणाम करे और कम-से-कम एक सौ आठ बार पप्चाक्षरी विद्याका जप करें। इसी
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.3098)
- **Original**: छ88 + कक ##है+5*4%%*कजे कं जले कक 30474 अक़औक क ह 3 कै है &# # $ ?# कक है ++$ 34000 0 कक तट 3 0 2007 3 व क कक अकार जक्तिविद्ञा (ओं गमः शिवाय) का जप करके उसका समर्पण करे और महादेवजीसे क्षमा माँगकर शेष पूजाकी समाप्ति करें
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.3099)
- **Original**: 179-180
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.3100)
- **Original**: एतत्पुण्यत्म॑. स्तोर्ष हिश्रयोहंदयंगमम्‌। सर्वाभीष्ठप्रद. साखार्ःत्तिमुकततेकसाघनम्‌
- **Translation**: 

---

