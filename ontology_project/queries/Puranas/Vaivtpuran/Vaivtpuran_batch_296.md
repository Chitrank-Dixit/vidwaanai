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

### Verse 1 (Vaivtpuran 13.12062)
- **Original**: सामग्रीका सानन्द संग्रह करके शास्त्रीय विधिसे गयी हो और प्रात:काल तीन तिथियोंका स्पर्श हो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12063)
- **Original**: प्रेरित हो आवश्यक कार्य करे। षोडश उपचारोंके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12064)
- **Original**: + श्रीकृष्णजन्मखण्ड « 7533 428 2 ।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12065)
- **Original**: ) ]]]]]]][/#+ ऋतिक नाम ये हैं--आसन, वसन, पाद्य, अर्ध्य, पुष्प,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12066)
- **Original**: करता है। बे सर्वश्रेष्ल एवं परम मनोहर हैं। उनके अनुलेपन, धूप, दीप, नैवेद्य, यज्ञोपवीत, आभूषण,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12067)
- **Original**: नेत्र शरत्कालके सूर्योदयकी बेलामें विकसित गन्ध, स्नानीय पदार्थ, ताम्बूल, मधुपर्क और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12068)
- **Original**: होनेवाले कमलोंकी प्रभाको छीन लेते हैं। विभिन्न पुनराचमनीय जल-इन सब सामानोंकों दिनमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12069)
- **Original**: अज्ोंमें धारित रत्रमय आभूषण उनके अपने ही जुटाकर रातमें व्रत-सम्बन्धी पूजनादि कार्य करे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12070)
- **Original**: अज्ञोंकी सौन्दर्य-शोभासे विभूषित होते हैं। गोपियोंकि स्रान आदिसे पवित्र हो धुले हुए धौत और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12071)
- **Original**: प्रसन्नतापूर्ण एवं अनुरागसूचक नेत्रकोण उन्हें उत्तरीय वस्त्र धारण करके आसनपर बैठे। फिर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12072)
- **Original**: सतत निहारते रहते हैं, मानो भगवान्‌का शरीर- आचमन-प्राणायामके पश्चात्‌ श्रीहरिको नमस्कार
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12073)
- **Original**: विग्रह उनके प्राणोंसे ही निर्मित हुआ है। वे करके स्वस्तिवाचन करें। तदनन्तर शुभ बेलामें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12074)
- **Original**: रासमण्डलके मध्यभागमें विराजमान तथा रासोल्लसके सप्तधान्यके ऊपर मज़ल-कलशकी स्थापना करके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12075)
- **Original**: लिये अत्यन्त उत्सुक हैं। राधाके मुखरूपी शरच्वद्धकी उसके ऊपर फल-शाखासहित आप्रपल्लव रखे।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12076)
- **Original**: सुधाका पान करनेके लिये चकोररूप हो रहे हैं। कलशमें चन्दनका अनुलेप करे और मुनियोंने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12077)
- **Original**: मणिराज कौस्तुभकी प्रभासे उनका वक्ष:स्थल वेदोंमें कलशके स्थापन और पूजनकी जो विधि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12078)
- **Original**: अत्यन्त उद्धासित हों रहा है और पारिजात- बतायी है, उसका प्रसन्नतापूर्वक सम्पादन करे।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12079)
- **Original**: पुष्पोंकी विविध मालाओंसे बे अत्यन्त शोभायमान फिर अलग-अलग धान्यपुञ्ञपर छः देवताओंका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12080)
- **Original**: हैं। उनका मस्तक उत्तम रत्नोंके सारतत्त्वसे निर्मित आवाहन करके विद्वान्‌ पुरुष उत्कृष्ट पह्मोपचार-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12081)
- **Original**: दिव्य मुकुटकी ज्योतिसे जगमगा रहा है। मनोविनोदकी सामग्रौद्वारा उनका पूजन करे। वे छः देवता
- **Translation**: 

---

