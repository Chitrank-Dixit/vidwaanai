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

### Verse 1 (Vaivtpuran 16.3474)
- **Original**: पैतृक स्थान है। यदि भाईके साथ द्रोह अनुचित सौभाग्य प्राप्त हुआ है। अतएव असंख्य प्राकृत
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3475)
- **Original**: है तो देबताओंने भाईसहित हिरण्याक्षकी हिंसा प्रलयको मैंने देखा है और आगे भी मैं बार-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3476)
- **Original**: क्‍यों करवायी ? शुम्भ आदि असुरोंको देवताओंने बार देखूँगा। वे परमेश्वर ही प्रकृतिरूप हैं और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3477)
- **Original**: क्यों मार गिराया? पूर्वकालमें जब समुद्र मथा उन्हींको पुरुष भी कहा जाता है। वे ही आत्मा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3478)
- **Original**: गया, उस समय अमृतका पान केवल देवताओंने और वे ही जीव हैं। वे नाना प्रकारके रूप धारण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3479)
- **Original**: किया; वे सम्पूर्ण फलके भागी हुए और हमें वहाँ करके सदा कार्यमें संलग्न रहते हैं। जो सदा! केवल क्लेशका भागीदार बनाया गया। यह सारा उनके नाम और गुणोंका कीर्तन करता है, वह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3480)
- **Original**: विश्व परमात्मा श्रीकृष्णका क्रीडाक्षेत्र है। वे यहाँ काल, मृत्यु, जन्म, रोग तथा जराके भयको जीत
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3481)
- **Original**: जब जिसको देते हैं, उस समय उसीका ऐश्वर्यपर लेता है। उन्हीं परमेश्वरने ब्रह्माकों सृष्टिकर्ता,, अधिकार होता है। देवताओं और दानवोंका विष्णुकों पालनकर्ता तथा मुझको संहारकर्ता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3482)
- **Original**: ऐश्वर्यक निमित्त सदासे विवाद होता आया है। बनाया है। उन्हींकी कृपासे हम सब लोग जगत्‌के
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3483)
- **Original**: कालके अनुसार बारी-बारीसे कभी उनको और शासक बने हैं। राजन्‌! इस समय मैं कालाग्रिरुद्रकों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3484)
- **Original**: कभी हम लोगोंको जय अथवा पराजय प्राप्त होती संहारके कार्यमें नियुक्त करके स्वयं उन परमेश्वरके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3485)
- **Original**: रहती है। हम दोनोंके विरोधमें आपका आना नाम और गुणका निरन्तर कीर्तन करता हूँ। इसीसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3486)
- **Original**: निष्फल है; क्योंकि आप हम दोनोंके साथ समान मृत्यु मुझपर अपना प्रभाव नहीं डाल सकती।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3487)
- **Original**: सम्बन्ध रखनेवाले, बन्धु, ईश्वर एबं महात्मा हैं। इस ज्ञानकी महिमासे मैं सदा निर्भय रहता हूँ।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3488)
- **Original**: हम लोगोंके साथ इस समय स्पर्धा रखना आपके मृत्यु भी मुझसे भय मानकर इस प्रकार भागती
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3489)
- **Original**: लिये बड़ी लज्जाकी बात है और यदि कहीं युद्धमें है, जैसे गरुड़के भयसे सर्प। आपकी पराजय हुई तो इससे भी अधिक आपकी नारद! सर्वेश भगवान्‌ शंकर सभाके मध्यभागमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3490)
- **Original**: अपकीर्ति फैलेगी। उपर्युक्त बातें कहकर चुप हो गये। तब दानवग़ज़ने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3491)
- **Original**: . मुने! शद्भगचूड़के ये वचन सुनकर भगवान्‌ उनके बचन सुनकर उनकी भूरि-भूरि प्रशंसा त्रिलोचन हँसने लगे। तत्पश्चात्‌ उन्होंने उस की, साथ ही मधुर वाणीमें विनयपूर्वक अपना
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3492)
- **Original**: दानवेश्वरका समुचित उत्तर देना आरम्भ किया। भाषण आरम्भ किया। महादेवजी बोले--राजन्‌! तुम लोग भी शद्स्‍भुचूड़ने कहा--भगवन्‌ ! आपने जो कुछ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3493)
- **Original**: तो ब्रह्माके हो वंशज हो। फिर तुम्हारे साथ युद्ध कहा है, वह सब सत्य है। उसे कभी अन्यथा
- **Translation**: 

---

