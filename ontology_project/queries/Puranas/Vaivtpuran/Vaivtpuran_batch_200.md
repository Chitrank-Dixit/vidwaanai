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

### Verse 1 (Vaivtpuran 13.10142)
- **Original**: हो गये। उन्होंने अपने कौतृहलको छिपा लिया। विद्याधरियोंके नृत्य, भाव-भंगी तथा भ्रमणसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10143)
- **Original**: नन्दजीने नित्यकर्म करके पवित्र हो दो धुले वस्त्र नन्दप्राड्रणकी अपूर्व शोभा हो रही थी। उसके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10144)
- **Original**: धारण किये। चन्दन, अगुरु, कस्तूरी और केसरसे साथ ही गन्धर्वराजोंके मूर्छनायुक्त संगीत तथा । अपने ललाट आदि अन्ञोमें तिलक किया। इसके स्वर्ण-सिंहासनों एवं रथोंके सम्मिलित शब्द वहाँ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10145)
- **Original**: बाद गर्गजी तथा मुनीश्वरोंकी आज्ञा ले ब्रजेश्वर गूँज रहे थे।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10146)
- **Original**: नन्द दोनों पैर धोकर सोनेके मनोहर पीढ़ेपर बैठे। इसी समय संदेशवाहकने प्रसन्नतापूर्वक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10147)
- **Original**: उन्होंने श्रीविष्णुका स्मरण करके आचमन किया। आकर नन्दरायजीसे कहा--' प्रभो! आपके भाई-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10148)
- **Original**: फिर ब्राह्मणोंसे स्वस्तिबाचन कराकर वेदोक्त बन्धु गोपराज एवं गोपगण पधारे हैं। उनमेंसे [कर्मका सम्पादन करनेके अनन्तर बालककों कुछ लोग घोड़ोंपर चढ़कर आये हैं, कुछ
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10149)
- **Original**: भोजन कराया। आनन्दमग्न हुए नन्दजीने मुनिवर हाथियोंपर सवार हैं और कितने ही रथोंपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10150)
- **Original**: गर्गके कथनानुसार शुभ बेलामें बालकका मज्जलमय आरूढ़ हो शीपघ्रतापूर्वक पधारे हैं। रत्ममय
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10151)
- **Original**: नाम रखा-कृष्ण'। इस प्रकार जगदीश्वरको अलंकारोंसे विभूषित कितने ही राजपुत्रोंका भी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10152)
- **Original**: सघृत भोजन कराकर उनका नामकरण करनेके यहाँ शुभागमन हुआ है। पतली और सेवकोंसहित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10153)
- **Original**: अनन्तर नन्दरायने बाजे बजबाये और मज्जल- गिरिभानुजी पधारे हैं। उनके साथ चार-चार लाख
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10154)
- **Original**: कृत्य करवाये। उन्होंने ब्राह्मणोंको प्रसन्नतापूर्वक रथ और हाथी हैं। घोड़े और शिविकाओंकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10155)
- **Original**: नाना प्रकारके सुवर्ण, भाँति-भाँतिके धन, भक्ष्य संख्या एक-एक करोड़ है। ऋषीन्द्र, मुनीन्‍्द्र, । पदार्थ और वस्त्र दिये। बन्दीजनों और भिक्षुकोंको विद्वान, ब्राह्मण, बन्दीजन और भिक्षुकोंके समूह [इतनी अधिक मात्रामें उन्होंने सुवर्ण बाँठ कि भी निकट आ गये हैं। गोप और गोपियोंकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10156)
- **Original**: सुवर्णक भारी भारसे आक्रान्त होनेके कारण वे गणना करनेमें कौन समर्थ हो सकता है? आप
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10157)
- **Original**: सब-के-सब चल नहीं पाते थे। ब्राह्मणों, स्वयं बाहर चलकर देखें।' बन्धुजनों और विशेषतः भिक्षुकोंको भी उन्होंने आँगनमें खड़े हुए दूतने जब ऐसी बात
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10158)
- **Original**: पूर्णतया मनोहर मिष्ठान्नता भोजन कराया। उस कहीं, तब उसे सुनकर व्रजराज नन्दजी स्वयं उन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10159)
- **Original**: समय नन्दगोकुलमें बड़े जोर-जोरसे निरन्तर यही समागत अतिथियोंके पास आये। उन सबको साथ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10160)
- **Original**: शब्द सुनायी देता था कि “दो और दो।' 'खाओ- ले आकर उन्होंने आँगनमें बिठाया और तत्काल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10161)
- **Original**: खाओ'। परिपूर्ण रत्न, वस्त्र, आभूषण, मूँगे, ही उनका पूजन किया। ऋषि आदिके समुदायको
- **Translation**: 

---

