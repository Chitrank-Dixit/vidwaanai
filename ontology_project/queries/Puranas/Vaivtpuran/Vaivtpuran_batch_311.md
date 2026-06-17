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

### Verse 1 (Vaivtpuran 13.17691)
- **Original**: यात्राकाले पठित्वा तु यो याति भक्तिपूर्वकम्‌ । तस्थ सर्वाभीष्टसिद्धिर्भवत्येव. न संशव:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.17692)
- **Original**: तेन वृष्ट अर दुःवप्रं सुस्वप्रमुपजायते । कदापि न भवेत्तस्थ ग्रहपीड़ा क्र दारुणा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.17693)
- **Original**: भवेद्‌ विनाश: शत्रुणां बन्धूनां च विवर्धनम्‌ । शश्रद्विँ्रविनाशश्च॒ शश्वत्‌. सप्पद्ठिवर्धनम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.17694)
- **Original**: स्थिरा भवेद्‌ गृहे लक्ष्मी: पुत्रपौत्रविवर्धिनी । सर्वैश्वर्यमिह् प्राप्य ह्ान्ते विष्णुपर्द लभेत्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.17695)
- **Original**: 'फल॑ चापि च तीर्थानां यज्ञानां यद्‌ भवेद्‌ श्रुवम्‌ । महतां सर्वदानानां. श्रीगणेशप्रसादत:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.17696)
- **Original**: डति श्रीब्रह्मवैवर्ते श्रीविष्पुकृत॑ं गणेशस्तोत्रं सम्पूर्णयू्‌। (गणपतिखण्ड 13
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.17697)
- **Original**: 40-58) 8 340 विष्णूपदिष्ठट॑ गणेशनामाष्टकं स्तोत्रम्‌ विष्णुरुवाच गणेशमेकदन्त॑ त्ञ हेरम्ब॑ विप्ननायकम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.17698)
- **Original**: लम्बोदर॑ शूर्पकर्ण गजवक्त्य॑ गुहाग्रजम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.17699)
- **Original**: नामाष्टार्थ॑ च्॒ पुत्रस्य श्रूणु मातहरप्रिये । स्तोत्राणां सारभूत॑ चर सर्वविप्नहर॑ परम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.17700)
- **Original**: ज्ञानार्थाचको गश्चन॒ णश्न॒ निर्वाणवाचक: । तयोरीशं पर ब्रह्म गणेशं प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.17701)
- **Original**: एकशब्द: प्रधाना्थों दन्‍तश्च॒ बलवाचक: । बल॑ प्रधानं सर्वस्मादेकदन्त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.17702)
- **Original**: दीनार्थाचको हेश्व रम्य: पालकवाचक: । दीनानां परिपालकं हेरम्यं॑ प्रणमाप्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.17703)
- **Original**: विपत्तिवाचको विपध्लो नायक: खण्डनार्थक: । विपत्खण्डनकारक॑ नमामि विप्ननायकम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.17704)
- **Original**: विष्णुदत्तैश्ध नैवेद्यैर्यस्थ लम्बोदर॑ पुरा । पित्रा दत्तैक्ष विविधैर्वन्दे लम्बोदरं च तम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.17705)
- **Original**: शूर्पकारा च॒ यत्कर्णा£. विध्नवारणकारणौ । सम्पदौ ज्ञानकूपौ च॒ शूर्पकर्ण॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.17706)
- **Original**: विष्णुप्रसादपुष्प॑ च यन्यूर्श्ि मुनिदत्तकम्‌ । तद़जेन्द्रवक्त्रयुक्ते गजबक्त्र॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.17707)
- **Original**: गुहस्याग्रे च॒ जातोउयपाविर्भूतोी हरालये
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.17708)
- **Original**: बन्दे गुहाग्रज॑ देव॑ सर्वदेवाग्रपूजितम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.17709)
- **Original**: एतन्नामाष्टक॑ दुर्ग नामभि: संयुतं परम्‌ । पुत्रस्य पश्य बेदे क्र तदा कोप॑ तथा कुरु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.17710)
- **Original**: एतन्नामाष्टक॑ स्तोत्र नानार्थसंयुतं॑ शुभम्‌ । त्िसंध्यं यः पठेन्नित्यं स सुखी सर्वतो जयी।
- **Translation**: 

---

