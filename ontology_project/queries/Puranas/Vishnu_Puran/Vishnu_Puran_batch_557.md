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

### Verse 1 (Vishnu Puran 0.11121)
- **Original**: अरे बनरक्षको ! जिस प्रकार [ समुद्रसे उत्पन्न हुए ] मदिरा, चन्द्रमा और लक्ष्मीका सब ट्मेग समानतासे भोग करते हैं ठसी प्रकार पारिजात-वक्ष भी सभीकी सम्पत्ति है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11122)
- **Original**: यदि पतिके बाहुबलसे गर्विता होकर शाचीने ही इसपर अपना अधिकार जमा रखा है तो उससे कहना कि सत्यभामा उस वृक्षक्रों हरण कराकर लिये जाती है, तुम्हें क्षमा करनेकी आवश्यकता नहीं है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11123)
- **Original**: अरे मालियो ! तुम तुरन्त जाकर मेंरे ये शब्द शचीसे कहो कि सत्यभामा अत्यन्त गर्वपूर्वक कड़े अक्षरोंमें यह कहती है कि यदि तुम अपने पतिक् अत्यन्त प्यारी हो और वे तुम्हारे नशीभूत हैं तो मेरे पतिको पारिजात हरण करनेसे रोकें
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11124)
- **Original**: मैं तुप्हारे पति शक्रको जानती हूँ और यह भी जानती हूँ कि से देवताओंके स्वामी हैं तथापि मैं मानवी ही तुम्हारे इस पारिजात-वृक्षकरो लिये जाती हूँ”
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11125)
- **Original**: श्रीपराशरजी बोल्े--सत्यभामाके इस प्रकार कहनेपर वनरक्षकोने शचीके पास जाकर उससे सम्पूर्ण कृत्तान्त ज्यों-का-स्यों कह दिया । यह सब सुनकर झचीने अपने पति देवराज इन्द्रकों उत्साहित किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11126)
- **Original**: हे द्विजोत्तम ! तब देवराज इन्ध पारिजात-वृक्षको छुड़ानेके लिये सम्पूर्ण देवसेनाके सहित श्रीहरिसे लड़नेके लिये चले
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11127)
- **Original**: जिस समय इन्द्रने अपने हाथमें बच्र किया उसी समय सम्पूर्ण देवगण परिघ, निश्बिश, गदा और शूछ आदि अस्न-दस्तोंसे सुसज्जित हो गये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11128)
- **Original**: तदनन्तर देवसेनासे घिरे हुए ऐगवतारूढ इन्द्रको युद्धके लिये उद्यत देख श्रीगोबिन्दने सम्पूर्ण दिशाओंक्ये 'शब्दायमान करते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11129)
- **Original**: 392 ततो दिश्लो नभश्लैव दृष्ठा शरशतैश्चितम्‌। मुमुचुस्विदशास्सवें ह्वाख्रशख्राण्यनेकश:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11130)
- **Original**: 57 एकैकमर्त्र शर्त्रं च देवैर्मुक्ते सहस्नरशः । चिच्छेद लीलयैवेशों जगतां मधुसूदनः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11131)
- **Original**: 568 पाशं॑ सलिलराजस्य समाकृष्योरगाशनः । चकार खण्डशश्चज्व्वा बालपन्नगदेहवत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11132)
- **Original**: 59 यमेन प्रहिते दण्ड गदाविक्षेपखण्डितम्‌। पृथिव्यों पातयामास भगवान्‌ देवकीसुत:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11133)
- **Original**: 60 शिबिकां च धनेशस्य चक्रेण तिलशो विभुः । चकार शौरिरर्क चर दृष्टिदृष्टटतौजसम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11134)
- **Original**: 69 नीतो5ग्िइशीततां बाणैद्राविता वसवो दिशा: । चक्रविच्छिन्नशूलाप्रा रुद्ा भुवि निपातिता:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11135)
- **Original**: 62 साध्या विश्वेष्य मर्तो गन्धर्वाश्षेव सायकैः: । शार््िणा प्रेरितैरस्ता व्योप्ति शाल्मलितूलवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11136)
- **Original**: 63 गरुत्पानपि तुण्डेन पक्षाभ्यां च नखाडुरैः । भक्षयंस्ताडयन्‌ देवान्‌ दारयंक्ष चचार वै
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11137)
- **Original**: 6ड ततइशरसहस्नेण देवेन्द्रमधुसूदनो परस्परं ववर्षाति धाराभिरिब तोबदौ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11138)
- **Original**: 65 ऐराबतेन गरुड़ो युयुधे रत सु । देवैस्समस्तैर्युयुधे झक्रेण च :
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11139)
- **Original**: 66 भिन्नेष्ठशेषबाणेषु झख्त्रेष्ृत्लेपु क्र त्वरन्‌। जग्राह वासवो वर््र कृष्णाश्चक्रं सुदर्शनम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11140)
- **Original**: 67 ततो हाहाकृतं सर्व त्रैल्लोक्यं द्विजसत्तम
- **Translation**: 

---

