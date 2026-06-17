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

### Verse 1 (Vaivtpuran 18.1279)
- **Original**: कर लेता है। जिसको गलित कोढ़का रोग हो या तथा करुणासागर हैं, उन भगवान्‌ शिवको मैं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1280)
- **Original**: उदरमें बड़ा भारी शूल उठता हो, वह यदि एक प्रणाम करता हूँ। जिनकी अड्भकान्ति हिम,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1281)
- **Original**: वर्षतक इस स्तोत्रकों सुने तो अवश्य ही उस चन्दन, कुन्द, चन्द्रमा, कुमुद तथा श्वेत कमलके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1282)
- **Original**: रोगसे मुक्त हो जाता है। यह बात मैंने व्यासजीके सदृश उज्ज्वल है, जो ब्रह्मज्योतिःस्वरूप तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1283)
- **Original**: मुँहसे सुनी है। जो कैदमें पड़कर शान्ति न पाता भक्तोंपर अनुग्रह करनेके लिये विभिन्न रूप धारण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1284)
- **Original**: हो, वह भी एक मासतक इस स्तोत्रको श्रवण करनेवाले हैं, उन भगवान्‌ शंकरको मैं प्रणाम
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1285)
- **Original**: करके अवश्य ही बन्धनसे मुक्त हो जाता है। करता हूँ। जो विषयोंके भेदसे बहुतेरे रूप धारण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1286)
- **Original**: जिसका राज्य छिन गया हो, ऐसा पुरुष यदि करते हैं, जल, अग्नि, आकाश, वायु, चन्द्रमा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1287)
- **Original**: भक्तिपूर्वक एक मासतक इस स्तोत्रका श्रवण करे और सूर्य जिनके स्वरूप हैं, जो ईश्वर एवं
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1288)
- **Original**: तो अपना राज्य प्राप्त कर लेता है। एक मासतक महात्माओंके प्रभु हैं और लीलापूर्वक अपना पद
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1289)
- **Original**: संयमपूर्वक इसका श्रवण करके निर्धन मनुष्य धन देनेकी शक्ति रखते हैं, जो भक्तोंक जीवन हैं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1290)
- **Original**: पा लेता है। राजयक्ष्मासे ग्रस्त होनेपर जो आस्तिक तथा भक्तोंपर कृपा करनेके लिये कातर हो उठते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1291)
- **Original**: पुरुष एक वर्षतक इसका श्रवण करता है, वह हैं, उन ईश्वरकों मैं नमस्कार करता हूँ। वेद भी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1292)
- **Original**: भगवान्‌ शंकरके प्रसादसे निश्चय ही रोगमुक्त हो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1293)
- **Original**: + ब्रह्मरक्वण्ड + 61 &$%&8%$$$%$ 55% 45% 5 6 53443 4 6555 4 $ # /# #% 5 #% ## 6868 # 6868 8 8
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1294)
- **Original**: #8# 86 6# 6 ## # 4888 #8 88 8888 # 88 जाता है। द्विज शौनक! जो सदा भक्तिभावसे इस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1295)
- **Original**: सुनता है तो वह गुरुके उपदेशमात्रसे बुद्धि और स्तबराजको सुनता है उसके लिये तीनों लोकोंमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1296)
- **Original**: विद्या पाता है। जो प्रारब्ध-कर्मसे दुःखी और कुछ भी असाध्य नहीं रह जाता। भारतवर्षमें दरिद्र मनुष्य भक्तिभावसे इस स्तोत्रका श्रवण उसको कभी अपने बन्धुओंसे वियोगका दुःख । करता है, उसे निश्चय ही भगवान्‌ शंकरकी कृपासे नहीं होता। वह अविचल एवं महान्‌ ऐश्वर्यका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1297)
- **Original**: धन प्राप्त होता है। जो प्रतिदिन तीनों संध्याओंके भागी होता है, इसमें संशय नहीं है। जो पूर्ण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1298)
- **Original**: समय इस उत्तम स्तोत्रको सुनता है, बह इस संयमसे रहकर अत्यन्त भक्तिभावसे एक मासतक
- **Translation**: 

---

