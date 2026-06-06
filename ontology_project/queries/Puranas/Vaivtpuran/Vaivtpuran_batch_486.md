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

### Verse 1 (Vaivtpuran 27.7188)
- **Original**: (गणपतिखण्ड 27। 62)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 27.17968)
- **Original**: * ओदुर्ास्तोत्राधि * 793 विपत्तिवाचको दुर्गश्षाकारो नाशवाचक: दुर्गों दैत्येन्द्रबचनोउप्याकारो नाशवाचकः शञ्च॒ कल्याणवचन इकारोत्कृष्टवाचकः श्रेय:संघोत्कृष्टदात्री शिवा तेन प्रकीर्तिता शिवो हि. मोक्षवचनश्राकारो दातृवाचक: अभयो भयनाशोक्तक्षाकारो दातृवाचकः राजश्रीवत्चननो माश्न॒याश्च प्रापणवाचक: माश्च मोक्षार्थचनो याश्र प्रापणबाचकः नारायणार्थाड्रभूता तेन तुल्या च तेजसा निर्गुणस्थ च॒ नित्यस्थ वाचकश्न॒ सनातनः जय: कल्याणबच्चननो ह्वाकारो दातृबाचकः । दुर्ग नश्यति या नित्य सा दुर्गा परिकीर्तिता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 27.17969)
- **Original**: । त॑ ननाश पुरा तेन बुधैर्दुर्गा प्रकीर्तिता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 27.17970)
- **Original**: । समूहवाचकश्चैब बाकारो. दातृवाचकः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 27.17971)
- **Original**: । शिवरशिम्मूर्तिमती शिवा तेन प्रकीर्तिता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 27.17972)
- **Original**: ) स्वयं निर्वाणदात्री या सा शिवा परिकीर्तिता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 27.17973)
- **Original**: प्रददात्यभयं॑ सद्दा: साभया परिकीर्तिता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 27.17974)
- **Original**: तां प्रापयति या सद्यः सा माया परिकीर्तिता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 27.17975)
- **Original**: ते प्रापयति या नित्यं सा माया परिकीर्तिता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 27.17976)
- **Original**: सदा नित्या निर्गुणा या कीर्तिता सा सनातनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 27.17977)
- **Original**: जय॑ ददाति या नित्यं सा जया परिकीर्तिता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 27.17978)
- **Original**: । तदा तस्य शरीरस्था तेन नारायणी स्मृता
- **Translation**: 

---

### Verse 13 (Vaivtpuran 27.17979)
- **Original**: सर्वमड्गलशब्दश्न सम्पूर्ण श्वरथवाचक: । आकारों. दातृवचनस्तद्वात्री सर्वमड्रला
- **Translation**: 

---

### Verse 14 (Vaivtpuran 27.17980)
- **Original**: नामाष्टकमिंद॑_ सार नामार्थसहसंयुतम्‌ । नारायणेन यद्‌ दत्त ब्रह्मणे नाभिपड्ूजे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 27.17981)
- **Original**: तस्मै दत्त्वा निद्वितक्ष बभूज जगतां पति:। मधुकैटभौ दुर्गान्‍्ताौ ब्रह्माणं हन्तुमुछातौ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 27.17982)
- **Original**: स्तोत्रेणानेन स ब्रह्मा स्तुतिं नत्वा चकार ह। इति क्रीब्रह्मवेंवतें ब्रह्मकृतं जवदु्ास्तोत्रं सम्पूर्णम्‌। (श्रीकृष्णजन्मखण्ड 27। 17-34 3-) #*्यकरयद%02>- जानकीकृतं पार्वतीस्तोत्रम्‌ू ( एतदेव राधाकृतं पार्वतीस्तोत्रम्‌ ) जानक्युवाच शक्तिस्वरूपे सर्वेषां सर्वाधारे गुणाश्रये । सदा शंकरयुक्ते च पतिं देहि नमोउस्तु ते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 27.17983)
- **Original**: सृष्टिस्थित्वन्तरूपेण... सुष्टिस्थित्यन्तरूपिणि । सृष्टिस्थित्यन्तनबीजानां बीजरूपे नमोस्तु ते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 27.17984)
- **Original**: है गौरि पतिमर्मज्े पतिब्रतपरायणे । पतिक्नते पतिरते पतिं देहि नमोउस्तु ते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 27.17985)
- **Original**: सर्वमड्गलमड्डढल्ये सर्वमड्गलसंयुते । सर्वमड्डलबीजे च नमस्ते. सर्वमड्रले
- **Translation**: 

---

### Verse 20 (Vaivtpuran 27.17986)
- **Original**: सर्वप्रिये.. सर्वबीजे. सर्वाशुभविनाशिनि । सर्वेशे सर्वजनके नमस्ते. शंकरप्रिये
- **Translation**: 

---

