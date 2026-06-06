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

### Verse 1 (Vishnu Puran 0.9001)
- **Original**: 3 ततो ग्रहगणस्सम्यक्श्नचचार दिवि द्विज
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9002)
- **Original**: विष्णोरंशे भुवं याते ऋतवश्चाबभुद्शुभा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9003)
- **Original**: डे न सेहे देवकीं द्रएं कश्चिदष्यतितेजसा । जाज्वल्यमानां तां दृष्ठा मनांसि क्षो भमाययु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9004)
- **Original**: 5 अदृष्टा: पुरुषैस्ल्लीभि्देवकी देवतागणा:। थिश्राणां वपुषा विष्णु तुष्ठवतुस्तामहर्निशम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9005)
- **Original**: 6 देवता ऊचुः प्रकृतिस्त्ये परा सूक्ष्मा ब्रह्मगर्भाभव: पुरा । ततो बाणी जगद्धातुर्वेदगर्भास शोभने
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9006)
- **Original**: 7 सुज्यस्वरूपगर्भास सृष्टिभूता सनातने। बीजभूता तु सर्वस्य यज्ञभूताभवख्रयी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9007)
- **Original**: 8 फलगर्भा ल्वपेवेज्या वद्धिगर्भा तथारणि: । अदितिदेवगर्भा त्वे दैत्यगर्भा तथा दिति:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9008)
- **Original**: 9 ज्योत्ता वासरगर्भा लव ज्ञानगर्भासि सन्नति: । नयगर्भा परा नीतिर्लजा त्वं प्रश्रयोद्ृहा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9009)
- **Original**: 10 कामगर्भा तथेच्छा लव तुष्टि: सन्‍्तोषगर्भिणी । म्रेध्वा च बोधगर्भासि श्ैर्यगर्भोद्रहा धृति:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9010)
- **Original**: 11 ग्रहर्क्षारकागर्भा ौरस्थाखिलहैतुकी । एता विभूतयो देवि तथान्याश्र सहस्नरहः । तथासंख्या जगद्धात्रि.साम्प्रते जठरे तब
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9011)
- **Original**: 12 भी ठरौ दिन यशोदाके गर्भमें स्थित हुई
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9012)
- **Original**: हे द्विज ! विष्णु-अंडाके पृथिवीमें पधारनेपर आकागर्में ग्रहगण व्यैक-ठीक गतिसे चलने लगे और ऋतृगण भी मड़लऊूमय डोकर शोभा पाने छरों
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9013)
- **Original**: उस समय अत्यन्त तेजसे देदीप्यमाना देबक्रीजीको कतई भी देख न सकता था । उन्हें देखकर [ दर्शाकॉंके ] चित्त थकित हो जाते थे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9014)
- **Original**: तब्र देंखतागण अन्य पुरुष तथा स्रियोंक्त्रें दिखायी न देते हुए, अपने दारीरमें [ गर्भरूपसे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9015)
- **Original**: भगतान्‌ तिष्णुको धारण करनेवाली देवकीजीकी अहर्निश् स्तुति करने लगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9016)
- **Original**: देखता बोले--हे शोभने ! तू पहले ब्रह्म- प्रतिबिम्बधारिणी पूलप्रकृति हुई थी और फिर जगद्विधाताकी वेदगर्भा वाणी हुई
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9017)
- **Original**: है सनातने ! तू ही सृज्य पदार्थोक्ो उत्पन्न करनेबात्जी और तू ही सृष्टिरूपा है; तू ही सबकी बीज-स्वरूपा यज्ञमयी येदत्रयी हुई है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9018)
- **Original**: तू ही फलमयी यज्ञक्रिया और अप्रिमयी अरणि है तथा तू ही देवमाता अदिति और दैत्यप्रसू दिति है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9019)
- **Original**: तू ही दिनकरी प्रथा और ज्ञानगर्भा गुरुशुश्रूषा है तथा तू हो तव्यायमयी परमनीति और विनयसम्पत्ना लज्जा है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9020)
- **Original**: तू ही काममयी इच्छा, सन्तोषमयी तुष्टि, बोधगर्भा प्रज्ञा और चैर्यधारिणी धुति है
- **Translation**: 

---

