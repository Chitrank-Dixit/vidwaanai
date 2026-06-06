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

### Verse 1 (Vaivtpuran 15.8710)
- **Original**: यों कहकर वसुधा बार-बार रोने लगी। निन्‍्दा करने लगते हैं। जगत्पिता आपने मेरी सृष्टि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.8711)
- **Original**: उसका रोदन सुनकर कृपानिधान ब्रह्माने उससे की है; अतः आपसे अपने मनकी बात कहनेमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.8712)
- **Original**: कहा--'वसुधे ! तुम्हारे ऊपर जो दस्युभूत राजाओंका मुझे कोई संकोच नहीं है। मैं जिनके भारसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.8713)
- **Original**: भार आ गया है, मैं किसी उपायसे अवश्य ही पीड़ित हूँ, उनका परिचय देती हूँ, सुनिये।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.8714)
- **Original**: उसे हटाऊँगा।' 'जो श्रीकृष्णभक्तिसे हीन हैं और जो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.8715)
- **Original**: पृथ्वीोकों इस प्रकार आश्वासन देकर श्रीकृष्ण-भक्तकी निन्‍्दा करते हैं, उन महापातकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.8716)
- **Original**: देवताओंसहित जगद्धाता ब्रह्मा भगवान्‌ शंकरके मनुष्योंका भार वहन करनेमें मैं सर्वथा असमर्थ
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8717)
- **Original**: निवासस्थान कैलास पर्वतपर गये। वहाँ पहुँचकर हूँ। जो अपने धर्मके आचरणसे शून्य तथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8718)
- **Original**: विधाताने कैलासके रमणीय आश्रम तथा भगवान्‌ नित्यकर्मसे रहित हैं, जिनकी वेदोंमें श्रद्धा नहीं शंकरको देखा। वे गड्भाजीके तटपर अक्षयवटके है; उनके भारसे मैं पीड़ित हूँ। जो पिता, माता,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8719)
- **Original**: नीचे बैठे हुए थे। उन्होंने व्याप्रचर्म पहन रखा गुरु, स्त्री, पुत्र तथा पोष्य-वर्गका पालन-पोषण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8720)
- **Original**: था। दक्षकन्याकी हड्डियोंके आभूषणसे वे विभूषित नहीं करते हैं; उनका भार वहन करनेमें मैं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8721)
- **Original**: थे। उन्होंने हाथोंमें त्रिशूल और पट्टिश धारण असमर्थ हूँ। पिताजी! जो मिथ्यावादी हैं, जिनमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8722)
- **Original**: कर रखे थे। उनके पाँच मुख और प्रत्येक मुखमें दया और सत्यका अभाव है तथा जो गुरुजनों
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8723)
- **Original**: तीन-तीन नेत्र थे। अनेकानेक सिद्धोंने उन्हें घेर और देवताओंकी निन्‍दा करते हैं; उनके भारसे [रखा था। बे योगीन्रगणसे सेवित थे और मुझे बड़ी पीड़ा होती है। जो मित्रद्रोही, कृतप्र,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8724)
- **Original**: कौतृहलपूर्वक गन्धवॉका संगीत सुन रहे थे। साथ झूठी गवाही देनेवाले, विश्वासघाती तथा धरोहर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8725)
- **Original**: ही अपनी ओर देखती हुई पार्वतीकी ओर हड़प लेनेवाले हैं; उनके भारसे भी मैं पीड़ित
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8726)
- **Original**: प्रेमपूर्वक तिरछी नजरसे देख लेते थे। अपने पाँच रहती हूँ। जो कल्याणमय सूक्तों, साम-मन्त्रों तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8727)
- **Original**: मुखोंद्वारा श्रीहरिके एकमात्र मज्जल नामका जप एकमात्र मड्भलकारी श्रीहरिके नामॉका विक्रय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.8728)
- **Original**: करते थे। गड्जाजीमें उत्पन्न कमलोंके बीजोंको करते हैं; उनके भारसे मुझे बड़ा कष्ट होता है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.8729)
- **Original**: मालासे जप करते समय उनके शरीरमें रोमाझ जो जीवघाती, गुरुद्रोही, ग्रामपुरोहित, लोभी, मुर्दा
- **Translation**: 

---

