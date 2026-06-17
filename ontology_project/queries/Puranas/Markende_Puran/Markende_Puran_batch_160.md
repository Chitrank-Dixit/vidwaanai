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

### Verse 1 (Markende Puran 0.3181)
- **Original**: कोपाध्मातों निशुम्भोष्ण झूल॑ जग्राह दानव: । आयात्त॑* भुष्टिपातेन देवी तच्चाप्यचूर्णयत्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3182)
- **Original**: आबिश्याथ गये सोडपि चिक्षेप चणिडकां प्रति। सापि दैथ्या प्रिशूलेन भिन्ना भस्मत्वमागता
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3183)
- **Original**: ततः परशुहस्त॑ तमाबान्तं दैत्मपुद्गायम्‌। आहत्व देवी ब्राणौधरपातयत भूतले
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3184)
- **Original**: तस्मिश्रिपतिते भूमौ निशुम्भे भीमबिक्रपे। भ्रातर्वतीव संक्रुद्धः प्रययो हन्तुपम्बिकाम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3185)
- **Original**: स रथस्थस्तथात्वुच्चेर्गृहीतपरमायुथै:
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3186)
- **Original**: भुजैरष्टाभिरतुलैव्यांप्याशेष॑ शभौ वभः
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3187)
- **Original**: 18 # तमायान्त॑ सप्तालोक्‍्य देवी शझद्भुमवादयत्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3188)
- **Original**: ज्याशर्ब्द ऋषि अनुषश्चकारातीव दु/सहम्‌
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3189)
- **Original**: 'पूरयामास ककुभो निजघण्टास्यनेन चा। समस्तदैत्यसैन्यानां. तेजोबधबिश्वायथिना
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3190)
- **Original**: ज़तः सिंहों महानादैसस्‍्त्याजितेभगहापदेः। पूस्यामास॒ गगने गा तथैलों दिज्ञों दश
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3191)
- **Original**: पा0- अशद्ाम। 4, पाः-त थोष॑दिशों।
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3192)
- **Original**: र्रड + संक्षिप्त भार्कण्डैयपुराण « 30150 + 39049 + +19194 1+1 का 71 6
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3193)
- **Original**: कर क9 19 + + का 74 6797 17197 6 # 71 7194 94 4 6+ # # का का का 14441 77 #144 7 #97
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3194)
- **Original**: #: #5 $ क+
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3195)
- **Original**: # क। 7 4 4 48 #: 4 + $
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3196)
- **Original**: के के के # 55% 55:65: 55 ततः काली समुत्यत्य गगन॑ छ्पाप्रताडबतू। कराभ्यां तन्निनादेन प्राक्स्वनास्ते तिरोहिता;
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3197)
- **Original**: अट्टाइहासमशितं शिबदूती चकार ह। तै: शब्दग्सुरास्त्रेसु: शुम्भ: कोप॑ पर यबौ
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3198)
- **Original**: दुरात्पेस्तिष्ठ तिष्ठेति व्याजहाराम्यिका बदा। तदा जयेत्यभिहिंत॑ देवैराकाशसंस्थिते:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3199)
- **Original**: शुम्भेतागत्य या शक्तिर्मक्ता ज्वालातिभीषणा। आयान्‍न्ती बल्लिकूटाभा सा निरस्ता महोल्कत्ा
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3200)
- **Original**: सिंहनादेन शुम्पस्य व्याप्त लोकत्रयान्तरम्‌। निर्घातनिःस्वनों घोरों जितवानवनीपते
- **Translation**: 

---

