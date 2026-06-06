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

### Verse 1 (Vaivtpuran 22.18243)
- **Original**: 8 4 5 9 4 4
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.18244)
- **Original**: इन्द्र प्रति हरिणोपदिष्ट॑ लक्ष्मीकवचम्‌ नारद उबाच आदविर्भूय हरिस्तस्मै किं स्तोत्र कवच ददा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.18245)
- **Original**: महालक्ष्म्याश्ष लक्ष्मीशस्तन्मे ब्रूहि तपोधन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.18246)
- **Original**: नारायण उवाच पुष्रे च तपस्तप्त्वा विराम सुरेश्व: । आविर्बंभूव तत्रैव क्लिए्ट दृष्ठा हरिः स्वयम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.18247)
- **Original**: तमुबाच इषीकेशो वरें वृणु वधेप्सितम्‌। स चर बत्रे वबरं लक्ष्मीमीशस्तस्मै ददौ मुदा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.18248)
- **Original**: वरं॑ दत्त्ता हृषीकेश: प्रवक्तुमुपचक्रमे । हित॑ सत्य च सारं च परिणामसुखावहम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.18249)
- **Original**: श्रीमधुसूदनउवाच गृहाण कवच शक्र सर्वदुःखविनाशनम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.18250)
- **Original**: परमैश्वर्यजनकं सर्वशत्रुविमर्दनम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.18251)
- **Original**: ब्रह्मणे च पुरा दत्त संसारे च जलप्लुते। यद्‌ धृत्वा जगतां श्रेष्ठ: सर्वैश्वर्ययुतो विधिः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.18252)
- **Original**: बभूवुर्ममव: सर्वे. सर्वैश्चर्ययुता यतः । सर्वैश्वर्यप्रदस्थास्थ कबचस्य ऋषिर्विधि:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.18253)
- **Original**: पड्नक्तिश्ठन्द्श॒ सा देवी स्वयं पद्मालया सुर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.18254)
- **Original**: सिद्धैश्चर्यजपेप्वेव बिनियोग: प्रकीर्तित:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.18255)
- **Original**: यद्‌ धृत्वा कवच लोक: सर्वत्र विजयी भवेत्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.18256)
- **Original**: मस्तक पातु मे यद्मा कणठं पातु हरिप्रिया । नासिकां पातु मे लक्ष्मी: कमला पातु लोचनम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.18257)
- **Original**: केशान्‌ केशवकान्ता च कपालं॑ कमलालया
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.18258)
- **Original**: जगद्मसूर्गण्डयुग्म॑ स्कर्न्ध सम्पत्प्रदा सदा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.18259)
- **Original**: 3» श्री कमलवासिन्ये स्वाहा पृष्ठ सदावतु । 3» श्रीं पद्मालयायै स्वाहा वक्ष: सदावतु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.18260)
- **Original**: पातु श्रीम॑म॒ कड्भालं बाहुयुग्मं च ते नमः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.18261)
- **Original**: 3 हीं श्रीं लक्ष्म्यै नम: पादौ पातु मे संततं चिरम्‌ । 3» हीं भ्रीं नमः पद्मायै स्वाहा पातु नितम्बकम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.18262)
- **Original**: 30 श्रीं महालक्ष्म्यै स्वाहा सर्वाजड्रं पातु मेसदा । 3» हीं श्रीं क्लीं महालध्ष्म्यै स्थाहा मां पातु सर्वत:
- **Translation**: 

---

