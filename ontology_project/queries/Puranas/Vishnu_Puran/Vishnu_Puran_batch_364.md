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

### Verse 1 (Vishnu Puran 0.7261)
- **Original**: तदनन्तर उसी अग्रिसे नाना प्रकारके यज्ञॉंका यजन करते हुए उन्होंने गन्धर्व-लोक प्राप्त किया और फिर उर्वशीसे उनका वियोग न हुआ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7262)
- **Original**: पूर्वकालमें एक ही अप्रि था, उस एकहोसे इस मन्वन्तरमें तीन प्रकारके अग्रियोंका प्रचार हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7263)
- **Original**: नच्तत कऔ तन इति श्रीविष्णुपुराणे चतुर्थें5शे षष्टोउध्यायः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7264)
- **Original**: क्क््ज-ः है 4 कजन सातवाँ अध्याय जहुका गड्जापान तथा जमदम्ि और विश्वामित्रकी उत्पत्ति श्रीपएराज्र उवाच तस्थाप्यायुर्धीमानम्ावसुर्विश्वावसु:श्रुतायु- भ्रीपराशरजी बलोले---सजा पुरूस्याफे परम बुद्धिमान्‌ आयु, अमावसु, विश्वावसु, श्रुतायु, शतायु इशतायुस्युतायुरितिसंज्ञा:ः षट्‌ पुत्रा अभवन्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7265)
- **Original**: और अयुतायु नामक छः पुत्र हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7266)
- **Original**: अमायसुके
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7267)
- **Original**: तथामावसोर्भीमनामा पुत्रो3भवत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7268)
- **Original**: भीमस्य काझ्जनः काझ्नात्सुहोत्रस्तस्यापि जहु:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7269)
- **Original**: योउसौ यज्ञवाटमस्विलं गड्जाम्भसा- प्रावितमबलोक्य क्रोधसंरक्ततोचनो भगवत्ते अज्ञपुरुषमात्मनि परमेण समाधिना सपारोप्याखिछामेव गड़गमपियत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7270)
- **Original**: अथैन॑ देवर्षय: प्रसादयामासु:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7271)
- **Original**: दुहितृत्वे चास्य गड्जामनयन्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7272)
- **Original**: जह्लोश्व॒ सुमन्तुर्नाम पुत्रो3भवत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7273)
- **Original**: तस्याप्यजकस्ततो बलकाश्रस्तस्मात्कुशस्तस्यापि कुझाम्बकुशनाभाधूर््तरजसो वसुश्चेति च॒त्वार: पुत्रा बभूबु:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7274)
- **Original**: तेषां कुझाम्बः शक्रतुल्यो मे पुत्रो भरवेदिति तपश्चकार
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7275)
- **Original**: त॑ चोग्रतपसमवलोक्य मा भव्वन्योउस्मत्तुल्यवीर्य डत्यात्मनैयास्थेन्द्र: पुश्रत्वमगच्छत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7276)
- **Original**: स॒गाधिनाम पुत्र: कौशिकोउभवत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7277)
- **Original**: गाधिश्व सत्यवतती कनन्‍्यामजनयत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7278)
- **Original**: भीम, भीमके काझन, काझनके सुहोत्र और सुहोत्रके जह्दू नामक पुत्र हुआ जिसने अपनी सम्पूर्ण चज्ञशाल्त्रकों गज्लाजलसे आउह्लानित देख क्रोघसे रक्तनयन हो भगवान्‌ यज्ञपुरुफष्कों परम समाधिकरे द्राय अपनेमें स्थापित कर सम्पूर्ण गल्माजीको पी लिया था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7279)
- **Original**: तब देवर्षियोने इन्हें प्रसत्र किया और गक्कजीकों इनकी पुत्रीरूपसे पाकर के गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7280)
- **Original**: जहूके सुमत्तु नामक पुत्र हुआ
- **Translation**: 

---

