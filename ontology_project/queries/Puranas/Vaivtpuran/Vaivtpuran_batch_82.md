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

### Verse 1 (Vaivtpuran 6.9451)
- **Original**: गोकुलमें तुम्हारे समीप आ जाऊँगा। उपर्युक्त कार्य सम्पादित होंगे। फिर बृन्दाबनमें। लाल कमलके समान नेत्रोंवाली श्रीराधा तुम्हारे साथ मेरा निवास होगा। फिर माता-पिता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9452)
- **Original**: श्रीकृष्णको प्रणाम करके प्रेमविच्छेदके भयसे तथा गोपियोंके शोकका पूर्णतः निवारण होगा।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9453)
- **Original**: कातर हो उनके सामने फूट-फूटकर रोने लगीं। भूतलका भार उतारकर तुम्हारे और गोप-गोपियोंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9454)
- **Original**: वे ठहर-ठहरकर कभी कुछ दूरतक जाती और साथ मेरा पुनः गोलोकमें आगमन होगा। राधे!
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9455)
- **Original**: जा-जाकर बार-बार लौट आती थीं। लौटकर मेरे अंशभूत जो नित्य परमात्मा नारायण हैं, वे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9456)
- **Original**: पुनः श्रीहरिका मुँह निहारने लगती थीं। सती लक्ष्मी और सरस्वतीके साथ वैकुण्ठलोककों
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9457)
- **Original**: राधा शरत्कालकी पूर्णिमाके चन्द्रमाकी कान्तिसुधासे पधारेंगे। धर्म और मेरे अंशोंका निवासस्थान
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9458)
- **Original**: पूर्ण प्रभुके मुखचन्द्रकी सौन्दर्य-माधुरीका अपने श्वेतद्वीपमें होगा। देवताओं और देवियोंके अंश भी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9459)
- **Original**: निमेषरहित नेत्र-चकोरोंद्वारा पान करती थीं। अक्षय धामको पधारेंगे। फिर इसी गोलोकमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9460)
- **Original**: तदनन्तर परमेश्वरी राधा प्रभुकी सात बार परिक्रमा तुम्हारे साथ मेरा निवास होगा। कान्ते ! इस प्रकार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9461)
- **Original**: करके सात बार प्रणाम करनेके अनन्तर पुनः समस्त भावी शुभाशुभका वर्णन मैंने कर दिया।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9462)
- **Original**: श्रीहरिके सामने खड़ी हुईं। इतनेमें ही करोड़ों मेरे द्वारा जो निश्चय हो चुका है, उसका कौन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9463)
- **Original**: गोप-गोपियोंका समूह वहाँ आ पहुँचा। उन निवारण कर सकता है? सबके साथ श्रीराधाने पुनः श्रीकृष्णको प्रणाम तदनन्तर श्रीहरिने देवताओं और देवियोंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9464)
- **Original**: किया। तत्पश्चात्‌ तैंतीस सखीस्वरूपा गोपकिशोरियों समयोचित बात कही--देवताओ ! अब तुमलोग
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9465)
- **Original**: और गोपसमूहोंके साथ सुन्दरी राधा श्रीहरिको भावी कार्यकी सिद्धिके लिये अपने-अपने स्थानकों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9466)
- **Original**: मस्तक झुकाकर भूतलके लिये प्रस्थित हुईं। वे जाओ। पार्वति! तुम अपने. दोनों पुत्रों तथा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9467)
- **Original**: [सब-के-सब श्रीहरिके बताये हुए स्थान नन्द- स्वामीके साथ कैलासकों जाओ। मैंने जो कार्य
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9468)
- **Original**: गोकुलको गये। फिर राधा वृषभानुके घरमें और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9469)
- **Original**: + श्रीकृष्णजन्मखण्ड * ड27 गोपियाँ अन्यान्य गोपोंके घरोंमें गयीं। गोप-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9470)
- **Original**: उन्हें कंसने तत्काल मार डाला। इस तरह उनके गोपियोंसहित श्रीराधाके भूतलपर चले जानेपर
- **Translation**: 

---

