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

### Verse 1 (Vaivtpuran 543.12394)
- **Original**: लिये पृथ्वीपर तुम्हारा निवास हुआ है; फिर तुम कुछ याद करती हो? क्‍या तुम्हें प्रेमशास्त्रके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12395)
- **Original**: मानवी स्त्री कैसे हो? तुम जन्म, मृत्यु और विद्वान्‌ तथा रतिचोर श्यामसुन्दरके उस चरित्रका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12396)
- **Original**: जराका नाश करनेवाली देवी हो। कलाबतीकी किश्चित्‌ भी स्मरण होता है, जो नारियोंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12397)
- **Original**: अयोनिजा पुत्री एवं पुण्यमयी हो; फिर तुम्हें चित्तको बरबस अपनी ओर खींच लेता है? तुम
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12398)
- **Original**: साधारण मानुषी कैसे माना जा सकता है? तीन श्रीकृष्णके अर्धाड्रसे प्रकट हुई हो; अत: उन्हींके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12399)
- **Original**: मास व्यतीत होनेपर जब मनोहर मधुमास (चैत्र) समान तेजस्विनी हो। समस्त देवाडुनाएँ तुम्हारी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12400)
- **Original**: उपस्थित होगा, तब रात्रिके समय निर्जन, निर्मल अंशकलासे प्रकट हुई हैं; फिर तुम मानवी कैसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12401)
- **Original**: एवं सुन्दर रासमण्डलमें वृन्दावनके भीतर श्रीहरिके हो? तुम श्रीहरिके लिये प्राणस्वरूपा हो और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12402)
- **Original**: साथ समस्त गोपिकाओंसहित तुम्हारी रासक्रीड़ा स्वयं श्रीहरि तुम्हारे प्राण हैं। बेदमें तुम दोनोंका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12403)
- **Original**: सानन्द सम्पन्न होगी। सती राधे! प्रत्येक कल्पमें भेद नहीं बताया गया है; फिर तुम मानवी कैसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12404)
- **Original**: भूतलपर श्रीहरिके साथ तुम्हारी रसमयी लीला हो? पूर्वकालमें ब्रह्माजी साठ हजार वर्षोतक तप
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12405)
- **Original**: होगी, यह विधाताने ही लिख दिया है। इसे कौन करके भी तुम्हारे चरणकमलोंका दर्शन न पा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12406)
- **Original**: रोक सकता है? सुन्दरी! श्रीहरिप्रिये! जैसे मैं सके; फिर तुम मानुषी कैसे हो? तुम तो महादेवजीकी सौभाग्यवती पत्नी हूँ, उसी प्रकार देवी हो। श्रीकृष्णकी आज्ञासे गोपीका रूप धारण
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12407)
- **Original**: तुम श्रीकृष्णकी सौभाग्यशालिनी वल्लभा हो। जैसे करके पृथ्वीपर पधारी हो; शान्ते! तुम मानवी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12408)
- **Original**: दूधमें धवलता, अग्नरिमें दाहिका शक्ति, भूमिमें स्त्री कैसे हो? मनुवंशमें उत्पन्न नृपश्रेष्ठ सुयज्ञ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12409)
- **Original**: गन्‍न्ध और जलमें शीतलता है; उसी प्रकार तुम्हारी ही कृपासे गोलोकमें गये थे; फिर तुम
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12410)
- **Original**: श्रीकृष्णमें तुम्हारी स्थिति है। देवाड़ना, मानवकन्या, मानुषी कैसे हो? तुम्हारे मन्त्र और कवचके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12411)
- **Original**: गन्धर्वजातिकौ स्त्री तथा राक्षसी-इनमेंसे कोई प्रभावसे ही भृगुबंशी परशुरामजीने इस पृथ्वीको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12412)
- **Original**: भी तुमसे बढ़कर सौभाग्यशालिनी न तो हुई है इक्कीस बार क्षत्रिय-नरेशोंसे शून्य कर दिया था।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12413)
- **Original**: और न होगी ही। मेरे वरसे ब्रह्मा आदिके भी ऐसी दशामें तुम्हें मानवी स्त्री कैसे कहा जा
- **Translation**: 

---

