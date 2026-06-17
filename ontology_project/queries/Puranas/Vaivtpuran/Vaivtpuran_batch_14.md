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

### Verse 1 (Vaivtpuran 0.461)
- **Original**: ज्ञानियोंमें श्रेष्ठ भगवान्‌ सनत्कुमार थे। इसके बाद नित्य, नैमित्तिक, द्विपरार्ध और प्राकृत-ये चार
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.462)
- **Original**: ब्रह्माणीक मुखसे सुवर्णके समान कान्तिमान्‌ प्रकारके प्रलय हैं। इन कल्पों और प्रलयोंकों तथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.463)
- **Original**: कुमार उत्पन्न हुआ, जो दिव्यरूपधारी था। उसके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.148)
- **Original**: एवं सर्वेश्वर हैं, वेद जिनका स्वरूप है, जो वेदोंके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.149)
- **Original**: उनके प्रत्येक मस्तकमें तीन-तीन नेत्र थे। उनके बीज, वेदोक्त फलके दाता और फलरूप हैं,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.150)
- **Original**: सिरपर चन्द्राकार मुकुट शोभा पाता था। परमेश्वर वेदोंके ज्ञाता, उसके विधानको जाननेवाले तथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.151)
- **Original**: शिवने हाथोंमें त्रिशूल, पट्टिश और जपमाला ले सम्पूर्ण बेदवेत्ताओंके शिरोमणि हैं, उन भगवान्‌ [रखी थी। वे सिद्ध तो हैं ही, सम्पूर्ण सिद्धोंके श्रोकृष्णको मैं प्रणाम करता हूँ।* ईश्वर भी हैं। योगियोंके गुरुके भी गुरु हैं। मृत्युकी ऐसा कहकर वे नारायणदेव भक्तिभावसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.152)
- **Original**: भी मृत्यु हैं, मृत्युके ईश्वर हैं, मृत्युस्वरूप हैं युक्त हो उनकी आज्ञासे उन परमात्माके सामने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.153)
- **Original**: और मृत्युपर विजय पानेवाले मृत्युञ्य हैं। वे रमणीय रत्रमय सिंहासनपर विराज गये। जो पुरुष
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.154)
- **Original**: ज्ञानानन्दरूप, महाज्ञानी, महान्‌ ज्ञानदाता तथा प्रतिदिन एकाग्रचित्त हो तीनों संध्याओंके समय
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.155)
- **Original**: सबसे श्रेष्ठ हैं। पूर्ण चन्द्रमाकी प्रभासे धुले हुए- नारायणद्वारा किये गये इस स्तोत्रको सुनता और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.156)
- **Original**: से गौरवर्ण शिवका दर्शन सुखपूर्वक होता है। पढ़ता है, वह निष्पाप हो जाता है। उसे यदि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.157)
- **Original**: उनकी आकृति मनको मोह लेती है। त्रह्मतेजसे पुत्रकी इच्छा हो तो पुत्र मिलता है और भार्याकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.158)
- **Original**: जाज्वल्यमान भगवान्‌ शिव वैष्णवोंके शिरोमणि इच्छा हो तो प्यारी भार्या प्राप्त होती है। जो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.159)
- **Original**: हैं। प्रकट होनेके पश्चात्‌ श्रीकृष्णके सामने खड़े अपने राज्यसे भ्रष्ट हो गया है, बह इस स्तोत्रके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.160)
- **Original**: हो भगवान्‌ शिवने भी हाथ जोड़कर उनका स्तवन पाठसे पुनः राज्य प्राप्त कर लेता है तथा धनसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.161)
- **Original**: किया। उस समय उनके सम्पूर्ण अज्जभोंमें रोमाश्ल बद्धित हुए पुरुषको धनकी प्राप्ति हो जाती है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.162)
- **Original**: हो आया था। नेत्रोंसे अश्रु झर रहे थे और उनकी कारागारके भीतर विपत्तिमें पड़ा हुआ मनुष्य यदि
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.163)
- **Original**: वाणी अत्यन्त गदद हो रही थी। इस स्तोत्रका पाठ करे तो निश्चय ही संकटसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.164)
- **Original**: महादेवजी बोले--जो जयके मूर्तिमान्‌ मुक्त हो जाता है। एक वर्षतक इसका संयमपूर्वक
- **Translation**: 

---

