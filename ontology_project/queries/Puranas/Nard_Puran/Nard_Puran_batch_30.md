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

### Verse 1 (Nard Puran 0.581)
- **Original**: योगानामादिभूत॑ त॑ नमामि प्रणवस्थितम्‌। नादात्मक॑ नादबौज॑ प्रणब्रात्मकमव्ययम्‌
- **Translation**: 

---

### Verse 2 (Nard Puran 0.582)
- **Original**: सद्भावं सच्चिदानन्द॑ ते वन्दे तिम्मचक्रिणम्‌। अजरं साक्षिणं त्वस्थ द्वावाइसनसगोचरम्‌ निरञ्नमनन्ताख्ये विष्णुरूप॑ नतो5स्म्यहम्‌
- **Translation**: 

---

### Verse 3 (Nard Puran 0.583)
- **Original**: इच्द्रियाणि मनो बुद्धि: सत्त्वं तेजो बल॑ धृति:
- **Translation**: 

---

### Verse 4 (Nard Puran 0.584)
- **Original**: वासुदेवात्मकान्याहु: क्षेत्र. क्षेत्रज़्णमेषग. च। विद्याविद्यात्मक॑ प्राहु: परात्परतरं तथा
- **Translation**: 

---

### Verse 5 (Nard Puran 0.585)
- **Original**: अनादिनिधनं शान्त॑ सर्वधातास्मच्युतम्‌ । ये प्रपन्ना महात्मानस्तेषां मुक्तिहँँ शाश्वती
- **Translation**: 

---

### Verse 6 (Nard Puran 0.586)
- **Original**: यर॑ वरेण्य॑ बरद॑ पुराण सनातन॑ सर्वगतं॑ समस्तम्‌। नतो5स्मि भूयो5पि नतो5स्मि भूयों नतो5स्मि भूयो5पि नतो5स्मि भूयः
- **Translation**: 

---

### Verse 7 (Nard Puran 0.587)
- **Original**: यत्पादतोयं भवरोगवैद्यों यत्पादपांशुविंमलत्वसिद्धयै। यन्नाम दुष्कर्मनिवारणाय तमप्रमेयं पुरुष भजामि
- **Translation**: 

---

### Verse 8 (Nard Puran 0.588)
- **Original**: सद्रूपं तमसद्रूप॑ सदसद्रूपमव्ययम्‌
- **Translation**: 

---

### Verse 9 (Nard Puran 0.589)
- **Original**: तततट्विलक्षणं. श्रेष्ठ. श्रेष्ठाच्छेष्ठतरं भजे
- **Translation**: 

---

### Verse 10 (Nard Puran 0.590)
- **Original**: निरज्न निराकार॑ पूर्णमाकाशमध्यगम्‌। परं॑च विद्याविद्याभ्यां हृदम्बुजनिवासिनम्‌
- **Translation**: 

---

### Verse 11 (Nard Puran 0.591)
- **Original**: स्वप्रकाशमनिर्देश्य॑ महतां च महत्तरम्‌ । अणोरणोयांसम्जं सर्वोपाधिविवर्जितम्‌
- **Translation**: 

---

### Verse 12 (Nard Puran 0.592)
- **Original**: यत्नित्य॑ परमानन्द॑ पर॑ ब्रह्म सनातनम्‌। विष्णुसंज्ञजगद्धाम तमस्मि शरणं गतः
- **Translation**: 

---

### Verse 13 (Nard Puran 0.593)
- **Original**: यं भजन्ति क्रियानिष्ठा यं पश्यन्ति च योगिनः । पृज्यात्पूज्यतरं शान्तं गतोउस्मि शरणं प्रभुष्‌
- **Translation**: 

---

### Verse 14 (Nard Puran 0.594)
- **Original**: ये न पश्यन्ति विद्वांसो य एतद्‌ व्याप्य तिप्ठति। सर्वस्मादधिक नित्य॑ नतो5स्मि विभुमव्ययम्‌
- **Translation**: 

---

### Verse 15 (Nard Puran 0.595)
- **Original**: अन्त:करणसंयोगाज्जीव इत्युव्यतें। च य;। अविद्याकार्ययहित: परमात्मेति. गौयत्ते
- **Translation**: 

---

### Verse 16 (Nard Puran 0.596)
- **Original**: सर्वात्मूफे सर्वहितुं सर्वकर्मफलप्रदम्‌ । वरं॑ वरेण्यमजनं प्रणतो5स्मि परात्परम्‌
- **Translation**: 

---

### Verse 17 (Nard Puran 0.597)
- **Original**: सर्वज्ञ सर्वंग॑ शान्त सर्वान्तर्यामिणं हरिम्‌ । ज्ञानात्मक॑ ज्ञाननि्धि ज्ञानसंस्थं विभुं भजे
- **Translation**: 

---

### Verse 18 (Nard Puran 0.598)
- **Original**: नमाम्यहं वेदनिरधिं मुरारि वेदान्तविज्ञानसुनिश्चितार्थम्‌
- **Translation**: 

---

### Verse 19 (Nard Puran 0.599)
- **Original**: सूर्यन्दुवत्प्रोज्वलनेत्रमिन्द्रं खगस्वरूपं च पतिस्वरूपम्‌
- **Translation**: 

---

### Verse 20 (Nard Puran 0.600)
- **Original**: सर्वेश्वर॑ सर्बगत॑ महान्त॑ वेदात्पक॑ वेदविदां वरिष्ठप्‌। त॑ वाइमनो5चिन्त्यमनन्तशक्ति ज्ञानैकवेच्ध पुरुष भजामि
- **Translation**: 

---

