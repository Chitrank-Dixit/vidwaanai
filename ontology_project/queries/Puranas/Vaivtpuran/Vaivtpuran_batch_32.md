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

### Verse 1 (Vaivtpuran 4.8536)
- **Original**: स्तोत्रराजकों सुनती है, वह निश्चय ही पुत्र पाती प्रातःकाल पाठ करता है, बह अवश्य ही अपनी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8537)
- **Original**: है। जो कन्याकी माता तो है परंतु पुत्रसे होन अभीष्ट वस्तु प्राप्त कर लेता है। इसके पाठसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8538)
- **Original**: है, वह यदि. पाँच महीनेतक कलशपर दुर्गाकी पुत्रार्थीकों पुत्र, कन्यार्थीको कन्या, विद्यार्थीको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8539)
- **Original**: सम्यक्‌ पूजा करके इस स्तोत्रकों श्रवण करती विद्या, प्रजार्थीकों प्रजा, राज्यभ्रष्टकों राज्य और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8540)
- **Original**: है तो उसे अवश्य ही पुत्रकी प्राप्ति होती है। धनहीनको धनकी प्राप्ति होती है। जिसपर गुरु, (अध्याय 45) #डल>लरनिग्यायए+. >> सबका स्तवन-पूजन और नमस्कार करके परशुरामका जानेके लिये उद्यत होना, गणेश-पूजामें तुलसी-निषेधके प्रसड्रमें गणेश-तुलसीके संवादका वर्णन तथा गणपतिखण्डका श्रवण-माहात्म्य श्रीनारायण कहते हैं--नारद! इस प्रकार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8541)
- **Original**: पुष्पोंसे भक्तिपूर्वक उनकी पूजा कौ। इस प्रकार परशुरामने हर्षमग्र-चित्तसे दुर्गाकी स्तुति करके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8542)
- **Original**: परशुरामने भक्तिभावसहित भाई गणेशका भलीभौँति पुनः श्रीहरिद्वारा बतलाये गये स्तोत्रसे गणेशका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8543)
- **Original**: पूजन करके गुरुपत्री पार्वती और गुरुदेव शिवकों स्तवन किया। तत्पश्चात्‌ नाना प्रकारके नैवेद्यों, नमस्कार किया तथा शंकरकी आज्ञा ले वे वहाँसे धूपों, दीपों, गन्‍्धों और तुलसीके अतिरिक्त अन्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8544)
- **Original**: जानेको उद्यत हुए। [63] सं0 ख्र0 खै0 पुराण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8545)
- **Original**: 396 » संक्षिप्त ब्रह्मवैचर्तघुराण + 04 0 22 2 22 3 )])2)2)]4]200720000]438]7744+04400980480080+] हद नारदजीने पूछा--प्रभो! परशुरामने जब
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8546)
- **Original**: नवयुवती कन्या हूँ और तपस्यामें संलग्र हूँ। मेरी विविध नैवेद्यों तथा पुष्पोंद्वारा भगवान्‌ गणेशकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8547)
- **Original**: यह तपस्या पति-प्राप्तिक लिये है; अत: आप पूजा की थी, उस समय उन्होंने तुलसीको छोड़
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8548)
- **Original**: मेरे स्वामी हो जाइये। तुलसीकी बात सुनकर क्यों दिया ? मनोहारिणी तुलसी तो समस्त पुष्पोंमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8549)
- **Original**: अगाध बुद्धिसम्पन्न गणेश श्रीहरिका स्मरण करते मान्य एवं धन्यवादकी पात्र हैं; फिर गणेश उस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8550)
- **Original**: हुए विदुषी तुलसीसे मधुरवाणीमें बोले। सारभूत पूजाको क्‍यों नहीं ग्रहण करते? गणेशने कहा--हे माता! विवाह करना श्रीनारायण बोले--नारद ! ब्रह्मकल्पमें एक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8551)
- **Original**: बड़ा भयंकर होता है; अत: इस बिषयमें मेरी ऐसी घटना घटित हुई थी, जो परम गुद्दा एवं
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8552)
- **Original**: बिलकुल इच्छा नहीं है; क्योंकि विवाह दुःखका मनोहारिणी है। उस प्राचीन इतिहासको मैं कहता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8553)
- **Original**: कारण होता है, उससे सुख कभी नहीं मिलता। हूँ, सुनो। एक समयकी बात है। नवयौवन-
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8554)
- **Original**: यह हरि-भक्तिका व्यवधान, तपस्थाके नाशका सम्पन्ना तुलसीदेवी नारायणपरायण हो तपस्याके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8555)
- **Original**: कारण, मोक्षद्वारका किवाड़, भव-बन्धनकी रस्सी, निमित्तसे तीर्थोमें भ्रमण करती हुई गड्जा-तटपर
- **Translation**: 

---

