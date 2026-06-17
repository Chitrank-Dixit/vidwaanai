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

### Verse 1 (Vaivtpuran 543.13134)
- **Original**: पुलकित हो रहा था। देवी शिवाके मुखपर भी चाहती हो; परंतु वे तो निराकार हैं! निराकारको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13135)
- **Original**: प्रसन्नता थी। उसने सखियोंसहित निकट जा पति बनाकर तुम्हारा कौन-सा मनोरथ सिद्ध
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13136)
- **Original**: माता-पिताकों प्रणाम किया। तब उन दोनोंने होगा? शुचिस्मिते ! यदि संहारकर्ता हरको स्वामो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13137)
- **Original**: आशीर्वाद देकर पुत्रीकों हृदयसे लगा लिया और बनानेकी इच्छा है तो यह भी ठौक नहीं है;
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13138)
- **Original**: 'ओ मेरी बच्ची!" कहकर प्रेमसे विड्डल हो रोने क्योंकि कौन ऐसी स्त्री है जो सर्वसंहारकारीको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13139)
- **Original**: लगे। उस समय दुर्गाको रथपर बिठाकर वे दोनों अपना कान्त (प्राणवल्लभ) बनानेकी इच्छा करेगी ?
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13140)
- **Original**: अपने घर गये। स््रियोंने निर्मब्छय किया और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13141)
- **Original**: + श्रीकृष्णजन्मखण्ड * 573 ऋ%ऋऋ#ऋ% 4 ऋ $% 4 % $ % # # % 4 # 6 ## ऋऋ# ऋ$ $ $ $ $ 4 % # #ऋ 5555 #% 86 #% ###5$%# %%%44 44464 %% 444 46 -ब्राह्मणोंने आशीर्वाद दिया। पर्वतराजने ब्राह्मणों
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13142)
- **Original**: मन-ही-मन उन्हें प्रणाम किया और वर माँगा, और बन्दीजनोंको धन दिया। उनसे वेद-पाठ और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13143)
- **Original**: ' आप हमारे पति हो जाइये।' 'एवमस्तु' कहकर मड्जल-पाठ करवाये। इस प्रकार वे दोनों अपनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13144)
- **Original**: शिव अन्तर्धान हो गये। हृदयमें शिवको न पुत्रीके साथ सुखसे घरमें रहने लगें। शिवाके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13145)
- **Original**: देखकर दुर्गाकी मूर्च्छा भड्ज हुई। उसने आँख आ जानेसे उनके मनमें बड़ा हर्ष था। .
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13146)
- **Original**: खोलकर देखा; सामने वही भिक्षुक गा रहा है। एक दिन हिमबान्‌ तप करनेके लिये
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13147)
- **Original**: भिक्षुके नृत्य और संगीतसे संतुष्ट हो मेना गज्जाजीके तटपर गये। मेना अपनी पुत्रीके साथ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13148)
- **Original**: सोनेके पात्रमें बहुत-से रत्र ले उसे देनेके लिये प्रसन्नतापूर्वक घरके आँगनमें बैठी थीं। इसी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13149)
- **Original**: गयीं; परंतु भिक्षुने भिक्षा्में दुर्गाकों ही माँगा; समय एक नाचने-गानेवाला भिक्षुक सहसा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13150)
- **Original**: दूसरी कोई वस्तु नहीं ली। वह कौतुकवश पुनः मेनाके पास आया। उसके बायें हाथमें सींगका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13151)
- **Original**: नृत्य करनेको उद्यत हुआ; परंतु मेना उसकी बात बाजा और दायें हाथमें डमरू था। बहुत ही [सुनकर कुपित हो उठी थीं। उन्हें आश्चर्य भी वृद्ध और जरासे अत्यन्त जर्जर हो चुका था।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13152)
- **Original**: हुआ था। उन्होंने भिश्षुकको बहुत डाँटा तथा उसने सारे शरीरमें विभूति लगा रखी थी। पीठपर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13153)
- **Original**: उसे घरसे बाहर निकाल देनेकी आज्ञा दी। इसी गुदड़ी लिये और लाल वस्त्र पहने वह भिक्षुक बीचमें अपना तप पूरा करके हिमवान्‌ घरपर बड़ा मनोहर जान पड़ता था। उसका कण्ठ बड़ा
- **Translation**: 

---

