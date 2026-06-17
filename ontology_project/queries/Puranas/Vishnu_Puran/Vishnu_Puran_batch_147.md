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

### Verse 1 (Vishnu Puran 0.2921)
- **Original**: निराकार और सर्वेध्वर श्रीअनन्त ही भृतस्वरूप होकर देख, मनुष्य और पञ्ञु आदि नानारूपोंसे घ्थित है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2922)
- **Original**: ऋक्‌, यजु, साम और अथर्बनेद, इतिहास (महाभारतादि), उपवेद (आमुर्वेदादि), वेदान्तवाक्य, समस्त केदांग, मनु आदि कथित समस्त धर्मशास्तर, पुणणादि सकल शास्त्र, आख्यान, अनुवाक (कल्पसूत्र) तथा समस्त काव्य-चर्चा और रागरागिनी आदि जो कुछ भी हैं वे सब शब्दमूर्तिधारी परमात्मा विष्णुका ही शरीर हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2923)
- **Original**: 83--85
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2924)
- **Original**: इस ल्णेकमें अथवा कहीं और भी जितने मूर्त, अपूर्त पदार्थ हैं, वे सब उ्हींका शरोर है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2925)
- **Original**: “मैं तथा यह सम्पूर्ण जगत्‌ जनार्दन श्रीहरिं ही हैं; उनसे भिन्न और कुछ भी कार्य-कारणादि नहीं है --- जिसके चित्तमें ऐसी भावना है उसे फिर देहजन्य राग- द्रेषादि द्रन्द्ररूप रोगकी प्राप्ति नहीं होती
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2926)
- **Original**: है ट्विज ! इस प्रकार तुमसे इस पुराणके पहले अंशका यथावत्‌ “वर्णन किया। इसका श्रवण करनेसे मनुष्य समस्त पापोंसे मुक्त हो जाता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2927)
- **Original**: हे मैत्रेय ! बारह वर्षतक कार्तिक मासमें पुष्कर क्षेत्रमें स्तन करनेसे जो फल होता है; वह सब्र मनुष्यको इसके श्रवणमात्रसे मिल जाता है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2928)
- **Original**: हे मुने ! देव, ऋषि, गन्धर्य, पितु और अभ्ष आदिकी उत्पत्तिका श्रवण करनेवाले पुरुषकों ले भवन्ति श्रृण्वत: पुंसो देवाद्या खरदा मुने
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2929)
- **Original**: देवादि वरदायक हो जाते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2930)
- **Original**: इति श्रीविष्णुपुराणे प्रथमें5शे द्वाविद्योडघ्याय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2931)
- **Original**: इति श्रीपराहरमुनिविरचिते श्रीविष्णुपरत्वनिर्णायके श्रीमति विष्णु- महापुराणे प्रथमोंडशः समाप्तः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2932)
- **Original**: #न्‍--जु _>अअक्‍-_-
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2933)
- **Original**: 35 श्रीमच्नारायणाय श्रीविष्णुपुराण 3... द्वितीय अंश जी गन पहला अध्याय प्रियव्तके बंदाका वर्णन श्रीमैत्रेय उनाच भगवन्सम्यगार्यात॑ मम्रैतदखिलें त्वया। जगत: सर्गसम्बन्धि यत्पृष्टोईसि गुरों मया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2934)
- **Original**: 91 योज्यपंशो जगत्सृष्टिसम्बन्धो गदितस्त्यया। तत्राह॑ ओतुमिच्छामि भूयो5पि मुनिसत्तम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2935)
- **Original**: 2 प्रियव्रतोत्तानपादौ सुतौ स्वायम्भुवस्य यौ। तयोरुत्तानपादस्य ध्रुवः पुत्रस्त्वयोदितः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2936)
- **Original**: 3 प्रियव्नतस्थ नैबोक्ता भवता द्विज सन्ततिः । तामहं आ्रोतुमिच्छामि प्रसन्नो वक्तुमहसि
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2937)
- **Original**: 4 औपयशर उवाच कर्दमस्पात्मजां कन्यामुप्येमे प्रियब्रतः । सम्राट कुक्षिश्ष तत्कन्ये दक्षपुत्रास्तथाउपरे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2938)
- **Original**: 5 महाप्रज्ञा महावीर्या विनीता दचिता पितु: । प्रियब्रतसुताः ख्यातास्तेषां नामानि मे श्रूणु
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2939)
- **Original**: 6 आम्मीध्रश्चाप्निबाहुअ॒वपुष्मान्युतिमांस्तथा ! मेधा मेघातिथिर्भव्य:ः सबनः पुत्र एब च
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2940)
- **Original**: 7 ज्योतिष्पान्दशमस्तेषां सत्यनामा सुतो5भवत्‌ ; फ्रियव्रतस्य पुत्रास्ते प्रख्याता बलबीर्यतः
- **Translation**: 

---

