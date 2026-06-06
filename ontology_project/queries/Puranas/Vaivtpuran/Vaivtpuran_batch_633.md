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

### Verse 1 (Vaivtpuran 63.5540)
- **Original**: करो। जगत्पूज्ये! महेश्वरि! यहाँ आओ, ठहरो, कान्तिमती तथा शान्तस्वरूपा हैं। योगसिद्धियोंमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5541)
- **Original**: हहरो। हे मातः ! हे अम्बिके! तुम इस प्रतिमामें बहुत बढ़ी-चढ़ी हैं। विधाताकी भी सृष्टि करनेवाली
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5542)
- **Original**: निवास करो। अच्युते ! इस प्रतिमामें तुम्हारे प्राण तथा सबकी माता हैं। समस्त लोकोंका कल्याण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5543)
- **Original**: निम्नभागमें रहनेवाले प्राणोंक साथ आवें, रहें। करनेवाली हैं। शरत्कालकी पूर्णिमाके चन्द्रमाकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5544)
- **Original**: तुम्हारी सम्पूर्ण शक्तियाँ इस प्रतिमामें तुरंत पदार्पण भाँति उनका परम सुन्दर मुख है। वे अत्यन्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5545)
- **Original**: करें। '30 हीं श्रीं क्लीं दुर्गाय॑ स्थाहा।' इस मनोहारिणी हैं। उनके भालदेशका मध्यभाग कस्तूरी-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5546)
- **Original**: मन्त्रका उच्चारण करके कहे--' हे सदाशिवे! इस बिन्दु, चन्दन-बिन्दु तथा सिन्दूर-बिन्दुसे सदा प्रतिमाके हृदयमें प्राण स्थित हों। चण्डिके ! उद्दीध्त होता रहता है। उनके नेत्र शरदऋतुके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5547)
- **Original**: सम्पूर्ण इन्द्रियोंके अधिदेवता यहाँ आवें। तुम्हारी मध्याह्कालमें खिले हुए कमलॉकी कान्तिको
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5548)
- **Original**: शक्तियाँ यहाँ आवें। ईश्वर यहाँ आवें। देवि! तुम छोने लेते हैं। काजलकी सुन्दर रेखाओंसे वे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 63.5549)
- **Original**: इस प्रतिमामें पधारों।' इस प्रकार आवाहन करके सर्वथा सुशोभित होते हैं। उनके श्रीअड्ढ करोड़ों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 63.5550)
- **Original**: निप्राद्भित मन्त्रसे परिहार-स्तुति करनी चाहिये। कन्दर्पॉंकी लावण्यलीलाकों तिरस्कृत करनेवाले
- **Translation**: 

---

### Verse 12 (Vaivtpuran 63.5551)
- **Original**: विप्रवर! एकाग्रचित्त होकर परिहारकों सुनो। हैं। वे रत्रमय सिंहासनपर विराजमान हैं। उनका शिवप्रिये! भगवति अम्बे! शिवलोकसे जो मस्तक उत्तम रत्रोंके बने हुए मुकुटसे उद्धासित तुम आयी हो, तुम्हारा स्वागत है। भद्रे! मुझपर होता है। वे स्रष्टाकी सृष्टिमें शिल्परूपा और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 63.5552)
- **Original**: कृपा करो। भद्गरकालि! तुम्हें नमस्कार है। दुर्गे! पालकके पालनमें दयारूपा हैं। संहारकालमें संहारककी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 63.5553)
- **Original**: माहे धरि! तुम जो मेरे घरमें आयी हो, इससे मैं उत्तम संहाररूपिणी शक्ति हैं। निशुम्भ और शुम्भको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 63.5554)
- **Original**: धन्य हूँ, कृतकृत्य हूँ और मेरा जीवन सफल है। मथ डालनेवाली तथा महिषासुरका मर्दन करनेवाली
- **Translation**: 

---

### Verse 16 (Vaivtpuran 63.5555)
- **Original**: आज मेरा जन्म सफल और जीवन सार्थक हुआ; हैं। पूर्वकालमें त्रिपुर-युद्धके समय त्रिपुरारि महादेवने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 63.5556)
- **Original**: क्योंकि मैं भारतवर्षके पुण्यक्षेत्रमें दुर्गजीका पूजन इनकी स्तुति की थी। मधु और कैटभके युद्धमें वे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 63.5557)
- **Original**: करता हूँ। जो विद्वान्‌ भारतवर्षमें आप पूजनीया विष्णुकी शक्तिस्वरूपिणी थीं। समस्त दैत्योंका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 63.5558)
- **Original**: दुर्गाका पूजन करता है, वह अन्तमें गोलोकधामकों वध तथा रक्तबीजका विनाश करनेवाली यही हैं।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 63.5559)
- **Original**: जाता है और इहलोकमें भी उत्तम ऐश्वर्यसे सम्पन्न
- **Translation**: 

---

