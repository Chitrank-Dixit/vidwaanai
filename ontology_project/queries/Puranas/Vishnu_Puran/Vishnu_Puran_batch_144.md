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

### Verse 1 (Vishnu Puran 0.2861)
- **Original**: उस ब्रह्मके मूर्त और अमूर्त दो रूप हैं, जो क्षर और अश्षररूपसे समस्त प्राणियोमें स्थित हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2862)
- **Original**: अक्षर ही वह पर्रह्म है और श्वर सम्पूर्ण जगत्‌ है। जिस प्रकार एकदेशोय अग्निका प्रकाश सर्वत्र फैला रहता है उसी अ्रकार यह सम्पूर्ण जगत्‌ परब्रह्मकी ही शक्ति है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2863)
- **Original**: है मैत्रेय ! अग्नरिकी निकटता और ताक ओेदसे जिस प्रकार उसके प्रकाशमें भों अधिकता और न्यूनताका भेद रहता है उसी प्रकार बह्मकी दाक्तिमें भी तारतम्य है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2864)
- **Original**: ब्रह्मा, विष्णु और शिव अरह्मकी प्रधान चक्तियाँ हैं, उनसे न्‍्यून देवगण हैं तथा उनके अनन्तर दक्ष आदि प्रजापतिगण हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2865)
- **Original**: उनसे भी न्यून मनुष्य, पशु, पक्षी, मृग और सरीसूपादि हैं तथा उनसे भी अत्यन्त न्यून वृक्ष, गुल्म और लता आदि हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2866)
- **Original**: आविर्भावतिरोभावजन्मनाशविकल्पवत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2867)
- **Original**: अतः है मुनितर ! आविर्भाव (उत्पन्न होना) तियोभाव # ग्राणायामादि साधनविषयक जानको 'साधनाल्ूम्यन-ज्ञान' कहते हैं।
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2868)
- **Original**: आ 22 ] प्रथम अंदा 103 सर्वशक्तिमयो विष्णु: स्वरूप ब्रह्मण: परम्‌ । मूर्त यद्योगिभिः पूर्व योगारम्भेषु चिन्त्यते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2869)
- **Original**: सालम्बनो महायोगः सबीजो यत्र संस्थित: । मनस्यव्याहते सम्यग्युक्रतां जायते मुने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2870)
- **Original**: 62 स परः परशक्तीनां ब्रह्मण: समनन्‍्तरम्‌। मूर्ते ब्रह्म महाभाग सर्वेत्रह्ममयों हरिः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2871)
- **Original**: 63 तत्र सर्वमिद॑ प्रोतमोत॑ चैबाखिलं जगत्‌। ततो जगज्जगत्तर्मन्स जगश्चाखिल मुने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2872)
- **Original**: 64 क्षराक्षमयों विष्णुर्बिभर्त्यखिलमीश्चर: । डा ->ऋ भ्रूषणास्तरस्वरूपवत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2873)
- **Original**: 65 उपाय भूषणाख्रस्वरूपस्थ॑ यपज्चैतदखिलं जगत्‌। बिभर््ति भगवान्विष्णुस्तन्‍्यपाख्यातुपहसि
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2874)
- **Original**: 66 श्रीपराजर ठवाच नमस्कृत्याप्रमेयाय विष्णवे प्रभविष्णवे । कथयापि यथाख्यात॑ वसिष्ठेन ममाभवत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2875)
- **Original**: 67 आल्मानमस्य जगतो निर्लेपमगुणामलम। विभर््ति कौस्तुभमणिस्वरूप भगबान्हरिः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2876)
- **Original**: 68 अवत्ससंस्थानधरमनन्तेन. समाश्रितम्‌ । प्रधान बुद्धिरप्यास्ते गदारूपेण माघवे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2877)
- **Original**: 869 भूतादिमिन्द्रियादि च॒ ट्विधाहड्डारमीश्चरः । बिभर्त्ति शल्लरूपेण झारडरूपेण च स्थितम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2878)
- **Original**: 70 चलत्स्वरूपमत्यत्त॑ जवेनान्तरितानिलम्‌ । चक्रस्वरूपं च मनो घत्ते विष्णुकरे स्थितम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2879)
- **Original**: 71 पम्चरूपा तु या माला वैजयन्ती गदाभृतः । सा भूतहेतुसड्ञाता भूतमाला च॒ वे ट्विज
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2880)
- **Original**: 72 यानीद्धियाण्यशेषाणि बुद्धिकर्मात्मकानि वै। शररूपाण्यशेषाणि तानि धत्ते जनार्दन:
- **Translation**: 

---

