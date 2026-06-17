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

### Verse 1 (Vishnu Puran 0.3801)
- **Original**: 82 सुधामा शह्बुपाशैव कर्दमस्यात्मजो द्विज
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3802)
- **Original**: हिरण्यरोमा चैवान्यश्षतुर्थ: केतुमानपि
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3803)
- **Original**: 83 निईन्द्रा निरभिमाना निस्तन्द्रा निष्परिग्रहाः । लोकपाला: स्थिता होते लोकालोके चतुर्दिशम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3804)
- **Original**: 84 उत्तर॑ यदगस्त्यस्थ अजबीध्याश्व दक्षिणम्‌। पितृयान: स वे पन्धा वैश्वानरपथाइहिः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3805)
- **Original**: 85 तन्नासते महात्मान ऋषयो ये5प्रिहोन्रिण: । भूतारण्मकृत॑ ब्रह्म शंसन्तो ऋत्विगुद्यता: । प्रारभन्ते तु ये ललोकास्तेषां पन्‍था: स दक्षिण:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3806)
- **Original**: 86 चलितं ते पुनर्ब्रहा स्थापयन्ति युगे युगे। सन्तत्या तपसा चैब मर्यादाभि: श्रुतेन च
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3807)
- **Original**: 87 जायमानास्तु पूर्वे च पश्चिमानां गृहेषु वे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3808)
- **Original**: पश्चिमाओ्ैव पूर्वेधां जायन्ते निधनेष्रिह
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3809)
- **Original**: 88 एबमावर्तमानास्ते तिष्ठन्ति नियतव्रता: । सबितुर्दक्षिणं मार्ग श्रिता ह्वाचन्रतारकम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3810)
- **Original**: 89 नागवीध्युत्तरं यश्व सप्तर्षिभ्यक्ष दक्षिणम्‌। उत्तर: सवितु: पन्धा देवयानश्ष स स्मृत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3811)
- **Original**: 90 तम्न ते वशिन: सिद्धा विमला ब्रह्मचारिण: । सन्‍्तर्ति ते जुगुप्सन्ति तस्मान्मृत्युजितश्न तैः । 99 अष्टछाशीतिसहल्लाणि पुनीनापूथध्बरेतसाम्‌ । उदक्पन्धानमर्यम्णा: स्थितान्याभूतसम्म्रबम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3812)
- **Original**: 92 तेउसम्प्रयोगाल्लो भस्य मैथुनस्य च वर्जनात्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3813)
- **Original**: इच्छाद्देषाप्रवृत्या च भूतारम्भविवर्जनात्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3814)
- **Original**: 93 भ्॒ कामासंयोगाच्छब्दादेदोषिदर्शनात्‌ । इत्यि: कारणै: शुद्धास्तेउमृतत्वं हि भेजिरे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3815)
- **Original**: 94 आभूतसम्वं॑ स्थानममृतत्य॑ विभाव्यते । औैलोक्यस्थितिकाछो5यमपुनर्मार उच्यते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3816)
- **Original**: 95 ब्रह्महत्याश्वमेधाभ्यां पापपुण्यकृतो विधि: । आधूतसम्प्रवान्तन्तु फल्ममुक्त तयोदिज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3817)
- **Original**: 96 ब्ितीय अंझ 135 मैंने पहले तुमसे जिस लोकाल्शेकपर्वतका वर्णन किया है, उसीपर चार ब्रतशील लोकपाल निवास करते हैं। 82
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3818)
- **Original**: हे द्विज ! सुधामा, कर्दमके पूत्र शखपाद और हिरज्यरोमा तथा केतुमानू--ये चारों निईन्ड, निरभिमान, निरालस्य और निष्परिप्रह ल्लरोेकपाकगण लोकालोक- पर्वतकी चारों दिज्ञाओंमें स्थित हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3819)
- **Original**: जो अगस्यथके उत्तर तथा अजवीधिके दक्षिणमें वैश्वानरमार्गसे भिन्न [ मृगवीधि नामक ] मार्ग है बही पितृयानपथ हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3820)
- **Original**: उस पिह्यानमार्गमें महात्मा- मुनिजन रहते हैं। जो स्मेग अग्निहोत्री होकर प्राणियोंकी उत्पत्तिके आरम्भक ब्रह्म (बेद) की स्तुति करते हुए यज्ञनुष्ठानके लिये उद्यत हो कर्मका आरम्भ करते हैं वह (पितृयान) उनका दक्षिणमार्ग है
- **Translation**: 

---

