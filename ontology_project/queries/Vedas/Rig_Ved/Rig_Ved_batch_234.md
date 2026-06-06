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

### Verse 1 (Rig Ved 0.4661)
- **Original**: है अग्निदिव ! आप हमारी इन समिधाओं तथा आहुतियों को स्वीकार करते हुए हमारे स्तोत्रों को भली-भाँति सुनें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.4662)
- **Original**: 10 ऋग्वेद संहिता भाग-9 2065, अया ते अग्ने विधेमोर्जों नपादश्वमिष्टे। एना सूक्तेन सुजात
- **Translation**: 

---

### Verse 3 (Rig Ved 0.4663)
- **Original**: हे शक्ति को क्षीण न करने वाले, द्रुतगामी, साधनों में गति प्रदान करने वाले, उत्तम ख्याति वाले अग्निदेव ! हमारो इस यज्ञ क्रिया तथा सूक्त से आप प्रसत्र हों
- **Translation**: 

---

### Verse 4 (Rig Ved 0.4664)
- **Original**: 2066. त॑ त्वा गीर्भिगिर्वणसं द्रविणस्युं द्रविणोद: । सपयेम सपर्यव:
- **Translation**: 

---

### Verse 5 (Rig Ved 0.4665)
- **Original**: हे ऐश्वर्यप्रदाता अग्निदेव ! आपकौ प्रतिष्ठा चाहने वाले हम आपके स्तुत्य तथा धन प्रदान करने वाले स्वरूप; की स्तुतियों के द्वारा पूजा करते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.4666)
- **Original**: 2067. स बोधि सूरिरमघवा वसुपते वसुदावन्‌। युयोध्य9स्मद्‌ द्वेघांसि
- **Translation**: 

---

### Verse 7 (Rig Ved 0.4667)
- **Original**: हे ऐश्वर्यप्रदाता धनाधिपति अग्निदेव
- **Translation**: 

---

### Verse 8 (Rig Ved 0.4668)
- **Original**: आप ऐश्वर्यवान्‌ तथा ज्ञानवान्‌ होकर हमारी कामनाओं को जानते हुए द्वेष करने वाले हमारे शत्रुओं को हमसे दूर करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.4669)
- **Original**: 2068. स नो वृष्टिं दिवस्परि स नो वाजमनर्वाणम्‌। स नः सहस्लिणीरिष:
- **Translation**: 

---

### Verse 10 (Rig Ved 0.4670)
- **Original**: अन्तरिक्ष से वे अग्निटेव हमारे लिए वृष्टि करें । वे हमें श्रेष्ण बल तथा हजारो प्रकार का अन्न प्रदान करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.4671)
- **Original**: 2069. ईव्ठानायावस्यबे यविष्ठ दूत नो गिरा। यजिष्ठ होतरा गहि
- **Translation**: 

---

### Verse 12 (Rig Ved 0.4672)
- **Original**: बलशाली तथा अत्यन्त प्रशंसा के योग्य, दुष्टों को पीड़ित करने वाले, होतारूप हे अग्निदेव ! आपके संरक्षण की कामना से स्तोत्र रूप वाणियों से हम आपका पूजन करते हैं। अत: आप हमारे पास आयें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.4673)
- **Original**: 2070. अन्तहईग्न ईयसे विद्वाउ्जन्मो भया कवे
- **Translation**: 

---

### Verse 14 (Rig Ved 0.4674)
- **Original**: दूतो जन्येव मित्र्य:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.4675)
- **Original**: है मेधावान्‌ अग्निदेव ! आप मनुष्यों के हृदयाकाश में विद्यमान रहकर उनके दोनों (वर्तमान तथा पिछले) जन्मों को आओ । आप मित्रतुल्य सभी के हितकारी हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.4676)
- **Original**: 2071. स विद्वां आ च पिप्रयो यक्षि चिकित्व आनुषक्‌। आ चास्मिन्सत्सि बर्हिषि
- **Translation**: 

---

### Verse 17 (Rig Ved 0.4677)
- **Original**: है अग्निदेव ! आप ज्ञानी हैं, अत: हमारी कामनाओं को पूर्ण कें। करें । आप चैतन्यतायुक्त हैं, अत: हमारे हविष्यात्र को यथा क्रम से देवताओं तक पहुँचा कर हमारे इस यज्ञ में हों
- **Translation**: 

---

### Verse 18 (Rig Ved 0.4678)
- **Original**: [ सूक्त -7 ] [ऋषि- सोमाहुति भार्गव
- **Translation**: 

---

### Verse 19 (Rig Ved 0.4679)
- **Original**: देवता- अग्नि
- **Translation**: 

---

### Verse 20 (Rig Ved 0.4680)
- **Original**: छन्द - गायत्री
- **Translation**: 

---

