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

### Verse 1 (Mahabharat 0.1261)
- **Original**: प्रकार युद्धमें मारे जानेसे उन्हें मतिमान्‌ अगस्यजीका जो झाप धर्मराज युधिष्ठिरको उपदेश कर वे अपने स्थानको चले गये।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1261)
- **Original**: प्रकार युद्धमें मारे जानेसे उन्हें मतिमान्‌ अगस्यजीका जो झाप धर्मराज युधिष्ठिरको उपदेश कर वे अपने स्थानको चले गये।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1262)
- **Original**: था, उसका भी अन्त हो गया। पाण्डबॉने वह रात बड़े भीमसेनके हाथसे जो राक्षस मारे गये थे, उनके शव
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1262)
- **Original**: था, उसका भी अन्त हो गया। पाण्डबॉने वह रात बड़े भीमसेनके हाथसे जो राक्षस मारे गये थे, उनके शव
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1263)
- **Original**: आनन्दसे कुबेरजीके महत्तोंमें ही खितायी। दि धौम्यका युथिष्ठिरको नाना स्थान दिखलाना और अर्जुनका गन्धमादनपर ल्ट्रैटठकर आना वैज्ञग्पायतजी कहते हैं--झन्नुदमन जनमेजय ! सूर्योदय
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1263)
- **Original**: आनन्दसे कुबेरजीके महत्तोंमें ही खितायी। दि धौम्यका युथिष्ठिरको नाना स्थान दिखलाना और अर्जुनका गन्धमादनपर ल्ट्रैटठकर आना वैज्ञग्पायतजी कहते हैं--झन्नुदमन जनमेजय ! सूर्योदय
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1264)
- **Original**: दर्शन देवता और दानवोंको भी दुर्लभ है। उस स्थानपर होनेपर मुनियर धोष्य अपने आहिक कर्पसे निवृत्त हो राजर्षि
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1264)
- **Original**: दर्शन देवता और दानवोंको भी दुर्लभ है। उस स्थानपर होनेपर मुनियर धोष्य अपने आहिक कर्पसे निवृत्त हो राजर्षि
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1265)
- **Original**: अखि्यमूर्ति श्रीहरि विगजते हैं। जो महान्‌ तपम्बी और आईएषिणके साथ पाण्डवोंकी ओर चले। पाण्छवोने उन
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1265)
- **Original**: अखि्यमूर्ति श्रीहरि विगजते हैं। जो महान्‌ तपम्बी और आईएषिणके साथ पाण्डवोंकी ओर चले। पाण्छवोने उन
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1266)
- **Original**: झुभकमॉे पव्ित्रचित्त हो गये हैं, वे अज्ञान और मोहसे रहित दोनोंके चरणोंमें प्रणाम किया और फिर हाथ जोड़कर अन्य
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1266)
- **Original**: झुभकमॉे पव्ित्रचित्त हो गये हैं, वे अज्ञान और मोहसे रहित दोनोंके चरणोंमें प्रणाम किया और फिर हाथ जोड़कर अन्य
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1267)
- **Original**: योगसिद्ध महात्मा यतिजन ही भक्तिके ट्वारा उनके पास जा सब ब्राह्मणोंका भी अभिवादन किया। फिर धौम्यने
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1267)
- **Original**: योगसिद्ध महात्मा यतिजन ही भक्तिके ट्वारा उनके पास जा सब ब्राह्मणोंका भी अभिवादन किया। फिर धौम्यने
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1268)
- **Original**: सकते हैं। वहाँ जाकर ये फिर इस ल्ेकमें नहीं आते। धर्मराजका हाथ पकड़कर पूर्व दिज्ञाकी ओर संकेत करते हुए
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1268)
- **Original**: सकते हैं। वहाँ जाकर ये फिर इस ल्ेकमें नहीं आते। धर्मराजका हाथ पकड़कर पूर्व दिज्ञाकी ओर संकेत करते हुए
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1269)
- **Original**: राजन्‌ ! यह परमेश्वरका स्थान घुव, अक्षय और अविनाझी कहा, “महाराज ! यह जो समुद्रपय॑न्त पृथ्वीपर फैल्मा हुआ
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1269)
- **Original**: राजन्‌ ! यह परमेश्वरका स्थान घुव, अक्षय और अविनाझी कहा, “महाराज ! यह जो समुद्रपय॑न्त पृथ्वीपर फैल्मा हुआ
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1270)
- **Original**: है; तुम इसे प्रणाम करो । देखो ! सूर्य, चन्द्रमा और समस्त महापर्वत दिखायी दे रहा है, इसका नाम मन्दराचल है।
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1270)
- **Original**: है; तुम इसे प्रणाम करो । देखो ! सूर्य, चन्द्रमा और समस्त महापर्वत दिखायी दे रहा है, इसका नाम मन्दराचल है।
- **Translation**: 

---

