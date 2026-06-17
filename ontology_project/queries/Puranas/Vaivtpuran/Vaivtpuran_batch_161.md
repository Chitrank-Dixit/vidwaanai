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

### Verse 1 (Vaivtpuran 12.806)
- **Original**: करके दास, दासी, माता और पत्नीका तथा पुत्रके कृपा करती है, उसे विष्णु-मन्त्र देती है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.807)
- **Original**: बादकी भी सैकड़ों पीढ़ियोंका उद्धार कर देता जो धर्मात्मा मनुष्य धर्मका भजन करता है,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.808)
- **Original**: है और स्वयं निश्चय ही गोलोकमें जाता है। मनुष्य बह निश्चय ही सम्पूर्ण धर्मका फल पाता है और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.809)
- **Original**: तभीतक कामासक्त होकर गर्भमें निवास करता इहलोकमें सुख भोगकर परलोकमें विष्णुके परमपदको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.810)
- **Original**: है, तभीतक यमयातना भोगता है और गृहस्थ प्राप्त कर लेता है। जो मनुष्य जिस देवताकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.811)
- **Original**: पुरुष तभीतक भोगोंकी इच्छा रखता है, जबतक भक्तिभावसे आराधना करता है, वह पहले उसीको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.812)
- **Original**: कि श्रीकृष्णका सेबन नहीं करता। यमराज उस पाता है, फिर समयानुसार उस देवताके साथ ही
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.813)
- **Original**: भक्तके कर्मसम्बन्धी लेखको तत्काल भयके मारे बह उत्तम बिष्णुधाममें चला जाता है। दूर कर देता है। ब्रह्माजी पहलेसे ही उसके भगवान्‌ श्रीकृष्ण प्रकृतिसे परे तथा तीनों
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.814)
- **Original**: स्वागतके लिये मधुपर्क आदि तैयार करके रखते गुणोंसे अतीत--निर्गुण हैं। ब्रह्मा, विष्णु और शिव
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.815)
- **Original**: हैं और सोचते हैं कि अहो! वह मेरे लोकको आदिके सेव्य, उनके आदिकारण, परात्पर अबिनाशी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.816)
- **Original**: लाँचकर इसी मार्गसे यात्रा करेगा। कोटिशत परब्रह्म एवं सनातन भगवान्‌ हैं। साकार, निराकार,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.817)
- **Original**: कल्पोंमें भी उसका वहाँसे निष्कासन नहीं होगा। ज्योति स्वरूप, स्वेच्छामय, सर्वव्यापी, सर्वाधार,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.818)
- **Original**: जैसे सर्प गरुड़को देखते ही भाग जाते हैं, उसी सर्वेश्वर, परमानन्दमय, ईश्वर, निर्लिप्त तथा साक्षिरूप
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.819)
- **Original**: तरह करोड़ों जन्मोंके किये हुए पाप भी श्रीकृष्ण- हैं। बे भक्तोंपर अनुग्रह करनेके लिये ही दिव्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.820)
- **Original**: भक्तसे भयभीत हो उसे छोड़कर पलायन कर विग्रह धारण करते हैं। जो उनकी आराधना करता
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.821)
- **Original**: जाते हैं। श्रीकृष्ण-भक्त मानव-शरीरको छोड़नेके है, वह सचमुच ही जीवन्मुक्त है। वह बुद्धिमान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.822)
- **Original**: बाद निर्भय हो गोलोकमें जाता है। वहाँ जानेपर पुरुष कोई वर नहीं ग्रहण करता। सालोक्य आदि
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.823)
- **Original**: दिव्य शरीर धारण करके सदा श्रीकृष्णकी सेवा चारों प्रकारकी मुक्तियोंकों भी वह तुच्छ समझने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.824)
- **Original**: करता है। श्रीकृष्ण जबतक गोलोकमें निवास लगता है। त्रह्मत्व, अमरत्व और मोक्ष भी उसके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.825)
- **Original**: करते हैं, तबतक भक्त पुरुष निरन्तर वहाँ उनकी लिये तुच्छ-सा हो जाता है। ऐश्वर्यको बह मिट्टीके
- **Translation**: 

---

