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

### Verse 1 (Bramha 0.1401)
- **Original**: भोणोंको प्राप्त कर लेता है। +>“#स्पेस्फसेक्‍-> पार्वतीदेवीकी तपस्या, वरदान-प्राप्ति तथा उनके द्वारा ग्राहके मुखसे ब्राह्मणग-बालकका उद्धार मुनियोने पूझा--प्रभो! दक्षकन्या सतीने क्रोधवश्
- **Translation**: 

---

### Verse 2 (Bramha 0.1402)
- **Original**: तपस्या कौ, जिसकी कहीं तुलना नहीं है। उस पूर्वशरीरका परित्याग करके फिर गिरियज़ हिमालयके
- **Translation**: 

---

### Verse 3 (Bramha 0.1403)
- **Original**: तपस्यासे मुझे बड़ा संतोष हुआ। तब मैंने उनके घरमें कैसे जन्म लिया? महादेवजीके साथ उनका
- **Translation**: 

---

### Verse 4 (Bramha 0.1404)
- **Original**: पास जाकर कहा--'उत्तम ब्रतके पालन करनेवाले संयोग कैसे हुआ? तथा उस दम्पतिमें वार्तालाप
- **Translation**: 

---

### Verse 5 (Bramha 0.1405)
- **Original**: गिरिराज! अब मैं तुम्हारी इस तपस्यासे संतुष्ट हूँ। किस प्रकार हुआ? तुम इच्छानुसार बर माँगो।' ख्रह्माजी बोले-मुनिवरो! पार्वती और
- **Translation**: 

---

### Verse 6 (Bramha 0.1406)
- **Original**: हिपालयने कहा--भगवन्‌! मैं सब गुणोंसे महादेवजीकी पवित्र कथा पापोंका नाश करनेवाली
- **Translation**: 

---

### Verse 7 (Bramha 0.1407)
- **Original**: सुशोभित संतान चाहता हूँ। यदि आप मुझपर और सम्पूर्ण कामनाओंको देनेवाली है; उसे कहता
- **Translation**: 

---

### Verse 8 (Bramha 0.1408)
- **Original**: संतुष्ट हैं तो ऐसा ही बर दीजिये। हूँ, सुनो। एक समयकी बात है, महर्षि कश्यप
- **Translation**: 

---

### Verse 9 (Bramha 0.1409)
- **Original**: गिरिराजकी यह बात सुनकर मैंने उन्हें हिमवानके घरपर पंधारे। उस समय हिसवानूने
- **Translation**: 

---

### Verse 10 (Bramha 0.1410)
- **Original**: मनोवाज्छित बर देते हुए कहा--'शैलेन्द्र! इस पूछा--' मुने! किस उपायसे मुझे अक्षय लोक प्राप्त
- **Translation**: 

---

### Verse 11 (Bramha 0.1411)
- **Original**: तपस्याके प्रभावसे तुम्हारे कन्या उत्पन्न होगी, होंगे, मेरी अधिक प्रसिद्धि होगी और सत्पुरुषोंमें
- **Translation**: 

---

### Verse 12 (Bramha 0.1412)
- **Original**: जिससे तुम सर्वत्र उत्तम कीर्ति प्राप्त करोगे। मैं पूजनीय समझा जाऊँगा?! तुम्हारे यहाँ कोटि-कोटि तीर्थ बास करेंगे। तुम कश्यपने कहा--महाबाहो ! उत्तम संतान होनेसे
- **Translation**: 

---

### Verse 13 (Bramha 0.1413)
- **Original**: सम्पूर्ण देवताओंसे पूजित होगे तथा अपने पुण्यसे यह सब कुछ प्राप्त हो जाता है। ब्रह्मा और
- **Translation**: 

---

### Verse 14 (Bramha 0.1414)
- **Original**: देवताओंको भी पावन बनाओगे। तदनन्तर गिरिराजने ऋषियोंसहित मेरी प्रसिद्धि तो केवल संतानके ही
- **Translation**: 

---

### Verse 15 (Bramha 0.1415)
- **Original**: समयानुसार अपनी पत्नी मैनाके गर्भसे अपर्णा कारण है। अत: गिरिराज! तुम घोर तपस्या करके
- **Translation**: 

---

### Verse 16 (Bramha 0.1416)
- **Original**: नामकी एक कन्या उत्पन्त कौ। अपर्णा बहुत गुणवान्‌ संतान--श्रेष्ठ कन्या उत्पन्न करो। समयतक निराहार रही, उसे उपवाससे रोकते हुए ख्रह्माजी कहते हैं--कश्यपजीके यों कहनेपर
- **Translation**: 

---

### Verse 17 (Bramha 0.1417)
- **Original**: माताने कहा--'बेटी! “उ मा' (ऐसा मत करो)।' गिरिराज हिमालयने नियममें स्थित होकर ऐसी
- **Translation**: 

---

### Verse 18 (Bramha 0.1418)
- **Original**: उस समय वे मातृस्नेहसे दुःखित हो रही थीं। भूताश्रयों भूतपति:.. सर्वलोकनमस्कृत:
- **Translation**: 

---

### Verse 19 (Bramha 0.1419)
- **Original**: स्रष्टा स॑वर्ततों वह्डि: सर्वस्थादिरलोलुप:
- **Translation**: 

---

### Verse 20 (Bramha 0.1420)
- **Original**: अनन्त: कपिलो भानु: कामद: सर्वतोमुख:। जयो विशालो यरदः सर्वभूतनिषेवित:
- **Translation**: 

---

