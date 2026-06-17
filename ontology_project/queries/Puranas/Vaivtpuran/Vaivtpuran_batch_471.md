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

### Verse 1 (Vaivtpuran 23.4034)
- **Original**: सुवर्ण, वस्त्र, घृत, फल और जल ब्राह्मणोंको उन्हें निर्मल भक्ति भी अवश्य देते हैं। वैष्णव
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.4035)
- **Original**: देनेवाले पुण्यात्मा पुरुष चन्रलोकमें जाते हैं। ब्राह्मणसे भिन्न जो सकाम मनुष्य हैं, वे विष्णुभक्तिसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.4036)
- **Original**: साध्वि! एक मन्वन्तरतक वे वहाँ सुविधापूर्वक रहित होनेके कारण किसी भी जन्ममें विशुद्ध
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.4037)
- **Original**: निवास करते हैं। उस दानके प्रभावसे उन्हें वहाँ बुद्धि नहीं पा सकते। साध्वि! जो तीर्थस्थानमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.4038)
- **Original**: सुदीर्ध कालतक निवास प्राप्त होता है। पतिब्रते! रहकर सदा तपस्या करते हैं, वे द्विज ब्रह्माके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.4039)
- **Original**: पवित्र ब्राह्मणको सुवर्ण, गौ और ताम्र आदि लोकमें जाते हैं और पुण्यभोगके पश्चात्‌ पुनः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.4040)
- **Original**: [द्रव्यका दान करनेवाले सत्पुरुष सूर्यलोकमें जाते भारतवर्षमें आ जाते हैं। भारतमें रहकर अपने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.4041)
- **Original**: हैं। जे भय-बाधासे शून्य हो, उस विस्तृत लोकमें कर्तव्य-कर्मांमें संलग्र रहनेवाले ब्राह्मण तथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.4042)
- **Original**: सुदीर्घ कालतक वास करते हैं। जो ब्राह्मणोंको सूर्यभक्त शरीर त्यागनेपर सूर्यलोकमें जाते हैं और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.4043)
- **Original**: पृथ्वी अथवा प्रचुर धान्य दान करता है, बह पुण्यभोगके पश्चात्‌ पुनः भारतवर्षमें जन्म पाते हैं।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.4044)
- **Original**: भगवान्‌ विष्णुके परम सुन्दर श्वेतद्वीपमें जाता है अपने धर्ममें निरत रहकर शिव, शक्ति तथा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.4045)
- **Original**: और दीर्घकालतक वहाँ वास करता है। भक्तिपूर्वक गणपतिकी उपासना करनेवाले ब्राह्मण शिवलोकमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.4046)
- **Original**: ब्राह्मणफो गृह-दान करनेवाले पुरुष स्वर्गलोकमें जाते हैं; फिर उन्हें लौटकर भारतवर्षमें आना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.4047)
- **Original**: जाते और वहाँ दीर्घकालतक निवास करते हैं; पड़ता है। जो धर्मरहित होनेपर भी निष्कामभावसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.4048)
- **Original**: वे उस लोकमें उतने वर्षोतक रहते हैं, जितनी श्रीहरिका भजन करते हैं, वे भी भक्तिके बलसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.4049)
- **Original**: संख्यामें उस दान-गृहके रज:कण हैं। मनुष्य श्रीहरिके धाममें चले जाते हैं। जिस-जिस देवताके उद्देश्यसे गृह-दान करता है, साध्वि! जो अपने धर्मका पालन नहीं करते,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.4050)
- **Original**: अन्तमें उसी देवताके लोकमें जाता है और घरमें वे आचारहीन, कामलोलुप लोग अवश्य ही
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.4051)
- **Original**: जितने धूलिकण हैं, उतने वर्षोतक वहाँ रहता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.4052)
- **Original**: 180 52%
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.4053)
- **Original**: 0 1222) 2 24 66222 22/ 24402 344 824 / 2 /22/244///448/ 4
- **Translation**: 

---

