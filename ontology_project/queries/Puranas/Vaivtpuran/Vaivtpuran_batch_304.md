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

### Verse 1 (Vaivtpuran 13.12222)
- **Original**: वस्तुओंको ही अपना आहार बनाओ। करनेके योग्य है; जिसमें मज़्लकर्मके अनुष्ठाकका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12223)
- **Original**: यह सुनकर श्रीकृष्णने कहा--तुम लोग संकल्प किया गया है; उसी मासमें तुम लोग
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12224)
- **Original**: आकर अपने-अपने बस्त्र ले जाओ। जलके भीतर घुसकर नंगी नहा रही हो; ऐसा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12225)
- **Original**: यह सुनकर श्रीराधाके अड्भॉमें रोमाश्न हो क्यों किया? इस कर्मके द्वारा तुम अपने ब्रतको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12226)
- **Original**: आया। वे श्रीहरिके निकट वस्त्र लेनेके लिये अज्गहीन करके उसमें हानि पहुँचा रही हो।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12227)
- **Original**: नहीं गयीं। उन्होंने जलमें योगासन लगाकर तुम्हारे पहननेके वस्त्र, पुष्पहार तथा ब्रतके योग्य
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12228)
- **Original**: श्रीहरिके उन चरणकमलोंका चिन्तन किया, जो वस्तुएँ, जो यहाँ रखी गयी थीं, किसने चुरा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12229)
- **Original**: ब्रह्मा, शिव अनन्त (शेषनाग) तथा धर्मके भी लॉ? जो स्त्री ब्रतकालमें नंगी स्नान करती है, वन्दनीय एवं मनोबाझ्छित वस्तु देनेवाले हैं। उन उसके ऊपर स्वयं बरुणदेव रुष्ट हो जाते हैं।।चरणकमलोंका चिन्तन करते-करते उनके नेत्रोंमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12230)
- **Original**: + श्रीकृष्णजन्मखण्ड * 539 55% $ % $ 55 5 $5 45 £ 55 6 45 #& % 4; 64 4 # 4444 4444 646 4644 8464 4444 44 ## 444 5 #% 5 555 5555% 44 8 .... आँसू उमड़ आये और वे भावातिरिकसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12231)
- **Original**: उन आप परमेश्वरको बारंबार नमस्कार है। जिनके उन गुणातीत प्राणेश्वरकी स्तुति करने लगीं।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12232)
- **Original**: सेवकोके स्पर्श और निरन्तर ध्यानसे तीर्थ पवित्र राधिका बोलीं--गोलोकनाथ! गोपीश्वर!
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12233)
- **Original**: होते हैं; उन भगवान्‌को मेरा नमस्कार है। मेरे स्वामिन्‌! प्राणवल्लभ! दीनबन्धों! दीनेश्वर! यों कहकर सती देवी राधिका अपने सर्वेश्वर! आपको नमस्कार है। गोपेश्वर! गोसमुदायके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12234)
- **Original**: शरीरकों जलमें और मन-प्राणोंको श्रीकृष्णमें ईश्वर! यशोदानन्दवर्धन! नन्दनन्दन! सदानन्द!
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12235)
- **Original**: स्थापित करके ढूँठे काठके समान अविचल- नित्यानन्द! आपको नमस्कार है। इन्द्रके क्रोधको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12236)
- **Original**: भावसे स्थित हो गयीं। श्रीराधाद्वारा किये गये भड़ (व्यर्थ) करनेवाले गोविन्द! आपने ब्रह्माजीके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12237)
- **Original**: श्रीहरिके इस स्तोत्रका जो मनुष्य तीनों संध्याओंके दर्षका भी दलन किया है। कालियदमन!
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12238)
- **Original**: समय पाठ करता है, वह श्रीहरिकी भक्ति और प्राणनाथ ! श्रीकृष्ण! आपको नमस्कार है। शिव
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12239)
- **Original**: दास्यभाव प्राप्त कर लेता है तथा उसे निश्चय और अनन्तके भी ईश्वर! ब्रह्मा और ब्राह्मणोंके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12240)
- **Original**: ही श्रीराधाकी गति सुलभ होती है।* जो विपत्तिमें ईश्वर! परात्पर! ब्रह्मस्वरूप! त्रह्मज्ञ! ब्रह्मबीज!
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12241)
- **Original**: भक्तिभावसे इसका पाठ करता है, उसे शीघ्र ही आपको नमस्कार है। चराचर जगत्ूपी वृक्षके
- **Translation**: 

---

