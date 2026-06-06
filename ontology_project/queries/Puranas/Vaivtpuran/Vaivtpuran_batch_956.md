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

### Verse 1 (Vaivtpuran 543.17434)
- **Original**: गोपियाँ वहाँ आ पहुँचीं। तब राधाने नन्‍्द पर्वतपर गयीं। वहाँ उन्होंने अनेक प्रकारके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17435)
- **Original**: आदिके लिये पृथक्‌-पृथक्‌ आवासस्थानकी मणिसमूहोंसे व्याप्त सुसज्जित रासमण्डलकों देखा।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17436)
- **Original**: व्यवस्था की। तदनन्तर परमानन्दरूपा गोपिका उससे कुछ दूर आगे जानेपर पुण्यमय वृन्दावन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17437)
- **Original**: राधा परमानन्दपूर्वक सबके साथ अपने परम मिला। आगे बढ़नेपर अक्षयव॒ट दिखायी दिया,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17438)
- **Original**: रुचिर भवनको प्रस्थित हुईं। (अध्याय 127) हज जऑलय 0221 ,00000 श्रीकृष्णके गोलोकगमनका वर्णन श्रीनारायण कहते हैं--नारद! परिपूर्णतम श्रीभगवानने कहा-- है गोपगण! हे बन्धो! प्रभु भगवान्‌ श्रीकृष्ण वहाँ तत्काल ही गोकुलवासियोंके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17439)
- **Original**: तुम लोग सुखका उपभोग करते हुए शान्तिपूर्वक सालोक्य मोक्षको देखकर भाण्डीरबनमें बटवृक्षके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17440)
- **Original**: यहाँ वास करो; क्योंकि प्रियाके साथ विहार, नीचे पाँच गोपोंके साथ ठहर गये। वहाँ उन्होंने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17441)
- **Original**: सुरम्य रासमण्डल और वृन्दावन नामक पुण्यवनमें देखा कि सारा गोकुल तथा गो-समुदाय व्याकुल
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17442)
- **Original**: श्रोकृष्णका निरन्तर निवास तबतक रहेगा, जबतक है। रक्षकोंके न रहनेसे वृन्दावन शुन्य तथा अस्त-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17443)
- **Original**: सूर्य और चन्द्रमाकी स्थिति रहेगी। तत्पश्चात्‌ व्यस्त हो गया है। तब उन कृपासागरकों दया आ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17444)
- **Original**: लोकोंके विधाता ब्रह्मा भो भाण्डीरवनमें आये। गयी। फिर तो, उन्होंने योगधारणाद्वारा अमृतकी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17445)
- **Original**: उनके पीछे स्वयं शेष, धर्म, भवानीके साथ स्वयं वर्षा करके वृन्दावनकों मनोहर, सुरम्य और गोपों
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17446)
- **Original**: शंकर, सूर्य, महेद्ध, चन्द्र, अग्नि, कुबेर, बरुण, तथा गोपियोंसे परिपूर्ण कर दिया। साथ ही
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17447)
- **Original**: पवन, यम, ईशान आदि देव, आठों वसु, सभी ग्रह, गोकुलवासी गोपोंको ढाढस भी बँधाया। तत्पश्चात्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17448)
- **Original**: रुद्र, मुनि तथा मनु-ये सभी शीघप्रतापूर्बक वहाँ वे हितकर नीतियुक्त दुर्लभ मधुर बचन बोले।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17449)
- **Original**: आ पहुँचे, जहाँ सामर्थ्यशाली भगवान्‌ श्रीकृष्ण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17450)
- **Original**: 772 « संक्षिप्त ब्रह्म॑वैयर्तपुराण * ।]]]]70]+):]0]00]] । । । । ।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17451)
- **Original**: ) 0 औ 3.4... विराजमान थे। तब स्वयं ब्रह्माने दण्डकी भाँति भूमिपर लेटकर उन्हें प्रणाम किया और यों कहा। बहा बोले--भगवन्‌! आप परिपूर्णतम ब्रह्मस्वरूप, नित्य विग्रहधारी, ज्योति:स्वरूप, परमब्रह्म और प्रकृतिसे परे हैं, आपको मेरा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17452)
- **Original**: नमस्कार प्राप्त हो। परमात्मन्‌! आप परम निर्लिप्त, निराकार, ध्यानके लिये साकार, स्वेच्छामय और परमधाम हैं; आपको प्रणाम है। सर्वेश! आप सम्पूर्ण कार्यस्वरूपोंके स्वामी, कारणोंके कारण और ब्रह्मा, शिव, शेष आदि देवोंके अधिपति'
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17453)
- **Original**: हैं, आपको बारंबार अभिवादन है। परात्पर! आप सरस्वती, पद्मा, पार्वती, सावित्री और राधाके
- **Translation**: 

---

