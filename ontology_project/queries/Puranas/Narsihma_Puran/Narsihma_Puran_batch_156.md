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

### Verse 1 (Narsihma Puran 0.3101)
- **Original**: 178 1 0 ऑनरसिंहपुाण अध्याय ध8 ([ अध्याय 48 रामाभिषेकं विपुलं श्वो भविष्यति जानथ। श्रुत्वेत्थं मन्त्रिण: प्राहुस्तं नुप॑ प्रणिपत्य च
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.3102)
- **Original**: 10 शोभन ते मतं राजन्‌ यदिद॑ परिभाषितम्‌। रामाभिषेकमस्माक सर्वेषां च॒ प्रियंकरम्‌
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.3103)
- **Original**: 11 इत्युक्तो दशरथस्तैस्तान्‌ सर्वान्‌ पुतरस्रबीत्‌। आनीयमत्तां द्रुतं सर्वे सम्भारा मम शासनातू
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.3104)
- **Original**: 12 सर्वतः सारभूता च॒ पुरी चेयं समन्‍्तत:। अद्य शोभान्विता कार्या कर्तव्यं यागमण्डलम्‌
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.3105)
- **Original**: 13 इत्येवमुक्ता राज्ञा ते मन्त्रिण: शीघ्रकारिण:। तथैव चक्तुस्ते सर्वे पुनःपुनरुदीरिता:
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.3106)
- **Original**: 14 प्राप्तर्षघ: स राजा चर शुभं दिनमुदीक्षयन्‌। कौशल्या लक्ष्मणश्चैब सुमित्रा नागरो जन:
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.3107)
- **Original**: 15 रामाभिषेकमाकर्ण्य मुर्द॑ प्राप्यातिहर्षित:। श्रश्नूश्वशुरयो: सम्यक्‌ शुभ्रूषणपरा तु सा
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.3108)
- **Original**: 16 मुदान्विता सिता सीता भर्तुराकर्ण्य शोभनम्‌। श्वोभाविन्यभिषेके तु रामस्य विदितात्पत:
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.3109)
- **Original**: 17 दासी तु मन्धरानाम्जी कैकेय्या: कुब्जरूपिणी। स्वां स्वामिनीं तु कैकेयीमिर्द वचनमत्नवीत्‌
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.3110)
- **Original**: 18 श्रृणु राज्जि महाभागे खच्चर्न मप्र शोभनप्‌। त्वत्पतिस्तु महाराजस्तव नाशाय चोद्यत:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.3111)
- **Original**: 19 रामोउसौ कौसलीपु्र: श्वो भविष्यति भूपति: । वसुवाहनकोशादि राज्यं च सकल॑ शुभे
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.3112)
- **Original**: 20 भविष्यत्यद्य रामस्थ भरतस्यथ न किंचन। भरतो5पि गतो दूर॑ मातुलस्य गृह प्रति
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.3113)
- **Original**: 29 हा कष्टे मन्दभाग्यासि सापत्यादु:खिता भूशम्‌। सैवमाकर्ण्य कैकेयी कुब्जामिदम्रधात्रवीत्‌
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.3114)
- **Original**: 22 पश्य मे दक्षतां कुब्जे अहय त्यं विचक्षणे। यथा तु सकल॑ राज्यं भरतस्य भविष्यति
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.3115)
- **Original**: 23 तुम सब लोग यह जान लो कि कल बड़े समारोहके साथ श्रीगमचद्धजोका राज्प्राभिषेक होगा'
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.3116)
- **Original**: 75--95,
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.3117)
- **Original**: यह सुनकर मन्त्रियोंते राजाकों प्रणाम करके उनसे कहा--' राजन्‌! आपने हमारे सम्रक्ष अपना जो यह विचार व्यक्त किया है, बहुत ही उत्तम है। श्रीरामका अभिषेक हम सभीके लिये प्रियकारक है'
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.3118)
- **Original**: उनके यों क्रहनेपर राजा पुनः उन सब लोगोंसे बोले--' अच्छा, अब मेरी आज्ञासे अभिषेकके सभो सामान शाप लाये जायें और समस्त बसुधाकी सारभुता इस अयोध्यापुरीको भो आज ही सब ओरसे सुसज्जित कर देना चाहिये। साथ हो एक यज्ञमण्डपको रचना भो चरम आवश्यक हैं!'
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.3119)
- **Original**: 4 राजाके यों कहने और यार-यार प्रेरणा करनेपर उन सब ज्ञोप्रकारी मन्त्रियोने उतके कथनानुसार सब कार्य पूर्ण कर दिये। राजा इस ज्ुभ दिनको प्रतीक्षा करते हुए बड़े हो आनन्दित हुए। कौशल्या, सुमित्रा, लक्ष्मण तथा अन्य पुरवासो श्रीरामचन्रजीफे राज्याभिषेकका शुभ समाचार सुनकर आनन्दके मारे फूले नहीं समाये। सास-ससुरकौ सेवामें भलोभाँति लगों रहनेवालो सीता भो अपने पतिके लिये इस शुभ संबादकों सुनकर बहुत ही प्रसन्न हुई
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.3120)
- **Original**: 14-165,
- **Translation**: 

---

