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

### Verse 1 (Vaivtpuran 47.4614)
- **Original**: प्रसज्गजके श्रवणमें कुमारकी बड़ी रुचि थी। हुआ था। उनके अधरोंपर मन्द मुस्कानकी छटा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 47.4615)
- **Original**: रासमण्डलका वर्णन चल रहा था। जब इस नमो राधाप्रियाये॑ च पद्मांशाये नमो नमः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 47.4616)
- **Original**: नमः कृष्णप्रियाये च गवां मात्रे नमो नमः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 47.4617)
- **Original**: कल्पवृक्षस्वरूपाये॑ सर्वेषां. सतत॑ परम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 47.4618)
- **Original**: त्रीदाय॑ँ धनदायै च॑ वृद्धिदाय नमों नमः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 47.4619)
- **Original**: शुभदाये प्रसन्नाये॑ गोप्रदाय॑े नमो नमः। यशोदायै कीर्तिदायैधर्मज्ञाया नमो नमः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 47.4620)
- **Original**: (प्रकृतिखण्ड 47
- **Translation**: 

---

### Verse 8 (Vaivtpuran 47.4621)
- **Original**: 24-27)
- **Translation**: 

---

### Verse 9 (Vaivtpuran 47.4622)
- **Original**: न प्रकृतिखण्ड * र4ड9 &#6##4%&##$## ## ## ## % # # $ # ##$ 4 ## ## % # 4 44 ## ## 8 % 4 4 # %$ 888 #### 58% 97444 74 क्फऋक आख्यानकी समाप्ति हुई और अपनी बात प्रस्तुत
- **Translation**: 

---

### Verse 10 (Vaivtpuran 47.4623)
- **Original**: स्मरण किया और उनकी आज्ञा पाकर वे अपनी करनेका अवसर आया, उस समय सती-साध्वी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 47.4624)
- **Original**: अर्धाज्भस्वरूपा पार्वतीसे इस प्रकार बोले--' देवि ! पार्वती मन्द मुस्कानके साथ अपने प्राणवह्लभके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 47.4625)
- **Original**: आगमाख्यानका आरम्भ करते समय मुझे परमात्मा समक्ष प्रश्न उपस्थित करनेको उद्यत हुईं। पहले
- **Translation**: 

---

### Verse 13 (Vaivtpuran 47.4626)
- **Original**: भगवान्‌ श्रीकृष्णने राधाख्यानके प्रसड्रसे रोक दिया तो वे डरती हुई-सी स्वामीकौ स्तुति करने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 47.4627)
- **Original**: था, परंतु महेश्वरि! तुम तो मेरा आधा अज्ज हो; लगीं। फिर जब प्राणेश्वरने मधुर वचनोंद्वारा उन्हें अतः स्वरूपतः मुझसे भिन्न नहीं हो। इसलिये प्रसन्न किया, तब वे देवेश्वरी महादेवी उमा महादेवजीके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 47.4628)
- **Original**: भगवान्‌ श्रीकृष्णने इस समय मुझे यह प्रसम्ष सामने वह अपूर्व राधिकोपाख्यान सुनानेके लिये
- **Translation**: 

---

### Verse 16 (Vaivtpuran 47.4629)
- **Original**: तुम्हें सुनानेकी आज्ञा दे दी है। सतीशिरोमणे ! मेरे अनुरोध करने लगीं, जो पुराणोंमें भी परम दुर्लभ है।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 47.4630)
- **Original**: इष्टदेवकी वल्लभा श्रीराधाका चरित्र अत्यन्त गोपनीय, श्रीपार्वती बोलीं--नाथ! मैंने आपके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 47.4631)
- **Original**: सुखद तथा श्रीकृष्णभक्ति प्रदान करनेवाला है। मुखारविन्दसे पाझरात्र आदि सारे उत्तमोत्तम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 47.4632)
- **Original**: दुर्गे! वह सब पूर्वापर श्रेष्ठ प्रसम्ष मैं जानता हूँ। मैं आगम, नीतिशास्त्र, योगियोंके योगशास्त्र, सिद्धोंक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 47.4633)
- **Original**: जिस रहस्यको जानता हूँ, उसे ब्रह्मा तथा नागराज सिद्धि-शास्त्र, नानाप्रकारके मनोहर तन्‍्त्रशास्त्र, शेष भी नहीं जानते। सनत्कुमार, सनातन, देवता, परमात्मा श्रीकृष्णके भक्तोंक भक्तिशास्त्र तथा
- **Translation**: 

---

