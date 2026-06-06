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

### Verse 1 (Bramha 0.6901)
- **Original**: यह सुनकर अर्जुनने धर्मराजके पास जा पहले कौन विश्वास कर सकता था और फिर
- **Translation**: 

---

### Verse 2 (Bramha 0.6902)
- **Original**: अपनी देखी और अनुभव की हुई सारी बातें तुम्हें आभीरोंसे परास्त होना पड़ेगा-यह बात
- **Translation**: 

---

### Verse 3 (Bramha 0.6903)
- **Original**: कह सुनायी । अर्जुनके मुखलसे मेरा संदेश सुनकर कौन मान सकता था। परंतु दोनों ही बातें सम्भव
- **Translation**: 

---

### Verse 4 (Bramha 0.6904)
- **Original**: समस्त पाण्डव परीक्षित्‌कों राज्यपर अभिषिक्त हुईं। पार्थ ! यह सम्पूर्ण भूतोंमें श्रीहरिकी लीलाका
- **Translation**: 

---

### Verse 5 (Bramha 0.6905)
- **Original**: करके बनमें चले गये। मुनिवरों! इस प्रकार ही -विलास है। अतः तुम्हें तनिक भी शोक नहीं
- **Translation**: 

---

### Verse 6 (Bramha 0.6906)
- **Original**: मैंने आपलोगोंसे यदुकुलमें अवतीर्ण भगवान्‌ करना चाहिये। सम्पूर्ण जगतके स्वामी भगवान्‌
- **Translation**: 

---

### Verse 7 (Bramha 0.6907)
- **Original**: श्रीकृष्णकी सम्पूर्ण लीलाओंका विस्तारपूर्वक श्रीकृष्णने हो सम्पूर्ण यादवोंका संहार किया है।
- **Translation**: 

---

### Verse 8 (Bramha 0.6908)
- **Original**: वर्णन किया। “स्पा 20>त> श्रीहरिके अनेक अवतारोंका संक्षिप्त वर्णन मुनियोंने कहा--मुनिश्रेष्ट! आपने श्रीकृष्ण
- **Translation**: 

---

### Verse 9 (Bramha 0.6909)
- **Original**: पुनः वर्णन कीजिये। हमने साधु पुरुषोंके मुखसे और बलरामका कैसा अद्भुत माहात्म्य बतलाया!
- **Translation**: 

---

### Verse 10 (Bramha 0.6910)
- **Original**: सुना है कि पुराणोंमें अमिततेजस्वी भगवान्‌ उनकी महिमा अलौकिक है। इस पृथ्वीपर
- **Translation**: 

---

### Verse 11 (Bramha 0.6911)
- **Original**: विष्णुके वाराह अबतारका वर्णन हैं। ब्रह्मन्‌! भगवान्‌के माहात्म्यकी चर्चा अत्यन्त दुर्लभ है।
- **Translation**: 

---

### Verse 12 (Bramha 0.6912)
- **Original**: भगवान्‌ नारायणने किस प्रकार वाराहरूप धारण महाभाग! आपके मुखसे भगवत्कथा सुनते-सुनते
- **Translation**: 

---

### Verse 13 (Bramha 0.6913)
- **Original**: किया? और किस प्रकार अपनी दंष्टासे एकार्णवर्में हमें तृप्ति नहों होती, अत: उनकी लीलाओंका
- **Translation**: 

---

### Verse 14 (Bramha 0.6914)
- **Original**: डूबी हुई पृथ्वीका उद्धार किया? सबको अपनी अन-बननन-म-म-म-नननानाया न जन्‍ननन-न-मममननननन-+--+332पयरनरअअनननगनगननननन+मन-+3+3+33393यययदणशति;ओओणनणझ यि * जातस्यथ नियतों मृत्यु: पतने च तथोम्नत: । विप्रयोगावसानस्तु संयोग: संचय: क्षय:
- **Translation**: 

---

### Verse 15 (Bramha 0.6915)
- **Original**: विज्ञाप न बुधा: शोकं न हर्षमुपयान्ति ये । तेपामेवेतरे चेष्टां शिक्षन्त: सन्ति तादशा:
- **Translation**: 

---

### Verse 16 (Bramha 0.6916)
- **Original**: 89-10)
- **Translation**: 

---

### Verse 17 (Bramha 0.6917)
- **Original**: 336 * साक्षप्त ब्नह्मपुराण * ओर आकृष्ट करनेवाले परम बुद्धिमान्‌ भगवान्‌
- **Translation**: 

---

### Verse 18 (Bramha 0.6918)
- **Original**: उनके नख, पशु उनके घुटने तथा यज्ञ उनका श्रीहरिकी समस्त लीलाओंका हम विस्तारपूर्वक
- **Translation**: 

---

### Verse 19 (Bramha 0.6919)
- **Original**: स्वरूप है। उद्भाता अन्त्र (आँत), होम लिड्र, श्रवण करना चाहते हैं। ' ओषधि एवं महान्‌ फल बीज हैं। वादी अन्तरात्मा, व्यासजी बोले--मुनिवरो ! तुमलोगोंने मुझपर मन्त्र नितम्ब और सोमरस उनका रक्त है। वेदी यह बहुत बड़े प्रश्कका भार रख दिया। मैं कंधा, हविष्य गन्ध तथा हव्य और गव्य उनका यथाशक्ति तुम्होरें प्रश्नोंका उत्तर दूँगा। भगवान्‌
- **Translation**: 

---

### Verse 20 (Bramha 0.6920)
- **Original**: प्रचण्ड वेग है। प्राग्वंश (यजमान-गृह) उनका विष्णुकी लीला-कथाका श्रवण करो। भगवान्‌
- **Translation**: 

---

