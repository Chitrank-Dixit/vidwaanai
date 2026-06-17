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

### Verse 1 (Vaivtpuran 6.9391)
- **Original**: तथा जल और शीतलतामें जैसे ऐक्य (भेदाभाव) मन, प्राण और आत्मा भी मुझमें ही स्थापित हैं।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9392)
- **Original**: है, उसी तरह हम दोनोंमें भेद नहीं है। मेरे अतः विरहकी बात कानमें पड़ते ही आँखोंका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9393)
- **Original**: बिना तुम निर्जीव हो और तुम्हारे बिना मैं अदृश्य पलक गिरना बंद हो गया है और हम दोनों
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9394)
- **Original**: हूँ। सुन्दरि! तुम्हारे बिना मैं संसारकी सृष्टि नहीं आत्माओंके मन, प्राण निरन्तर दग्ध हो रहे हैं।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9395)
- **Original**: कर सकता, यह निश्चित बात है। ठीक उसी बोले--देवि! उत्तम आध्यात्मिक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9396)
- **Original**: तरह, जैसे कुम्हार मिट्टीके बिना घड़ा नहीं बना योग शोकका उच्छेद करनेवाला होता है। अतः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9397)
- **Original**: सकता और सुनार सोनेके बिना आधूषणोंका उसे बताता हूँ, सुनो। यह योग योगीन्द्रोंके लिये
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9398)
- **Original**: निर्माण नहीं कर सकता। स्वयं आत्मा जैसे नित्य भी दुर्लभ है। सुन्दरि! देखो, सारा ब्रह्माण्ड आधार
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9399)
- **Original**: है, उसी प्रकार साक्षात्‌ प्रकृतिस्वरूपा तुम नित्य और आधेयके रूपमें विभक्त है। इनमें भी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9400)
- **Original**: हो। तुममें- सम्पूर्ण शक्तियोंका समाहार सश्लित है। आधारसे पृथक्‌ आधेयकी सत्ता सम्भव नहीं है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9401)
- **Original**: तुम सबकी आधारभूता और सनातनी हो*। भयथा क्षिरे च धावल्य दाहिका च हुताशने। भूमौ गन्धो जले शैत्य॑ तथा त्वयि मम स्थिति:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9402)
- **Original**: धावल्यदुग्धयॉरैक्य॑ दाहिकानलयोर्यथा । भूगन्धजलशैत्यानां, नास्ति भेदस्तथा55वयो:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9403)
- **Original**: * श्रीकृष्णजन्मखण्ड * 4ड25 #4448644 464 4444 488 4 8 69 68584 48 6 # 6 # 54 45% 454 5 4 5 $ 55 # 5 #5 4551 ऋ अर # 6 5 4 # 1 81/ 8888 55 लक्ष्मी, सरस्वती, पार्वती, ब्रह्मा, शिव, शेषनाग
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9404)
- **Original**: तुम्हें गोकुलमें जाना है। राधिके! मैं भी इन और धर्म-ये सब मेरे प्राणोंके समान हैं; परंतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9405)
- **Original**: असंख्य गोपोंको यहीं स्थापित करके पीछेसे तुम मुझे प्राणोंसे भी बढ़कर प्यारी हो। राधिके !
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9406)
- **Original**: वसुदेवके निबासस्थान मथुरापुरीमें पदार्पण करूँगा। ये सब देवता और देवियाँ मेरे निकट हैं; परंतु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9407)
- **Original**: मेरे प्रिय-से-प्रिय गोप बहुत बड़ी संख्यामें मेरे तुम यदि इनसे अधिक न होतीं तो मेरे वक्ष:-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9408)
- **Original**: साथ क्रीडाके लिये व्रजमें चलें और वहाँ गोपोंके स्थलमें कैसे विराजमान हो सकती थीं? सुशीले घरमें जन्म लें। राधे! आँसू बहाना छोड़ो। साथ ही इस निष्फल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9409)
- **Original**: . नारद! यों कहकर श्रीकृष्ण चुप हो गये। भ्रमका परित्याग करो। शड्जा छोड़कर निर्भीक-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9410)
- **Original**: देवता, देवियाँ, गोप और गोपियाँ वहीं ठहर गयीं। भावसे वृषभानुके घरमें पधारों। सुन्दरि! नौ ब्रह्मा, शिव, धर्म, शेषनाग, पार्वती, लक्ष्मी और मासतक कलावतीके पेटमें स्थित गर्भको मायाद्वारा
- **Translation**: 

---

