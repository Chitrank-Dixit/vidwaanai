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

### Verse 1 (Vaivtpuran 265.5057)
- **Original**: लिये परम दुर्लभ है। केवल जलमय तीर्थ ही शम्भु, नारायण और प्रकृति-इन तीनों नित्य
- **Translation**: 

---

### Verse 2 (Vaivtpuran 265.5058)
- **Original**: तीर्थ नहीं है, मिट्टी और पत्थरकी प्रतिमारूप तत्त्वोंका नित्य परमात्मा श्रीकृष्णमें लय होना
- **Translation**: 

---

### Verse 3 (Vaivtpuran 265.5059)
- **Original**: देवता ही देवता नहीं हैं, श्रीकृष्णभक्त ही मुख्य लीलामात्र है, वास्तविक नहीं है। स्वयं निर्गुण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 265.5060)
- **Original**: तीर्थ और देवता हैं। वे जलमय तीर्थ और मिट्टी- परमपुरुष परमात्मा ही कालके अनुसार सगुण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 265.5061)
- **Original**: पत्थरके देवता दीर्घकालमें उपासकको पवित्र होते हैं। वे स्वयं ही मायासे नारायण, शिव एवं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 265.5062)
- **Original**: करते हैं, परंतु श्रीकृष्णभक्त दर्शनमात्रसे ही पवित्र प्रकृतिके रूपमें प्रकट होते हैं; अत: सदा उनके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 265.5063)
- **Original**: कर देते हैं। समस्त वर्णामें ब्राह्मण श्रेष्ठ हैं, उनमें समान ही हैं। जैसे अग्नि. और उसकी चिनगारियोंमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 265.5064)
- **Original**: भी जो भारतवर्षमें रहकर स्वधर्म-पालनमें लगे भेद नहीं है, वैसे ही नारायण आदि तथा ।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 265.5065)
- **Original**: रहते हैं, बे श्रेष्ठ हैं। उनमें भी जो श्रीकृष्णमन्त्रका श्रीकृष्णमें कोई अन्तर नहीं है। ब्रह्माजीके द्वारा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 265.5066)
- **Original**: उपासक श्रोकृष्णभक्तिपरायण तथा प्रतिदिन श्रीकृष्णके प्रत्येक कल्पमें जिन-जिन रुद्र, आदित्य आदिकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 265.5067)
- **Original**: नैवेद्यमों भोजन करनेवाला है, वह सर्वश्रेष्ठ और सृष्टि हुई है, वे सब मृत्युकन्यासे पराजित होनेंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 265.5068)
- **Original**: महान्‌ पवित्र है। आप वैष्णव हैं, अत: ब्राह्मणोंमें कारण नश्वर हैं। परंतु शिवकी सृष्टि ब्रह्माजीने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 265.5069)
- **Original**: श्रेष्ठ हैं। साथ ही महान्‌ ज्ञानके श्रेष्ठ सागर हैं। नहीं की है। शिव सत्य, नित्य एवं सनातन हैं।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 265.5070)
- **Original**: मुने! आप-जैसे शिव-शिष्य महात्मा पुरुषको भूमिपाल ! उनके निमेषमात्रमें कितने ही ब्रह्मओंका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 265.5071)
- **Original**: पाकर मैं दूसरे किसकी शरण जाऊँ? महामुने!
- **Translation**: 

---

### Verse 16 (Vaivtpuran 265.5072)
- **Original**: 4 अकृषत<:डरशक 0! 5. 33 अंक्रऋ##ऋ## # ऋक़ कक कक ईं# ########## 4 ############ 55554 ## #$% आपके शापसे इस समय मैं गलित कुष्ठका रोगी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 265.5073)
- **Original**: यह कह गये कि मैं एक वर्षके बाद फिर हूँ। अपवित्र हूँ और तपके अधिकारसे वद्धित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 265.5074)
- **Original**: आऊँगा। शिवे! राजा प्रतिदिन भक्तिभावसे हूँ। ऐसी दशामें कैसे तपस्या करूँ? ब्राह्मणफे चरणोदकका पान करने लगे। उन्होंने सुतपा बोले--राजन्‌! सनातनी विष्णुमाया
- **Translation**: 

---

### Verse 19 (Vaivtpuran 265.5075)
- **Original**: एक वर्षतक ब्राह्मणोंकी पूजा की और उन्हें हरि-भक्ति प्रदान करनेवाली है। वह जिन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 265.5076)
- **Original**: भोजन कराया। वर्ष बीतते-बीतते राजा रोग- लोगोंपर कृपा करती है, उन्हें भगवान्‌की भक्ति
- **Translation**: 

---

