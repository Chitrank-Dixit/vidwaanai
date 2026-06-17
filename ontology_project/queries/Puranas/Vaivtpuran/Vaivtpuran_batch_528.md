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

### Verse 1 (Vaivtpuran 32.7697)
- **Original**: फिर प्रातःकाल ग्रामके अधिदेवताका रुदन विवाहोत्सव मनाया जा रहा है, जिसमें सभी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.7698)
- **Original**: सुनकर मैं जाग पड़ा। अब बतलाओ, इसका गायक गीत गा रहे हैं और नाच रहे हैं। रातमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.7699)
- **Original**: क्या उपाय है। राजाकी बात सुनकर मनोरमाका देखा कि लोग रमण कर रहे हैं, परस्पर हृदय दुःखी हो गया। वह रोती हुई राजाधिराज खींचातानी कर रहे हैं और कौवे तथा कुत्ते लड़
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.7700)
- **Original**: कार्तवीर्यसे गढ़द वाणीमें बोली। रहे हैं। कामिनि! रातमें मोटक, पिण्ड, शवसंयुक्त
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.7701)
- **Original**: मनोरमाने कहा--हे नाथ! आप रमण श्मशान, लाल वस्त्र और सफेद बस्त्र भी दीखे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.7702)
- **Original**: करनेवालोंमें उत्तम, समस्त महीपालॉमें श्रेष्ठ और हैं। शोभने! मैंने देखा कि एक विधवा स्त्री,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.7703)
- **Original**: मुझे प्राणोंसे भी अधिक प्रिय हैं। प्राणेश्वर! मेरा जो काले रंगकीो थी और काला वस्त्र पहने हुए
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.7704)
- **Original**: शुभकारक बचन सुनिये। जमदग्निनन्दन महाबली थी तथा जिसके बाल खुले हुए थे, नंगी होकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.7705)
- **Original**: भगवान्‌ परशुराम नारायणके अंश हैं। ये सृष्टिका मेरा आलिड्भन कर रही है। प्रिये! नाई मेरे सिर । संहार करनेवाले जगदीश्वर शिवके शिष्य हैं। तथा दाढ़ीके बाल छील रहा है और वक्ष:स्थलपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.7706)
- **Original**: जिनकी ऐसी प्रतिज्ञा है कि मैं इक्कीस बार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.7707)
- **Original**: +* गणपतिस्रण्ड » 367 है [[][[]/[]]4/4004
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.7708)
- **Original**: 3,44404504004050333333343434544354*3>अअय्वब् डे पृथ्वीको भूपालोंसे शून्य कर दूँगा, उनके साथ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.7709)
- **Original**: कुछ कहा है, वह सब मैंने सुन लिया। अब आप युद्ध न छेड़िये। पापी रावणको जीतकर जो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.7710)
- **Original**: मैं जो कहता हूँ, उसे श्रवण करो। शोकपीड़ित आप अपनेकों शूरवीर मानते हैं, (यह आपका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.7711)
- **Original**: लोगोंके वचन सभाओंमें प्रशंसनीय नहीं माने भ्रम है; क्योंकि) उसे आपने नहीं जीता है,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.7712)
- **Original**: जाते। सुन्दरी! कर्मभोगके योग्य काल आनेपर बल्कि वह अपने पापसे पराजित हुआ है; क्योंकि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7713)
- **Original**: सुख, दुःख, भय, शोक, कलह और प्रेम-ये जो धर्मकी रक्षा नहीं करता, उसका भूतलपर कौन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7714)
- **Original**: सभी होते रहते हैं; क्योंकि काल राज्य देता है; रक्षक हो सकता है? वह मूर्ख स्वयं नष्ट हो जाता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7715)
- **Original**: काल मृत्यु और पुनर्जन्‍्मका कारण होता है, काल है और वह जीते हुए भी मृतकके समान है। जो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7716)
- **Original**: संसारकी सृष्टि करता है, काल ही पुनः उसका धर्मके तथा शुभाशुभ कर्मके साक्षी और आत्माराम
- **Translation**: 

---

