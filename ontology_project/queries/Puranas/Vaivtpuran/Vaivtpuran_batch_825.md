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

### Verse 1 (Vaivtpuran 543.14814)
- **Original**: प्रज्वलित दीपक और दर्पण प्रस्तुत किये गये। पहरके बीत जानेपर शुभ बेलामें शुभ नक्षत्रसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14815)
- **Original**: पुरोहितजीने सुल्लनिग्ध दूर्वाकाण्ड, श्वेत पुष्प तथा चन्द्रमाका संयोग होनेपर अमृतयोगसे युक्त लग्न
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14816)
- **Original**: शुभसूचक श्वेत धान्य श्यामसुन्दरके हाथमें दिये। आया। लग्नके स्वामी शुभ ग्रहोंमेंसे कोई एक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14817)
- **Original**: उन सबको लेकर उन्होंने मस्तकपर रख लिया। अथवा बुध थे। उस लग्रपर शुभ ग्रहोंकी दृष्टि थी।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14818)
- **Original**: तत्पश्चात्‌ श्रीहरिने घी, मधु, चाँदी, सोना और पापग्रहोंके संयोगसे जो दुर्योग या दोष आदि प्राप्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14819)
- **Original**: दहीके दर्शन किये। ललाटमें चन्दनका लेप करके होते हैं, उनका उस लग्नमें सर्वधा अभाव था। ऐसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14820)
- **Original**: गलेमें पुष्पमाला धारण की
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14821)
- **Original**: गुरुजनों तथा ब्राह्मणके समयमें श्रीहरिने स्वयं उठकर माता यशोदाकों
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14822)
- **Original**: चरणोंमें भक्तिभावसे मस्तक झुकाया और शह्डुध्वनि, जगाया, मड्जल-कृत्य करवाया और बन्धुजनोंकों
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14823)
- **Original**: वेदपाठ, संगीत, मड्गलाष्टक एवं ब्राह्मणके मनोहर आश्वासन दिया। जो विश्व-ब्रह्माण्डके स्वतन्त्र कर्ता
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14824)
- **Original**: आशीर्वाद बड़े आदरके साथ सुने। सर्वत्र मज्भगल और स्वतन्त्र पालक हैं, उन्हीं भगवानने राधिकाजीके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14825)
- **Original**: प्रदान करनेवाले अपने ही मड्रलमय स्वरूपका भयसे भीत-से होकर बाजा बजानेकी मनाही कर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14826)
- **Original**: ध्यान करके उन्होंने परम सुन्दर दाहिने पैरको आगे दी। वे दोनों पैर धोकर दो शुद्ध वस्त्र धारण करके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14827)
- **Original**: बढ़ाया। नासिकाके वामभागसे वायुको भीतर चन्दन आदिसे लिपे हुए शुद्ध स्थानमें बैठे। उनके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14828)
- **Original**: भरकर भगवान्‌ने मध्यमा अंगुलिसे बामरन्भ्रको वामभागमें चन्दन आदिसे सुसज्जित तथा फल और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14829)
- **Original**: दबाया और नाकके दाहिने छिद्गसे उस वायुकों
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14830)
- **Original**: छडड * संक्षिप्त ब्रह्मवैचर्तपुराण * ###%#%#### #%$%$%% ।]]/]7)]]]]]7]]। 0 8
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14831)
- **Original**: 34.5... बाहर निकाल दिया। तत्पश्चात्‌ नन्दनन्दन नन्दके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14832)
- **Original**: सारतत्त्व्से शत-शत वीथियोंका निर्माण किया श्रेष्ठ प्राद़्णमें सानन्द आये। वे परमानन्दमय,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14833)
- **Original**: गया था। पुण्य वस्तुओंके संचयसे सम्पन्न श्रेष्ठ नित्यानन्दस्वरूप तथा सनातन हैं। नित्य-अनित्य
- **Translation**: 

---

