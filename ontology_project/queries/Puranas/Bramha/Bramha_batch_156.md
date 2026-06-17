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

### Verse 1 (Bramha 0.3101)
- **Original**: देवताओंको परास्त करके यज्ञ छोनकर रसातलमें
- **Translation**: 

---

### Verse 2 (Bramha 0.3102)
- **Original**: 170 * संक्षित्त श्रहापुराण * जा पहुँचा। यज्ञके रसातल चले जानेपर पृथ्वीपर
- **Translation**: 

---

### Verse 3 (Bramha 0.3103)
- **Original**: वह समस्त अभीष्ट बस्तुओंको देनेवाला है। उसका सर्वथा अभाव हो गया। देवताओंने सोचा,
- **Translation**: 

---

### Verse 4 (Bramha 0.3104)
- **Original**: कुशावर्त उस तीर्थका नाम है, जहाँ महात्मा गौतमने यज्ञके बिना न तो यह लोक रह जायगा और न
- **Translation**: 

---

### Verse 5 (Bramha 0.3105)
- **Original**: गज़ाका कुशोंसे आबर्तन किया था। वे बहाँ गड्जाको परलोक हो; अतः अपने शत्रुके पीछे उन्होंने
- **Translation**: 

---

### Verse 6 (Bramha 0.3106)
- **Original**: कुशसे लौटाकर ले आये थे। कुशावर्तमें किया रसातलमें भी घावा किया। परंतु इन्द्र आदि देवता
- **Translation**: 

---

### Verse 7 (Bramha 0.3107)
- **Original**: हुआ स्नान और दान पितरोंको तृप्ति देनेवाला है। सिन्धुसेनको जीत न सके। तब उन्होंने पुराणपुरुष
- **Translation**: 

---

### Verse 8 (Bramha 0.3108)
- **Original**: जहाँ नदियोंमें श्रेष्ठ गल्ला नीलपर्वतसे निकली हैं, भगवान्‌ विष्णुके पास जाकर यज्ञापहटरण आदि
- **Translation**: 

---

### Verse 9 (Bramha 0.3109)
- **Original**: वहाँ वे नीलगद्जाके नामसे विख्यात हैं। राक्षषकी सब करतूत कह सुनायो। भगवानने
- **Translation**: 

---

### Verse 10 (Bramha 0.3110)
- **Original**: मनुष्य शुद्धचित्त होकर तीलगज्जामें स्नान आदि उन्हें सान्त्वना देते हुए कहा-“मैं बाराहरूप
- **Translation**: 

---

### Verse 11 (Bramha 0.3111)
- **Original**: जो कुछ भो शुभ कर्म करता है, वह सब अक्षय धारण करके शड्ख, चक्र और गदा हाथमें ले
- **Translation**: 

---

### Verse 12 (Bramha 0.3112)
- **Original**: जानना चाहिये। उससे पितरोंकों बड़ी तृप्ति रसातलमें जाऊँगा और मुख्य-मुख्य राक्षसोंका
- **Translation**: 

---

### Verse 13 (Bramha 0.3113)
- **Original**: होती है। संहार करके पुण्यमय यज्ञकों लौटा लाऊँगा।। गोदावरीमें परम उत्तम कपोततीर्थ भी है, देवताओ! तुम सब लोग स्वर्भमें जाओ। तुम्हारी
- **Translation**: 

---

### Verse 14 (Bramha 0.3114)
- **Original**: जिसकी तीनों लोकॉमें प्रसिद्धि है। मुने! मैं उस मानसिक चिन्ता दूर हो जानी चाहिये।' तीर्थका स्वरूप और महान्‌ फल बतलाता हूँ, गज्भाजी जिस मार्गसे रसातलमें गयी थों, उसी
- **Translation**: 

---

### Verse 15 (Bramha 0.3115)
- **Original**: सुनो। ब्रह्मगिरिपर एक बड़ा भयंकर व्याध रहता भार्गसे पृथ्वीको छेदकर चक्रधारी भगवान्‌ भी
- **Translation**: 

---

### Verse 16 (Bramha 0.3116)
- **Original**: था। वह ब्राह्मणों, साधुओं, यतियों, गौओं, पक्षियों रसातलमें पहुँच गये। उन्होंने वाराहरूप धारण
- **Translation**: 

---

### Verse 17 (Bramha 0.3117)
- **Original**: तथा मृगोंकी हत्या किया करता था। वह पापात्मा करके रसातलवासी राक्षसों और दानवोंका बध
- **Translation**: 

---

### Verse 18 (Bramha 0.3118)
- **Original**: बड़ा ही क्रोधी और असत्यवादी था। उसके किया तथा महायज्ञको मुखमें रखकर रसातलसे
- **Translation**: 

---

### Verse 19 (Bramha 0.3119)
- **Original**: हाथमें सदा पाश और धनुष मौजूद रहते थे। उस निकल आये। उस समय देवता ब्रह्मगिरिपर
- **Translation**: 

---

### Verse 20 (Bramha 0.3120)
- **Original**: महापापी व्याधके मनमें सदा पापके हो संकल्प श्रीहरिकी प्रतीक्षा करते थे। उस मार्गसे निकलकर
- **Translation**: 

---

