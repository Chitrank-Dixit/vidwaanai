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

### Verse 1 (Rig Ved 0.8141)
- **Original**: हे वायु देवता ! आप श्रेष्ठ अक्षों वाले हैं और इन्द्रदेव आपके सारथि हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8142)
- **Original**: आप कामनाओं को पूर्ण करने के लिए सैकड़ों अश्धों द्वारा हमारे समीप पधारें । आप तथा इद्धदेव अभिपुत सोमरस का पान करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8143)
- **Original**: 3544. आ वां सहस्नं हरय इन्द्रवायू अभि प्रयः
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8144)
- **Original**: बहन्तु सोमपीतये
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8145)
- **Original**: हे इन्द्र और वायुदेवो ! आप दोनों को हजारों संख्या वाले घोड़े द्रतगति से सोम पान के लिए ले आएँ
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8146)
- **Original**: 3545, रथं हिरण्यवन्धुरमिन्द्रवायू स्वध्वरम्‌। आ हि स्थाथो दिविस्पृशम्‌
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8147)
- **Original**: हे इन्द्र और वायुदेवों ! आप दोनों सोने से जड़े हुए, यज्ञ को भली-प्रकार सिद्ध करने वाले तथा अंतरिक्ष को स्पर्श करने वाले रथ पर आकर आसीन होते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8148)
- **Original**: 3546, रथेन पृथुपाजसा दाश्वांसमुप गच्छतम्‌ । इन्द्रवायू इहा गतम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8149)
- **Original**: हे इन्द्र और वायुदेवो ! आप दोनों अत्यधिक सामर्थ्यशालो रथ के द्वारा हविप्रदाता यंजमान के निकट गमन करें तथा इस यज्ञ मण्डप में पथारें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8150)
- **Original**: 3547, इन्द्रबायू अय॑ सुतस्त देवेभि: सजोषसा
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8151)
- **Original**: पिबत॑ दाशुषो गृहे
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8152)
- **Original**: हे इन्द्र और वायुदेवो ! यह सोमरस आपके लिए अभिषुत किया गया है । देवताओं के साथ समान रूप से स्नेह करने वाले होकर आप दोनो हविप्रदाता यजमान के यज्ञ मण्डप में उसका पान करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8153)
- **Original**: 3548. इह प्रयाणमस्तु बामिन्द्रवायू विभोचनम्‌। इह वां सोमपीतये
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8154)
- **Original**: हे इन्र और वायुदेवो ! आप दोनों का इस यज्ञ में पदार्पण हो । यहाँ पधार कर सोमपान के निमित्त आप दोनों अपने अश्वों को मुक्त करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8155)
- **Original**: [ सूक्त - 47 ] [ऋषि - वामदेव गौतप । देवता - इन्द्रयायु; 1 वायु
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8156)
- **Original**: छन्द - अन॒ष्टप
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8157)
- **Original**: 3549. वायो शुक्रो अयामि ते मध्वो अग्र॑ दिविष्टिषु । आ याहि सोमपीतये स्पाहों देव नियुत्वता
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8158)
- **Original**: है वायो ! निर्दोष हम, आपके लिए यज्ञ में सर्वप्रथम सोगरस भेंट करते हैं । है टेव
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8159)
- **Original**: आदर के योग्य आप नियुत (नामक) अश्व पर बैठ कर सोमपान के निमित्त पधारें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8160)
- **Original**: 3550. इन्द्रश्च वायवेषां सोमानां पीतिमर्हथः । युवां हि यन्तीन्दवो निम्नमापों न सक्ष्यक्‌
- **Translation**: 

---

