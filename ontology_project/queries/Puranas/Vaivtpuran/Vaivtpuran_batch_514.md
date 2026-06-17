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

### Verse 1 (Vaivtpuran 30.17792)
- **Original**: तत्रोबास तमाबोध्य चावरुह्म वृषाच्छिव:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 30.17793)
- **Original**: मुच्यते सर्वपापेभ्यो भयेभ्यक्ष॒भवार्णवे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 30.17794)
- **Original**: भार्याहीनो लभेद्‌ भायाँ सुशीलां सुमनोहराम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 30.17795)
- **Original**: राज्यभ्रष्टो लभेद्‌ राज्यं शंकरस्यथ प्रसादतः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 30.17796)
- **Original**: गर्भीरेठइतिजलाकीणें.. भग्रपोते. विषादने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 30.17797)
- **Original**: सर्वतो मुच्यते स्तुत्वा शंकरस्य प्रसादतः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 30.17798)
- **Original**: जति श्रीब्रह्मबैवर्तें हिमालयक्ृतं शिवस्तोत्र सम्पूर्ण्‌। ( श्रीकृष्णजन्मखण्ड 38। 65-78 ) #जलज पिया 9ल्‍->>>
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7458)
- **Original**: 358 * संक्षिप्त बरह्मवैवर्तपुराण * कक कक ऋ कक ऋऋऋऋऋक्ककऋ ऋऋऋक्क कऋ्ऋऋ्क ऋऋक् कक ऋऋऋऋऋऋऋ जिस पुरुषकों यह मन्त्र सिद्ध हो जाता है, उसके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7459)
- **Original**: राधाके वक्ष:स्थलमें विराजमान रहते हैं। सिद्धेन्द्र, लिये विश्व करतलगत हो जाता है। वह समुद्रोंको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7460)
- **Original**: मुनीद्र और देवेन्द्र जिनकी सेवामें लगे रहते हैं पी सकता है, विश्वका संहार करनेमें समर्थ हो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7461)
- **Original**: तथा ब्रह्मा, विष्णु, महेश और श्रुतियाँ जिनका .. है और इसी पाक्रभौतिक शरीरसे वैकुण्ठमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7462)
- **Original**: स्तवन करती रहती हैं; उन श्रीकृष्णका मैं भजन जा सकता है। उसके चरणकमलकी करता हूँ। स्पर्शमात्रसे सारे तीर्थ पवित्र हो जाते हैं और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7463)
- **Original**: जो मनुष्यं इस ध्यानसे श्रीकृष्णका ध्यान पृथ्वी तत्काल पावन हो जाती है। मुने! जो भोग
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7464)
- **Original**: करके उन्हें षोडशोपचार समर्पित कर भक्तिपूर्वक और मोक्षका प्रदाता है, सर्वेश्वर श्रीकृष्णफका वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7465)
- **Original**: उनका भलीभाँति पूजन करता है, वह सर्वज्ञत्व सामवेदोक्त ध्यान मेरे मुखसे श्रवण करो। जो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7466)
- **Original**: प्राप्त कर लेता है। (पूजनकी विधि यों है-- )पहले रत्ननिर्मित सिंहासनपर आसीन हैं; जिनका वर्ण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7467)
- **Original**: भगवान्‌को भक्तिपूर्वक अर्घ्य, पाद्य, आसन, वस्त्र, नूतन जलधरके समान श्याम है; नेत्र नीले
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7468)
- **Original**: भूषण, गौ, अर्घ्य, मधुपर्क, परमोत्तम यज्ञसूत्र, कमलकी शोभा छोने लेते हैं; मुख शारदीय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7469)
- **Original**: धूप, दीप, नैवेद्य, पुन आचमन, अनेक प्रकारके पूर्णिमाके चन्द्रमाकों मात कर रहा है, उसपर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7470)
- **Original**: पुष्प, सुवासित ताम्बूल, चन्दन, अगुरु, कस्तूरी, मन्द मुस्कानकी मनोहर छटा छायी हुई है। जो
- **Translation**: 

---

