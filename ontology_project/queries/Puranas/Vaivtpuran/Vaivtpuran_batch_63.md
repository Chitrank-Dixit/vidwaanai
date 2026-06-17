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

### Verse 1 (Vaivtpuran 6.2479)
- **Original**: पद अथवा अमरत्व-कुछ भी पानेकी अभिलाषा बात सुनकर उनके आराध्य स्वामी भगवान्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.2480)
- **Original**: बह नहीं करता। ब्रह्मा, इन्द्र एवं मनुकी उपाधि श्रीहरिका मुखमण्डल मुस्कानसे खिल उठा। फिर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.2481)
- **Original**: तथा स्वर्गके राज्यका सुख-ये सभी परम दुर्लभ वे अत्यन्त गूढ़ एवं श्रेष्ठ रहस्य कहनेके लिये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.2482)
- **Original**: हैं; किंतु मेरा भक्त स्वप्नमें भी इनकी इच्छा नहीं प्रस्तुत हो गये। करता । ऐसे मेरे बहुत-से भक्त भारतवर्षमें श्रीभगवान्‌ बोले--लक्ष्मी ! भक्तोंके लक्षण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.2483)
- **Original**: निवास करते हैं। उन भक्तोंके-जैसा जन्म सबके श्रुति एवं पुराणोंमें छिपे हुए हैं। इन पुण्यमय
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.2484)
- **Original**: लिये सुलभ नहीं हैं। जो सदा मेरा गुणानुवाद लक्षणोंमें पापोंका नाश करने, सुख देने तथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.2485)
- **Original**: सुनते और सुनने योग्य पद्मोंकों गाकर आनन्दसे भुक्ति-मुक्ति प्रदान करनेको प्रचुर शक्ति है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.2486)
- **Original**: विह्ल हो जाते हैं, वे बड़भागी भक्त अन्य जिसको सदूुरुके द्वारा विष्णुका मन्त्र प्राप्त होता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.2487)
- **Original**: साथारण मनुष्य, तीर्थ एवं मेरे परमधामकों भी है (और जो सब कुछ छोड़कर केवल मुझको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.2488)
- **Original**: पवित्र करके धराधामपर पधारते हैं। ही सर्वस्व मानता है), उसीको वेद-वेदाड़ पद्मे! इस प्रकार मैंने तुम्हारे प्रश्नका समाधान पुण्यात्मा एवं श्रेष्ठ मनुष्य बतलाते हैं। ऐसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.2489)
- **Original**: कर दिया। अब तुम्हें जो उचित जान पड़े, वह व्यक्तिके जन्म लेनेमात्रसे पूर्वके सौ पुरुष, चाहे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.2490)
- **Original**: करों। तदनन्तर वे सभी देवियाँ, भगवान्‌ श्रीहरिने वे स्वर्गमें हों अथवा नरकमें-तुरंत मुक्तिके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.2491)
- **Original**: जो कुछ आज्ञा दी थी, उसीके अनुसार कार्य करनेमें अधिकारी हो जाते हैं। यदि उन पूर्वजोंमेंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.2492)
- **Original**: संलग्र हो गयीं। स्वयं भगवान्‌ अपने सुखदायी किन्हींका कहीं जन्म हो गया है तो उन्होंने जिस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.2493)
- **Original**: आसनपर विराजमान हो गये। योनिमें जन्म पाया है, वहीं उनमें जीवन्मुक्तता (अध्याय 6) हज 408 रस 42 00000 *न हाम्भयानि तीर्थानि न देवा मृच्छिलामया:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.2494)
- **Original**: ते पुनन्त्यप कालेन बविष्णुभक्ता: क्षणादहों
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.2495)
- **Original**: (प्रकृतिखण्ड 6। 110) न बाजञ्छन्ति सुखं मुक्ति सालोक्यादिचतुष्टयम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.2496)
- **Original**: ब्रह्मत्वममरत्व॑या तद्वाब्छा मम सेबने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.2497)
- **Original**: इन्द्र्व॑ च मनुत्य॑ च ब्रह्मत्व॑ च सुदुर्लभम्‌ । स्वर्गराज्यादिभोग॑ च स्वप्रेषपि च न वाज्छति
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.2498)
- **Original**: (प्रकृतिखण्ड 6। 119-120)
- **Translation**: 

---

