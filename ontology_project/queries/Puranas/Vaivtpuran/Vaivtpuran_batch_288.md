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

### Verse 1 (Vaivtpuran 13.11902)
- **Original**: यदि उसे भस्म न करके त्याग ही दिया होता तपस्या कर रहे थे; उन्हें ध्यानसे अपनी पुत्रीके तो बह मेरे ही पास रह जाती।' फिर रोषसे मरणका तृत्तान्त ज्ञात हो गया। तब वे शोकाकुल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11903)
- **Original**: भरकर शाप दे दिया कि तुम्हारा पराभव होकर दुर्वासाके पास आये। दुर्वासाने श्वशुरको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11904)
- **Original**: होगा।' इतना कहकर मुनि और्व लौट गये। यह प्रणाम करके सब बातें बतायीं और उस घटित
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11905)
- **Original**: कथा सुनकर नारदजीने दुर्वासाके पराभवका घटनाके लिये महान्‌ दुःख प्रकट किया। मुनिवर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11906)
- **Original**: इतिहास पूछा। औदवरने दुर्वासाकों उलाहना दिया और कहा--' तुमने नारद बोले--भगवन्‌! दुर्वासा साक्षात्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11907)
- **Original**: + भ्रीकृष्णेजन्मखण्ड « 527 ऋऋ%%%##&###%$ %%% #ऋ कक # ## ##%$$%##### 7 # # 6&%$%$$%ऋकऋ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11908)
- **Original**: # # #### कक स्य्ण्नन्न्ननन् चल्ं___ंंअऑऑडड्स्5555:5:2525 05 4 40404040404.0./ ।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11909)
- **Original**: 0. 60444/।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11910)
- **Original**: भगवान्‌ शंकरके अंश हैं तथा तेजमें भी उन्हींके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11911)
- **Original**: थे। उनके कण्ठ, ओठ और तालु सूख गये थे। समान हैं। फिर कौन ऐसा महातेजस्वी पुरुष था,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11912)
- **Original**: मुनीन्द्रपर दृष्टि पड़ते ही राजाने उठकर उन्हें जिसने उनका भी पराभव कर दिया? प्रणाम किया और प्रसन्नतापूर्वक पैर धोनेके लिये भगवान्‌ श्रीनारायणने कहा--मुने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11913)
- **Original**: सूर्यबंशमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11914)
- **Original**: जल प्रस्तुत करके बैठनेको स्वर्णका सिंहासन अम्बरीष नामसे प्रसिद्ध एक राजाधिराज (सम्राट)
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11915)
- **Original**: दिया। विप्रवर दुर्वासा उन्हें आशीर्वाद देकर उस हो गये हैं। उनका मन सदा श्रीकृष्णके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11916)
- **Original**: सुखद आसनपर बैठे। तब राजाने भयभीत होकर चरणकमलोंके चिन्तनमें ही लगा रहता था।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11917)
- **Original**: उनसे पूछा--“मुने ! मेरे लिये आपकी क्या आज्ञा राज्यमें, रानियोंमें, पुत्रोंमें, प्रजाओंमें तथा पुण्य
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11918)
- **Original**: है? यह मुझे बताइये।' राजाकी बात सुनकर कर्मोद्वारा अर्जित की हुई सम्पत्तियोंमें भी उनका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11919)
- **Original**: मुनिवर दुर्वासाने कहा--'नृपश्रेष्ठ! मैं भूखसे चित्त क्षणभरके लिये भी नहीं लगता था। वे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11920)
- **Original**: पीड़ित होकर यहाँ आया हूँ। अत: मुझे भोजन धर्मात्मा नरेश दिन-रात सोते-जागते हर समय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11921)
- **Original**: कराओ; परंतु मैं अधमर्षण-मन्त्रका जप करके प्रसन्नतापूर्वक श्रीहरिका ध्यान किया करते थे।
- **Translation**: 

---

