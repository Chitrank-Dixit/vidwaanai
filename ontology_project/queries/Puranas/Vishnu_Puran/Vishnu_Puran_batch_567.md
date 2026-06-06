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

### Verse 1 (Vishnu Puran 0.11321)
- **Original**: 14 तद्धस्मस्पर्शसम्भूतताप: कृष्णाड्सड्रमात्‌ । अबाप बलदेवो5उपि श्रममामीलितेक्षण:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11322)
- **Original**: 15 ततस्स युद्धच्ममानस्तु सह देबेन शार्ड्रिणा । वैष्णवेन ज्वरेणाशु कृष्णदेह्ान्निराकृत:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11323)
- **Original**: 16 नारायणभुजाघातपरिपीडनविद्वलम्‌__। ते वीक्ष्य क्षम्यतामस्येत्याह देव: पितामह:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11324)
- **Original**: 17 ततश्च क्षान्तमेवेति प्रोच्य ते वैष्णवं ज्वरम्‌ आत्मन्येब लय निनन्‍्ये भगवान्म्रधुसूदनः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11325)
- **Original**: 18 ज्वर उवाच मम त्वया सर्म युद्धे ये स्मरिष्यन्ति मानवा: । भविष्यन्तीत्युक्त्वा चने ययो ज्वरः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11326)
- **Original**: 19 ततो5पीन्भगवान्यञ्ञ जित्वा नीत्वा तथा क्षयम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11327)
- **Original**: दानवानां बले कृष्णश्रूर्णयामास लीलया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11328)
- **Original**: 20 ततस्समस्तसैन्येन दैतेयानां बलेस्सुत: । युयुथे शब्डरक्षैव कार्त्तिकियश्न शौरिणा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11329)
- **Original**: 29 हरिशह्डूरयोर्युद्धमतीवासीत्सुदारूणम्‌.._
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11330)
- **Original**: चुक्षुभुस्सकला लोका: हास्त्राद्यांशुप्रतापिता:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11331)
- **Original**: 22 प्रलयोड्यमशेषस्थ जगतो .नूनमागत: । मेनिरे त्रिदशास्तत्र वर्तमाने महारणे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11332)
- **Original**: 23 जृम्मकास्त्रेण गोविन्दो जृम्भयामास शद्भूरम्‌ । ततः प्रणेशुर्दैतिया: प्रमथाश्ष समन्ततः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11333)
- **Original**: 24 जुम्भाभिभूतस्तु हरो रथोपस्थ ठपाविदवत्‌ । न शझाक ततो योदध्धु कृष्णेनाक्लिप्रकर्मणा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11334)
- **Original**: 25 गरुडक्षतवाहश्चप्रद्युम्नाप्ेण पीडित: । कृष्णहुड्डारनिर्धूतशक्तिश्ापययो.. गुहः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11335)
- **Original**: 26 चढ़कर श्रीहरि बलराम और प्रदयुश्नके सहित 'याणासुरको राजधानीमें आये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11336)
- **Original**: नगरमें घुसते ही उन तीनॉका भगवान्‌ हौकरके पार्षद प्रमथगणोंसे युद्ध हुआ; उन्हें नष्ट करके श्रीहरि वाणासुरको राजधानीके समीप चले जये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11337)
- **Original**: तदनन्तर बाणासुरकी रक्षाके लिये तीन सिर और तीन पैरवाला माहेश्वर नामक महान्‌ ज्वर आगे बढ़कर श्रीभगवानसे लड़ने ऊूगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11338)
- **Original**: [ उस ज्वस्का ऐसा प्रभाव था कि ] उसके फेंके हुए भस्मके स्पर्शसे सन्तप्त हुए श्रोकृष्णचन्द्रके शरीस्का आलिक्जन करनेपर बलदेवजीने भी शिथिल होकर नेत्र मुँद लिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11339)
- **Original**: इस प्रकार भगवान्‌ शार्ज्रधरके साथ [ उनके शरीरमें व्याप्त होकर ] युद्ध करते हुए उस महेश्वर ज्वरको वैष्णव ज्वरने तुरंत उनके दारीरसे निव्यल दिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11340)
- **Original**: उस समय श्रीनारायणकी भुजाओकि आघातसे उस माहेश्वर ज्वर्को पीड़ित और घिह्ल्‍ल हुआ देखकर पितामह ब्रह्माजीने भगवानसे कहा--'इसे क्षमा कीजिये'
- **Translation**: 

---

