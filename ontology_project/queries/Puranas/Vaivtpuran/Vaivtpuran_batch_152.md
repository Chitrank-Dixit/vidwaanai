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

### Verse 1 (Vaivtpuran 10.9916)
- **Original**: काण्ड कैसे घटित हुआ ?' उनकी बात सुनकर मायाके स्वामी भगवान्‌ श्रीकृष्ण मायासे भूखे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 10.9917)
- **Original**: सब बालक बोले--गोपगण! सुनो। अवश्य ही बनकर दोनों चरण ऊपर फेंक-फेंककर रोने लगे।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 10.9918)
- **Original**: श्रीकृष्फे चरणोंका धक्का लगनेसे यह छकड़ा मुने ! उनके पास ही गोरसके मटकोंसे भरा हुआ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 10.9919)
- **Original**: टूटा है।' बालकोंकी यह बात सुनकर गोप और छकड़ा खड़ा था। श्रीकृष्णका एक पैर उससे जा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 10.9920)
- **Original**: गोषियाँ हँसने लगीं। उन्हें उनकी बातपर विश्वास लगा। विश्वम्भरके पैरका आघात लगनेसे वह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 10.9921)
- **Original**: नहीं हुआ। वे बोलीं-'बच्चोंकी बातें सत्य नहीं छकड़ा चूर-चूर हो गया। उस छकड़ेके टुकड़े-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 10.9922)
- **Original**: हैं।' तुरंत ही श्रेष्ठ ब्राह्मण आये और उन्होंने डुकड़े हो गये। उसके टूटे काठ वहीं बिखर गये।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 10.9923)
- **Original**: शिशुकी रक्षाके लिये स्वस्तिवाचन किया। एक उसपर लदा हुआ दही, दूध, माखन, घी और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 10.9924)
- **Original**: ब्राह्मणने शिशुके शरीरपर हाथ रखकर कवच मधु धरतीपर गिरकर बह चला। यह आश्चर्य देख
- **Translation**: 

---

### Verse 10 (Vaivtpuran 10.9925)
- **Original**: पढ़ा। विप्रवर! वह समस्त शुभ लक्षणोंसे युक्त भयसे व्याकुल हुई गोपियाँ बालकके पास दौड़ी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 10.9926)
- **Original**: कवच मैं तुम्हें बता रहा हूँ। यह बही कवच हुई आयोां। उन्होंने देखा छकड़ा टूट चुका है और है, जिसे पूर्वकालमें श्रीविष्णुके नाभिकमलपर बालक उसकी बिखरी हुई लकड़ियोंके भीतर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 10.9927)
- **Original**: विराजमान ब्रह्माजीकों भगवती योगमायाने दिया दबा है। टूटे-फूटे मटकोंका समूह तथा बहुत-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 10.9928)
- **Original**: था।उस समय जलमें शयन करनेवाले त्रिलोकोनाथ सा गोरस भी वहाँ गिरा दिया। लकड़ियोंको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 10.9929)
- **Original**: विष्णु जलके भीतर नींद ले रहे थे और ब्रह्माजी 4 82 का मधु-कैटभके भयसे डरकर योगनिद्राकी स्तुति कर रहे थे। उसी अवसरपर योगनिद्राने उन्हें थ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 10.9930)
- **Original**: कबचका उपदेश दिया था।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 10.9931)
- **Original**: . योगनिद्रा बोली--ब्रह्मन्‌! तुम अपना भय
- **Translation**: 

---

### Verse 17 (Vaivtpuran 10.9932)
- **Original**: दूर करो। जगत्पते! जहाँ श्रीहरि विराजमान हैं *
- **Translation**: 

---

### Verse 18 (Vaivtpuran 10.9933)
- **Original**: और मैं मौजूद हूँ, वहाँ तुम्हें भय किस बातका है? तुम यहाँ सुखपूर्वक रहो। श्रीहरि तुम्हारे मुखकी रक्षा करें। मधुसूदन मस्तककी, श्रीकृष्ण दोनों नेत्रोंकी तथा राधिकापति नासिकाकी रक्षा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 10.9934)
- **Original**: » श्रीकृष्णजन्मखण्ड + डंड7 ऋक्ष कक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 10.9935)
- **Original**: क# # ## #### 5555 ###### ## ऋक्ऋकऋऋड़ऊफऊऋक क्र # क्र 6%#%%%55 4 4 # 4 # केशव रक्षा करें। हषीकेश अधरोष्ठकी, गदाग्रज
- **Translation**: 

---

