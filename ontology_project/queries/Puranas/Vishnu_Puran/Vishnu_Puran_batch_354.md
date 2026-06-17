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

### Verse 1 (Vishnu Puran 0.7061)
- **Original**: सीरध्वजस्यापत्यं भानुमान्‌ भानुमतरशतहुन्न: तस्य तु शुचिः तस्माधचोर्जनामा पुत्रों जज्ञे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7062)
- **Original**: तस्थापि झतध्वज:, तत: कृति: कृतेरख्नन: , तत्पुत्र: कुरुजित्‌ ततो5रिष्टनेमि: मात. श्रुतायुष: सुपार्श तस्मात्सुज्ञग:, ततः क्षेमाविनो5नेना तस्माद्धामरथ:, तस्य सत्यरथः, तस्मादुपगु- रुपगोरुपगुप्त:, तत्पुत्र: स्वागतस्तस्य च स्वानन्दः, तस्माश्च सुवर्चा:, तस्य च सुपार्श्व:, तस्थापि सुभाष: , तस्थ सुश्नुत: तस्मात्सुश्रुताज्जय: तस्य पुत्रो विजयो विजबस्य ऋतः, ऋतात्सुनयः सुनयाद्वीतहव्य: तस्मादधृतिर्धृतिर्बहुलाश्र: , तस्य पुत्र: कृति:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7063)
- **Original**: कृतौ सन्तिष्ठतेडयं जनकजंशः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7064)
- **Original**: इत्येते मैथिलछा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7065)
- **Original**: प्रायेणैते आत्मविद्याभ्रयिणो भूपाला भवन्ति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7066)
- **Original**: राजाके ऐसा कहनेपर देवताओंने उनको समस्त जीवॉके नेत्रोमें अवस्थित कर दिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7067)
- **Original**: तभीसे प्राणी निमेषोत्भेष (पलक खोलना-मुँदना) करने लगे हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7068)
- **Original**: तदननत्तर अराजकताके भयसे मुनिजनोंने उस पुत्रहीन राजाके दशरीस्को अरणि (दामीदण्ड) से मैथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7069)
- **Original**: उससे एक कुमार उत्पन्न हुआ जो जन्म लेनेके कारण 'जनक' कहलाया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7070)
- **Original**: इसके पिता विदेश थे इसल्ये यह 'वैदेह' कहलाता है, और मन्थनसे उत्पन्न होनेके कारण 'मिथि' भी कहा जाता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7071)
- **Original**: उसके उदावसु नामक पुत्र हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7072)
- **Original**: डदावसुके नन्दिवर्द्धन, नन्दिषर्द्धधके सुकेतु, सुकेतुके देवरात, देवरातके सुघृतिके घृष्टकेतु, घृष्टकेतुके हर्यश्व, हर्यश्वके मनु, मनुके प्रतिक, प्रतिकके कृतरथ, कृतरथके देवमीौढ, देवमीढके हस्वरोमा और हृस्वरोमाके सौरध्चज नामक पुत्र हुआ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7073)
- **Original**: 28--27
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7074)
- **Original**: खह पुत्रकी कासनासे यज्ञभूमिको जोत रहा था। इसी समय हल्के अग्र भागमें उसके सीता नामक़ी कन्या उत्पन्न हुई
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7075)
- **Original**: सीरध्वजका भाई सांकाश्यनरेश . कुशध्वज था
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7076)
- **Original**: सीरध्वजके भानुमान्‌ नामक पूत्र हुआ। भानुमानके शतघुप्न, शतघुप्नके शुचि, शुचिके ऊर्जनामा, ऊर्जनामाके शतध्वज़, शतध्वजके कृति, कृतिके अज्ञन, अज्जनके कुरुजित्‌, कुरुजितके अरिप्टनेमि, अरिष्टनेमिके श्रुतायु, श्रुतायुके सुपार्थ, सुपार्थके सूझ्य, सृझयके श्षेमाबी, क्षेमाजीके अनेना, अनेनाके भौमरथ, भौमरथके सत्यरथ, सत्यरथके ठपगु, उपगुके उपगुप्त, उपगुप्तके स्वागत, स्वागतके स्वानन्द, स्वानन्दके सुबर्चा, सुबर्चाके सुपार्श्व, सुपार्शके सुभाष, सुभाषके सुश्रुत, सुश्रुतके जय, जयके लिजय, लिजयके ऋत, ऋतके सुनय, सुनयक्के यीतहख्य, वीतहव्यके धृति, धतिके बहुलाभश्र और जहुस्तश्नके कृति नामक पुत्र हुआ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7077)
- **Original**: कृतिमें ही इस जनकलंशक्ती समात्ि हो जाती है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7078)
- **Original**: ये ही मैथिलमूपालगण हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7079)
- **Original**: प्रायः ये सभो राजालोग आत्मविद्याकों आश्रय देनेवाले होते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7080)
- **Original**: न जद “तन इति श्रीविष्णुपुराणे चतुर्थे5शे पदञ्नमोउध्यायः
- **Translation**: 

---

