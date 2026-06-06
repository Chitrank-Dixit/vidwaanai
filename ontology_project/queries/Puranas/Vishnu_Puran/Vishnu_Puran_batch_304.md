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

### Verse 1 (Vishnu Puran 0.6061)
- **Original**: अश्रीपराशरजी ओल्के---भगवान्‌क्ी ऐसी आज्ञा होनेपर देवगण उन्‍हें प्रणाम कर जहाँसे आये थे वहाँ चले गये तथा उनके साथ मायामोह भी जहाँ असुरगण थे वहाँ गया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6062)
- **Original**: स्स्न्च्न है ततततन इति श्रीविष्णुफुराणे तृतीयेंडशे सप्तदशोउध्याय:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6063)
- **Original**: जमा औ “++5+ अठारहवाँ अध्याय मायामोह और असुरोंका संवाद तथा राजा दतधनुकी कथा श्रीपराज्ञर उताच श्रीपराझरजी बोले--हे मैत्रेय! तदनन्तर तपस्यभिरतान्सो$थ मायामोहो महासुरान्‌।
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6064)
- **Original**: मायामोहने [देवताओंके साथ] जाकर: देखा कि मैत्रेय ददृूशे गत्वा नर्मदातीरसंश्रितान
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6065)
- **Original**: 91 असुरगण नर्मदाके तटपर तपस्थायें रूगे हुए हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6066)
- **Original**: तब ततो दिगम्बरों मुण्डो बहिपिच्छधरो द्विज । उस मयूरपिच्छधारी दिगम्बर और मुण्डितकेश मायापोहने मायामोहो5सुरान्‌ इलकषणमिदं वचनमत्रवीत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6067)
- **Original**: असुरोंसे अति मधुर बाणीमें इस प्रकार कह्दा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6068)
- **Original**: आ0् 18
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6069)
- **Original**: ] मायापोह उवाच है दैत्यपतयो ब्रूत यदर्थ तप्यते तपः। ऐहिक॑ वाथ पारत््यं तपस: फलमिच्छथ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6070)
- **Original**: 3 असुय ऊचुः पारप्यफलछाभाय तपश्चर्या महामते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6071)
- **Original**: अस्माभिरियमारव्या कि वा तेउनत्न विवक्षितम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6072)
- **Original**: 4 फयामोह उवाच कुरुध्य॑ मम वाक्यानि यदि मुक्तिमभीप्सथ । अ्हईध्वमेन॑ धर्म च्॒ मुक्तिद्वारमसंवृतम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6073)
- **Original**: 5 धर्मों विमुक्तेरहोंठयँ नैतस्पादपरों वर: । अशत्रैव संस्थिता: स्वर्ग विपुक्ति वा गमिष्यथ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6074)
- **Original**: 6 अर्हध्व॑ धर्ममेते च सर्वे यूयं महाबला:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6075)
- **Original**: 7 श्रीपराश्र उवाच एवंप्रकारैर्बहुभिरयुक्तिदर्शनचर्चिति: ] मायामोहेन ते दैत्या वेदमार्गादपाकृता:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6076)
- **Original**: <8 ' भ्र्मायैतद्र्माय सदेतन्न सदित्यपि । बिमुक्तये त्वि्द नैतद्विमुक्ति सम्प्रयच्छति
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6077)
- **Original**: 9 परमार्थोज्यमत्यर्थ परमार्थो न चाप्ययम्‌। कार्यमेतदकार्य च्व नैतदेवं स्फुट्टं त्विदम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6078)
- **Original**: 10 दिग्वाससामयं धर्मों धर्मोईयं बहुवाससाम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6079)
- **Original**: 19 इत्यनेकान्तवाद॑ च्॒ मायापोहेन नैकधा। तेन दर्शयता दैत्यास्स्वधर्म त्याज़िता द्विज
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6080)
- **Original**: 12 अहतेत॑ महाधर्म मायामोहेन ते यतः । प्रोक्तास्तमाश्रिता धर्ममाहतास्तेन तेईडभवन्‌
- **Translation**: 

---

