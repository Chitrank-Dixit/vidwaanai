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

### Verse 1 (Vaivtpuran 13.10242)
- **Original**: ब्राह्मणों और बन्दीजनोंने बालकको शुभ आशीर्वाद खड़े हो गये। नन्‍्दरानी उनका हाथ पकड़कर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10243)
- **Original**: दिये। सबने मिलकर ब्राह्मणोंसे श्रीहरिका नाम- अपने घर ले आयीं। उन्होंने मधुसूदनको वस्त्रसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10244)
- **Original**: कौर्तन करवाया। वृक्षमें बाँध दिया। श्रीकृष्फो बाँधकर यशोदा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10245)
- **Original**: नारदजीने पूछा-- भगवन्‌! वह सुन्दर वेषधारी अपने घरमें चली गयीं तथा जगत्पति परमेश्वर पुरुष कौन था, जो गोकुलमें वृक्ष होकर रहता श्रीहरि वृक्षकी जड़के पास खड़े रहे। नारद!
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10246)
- **Original**: था? किस कारणसे उसे वृक्ष होना पड़ा था? श्रीकृष्णके स्पर्शमात्रसे वह पर्वताकार वृक्ष सहसा भगवान्‌ नारायण बोले--एक बार कुबेरपुत्र भयानक शब्द करके वहाँ गिर पड़ा। उस वृक्षसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10247)
- **Original**: नलकूबर अप्सरा रम्भाके साथ नन्दनवनमें चला सुन्दर वेषधारी एक दिव्य पुरुष प्रकट हुआ।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10248)
- **Original**: गया। वहाँ उसने भाँति-भाँतिसे बिहार किये। इसी वह रत्लमव अलंकारोंसे विभूषित, गौरवर्ण तथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10249)
- **Original**: समय महर्षि देवल उधरसे निकले। उनकी दृष्टि किशोर-अवस्थाका था। सुवर्णमय श्रृज्धास्से। नलकूबर और रम्भापर पड़ गयी। इधर मुनिको विभूषित जगदीश्वर श्रीकृष्णको प्रणाम करके वह देखकर भी नलकूबर-रम्भाने उठकर उनका दिव्य पुरुष मुस्कराता हुआ दिव्य रथपर आरूढ़
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10250)
- **Original**: सम्मान नहीं किया। मुनिवर देवल उन दोनोंकी हुआ और अपने घरको चला गया। वृक्षको गिरते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10251)
- **Original**: ऐसी दुर्वृत्ति देखकर कुपित हो गये और उन्हें देख ब्रजेश्वरी यशोदा भयसे त्रस्त हो उठीं। उन्होंने शाप देते हुए बोले--'नलकूबर! तुम गोकुलमें रोते हुए बालक श्यामसुन्दरकों उठाकर छातीसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10252)
- **Original**: जाकर वृक्षरूप धारण करो। फिर श्रीकृष्णका लगा लिया। इतनेमें ही गोकुलके गोप और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10253)
- **Original**: स्पर्श पानेपर अपने भवनमें लौट आओगे और गोपियाँ उनके घरमें आ पहुँचीं। वे सब-की-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10254)
- **Original**: रम्भा! तुम भी मनुष्ययोनिमें जन्म लेकरं राजा सब यशोदाको फटकारने लगीं। उन्होंने प्रसन्नतापूर्वकत
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10255)
- **Original**: जनमेजयकी . सौभाग्यशालिनी पत्नी बनो। शिशुकी रक्षाके लिये शान्तिकर्म किया। अश्वमेधयज्ञमें इन्द्रका स्पर्श पाकर तुम पुनः सब गोपियाँ बशोदासे कहने लगीं--
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10256)
- **Original**: स्वर्गमें चली जाओगी।' नन्दरानी ! अत्यन्त वृद्धावस्थामें तुम्हें यह पुत्र प्रात. बह नलकूबर ही यह वृक्ष बना और रम्भाने हुआ है। संसारमें जो भी धन, धान्य तथा रत्न
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10257)
- **Original**: भारतमें राजा सुचन्द्रको कन्यारूपसे जन्म लेकर है, वह सब पुत्रके लिये ही है। आज हमने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10258)
- **Original**: जनमेजयकी महारानी बननेका सौभाग्य प्राप्त किया। सचमुच यह जान लिया कि तुम्हारे भीतर सुबुद्धि
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10259)
- **Original**: जनमेजयके अश्वमेधयज्ञमें इन्द्रने महारानीको स्पर्श नहीं है। जो खाद्यपदार्थ पुत्रने नहीं खाया, वह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10260)
- **Original**: कर लिया। इससे उसने योगावलम्बन करके सब इस भूतलपर निष्फल ही है। ओ निध्ठ॒ुरे!
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10261)
- **Original**: देहको त्याग दिया और वह स्वर्गधामको चली तुमने दही-दूधके लिये अपने लालाको वृक्षकी
- **Translation**: 

---

