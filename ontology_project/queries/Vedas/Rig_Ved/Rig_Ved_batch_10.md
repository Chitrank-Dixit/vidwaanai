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

### Verse 1 (Rig Ved 0.181)
- **Original**: 8 । 79, एवा हि ते विभूतय ऊतय इन्द्र मावते। सद्यश्चित्‌ सन्ति दाशुधे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.182)
- **Original**: हे इन्द्रदेव ! हमारे लिये इष्टदाप्री और संरक्षण प्रदान करने वाली जो आपकी विभूतियाँ हैं, वे सभी दान देने (श्रेष्ठ कार्य में नियोजन करने) वालों को भी तत्काल प्राप्त होती हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.183)
- **Original**: 10 ऋतेद संहिता भाग-9 80, एवा ह्वस्य काप्या स्तोम उक्थं च शंस्यथा। इन्द्राय सोमपीतये
- **Translation**: 

---

### Verse 4 (Rig Ved 0.184)
- **Original**: दाता की स्तुतियाँ और उक्थ वचन अति मनोरम एवं प्रशंसनीय हैं । ये सब सोमपान करने वाले इन्द्रदेव के लिये हैं
- **Translation**: 

---

### Verse 5 (Rig Ved 0.185)
- **Original**: [ सूक्त - 9 ] [ऋषि - मधुच्छन्दा वैश्वामित्र । देवता-इन्द्र । छन्द- गायत्री
- **Translation**: 

---

### Verse 6 (Rig Ved 0.186)
- **Original**: ] 81. इन्द्रेहि मत्स्यन्धसो विश्वेभि: सोमपर्वाभि:। महाँ अभिष्टिरोजसा
- **Translation**: 

---

### Verse 7 (Rig Ved 0.187)
- **Original**: हे इद्धदेव ! सोमरूपी अन्नों से आप प्रफुल्लित होते हैं, अतः अपनी शक्ति से दुर्दान्त शत्रुओं पर विजय श्री वरण करने की क्षमता प्राप्त करने हेतु आप ( यज्जञशाला में ) पधारें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.188)
- **Original**: 82. एमेन॑ सृजता सुते मन्दिमिन्द्राय मन्दिने। चक्रि विश्वानि चक्रये
- **Translation**: 

---

### Verse 9 (Rig Ved 0.189)
- **Original**: (हे याजको !) प्रसन्‍नता देने वाले सोमरस को (निचोड़कर) तैयार करो तथा सम्पूर्ण कार्यों के कर्त्ता इन्द्र देव के लिये सामर्थ्य बढ़ाने वाले इस सोम को अर्पित करों
- **Translation**: 

---

### Verse 10 (Rig Ved 0.190)
- **Original**: 83. मत्स्वा सुशिप्र मन्दिभि: स्तोमेभिर्विश्चचर्षणे । सचैधु सवनेष्वा
- **Translation**: 

---

### Verse 11 (Rig Ved 0.191)
- **Original**: हे उत्तम शश्नों से सुसज्जित ( अथवा शोभन नासिका वाले ), सर्वद्रष्टा इन्द्रदेव ! हमारे इन यज्ञों में आकर प्रफुल्लता प्रदान करने वाले स्तोत्रों से आप आनन्दित हों
- **Translation**: 

---

### Verse 12 (Rig Ved 0.192)
- **Original**: 84. असृग्रमिन्द्र ते गिर: प्रति त्वामुदहहासत। अजोषा वृषभं पतिम्‌
- **Translation**: 

---

### Verse 13 (Rig Ved 0.193)
- **Original**: हे इन्द्रदेव ! आपकी स्तुति के लिये हमने स्तोत्रों की रचना की है । हे चलशाली और पालनकर्त्ता इन्द्रदेव ! इन स्तुतियों द्वारा की गईं प्रार्थना को आप स्वीकार करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.194)
- **Original**: 85. सं चोदय चित्रमर्वाग्राध इन्द्र वरेण्यम्‌। असदित्ते विभु प्रभु
- **Translation**: 

---

### Verse 15 (Rig Ved 0.195)
- **Original**: हे इन्द्रदेव ! आप ही विपुल ऐश्वर्यों के अधिपति हैं, अतः विविथ प्रकार के श्रेष्ठ ऐश्वर्यों को हमारे पास प्रेरित करें; अर्थात्‌ हमें श्रेष्ठ ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.196)
- **Original**: 86. अस्मान्त्सु तत्र चोदयेन्द्र राये रभस्वत:
- **Translation**: 

---

### Verse 17 (Rig Ved 0.197)
- **Original**: तुविद्युम्न यशस्व॒तः
- **Translation**: 

---

### Verse 18 (Rig Ved 0.198)
- **Original**: हे प्रभूत ऐश्वर्य सम्पन्न इन्द्रदेव ! आप वैभव की प्राप्ति के लिये हमें श्रेष्ठ कर्मों में प्रेरित करें, जिससे हम परिश्रमी और यशस्वी हो सकें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.199)
- **Original**: £7. सं गोमदिन्द्र वाजवदस्मे पृथु श्रवो बृहत्‌ । विश्वायुर्धेड्ाक्षितम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.200)
- **Original**: हे इद्धदेव ! आप हमें गौओं, धन-धान्यों से युक्त अपार वैभव एवं अक्षय पूर्णायु प्रदान करें
- **Translation**: 

---

