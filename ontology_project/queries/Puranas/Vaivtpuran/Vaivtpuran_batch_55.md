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

### Verse 1 (Vaivtpuran 5.2353)
- **Original**: सुप्त॑ स्व॑ दैववशान्रवीभूत॑ पुनः कुरु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 5.2354)
- **Original**: यथाहुरं भस्मनि च करोति देवता पुनः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 5.2355)
- **Original**: अह्स्वरूपा परमा ज्योतोीरूपा सनातनी । सर्वविद्याध्रिदेत्तें या तस्ये वाण्ये नमो नमः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 5.2356)
- **Original**: यया विना जगत्‌ सवव॑ शश्ज्जीवन्मृतं सदा। ज्ञानाधिदेवी या तस्थे सरस्वत्ये नमो नमः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 5.2357)
- **Original**: यया विना जगत्‌ सर्व॑ मृकमुन्मत्तततू सदा । यागधिष्ठातृदेवी या तस्थै याण्ये नमो नमः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 5.2358)
- **Original**: हिमचचनकुन्देन्दुकुमुदाम्भोजसंनिभा । वर्णांधिदेवी या तस्थे चाक्षराये॑ नमो नमः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 5.2359)
- **Original**: विसगंबिन्द॒मात्नाणां यदधिष्ठानमेव च। इत्थं त्व॑ं गीयसे सद्धिर्भारत्य॑ ते नमो नमः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 5.2360)
- **Original**: यया बिना च संख्याता संख्यां कतूं न शक्यते । कालसंख्यास्वकूपा या तस्यै देव्ये नमो नमः व्याख्यास्वकूपा या देवों व्याख्याधिष्ठातदेवता । भ्रमसिद्धान्तक्पा या तस्थे देव्ये नमो नमः
- **Translation**: 

---

### Verse 9 (Vaivtpuran 5.2361)
- **Original**: स्पृतिशक्तिज्ञांनशक्तिबुंद्धिशक्तिस्वरूपिणी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 5.2362)
- **Original**: प्रतिभा कल्पता शक्तिया च तस्‍स्मेँ नमो नमः । बभूव जडवत्‌ सो5पि सिद्धात्त॑ कर्तुमक्षम: । उबाच स॒च तां स्तौहि वाणीमिष्टां प्रजापते । चकार त्वत्प्रसादेना तेदा सिद्धान्तमुत्तमम्‌ । बभूव मूकवत्‌ सो5पि सिद्धान्त कर्तुमक्षम: । ततश्बकार सिद्धान्त॑ निर्मल भ्रमभञ्जञनम्‌ । मौनीभूत; स॑ सस्मारत्वापेव जगदम्विकाम्‌ । सम्प्राप्प निर्मल॑ ज्ञान प्रमादध्यंसकारणम्‌ । त्थां सिषेये च दध्याौ थ शतपर्ष च॒ पुष्करे। तदा वेदविभागं चर पुराणं च चकार सः
- **Translation**: 

---

### Verse 11 (Vaivtpuran 5.2363)
- **Original**: क्षणं त्वामेत्त संचिन्त्य तस्मै ज्ञानं ददौ विभुः । दिव्यं वर्षसहस्ल॑ च स त्वां दध्यौ च पुष्करे। उवाच शब्दशास्त्रं च तदर्थ च सुरेश्वरम्‌ । ते च त्वां परिसंचित्य प्रवर्तन्ते सुरेध्वरीम्‌ । दैत्येद्रेधआ.. सुरैशापि ब्रद्मविष्णुशिवादिभि: । यां स्तोतुं किमह. स्तौमि तामेकास्येन मानव: । प्रणवाम निराहाये रुखेद चर मुहर्मुहुः। सुकवीद्रों भवेत्युक्ता वैकुण्ठ॑ च जगाम है । स॑ कवीद्रों महावासी बृहस्यतिसमों धभवेत्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 5.2364)
- **Original**: सनत्कुमारों ब्रह्माणं ज्ञानं पप्रच्छ यत्र खै
- **Translation**: 

---

### Verse 13 (Vaivtpuran 5.2365)
- **Original**: तदा55जगाम भगबानात्मा. श्रीकृष्ण ईश्वर:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 5.2366)
- **Original**: स॒च तुशव त्वां ब्रह्म चाज्ञया परमात्मनः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 5.2367)
- **Original**: यदाप्यनन्त॑ पप्रच्छ जझ्ञानमेंके वसुंघरा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 5.2368)
- **Original**: तदा त्यां स च तुष्टाव संत्रस्त: कश्यपाज्ञया
- **Translation**: 

---

### Verse 17 (Vaivtpuran 5.2369)
- **Original**: व्यास: पुराणसूत्र च पप्रच्छ वाल्मिकि यदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 5.2370)
- **Original**: तदा चकार सिद्धान्त स्वद्रेण मुनीश्चर:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 5.2371)
- **Original**: पुराणसूत्र श्रुववा च॒ व्यास: कृष्णकलोद्रव:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 5.2372)
- **Original**: तदा त्वन्नों वर प्राप्य सत्कवोन्द्रों बभूव ह
- **Translation**: 

---

