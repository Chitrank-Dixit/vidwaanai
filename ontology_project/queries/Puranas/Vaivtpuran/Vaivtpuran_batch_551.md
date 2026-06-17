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

### Verse 1 (Vaivtpuran 38.18226)
- **Original**: क्षमस्त भगवत्यम्ब क्षमाशीले परात्परे । उपमे सर्वसाध्वीनां देवानां देवपूजिते । सर्वसम्पत्स्वरूपा त्व॑ सर्वेषां सर्वरूपिणी । कैलासे पार्वती त्वं च क्षीरोदे सिन्धुकन्यका । वैकुण्ठे च महालक्ष्मीदेंबदेवी सरस्वती । कृष्णप्राणाधिदेवी त्व॑ गोलोके राधिका स्वयम्‌ । कृष्णप्रिया त्वं भाण्डीरे चन्द्रा चन्दनकानने । पद्मावती पद्मतनने मालती मालतीवने । कदम्बमाला त्य॑ देवि कदम्बकाननेईपि चर । इत्युक्सा देवता: सर्वे मुनयो मनवस्तथा । इति लक्ष्मीस्तवं पुण्य॑ सर्बदेबै: कृत शुभम्‌ । अभार्यों लभते भायाँ विनीतां च॑ सुतां सतीम्‌ । पुत्रपौत्रवर्ती शुद्धां कुलजाँ कोमलां बराम्‌ । परमैश्चर्ययुक्ते च विद्यावन्त॑ यशस्विनम्‌ । शुद्धसत्त्वस्वरूपे त्वया बिना जगत्सर्व॑ मृततुल्यं चर निष्फलम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 38.18227)
- **Original**: रासेश्चवर्यश्रिदेवी त्व॑ त्वत्कलाः सर्वयोषित:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 38.18228)
- **Original**: स्वर्ग च स्वर्गलक्ष्मीस्त्व॑ मर्त्यलक्ष्मीक्ष भूतले
- **Translation**: 

---

### Verse 4 (Vaivtpuran 38.18229)
- **Original**: गड्ढा च तुलसी त्व॑ च्व॒ सावित्री ब्रह्मलोकतः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 38.18230)
- **Original**: रासे रासेश्वरी त्व॑ च वृन्दा वृन्दावने खने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 38.18231)
- **Original**: विरजा चम्पकवने शतश्रृट्धे त्र॒ सुन्दरी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 38.18232)
- **Original**: कुन्दन्ती कुन्दनने सुशीला केतकीवने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 38.18233)
- **Original**: राजलक्ष्मी राजगेहे गृहलक्ष्मीगृहे. गृहे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 38.18234)
- **Original**: रुरुदुर्नप्रवदना: शुष्ककण्ठौष्ठतालुका:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 38.18235)
- **Original**: यः पठेत्‌ प्रातरुत्थाय स वै सर्व लभेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 38.18236)
- **Original**: सुशीलां सुन्दी रष्यामतिसुप्रियवादिनीम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 38.18237)
- **Original**: अपुत्रो लभते पुत्र॑ वैष्णव॑ चिरजीविनम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 38.18238)
- **Original**: भ्रष्टराज्यो लभेद्‌ राज्य भ्रष्टश्रीलभते थ्रियम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 38.18239)
- **Original**: हतबन्धुर्लभेद्‌ बन्धु धनप्रष्टो धर्न लभेत्‌ । कीर्तिहीनो लभेत्‌ कीति प्रतिष्ठां च लभेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 38.18240)
- **Original**: सर्वमड्ुलर्द॑ स्तोत्र शोकसंतापनाशनम्‌ । हर्षानन्दकरे शश्रद्धर्ममोक्षसुदृत्प्रदम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 38.18241)
- **Original**: इति श्रीब्रह्मवैवरतें देवकृत॑ लक्ष्यीस्तोजं सम्पूर्णय्‌। ( श्रीकृष्णजन्मखण्ड 56 । 75-90) ++*-स्फकपड >>
- **Translation**: 

---

### Verse 17 (Vaivtpuran 38.18272)
- **Original**: दण्ड + संक्षिप्त ब्रह्म॑लैवर्तपुराण « कऋकऋऋ% कक कक 49444 45459 59449 954 ###%#%##### 66 ########ऋऋक 37% श्रीं नारायणेशायै॑ मम कण्ठं सदावतु । 30 श्रीं केशवकान्तायै मम स्कन्ध॑ सदावतु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 38.18273)
- **Original**: 39 श्रीं पद्मनिवासिन्ये स्वाहा नाभिं सदावतु । 3» ड्डीं श्रीं संसारमात्रे मम वक्ष: सदावतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 38.18274)
- **Original**: 3» श्रीं श्रीं कृष्णकान्तायै स्वाहा पृष्ठ सदावतु । 30 हीं श्रीं श्रिये स्वाहा मम हस्तौ सदावतु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 38.18275)
- **Original**: 3 श्रीं निवासकान्ताय॑ मम पादौ सदायतु
- **Translation**: 

---

