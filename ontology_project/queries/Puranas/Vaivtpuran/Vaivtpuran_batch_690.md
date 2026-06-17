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

### Verse 1 (Vaivtpuran 119.19050)
- **Original**: अपणिडतो5हमसुरो न सुरः क्षन्तुमहसि। इति भ्रीब्रह्मवैवर्ते बलिकु्त श्रीकृष्णस्तोज॑ सम्पूर्णय्‌। (श्रोकृष्णजन्मखण्ड 119। 23-59 <) #3#83+4_# चर य202/42/-0-90 राधाकृतं श्रीकृष्णस्तोत्रम्‌ राधिकोवाच अद्य में सफल॑ जन्म जीवितं चर सुजीखितम्‌ । यद्‌ दृष्ठा मुखचन्द्र ते सुस्त्रिग्ध॑ लोचन मनः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 119.19051)
- **Original**: पञ्ञ प्राणाश्व स्त्रग्धाक्ष परमात्मा च सुप्रियः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 119.19052)
- **Original**: उभयोईर्षबीज॑ च दुर्लभ बन्धुदर्शनम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 119.19053)
- **Original**: शोकार्णवे निमग्राह॑ प्रदग्धा विरहानलै: । त्वद्दृष्टयामृतवृष्ठणा च सुषिक्ताद्य सुशीतला
- **Translation**: 

---

### Verse 5 (Vaivtpuran 119.19054)
- **Original**: शिवा शिवप्रदाईं च॒ शिवबीजा त्वया सह । शिवस्वरूपा निश्वेष्टाप्पदष्टठा च॒ त्वया बिना
- **Translation**: 

---

### Verse 6 (Vaivtpuran 119.19055)
- **Original**: त्वयि तिष्ठति देहे चर देही भ्रीमाउ्छुचि: स्वयम्‌ । सर्वशक्तिस्वरूपश्च॒ शवरूपो गते त्वयि
- **Translation**: 

---

### Verse 7 (Vaivtpuran 119.19056)
- **Original**: स्त्रीपुंसोर्विशों नाथ सामान्यश्र सुदारुण: । यान्त्येब शक्तिभिः प्राणा विच्छेदात्‌ परमात्मन:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 119.19057)
- **Original**: इत्युक्चा राधिका देवी परमात्मानमीश्चरम्‌ । स्वासने बरासयामास कृत्वा पादार्चन॑मुदा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 119.19058)
- **Original**: इ्ति श्रीब्रह्मवैवर्ते गधाकुत श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 125। 15-21) नतीजा :54950-.0.00
- **Translation**: 

---

### Verse 10 (Vaivtpuran 119.19059)
- **Original**: » भ्रीकृष्णस्तोत्राणि * <31 ब्रह्माण्डपावनं श्रीकृष्णकवचम्‌ शौनक उवाच कि स्तोत्र कबच॑ विष्णोर्मनत्रपूजाविथि: पुरा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 119.19060)
- **Original**: दत्तो वसिष्ठस्ताभ्यां च त॑ भवान्‌ वक्तुमहति
- **Translation**: 

---

### Verse 12 (Vaivtpuran 119.19061)
- **Original**: द्वादशाक्षरमनत्र च शूलिन: कवचादिकम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 119.19062)
- **Original**: दत्त गन्धर्वराजाय वसिष्ठेन च कि पुरा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 119.19063)
- **Original**: तदपि बरूहि हे सौते श्रोतुं कौतृहलं मम । शंकरस्तोत्रकबच॑ मन्त्र दुर्गतिनाशनम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 119.19064)
- **Original**: सौतिरुवाच तुष्टाव ग्रेन स्तोत्रेण मालती परमेश्वरम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 119.19065)
- **Original**: तदेव स्तोत्र दत्त चर मन्त्र च कबच॑ श्रृणु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 119.19066)
- **Original**: 34 नमो भगवते रासमण्डलेशाय स्वाहा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 119.19067)
- **Original**: इमं॑ मन्त्र कल्पतरु प्रददौ घोडशाक्षरम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 119.19068)
- **Original**: पुरा दत्त कुमाराय ब्रह्मणा पुष्करे हरेः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 119.19069)
- **Original**: पुरा दत्त च कृष्णेन गोलोके शंकराय चा
- **Translation**: 

---

