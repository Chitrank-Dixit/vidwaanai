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

### Verse 1 (Vishnu Puran 0.7461)
- **Original**: । सो5पि पौरव॑ यौवनमासाद्य धर्माविरोधेन यथाकामं यथाकालोपपन्नं यथोत्साहं विषयांश्नचार
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7462)
- **Original**: सम्यकू चर प्रज़ापालनमकरोत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7463)
- **Original**: विश्वाच्या देवयान्या च सहोषभोगं भुक्‍्त्वा कामानामन्ते प्राप्स्यामीत्यनुदिनं. उन्मनस्को बभूव
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7464)
- **Original**: अनुदिनं चोपभोगतः कामा- नतिरस्यान्मरेने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7465)
- **Original**: ततश्लैवमगायत
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7466)
- **Original**: न जातु काम: कामानामुपभोगेन शाम्यति । हविषा कृष्णवर्त्मेव भूय एवाधिवर्द्धते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7467)
- **Original**: 23 एकस्यापि न पर्याप्त तस्मात्तृष्णां परित्यजेत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7468)
- **Original**: 24 यदा न कुरुते भावं सर्वभूतेषु पापकम्‌ । समदृष्टेस्तदा पुंस: सर्वास्सुखभया दिशा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7469)
- **Original**: 25 या दुस्यजा दुर्मतिभिर्या न जीर्यति जीर्यत: । तां तृष्णां सन्त्यजेत्माज्ञस्सुखेनैवाभिपूर्यते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7470)
- **Original**: 26 जीर्यन्ति जीर्यतः केशा दत्ता जीर्य॑त्ति जीर्य॑त: । धनाश्ञा जीविताशा च जीर्यतो5पि न जीर्यत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7471)
- **Original**: 27 पूर्ण वर्षसहस््न॑ मे विषयासक्तब्षेतस: । तथाप्यनुदिन॑ तृष्णा मम तेषूपजायते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7472)
- **Original**: 28 चतुर्थ अंश अश्10
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7473)
- **Original**: ॑ उनुआऋुऑल तटलटछ/2 / ल्‍ ल्‍च्तर्थअंश हतछरऊछऊछऊछऊछऊझऊझऊझऊझऊऋऋऊझकफरऋऊऋ रेाू5 में अभी विषय-भोगोंसे तृप्त नहीं हुआ हूँ, इसलिये एक सहस वर्षतक मैं तुम्हारी युवावस्थासे उन्हें भोगना चाहता हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7474)
- **Original**: इस लिषयमें तुम्हें किसी प्रकारकी आनाक्यनी नहीं करनी चाहिये ।' किंतु पिताके ऐसा कहनेपर भी यदुने वुद्धावस्थाकों पहण करना न चाहा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7475)
- **Original**: तब पिताने उसे इप दिया कि तेरी सन्तान राज्य-पदके योग्य न होगी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7476)
- **Original**: फिर राजा ययातिने तुर्वसु, ट्रह्मु और अनुसे भी अपना यौवन देकर बृद्धावस्था अहण करनेके लिये कहा; तथा उनमेंसे प्रत्येकके अस्वोकार करनेपर उन्होंने उन समीको जाप दें दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7477)
- **Original**: अन्त्ें सबसे छोटे शर्मिष्ठाके पुष्र पूरसे भी यही बात कही तो ठसने अति नम्नता और आदरके साथ पिताक्यें प्रणाम करके उदारतापूर्वक कहा--“यह तो हमारे कपर आपका महान्‌ अनुम्रह है। ऐसा कहकर पूछने अपने पिताको वृद्धालस्था ग्रहण कर उन्हें अपना यौवन दे दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7478)
- **Original**: 1575-- 67
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7479)
- **Original**: राजा ययातिने पूरूका यौवन लेकर समयानुसार प्राप्त हुए. यथेच्छ तिषयोंकों अपने उत्साहके अनुसार घर्म- पूर्षक्त भोगा और अपनी प्रजाका भली प्रकार पालन किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7480)
- **Original**: फिर विश्वायो और देवयानीके साथ विविध भोगॉंको भोगते हुए 'मैं कामनाओंका अन्त कर दूँगा'--ऐसे सोचते-सोचते बे प्रतिदिन [ भोगोकि लिये ] उत्कण्ठित रहने लगें
- **Translation**: 

---

