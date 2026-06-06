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

### Verse 1 (Vaivtpuran 44.8397)
- **Original**: है; अत: जिनका बल सबसे बढ़कर है; उन निस्संदेह उसीके समान होते हैं। गुरुकी स्त्री और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 44.8398)
- **Original**: 'एकदन्त' को मैं नमस्कार करता हूँ। ' हे' दीनार्थवाचक पुत्रकी परशुरामने अवहेलना कर दी है, उसीका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 44.8399)
- **Original**: और 'रम्ब' पालकका वाचक है; अत: दीनोंका सम्मार्जन करनेके लिये मैं तुम्हारे घर आया हूँ।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 44.8400)
- **Original**: पालन करनेवाले 'हेरम्ब' को मैं शीश नवाता हूँ। श्रीनारायण कहते हैं--नारद ! वहाँ भगवान्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 44.8401)
- **Original**: 'विध्र' विपत्तिवाचक और 'नायक' खण्डनार्थक विष्णु शिवजीसे ऐसा कहकर दुर्गाकों समझाते है, इस प्रकार जो विपत्तिके बिनाशक हैं; उन हुए सत्यके साररूप उत्तम बचन बोले। *बिप्ननायक' को मैं अभिवादन करता हूँ। पूर्वकालमें विष्णुने कहा--देवि! मैं नीतियुक्त, वेदका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 44.8402)
- **Original**: विष्णुद्वारा दिये गये नैवेद्यों तथा पिताद्वारा समर्पित तत्त्वरूप तथा परिणाममें सुखदायक वचन कहता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 44.8403)
- **Original**: अनेक प्रकारके मिष्टान्नोंक खानेसे जिनका उदर हूँ, मेरे उस शुभ वचनको सुनो। गिरिराजकिशोरी !
- **Translation**: 

---

### Verse 8 (Vaivtpuran 44.8404)
- **Original**: लम्बा हो गया है; उन “लम्बोदर' की मैं वन्दना तुम्हिरे लिये जैसे गणेश और कार्तिकेय हैं,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 44.8405)
- **Original**: करता हूँ। जिनके कर्ण शूर्पाकार, विश्न-निवारणके निस्संदेह उसी प्रकार भृगुबंशी परशुराम भी हैं।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 44.8406)
- **Original**: हेतु, सम्पदाके दाता और ज्ञानरूप हैं; उन ' शूर्पकर्ण' सर्वज्ञे! इनके प्रति तुम्हिर अथवा शंकरजीके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 44.8407)
- **Original**: को मैं सिर झुकाता हूँ। जिनके मस्तकपर मुनिद्वारा स्रेहमें भेदभाव नहीं है। अत: मात:! सबपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.8408)
- **Original**: दिया गया विष्णुका प्रसादरूप पुष्प वर्तमान है और विचार करके जैसा उचित हो, वैसा करो। पुत्रके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.8409)
- **Original**: जो गजेन्द्रके मुखसे युक्त हैं; उन “गजवक्त्र' को मैं साथ पुत्रका यह विवाद तो दैवदोषसे घटित हुआ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.8410)
- **Original**: नमस्कार करता हूँ। जो गुह (स्कन्द)-से पहले है। भला, दैवको मिटानेमें कौन समर्थ हो सकता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.8411)
- **Original**: जन्म लेकर शिव-भवनमें आविर्भूत हुए हैं तथा है? क्योंकि दैव महाबली है। वत्से ! देखो, तुम्हारे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.8412)
- **Original**: समस्त देवगणोंमें जिनकी अग्रपूजा होती है; उन पुत्रका 'एकदन्त' नाम वेदोंमें विख्यात है।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 44.8413)
- **Original**: '“गुहाग्रज' देवकी मैं वनदना करता हूँ। दुर्गे! अपने वरानने ! सभी देव उसे नमस्कार करते हैं। ईश्वरि !
- **Translation**: 

---

### Verse 18 (Vaivtpuran 44.8414)
- **Original**: पुत्रके नामोंसे संयुक्त इस उत्तम नामाष्टक स्तोत्रको सामवेदमें कहे हुए अपने पुत्रके नामाष्टक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 44.8415)
- **Original**: पहले वेदमें देख लो, तब ऐसा क्रोध करो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 44.8416)
- **Original**: जो इस स्तोत्रकों ध्यान देकर श्रवण करो। मातः! वह
- **Translation**: 

---

