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

### Verse 1 (Rig Ved 0.2361)
- **Original**: धन वैभव के पूल आधार ये अग्नि देव ऐश्वर्यों से युक्त करने वाले, यज्ञ की सूचक ध्वजा के समान तथा मनुष्य के निमित्त इष्टफल प्रदायक हैं। अपरत्व के रक्षक देवों ने ऐसे अग्निदेव को धारण किया है
- **Translation**: 

---

### Verse 2 (Rig Ved 0.2362)
- **Original**: 1074. नू थ पुरा ख सदन॑ रयीणां जातस्थ च जायमानस्य च क्षाम्‌। सतक्ष गोपां भवतओ भूरेदेंवा अग्निं धारयन्द्रविणोदाम्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.2363)
- **Original**: ये अग्निदेव वर्तपान और पूर्व की सम्पदाओं के आधार हैं । जो उत्पन्न हुए या उत्पन्न होने वालों के आश्रय स्थान हैं। जो उत्पन्न हुए या उत्पन्न होने बालों के आश्रय स्थान हैं । जो विद्यमान और उत्पन्न होने वाले सभो पदार्थों के संरक्षक हैं। देवों ने उन धन प्रदाता अग्निदेव को धारण किया है
- **Translation**: 

---

### Verse 4 (Rig Ved 0.2364)
- **Original**: 1075, द्रविणोदा द्रविणसस्तुरस्य द्रविणोदा: सनरस्य प्र यंसत्‌। द्रविणोदा वीरवतीमिषं नो द्रविणोदा रासते दीर्घमायु:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.2365)
- **Original**: धन-प्रदाता अग्निदेव हमारे उपयोग के लिए जंगम ऐश्वर्य साधत (गवादि धन ) और स्थावर ऐश्वर्य साधन (वानस्पतिक पदार्थ) भी दें वे सन्तान युक्त धन सम्पदा और दीर्घ आयु भी प्रदान करें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.2366)
- **Original**: में0 9 सू0 ₹7 53। 1076, एवा नो अग्ने समिधा वृधानो रेवत्पावक श्रवसे वि भाहि। तन्नो मित्रो वरुणो मामहन्तामदितिः सिन्धु: पृथिवी उत जौ:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.2367)
- **Original**: हे प्रविव्रकर्मा अग्निदेव ! समिधाओं से सम्वर्धित होकर आप हमें धन देते हुए अपने यश से प्रकाशित हों । हमारे इस निवेदन का मित्र, वरुण, अदिति, समुद्र, पृथिवी और चुलोक भी अनुमोदन करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.2368)
- **Original**: [ सूक्त - 97 ] [ऋषि - कुत्स आ्विरस
- **Translation**: 

---

### Verse 9 (Rig Ved 0.2369)
- **Original**: देवता- अग्नि अथवा शुति ऑग्न
- **Translation**: 

---

### Verse 10 (Rig Ved 0.2370)
- **Original**: छन्‍्द - गायत्री
- **Translation**: 

---

### Verse 11 (Rig Ved 0.2371)
- **Original**: ] 1077. अप न: शोशुचदघमग्ने शुशुग्ध्या रयिम्‌। अप नः शोशुचदघम्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.2372)
- **Original**: है अग्निदेव ! आप हमारे पापों को भस्म करें । हमारे चारों ओर ऐश्वर्य को प्रकाशित करें । हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.2373)
- **Original**: 1078. सुक्षेत्रिया सुगातुया वसूया च यजामहे। अप नः शोशुचदघम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.2374)
- **Original**: है अग्निदेव ! उत्तम क्षेत्र, उत्तम मार्ग और उत्तम धन की इच्छा से हम आपका यजन करते हैं । आप हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.2375)
- **Original**: 1079. प्र यद्धन्दिष्ठ एवां प्रास्माकासश्व सूरय:। अप न: शोशुचदघम्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.2376)
- **Original**: है अग्निदेव ! हम सभी साधक वीरता और बुद्धि पूर्वक आपकी विशिष्ट प्रकार से भक्ति करते हैं। आप हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.2377)
- **Original**: 1080. प्र यत्ते अग्ने सूरयो जायेमहि प्र ते ववम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.2378)
- **Original**: अप नः शोशुचदघम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.2379)
- **Original**: है अग्निदेव ! हम सभी और ये विद्वदूगण आपकी उपासना से आपके सदृश प्रक्ाशवान्‌ हुए हैं, अत: आप हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.2380)
- **Original**: 1081. प्र यदग्ने: सहस्वतो विश्वतो यन्ति भानव:। अप नः शोशुचदघम्‌
- **Translation**: 

---

