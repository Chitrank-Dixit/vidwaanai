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

### Verse 1 (Vishnu Puran 0.6861)
- **Original**: दिलीपस्य भगीरथ: योउसो गड्डां स्वर्गादिहानीय भागीरथीसंज़ां चकार
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6862)
- **Original**: भगीर थात्सुह्ेत्रस्मुहोत्राच्छत: ,तस्यापि नाभाग: ततो>्म्बरीष: , तत्पुत्रस्सिन्धुद्वीप: सिन्धुद्दीपा- दयुतायु:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6863)
- **Original**: तत्पुत्रश्च ऋतुपर्ण:, योउसौ नलसहायो5क्षहददयज्ञो3भूत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6864)
- **Original**: ऋतुपर्णपुत्रस्सर्वकाम:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6865)
- **Original**: . तत्तनय- स्सुदास:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6866)
- **Original**: _ सुदासात्सौदासो. मिन्न- सहनामा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6867)
- **Original**: स चाटव्यां मृगयार्थी पर्यटन्‌ व्याप्रद्ययमपश्यत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6868)
- **Original**: ताभ्यां तदनमपमृर्गं कृत मत्वैंके तयोर्बाणेन जघान
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6869)
- **Original**: प्रियमाणश्वासावतिभीषणाकृतिरतिकराल्वदनो राक्षसो5भूत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6870)
- **Original**: द्वितीयो5पि प्रतिक्रियां ते करिष्यामीत्युक्त्वान्तर्धानं जगाम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6871)
- **Original**: । डंडे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6872)
- **Original**: कालेन गच्छता सौदासो यज्ञमयजत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6873)
- **Original**: परिनिष्ठितयज्ञे आचार्य वसिष्टे निष्क्रान्ते तद्रक्षो बसिष्टरूपमास्थाय यज्ञावसाने मम नरमांसभोजन देयमिति तस्संस्क्रितां क्षणादागमिष्यापी- स्युक्ता निष्क्रान्त:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6874)
- **Original**: भृूयश्व सूदवेषं कृत्वा राजाज्ञया मानुषं मांस॑ संस्कृत्य राज्ञे न्‍्यवेदयत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6875)
- **Original**: असावपि हिरण्यपात्रे मांसमादाव वसिष्ठागमनप्रतीक्षाको5भवत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6876)
- **Original**: आगताय बसिष्टाय निवेदितवान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6877)
- **Original**: स॒चाप्यचिन्तयदहो अस्य राज्ञो दोइशील्यं येनैतन्मांसमस्माक॑ प्रयक्कति. किमेतवृद्रव्य- जातपिति ध्यानपरोईडभवत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6878)
- **Original**: अपद्यध् तन्मांस मानुषम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6879)
- **Original**: अतः क्रोधकलुषी- कृतचेता राजनि झापसपुत्ससर्ज
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6880)
- **Original**: यस्मादभोज्यमेतदस्मद्विधानां.._ तपस्विनामव- गछ्छन्नपि भवान्यह्यं ददाति तस्मात्तवैवात्र लोलुपता भविष्यतीति
- **Translation**: 

---

