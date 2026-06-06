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

### Verse 1 (Rig Ved 0.8181)
- **Original**: ! आप अपने सैकड़ों संख्या वाले पोषण योग्य अश्वों को रथ में नियोजित करें । आपके हजारों अश्वों वाले रथ वेगपूर्वक पधारें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.8182)
- **Original**: [ सूक्त - 49 ] [ ऋषि « वाम्देव गौतम । देवता - इन्द्रावहस्पती । छन्द - गायत्री ।
- **Translation**: 

---

### Verse 3 (Rig Ved 0.8183)
- **Original**: 3558. इदे बामास्ये हविः प्रियमिन्द्रावृहस्पती
- **Translation**: 

---

### Verse 4 (Rig Ved 0.8184)
- **Original**: उक्थं मद शस्यते
- **Translation**: 

---

### Verse 5 (Rig Ved 0.8185)
- **Original**: मे डे सु0 50 5 हे इन्द्र और बृहस्पतिदेवो ! यह स्नेह युक्त आहुतियाँ हम आपके मुख (यज्ञाग्नि) में समर्पित करते हैं । आप दोनों को हम स्तोत्र तथा हर्षप्रदायक सोमरस प्रदान करते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.8186)
- **Original**: 3559, अयं वां परि षिच्यते सोम इन्द्रावहस्पती । चारुर्मदाय पीतये
- **Translation**: 

---

### Verse 7 (Rig Ved 0.8187)
- **Original**: हे इन्द्र और बृहस्पतिदेवो ! आपके हर्ष के लिए तथा सोमरस पान के लिए यह मनोहर सोमरस अभिषुत किया जाता है
- **Translation**: 

---

### Verse 8 (Rig Ved 0.8188)
- **Original**: 3560, आ न इन्द्राबृहस्पती गृहमिन्द्रक्ष गच्छतम्‌। सोमपा सोमपीतये
- **Translation**: 

---

### Verse 9 (Rig Ved 0.8189)
- **Original**: है सोमपान करने वाले इन्द्र तथा बृहस्पतिदेवो ! सोमरस पान के निमित आप तथा इन्द्रदेव हमारे घर में पथारें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.8190)
- **Original**: 3561. अस्मे इन्द्राबृहस्पती रयिं धत्त शतग्विनम्‌। अश्वावन्तं सहल्लिणम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.8191)
- **Original**: हे इन्द्र और बृहस्पतिदेवों ! आप हमें सैकड़ों गौओं तथा हजारों अश्वों से सम्पन्न ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.8192)
- **Original**: 3562. इन्द्राबृहस्पती बय॑ सुते गीर्भिहबामहे । अस्य सोमस्य पीतये
- **Translation**: 

---

### Verse 13 (Rig Ved 0.8193)
- **Original**: हे इन्द्र और वृहस्पतिटेवो ! सोमरस के निचोड़े जाने पर हम सोमरस के निमित्त प्रार्थनाओं द्वारा आपको आवाहित करते हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.8194)
- **Original**: 3563. सोममिन्द्राबृहस्पती पिवतं दाशुषों गृहे। मादयेथां तदोकसा
- **Translation**: 

---

### Verse 15 (Rig Ved 0.8195)
- **Original**: हे इन्ध और बृहस्पतिदेवो ! आप दोनों हवि प्रदाता यजमान के गृह में सोमपान करें तथा उसके गृह में वास करके हर्षित हों
- **Translation**: 

---

### Verse 16 (Rig Ved 0.8196)
- **Original**: [ सूक्त - 50 ]
- **Translation**: 

---

### Verse 17 (Rig Ved 0.8197)
- **Original**: ऋषि - वामदेव गौतम । देवता - बृहस्पति; 10-11 इद्धावृहस्पती । छन्द्‌ - व्रिष्रुप: 10 जगती
- **Translation**: 

---

### Verse 18 (Rig Ved 0.8198)
- **Original**: 3564 यस्तस्तम्भ सहसा वि ज्मो अन्तान्बृहस्पतिस्त्रिषधस्थो रवेण । त॑ प्रलास ऋषयो दीश्याना: पुरो विप्रा दथ्चिरे मन्द्रजिद्वम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.8199)
- **Original**: तीनों लोकों में निवास करने वाले जिन वृहस्पतिदेव ने धरती की दशों दिशाओं कौ स्तम्भित किया, उन मीठी बोली वाले बृहस्पतिदेव को पुरातन ऋषियों तथा तेजस्वो विद्वानों ने पुरोभाग में स्थापित किया
- **Translation**: 

---

### Verse 20 (Rig Ved 0.8200)
- **Original**: 3565, धुनेतय: सुप्रकेतं मदन्तो बृहस्पते अभि ये नस्ततस्रे । पृषन्तं सृप्रमदब्धमूरव॑ बृहस्पते रक्षतादस्य योनिम्‌
- **Translation**: 

---

