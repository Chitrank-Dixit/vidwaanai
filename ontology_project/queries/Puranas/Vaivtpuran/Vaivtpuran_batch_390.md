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

### Verse 1 (Vaivtpuran 19.6894)
- **Original**: करें। लक्ष्मी नासिकाकी रक्षा करें। कमला नेत्रकी और कवच प्रदान किया था, वह मुझे बतलाइये।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.6895)
- **Original**: रक्षा करें। केशवकान्ता केशोंकी, कमलालया नारायणने कहा--नारद! जब पुष्करमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.6896)
- **Original**: कपालकी, जगज्जननी दोनों कपोलॉंकी और तपस्या करके देवराज इन्द्र शान्त हुए, तब उनके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.6897)
- **Original**: सम्पत्प्रदा सदा स्कन्धकी रक्षा करें। '3» श्रीं क्लेशको देखकर स्वयं श्रीहरि वहीं प्रकट हुए।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.6898)
- **Original**: कमलवासिन्यै स्वाहा ' मेरे पृष्ठणागका सदा पालन उन हषीकेशने इन्द्रसे कहा--“ तुम अपने इच्छानुसार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.6899)
- **Original**: करे! '3» श्रीं पद्मालयायै स्वाहा' वक्ष:स्थलको वर माँग लो।' तब इन्द्रने लक्ष्मीको ही वररूपसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.6900)
- **Original**: सदा सुरक्षित रखे। श्री देवीको नमस्कार है, वे वरण किया और श्रीहरिने हर्षपूर्वक उन्हें दे दिया।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.6901)
- **Original**: मेरे कड्डाल तथा दोनों भुजाओंको बचावें। 3 यर देनेके पश्चात्‌ हषीकेशने जो हितकारक, सत्य,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.6902)
- **Original**: हीं श्रीं लक्ष्म्य नमः” चिरकालतक निरन्तर मेरे साररूप और परिणाममें सुखदायक था, ऐसा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.6903)
- **Original**: पैरोॉंका पालन करे। '30 हीं श्रीं नमः पद्मायै वचन कहना आरम्भ किया। स्वाहा' नितम्बभागकी रक्षा करे। '39 श्रीं श्रीमधुसूदन बोले--इन्द्र ! ( लक्ष्मी-प्राप्तिके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.6904)
- **Original**: महालक्ष्म्यै स्वाहा' मेरे सर्वाज्रकी सदा रक्षा करे। लिये) तुम लक्ष्मी-कबच ग्रहण करो। यह समस्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.6905)
- **Original**: '3& हुं श्रीं क्‍्लीं महालक्ष्म्य स्वाहा' सब ओरसे दुःखोंका विनाशक, परम ऐश्वर्यका उत्पादक और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.6906)
- **Original**: सदा मेरा पालन करे। वत्स! इस प्रकार मैंने सम्पूर्ण शत्रुओंका मर्दन करनेवाला है। पूर्वकालमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.6907)
- **Original**: तुमसे इस सर्व श्चर्यप्रद नामक परमोत्कृष्ट कवचका जब सारा संसार जलमग्र हो गया था, उस समय
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.6908)
- **Original**: वर्णन कर दिया। यह परम अद्भुत कवच सम्पूर्ण मैंने इसे ब्रह्माकों दिया था। जिसे धारण करके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.6909)
- **Original**: सम्पत्तियोंको देनेवाला है। जो मनुष्य विधिपूर्वक ब्रह्मा त्रिलोकीमें श्रेष्ठ और सम्पूर्ण ऐश्वर्योंसे सम्पन्न
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.6910)
- **Original**: गुरुकी अर्चना करके इस कवचको गलेमें अथवा हो गये थे। इसीके धारणसे सभी मनुलोग सम्पूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.6911)
- **Original**: दाहिनी भुजापर धारण करता है, वह सबको ऐश्वर्योंक भागी हुए थे। देवराज! इस सर्वश्चर्यप्रद
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.6912)
- **Original**: जीतनेवाला हो जाता है। महालक्ष्मी कभी उसके कवचके ब्रह्मा ऋषि हैं, पद्धक्ति छन्द है, स्वयं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.6913)
- **Original**: घरका त्यांग नहीं करतीं; बल्कि प्रत्येक जन्ममें पद्मालया लक्ष्मी देवी हैं और सिद्धैश्वर्यके जपोंमें
- **Translation**: 

---

