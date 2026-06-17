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

### Verse 1 (Vishnu Puran 0.7441)
- **Original**: यदुं चर तुर्वसूं चैव देवयानी व्यजायत। द्रह्मूं चानुं च पूरुं च शरर्मिष्ठा वार्षपर्वणी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7442)
- **Original**: 6 काव्यशापाच्चाकालेनेव. ययातिर्जरामबाप
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7443)
- **Original**: प्रसन्नशुक्रवचनाध्च स्वजरां सड्क्रामयितुं ज्येष्ठं. पुत्र यदुमुबाच
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7444)
- **Original**: . वत्स त्वन्यातामहशापादियमकालेनैल जरा ममोपस्थिता तामहं महायल-विक्रमदाली पुत्र हुए
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7445)
- **Original**: यततिने राज्यकी इच्छा नहीं की, इसलिये ययाति ही राजा ख
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7446)
- **Original**: ययातिने शुक्राचार्यजीकी पुत्री देववानी और बृषपर्याकी कन्या शार्मिष्ठासे विवाह किया था
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7447)
- **Original**: उनके वंश्ञके सम्ब्धमें यह इलोक प्रसिद्ध है--
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7448)
- **Original**: 'देवयानीने यदु और तुर्वसूको जन्म दिया तथा वृषपर्वाको पुत्री दार्मिष्ठाने द्रह्मु, अनु और पूरु्को उत्पन्न किया'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7449)
- **Original**: ययातिको शुक्राचार्यजोके शापसे वृद्धावस्थाने असमय ही घेर लिया था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7450)
- **Original**: पीछे झुक़जीके प्रसन्न होकर कहनेपर उन्होंने अपनी वृद्धावरथाको ग्रहण करनेके लिये बड़े पुत्र यदुसे कहा--
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7451)
- **Original**: “वल्स ! तुम्हारे नानाजीके शापसे मुझे असमयमें ही वृद्धावस्थाने घेर लिया है, अब तस्थैबानुप्रहाद्धवतस्सज्चारयामि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7452)
- **Original**: उन्हींकी कृपासे मैं उसे तुमको देना चाहता हूँ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7453)
- **Original**: अआ> 90 ] एक वर्षसहस्नमतृप्तोईस्मि विषयेषु त्वद्ययसा विषयानहं भोक्तुमिच्छापि
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7454)
- **Original**: नात्र भवता प्रत्याख्यानं. कर्त्तव्यमित्युक्तस्स यदुर्नैच्छत्तां जरापमादातुम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7455)
- **Original**: त॑ च पिता डाशाप त्वखसूतिर्न राज्या्ा भविष्यतीति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7456)
- **Original**: अनन्तरं च॒ तुर्वसुं डुल्युमनुं च पृथिबीपति जराग्रहणार्थ स्वयोबनप्रदानाय चाभ्यर्थयामास
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7457)
- **Original**: तैरप्येकैकेन प्रत्याख्यातस्ताउ्छशाप
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7458)
- **Original**: अथ शर्मिष्ठातनवमशेषकनीयांसं पूरूं तथैवाह
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7459)
- **Original**: स चातिप्रवणमति: सबहुमान॑ पितरे प्रणम्य महाप्रसादो5यमस्माकमित्युदार- मभिधाय जरा जग्राह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7460)
- **Original**: स्वकीयं च यौवन स्वपित्रे ददौ
- **Translation**: 

---

