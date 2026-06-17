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

### Verse 1 (Vaivtpuran 44.8417)
- **Original**: नामाष्टक स्तोत्रका, जो नाना अर्थोसे संयुक्त एवं उत्तम स्तोत्र सम्पूर्ण विष्नोंका नाशक है। शुभकारक है, नित्य तीनों संध्याओऑंके समय पाठ मातः ! तुम्हारे पुत्रके गणेश, एकदन्त, हेरम्ब,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 44.8418)
- **Original**: करता है, वह सुखी और सर्वत्र विजयी होता है। विप्ननायक, लम्बोदर, शुर्पकर्ण, गजवक्त्र और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 44.8419)
- **Original**: उसके पाससे विन्न उसी प्रकार दूर भाग जाते हैं, गुहाग्रज--ये आठ नाम हैं। इन आठों नामॉका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 44.8420)
- **Original**: जैसे गरुड़के निकटसे साँप । गणेश्वरकी कृपासे वह अर्थ सुनो। शिवप्रिये! यह उत्तम स्तोत्र सभी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 44.8421)
- **Original**: निश्चय ही महान्‌ ज्ञानी हो जाता है, पुत्रार्थीको पुत्र स्तोत्रोंका सारभूत और सम्पूर्ण विश्लोंका निवारण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 44.8422)
- **Original**: और भार्याकी कामनावालेकों उत्तम स्त्री मिल करनेवाला है। “ग' ज्ञानार्थाचक और “ण'
- **Translation**: 

---

### Verse 7 (Vaivtpuran 44.8423)
- **Original**: जाती है तथा महामूर्ख निश्चय ही विद्वान्‌ और श्रेष्ठ निर्वाणवाचक है। इन दोनों (ग+ण)-के जो ईश
- **Translation**: 

---

### Verse 8 (Vaivtpuran 44.8424)
- **Original**: कवि हो जाता है*। हैं; उन परब्रह्म 'गणेश' को मैं प्रणाम करता हूँ। (अध्याय 44) 34000 02 229934295-.00005 के विष्णुरुवाच-- गणेशमेकदन्त॑ च हेरम्ब॑ विप्ननायकम्‌ । लम्बोदर॑ शूर्पकर्ण गजवक्त्न॑ गुहाग्रजम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 44.17799)
- **Original**: + शिवस्तोत्राणि * उ87 ह..3
- **Translation**: 

---

### Verse 10 (Vaivtpuran 44.17800)
- **Original**: 4 8 4 8 8 4 «4 44 4 044 4... 4.4: _++0-.8033. 00088... 7-7 >#ूड7 हिमालयकृतं शिवस्तोत्रम्‌ (2) हिमालय उवाच प्रसीद दक्षयज्ञत्त॒ नरकार्णवतारक । सर्वात्मरूप सर्वेश 'परमानन्दविग्रह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 44.17801)
- **Original**: गुणार्ण गुणातीत गुणयुक्त गुणेश्वर। गुणबीज महाभाग प्रसीद गुणिनां बर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.17802)
- **Original**: योगाधार योगरूप योगज्ञ योगकारण । योगीश योगिनां बीज प्रसीद योगिनां गुरो
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.17803)
- **Original**: प्रलय प्रलयाह्मैक भ्वप्रलयकारण । प्रलयान्ते सुष्टिबीज प्रसीद परिपालक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.17804)
- **Original**: संहारकाले घोरे च सृष्टिसंहारकारण । दुर्निवार्य दुराराध्य चाशुतोष प्रसीद मे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.17805)
- **Original**: कालस्वरूप कालेश काले च फलदायक । कालबीजैक कालप्न प्रसीदकालपालक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.17806)
- **Original**: शिवस्वरूप शिवद शिवबीज शिवाश्रय । शिवभूत शिवप्राण प्रसीद परमाश्रय
- **Translation**: 

---

### Verse 17 (Vaivtpuran 44.17807)
- **Original**: इत्येब॑ स्तवन॑ कृत्वा विरराम हिमालय: । प्रशशंसुः सुरा: सर्वे मुनवश्ष गिरीश्वरम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 44.17808)
- **Original**: हिमालयकृतं स्तोत्र संयतो यः पठेन्नर: । प्रददाति शिवस्तस्मै बाउछत राधिके ध्रुवम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 44.17809)
- **Original**: इति श्राब्रह्मवैवर्ते हिमालयकृत॑ शिवस्तोत्रं सप्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 44। 63--71) शुक्रकृतं शिवस्तोत्रम्‌ शुक्र उवाच सुराणामसुराणां च्॒ सर्वेषां जगतामपि । त्वप्रेव शास्ता भगवान्‌ को वा शास्ति सुरे5सुरे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 44.17810)
- **Original**: कृत्वा सुराणां साहाव्य॑ कथं दैत्यान्‌ हनिष्यसि । संहर्तु: सर्वजगतां दैत्यौधे कि च पौरुषम्‌
- **Translation**: 

---

