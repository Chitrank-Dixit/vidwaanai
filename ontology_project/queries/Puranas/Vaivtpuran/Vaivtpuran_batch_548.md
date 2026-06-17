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

### Verse 1 (Vaivtpuran 37.18096)
- **Original**: यदि स्यात्‌ सिद्धकवच: सर्वसिद्धी श्वरो भवेत्‌ । महादानानि सर्वाणि तपांसि चर ब्रतानि च। निश्चितं कवचस्यास्थ कलां नाहन्ति घोडशीम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 37.18097)
- **Original**: इद कबचमन्नात्वा भजेत्‌ कालीं जगत्प्रसूम । शतलक्षप्रजप्तोषप न मन्त्र: सिद्धिदायक:ः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 37.18098)
- **Original**: इति अ्रीब्रह्मवैवर्ते मन्‍त्रसाहित॑ कालीकवर्च सम्पूर्णम्‌। (गणपतिखण्ड 37। 1--24) “++“म्चप्थ >> ब्रह्माण्डविजयं नाम दुर्गाकबचम्‌ नारायण उबाच श्रुणु नारद वक्ष्यामि दुर्गाया: कवच शुभम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 37.18099)
- **Original**: श्रीकृष्णेनेव यद्‌ दत्त गोलोके ब्रह्मणे पुरा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 37.18100)
- **Original**: ब्रह्मा त्रिपुरसंग्रामे शंकराय ददौ पुरा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 37.18101)
- **Original**: जधान त्रिपुरं रुड्रो यद्‌ धृत्वा भक्तिपूर्वकम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 37.18102)
- **Original**: हरो ददौ गौतमाय पशद्माक्षाय चर गौतम:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 37.18103)
- **Original**: यतो जबभूव पग्माक्ष: स्तद्वीपेश्रो जयी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 37.18104)
- **Original**: यद्‌ धृत्वा पठनाद्‌ ब्रह्मा ज्ञानवाज्छक्तिमान्‌ भुवि । शिवों बभूव सर्वज्ञो योगिनां श्र गुरुर्यत:। शिवतुल्यों गौतमश्ञ बरभूव मुनिसत्तम:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 37.18105)
- **Original**: ज्रह्माण्डबिजयस्यास्य कवचस्य॒ प्रजापति: । ऋषिश्छन्दश्न गायत्री देवी दुर्गतिनाशिनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 37.18106)
- **Original**: स्रह्माण्डलिजये चैव विनियोग: प्रकीर्तितः । पुण्यतीर्थ च महतां कवच परमाद्धुतम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 37.18107)
- **Original**: 3 हीं दुर्गतिनाशिन्यै स्वाहा में पातु मस्तकम्‌ । 3* ह्रीं मे पातु कपालं च 33% ह्रीं श्रीमिति लोचने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 37.18108)
- **Original**: पातु में कर्णयुग्म च 37 दुर्गाय॑ नमः: सदा । 30 हुं श्रीमिति नासां मे सदा पातु चर सर्वतः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 37.18109)
- **Original**: हीं श्रीं हमिति दन्तानि पातु क्लीमोष्ठयुग्मकम्‌ । क्री क्रों क्रो पातु कण्ठं च दुर्गे रक्षतु गण्डकम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 37.18110)
- **Original**: स्कर्च्ध दुर्गविनाशिनय स्वाहा पातु निरन्तरम्‌ । वक्षो विपद्विनाशिन्यै स्वाहा में पातु सर्वतः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 37.18111)
- **Original**: दुर्गे दुर्ग रक्षिणीति स्वाहा नाभि सदावतु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 37.18112)
- **Original**: दुर्गे दुर्गें रक्ष रक्ष पृष्ठ मे पातु सर्वतः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 37.18113)
- **Original**: 30 हुं दुर्गायै स्वाहा च हस्तौ पादौं सदावतु । 3» ड्डीं दुर्गाय॑ स्वाहा च्॒ सर्वाजड्ठं मे सदाबतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 37.18114)
- **Original**: प्राच्यां पातु महामाया आग्रेय्यां पातु कालिका । दक्षिणे दक्षकन्या अ्॑व नैऋत्यां शिवसुन्दरी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 37.18115)
- **Original**: पश्चिमे पार्वती पातु बाराही वारुणे सदा । कुबेरमाता कौबेयामैशान्यामीशक्वी. सदा
- **Translation**: 

---

