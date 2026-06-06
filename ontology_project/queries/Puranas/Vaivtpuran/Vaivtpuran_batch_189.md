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

### Verse 1 (Vaivtpuran 13.3149)
- **Original**: उसकी कमरमें सुशोभित थी। मालतीके पुष्पोंकी सम्पन्न वह देवी वहीं रहकर समय व्यतीत कर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3150)
- **Original**: मालासे सम्पन्न केश-कलाप उसके मस्तकपर रही थी। नारद! उसी समय महान्‌ योगी शह्डुचूड़का
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3151)
- **Original**: शोभा पा रहे थे। उसके कानोंमें अमूल्य रक्नोंसे बदरीवनमें आगमन हो गया। जैगीषव्यमुनिकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3152)
- **Original**: बने हुए मकराकृत कुण्डल थे। सर्वोत्तम रज्रोंसे कृपासे भगवान्‌ श्रीकृष्णका मनोहर मन्त्र उसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3153)
- **Original**: निर्मित हार उसके वक्ष:स्थलकों समुज्ज्वल बना प्राप्त हो चुका था। उसने पुष्करक्षेत्रमें रहकर उस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3154)
- **Original**: रहा था। रत्रमय कंकण, केयूर, शद्ध और मन्त्रकों सिद्ध भी कर लिया था। सर्वमड्भलमय
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3155)
- **Original**: अँगूठियाँ उस देवीकी शोभा बढ़ा रही थीं। कबचसे उसके गलेकी शोभा हो रही थी। ब्रह्मा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3156)
- **Original**: साध्वी तुलसीका आचरण अत्यन्त प्रशंसनोय उसे अभिलषित वर दे चुके थे और उन्हींकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3157)
- **Original**: था। ऐसे भव्य शरीरसे शोभा पानेवाली उस आज्ञासे वह वहाँ आया भी था। वह आ रहा था,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3158)
- **Original**: सुन्दरी तुलसीको देखकर शद्गुचूड़ उसके पास तभी तुलसीकी दृष्टि उसपर पड़ गयी। उसकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3159)
- **Original**: आकर बैठ गया और मीठे शब्दोंमें बोला। सुन्दर कमनीय कान्ति थी। उसकी कान्ति श्वेत। . शद्भुचूड़ने पूछा--देवि! तुम कौन हो? चम्पाके समान थी। रत्रमय अलंकारोंसे वह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3160)
- **Original**: तुम्हारे पिता कौन हैं? तुम अवश्य ही सम्पूर्ण अलंकृत था। उसके मुखकी शोभा शरत्पूर्णिमाके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3161)
- **Original**: स्त्रियोंमें धन्यवाद एवं समादरकी पात्र हो। समस्त अन्द्रमाकी तुलना कर रही थी। नेत्र ऐसे जान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3162)
- **Original**: मड्डल प्रदान करनेवाली कल्याणि! तुम वास्तवमें पड़ते थे, मानो शरत्कालके प्रफुल्ल कमल हों। दो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3163)
- **Original**: हो कौन? सदा सम्मान पानेवाली सुन्दरि! तुम रत्रमय कुण्डल उसके गण्डस्थलको छबि बढ़ा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3164)
- **Original**: अपना परिचय देनेकी कृपा करो। रहे थे। पारिजातके पुष्पोंकी माला उसके गलेको नारद! सुन्दर नेत्रोंसे शोभा पानेवाली तुलसीने सुशोभित कर रही थी और उसका मुखकमल
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3165)
- **Original**: शद्नचूड़के ऐसे बचनकों सुनकर मुख नोचेकी मुस्कानसे भरा था। कस्तूरी और कुछ्डूमसे युक्त
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3166)
- **Original**: ओर झुकाकर उससे कहना आरम्भ किया।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3167)
- **Original**: ] संक्षिम ख्रह्मवैवर्तपुराण # श्ड8 त॑ अंश ऋअऋ अं अत अं ऋ 92 5/ 4 94% 54% 25% 5424: 44#/89 84922 84% 4
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3168)
- **Original**: 9 94484 871
- **Translation**: 

---

