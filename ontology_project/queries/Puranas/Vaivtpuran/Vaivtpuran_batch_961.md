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

### Verse 1 (Vaivtpuran 543.17534)
- **Original**: रहती थी; अतः उन्हें आया देखकर वे आनन्दमग्र मारकर “ रक्तबीजविनाशिनी ' कहलाती हूँ। आपकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17535)
- **Original**: हो गये। उनके नेत्र और मुख हर्षसे स्िल उठे। आज्ञासे मैं सत्यस्वरूपिणी दक्षकन्या 'सती' हुई।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17536)
- **Original**: फिर तो वे दुन्दुभियाँ बजाने लगे। वहाँ योगधारणद्वारा शरीरका त्याग करके आपके उधर बिरजा नदीको पार करके जगत्पति ही आदेशसे पुनः गिरिराजनन्दिनी “पार्वती” हुई;
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17537)
- **Original**: श्रीकृष्णकी दृष्टि ज्यों ही राधापर पड़ी, त्यों हो जिसे आपने गोलोकस्थित रासमण्डलमें शंकरको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17538)
- **Original**: वे रथसे उतर पड़े और राधिकाके हाथकों अपने दे दिया था। मैं सदा विष्णुभक्तिमें रत रहती हूँ;
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17539)
- **Original**: हाथमें लेकर शतश्रृद्ध पर्वतपर घूमने चले गये। इसी कारण मुझे वैष्णवी और विष्णुमाया कहा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17540)
- **Original**: वहाँ सुरम्य रासमण्डल, अक्षयवट और पुण्यमय जाता है। नारायणकी माया होनेके कारण मुझे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17541)
- **Original**: बृन्दाबनको देखते हुए तुलसी-काननमें जा पहुँचे। लोग नारायणी कहते हैं। मैं श्रीकृष्णकी प्राणप्रिया,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17542)
- **Original**: वहाँसे मालतीबनको चले गये। फिर श्रीकृष्णने उनके प्राणोंकी अधिष्ठात्री देवी और बासुस्वरूप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17543)
- **Original**: कुन्दवन तथा माधवी-काननको बायें करके महाविष्णुकी जननी स्वयं राधिका हूँ। आपके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17544)
- **Original**: मनोरम चम्पकारण्यको दाहिने छोड़ा। पुनः आदेशसे मैंने अपनेकों पाँच रूपोंमें विभक्त कर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17545)
- **Original**: सुरुचिर चन्दनकाननकों पीछे करके आगे बढ़े दिया; जिससे पाँचों प्रकृति मेरा ही रूप हैं। मैं ही
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17546)
- **Original**: तो सामने राधिकाका परम रमणीय भवन दीख घर-घरमें कला और कलांशसे प्रकट हुई वेदपत्नियोंके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17547)
- **Original**: पड़ा। वहाँ जाकर बे राधाके साथ श्रेष्ठ रलसिंहासनपर रूपमें वर्तमान हूँ। महाभाग! वहाँ गोलोकमें मैं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17548)
- **Original**: विराजमान हुए। फिर उन्होंने सुवांसित जल पिया बिरहसे आतुर हो गोपियोंके साथ सदा अपने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17549)
- **Original**: तथा कपूरयुक्त पानका बोीड़ा ग्रहण किया। आबासस्थानमें चारों ओर चक्कर काटती रहती हूँ;
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17550)
- **Original**: तत्पश्चात्‌ वे सुगन्धित चन्दनसे चर्चित पुष्पशय्यापर अतः आप शीघ्र ही वहाँ पधारिये। सोये और रस-सागरमें निमग्र हो सुन्दरी राधाके नारद! पार्वतीके बचन सुनकर रसिकेश्वर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17551)
- **Original**: साथ बिहार करने लगे। श्रीकृष्ण हँसे और रत्लनिर्मित विमानपर सवार नारद! इस प्रकार मैंने रमणीय गोलोकारोहणके हो उत्तम गोलोककों चले गये। तब सनातनी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17552)
- **Original**: विषयमें अपने पिता धर्मके मुखसे जो कुछ सुना विष्णुमाया स्वयं पार्वतीने मायारूपिणी वंशीके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17553)
- **Original**: था, वह सब तुम्हें बता दिया। अब पुनः और नादसे आच्छन्न हुए देवगणको जगाया। वे सभी
- **Translation**: 

---

