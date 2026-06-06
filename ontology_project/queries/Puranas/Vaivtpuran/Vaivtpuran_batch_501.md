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

### Verse 1 (Vaivtpuran 28.7218)
- **Original**: किरीट, कुण्डल तथा रेशमी पीताम्बरसे विभूषित श्रीहरिका स्मरण करते हुए इसी मन्त्रसे पिताका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.7219)
- **Original**: थे। वे उस रेणुकाकों रथमें बिठाकर ब्रह्मलोकमें दाह करो।* हे भृगुनन्दन! पहले तुम भाइयोंके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.7220)
- **Original**: गये और जमदग्नरिको लेकर श्रीहरिके संनिकट साथ सिरमें आग लगाओ।'' तब भृगुमुनिके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.7221)
- **Original**: जा पहुँचे। वहाँ वैकुण्ठमें बे दोनों पति-पत्नी आज्ञानुसार परशुरामने अपने गोत्रवालोंके साथ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.7222)
- **Original**: निरन्तर श्रीहरिकी परिचर्या, जो मड्जलोंको मम्बरल वह सारा कार्य सम्पन्न किया। है, करते हुए श्रीहरिके संनिकट रहने लगे। तदनन्तर रेणुकाने वहाँ अपने पुत्र परशुरामको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.7223)
- **Original**: . नारद! इधर परशुरामने ब्राह्मणों तथा भृगुजीके छातीसे लगा लिया और परिणाममें सुखदायक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.7224)
- **Original**: सहयोगसे माता-पिताकी शेष क्रिया समाप्त करके कुछ वचन कहे--'बेटा! इस भवसागरमें विरोध
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.7225)
- **Original**: ब्राह्मणॉंकों बहुत-सा धन दान दिया। फिर गौ, न करना सम्पूर्ण मड्रलोंका मड्गल है और विरोध
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.7226)
- **Original**: भूमि, स्वर्ण, वस्त्र, सुवर्णनिर्मित पलंगसहित नाशका कारण तथा समस्त उपद्रवोंका हेतु है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.7227)
- **Original**: मनोरम दिव्य शय्या, जल, अन्न, चन्दन, रत्रदीप, अत: भयंकर क्षत्रियोंके साथ विरोध न करना
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.7228)
- **Original**: चाँदीका पहाड़, सुवर्णक आधारसहित स्वर्णनिर्मित ही उचित है; किंतु मेरे सुनते-सुनते तुमने जो उत्तम आसन, सुवासित ताम्बूल, छत्र, पादुका, प्रतिज्ञा की है उसे पूर्ण करना चाहिये। इसके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.7229)
- **Original**: फल, मनोहर माला, फल-मूल-जल और मनोहर लिये तुम दिव्य मन्त्रोंके ज्ञाता भूगु और ब्रह्माके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.7230)
- **Original**: मिष्टान्न तथा धन ब्राह्मणोंको देकर वे ब्रह्मलोकको साथ विचार करके जैसा उचित हो वैसा करना।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.7231)
- **Original**: चल पड़े। ब्रह्मलोकमें पहुँचकर परशुरामने ....ः. आलोचित कर्म शुभकारक होता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.7232)
- **Original**: भक्तिभावसे अव्ययात्मा ब्रह्माजीकों नमस्कार है।' यों कहकर रेणुका परशुरामकों छोड़कर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.7233)
- **Original**: करके रोते हुए सारी घटना कह सुनायी। कृपामय अपने पतिका आलिड्डन करके श्रीहरिका स्मरण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.7234)
- **Original**: ब्रह्माजीने सारी बातें सुनकर उन्हें शुभाशीर्वाद करते हुए परशुरामकी ओर निहारती हुई चितामें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.7235)
- **Original**: दिया और अपने हृदयसे लगा लिया। भृगुवंशी सो गयी। तब भाइयोंके साथ परशुरामने चितामें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.7236)
- **Original**: परशुरामकी बहुत-से जीवोंका विनाश करनेवाली, आग लगा दी। फिर भाइयों और पिताके शिष्योंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.7237)
- **Original**: दुष्कर एवं भयंकर प्रतिज्ञाकों सुनकर चतुर्मुख साथ बे बिलाप करने लगे। इतनेमें ही सती रेणुका
- **Translation**: 

---

