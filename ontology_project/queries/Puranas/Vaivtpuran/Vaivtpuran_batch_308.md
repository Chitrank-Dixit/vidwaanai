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

### Verse 1 (Vaivtpuran 13.12302)
- **Original**: पार्वती बोलीं--बेदवती ! तुम्हारा कल्याण मनको मोह लेनेवाली है। ब्रह्मा आदि देवता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12303)
- **Original**: हो। तुम इच्छानुसार वर माँगो। तुम्हारे इस ब्रतसे निरन्तर उनकी स्तुति करते हैं। उनके श्रीअज्ञोंकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12304)
- **Original**: मैं संतुष्ट हूँ; अतः तुम्हें मनोबाज्छित वर दूँगी। प्रभा करोड़ों सूर्योकों लब्जित करती है। नीचे-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12305)
- **Original**: नारद! पार्वतीकी बात सुनकर साध्वी ऊपरके ओठ पके बिम्बफलके सदृश लाल हैं।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12306)
- **Original**: वेदवतीने उन प्रसन्नददया देवीकी ओर देखा और अड्भकान्ति सुन्दर चम्पाके समान है। मोतीकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12307)
- **Original**: दोनों हाथ जोड़ उन्हें प्रणाम करके वह बोली। लड़ियोंकों भी लजानेवाली दन्तावली उनके बेदवतीने कहा--देवि! मैंने नारायणकों मुखकी शोभा बढ़ाती है। बे मोक्ष और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12308)
- **Original**: मनसे चाहा है; अतः वे ही मेरे प्राणबल्लभ पति मनोवाज्छित कामनाओंको देनेवाली हैं।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12309)
- **Original**: हों--यह वर मुझे दीजिये। दूसरे किसी वरको शरत्कालके पूर्ण चन्द्रको भी तिरस्कृत करनेवाली
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12310)
- **Original**: लेनेकी मुझे इच्छा नहीं है। आप उनके चरणोमें चन्द्रमुखी देवी पार्वतीका मैं भजन करता हूँ।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12311)
- **Original**: सुदृढ़ भक्ति प्रदान कीजिये। इस प्रकार ध्यान करके मस्तकपर फूल
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12312)
- **Original**: वेदवतीकी बात सुनकर जगदम्बा पार्वती रखकर ब्रती पुरुष प्रसन्नतापूर्वक हाथमें पुष्प ले [हँस पड़ीं और तुरंत रथसे उतरकर उस पुनः भक्तिभावसे ध्यान करके पूजन आरम्भ करे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12313)
- **Original**: हरिवल्लभासे बोलीं। पूर्वोक्त मन्त्रसे ही प्रतिदिन हर्षपूर्वक पोडशोपचार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12314)
- **Original**: . पार्वतीने कहा--जगदम्ब! मैंने सब जान चढ़ावे। फिर ब्रती भक्ति और प्रसन्नताके साथ ललिया। तुम साक्षात्‌ सती लक्ष्मी हो और पूर्वकथित स्तोत्रट्टारा ही देवीकी स्तुति करके उन्हें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12315)
- **Original**: भारतवर्षकों अपनी पदधूलिसे पवित्र करनेके प्रणाम करे। प्रणामके पश्चात्‌ भक्तिभावसे मनको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12316)
- **Original**: लिये यहाँ आयी हो। साध्वि! परमेश्वरि! तुम्हारी एकाग्र करके गौरीब्रतकी कथा सुने। चरणरजसे यह पृथ्वी तथा यहाँके सम्पूर्ण तीर्थ नारदजीने पूछा--भगवन्‌! आपने ब्रतके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12317)
- **Original**: तत्काल पवित्र हो गये हैं। तपस्विनि! तुम्हारा विधान, फल और गौरीके अद्भुत स्तोत्रका वर्णन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12318)
- **Original**: यह ब्रत लोकशिक्षाके लिये है। तुम तपस्या करो। कर दिया। अब मैं गौरी-ब्रतकी शुभ कथा सुनना
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12319)
- **Original**: देवि! तुम साक्षात्‌ नारायणकी वल्लभा हो और चाहता हूँ। पहले किसने इस ब्रतको किया था ?
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12320)
- **Original**: जन्म-जन्ममें उनकी प्रिया रहोगी। भविष्यमें और किसने भूतलपर इसे प्रकाशित किया था?
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12321)
- **Original**: भूतलका भार उतारनेके लिये तथा यहाँके इन सब यातोंको आप विस्तारपूर्वक बताइये;
- **Translation**: 

---

