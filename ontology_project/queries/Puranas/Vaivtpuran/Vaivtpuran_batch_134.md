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

### Verse 1 (Vaivtpuran 8.6240)
- **Original**: पदार्थोंको, जिन्हें खाकर मेरी सुन्दर तोंद हो जाय, प्रकारंका भोजन एकत्रित किया है, अत: उन्हीं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6241)
- **Original**: मुझे प्रदान कीजिये। अनेक प्रकारके मिष्टान्नोंको खानेके लिये मैं आया आपके स्वामी सारी सम्पत्तियोंके दाता तथा हूँ। मैं आपका पुत्र हूँ। जो मिष्टान्न तीनों लोकोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6242)
- **Original**: त्रिलोकौके सृष्टिकर्ता हैं और आप सम्पूर्ण दुर्लभ हैं, उन पदार्थोंकों मुझे देकर आप सबसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6243)
- **Original**: ऐश्वर्योंको प्रदान करनेवाली महालक्ष्मीस्वरूपा हैं; पहले मेरी पूजा करें। साध्वि! बेदवादियोंका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6244)
- **Original**: अत: आप मुझे रमणीय रत्नसिंहासन, अमूल्य कथन है कि पिता पाँच प्रकारके होते हैं। माताएँ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6245)
- **Original**: रत्नोंके आभूषण, अग्रिशुद्ध सुन्दर वस्त्र, अत्यन्त अनेक तरहकी कही जाती हैं और पुत्रके पाँच
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6246)
- **Original**: दुर्लभ श्रीहरिका मन्त्र, श्रीहरिमें सुदृढ़ भक्ति, विद्यादातान्नरदाता च भयत्राता च जन्मद: । कन्यादाता च वेदोक्ता नराणां पितर: स्मृता:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6247)
- **Original**: गुरुपत्री गर्भधात्री स्तनदात्री पितुः स्वसा । स्वसा मातुः सपत्री च भृत्य:. शिष्यक्ष पोष्यक्ष वीर्यज: शरणागत: । धर्मपुत्राध चत्वारों वीर्यजो धनभागिति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6248)
- **Original**: (गणपतिखण्ड 8। 47-49)
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6249)
- **Original**: # रेणपतिखण्ड * 313 [[[[[[[[[[[/]]/]
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6250)
- **Original**: // 04040 04404 44404440433 33333 टट मृत्युज्रय नामक ज्ञान, सुखप्रदायिनी दानशक्ति
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.6251)
- **Original**: है।जिन मनुष्योंको भक्तोंका दर्शन अथवा आलिड्डन और सर्वसिद्धि दीजिये। सतीमाता! आप ही सदा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.6252)
- **Original**: प्राप्त हो जाता है, वे मानो समस्त तीर्थोमें भ्रमण श्रीहरिकी प्रिया तथा सर्वस्व प्रदान करनेवाली
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.6253)
- **Original**: कर चुके और उन्हें सम्पूर्ण यज्ञोंकी दीक्षा मिल शक्ति हैं; अत: अपने पुत्रके लिये आपको कौन-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.6254)
- **Original**: चुकी। जैसे सब कुछ भक्षण करनेपर भी अग्नि सी वस्तु अदेय है? मैं उत्तम धर्म और तपस्यामें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.6255)
- **Original**: और समस्त पदार्थोंका स्पर्श करनेपर भी वायु लगे हुए मनको अत्यन्त निर्मल करके सारा कार्य
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.6256)
- **Original**: दूषित नहीं कहे जाते, उसी प्रकार निरन्तर हरिमें करूँगा, परंतु जन्महेतुक कामनाओमें नहीं लगूँगा; [चित्त लगानेवाले भक्त पापोंसे लिप्त नहीं होते। क्योंकि मनुष्य अपनी इच्छासे कर्म करता है,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.6257)
- **Original**: करोड़ों जन्मोंके अन्तमें मनुष्य-जन्म मिलता है। कर्मसे भोगकी प्राप्ति होती है। वे भोग शुभ और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.6258)
- **Original**: फिर मनुष्य-योनिमें बहुत-से जन्मोंके बाद उसे अशुभ दो प्रकारके होते हैं और बे ही दोनों
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.6259)
- **Original**: भक्तोंका सद्ज प्राप्त होता है। सुख-दुःखके हेतु हैं। जगदम्बिके! न किसीसे
- **Translation**: 

---

