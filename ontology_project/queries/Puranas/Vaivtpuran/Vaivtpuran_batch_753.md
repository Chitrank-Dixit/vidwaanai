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

### Verse 1 (Vaivtpuran 543.13374)
- **Original**: पीड़ित हुए समस्त देवताओंने इसके लिये उनका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13375)
- **Original**: अत: तुम्हीं बताओ पर्वतोंमें कौन-से ऐसे हैं, स्तबन किया है। देवताओंकी पीड़ा देखकर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13376)
- **Original**: जो देवताओंसे युद्ध कर सकें। पवनसे प्रेरित हो ब्रह्माजीके प्रार्थना करनेपर कृपालु भगवान्‌ शिवने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13377)
- **Original**: समस्त पर्वत एक ही क्षणमें समुद्रोंके भीतर जा कृपापूर्वक उनके इस अनुरोधको स्वीकार किया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13378)
- **Original**: गिरेंगे। शैलेन्द्र! यदि एकके लिये सारी सम्पत्तिका है। विवाहकी प्रतिज्ञा करके योगीन्द्र शिवने जब
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13379)
- **Original**: विनाश हो रहा हो तो उस एकको देकर शेष शिवाको असंख्य क्लेश उठाते देखा, तब तुम्हारी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13380)
- **Original**: सबकी रक्षा कर लेनी चाहिये; परंतु यह नियम पुत्रीकी तपस्याके स्थानमें वे स्वयं ब्राह्मणका रूप
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13381)
- **Original**: शरणागतके लिये लागू नहीं है। शरणागतको धारण करके आये और उसे आश्वासन तथा वर [ रक्षाके लिये तो अपने प्राणोंका परित्याग कर देकर पुनः अपने स्थानकों लौट गये। देना भी उचित है। फिर स्त्री, पुत्र, धन आदि गिरिराज! इस समाचारकों सुनकर ही इन्द्र
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13382)
- **Original**: अन्य सब वस्तुओंकी तो बात ही कया है? ऐसा आदि सब देवता प्रसन्नतापूर्वक यहाँ आये थे।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13383)
- **Original**: नीतिवेत्ताऑंका मत है। महाराज अनरण्य ब्राह्मणको भगवान्‌ नारायण, ब्रह्मा, धर्म, ऋषि-मुनि, गन्धर्व,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13384)
- **Original**: अपनी पुत्री देकर शापसे मुक्त हुए और अपनी यक्ष और राक्षस सब इस समय एक स्थानपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13385)
- **Original**: समस्त सम्पदाओंकी रक्षा कर सके। अनरण्य मिले और इस विषयपर सबने अच्छी तरह विचार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13386)
- **Original**: ब्राह्मणोंके हितकारी थे; परंतु उन्हींके शापमें किया। उन्हीं लोगोंने हमें शीघ्र यहाँ भेजा है।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13387)
- **Original**: डूबकर अत्यन्त कातर हो गये थे। उस समय देवी अरुन्धती अपने कर्तव्यका पालन करके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13388)
- **Original**: नोतिशास्त्रके विद्वानोंने उन्हें शीघ्र ही कर्तव्यका उऋण हो चुकी हैं। तुम्हें समझानेमें हमें सदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13389)
- **Original**: बोध कराया और उसको पालन करके वे संकटसे ही अधिक प्रसन्नता होती है; तुम्हारे सामने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13390)
- **Original**: मुक्त हुए। शैलेन्द्र! तुम भी शिवको अपनी पुत्री शिवाके विवाहका शुभ कार्य प्राप्त है, जो सब देकर समस्त बन्धुजनोंकी रक्षा करो और कालमें सुख देनेवाला है। शैलेद्र ! यदि स्वेच्छापूर्वक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13391)
- **Original**: देवताओंको भी अधीन बना लो। शिवाका विवाह शिवके साथ नहीं करोगे तो भी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13392)
- **Original**: . वसिष्ठजीकी बात सुनकर पर्वतेश्वर हँसे; वह होकर ही रहेगा; क्योंकि भवितव्यता प्रबल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13393)
- **Original**: उन्होंने व्यथित हृदयसे राजा अनरण्यका वृत्तान्त होती है। वे महादेवजी रत्नसारनिर्मित रथपर
- **Translation**: 

---

