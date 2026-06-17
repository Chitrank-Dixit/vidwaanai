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

### Verse 1 (Narsihma Puran 0.4821)
- **Original**: र्छ्ड ततो देवगणा: सर्वे खासवेन समन्विता:। जम्मुझ् ब्रह्मसद्न तथा दीना शची तदा
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.4822)
- **Original**: 100 ख्रह्मा भग्रसमाधिश्च तावत्‌ तत्रेव संस्थिता: । देबा ऊचुश्ष ते सर्वे वासवेन समन्विता:
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.4823)
- **Original**: 101 तृणबिन्दोर्पुने: शापाद्यात: स्त्रीत्वं सुराधिप:। स मुनि: कोपबान ब्रह्मग्रैव गच्छत्यनुग्रहम्‌
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.4824)
- **Original**: 102 प्रिठामह उकाच्र न॒मुनेरपराध: स्थात्तणविन्दोर्महात्मन:। स्वकर्मणोपयातो उसौ स्त्रीत्वं स्वीवधकारणात्‌
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.4825)
- **Original**: 103 जहार चित्रसेनां चर सुगुप्तां धनदाड़ुनाम्‌
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.4826)
- **Original**: 904 तथा जघान युवती तृणबिन्दोस्तपोवने। तेन कर्मविपाकेन स्त्रीभाव॑ वासवों गत:
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.4827)
- **Original**: 105 देवा हऊुपः यदसौ कृतयाय्शम्भोर्दुर्नय॑ नाथ दुर्मति:। तत्सर्व साधयिष्यामों वयं शच्या समन्बिता:
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.4828)
- **Original**: 106 कान्ता धनाधिनाथस्य गूढा तिष्ठति या बिभो। तां च तस्मे प्रदास्याम: सर्वे कृत्वा परां मतिमू
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.4829)
- **Original**: 107 ब्रयोदश्यां अतुर्दश्यां देवराज: शचीयुतः
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.4830)
- **Original**: नन्दने चार्चन॑ कर्ता सर्वदा यक्षरक्षसाम्‌
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.4831)
- **Original**: 108 तत: शी तदा गूढं चित्रसेनां बिगृह्मां च। मुपोच्च यक्षभवन प्रियकष्टानुवर्तिनीम्‌
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.4832)
- **Original**: 109 एतस्मित्नन्तरे दूतोउइकाले लड्ढां समागत:। धनेशं कथयामास चित्रसेनासमागम्म्‌
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.4833)
- **Original**: 110 शच्या साकं समायाता तब कान्‍्ता धनाधिप। सख्त्री स्वामतुलां प्राप्य चरितार्था बभूव सा
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.4834)
- **Original**: 911 धनेशो5पि कृतार्थो5भूजगाम निजबेश्मनि। देक ऊचु: सर्वमेतत्कृतं ब्रह्मन्‌ प्रसादात्ते न संशय:
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.4835)
- **Original**: 112 ( अस्याय 63 5-2 आर आए >>: शत अं कम तत्पक्षात्‌ सभी देवता और दौना शची इन्द्रको साथ लेकर अद्याजोफे धामकों गये। जबतफ त्रह्माजी समाधिसे विरत हुए, तबतक ये सभी वहाँ ठहरे रहे और इन्द्रके साथ हो सब देवता ब्रह्माजीसे बोले
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.4836)
- **Original**: 98--101
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.4837)
- **Original**: “ब्रह्म! सुरणाज इद्ध तृणचिन्दु मुनिके शापसे स्त्रीयोनिको ग्राप्त हो गये हैं; वे मुनि बड़े क्रोधी हैं, किसी प्रकार अनुग्रह नहीं करते'
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.4838)
- **Original**: ख्रहद्माजी बोले-- इसमें उन महात्मा तृणविरदु मुनिका कोई अपराध नहीँ है। इन्द्र स्त्रीवघरूपी अपने ही कर्मसे स्त्रीभाषको प्राप्त हुए हैं। देवताओं! देवराज इच्धने भी मदमत होकर बढ़ा ही अन्याय किया है, जो कुबेरकी पत्नी चित्रसेनाका गुसरूपसे अपहरण कर लिया। यहा नहीं, इन्होंने तृणबिन्दुके तपोबनमें एक युवतोका यध किया है, अत: अपने इस निन्‍्द्य कर्मके परिणामस्वरूप ही ये इन्द्र स्त्रीभावको प्राप्त हुए हैं
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.4839)
- **Original**: 103--105
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.4840)
- **Original**: देवगण बोले--नाथ इन्होंने दुर्युद्धिसे प्रेरित होकर जो शंकरप्रिय कुबेरका अपमान किया है, उसके लिये हम सब लोग शचीौके साथ कुयेरको प्रसन्न करनेका यत्र करेंगे। विभो! कुबेरकों पत्नी चित्रसेना मन्दराचलपर गुमरूपसे रहती है, हम सभी लोग सम्मति करके उसे कुबेर्को अर्पित कर देंगे। देवराज इन्द्र भी प्रति त्रयोदशी और चहुर्दशीकों नन्दनवनमें शचोकों साथ लेकर यक्ष और राक्षसॉंकी पूजा करेंगे
- **Translation**: 

---

