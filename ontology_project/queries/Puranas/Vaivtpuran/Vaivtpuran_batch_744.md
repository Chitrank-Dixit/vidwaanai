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

### Verse 1 (Vaivtpuran 543.13194)
- **Original**: बोले--'अहो! हमने विश्वनाथकों दिनमें स्वप्रकी मन्दहासकी छटा छा रही थी। वे भक्तोंपर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13195)
- **Original**: भाँति देखा है। भगवान्‌ शिव हम दोनोंको बच्चित अनुग्रहके लिये कातर दिखायी देते थे। अपने
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13196)
- **Original**: करके अपने स्थानकों चले गये।' तेजसे प्रज्वलित हो रहे थे। उनके पाँच मुख। . उन दोनों पति-पत्नौकी भगवान्‌ शिवमें भक्ति और प्रत्येक मुखमें तीन-तीन नेत्र थे। फिर दूसरे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13197)
- **Original**: बढ़ रही है-यह देख सब देवताओंको चिन्ता ही क्षणमें वह भिक्षुक “जगत्स्रष्टा' चतुर्मुख
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13198)
- **Original**: हो गयी। इन्द्र आदि देवता भारसे सुमेरुकी रक्षाके ब्रह्माके रूपमें दृष्टिगोचर हुआ। ब्रह्माजी स्फटिककी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13199)
- **Original**: लिये युक्ति करने लगे। ये आपसमें कहने माला लेकर हरिनामका जप कर रहे थे।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13200)
- **Original**: लगे--'यदि हिमवान्‌ अनन्य भक्तिसे भारतमें हिमवानने देखा, क्षणभरमें वह त्रिगुणात्मक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13201)
- **Original**: भगवान्‌ शिवको कन्यादान करेंगे तो निश्चय ही सूर्यस्वरूप हो गया। अत्यन्त दुःसह प्रकाशसे युक्त
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13202)
- **Original**: निर्वाण-मोक्षको प्राप्त होंगे। अनन्त रत्नोंका सूर्यदेव ब्रह्मतेजसे जाज्वल्यमान थे। फिर एक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13203)
- **Original**: आधार हिमालय यदि पृथ्वीको छोड़कर चला क्षणतक वह अत्यन्त तेजसे प्रज्वलित अग्निके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13204)
- **Original**: जायगा तो इसका “रत्ञगर्भा' नाम अवश्य ही रूपमें विद्यमान रहा। तत्पश्चात्‌ क्षणभर आह्वादजनक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13205)
- **Original**: मिथ्या हो जायगा। शूलपाणि शिवको अपनी चन्द्रमाके रूपमें शोभा पाता रहा। तदनन्तर एक
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13206)
- **Original**: कन्या दे स्थावरत्वका परित्याग और दिव्य रूप
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13207)
- **Original**: + श्रीकृष्णजन्मखण्ड के 575 5%%%###%$%%$ # # # कक कक जन मम मामा म 3299 88% अर 48484 %#% 44 #5# 48 55% 6 % % ## 44 4
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13208)
- **Original**: # ऋ # 8 # $ # ऋ ऋ ऋऊ #
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13209)
- **Original**: ़ 6 6 8 8 5 #% धारण करके वे विष्णुलोकको चले जाय॑ँगे। जो सर्वश्रेष्ठ शिव, दुर्गा, लक्ष्मी, सरस्वती, गीता, तो अनायास ही उन्हें नारायणका सारूप्य प्राप्त
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13210)
- **Original**: तुलसी, गड्जा, वेद, बरेदमाता सावित्री, व्रत, हो जायगा। वे भगवान्‌के पार्षद्भावकों पाकर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13211)
- **Original**: तपस्या, पूजा, मन्त्र तथा मन्त्रदाता गुरुमें दोष हरिदास हो जायँंगे।' यह सब सोचकर देवताओंने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13212)
- **Original**: बताते हैं; वे अन्धकृप नामक नरकमें यातना आपसमें सलाह की और वे गुरु बृहस्पतिको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13213)
- **Original**: भोगते हैं और वहाँ उन्हें ब्रह्मामी आधी आयुतक हिमालयके घर भेजनेके लिये गये। उन सबने
- **Translation**: 

---

