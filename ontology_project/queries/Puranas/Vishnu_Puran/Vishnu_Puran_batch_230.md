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

### Verse 1 (Vishnu Puran 0.4581)
- **Original**: 14 वसिष्ठतनया होते सप्त सप्तर्षयो3भवन्‌ । अजः परशुदीप्ताद्यास्तथोत्तममनोस्सुता;
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4582)
- **Original**: 15 तामसस्थान्तरे देवास्सुपारा हस्यस्तथा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4583)
- **Original**: सत्याक्ष सुधियश्चेव सप्तविंशतिका गणा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4584)
- **Original**: 16 शिबिरिन्द्रस्त्था चासीच्छतयज्ञोपलक्षण: । सप्तर्षयश्न ये तेषां तेषां नामानि में श्रूणु
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4585)
- **Original**: 17 ज्योतिर्धामा पृथु: काव्यश्षैत्रोउपिवनकस्तथा । पीबसश्चर्षयो होते सप्त तन्नापि चान्तरे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4586)
- **Original**: 18 नरः ख्याति: केतुरूपो जानुजद्भादयस्तथा । पुत्रास्तु तामसस्थासत्राजानस्मुमहाबलाः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4587)
- **Original**: 19 पश्चमे वापि मैत्रेय रैवतो नाम नामतः । मनुर्विभुश्ष॒तत्रेन्रों देवांश्षात्रान्ते श्रुणु
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4588)
- **Original**: 20 अमिताभा भूतरया बैकुण्ठास्ससुमेधसः । एते देवगणास्तत्र चतुर्दश चतुर्दश
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4589)
- **Original**: 21 हिरण्यरोमा.वेद्श्रीरूर्ध्वबराहुस्तथापरः । वेदबाहुस्सुधामा चर पर्जन्यश्चष महामुनिः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4590)
- **Original**: एते सप्रर्षवो विप्र तत्रासब्रैवतेउन्तरे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4591)
- **Original**: 22 बलबन्धुश्न सम्भाव्यस्सत्यकद्याश्च तत्सुता: । नरेन्द्राश्नो महायीया बभृधुर्मुनिसत्तम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4592)
- **Original**: 23 स्वारोच्िषश्रोत्तमश्न॒तामसो रैबतस्तथा । प्रियब्रतान्वया होते चत्वारों मनवस्स्‍्मृता:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4593)
- **Original**: 24 विष्णुमाराध्य तपसा स राजर्षि: प्रियत्रत: । मन्वन्तराधिपानेताँल्‍लख्थवानात्मवंशजान्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4594)
- **Original**: 25 बष्टे मन्वन्तरे चासीधाक्षुषास्यस्तथा मनुः । मनोजबस्तथैवेन्द्रो देवानपि निबोध में
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4595)
- **Original**: 26 आप्या: प्रसूता भव्याश्न पृथुकाश्न दिबौकस: । महानुभावा लेखाश्न पद्ञिते ह्ाष्टका गणा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4596)
- **Original**: 27 हे ब्रह्मन्‌ ! तीसरे मन्वन्तरमें उत्तम नामक मनु और सुझान्ति नामक देवाधिपति इन्द्र थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4597)
- **Original**: उस समय सुधाम, सत्य, जप, ग्रतर्दन और चद्ावर्ती--ये पाँच खारह-खारह टेखताओंकि गण थे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4598)
- **Original**: तथा वसिष्ठजीके सात पुत्र सप्तर्तिगण और अज, परज्ञु एवं दीम आदि उत्तमम्नुके पुत्र थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4599)
- **Original**: तामस- मन्वत्तरमें सुपार, हरि, सत्य और सुधि--ये चार देवताओंके यर्ग थे और इनमेंसे प्रत्येक वर्गें सत्ताईस-सत्ताईइस देवगण थे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4600)
- **Original**: सौ अश्वमेध यश्ञवाल्त्र राजा हिबि इन्द्र था तथा उस समय जो सप्तर्षिणण थे उनके नाम मुझसे सुनों--
- **Translation**: 

---

