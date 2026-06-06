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

### Verse 1 (Vishnu Puran 0.7621)
- **Original**: तस्य स॒ विदर्भ इति पिता नाम चक्रे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7622)
- **Original**: स च तां स्वुषामुप्येमे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7623)
- **Original**: तस्यां चासौं पुत्रा- वजनयत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7624)
- **Original**: पुनश्च तृतीय रोमपादसंज्ञ पुत्रमजीजनद्यो नारदादवाप्तज्ञानवानभवत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7625)
- **Original**: रोमपादाइधुर्ब्रोर्धृतिर्थृते कैशिकस्यापि चेदि: पुत्रो5भवदयस्य सन्ततो चैद्या भूपाला:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7626)
- **Original**: क्रथस्य स्ुषापुत्रस्य कुन्तिरभवत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7627)
- **Original**: कुन्तेर्धष्टिर्प्टेनिधृतिर्निधृतेर्दशाईस्ततश्ल व्योमा तस्थापि जीमूतस्ततश्च विकृतिस्ततश्च भीमरथ:, तस्मात्रवरथस्तस्थापि दह्मारथस्ततश्च॒ शकुनिः, तत्तनयः करम्भिः करभम्भेदेंबरातो$भवत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7628)
- **Original**: तस्माददेवक्षत्रस्तस्यापि मधुर्मधो: कुमारवंद्ाः पृथिवीपतिरभवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7629)
- **Original**: ततश्चांशुस्तस्माश सत्वत:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7630)
- **Original**: सत्वतादेते सात्वता:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7631)
- **Original**: इत्येतां जयामघस्य सन्तर्ति सम्बक्‍्छुद्धासमन्वित: श्र॒ुत्वा पुमान्‌ मैत्रेय स्वपापै: प्रमुच्यते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7632)
- **Original**: । श्रीविष्णुपुराण [ अ* 13 रहनेपर भी थोड़े ही दिनोंमें शौव्याके गर्भ रह गया और यथासमय एक पुत्र उत्पन्न हुआ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7633)
- **Original**: पिताने उसका नाम विदर्भ रखा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7634)
- **Original**: और उसीके साथ उस पृत्रवधूका पाणिप्रहण हुआ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7635)
- **Original**: उससे बिदर्भने क्रथ और कैशिक नामक दो पुत्र उत्पन्न किये ।। 37
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7636)
- **Original**: फिर रोमपाद नामक एक तीसरे पुत्र॒क्ो जन्म दिया जो नारदजीके उपदेदसे ज्ञान- विज्ञान सम्पन्न हो गया था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7637)
- **Original**: रोमपादके वभु, बभुके धृति, धृतिके कैज्लिक और कैडशिकके चेदि नामक पूत्र हुआ जिसकी सन्ततिमें चैच्च राजाओंने जन्म लिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7638)
- **Original**: ज्यामबकी पूत्रवधूके पुत्र क्रथके कुन्ति नामक पुत्र हुआ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7639)
- **Original**: कुन्तिके धृष्टि, धृष्टिके निधृति, निधृतिके दज्माई, दरा्के व्योमा, व्योमाके जीमूत, जीमूतके निकृति, विकृतिके भीमरथ, भीमरथके नवरथ, नवरथके दशरथ, दशरथके शकुनि, शकुनिके करम्भि, करम्भिके देवरात, देव णतके देवक्षप्र, देवक्षत्रके मधु, मधुके कुमारवंश, कुमार- वंद्ञके अनु, अनुके राजा पुरुमित्र, पुरुमित्रके अंश्ु और अँशुके सत्वत नामक पुत्र हुआ तथा सलतसे सात्कतवंशका प्रादर्भाव हुआ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7640)
- **Original**: 41--44
- **Translation**: 

---

