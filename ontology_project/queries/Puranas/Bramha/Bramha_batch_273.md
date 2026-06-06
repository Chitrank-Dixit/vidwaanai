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

### Verse 1 (Bramha 0.5441)
- **Original**: आया। उन्हें बड़ा विस्मय हुआ। विभीषणने प्रसन्न- कठोर ब्रतका पालन करते हुए भारी तपस्या की,
- **Translation**: 

---

### Verse 2 (Bramha 0.5442)
- **Original**: चित्तसे मस्तक झुकाकर भगवान्‌कों प्रणाम किया जो दूसरोंके लिये अत्यन्त दुष्कर थी। उस
- **Translation**: 

---

### Verse 3 (Bramha 0.5443)
- **Original**: और कहा--'आज मेरा जन्म सफल हो गया। तपस्यासे संतुष्ट होकर मैंने रावणको वरदान दिया,
- **Translation**: 

---

### Verse 4 (Bramha 0.5444)
- **Original**: आज मेरी तपस्थाका फल मिल गया। यों 'तुम्हें . सम्पूर्ण देवताओं, दैत्यों, नागों और
- **Translation**: 

---

### Verse 5 (Bramha 0.5445)
- **Original**: कहकर धर्मात्मा विभीषण बारंबार भगवानूको राक्षसोंमेंसे कोई नहीं मार सकेगा। शापके भयंकर
- **Translation**: 

---

### Verse 6 (Bramha 0.5446)
- **Original**: प्रणाम करके अपने बड़े भाईके पास गये और प्रहारसे भी तुम्हारी मृत्यु नहों होगी। तुम यमदूतोंसे [हाथ जोड़कर बोले-'राजन्‌! आप बह प्रतिमा भी अवध्य रहोगे।' ऐसा बर पाकर बह राक्षस
- **Translation**: 

---

### Verse 7 (Bramha 0.5447)
- **Original**: देकर मुझपर कृपा कौजिये। मैं उसकी आराधना सम्पूर्ण यक्षों और उनके राजा धनाध्यक्ष कुबेरकों
- **Translation**: 

---

### Verse 8 (Bramha 0.5448)
- **Original**: करके भवसागरसे पार होना चाहता हूँ। भी परास्त करके इन्द्रको भी जीतनेके लिये उद्यत
- **Translation**: 

---

### Verse 9 (Bramha 0.5449)
- **Original**: बात सुनकर रावणने कहा--“बीर ! तुम प्रतिमा ले हुआ। उसने देवताओंके साथ बड़ा भयड्जूर संग्राम
- **Translation**: 

---

### Verse 10 (Bramha 0.5450)
- **Original**: लो, मैं उसे लेकर क्या करूँगा। मैं तो ब्रह्माजीको किया। उसके पुत्रका नाम मेघनाद था। मेघनादने
- **Translation**: 

---

### Verse 11 (Bramha 0.5451)
- **Original**: आराधना करके तीनों लोकॉपर विजय पा रहा इन्द्रको जीत लिया, अत: वह इन्द्रजितके नामसे
- **Translation**: 

---

### Verse 12 (Bramha 0.5452)
- **Original**: हूँ।' विभीषण बड़े बुद्धिमान्‌ थे। उन्होंने वह प्रसिद्ध हुआ। तदनन्तर बलवान्‌ रावणने अमग्वतीपुरीमें
- **Translation**: 

---

### Verse 13 (Bramha 0.5453)
- **Original**: कल्याणमयी प्रतिमा ले ली और उसके द्वारा एक प्रवेश करके देवराज इन्द्रके सुन्दर भवनमें भगवान्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.5454)
- **Original**: सौ आठ वर्षोतक भगवान्‌ विष्णुकी आराधना की। वासुदेवकी प्रतिमा देखी, जो अज्ञकके समान [इससे उन्होंने अणिमा आदि आठों सिद्धियोंके साथ श्यामवर्ण और समस्त शुभ लक्षणोंसे सम्पन्न थी।
- **Translation**: 

---

### Verse 15 (Bramha 0.5455)
- **Original**: अजर-अपर रहनेका बरदान प्राप्त कर लिया। पद्मपत्रके समान विशाल नेत्र, बनमालासे ढके हुए
- **Translation**: 

---

### Verse 16 (Bramha 0.5456)
- **Original**: रावण बड़ा पापी और क्रूर राक्षस था। उसने बक्ष:स्थलमें श्रीवत्सका सुन्दर चिह, मस्तकपर
- **Translation**: 

---

### Verse 17 (Bramha 0.5457)
- **Original**: देवता, गन्धर्व, किंनर, लोकपाल, मनुष्य, मुनि थनमालाबृतोरस्कां मुकुटाद्रदधारिणीम्‌ । पीतवस्त्रों सुपीनांसां कुष्डलाभ्यामलंकृताम्‌
- **Translation**: 

---

### Verse 18 (Bramha 0.5458)
- **Original**: एवं सा प्रतिमा दिव्या गुडामन्तैस्तदा स्थयम्‌ । प्रतिष्ठाकालमासाद्य मयासौ निर्मिता पुरा
- **Translation**: 

---

### Verse 19 (Bramha 0.5459)
- **Original**: (176। 8--11)
- **Translation**: 

---

### Verse 20 (Bramha 0.5460)
- **Original**: * अनन्त आसुदेवकी महिमा तथा पुरुषोत्तम-क्षेत्रके माहात्प्यक्ा उपसंहार * 263 और सिद्धोंको भी युद्धमें जीतकर उनकी स्त्रियोंकों
- **Translation**: 

---

