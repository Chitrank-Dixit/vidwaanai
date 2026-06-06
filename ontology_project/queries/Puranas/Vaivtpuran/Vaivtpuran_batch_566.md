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

### Verse 1 (Vaivtpuran 39.18169)
- **Original**: सुरभी सा गवां माता दक्षिणा यज्ञकामिनी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.18170)
- **Original**: स्वाहा त्व॑ च हविरदाने कव्यदाने स्वधा स्मृता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.18171)
- **Original**: शुद्धसत्त्वस्वरूपा_त्व॑ नारायणपरायणा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.18172)
- **Original**: परमार्थप्रदा त्व॑ च हरिदास्यप्रदा परा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.18173)
- **Original**: जीबन्मृतं चर विश्व च॒ शबतुल्यं यया बिना
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.18174)
- **Original**: यया बिना न सम्भाष्यो बान्धवैर्बान्धव: सदा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.18175)
- **Original**: धर्मार्थकाममोक्षाणां त्व॑ च् कारणरूपिणी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.18176)
- **Original**: तथा त्व॑ सर्वदा माता सर्वेषां सर्वरूपतः:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.18177)
- **Original**: त्वया हीनो जनः को5पि न जीवत्येब निश्चितम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.18178)
- **Original**: वैरिग्रस्त॑ च विषय देहि महां सनातनि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.18179)
- **Original**: सर्वसम्पट्टिहानाश्भध ताबदेव हरिप्रिये
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.18180)
- **Original**: कीर्ति देहि धन देहि यशों महू च देहि बै
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.18181)
- **Original**: ज्ञानं देहि चर धर्म च्॒ सर्वसौभाग्यमीप्सितम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.18182)
- **Original**: जय॑ पराक्रम॑ युद्धे परमैश्नयंमेव च
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.18183)
- **Original**: प्रणनाम साशथ्रुनेत्रो मूर्न्‍्धा चैब पुनः पुनः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.18184)
- **Original**: सर्वे चक्ुः परीहारं सुरा्थे चर पुनः पुनः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.18185)
- **Original**: केशवाय ददौ लक्ष्मी: संतुष्टा सुरसंसदि
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.18186)
- **Original**: देवी ययौ हरे क़ोडं हृष्टा क्षीरोदशायिन:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.18187)
- **Original**: दत्त्वा शुभाशिषं तौ च देवेभ्य: प्रीतिपूर्वकम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.18188)
- **Original**: कुबेरतुल्य: स भवेद्‌ राजराजेश्वरो महान्‌
- **Translation**: 

---

