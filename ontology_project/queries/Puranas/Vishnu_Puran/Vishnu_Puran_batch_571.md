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

### Verse 1 (Vishnu Puran 0.11401)
- **Original**: आपने जो अभय दिया है वह सब मैंने भी दे दिया। हे श्भूर ! आप अपनेको मुझसे सर्वथा अभिन्न देखें
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11402)
- **Original**: आप यह भल्ल प्रकार समझ लें कि जो मैं हूँ सो आप हैं तथा यह सम्पूर्ण जगत्‌, देव, असुर और मनुष्य आदि कोई भी मुझसे भिन्न नहीं हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11403)
- **Original**: है हर ! जिन लोगोंका चित्त अविद्यासे मोहित है वे भिन्नदर्शी पुरुष ही हम दोनोंमें भेद देखते और बतल्मते हैं। हे जृषभध्वज ! मैं प्रसन्न हूँ, आप पधारिये, में भी अब जाऊँगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11404)
- **Original**: श्रीपराशस्जी खोले--इस प्रकार कहकर भगवान कृष्ण जहाँ प्रगयुम्नकुमार अनिरुद्ध थे वहाँ गये। उनके पहुँचते ही अनिरुद्धके बन्धनरूप समस्त नागगण गरुडके बेगसे उत्पन्न हुए वायुके प्रहास्से नष्ट हो गये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11405)
- **Original**: तदनन्तर सपत्रीक अनिरुद्धकों गर्डपर चढ़ाकर बलराम, प्रचुप्न और कृष्णचन्द्र द्वारकापुरमें वजैट आये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11406)
- **Original**: हे विप्र ! वहाँ भू-भार-हरणकी इच्छासे रहते हुए श्रीजनार्दन अपने पुत्र-पौत्रादिसे घिरे रहकर अपनी रानियोंके साथ रमण करने लगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11407)
- **Original**: _-++ है. _>_-_>_>____» इति श्रीविष्णुपुराणे पद्षमेंडशे त्रयख्त्िशोउध्याय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11408)
- **Original**: डेण्रे श्रीविष्णुप्‌राण [ आू 34 चौंतीसवाँ अध्याय पौण्डुक-वध् तथा काशीदहन श्रीमत्रेय उवाच श्रीमैज्ेयजी बोले--हे गुरो! श्रीविष्णुभगवानते चक्रे कर्म महच्छौरिबिंभ्राणो मानुषषी तनुम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11409)
- **Original**: मनुष्य-शरीर घारणकर जो लीलासे ही इन्द्र, शद्भूर और जिगाय शक्रं शर्व च सर्वान्दिवांश्व लीलया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11410)
- **Original**: 1 यथान्यदकरोत्कर्म दिव्यच्रेष्टाविघातकृत्‌ । तत्कथ्यतां महाभाग पर॑ कौतूहलं हि में
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11411)
- **Original**: 2 श्रीपरात्ार उताच गदतो मम्त विप्रषें श्रूयतामिदमादरात्‌ । नरावतारे कृष्णेन दग्धा वाराणसी यथा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11412)
- **Original**: 3 पौण्डको वासुदेबस्तु वासुदेबो3भवद्भुवि। अवतीर्णस्त्वमित्युक्तो जनैरज्ञानमोहिते:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11413)
- **Original**: 4 स॒मेने वासुदेवो<हमवतीणों महीतले। नष्टस्मृतिस्ततस्सर्व॑ विष्णुचिनह्ममचीकरत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11414)
- **Original**: 5 दूत चर प्रेषयामास कृष्णाय सुमहात्मने । त्यक्त्वा चक्रादिकं चिह्न मदीयं नाम चात्मन:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11415)
- **Original**: 6 वासुदेवात्मक॑ मूढ त्यक्त्वा सर्वमशेषत: । आत्मनो जीवितार्थाय ततो मे प्रणति ब्रज
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11416)
- **Original**: 7 डत्युक्तस्सम्प्हस्थैन॑ दूत॑ प्राह जनार्दनः । निजचिह्ममहं चक्र समुत्स्रक्ष्ये तव्यीति वै
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11417)
- **Original**: 8 वाच्यश्न पोण्डूको गत्वा त्वया दूत वचो मम । ज्ञातस्त्वद्वाक्यसद्धावो यत्कार्य॑ तद्दिधीयताप्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11418)
- **Original**: 9 गृहीतचिह्नवेषो5हमागमिष्यामि ते पुरम्‌। उत्स्रक्ष्यामि च तधके निजचिहपसंशयम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11419)
- **Original**: 10 अज्ञापूर्व " यदिदमागच्छेति त्वयोदितम्‌। सम्पादयिष्ये श्रस्तुभ्य॑ समागम्याविछम्बितम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11420)
- **Original**: 11 झरणं ते समभ्येत्य कर्तास्मि नृपते तथा। यथा लत्तो भयं भूयो न मे किश्निद्धविष्यति
- **Translation**: 

---

