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

### Verse 1 (Rig Ved 0.11461)
- **Original**: सूर्योदय के समय जो साधक इन्द्र और अग्निदेवों की उपासना करते हैं, वे इन दोनों सामर्थ्यबान्‌ देवों की कृपा से शत्रु का नाश करके अन्न और धन प्राप्त करते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11462)
- **Original**: 4988. ता योधिष्टमभि गा इन्द्र नूनमपः स्वरुपसो अग्न ऊल्हहा:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11463)
- **Original**: दिशः स्वरुषस इन्द्र चित्रा अपो गा अग्ने युवसे नियुत्वान्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11464)
- **Original**: हे इन्द्र और अग्निदेवों ! आप गौओं, जल प्रवाह, प्रकाश एवं उषा को उठाकर दूर ले जाने बालों से संग्राम करके उन्हें नष्ट करें । आप अपने भक्तों को, श्रेष्ठ प्रकाश, गौएँ एवं उत्तम प्रकार का जल प्रदान करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11465)
- **Original**: 4989. आ वृत्रहणा वृत्रहि: शुष्मैरिन्द्र यातं नमोभिरग्ने अर्वाक्‌ । युवं राघोभिरकवेभिरिन्द्राग्ने अस्मे भवतमुत्तमेभि:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11466)
- **Original**: हे वृवहन्ता इद्ध और अग्निदेवो ! शत्रु को नष्ट करने वाले सामर्थ्य के साथ अन्न लेकर आप हमारे निकट आएँ । आप दोनों अनिन्द्र एवं श्रेष्ठ धन सहित हमारे पास पधारें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11467)
- **Original**: 4990. ता हुवे ययोरिदं पण्ने विश्व पुरा कृतम्‌। इन्द्राग्नी न मर्धतः
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11468)
- **Original**: .. इन्द्रदेव और अग्निदेव का विश्व निर्माण में पहले से सहयोग रहा है । इस कारण उनकी प्रशंसा करते हुए हम उनका आवाहन करते हैं । वे इन्द्र और अम्निदेव स्तोता और याजकों की रक्षा करते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11469)
- **Original**: 4991. उग्ा विघनिना मृध इन्द्राग्नी हवामहे
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11470)
- **Original**: ता नो पृव्ठात ईदूशे
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11471)
- **Original**: द्ड ऋग्वेद संहिता भाग - 2 उम्म शत्रु को संग्राम में विदीर्ण करने वाले, जो इन्द्र और अग्निदेव हैं, उनका हम आवाहन करते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11472)
- **Original**: वे दोनों देव हमें सफल और सुखी बनाएँ
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11473)
- **Original**: 4992. हतो वृत्राण्यार्या हतो दासानि सत्पती । हतो विश्वा अप द्विषः
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11474)
- **Original**: जो इन््देव और अग्निदेव दुष्ट असुरों की दुष्टता का संहार करते हैं एवं सज्जनों की रक्षा करते हैं , उन्हीं देवों ने सब शत्रुओं का विनाश किया है
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11475)
- **Original**: 4993, इन्द्राग्नी युवामिमे3भि स्तोमा अनूषत
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11476)
- **Original**: पिबतं शम्भुवा सुतम्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11477)
- **Original**: हे सुखप्रदाता इन्द्रदेव और अग्निदेव ! ये स्तोतागण आप दोनों की वन्दना करते हैं। आप दोनों सोमरस का पान करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11478)
- **Original**: 4994. या वां सन्ति पुरुस्पृहो नियुतो दाशुषे नरा। इन्द्राग्गी ताभिरा गतम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11479)
- **Original**: जगत्‌ के नायक हे इन्रदेव और अग्निदेव ! याजकों द्वारा प्रशंसा किये जाते हुए, आप दोनों उनसे प्रदत्त हविष्यात्र के लिए यज्ञशाला में अपने द्रुतगामी वाहन (अश्व) की सहायता से पधारें तथा दानदाताओं की सहायता करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11480)
- **Original**: 4995, ताभिरा गच्छतं नरोपेदं सवन॑ सुतम्‌। इन्द्राग्गी सोमपीतये
- **Translation**: 

---

