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

### Verse 1 (Vaivtpuran 35.7902)
- **Original**: कवचस्य प्रसादेन जीवन्मुक्तो. भवेन्नर: । सर्वज्ञ: सर्वसिद्धीशो मनोयायी भवेद्‌ घुवम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7903)
- **Original**: इंदे कव॒चमज्ञात्वा भजेद्‌ यः शंकर प्रभुम्‌ । शतलक्षप्रज्तोतपि न मज्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7904)
- **Original**: (गणपतिखण्ड 35। 114-139)
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.7905)
- **Original**: 374 + संक्षिप्त ब्रह्मवैयर्तपुराण « ।77(4/[00[4+]777)][]]]]]।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.7906)
- **Original**: 8 8 । 4] %#####%# अम्बिकाका मन प्रसन्न हो गया और “भय मत
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.7907)
- **Original**: विनाश करनेवाला, अत्यन्त पूजनीय, प्रशंसनीय करो' यों कहकर वे वहीँ अन्तर्धान हो गयीं। जो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.7908)
- **Original**: और त्रिलोकौपर विजय पानेका कारण है। वह मनुष्य भक्तिपूर्वक इस परशुरामकृत स्तोत्रका पाठ
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.7909)
- **Original**: कवच जिसके गलेमें वर्तमान है, उसे जीतनेके करता है, वह अनायास ही महान्‌ भयसे छूट
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.7910)
- **Original**: लिये भूतलपर तुम कैसे समर्थ हो सकते हो? जाता है। वह त्रिलोकौमें पूजित, त्रैलेक्यविजयी,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.7911)
- **Original**: अतः भार्गव! तुम भिक्षाके लिये जाओ और ज्ञानियोंमें श्रेष्ठ और शत्रुपक्षका विमर्दन करनेवाला
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.7912)
- **Original**: राजासे प्रार्थना करो। सूर्यवंशमें उत्पन्न हुआ वह हो जाता है*। इसी बीच ब्रह्माजी धर्मात्माओंमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.7913)
- **Original**: राजा परम धर्मात्मा एवं दानी है। माँगनेपर बह श्रेष्ठ भूगुवंशी परशुरामके पास आकर उनसे उस
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.7914)
- **Original**: निश्चय ही प्राण, कवच, मन्त्र आदि सब कुछ रहस्यका वर्णन करने लगे।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.7915)
- **Original**: दे डालेगा। ब्रह्माजी बोले--महाभाग राम! अपनी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.7916)
- **Original**: मुने! तब परशुराम संन्‍्यासीका वेष धारण प्रतिज्ञा सफल करनेके लिये पहले तुम सुचन्द्रको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.7917)
- **Original**: करके राजाके पास गये और उससे उन्होंने मन्त्र विजयके हेतुभूत रहस्यका मुझसे श्रवण करो। तथा परम अद्भुत कवचकी याचना कौ। तब पूर्वकालमें दुर्वासाने सुचन्द्रको दशाक्षरी महाविद्या राजाने अत्यन्त आदरपूर्वक उन्हें मन्त्र और तथा भद्गरकालीका परम दुर्लभ कवच प्रदान किया
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.7918)
- **Original**: कवच दे दिया। तदनन्तर परशुरामने शंकरजीके था। भद्रकालीका कवच देवताओंके लिये भी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.7919)
- **Original**: त्रिशूलसे उस राजाका काम तमाम कर दिया। अत्यन्त दुर्लभ है। वह कबच सम्पूर्ण शत्रुओंका (अध्याय 36) 24543 दशाक्षरी विद्या तथा काली-कवचका वर्णन नारदजीने कहा--सर्वज्ञ नाथ! अब मैं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.7920)
- **Original**: कबचका वर्णन करता हूँ, सुनो। “30 हीं भ्रीं आपके मुखसे भद्रकाली-कवच तथा उस दशाक्षरी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.7921)
- **Original**: क्लीं कालिकायै स्वाहा' यही दशाक्षरी विद्या विद्याको सुनना चाहता हूँ। है। इसे पुष्करतीर्थमें सूर्य-ग्रहणके अवसरपर श्रीनारायण बोले--नारद! मैं दशाक्षरी
- **Translation**: 

---

