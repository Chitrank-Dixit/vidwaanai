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

### Verse 1 (Vaivtpuran 35.7802)
- **Original**: सा अपराध हुआ ? फिर भी, आपके पिताने महान्‌ *कर्मणा ब्राह्मणो जात: करोति ब्रह्मभावनम्‌ । स्वधर्मनिरत: शुद्धस्तस्माद्‌. ब्राह्मण. ठच्यते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7803)
- **Original**: अन्तर्बहिश्न॒ मननात्‌ू कुर्ते कर्म नित्यश: । मौनी शश्वद्‌ वदेत्‌ काले यो हि स॒ मुनिरुच्यते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7804)
- **Original**: स्वर्ण लोष्टे गृहेउरण्ये पड्ढे सुस्त्ग्धचन्दने । समता भावना यस्थ स योगी परिकीर्तित:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 35.7805)
- **Original**: सर्वजीवेषु यो विष्णु भावयेत्‌ समताधिया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 35.7806)
- **Original**: हरौ करोति भक्ति च हरिभक्त: स च स्मृतः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 35.7807)
- **Original**: (गणपतिखण्ड 35
- **Translation**: 

---

### Verse 7 (Vaivtpuran 35.7808)
- **Original**: 70-73)
- **Translation**: 

---

### Verse 8 (Vaivtpuran 35.7809)
- **Original**: “» गणपेतिस्वण्ड « 371 ।7+774+744]/]//4//4#8/।[[[[[।[(।00008]44/ 0 ] 2 4 8 8
- **Translation**: 

---

### Verse 9 (Vaivtpuran 35.7810)
- **Original**: 4) 448 4
- **Translation**: 

---

### Verse 10 (Vaivtpuran 35.7811)
- **Original**: बल-पराक्रमसे सम्पन्न बहुत-से भूपालॉका वध
- **Translation**: 

---

### Verse 11 (Vaivtpuran 35.7812)
- **Original**: उठाया। त्रिशूल चलाते समय आकाशवाणी कर डाला। इस समय यहाँ शिशु-अवस्थावाले
- **Translation**: 

---

### Verse 12 (Vaivtpuran 35.7813)
- **Original**: हुई--'विप्रवरो! शिंवजीका यहः त्रिशूल अमोघ राजकुमार ही आये हैं। आपने सम्पूर्ण पृथ्वीको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 35.7814)
- **Original**: है, इसे मत चलाओ; क्योंकि मत्स्यराजके गलेमें इक्कीस बार भूपालोंसे शून्य कर देनेके लिये जो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7815)
- **Original**: सर्वाड्रोंकी रक्षा करनेवाला शिवजीका दिव्य प्रतिज्ञा की है, उसका पालन कीजिये। युद्ध करना
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7816)
- **Original**: कबच बँधा है, जिसे पूर्वकालमें दुर्वासाने दिया तो क्षत्रियोंका धर्म ही है। युद्धमें मृत्युको प्राप्त था। अतः: पहले राजासे उस प्राण-प्रदान हो जाना उनके लिये निन्दित नहीं है; परंतु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7817)
- **Original**: करनेवाले कबचको माँग लो।' मुने! तदनन्तर ब्राह्मणोंकी रण-स्पृहा लोक और वेद--दोनोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7818)
- **Original**: परशुरामने त्रिशूल चलाकर राजापर चोट की, विडम्बनाकी पात्र है। वाणी ही जिनका बल और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7819)
- **Original**: परंतु राजाके शरीरसे टकराकर उस त्रिशूलके सौ तप ही जिनका धन है, उन ब्राह्मणोंकी शान्ति
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7820)
- **Original**: टुकड़े हो गये। तब आकाशबाणी सुनकर महान्‌ ही प्रत्येक युगमें स्वस्तिकारक कर्म है। युद्ध
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7821)
- **Original**: पराक्रमी जमदग्रिनन्दन परशुरामने श्रृड्रधारी संन्‍्यासीका करना ब्राह्मणका धर्म नहीं है। शान्तिपरायण
- **Translation**: 

---

