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

### Verse 1 (Vaivtpuran 15.8650)
- **Original**: मुक्त हो जाता है। पातकीके स्पर्शसे उस भक्तमें जीवॉपर दया है तथा जो सम्पूर्ण जगत्‌को श्रीकृष्ण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.8651)
- **Original**: जो पाप आता है, उसका नाश उसके अन्तः- जानता है, वह महाज्ञानी पुरुष ही वैष्णव भक्त
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.8652)
- **Original**: करणमें बैठे हुए भगवान्‌ मधुसूदन अवश्य कर माना गया है। जो निर्जन स्थानमें अथवा तीर्थोंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.8653)
- **Original**: देते हैं। ब्रह्मन्‌! इस प्रकार मैंने भगवान्‌ विष्णु सम्पर्कमें रहकर आसक्तिशून्य हो बड़े आनन्दके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.8654)
- **Original**: और वैष्णव भक्तके गुणोंका वर्णन किया है। अब साथ श्रीहरिके चरणारविन्दका चिन्तन करते हैं, वे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.8655)
- **Original**: मैं तुम्हें श्रीहरिके जन्मका प्रसड्र सुनाता हूँ, सुनो। वैष्णव माने गये हैं। जो सदा भगवान्‌के नाम और श्रीनारायणने कहा--एक बार गोलोकमें गुणका गान करते, मन्त्र जपते तथा कथा-दवार्ता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.8656)
- **Original**: श्रीकृष्ण विरजादेवीके समीप थे। श्रीराधाकों यह कहते-सुनते हैं, वे अत्यन्त वैष्णब हैं। मीठी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8657)
- **Original**: ठीक नहीं लगा। श्रीराधा सखियोंसहित वहाँ जाने वस्तुएँ पाकर श्रीहरिको प्रसन्नतापूर्वक भोग लगानेके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8658)
- **Original**: लगीं। तब श्रीदामने उन्हें रोका। इसपर श्रीराधाने लिये जिसका मन हर्षसे खिल उठता है, वह
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8659)
- **Original**: श्रीदामको शाप दे दिया कि “तुम असुरयोगिको ज्ञानियोमें श्रेष्ठ भक्त है। जिसका मन सोते, जागते,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8660)
- **Original**: प्रात हो जाओ।' तब श्रीदामने भी श्रीराधाको दिन-रात श्रीहरिके चरणारविन्दमें ही लगा रहता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8661)
- **Original**: यह शाप दिया कि “आप भी मानवी-योनिमें है और जो बाह्य शरीरसे पूर्व कर्मॉंका फल भोगता
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8662)
- **Original**: जाये। वहाँ गोकुलमें श्रीहरिके हो अंश महायोगी है, वह वैष्णव है। तीर्थ सदा वैष्णबॉके दर्शन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8663)
- **Original**: रायाण नामक एक वैश्य होंगे। आपका छायारूप और स्पर्शकी अभिलाषा करते हैं; क्योंकि उनके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8664)
- **Original**: उनके साथ रहेगा। अतएब भूतलपर मूढ़ लोग सड्से उन तीर्थोंके वे सारे पाप नष्ट हो जाते हैं, , आपको रायाणकी पत्नी समझेंगे, श्रीहरिके साथ जो उन्हें पापियोंके संसर्गसे मिले होते हैं। जितनी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8665)
- **Original**: कुछ समय आपका विछोह रहेगा।' देरमें गाय दुही जाती है, उतनी देर भी जहाँ। इससे श्रीदाम और श्रीराधा दोनोंको ही क्षोभ वैष्णव पुरुष ठहर जाता है, वहाँकी धरतीपर उतने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8666)
- **Original**: हुआ। तब श्रीकृष्णने श्रीदामको सान्त्वना देकर समयके लिये सम्पूर्ण तीर्थ निवास करते हैं। वहाँ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8667)
- **Original**: कहा कि “तुम त्रिभुवनविजेता सर्वश्रेष्ठ शह्बुचूड मरा हुआ पापी मनुष्य निश्चय ही पापमुक्त हो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.8668)
- **Original**: नामक असुर होओगे और अन्तमें श्रीशंकरके श्रीहरिके धाममें वैसे ही चला जाता है, जैसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.8669)
- **Original**: त्रिशूलसे भिन्न-देह होकर यहाँ मेरे पास लौट अन्तकालमें श्रीकृष्णकी स्मृति होनेपर अथवा
- **Translation**: 

---

