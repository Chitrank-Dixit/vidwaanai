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

### Verse 1 (Vaivtpuran 13.12342)
- **Original**: संहारके जो बीज हैं, उनकौ भी बोजरूपिणी हैं; जब वे घरको लौटने लगे, उस समय वहीँ उनके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12343)
- **Original**: आपको नमस्कार है। पतिके मर्मकों जाननेवाली प्रति आकाशवाणी हुई--'राजन्‌! यह अयोनिजा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12344)
- **Original**: पतिब्रतपरायणे गौरि! पतित्रते! पत्यनुरागिणि! मुझे कन्या साक्षात्‌ लक्ष्मी है; इसे ग्रहण करो। स्वयं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12345)
- **Original**: पति दीजिये; आपको नमस्कार है। आप समस्त भगवान्‌ नारायण तुम्हारे दामाद होंगे।' यह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12346)
- **Original**: मड्जलोंके लिये भी मड्जलकारिणी हैं। सम्पूर्ण आकाशवाणी सुन कन्याको गोदमें लिये राजर्षि
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12347)
- **Original**: मड्नलोंसे सम्पन्न हैं, सब प्रकारके मड्जलोंको जनक घरकों गये और प्रसन्नतापूर्वक उन्होंने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12348)
- **Original**: बीजरूपा हैं; सर्वमज़ले! आपको नमस्कार है। लालन-पालनके लिये उसे अपनी प्यारी रानीके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12349)
- **Original**: आप सबको प्रिय हैं, सबकी बीजरूपिणो हैं, हाथमें दे दिया। युवती होनेपर सती सीताने इस
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12350)
- **Original**: समस्त अशुभोंका विनाश करनेवाली हैं, सबकी ब्रतके प्रभावसे त्रिलोकीनाथ विष्णुके अवताररूप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12351)
- **Original**: ईश्वरी तथा सर्वजननी हैं; शंकरप्रिये! आपको दशरथनन्दन श्रीरामको प्रियतम पतिके रूपमें प्राप्त
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12352)
- **Original**: नमस्कार है। परमात्मस्वरूपे ! नित्यरूपिणि ! सनातनि! कर लिया। महर्षि वसिष्ठने इस व्रतको पृथ्वीपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12353)
- **Original**: आप साकार और निराकार भी हैं; सर्वरूपे ! आपको प्रकाशित किया तथा श्रीराधाने इस ब्रतका नमस्कार है। क्षुधा, तृष्णा, इच्छा, दया, श्रद्धा, निद्रा, अनुष्ठान करके श्रीकृष्णकों प्राणवल्लभके रूपमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12354)
- **Original**: तन्द्रा, स्मृति और क्षमा-ये सब आपकी कलाएँ प्राप्त किया। अन्यान्य गोपकुमारियोंने इस ब्रतके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12355)
- **Original**: हैं; नारायणि! आपको नमस्कार है। लज्जा, मेधा, प्रभावसे उनको पाया। नारद! इस प्रकार मैंने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12356)
- **Original**: तुष्टि, पुष्टि, शान्ति, सम्पत्ति और वृद्धि--ये सब भी गौरी-ब्रतकी कथा कही। जो कुमारी भारतवर्षमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12357)
- **Original**: आपकी ही कलाएँ हैं; सर्वरूपिणि! आपको इस ब्रतका पालन करती है, उसे श्रीकृष्ण-तुल्य
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12358)
- **Original**: नमस्कार है।दृष्ट और अदृष्ट दोनों आपके ही स्वरूप
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.17688)
- **Original**: + गणेशस्तोत्राणि * 783 ###8888#8###% 84844 54585 85 85888 + 4 #ऋअअअकअ्फ़फडऊक्कअ्डअकअऋअ 89 88988 8888 8 8 % 8888 8 8585 8 इत्येब॑ स्तवन कृत्या सुरेश सुरसंसदि । सुरेशश्र सुरैः सार्द्ध विरराम रमापति:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.17689)
- **Original**: इद विष्णुकृतं स्तोत्रं गणेशस्यथ चर यः पठेत्‌ । सायंप्रातश्ष॒मध्याद्षे भक्तियुक्त: समाहितः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.17690)
- **Original**: तद्दिघ्ननिप्नं कुरुते बविघ्लेशः: सतत मुने । वर्थते सर्वकल्याणं कल्याणजनक: सदा
- **Translation**: 

---

