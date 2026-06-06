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

### Verse 1 (Vishnu Puran 0.1681)
- **Original**: प्रबेता बोछे--हे तात ! जिस कर्मसे हम प्रजा- वृद्धिमें समर्थ हो सकें उसकी आप हमसे भल्ली प्रकार ख्याख्या कीजिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1682)
- **Original**: श्रीविष्णुपुराण ( अ* एड फतोवाच आराध्य बरदं बविष्णुमि्ठप्राप्तिमसंशयम्‌ समेति नान्यथा मर्त्य: किमन्यत्कथयामि व:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1683)
- **Original**: 14 तस्मात्मजाबिबृद्धयर्थ सर्वभूतप्रभुं हरिम्‌ । आराधयत गोविन्द यदि सिद्धिमभीप्सथ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1684)
- **Original**: 15 धर्ममर्थ च काम च मोक्ष चान्विच्छतां सदा । आराधनीयो... भगवाननादिपुरुषोश्म
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1685)
- **Original**: 16 यस्मिन्नाराधिते सर्ग चकारादौ प्रजापति: । तमाराध्याच्युतं वृद्धि; प्रजानां वो भविष्यति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1686)
- **Original**: 97 अ्रीपराशर उवाच इत्येबमुक्तास्ते पित्ना पुत्रा: प्रचेततो दश । मज्ना: पयोधिसलिले तपस्तेपु: समाहिता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1687)
- **Original**: 18 दह्वर्षसहस्लाणि न्यस्तचित्ता जगत्पतो। नारायणे मुनिश्रेष्ठ सर्वलोकपरायणे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1688)
- **Original**: 19 तम्रैवावस्थिता देवमेकाप्रमनसो हरिम्‌। तुष्ठवुर्यस्स्तुत: कामान्‌ स्तोतुरिष्टान्प्रयच्छति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1689)
- **Original**: 20 श्रीमैत्रेय उताच स्तवं प्रचेतसो जिध्णो: समुद्राग्भसि संस्थिता: । चक्कुस्तन्पे मुनिश्रेष्ठ सुपुण्यं वक्तुमहसि
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1690)
- **Original**: 21 श्रीपएान्चर उवाच प्रवेतस ऊचुः नताः सम सर्वक्‍चसां प्रतिष्ठा यत्र शाश्वती । तमाझन्तमशेषस्थ जगतः परम प्रभुम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1691)
- **Original**: 23 ज्योतिराष्यमनौपम्यमण्वनन्तमपारवत्‌ । योनिभूतमशेधस्थ स्थावरस्थ चरस्य च
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1692)
- **Original**: 24 अस्थाह: प्रथम रूपमरूपस्थ तथा निशा। सन्‍्ध्या च परमेशस्य तस्मै कालात्यने नमः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1693)
- **Original**: 25 भुज्यतेड्नुदिन देव: पितृभिश्ञ सुधात्मकः । जीवभूतः समस्तस्य तस्मै सोमात्यने नमः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1694)
- **Original**: 26 यस्तमांस्यत्ति तीव्रात्मा प्रभाभिर्भासयन्नभ: । धर्मशीताम्भसों योनिस्तस्मै सूर्यात्मने नमः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1695)
- **Original**: 27 पिताने कहा--वरदायक भगवान्‌ विष्णुकी आराधना करनेसे ही मनृष्यकों निःसन्देह इष्ट वस्तुकी प्राप्ति होती है और किसी उपायसे नहीं। इसके सित्रा और मैं तुमसे क्या कहूँ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1696)
- **Original**: इसलिये यदि तुम सफल्थ्ता चाहते हो तो प्रजा-बद्धिके लिये सर्वभूतोकि स्वामी श्रीहरि गोबिन्दकी उपासना करों
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1697)
- **Original**: धर्म, अर्थ, काम या मोक्षकी इच्छायाल्त्रेंकों सदा अनादि पुरुषोत्तम भगवान्‌ विष्णुकी ही आराधना करनी चाहिये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1698)
- **Original**: कल्पके आरम्भमें जिनकी उपासना करके प्रजापतिने संसारकी रचना की है, तुम उन अच्युतकी ही आराधना करो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1699)
- **Original**: इससे तुम्हारी सत्तानकी वृद्धि होगी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1700)
- **Original**: श्रीपराहरजी खोले--पिताकी ऐसी आजा होनेपर अ्रचेता नामक दसों पुत्रोनि समुद्रके जलमें डूबे रहकर स्ावधानतापूर्बक तप करना आरम्भ कर दिया
- **Translation**: 

---

