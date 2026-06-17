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

### Verse 1 (Vaivtpuran 16.3274)
- **Original**: व्यवस्थाके अनुसार ही हो रहा है। अत: सम्पूर्ण जोड़कर बड़ी विनयके साथ भगवान्‌ श्रीहरिके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3275)
- **Original**: मायाओंका पूर्ण ज्ञाता अपार बलशाली योगीश सामने सारी परिस्थिति निवेदित की। श्रीहरि सर्वत्र
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3276)
- **Original**: यह शह्बुचूड़ समयपर पुनः उस गोलोकमें ही एवं सबके अभिभप्रायसे पूर्ण परिचित हैं। ब्रह्माकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3277)
- **Original**: चला जायगा। आप लोग मेरा यह त्रिशूल लेकर बात सुनकर उनके मुखपर हँसी छा गयी और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3278)
- **Original**: शीघ्र भारतवर्षमें चलें। शंकर मेरे त्रिशुलसे उस उन्होंने मनको मुग्ध करनेवाला अद्भुत रहस्य
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3279)
- **Original**: दानवका संहार करें। दानव शह्लुचूड़ मेरे ही कहना आरम्भ किया। सम्पूर्ण मडल प्रदान करनेवाले कवचोंकों कण्ठमें भगवान्‌ श्रीहरि बोले--ब्रह्मन्‌! यह महान्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3280)
- **Original**: सदा धारण किये रहता है; इसीलिये वह अखिल तेजस्वी शह्लुचूड़ पूर्वजन्ममें एक गोप था। यह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3281)
- **Original**: विश्वविजयी है। ब्रह्म! उसके कण्ठमें कवच मेरा ही अंश था। मेरे प्रति इसकी अदूट श्रद्धा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3282)
- **Original**: रहते हुए कोई भी उसे मारनेमें सफल नहीं हो थी। इसके सम्पूर्ण वृत्तान्तसे मैं पूर्ण परिचित हूँ।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3283)
- **Original**: सकता। अत: मैं ही ब्राह्मणका वेष धारण करके यह वृत्तान्त एक पुराना इतिहास है। गोलोकसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3284)
- **Original**: कबचके लिये उससे याचना करूँगा। साथ ही सम्बन्ध रखनेवाले इस समस्त पुण्यप्रद इतिहासकों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3285)
- **Original**: जिस समय उसकी स्त्रीका सतीत्व नष्ट होगा, सुनिये। शट्बचूड़ उस समय सुदामा नामसे प्रसिद्ध
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3286)
- **Original**: उसी समय उसकी मृत्यु होगी-यह आपने गोप था। मेरे पार्षदोंमें उसकी प्रधानता थी।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3287)
- **Original**: उसको वर दे रखा है। एतदर्थ उसकी पत्नीके श्रीराधाके शापने उसे दानव-योनिमें उत्पन्न होनेके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3288)
- **Original**: उदरमें मैं बीर्य स्थापित करूँगा-मैंने यह निश्चित लिये विवश कर दिया। कर लिया है। (वैसे 'तुलसी' मेरी नित्यप्रिया राधा अति करुणामयी हैं। सखियोंका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3289)
- **Original**: है, इससे वस्तुत: मुझ सर्वात्माकों कोई दोष भी तिरस्कार करनेके कारण राधाने शाप तो दे दिया,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3290)
- **Original**: नहीं होगा।) उसी समय शह्भचूड़की मृत्यु हो परंतु जब सुदामा मुझे प्रणाम करके रोता हुआ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3291)
- **Original**: जायगी-इसमें कोई संदेह नहीं है। तदनन्तर उस सभाभवनसे बाहर जाने लगा, तब दयामयी राधा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3292)
- **Original**: दानवकी यह पत्नी अपने उस शरीरकों त्यागकर कृपावश तुरंत संतुष्ट हो गयीं। उनकी आँखोंमें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3293)
- **Original**: पुनः मेरी प्रिय पत्नी बन जायगी। आँसू भर आये। उन्होंने सुदामाको रोक लिया। नारद! इस प्रकार कहकर जगत्प्रभु भगवान्‌ कहा--'वत्स! रुके रहो, मत जाओ, कहाँ
- **Translation**: 

---

