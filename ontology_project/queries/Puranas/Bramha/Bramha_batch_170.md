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

### Verse 1 (Bramha 0.3381)
- **Original**: नामक देशको प्रस्थान किया। वहाँ पहुँचकर चिन्तन करने, वहाँ जाने और भक्तिपूर्वक उसका
- **Translation**: 

---

### Verse 2 (Bramha 0.3382)
- **Original**: उसने घोड़ीका रूप धारण करके कठोर तपस्या * गृहस्थ-आश्रममें भोगकी प्राप्ति तो स्वाभाविक है और मोक्षको प्राप्ति निष्काम धर्मका अनुष्ठान करनेसे होती है। + अकर्मण: कर्म पुण्य॑ कर्म चाप्याश्रमेषु च। जात्याश्रितं च राजेन्द्र तत्रापि श्रृणु धर्मवित्‌
- **Translation**: 

---

### Verse 3 (Bramha 0.3383)
- **Original**: आश्रमाणि च चत्वारि कर्मट्वारणि मानद ! चतुर्णामाश्रमाणां च गार्हस्थ्यं पुण्य स्मृतम्‌
- **Translation**: 

---

### Verse 4 (Bramha 0.3384)
- **Original**: (88। 13-15)
- **Translation**: 

---

### Verse 5 (Bramha 0.3385)
- **Original**: « गारुड़तोर्थ और गोवर्धनतीर्थकी पहिपा * 163 आरम्भ की। जब सूर्यदेवको इसका पता लगा,
- **Translation**: 

---

### Verse 6 (Bramha 0.3386)
- **Original**: नामक नदियोंके रूपमें आयी थीं। उन दोनोंका तब से भी घोड़ेका रूप धारण करके उसके पास
- **Translation**: 

---

### Verse 7 (Bramha 0.3387)
- **Original**: जहाँ गज्जामें संगम हुआ है, वह बहुत उत्तम तीर्थ गये। पतिब्रता उषा परपुरुषकी आशड्डासे भागकर
- **Translation**: 

---

### Verse 8 (Bramha 0.3388)
- **Original**: है। उसमें भिन्न-भिन्न देवताओं और तौथ्थोंका भारतवर्षमें गौतमीके तटपर आयी। वहाँ उसका
- **Translation**: 

---

### Verse 9 (Bramha 0.3389)
- **Original**: पृथक्‌ू-पृथक्‌ समागम हुआ है। उक्त संगममें पतिके साथ समागम हुआ, जिससे अश्विनीकुमारेंकी
- **Translation**: 

---

### Verse 10 (Bramha 0.3390)
- **Original**: सत्ताईस हजार तीर्थोंका समुदाय है। बहाँ किया उत्पत्ति हुई। वह स्थान अश्वतीर्थ, भानुतीर्थ और
- **Translation**: 

---

### Verse 11 (Bramha 0.3391)
- **Original**: हुआ स्नान और दान अक्षय पुण्य देनेवाला है। पञ्चवटी आश्रमके नामसे विख्यात हुआ। तापी
- **Translation**: 

---

### Verse 12 (Bramha 0.3392)
- **Original**: नारद! उस तीर्थके स्मरण, कीर्तन और श्रवणसे और यमुना दोनों सूर्यकी कन्याएँ थीं। वे गौतमी-
- **Translation**: 

---

### Verse 13 (Bramha 0.3393)
- **Original**: भी मनुष्य सब पापोंसे मुक्त हो धर्मवान्‌ू और तटपर अपने पितासे मिलनेके लिये अरुणा-बरुणा , सुखो होता है। /7->5470775 गारड़तीर्थ और गोवर्धनतीर्थकी महिमा ब्रह्माजी कहते हैं--नारद ! गार्ड नामक
- **Translation**: 

---

### Verse 14 (Bramha 0.3394)
- **Original**: रखा है। यदि बह जीवित होता तो यहाँ आये तीर्थ सब विध्नोंकी शान्ति करनेवाला है। उसके
- **Translation**: 

---

### Verse 15 (Bramha 0.3395)
- **Original**: बिना न रहता।' नन्दीकी बात सुनकर भगवान्‌ प्रभावका वर्णन करता हूँ, ध्यान देकर सुनो।
- **Translation**: 

---

### Verse 16 (Bramha 0.3396)
- **Original**: शिवने नागकी अबस्थाकों जान लिया और शेषनागके एक महाबली पुत्र था, जो मणिनागके
- **Translation**: 

---

### Verse 17 (Bramha 0.3397)
- **Original**: कहा-- वह नाग गरुड़के घरमें बँधा पड़ा है। तुम नामसे प्रसिद्ध हुआ। उसे सदा गरुड़का भय बना
- **Translation**: 

---

### Verse 18 (Bramha 0.3398)
- **Original**: शीघ्र जाकर जगदीश्वर भगवान्‌ विष्णुकी स्तुति रहता था, अतः उसने अपनी भक्तिके द्वारा
- **Translation**: 

---

### Verse 19 (Bramha 0.3399)
- **Original**: करों और गरुड़के द्वारा बन्धनमें डाले हुए नागकों भगवान्‌ शंकरको संतुष्ट किया। प्रसन्न
- **Translation**: 

---

### Verse 20 (Bramha 0.3400)
- **Original**: मेरे कहनेसे ले आओ ।' प्रभुकी बात सुनकर नन्‍्दी भगवान्‌ महेश्वले कहा--'नाग! कोई बर माँगो।'
- **Translation**: 

---

