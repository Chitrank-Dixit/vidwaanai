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

### Verse 1 (Vaivtpuran 543.13214)
- **Original**: रहना पड़ता है तथा वे सर्प-समूहोंसे भक्षित हो गुरुको प्रणाम करके निवेदन किया--'गुरुदेव!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13215)
- **Original**: सदा चीखते-चिह्लते रहते हैं। जो दूसरे देवताओंके आप हिमालयके यहाँ जाकर उनके समक्ष
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13216)
- **Original**: साथ तुलना करके भगवान्‌ हषीकेशकी निन्‍्दा भगवान्‌ शिवकी निन्‍्दा कीजिये। यह तो निश्चय
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13217)
- **Original**: करते हैं; विष्णुभक्ति प्रदान करनेवाले पुराणमें, है कि दुर्गा शिवके सिवा दूसरे किसी वरका जो श्रुतिसे भी उत्कष्ट है, दोष निकालते हैं; राधा वरण नहीं करेगी। उस दशामें हिमवान्‌ अनिच्छासे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13218)
- **Original**: तथा उनकी कायब्यूहरूपा गोपियोंकी और सदा ही अपनी पुत्री शिवको देंगे। ऐसा करनेसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13219)
- **Original**: पूजित होनेवाले ब्राह्मणोंकी भी निन्‍्दा करते हैं; कन्यादानका फल कम हो जायगा। कालान्तरमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13220)
- **Original**: वे देवता ही क्‍यों न हों, ब्रह्माजीकी आयुपर्यन्त गिरिराज भले ही मुक्त हो जाये; परंतु इस समय
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13221)
- **Original**: नरकके गड्ढेमें पकाये जाते हैं। उनके मुँह नीचे तो इन्हें पृथ्वीपर रहना ही चाहिये। भगवन्‌! आप
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13222)
- **Original**: लटकाये जाते हैं और उनकी जाँघें ऊपरकी ओर ही अनन्त रत्नोंके आधारभूत हिमालयको भारतवर्षमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13223)
- **Original**: होती हैं। विकृताकार सर्पसमूह तथा सर्पकी-सी रखिये। (इन्हें यहाँसे जाने न दीजिये।) आकृतिवाले कौट उनके सारे अज्जॉमें लिपटकर देवताओंका वचन सुनकर गुरु बृहस्पतिजीने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13224)
- **Original**: काटते रहते हैं और वे अत्यन्त कातर तथा दोनों हाथ कानोंमें लगा लिये और “नारायण!'
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13225)
- **Original**: भयभीत हो सदा आर्तनाद किया करते हैं। निश्चय “नारायण !' का स्मरण करते हुए उनकी प्रार्थना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13226)
- **Original**: ही वहाँ उन्हें क्षोभपूर्वक कफ एवं मल-मूत्र खाने अस्वीकार कर दी। वेद-बेदान्तके विद्वान्‌ बृहस्पति
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13227)
- **Original**: पड़ते हैं। रोषसे भरे हुए यमराजके किड्जूर उनके हरि और हरके महान्‌ भक्त थे। उन्होंने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13228)
- **Original**: मुँहमें जलती हुई लुआठी डाल देते हैं। तौनों देवताओंको बारंबार फटकारकर कहा। संध्याओंके समय उन्हें डाँट बताते हुए डंडोंसे बृहस्पति बोले--स्वार्थ-साधनमें तत्पर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13229)
- **Original**: पीठते हैं। डंडॉंके प्रहारसे जब उन्हें प्यास लगती रहनेवाले देवताओ! मेरी सच्ची बात सुनो। मेरा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13230)
- **Original**: है, तब वे उन यमदूतोंके भयसे मूत्र-पान करते यह वचन नीतिका सारतत्त्व, वेदोंद्वारा प्रतिपादित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13231)
- **Original**: हैं। जब दूसरा कल्प आरम्भ होता है और पहले- तथा परिणाममें सुख देनेवाला है। जो पापी शिव
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13232)
- **Original**: पहल सृष्टिका आयोजन किया जाता है, उस और बविष्णुके भक्तकी, भूदेवता ब्राह्मणोंकी, गुरु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13233)
- **Original**: समय उन पापियोंके पापोंका निवारण होता और पतित्रताकी, पति, भिक्षु, ब्रह्मचारी तथा
- **Translation**: 

---

